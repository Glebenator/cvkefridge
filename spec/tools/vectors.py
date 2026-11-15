#!/usr/bin/env python3
"""The reference model of the core rules in spec/rules.md.

It calculates the expected values of the test vectors in spec/vectors/ from their inputs.

    python spec/tools/vectors.py           Check that each "expect" value in the vector files is correct.
    python spec/tools/vectors.py --write   Write the "expect" values. Use it after you add an input.

It uses the Python standard library only. It is not app code. The apps do not run it.
"""
import datetime
import json
import sys
from pathlib import Path

SPEC = Path(__file__).resolve().parent.parent
VECTORS = SPEC / "vectors"

CATEGORIES = ["produce", "dairy", "meat", "condiment", "beverage", "bakery", "leftovers", "other"]
UNITS = ["pcs", "g", "kg", "ml", "l", "pack", "bottle", "slice", "cup"]
STORAGE_KINDS = ["pantry", "fridge", "freezer"]
EXPIRY_SOURCES = ["printed", "estimated", "chosen"]
ID_CHARACTERS = set("abcdefghijklmnopqrstuvwxyz0123456789-")
EPOCH = datetime.date(1970, 1, 1)


# ---- 2. Calendar dates

def parse_date(text):
    """The date of a text in the form YYYY-MM-DD, or None."""
    if not isinstance(text, str) or len(text) != 10 or text[4] != "-" or text[7] != "-":
        return None
    digits = text[0:4] + text[5:7] + text[8:10]
    if any(c not in "0123456789" for c in digits):
        return None
    try:
        return datetime.date(int(text[0:4]), int(text[5:7]), int(text[8:10]))
    except ValueError:
        return None


def format_date(date):
    return None if date is None else "%04d-%02d-%02d" % (date.year, date.month, date.day)


def plus_days(date, days):
    try:
        return date + datetime.timedelta(days=days)
    except OverflowError:
        return None


def date_of_instant(epoch_millis, utc_offset_seconds):
    return EPOCH + datetime.timedelta(days=(epoch_millis + utc_offset_seconds * 1000) // 86_400_000)


# ---- 3. Freshness

def days_left(today, expiry_date):
    return None if expiry_date is None else (expiry_date - today).days


def freshness(left):
    if left is None:
        return "noExpiryDate"
    if left < 0:
        return "expired"
    return "expiring" if left <= 2 else "fresh"


# ---- 4. Expiry estimate

def estimate(foods, food_id, storage_kind, date_added):
    for food in foods:
        if food["id"] == food_id:
            days = food["days"].get(storage_kind)
            return None if days is None else plus_days(date_added, days)
    return None


# ---- 5. and 6. Use-first order and the plan of a use

def use_first(batches):
    active = [b for b in batches if b["quantity"] > 0]
    return sorted(active, key=lambda b: (
        0 if b["expiryDate"] else 1,
        b["expiryDate"] or "",  # The text form of a date sorts in date order.
        b["dateAdded"],
        b["id"],
    ))


def plan_use(batches, product_id, quantity):
    takes = []
    left = max(quantity, 0)
    for batch in use_first([b for b in batches if b["productId"] == product_id]):
        if left == 0:
            break
        taken = min(left, batch["quantity"])
        takes.append({"batchId": batch["id"], "quantity": taken})
        left -= taken
    return {"takes": takes, "shortfall": left}


# ---- 7. The change log

FIXED_AREAS = {
    "fridge": {"id": "fridge", "name": "Fridge", "kind": "fridge", "fixed": True},
    "freezer": {"id": "freezer", "name": "Freezer", "kind": "freezer", "fixed": True},
}


def replay(changes):
    ordered = []
    seen = set()
    for change in sorted(changes, key=lambda c: (c["at"], c["id"])):
        if change["id"] not in seen:
            seen.add(change["id"])
            ordered.append(change)
    by_id = {c["id"]: c for c in ordered}

    undone = set()
    undo_rejections = {}
    for change in ordered:
        body = change["body"]
        if body["type"] != "changeUndone":
            continue
        target = by_id.get(body["changeId"])
        if target is None:
            undo_rejections[change["id"]] = "unknownChange"
        elif target["body"]["type"] == "changeUndone":
            undo_rejections[change["id"]] = "cannotUndo"
        else:
            undone.add(target["id"])

    products, batches, history, rejected = {}, {}, [], []
    areas = {key: dict(value) for key, value in FIXED_AREAS.items()}

    def apply(change):
        """Applies one change. Returns the reason if the change cannot apply."""
        nonlocal history
        body = change["body"]
        kind = body["type"]
        if kind == "productSaved":
            product = dict(body["product"])
            product.setdefault("note", None)
            product.setdefault("storageText", None)
            products[product["id"]] = product
        elif kind == "productDeleted":
            if body["productId"] not in products:
                return "unknownProduct"
            del products[body["productId"]]
            for batch_id in [b["id"] for b in batches.values() if b["productId"] == body["productId"]]:
                del batches[batch_id]
            history = [h for h in history if h["productId"] != body["productId"]]
        elif kind == "storageAreaSaved":
            area = body["area"]
            if area["id"] in FIXED_AREAS:
                return "fixedStorageArea"
            areas[area["id"]] = {"id": area["id"], "name": area["name"], "kind": area["kind"], "fixed": False}
        elif kind == "storageAreaDeleted":
            area_id = body["storageAreaId"]
            if area_id in FIXED_AREAS:
                return "fixedStorageArea"
            if area_id not in areas:
                return "unknownStorageArea"
            if any(b["storageAreaId"] == area_id and b["quantity"] > 0 for b in batches.values()):
                return "storageAreaInUse"
            del areas[area_id]
        elif kind == "batchAdded":
            batch = body["batch"]
            if batch["id"] in batches:
                return "duplicateBatch"
            if batch["productId"] not in products:
                return "unknownProduct"
            if batch["storageAreaId"] not in areas:
                return "unknownStorageArea"
            if batch["quantity"] <= 0:
                return "invalidQuantity"
            batches[batch["id"]] = dict(batch)
        elif kind == "batchEdited":
            batch = batches.get(body["batchId"])
            if batch is None:
                return "unknownBatch"
            if body["storageAreaId"] not in areas:
                return "unknownStorageArea"
            if body["quantity"] <= 0:
                return "invalidQuantity"
            for field in ("quantity", "storageAreaId", "dateAdded", "expiryDate", "expirySource"):
                batch[field] = body[field]
        elif kind in ("batchUsed", "batchThrownAway"):
            batch = batches.get(body["batchId"])
            if batch is None:
                return "unknownBatch"
            if body["quantity"] <= 0:
                return "invalidQuantity"
            if batch["quantity"] == 0:
                return "batchEnded"
            taken = min(body["quantity"], batch["quantity"])
            batch["quantity"] -= taken
            history.append({
                "changeId": change["id"],
                "batchId": batch["id"],
                "productId": batch["productId"],
                "quantity": taken,
                "outcome": "used" if kind == "batchUsed" else "thrownAway",
                "date": body["date"],
            })
        elif kind == "batchDeleted":
            if body["batchId"] not in batches:
                return "unknownBatch"
            del batches[body["batchId"]]
            history = [h for h in history if h["batchId"] != body["batchId"]]
        elif kind == "changeUndone":
            return undo_rejections.get(change["id"])
        else:
            raise ValueError("Unknown change type: %s" % kind)
        return None

    for change in ordered:
        if change["id"] in undone:
            continue
        reason = apply(change)
        if reason is not None:
            rejected.append({"changeId": change["id"], "reason": reason})

    return {
        "products": [products[key] for key in sorted(products)],
        "storageAreas": [areas[key] for key in sorted(areas)],
        "batches": [batches[key] for key in sorted(batches)],
        "history": history,
        "rejected": rejected,
    }


# ---- Input checks. They find a mistake in a vector file before an app does.

def check_id(value, where):
    if not isinstance(value, str) or not 1 <= len(value) <= 64 or set(value) - ID_CHARACTERS:
        raise ValueError("%s: %r is not an identifier" % (where, value))


def check_batch(batch, where):
    for field in ("id", "productId", "storageAreaId"):
        check_id(batch[field], where)
    if not isinstance(batch["quantity"], int):
        raise ValueError("%s: the quantity is not a whole number" % where)
    if parse_date(batch["dateAdded"]) is None:
        raise ValueError("%s: dateAdded is not a date" % where)
    check_expiry(batch, where)


def check_expiry(record, where):
    date, source = record["expiryDate"], record["expirySource"]
    if (date is None) != (source is None):
        raise ValueError("%s: expiryDate and expirySource must both have a value, or both be null" % where)
    if date is not None and (parse_date(date) is None or source not in EXPIRY_SOURCES):
        raise ValueError("%s: bad expiry date or source" % where)


def check_change(change, where):
    check_id(change["id"], where)
    check_id(change["origin"], where)
    if not isinstance(change["at"], int):
        raise ValueError("%s: 'at' is not a whole number" % where)
    body = change["body"]
    kind = body["type"]
    if kind == "productSaved":
        product = body["product"]
        check_id(product["id"], where)
        if product["category"] not in CATEGORIES or product["unit"] not in UNITS + [None]:
            raise ValueError("%s: bad category or unit" % where)
        if not isinstance(product["name"], str):
            raise ValueError("%s: the name is not text" % where)
        for field in ("barcode", "foodId", "note", "storageText"):
            if product.get(field) is not None and not isinstance(product[field], str):
                raise ValueError("%s: %s is not text" % (where, field))
    elif kind == "storageAreaSaved":
        check_id(body["area"]["id"], where)
        if body["area"]["kind"] not in STORAGE_KINDS:
            raise ValueError("%s: bad storage kind" % where)
    elif kind == "batchAdded":
        check_batch(body["batch"], where)
    elif kind == "batchEdited":
        check_id(body["batchId"], where)
        check_id(body["storageAreaId"], where)
        check_expiry(body, where)
    elif kind in ("batchUsed", "batchThrownAway"):
        check_id(body["batchId"], where)
        if parse_date(body["date"]) is None:
            raise ValueError("%s: bad date" % where)
    elif kind in ("productDeleted", "storageAreaDeleted", "batchDeleted", "changeUndone"):
        check_id(body[{"productDeleted": "productId", "storageAreaDeleted": "storageAreaId",
                       "batchDeleted": "batchId", "changeUndone": "changeId"}[kind]], where)
    else:
        raise ValueError("%s: unknown change type %r" % (where, kind))


def check_foods(table, where):
    ids = set()
    for food in table["foods"]:
        check_id(food["id"], where)
        if food["id"] in ids:
            raise ValueError("%s: the food %s is in the table two times" % (where, food["id"]))
        ids.add(food["id"])
        if not food["name"] or food["name"] != food["name"].strip():
            raise ValueError("%s: bad name for %s" % (where, food["id"]))
        if food["category"] not in CATEGORIES:
            raise ValueError("%s: bad category for %s" % (where, food["id"]))
        for kind, days in food["days"].items():
            if kind not in STORAGE_KINDS or not isinstance(days, int) or days < 1:
                raise ValueError("%s: bad days for %s" % (where, food["id"]))
        if food.get("usualKind", "fridge") not in STORAGE_KINDS:
            raise ValueError("%s: bad usual storage kind for %s" % (where, food["id"]))
        if food.get("common", True) is not True:
            raise ValueError("%s: common must be true or absent for %s" % (where, food["id"]))
        tips = food.get("tips", {"fridge": "a"})
        if not tips or any(kind not in STORAGE_KINDS or not isinstance(tip, str) or not tip or tip != " ".join(tip.split())
                           for kind, tip in tips.items()):
            raise ValueError("%s: bad tips for %s" % (where, food["id"]))
        aliases = food.get("aliases", ["a"])
        if not aliases or any(not isinstance(a, str) or not a or a != a.strip().lower() for a in aliases):
            raise ValueError("%s: bad aliases for %s" % (where, food["id"]))


# ---- 8. The storage hint of a looked-up product

SPACES = "   "
DIGITS = "0123456789"
MINUS_SIGNS = "-−–"
DEGREE = "°"
FROZEN_MAX = -6
FRIDGE_MAX = 10
HINT_KINDS = ["freezer", "fridge", "pantry"]


def skip_spaces_back(text, end):
    """The position after the last character before `end` that is not a space."""
    while end > 0 and text[end - 1] in SPACES:
        end -= 1
    return end


def digits_back(text, end):
    """The start of the digits that end at `end`."""
    start = end
    while start > 0 and text[start - 1] in DIGITS:
        start -= 1
    return start


def temperatures(text):
    """The Celsius temperatures of a lowercase text, in the order of their degree signs (rule 8.1)."""
    found = []
    for at, char in enumerate(text):
        if char != DEGREE:
            continue
        after = at + 1
        while after < len(text) and text[after] in SPACES:
            after += 1
        if after < len(text) and text[after] == "f" and not (after + 1 < len(text) and "a" <= text[after + 1] <= "z"):
            continue
        end = skip_spaces_back(text, at)
        start = digits_back(text, end)
        if start == end:
            continue
        if start >= 2 and text[start - 1] in ".," and text[start - 2] in DIGITS:
            end = start - 1
            start = digits_back(text, end)
        if end - start > 3:
            continue
        value = int(text[start:end])
        sign = skip_spaces_back(text, start)
        if sign > 0 and text[sign - 1] in MINUS_SIGNS:
            before = skip_spaces_back(text, sign - 1)
            previous = text[before - 1] if before > 0 else None
            of_range = previous is not None and (
                previous in DIGITS or previous == DEGREE
                or (previous == "c" and skip_spaces_back(text, before - 1) > 0
                    and text[skip_spaces_back(text, before - 1) - 1] == DEGREE))
            if not of_range:
                value = -value
        found.append(value)
    return found


def kind_of_storage_text(hints, text):
    """The storage kind of a storage text, or None (rule 8.2)."""
    text = text.lower()
    starts = [position for position in (text.find(phrase) for phrase in hints["afterOpening"]) if position >= 0]
    found = temperatures(text[:min(starts)] if starts else text)
    frozen = [value for value in found if value <= FROZEN_MAX]
    if not found or (frozen and len(frozen) != len(found)):
        return None
    if frozen:
        return "freezer"
    return "fridge" if max(found) <= FRIDGE_MAX else "pantry"


def kind_of_tags(hints, tags):
    """The storage kind of the category tags, or None (rule 8.3)."""
    return next((kind for kind in HINT_KINDS if any(tag in hints["tags"].get(kind, []) for tag in tags)), None)


def storage_hint(hints, storage_text, tags):
    """The storage hint as it is in the vectors (rule 8.4)."""
    kind = None if storage_text is None else kind_of_storage_text(hints, storage_text)
    if kind is not None:
        return {"kind": kind, "source": "storageText"}
    kind = kind_of_tags(hints, tags)
    return {"kind": kind, "source": None if kind is None else "tags"}


def check_hints(hints, where):
    phrases = hints["afterOpening"]
    if any(not isinstance(p, str) or not p or p != p.strip().lower() for p in phrases) or len(set(phrases)) != len(phrases):
        raise ValueError("%s: an afterOpening phrase is empty, not in lowercase, or two times in the list" % where)
    if any(kind not in STORAGE_KINDS for kind in hints["tags"]):
        raise ValueError("%s: a key of tags is not a storage kind" % where)
    seen = set()
    for kind, tags in hints["tags"].items():
        for tag in tags:
            if not isinstance(tag, str) or not tag or tag != tag.strip().lower() or tag in seen:
                raise ValueError("%s: bad tag %r for %s, or the tag is two times in the table" % (where, tag, kind))
            seen.add(tag)


# ---- The expected values of each vector file

def expect_calendar_date(data):
    for case in data["parse"]:
        date = parse_date(case["text"])
        yield case, ({"valid": False} if date is None else
                     {"valid": True, "year": date.year, "month": date.month, "day": date.day})
    for case in data["plusDays"]:
        yield case, {"date": format_date(plus_days(parse_date(case["date"]), case["days"]))}
    for case in data["daysUntil"]:
        yield case, {"days": (parse_date(case["to"]) - parse_date(case["from"])).days}
    for case in data["order"]:
        dates = sorted(parse_date(text) for text in case["dates"])
        yield case, {"sorted": [format_date(date) for date in dates]}
    for case in data["dateOfInstant"]:
        yield case, {"date": format_date(date_of_instant(case["epochMillis"], case["utcOffsetSeconds"]))}


def expect_freshness(data):
    for case in data["cases"]:
        expiry = None if case["expiryDate"] is None else parse_date(case["expiryDate"])
        left = days_left(parse_date(case["today"]), expiry)
        yield case, {"daysLeft": left, "freshness": freshness(left)}


def expect_expiry_estimate(data):
    check_foods(data, "expiry-estimate.json")
    for case in data["cases"]:
        date = estimate(data["foods"], case["foodId"], case["storageKind"], parse_date(case["dateAdded"]))
        yield case, {"expiryDate": format_date(date), "expirySource": None if date is None else "estimated"}


def expect_use_first(data):
    for case in data["cases"]:
        for batch in case["batches"]:
            check_batch(batch, "use-first.json " + case["name"])
        yield case, {"order": [batch["id"] for batch in use_first(case["batches"])]}


def expect_plan_use(data):
    for case in data["cases"]:
        for batch in case["batches"]:
            check_batch(batch, "plan-use.json " + case["name"])
        yield case, plan_use(case["batches"], case["productId"], case["quantity"])


def expect_change_log(data):
    for case in data["cases"]:
        for change in case["changes"]:
            check_change(change, "change-log.json " + case["name"])
        yield case, replay(case["changes"])


# Foods with tips that are always in the samples of food-table.json: bananas, tomatoes, and frozen pizza.
TIP_SAMPLES = {"fk-251", "fk-306", "fk-571"}


def expect_food_table(data):
    """Facts about spec/foods.json. They prove that an app reads the whole table."""
    table = json.loads((SPEC / "foods.json").read_text(encoding="utf-8"))
    check_foods(table, "foods.json")
    foods = table["foods"]
    step = max(1, len(foods) // 12)
    sampled = foods[::step] + [food for food in foods if food["id"] in TIP_SAMPLES and food not in foods[::step]]
    samples = [{"foodId": food["id"], "name": food["name"], "category": food["category"], "days": food["days"],
                "usualKind": food.get("usualKind"), "common": food.get("common", False),
                "aliases": food.get("aliases", []), "tips": food.get("tips", {})}
               for food in sampled]
    with_days = {kind: sum(1 for food in foods if kind in food["days"]) for kind in STORAGE_KINDS}
    usual = {kind: sum(1 for food in foods if food.get("usualKind") == kind) for kind in STORAGE_KINDS}
    common = sum(1 for food in foods if food.get("common"))
    aliases = sum(len(food.get("aliases", [])) for food in foods)
    with_tips = {kind: sum(1 for food in foods if kind in food.get("tips", {})) for kind in STORAGE_KINDS}
    yield data, {"count": len(foods), "withDays": with_days, "withUsualKind": usual, "common": common,
                 "aliases": aliases, "withTips": with_tips, "samples": samples}


def expect_storage_hint(data):
    check_hints(data["hints"], "storage-hint.json")
    for case in data["temperatures"]:
        yield case, {"celsius": temperatures(case["text"].lower())}
    for case in data["cases"]:
        yield case, storage_hint(data["hints"], case["storageText"], case["tags"])


def expect_storage_hints_table(data):
    """Facts about spec/storage-hints.json, and the hints of real products. They prove that an app reads the table."""
    hints = json.loads((SPEC / "storage-hints.json").read_text(encoding="utf-8"))
    check_hints(hints, "storage-hints.json")
    for case in data["facts"]:
        yield case, {"afterOpening": len(hints["afterOpening"]),
                     "tags": {kind: len(hints["tags"].get(kind, [])) for kind in STORAGE_KINDS}}
    for case in data["cases"]:
        yield case, storage_hint(hints, case["storageText"], case["tags"])


FILES = {
    "calendar-date.json": expect_calendar_date,
    "freshness.json": expect_freshness,
    "expiry-estimate.json": expect_expiry_estimate,
    "use-first.json": expect_use_first,
    "plan-use.json": expect_plan_use,
    "change-log.json": expect_change_log,
    "food-table.json": expect_food_table,
    "storage-hint.json": expect_storage_hint,
    "storage-hints-table.json": expect_storage_hints_table,
}


def main():
    write = "--write" in sys.argv[1:]
    failures = 0
    cases = 0
    names = {path.name for path in VECTORS.glob("*.json")}
    for name in sorted(names ^ set(FILES)):
        print("%s: the file and the list in vectors.py do not agree" % name)
        failures += 1
    for name, expect in FILES.items():
        path = VECTORS / name
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for case, expected in expect(data):
            cases += 1
            if write:
                case["expect"] = expected
            elif case.get("expect") != expected:
                failures += 1
                print("%s: %s\n  in the file: %s\n  calculated:  %s" % (
                    name, case.get("name", {k: v for k, v in case.items() if k != "expect"}),
                    json.dumps(case.get("expect")), json.dumps(expected)))
        if write:
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print("%d cases, %d failures%s" % (cases, failures, ", files written" if write else ""))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

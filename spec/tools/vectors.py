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

CATEGORIES = ["produce", "dairy", "meat", "condiment", "beverage", "bakery", "leftovers", "other",
              "grains", "canned", "baking", "snacks", "meals"]
UNITS = ["pcs", "g", "kg", "ml", "l", "pack", "bottle", "slice", "cup"]
STORAGE_KINDS = ["pantry", "fridge", "freezer"]
EXPIRY_SOURCES = ["printed", "estimated", "chosen"]
DATE_TYPES = ["useBy", "bestBefore"]
AFTER_DATE_CLASSES = ["strict", "check"]
# The categories that give the after-date class `check` to a product with no food of the table (rule 9.1).
CHECK_CATEGORIES = ["condiment", "beverage", "bakery", "grains", "canned", "baking", "snacks"]
TIP_KINDS = ["freeze", "cook", "useUp"]
# The days that a batch stays good after it is thawed, for each food (rule 5.2).
THAWED_DAYS = 1
# The days in the freezer for a frozen batch of a food with no days for the freezer (rule 5.2).
DEFAULT_FREEZER_DAYS = 30
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


# ---- 5. and 6. The good-until date, the use-first order, and the plan of a use

def food_of(foods, food_id):
    return next((food for food in foods if food["id"] == food_id), None)


def opened_days(foods, food_id, storage_kind):
    """The opened days of a food for a storage kind, or None (rule 4)."""
    food = food_of(foods, food_id)
    return None if food is None else food.get("openedDays", {}).get(storage_kind)


def freezer_days(foods, food_id):
    """The days of a food for the freezer, or None (rule 4)."""
    food = food_of(foods, food_id)
    return None if food is None else food["days"].get("freezer")


def good_until(batch, days_opened, days_freezer):
    """The good-until date of a batch and its source (rule 5.2). `days_opened` is the opened days of the food of the
    batch for the storage kind of its storage area, or None. `days_freezer` is the days of that food for the freezer,
    or None. With None, a frozen batch has the default freezer days."""
    if batch.get("thawedDate") is not None:
        date = plus_days(parse_date(batch["thawedDate"]), THAWED_DAYS)
        return {"date": format_date(date), "source": None if date is None else "thawed"}
    if batch.get("frozenDate") is not None:
        days = DEFAULT_FREEZER_DAYS if days_freezer is None else days_freezer
        date = plus_days(parse_date(batch["frozenDate"]), days)
        return {"date": format_date(date), "source": None if date is None else "frozen"}
    expiry = None if batch["expiryDate"] is None else parse_date(batch["expiryDate"])
    opened = None if batch.get("openedDate") is None else parse_date(batch["openedDate"])
    after_opening = None if opened is None or days_opened is None else plus_days(opened, days_opened)
    if after_opening is not None and (expiry is None or after_opening < expiry):
        return {"date": format_date(after_opening), "source": "opened"}
    return {"date": batch["expiryDate"], "source": batch["expirySource"]}


def good_until_in(foods, products, areas, batch):
    """The good-until date of a batch of an inventory. A batch with no product, no food, or no storage area in the
    lists has no opened days. A batch with no product or no food in the lists has no days for the freezer."""
    product = next((p for p in products if p["id"] == batch["productId"]), None)
    area = next((a for a in areas if a["id"] == batch["storageAreaId"]), None)
    days = None if product is None or area is None else opened_days(foods, product.get("foodId"), area["kind"])
    return good_until(batch, days, None if product is None else freezer_days(foods, product.get("foodId")))


def good_until_of(foods, product, batch, storage_kind):
    """The good-until date of a batch of a product, in a storage area of a storage kind."""
    food_id = product.get("foodId")
    return good_until(batch, opened_days(foods, food_id, storage_kind), freezer_days(foods, food_id))


def freshness_of(until, today):
    """The freshness that a good-until date gives for today (rule 3)."""
    return freshness(days_left(today, None if until["date"] is None else parse_date(until["date"])))


def use_first(batches, date_of=lambda batch: batch["expiryDate"]):
    """The active batches in the use-first order (rule 5.3). `date_of` gives the good-until date of a batch as text.
    For a batch with no opened date, that is its expiry date."""
    active = [b for b in batches if b["quantity"] > 0]
    return sorted(active, key=lambda b: (
        0 if date_of(b) else 1,
        date_of(b) or "",  # The text form of a date sorts in date order.
        b["dateAdded"],
        b["id"],
    ))


def plan_use(batches, product_id, quantity, date_of=lambda batch: batch["expiryDate"]):
    takes = []
    left = max(quantity, 0)
    for batch in use_first([b for b in batches if b["productId"] == product_id], date_of):
        if left == 0:
            break
        taken = min(left, batch["quantity"])
        takes.append({"batchId": batch["id"], "quantity": taken})
        left -= taken
    return {"takes": takes, "shortfall": left}


# ---- 9. The later-date offer

def after_date_class(foods, product):
    """The after-date class of a product (rule 9.1)."""
    food = food_of(foods, product.get("foodId"))
    if food is not None:
        return food.get("afterDate", "strict")
    return "check" if product["category"] in CHECK_CATEGORIES else "strict"


def later_date_offer(foods, product, batch, storage_kind, today):
    """If the app can offer a later date for a batch, and the reason when it cannot (rule 9.2)."""
    until = good_until_of(foods, product, batch, storage_kind)
    state = freshness_of(until, today)
    if state not in ("expiring", "expired"):
        reason = "notDue"
    elif until["source"] == "printed" and batch.get("dateType") == "useBy":
        reason = "useByDate"
    elif after_date_class(foods, product) == "strict":
        reason = "strictFood"
    elif until["source"] in ("opened", "frozen", "thawed"):
        reason = until["source"]
    else:
        reason = None
    return {"offer": reason is None, "reason": reason}


# ---- 11. The freeze check

def freeze_check(foods, product, batch, storage_kind, today):
    """If the app can move a batch to a freezer, and the reason when it cannot (rule 11)."""
    if storage_kind == "freezer":
        reason = "inFreezer"
    elif batch.get("thawedDate") is not None:
        reason = "thawed"
    elif freshness_of(good_until_of(foods, product, batch, storage_kind), today) == "expired":
        reason = "afterDate"
    else:
        reason = None
    return {"permitted": reason is None, "reason": reason}


# ---- 10. The before-date tips

def before_date_tips(table, foods, product, batch, storage_kind, today):
    """The identifiers of the before-date tips that a batch shows, in the order of the table (rule 10)."""
    food = food_of(foods, product.get("foodId"))
    if food is None:
        return []
    if freshness_of(good_until_of(foods, product, batch, storage_kind), today) != "expiring":
        return []
    can_freeze = "freezer" in food["days"] and freeze_check(foods, product, batch, storage_kind, today)["permitted"]
    shown = []
    for tip in table["tips"]:
        if food["id"] not in tip["foods"]:
            continue
        if tip["kind"] == "freeze" and not can_freeze:
            continue
        shown.append(tip["id"])
    return shown


def check_tips(table, where, foods=None, freezer_days=False):
    """Finds a mistake in a table of before-date tips. With `foods`, each food of a tip must be in that table. With
    `freezer_days`, each food of a freeze tip must have days for the freezer: the tip is not shown without them."""
    for key, source in table["sources"].items():
        check_id(key, where)
        if any(not isinstance(source.get(field), str) or not source[field] for field in ("name", "url", "licence")):
            raise ValueError("%s: the source %s must have a name, a url, and a licence" % (where, key))
        if not source["url"].startswith("https://"):
            raise ValueError("%s: the url of the source %s does not start with https://" % (where, key))
    ids = set()
    by_id = None if foods is None else {food["id"]: food for food in foods}
    for tip in table["tips"]:
        check_id(tip["id"], where)
        if tip["id"] in ids:
            raise ValueError("%s: the tip %s is in the table two times" % (where, tip["id"]))
        ids.add(tip["id"])
        if tip["kind"] not in TIP_KINDS or tip["source"] not in table["sources"]:
            raise ValueError("%s: bad kind or source for the tip %s" % (where, tip["id"]))
        if not isinstance(tip["text"], str) or not tip["text"] or tip["text"] != " ".join(tip["text"].split()):
            raise ValueError("%s: bad text for the tip %s" % (where, tip["id"]))
        if not tip["foods"] or len(set(tip["foods"])) != len(tip["foods"]):
            raise ValueError("%s: the tip %s has no food, or a food two times" % (where, tip["id"]))
        for food_id in tip["foods"]:
            check_id(food_id, where)
            if by_id is not None and food_id not in by_id:
                raise ValueError("%s: the food %s of the tip %s is not in the table of foods"
                                 % (where, food_id, tip["id"]))
            if freezer_days and tip["kind"] == "freeze" and "freezer" not in by_id[food_id]["days"]:
                raise ValueError("%s: the food %s of the freeze tip %s has no days for the freezer"
                                 % (where, food_id, tip["id"]))


# ---- 7. The change log

# The values of a batch that a change from before them does not have. A missing key is no value.
OPTIONAL_BATCH_FIELDS = ("dateType", "openedDate", "frozenDate", "thawedDate")

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
            batch = dict(batch)
            for field in OPTIONAL_BATCH_FIELDS:
                batch.setdefault(field, None)
            batches[batch["id"]] = batch
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
            for field in OPTIONAL_BATCH_FIELDS:
                batch[field] = body.get(field)
        elif kind == "batchOpened":
            batch = batches.get(body["batchId"])
            if batch is None:
                return "unknownBatch"
            if batch["quantity"] == 0:
                return "batchEnded"
            batch["openedDate"] = body["date"]
        elif kind in ("batchFrozen", "batchThawed"):
            batch = batches.get(body["batchId"])
            if batch is None:
                return "unknownBatch"
            if batch["quantity"] == 0:
                return "batchEnded"
            if body["storageAreaId"] not in areas:
                return "unknownStorageArea"
            batch["storageAreaId"] = body["storageAreaId"]
            if kind == "batchFrozen":
                batch["frozenDate"] = body["date"]
                batch["thawedDate"] = None
            else:
                batch["thawedDate"] = body["date"]
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
    date_type = record.get("dateType")
    if date_type is not None and (date_type not in DATE_TYPES or source != "printed"):
        raise ValueError("%s: bad date type, or a date type for a date that is not printed" % where)
    for field in ("openedDate", "frozenDate", "thawedDate"):
        if record.get(field) is not None and parse_date(record[field]) is None:
            raise ValueError("%s: %s is not a date" % (where, field))


def check_product(product, where):
    check_id(product["id"], where)
    if product["category"] not in CATEGORIES or product["unit"] not in UNITS + [None]:
        raise ValueError("%s: bad category or unit" % where)
    if not isinstance(product["name"], str):
        raise ValueError("%s: the name is not text" % where)
    for field in ("barcode", "foodId", "note", "storageText"):
        if product.get(field) is not None and not isinstance(product[field], str):
            raise ValueError("%s: %s is not text" % (where, field))


def check_change(change, where):
    check_id(change["id"], where)
    check_id(change["origin"], where)
    if not isinstance(change["at"], int):
        raise ValueError("%s: 'at' is not a whole number" % where)
    body = change["body"]
    kind = body["type"]
    if kind == "productSaved":
        check_product(body["product"], where)
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
    elif kind in ("batchUsed", "batchThrownAway", "batchOpened", "batchFrozen", "batchThawed"):
        check_id(body["batchId"], where)
        if kind in ("batchFrozen", "batchThawed"):
            check_id(body["storageAreaId"], where)
        if parse_date(body["date"]) is None:
            raise ValueError("%s: bad date" % where)
    elif kind in ("productDeleted", "storageAreaDeleted", "batchDeleted", "changeUndone"):
        check_id(body[{"productDeleted": "productId", "storageAreaDeleted": "storageAreaId",
                       "batchDeleted": "batchId", "changeUndone": "changeId"}[kind]], where)
    else:
        raise ValueError("%s: unknown change type %r" % (where, kind))


def check_foods(table, where, with_class=False):
    """Finds a mistake in a table of foods. With `with_class`, each food must have an after-date class."""
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
        opened = food.get("openedDays", {"fridge": 1})
        if not opened or any(kind not in STORAGE_KINDS or not isinstance(days, int) or days < 1
                             for kind, days in opened.items()):
            raise ValueError("%s: bad opened days for %s" % (where, food["id"]))
        if food.get("afterDate", None if with_class else "strict") not in AFTER_DATE_CLASSES:
            raise ValueError("%s: bad or no after-date class for %s" % (where, food["id"]))
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


# Foods that are always in the samples of food-table.json. With tips: bananas, tomatoes, and frozen pizza. With
# opened days: hard cheese, hot dogs, ketchup, and peanut butter.
TIP_SAMPLES = {"fk-251", "fk-306", "fk-571", "fk-3", "fk-98", "fk-348", "fk-387"}


def expect_food_table(data):
    """Facts about spec/foods.json. They prove that an app reads the whole table."""
    table = json.loads((SPEC / "foods.json").read_text(encoding="utf-8"))
    check_foods(table, "foods.json", with_class=True)
    foods = table["foods"]
    step = max(1, len(foods) // 12)
    sampled = foods[::step] + [food for food in foods if food["id"] in TIP_SAMPLES and food not in foods[::step]]
    samples = [{"foodId": food["id"], "name": food["name"], "category": food["category"], "days": food["days"],
                "usualKind": food.get("usualKind"), "common": food.get("common", False),
                "aliases": food.get("aliases", []), "tips": food.get("tips", {}),
                "openedDays": food.get("openedDays", {}), "afterDate": food["afterDate"]}
               for food in sampled]
    with_days = {kind: sum(1 for food in foods if kind in food["days"]) for kind in STORAGE_KINDS}
    usual = {kind: sum(1 for food in foods if food.get("usualKind") == kind) for kind in STORAGE_KINDS}
    common = sum(1 for food in foods if food.get("common"))
    aliases = sum(len(food.get("aliases", [])) for food in foods)
    with_tips = {kind: sum(1 for food in foods if kind in food.get("tips", {})) for kind in STORAGE_KINDS}
    with_opened = {kind: sum(1 for food in foods if kind in food.get("openedDays", {})) for kind in STORAGE_KINDS}
    classes = {name: sum(1 for food in foods if food["afterDate"] == name) for name in AFTER_DATE_CLASSES}
    categories = {name: sum(1 for food in foods if food["category"] == name) for name in CATEGORIES}
    yield data, {"count": len(foods), "withDays": with_days, "withUsualKind": usual, "common": common,
                 "aliases": aliases, "withTips": with_tips, "withOpenedDays": with_opened, "afterDate": classes,
                 "category": categories, "samples": samples}


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


def check_case(case, where):
    """Checks the product and the batch of a case of rules 5.2, 9, 10, and 11."""
    check_product(case["product"], where)
    check_batch(case["batch"], where)
    if case["storageKind"] not in STORAGE_KINDS or parse_date(case["today"]) is None:
        raise ValueError("%s: bad storage kind or bad date for today" % where)


def expect_good_until(data):
    check_foods(data, "good-until.json")
    foods = data["foods"]
    for case in data["cases"]:
        check_case(case, "good-until.json " + case["name"])
        until = good_until_of(foods, case["product"], case["batch"], case["storageKind"])
        left = days_left(parse_date(case["today"]), None if until["date"] is None else parse_date(until["date"]))
        yield case, {"date": until["date"], "source": until["source"], "daysLeft": left, "freshness": freshness(left)}
    for section in ("order", "plan"):
        for case in data[section]:
            where = "good-until.json " + case["name"]
            for product in case["products"]:
                check_product(product, where)
            for area in case["storageAreas"]:
                check_id(area["id"], where)
                if area["kind"] not in STORAGE_KINDS:
                    raise ValueError("%s: bad storage kind" % where)
            for batch in case["batches"]:
                check_batch(batch, where)

            def date_of(batch, case=case):
                return good_until_in(foods, case["products"], case["storageAreas"], batch)["date"]
            if section == "order":
                yield case, {"order": [batch["id"] for batch in use_first(case["batches"], date_of)]}
            else:
                yield case, plan_use(case["batches"], case["productId"], case["quantity"], date_of)


def expect_later_date_offer(data):
    check_foods(data, "later-date-offer.json")
    for case in data["classes"]:
        check_product(case["product"], "later-date-offer.json " + case["name"])
        yield case, {"afterDate": after_date_class(data["foods"], case["product"])}
    for case in data["cases"]:
        check_case(case, "later-date-offer.json " + case["name"])
        yield case, later_date_offer(data["foods"], case["product"], case["batch"], case["storageKind"],
                                     parse_date(case["today"]))


def expect_freeze_check(data):
    check_foods(data, "freeze-check.json")
    for case in data["cases"]:
        check_case(case, "freeze-check.json " + case["name"])
        yield case, freeze_check(data["foods"], case["product"], case["batch"], case["storageKind"],
                                 parse_date(case["today"]))


def expect_before_date_tips(data):
    check_foods(data, "before-date-tips.json")
    check_tips(data["table"], "vectors/before-date-tips.json", data["foods"])
    for case in data["cases"]:
        check_case(case, "before-date-tips.json " + case["name"])
        yield case, {"tips": before_date_tips(data["table"], data["foods"], case["product"], case["batch"],
                                              case["storageKind"], parse_date(case["today"]))}


def expect_before_date_tips_table(data):
    """Facts about spec/before-date-tips.json, and the tips of batches with that table and spec/foods.json."""
    foods = json.loads((SPEC / "foods.json").read_text(encoding="utf-8"))["foods"]
    table = json.loads((SPEC / "before-date-tips.json").read_text(encoding="utf-8"))
    check_tips(table, "before-date-tips.json", foods, freezer_days=True)
    for case in data["facts"]:
        yield case, {"sources": len(table["sources"]), "tips": len(table["tips"]),
                     "kinds": {kind: sum(1 for tip in table["tips"] if tip["kind"] == kind) for kind in TIP_KINDS},
                     "foods": len({food_id for tip in table["tips"] for food_id in tip["foods"]})}
    for case in data["cases"]:
        check_case(case, "before-date-tips-table.json " + case["name"])
        yield case, {"tips": before_date_tips(table, foods, case["product"], case["batch"], case["storageKind"],
                                              parse_date(case["today"]))}


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
    "good-until.json": expect_good_until,
    "later-date-offer.json": expect_later_date_offer,
    "before-date-tips.json": expect_before_date_tips,
    "before-date-tips-table.json": expect_before_date_tips_table,
    "freeze-check.json": expect_freeze_check,
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

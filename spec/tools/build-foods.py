#!/usr/bin/env python3
"""Makes spec/foods.json from the USDA FSIS FoodKeeper data.

    python spec/tools/build-foods.py <path to foodkeeper.json> <date of the download, YYYY-MM-DD>

Get the source file with a browser from https://www.fsis.usda.gov/shared/data/EN/foodkeeper.json. The server refuses
requests from scripts. The data set is "FSIS - FoodKeeper Data" at https://catalog.data.gov/dataset/fsis-foodkeeper-data,
with the licence CC0 1.0. The source file is not in this repository.

The rules of the conversion:
- A food gets the identifier "fk-" plus the FoodKeeper ID.
- The days for a storage kind come from the "date of purchase" values (DOP_Pantry, DOP_Refrigerate, DOP_Freeze). If a
  food has none, they come from the general values (Pantry, Refrigerate, Freeze). Values for "after thawing" are not
  used.
- The opened days ("openedDays") for a storage kind come from the "after opening" values (Pantry_After_Opening,
  Refrigerate_After_Opening). The source has none for the freezer. The rules of the next three lines apply to them
  also. A food with no opened days has no "openedDays" key.
- The days are the minimum of the range, which is the careful value. If only the maximum has a value, that is used.
- Weeks are 7 days, months are 30 days, and years are 365 days. A value in hours, and a value below 1 day, gives no
  days.
- "Package use-by date", "Indefinitely", "When Ripe", and "Not Recommended" give no days. The app then makes no
  estimate, and the person enters the printed date.
- The usual storage kind ("usualKind") is the first kind of pantry, fridge, and freezer for which the source has a
  time: a number, "Package use-by date", "When Ripe", or "Indefinitely". All the groups of the kind count, also
  "after opening" and "after thawing". "Not Recommended" and a tip with no time do not count. A food of the
  FoodKeeper category "Food Purchased Frozen" has the usual kind freezer. A food with no time has no usual kind.
- The tip for a storage kind ("tips") is the text of the source about how to keep the food in that kind: the tip of
  the "date of purchase" group (DOP_Pantry_tips, DOP_Refrigerate_tips, DOP_Freeze_Tips), and if the food has none, the
  tip of the general group (Pantry_tips, Refrigerate_tips, Freeze_Tips). The text is as in the source, with one space
  between words, and with the spelling mistakes in TIP_REPAIRS corrected. A food with no tip has no "tips" key.
- "common" (true) and "aliases" come from spec/tools/food-extras.json, which is edited by hand. An alias is in lowercase.
  An alias that is the name of the food, or that is two times in the list, is not added. A food that is not common has
  no "common" key, and a food with no alias has no "aliases" key.
- The after-date class ("afterDate") is "strict" or "check". It comes from spec/tools/food-classes.json, which is edited
  by hand: the class of the FoodKeeper category of the food, or the other class when the file lists the food. A food
  of a category that is not in the file is strict. Each food has the key. The names of the categories in the file must
  agree with the source.
- The category ("category") is the category of the FoodKeeper category of the food (CATEGORY), or the category that
  spec/tools/food-categories.json gives the food. That file is edited by hand. It lists the foods of a FoodKeeper
  category that has foods of more than one category of this product, for example "Shelf Stable Foods" and "Food
  Purchased Frozen". Frozen food has the category of what it is. ADR 0017 has the reasons.
"""
import json
import sys
from pathlib import Path

SPEC = Path(__file__).resolve().parent.parent
EXTRAS = SPEC / "tools" / "food-extras.json"
CLASSES = SPEC / "tools" / "food-classes.json"
CATEGORIES_FILE = SPEC / "tools" / "food-categories.json"
AFTER_DATE_CLASSES = ["strict", "check"]

# The categories of this product (rule 1 of spec/rules.md).
CATEGORIES = ["produce", "dairy", "meat", "condiment", "beverage", "bakery", "leftovers", "other",
              "grains", "canned", "baking", "snacks", "meals"]

DAYS_PER = {"days": 1, "weeks": 7, "months": 30, "year": 365, "years": 365}

# FoodKeeper Category_ID to the category of this product. spec/tools/food-categories.json gives a different category
# to single foods. For a category with foods of more than one category, the map has the category of most of them.
CATEGORY = {
    1: "other",       # Baby Food
    2: "bakery",      # Baked Goods: Bakery
    3: "baking",      # Baked Goods: Baking and Cooking
    4: "bakery",      # Baked Goods: Refrigerated Dough
    5: "beverage",    # Beverages
    6: "condiment",   # Condiments, Sauces & Canned Goods
    7: "dairy",       # Dairy Products & Eggs
    8: "meat",        # Food Purchased Frozen
    9: "grains",      # Grains, Beans & Pasta
    10: "meat", 11: "meat", 12: "meat", 13: "meat",   # Meat
    14: "meat", 15: "meat", 16: "meat", 17: "meat",   # Poultry
    18: "produce",    # Produce: Fresh Fruits
    19: "produce",    # Produce: Fresh Vegetables
    20: "meat", 21: "meat", 22: "meat",               # Seafood
    23: "snacks",     # Shelf Stable Foods
    24: "other",      # Vegetarian Proteins
    25: "meals",      # Deli & Prepared Foods
}

# The source groups for each storage kind, the preferred group first.
GROUPS = {
    "pantry": ["DOP_Pantry", "Pantry"],
    "fridge": ["DOP_Refrigerate", "Refrigerate"],
    "freezer": ["DOP_Freeze", "Freeze"],
}

# The source group with the days after the package is opened, for each storage kind that has one.
OPENED_GROUPS = {
    "pantry": "Pantry_After_Opening",
    "fridge": "Refrigerate_After_Opening",
}

# The source groups that show that a food can be kept in a storage kind, for the usual storage kind. The order of the
# keys is the order of preference.
USUAL_GROUPS = {
    "pantry": ["DOP_Pantry", "Pantry", "Pantry_After_Opening"],
    "fridge": ["DOP_Refrigerate", "Refrigerate", "Refrigerate_After_Opening", "Refrigerate_After_Thawing"],
    "freezer": ["DOP_Freeze", "Freeze"],
}

# The FoodKeeper Category_ID "Food Purchased Frozen".
PURCHASED_FROZEN = 8

# The source groups with the tip for each storage kind, the preferred group first. The source writes "Freeze_Tips"
# with a capital letter.
TIP_GROUPS = {
    "pantry": ["DOP_Pantry_tips", "Pantry_tips"],
    "fridge": ["DOP_Refrigerate_tips", "Refrigerate_tips"],
    "freezer": ["DOP_Freeze_Tips", "Freeze_Tips"],
}

# Spelling mistakes of the source in the tips.
TIP_REPAIRS = {
    "Nnot necessary.": "Not necessary.",
    "It is not recommend freezing cranberry sauce, as after thawing, it may become too watery.":
        "Freezing cranberry sauce is not recommended, as after thawing, it may become too watery.",
}

# The metrics with no number that still give a time to keep the food.
TIME_WORDS = {"package use-by date", "when ripe", "indefinitely"}


def clean(text):
    """Text without space at the ends, and with the damaged character of the source file repaired."""
    if text is None:
        return None
    text = " ".join(str(text).split())
    return text.replace("consomm�", "consommé") or None


def days_of(row, group):
    metric = clean(row.get(group + "_Metric"))
    value = row.get(group + "_Min")
    if not isinstance(value, (int, float)):
        value = row.get(group + "_Max")
    if metric is None or not isinstance(value, (int, float)) or metric.lower() not in DAYS_PER:
        return None
    days = int(value * DAYS_PER[metric.lower()])
    return days if days >= 1 else None


def has_time(row, group):
    """True when the group of the row gives a time to keep the food."""
    metric = clean(row.get(group + "_Metric"))
    if metric is None or metric.lower() == "not recommended":
        return False
    number = any(isinstance(row.get(group + end), (int, float)) for end in ("_Min", "_Max"))
    return number or metric.lower() in TIME_WORDS


def usual_kind(row):
    if int(row["Category_ID"]) == PURCHASED_FROZEN:
        return "freezer"
    return next((kind for kind, groups in USUAL_GROUPS.items() if any(has_time(row, g) for g in groups)), None)


def tips_of(row):
    tips = {}
    for kind, groups in TIP_GROUPS.items():
        tip = next((text for text in (clean(row.get(group)) for group in groups) if text), None)
        if tip:
            tips[kind] = TIP_REPAIRS.get(tip, tip)
    return tips


def rows_of(source, name):
    """The rows of a sheet of the source, each as one dictionary."""
    sheet = next(s for s in source["sheets"] if s["name"] == name)
    for cells in sheet["data"]:
        row = {}
        for cell in cells:
            row.update(cell)
        yield row


def after_date_classes(source):
    """The after-date class of each FoodKeeper category, and of the foods that the file lists."""
    classes = json.loads(CLASSES.read_text(encoding="utf-8"))
    names = {}
    for row in rows_of(source, "Category"):
        sub = clean(row.get("Subcategory_Name"))
        names[str(int(row["ID"]))] = clean(row["Category_Name"]) + (": " + sub if sub else "")
    problems = []
    for key, category in classes["categories"].items():
        if names.get(key) != category["name"]:
            problems.append("category %s is %r in the source" % (key, names.get(key)))
        if category["afterDate"] not in AFTER_DATE_CLASSES:
            problems.append("category %s has a bad class" % key)
    by_category = {int(key): category["afterDate"] for key, category in classes["categories"].items()}
    if set(classes["foods"]) - set(AFTER_DATE_CLASSES):
        problems.append("'foods' has a key that is not a class")
    by_food = {}
    for name in AFTER_DATE_CLASSES:
        for food_id in classes["foods"].get(name, []):
            if food_id in by_food:
                problems.append("%s is in 'foods' two times" % food_id)
            by_food[food_id] = name
    return by_category, by_food, problems


def food_categories():
    """The category of each food that spec/tools/food-categories.json lists."""
    listed = json.loads(CATEGORIES_FILE.read_text(encoding="utf-8"))["foods"]
    problems = ["'foods' has a key that is not a category: %s" % key for key in listed if key not in CATEGORIES]
    by_food = {}
    for name, food_ids in listed.items():
        for food_id in food_ids:
            if food_id in by_food:
                problems.append("%s is in 'foods' two times" % food_id)
            by_food[food_id] = name
    return by_food, problems


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    source = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    class_of_category, class_of_food, problems = after_date_classes(source)
    category_of_food, category_problems = food_categories()
    foods = []
    for row in rows_of(source, "Product"):
        days = {}
        for kind, groups in GROUPS.items():
            for group in groups:
                value = days_of(row, group)
                if value is not None:
                    days[kind] = value
                    break
        food = {"id": "fk-%d" % int(row["ID"]), "name": clean(row["Name"])}
        subtitle = clean(row.get("Name_subtitle"))
        if subtitle:
            food["subtitle"] = subtitle
        food["category"] = CATEGORY[int(row["Category_ID"])]
        keywords = []
        for word in (clean(row.get("Keywords")) or "").split(","):
            word = word.strip().lower()
            if word and word not in keywords:
                keywords.append(word)
        food["keywords"] = keywords
        food["days"] = days
        opened = {kind: value for kind, value in ((kind, days_of(row, group)) for kind, group in OPENED_GROUPS.items())
                  if value is not None}
        if opened:
            food["openedDays"] = opened
        usual = usual_kind(row)
        if usual:
            food["usualKind"] = usual
        tips = tips_of(row)
        if tips:
            food["tips"] = tips
        food["afterDate"] = class_of_category.get(int(row["Category_ID"]), "strict")
        foods.append(food)
    foods.sort(key=lambda food: int(food["id"][3:]))

    extras = json.loads(EXTRAS.read_text(encoding="utf-8"))
    by_id = {food["id"]: food for food in foods}
    for food_id, name in class_of_food.items():
        if food_id not in by_id:
            problems.append("%s is not in the source" % food_id)
        elif by_id[food_id]["afterDate"] == name:
            problems.append("%s has the class of its category; remove it from 'foods'" % food_id)
        else:
            by_id[food_id]["afterDate"] = name
    if problems:
        print("food-classes.json: %s" % "; ".join(problems))
        return 1
    for food_id, name in category_of_food.items():
        if food_id not in by_id:
            category_problems.append("%s is not in the source" % food_id)
        elif by_id[food_id]["category"] == name:
            category_problems.append("%s has the category of its FoodKeeper category; remove it from 'foods'" % food_id)
        else:
            by_id[food_id]["category"] = name
    if category_problems:
        print("food-categories.json: %s" % "; ".join(category_problems))
        return 1
    unknown = [food_id for food_id in list(extras["common"]) + list(extras["aliases"]) if food_id not in by_id]
    if unknown:
        print("food-extras.json has foods that are not in the source: %s" % ", ".join(unknown))
        return 1
    for food_id in extras["common"]:
        by_id[food_id]["common"] = True
    for food_id, names in extras["aliases"].items():
        food = by_id[food_id]
        aliases = []
        for name in names:
            name = " ".join(name.split()).lower()
            if name and name != food["name"].lower() and name not in aliases:
                aliases.append(name)
        if aliases:
            food["aliases"] = aliases

    if "�" in json.dumps(foods, ensure_ascii=False):
        print("The source has a damaged character that clean() does not repair.")
        return 1

    lines = ["{"]
    header = {
        "source": "USDA FSIS FoodKeeper Data, https://catalog.data.gov/dataset/fsis-foodkeeper-data",
        "sourceFile": source.get("fileName"),
        "sourceLicence": "CC0 1.0",
        "downloaded": sys.argv[2],
        "note": "Made by spec/tools/build-foods.py. Do not edit by hand.",
    }
    for key, value in header.items():
        lines.append("  %s: %s," % (json.dumps(key), json.dumps(value, ensure_ascii=False)))
    lines.append('  "foods": [')
    lines.extend("    %s%s" % (json.dumps(food, ensure_ascii=False), "," if index < len(foods) - 1 else "")
                 for index, food in enumerate(foods))
    lines.append("  ]")
    lines.append("}")
    (SPEC / "foods.json").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("%d foods; with days: %s" % (len(foods), {
        kind: sum(1 for food in foods if kind in food["days"]) for kind in GROUPS}))
    print("with opened days: %s; with one or more: %d" % (
        {kind: sum(1 for food in foods if kind in food.get("openedDays", {})) for kind in OPENED_GROUPS},
        sum(1 for food in foods if "openedDays" in food)))
    print("category: %s" % {name: sum(1 for food in foods if food["category"] == name) for name in CATEGORIES})
    print("after-date class: %s" % {
        name: sum(1 for food in foods if food["afterDate"] == name) for name in AFTER_DATE_CLASSES})
    return 0


if __name__ == "__main__":
    sys.exit(main())

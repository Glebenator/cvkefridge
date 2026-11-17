# Add five categories for the pantry and ready meals

The category of a product has eight values: `produce`, `dairy`, `meat`, `condiment`, `beverage`, `bakery`,
`leftovers`, and `other`. They came from the old FridgeFriend app (ADR 0003), and nobody researched them. The category
has three uses:

- the category filter and the sort on My Fridge,
- the after-date class of a product that has no food of the table (rule 9.1 of `spec/rules.md`, ADR 0014),
- the food match of a scanned product: the category of the scan rules narrows the foods that can match the name
  (`ProductCategories` and `FoodMatch` in the Android app).

The research of 17 November 2026 found these problems:

- `other` had 223 of the 661 foods of `spec/foods.json`. 182 of them are pantry foods: pasta, rice, flour, cereal,
  canned food, crackers, nuts, spices, and oils. Frozen food, baby food, and tofu were also `other`.
- 194 of these 223 foods have the after-date class `check`. But rule 9.1 makes a product of the category `other` with
  no food `strict`. A scanned dry food thus got no "Still good?".
- With the old scan rules, 35 of the 100 most-scanned Open Food Facts products of Canada got `other`, and 13 of the 100
  most-scanned products of the United States (search API, sorted by `unique_scans_n`, fetched on 17 November 2026).
- `leftovers` also had food that people buy at a deli counter: hummus, deli meat, and potato salad (FoodKeeper category
  25, "Deli & Prepared Foods"). No scan rule gave `leftovers`, so the category had two meanings.
- Official lists are finer. The USDA FoodKeeper has 25 categories. The storage table of Health Canada has 12 headings
  for the fridge and the freezer.
- Competitors have 6 or 7 categories (Expireless, Well Stockd). Users of KitchenPal say that its categories are "too
  coarse". Users of Pantry Check say that it has "way too many" (`docs/research/competitor-apps.md`).

The owner approved the decision below on 17 November 2026.

## Decisions

- **The eight keys stay.** A change log keeps the key of the category of each product (rule 7), so an old log stays
  valid. No key is renamed.
- **Five categories are added.**

| Key | Label | Holds | After-date class with no food (rule 9.1) |
|---|---|---|---|
| `grains` | Pasta, rice & grains | dry pasta, rice, cereal, dry beans, lentils, seeds | `check` |
| `canned` | Canned & jarred | canned vegetables, fruit, fish, meat, and broth; food in jars | `check` |
| `baking` | Baking & spices | flour, sugar, honey, syrup, salt, spices, oils, fats | `check` |
| `snacks` | Snacks & sweets | chips, crackers, nuts, chocolate, candy, ice cream | `check` |
| `meals` | Ready meals & deli | bought meals, frozen entrees, pizza, deli salads, hummus | `strict` |

- **Two labels change. Their keys stay.** `dairy` is "Dairy & eggs". `meat` is "Meat & fish". The other labels stay.
- **`leftovers` is home-cooked food only.** Food from a deli counter is `meals`, or `meat` for deli meat.
- **There is no "Frozen" category.** Frozen is a storage kind (rule 1), not a food group. Frozen food gets the
  category of what it is: frozen vegetables are `produce`, frozen fish is `meat`, and frozen entrees and pizza are
  `meals`.
- **The after-date class of a food does not change.** The class comes from the FoodKeeper category and from
  `spec/tools/food-classes.json`, not from the category of this product. The rebuilt table has the same 262 strict and
  399 check foods.
- **A product with no food gets its class from the new categories also.** The four pantry categories are `check`:
  dry and canned food keeps long, and the person can check it. `meals` is `strict`, as `leftovers`: a bought meal has
  cooked meat, fish, egg, or rice, and the senses do not show if it is safe.

### The table of foods

- `spec/tools/build-foods.py` gives each food the category of its FoodKeeper category (the map `CATEGORY`).
- Five FoodKeeper categories, and some single foods of other categories, have foods of more than one category. The new
  file `spec/tools/food-categories.json` is edited by hand, in the same way as `food-classes.json`. It lists the foods
  that get a different category than the map gives. `build-foods.py` stops when a food is not in the source, when a
  food is in two lists, or when a food is in the list of the category that the map already gives it.
- The map gives the category of most foods of a FoodKeeper category: 3 "Baking and Cooking" is `baking`, 8 "Food
  Purchased Frozen" is `meat`, 9 "Grains, Beans & Pasta" is `grains`, 23 "Shelf Stable Foods" is `snacks`, and 25
  "Deli & Prepared Foods" is `meals`.
- The category of a food agrees with the category that the scan rules give to the same food, because `FoodMatch` looks
  only at foods of the category of the scan. Thus:
  - Peanut butter, the other nut butters, and chocolate hazelnut spread are `condiment`. Open Food Facts puts them
    under `en:spreads`.
  - Honey and syrups are `baking`. Open Food Facts puts them under `en:sweeteners`.
  - Plain chocolate (food fk-216) is `snacks`. Open Food Facts puts all chocolate under `en:sweet-snacks`.
  - Canned tuna, canned seafood, canned meat, canned chicken, and canned ham are `canned`, not `meat`.
  - Deli meat (luncheon meat, sliced turkey, ham, salami, Canadian bacon, and pâté) is `meat`. Open Food Facts puts
    it under `en:meats-and-their-products`.
  - Guacamole, salsa, and olives from an olive bar are `condiment`. Open Food Facts puts them under `en:dips` and
    `en:sauces`. Hummus is `meals`, because the owner named it there, and the scan rule of `meals` has the tag
    `en:hummus`.
  - Cookies and cakes stay `bakery`, as in FoodKeeper.
- The foods named "Leftovers", cooked rice, cooked pasta, cooked quinoa, casseroles, homemade broth, homemade
  vegetable soup, and homemade kugel are `leftovers`.
- Baby food (7 foods), tofu, textured soy protein, soy meat substitutes, and tempeh stay `other`. No category fits
  them.
- The result: 13 foods are `other`, not 223. The counts are in `spec/vectors/food-table.json` (key `category`).

### The scan rules

A rule matches a whole category tag of Open Food Facts. The tags of a product include all parent categories. The first
rule that matches gives the category. Each tag below was checked against the categories taxonomy of Open Food Facts
(`https://static.openfoodfacts.org/data/taxonomies/categories.json`, 17 November 2026). The order is:

| # | Category | Tags |
|---|---|---|
| 1 | `canned` | `en:canned-foods` |
| 2 | `meals` | `en:meals`, `en:sandwiches`, `en:hummus` |
| 3 | `dairy` | `en:dairies`, `en:eggs` |
| 4 | `meat` | `en:meats-and-their-products`, `en:meats`, `en:poultries`, `en:fishes`, `en:seafood` |
| 5 | `beverage` | `en:beverages` |
| 6 | `bakery` | `en:breads`, `en:biscuits-and-cakes`, `en:pastries`, `en:viennoiseries` |
| 7 | `snacks` | `en:snacks`, `en:confectioneries`, `en:chocolates`, `en:desserts`, `en:nuts` |
| 8 | `baking` | `en:vegetable-oils`, `en:animal-fats`, `en:sweeteners`, `en:herbs-and-spices`, `en:salts`, `en:flours`, `en:cooking-helpers` |
| 9 | `condiment` | `en:condiments`, `en:sauces`, `en:spreads` |
| 10 | `grains` | `en:cereals-and-their-products`, `en:pastas`, `en:legumes-and-their-products`, `en:seeds` |
| 11 | `produce` | `en:fruits`, `en:vegetables`, `en:fruit-based-foods`, `en:vegetables-based-foods` |

The reasons for the order and the tags:

- **`canned` is first.** Canned tuna has the tags `en:fishes` and `en:canned-foods`. With `meat` first, canned tuna is
  `meat`, and `FoodMatch` cannot find the food "Tuna, canned". Canned soup is under `en:meals` also; it is `canned`,
  as the owner said ("canned vegetables, fish, soup").
- **`meals` is before `dairy` and `meat`.** A pizza with cheese and a meal with fish are meals.
  `en:pizzas`, `en:soups`, and `en:prepared-salads` are children of `en:meals`, so the rule does not need them.
- **`meat` uses `en:meats-and-their-products`, not `en:meats`.** Ham and sausages are under `en:prepared-meats`, which
  is not a child of `en:meats`. The old rule did not find them. `en:meats`, `en:poultries`, and `en:fishes` stay in
  the rule for a product that has a tag but not all of its parents. A meat substitute under
  `en:prepared-alternate-meats` is also `meat`.
- **`bakery` is before `snacks`.** In the taxonomy, `en:biscuits-and-cakes`, `en:pastries`, and `en:viennoiseries` are
  children of `en:sweet-snacks`. With `snacks` first, a croissant is a snack. `en:biscuits-and-cakes` stays in
  `bakery`, so that a scanned cookie finds the food "Cookies", which FoodKeeper puts in "Bakery". `en:breads` is a
  child of `en:cereals-and-their-products`, so `bakery` is also before `grains`.
- **`snacks` is before `baking`.** Chocolate for cooking has `en:cooking-helpers` and `en:chocolates`. It is `snacks`,
  as the food "Chocolate".
- **`baking` is before `condiment`, and it does not use `en:fats`.** Salt and spices are children of `en:condiments`.
  Some peanut butters and hazelnut spreads have the tag `en:fats`, so the rule uses `en:vegetable-oils` and
  `en:animal-fats`. Butter is `dairy`, because `dairy` comes first. Honey has `en:sweeteners` and `en:spreads`, and it
  is `baking`.
- **`condiment` is before `grains`.** Peanut butter is under `en:legumes-and-their-products` and `en:spreads`. It is
  `condiment`.
- **`grains` does not need `en:rices` or `en:breakfast-cereals`.** They are children of
  `en:cereals-and-their-products`.
- **The old produce tag `en:fruits-based-foods` does not exist.** The tag is `en:fruit-based-foods`.
- **Results with the two samples above:** 2 of 100 products of Canada and 2 of 100 products of the United States are
  `other`. Two of the four have no category tags. The other two are a grain-free granola and a baking powder.
- **Results for the food match** (a model of `FoodMatch` in Python, the two samples and 20 more product names): 39
  products find the same food as before, 12 find a food that they did not find before (for example peanut butter,
  canned tuna, hummus, salt, and spices), and 5 do not find the food that they found before. Four of the five were
  wrong before: olive oil found "Olives", peanut butter pretzels found "Peanut butter", and noodles with chicken
  flavour found "Fried chicken". One is a real loss: pitted dates with the wrong tag "mixed nuts and dried fruits"
  are `snacks`, and the food "Dates" is `produce`.

The rules are in the Android app (`lookup/ProductMapping.kt`). The iOS app has no product lookup yet. When it gets
one, it uses the same order and the same tags. The rules are not in `spec/` yet, as before.

### An old app version and a new key

Each app reads the change log with `ChangeCodec`. A category key that the app does not know is an error:

- Android: `ChangeCodec.decode` throws `IllegalArgumentException` ("Unknown value of category"). `FridgeViewModel`
  then shows the state "LoadFailed", and the reminders see no inventory. `ChangeLogStore.append` reads the log before
  it writes, so it also fails, and the file does not change.
- iOS: `decodeEnum` throws `JSONFormatError` ("category has an unknown value").

A log with a new key can come only from a new app version. The log stays on one phone (ADR 0002), so this happens only
when the person installs an older version over a newer one, or restores a backup into an older version. No data is
lost: the file stays as it is, and a new version reads it again. This ADR does not change the codec. Household
sharing (deferred) must decide what an old phone does with a key that it does not know.

## Consequences

- `spec/rules.md` rules 1 and 9.1, `GLOSSARY.md`, `spec/tools/build-foods.py`, `spec/tools/vectors.py`,
  `spec/foods.json`, and the vectors `food-table.json`, `later-date-offer.json`, and `change-log.json` change.
- Each app has 13 values in its `Category` enum, and the category menu on My Fridge and the forms show 13 values. The
  menu shows only the categories that have food, so a small inventory still shows few values.
- A product that the person saved before this change keeps its category. A product of the category `other` does not
  move to a new category.

# Offer a later date only for food that the person can check

ADR 0009 gave each batch that is expiring or expired the controls "Still good?" with "+1 day", "+1 week", and "Other
date". That includes raw chicken and food with a safety date. On 17 November 2026 the owner said that the app must be
careful: it must not suggest that a person eats spoiled food. This ADR is the second part of the work that ADR 0013
starts. It replaces a part of ADR 0009.

The expiry research ([expiry-dates.md](../research/expiry-dates.md), section 5) found:

- In the European Union and the United Kingdom, "use by" is a safety date. Food is not safe after it, and the senses
  do not show the danger (Regulation (EU) 1169/2011, Article 24). "Best before" is a quality date. Food is often
  still good after it, and the person can look, smell, and taste.
- In Canada, almost all food has "best before", also raw meat. An "expiration date" is only on infant formula, meal
  replacements, and similar foods, and such food must be thrown away after the date. Health Canada says not to judge
  the safety of food by its smell or its taste.
- The United States has no federal rule, with the exception of infant formula.

The label alone thus does not say if a food can be good after its date. Each food also needs its own class.

## Decisions

- **A printed date can have a date type.** The value is `useBy`, `bestBefore`, or none. The key is `dateType` in the
  batch of a `batchAdded` change and in a `batchEdited` change. A change with no `dateType` key has no date type, as
  for the opened date (ADR 0013). Only a date with the source `printed` has a date type. None means that the app does
  not know the type. The app does not guess it.
- **The words of the package give the date type.** "Use by" and "expiration date" are `useBy`. "Best before", "best
  before end", "best by", and "best if used by" are `bestBefore`. "Sell by", "display until", "packaged on", "freeze
  by", and a date with no words have no date type. "Use by" on a package from the United States is `useBy` also: the
  words do not have a legal meaning there, and the careful value is the safety date.
- **The glossary has the terms date type, use-by date, and best-before date.** The glossary said to avoid "best
  before" and "use by" as words for the expiry date. That stays. They are the words of a label, and a label is a
  date type.
- **Each food of the table has an after-date class: `strict` or `check`.** A strict food is not good to eat after
  its date, and the senses do not show if it is safe. A check food is often still good after its date, and the person
  can check it. The key is `afterDate` in `spec/foods.json`. 262 foods are strict and 399 are check.
- **The classes are in a file that is edited by hand.** `spec/tools/food-classes.json` gives a class to each of the
  25 FoodKeeper categories, and it lists the foods that have the other class than their category.
  `spec/tools/build-foods.py` adds the classes to the table, and it stops when a category name does not agree with
  the source.
- **A food with no clear class is strict.** The strict categories are baby food, refrigerated dough, dairy products
  and eggs, fresh meat, smoked or processed meat, stuffed meat, all poultry that is not in a can, all seafood,
  vegetarian proteins, and deli and prepared foods. The exceptions in the two directions are in the file. The main
  ones:
  - Check in a strict category: butter, hard cheese, grated parmesan, processed cheese, margarine, yogurt, kefir,
    buttermilk, sour cream, milk, plant drinks, milk powder, miso, and dry soy protein. GOV.UK and the Voedingscentrum
    name milk and dairy products with a best-before date as food that a person can smell.
  - Strict in a check category: pies and cakes with cream, custard, or egg, quiche, juice that is freshly squeezed,
    food that is made or canned at home, fresh pasta, cooked grains, sprouts, bagged greens, baby carrots, cut squash,
    vegetables in oil, and drinks that replace a meal.
  - Eggs are strict. The Food Standards Agency says that eggs are safe for a couple of days after the best-before
    date if they are cooked well. "+1 week" is more than that, and the offer cannot say how to cook the eggs.
  - A food that is purchased frozen has the class of the same food when it is not frozen: frozen fish, shellfish,
    sausages, prepared meals, pizza, and dough are strict, and frozen vegetables, fruit, potato products, and ice
    cream are check. The core does not know if the batch was thawed (ADR 0016).
- **A product with no food of the table gets its class from its category.** `condiment`, `beverage`, and `bakery`
  are `check`. `produce`, `dairy`, `meat`, `leftovers`, and `other` are `strict`. A product of the category `produce`
  with no food can be cut fruit or a bagged salad, and `other` has each food that has no better category. The class
  of the food comes before the category.
- **Rule 9 of `spec/rules.md` says if the app can show the later-date offer.** The result is an offer, or no offer
  with a reason:
  1. `notDue`: the batch is not expiring and not expired.
  2. `useByDate`: the good-until date is a printed date with the date type `useBy`.
  3. `strictFood`: the after-date class of the product is `strict`. This is also the result for a strict food with
     a best-before date, as on raw meat in Canada, with no date type, and with an estimated date.
  4. `opened`: the good-until date comes from the opened date. A chosen date cannot move it (ADR 0013).
  5. In each other case, the app shows the offer.
- **The freezer is not an exception.** Frozen food stays safe, so a strict food in a freezer could get the offer
  after its estimated date. But the core does not know when the batch went into the freezer. Raw chicken that goes
  into the freezer five days after its date would then get the offer. The same rule applies in each storage kind.
- **The edit form stays open.** The person can change the expiry date of each batch in the edit form, as before. A
  date that the person selects there is a printed date (ADR 0009). The estimate for a strict food is the careful
  value of the table, for example 1 day for raw chicken. If the package has a later date, the person enters it.
- **The reason is for the screen.** With no offer, the app can say why, for example "Do not eat this after its
  use-by date." The words are a decision of the screens, not of this ADR.

## What this replaces in ADR 0009

The third decision of ADR 0009 said that a batch that is expiring or expired has "Still good?". Now such a batch has
"Still good?" only when rule 9 gives an offer. The other decisions of ADR 0009 stay: the source `chosen`, "Your date",
the three buttons and what they do, and the rule of the edit form.

## Results

- `spec/vectors/later-date-offer.json` has the cases for the class of a product and for the offer. `change-log.json`
  has cases with a date type. `food-table.json` has the number of foods in each class and the class of the sampled
  foods.
- An earlier version of the app reads a change log with a date type, but it does not keep the date type: both codecs
  ignore a key that they do not know. The app has no users yet, so no conversion is necessary.
- The add form and the edit form need a control for the date type of a printed date. It is optional. A batch from
  before this decision has no date type.
- Most scanned products have no food of the table (ADR 0011). Their class comes from their category, and `other` is
  strict. A bag of crisps with no food thus gets no offer. A later step can give a looked-up product a class from its
  category tags, as rule 8 does for the storage kind.
- The classes are a selection by hand from the names of the foods. No official source has a list with these two
  classes for these 661 foods. The owner or a person who knows food safety can change the file.
- Section 8.2 of the plan has the decisions that the owner has to make: the class of eggs, the offer for a strict
  food in a freezer, the class of a product with no food, and the offer for a batch that is opened.

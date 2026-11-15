# Show storage tips and mark the text of the package

On 14 November 2026, after the storage hint (ADR 0011), the owner asked for storage tips: when somebody scans bananas,
the app says how to keep them. The owner also asked for a check mark that shows a tip from data about the scanned
product, so that the person can tell it from general advice.

The app has two sources with facts about storage:

- The **storage text** of a product: the text on its package, which the product lookup gets from Open Food Facts
  (ADR 0011). In samples of the products with the most scans, 20 % to 45 % of the products had one.
- The FoodKeeper data of the United States Department of Agriculture, which is the source of the table of foods. It
  has the time that a food keeps in each storage kind, and a short tip for some storage kinds of some foods.

## Decisions

- **The app shows storage tips in one card with two parts.** The first part is the storage text of the product. The
  second part is the general advice for the food of the table of foods.
- **Only the storage text has the check mark.** It has the words "From the package" and a check mark, and the card
  says that the text is about this product and that it comes from Open Food Facts. The general advice has no check
  mark. The card says that it is about the food in general, and that it comes from the USDA FoodKeeper data. The
  product rule "Do not show a guess as a fact" asks for this difference.
- **A product keeps its storage text.** The `productSaved` change has the key `storageText` (rule 7.2 of
  `spec/rules.md`), as it has `note` (ADR 0010). A change with no `storageText` key has no storage text. The person
  does not write or edit the storage text. An edit of the product keeps it.
- **The app saves a cleaned storage text.** The app puts one space between words, removes the spaces at the ends, and
  cuts a text of more than 500 characters after a whole word. The core keeps the text as it gets it.
- **A later scan replaces the storage text.** A new product gets the storage text of its scan. A product in the
  inventory gets the storage text of an add that has one. An add with no storage text keeps the text of the product.
- **The app shows the storage text as it is.** The text is in the language of the device when Open Food Facts has
  it in that language. If not, it is in the main language of the product, or in English. The app does not translate
  it.
- **The table of foods has tips.** `spec/foods.json` has `tips` for a food: a text for a storage kind.
  `spec/tools/build-foods.py` takes them from the FoodKeeper data. 147 of the 661 foods have a tip. The words are
  the words of the source. The tips are in English only.
- **The general advice has three kinds of line.** The usual storage kind of the food ("Usual place"). Then, for
  each storage kind, the time that the food keeps there and the tip. The time comes from the days of the table. The
  card shows it as an estimate ("About 3 days."), in the largest unit that gives a whole number: 60 days are 2 months.
- **The card is on the add form and on the screen of the food.** On the add form it is below the storage area,
  because it helps the person to select one. It shows the general advice also for a name that the person types. On
  the screen of the food it is below the batches, so that "Used" and "Thrown away" stay near the top.
- **No language model writes a tip.** Each text in the card comes from one of the two sources. The app does not make
  a text that no source has.

## Results

- The vectors of `change-log.json` have a case with a storage text and products with no `storageText` key, and a
  case that removes a storage text. The expected products of all cases have `storageText`. The vectors of
  `food-table.json` have the number of foods with a tip for each storage kind, and the tips of the sampled foods.
- An earlier version of the app reads a change log with a storage text, but it does not keep the text: both codecs
  ignore a key that they do not know. The app has no users yet, so no conversion is necessary.
- A storage text is data about a product, like its name. It does not go to logs or to crash reports.
- Some tips of the source are short notes about its own numbers, for example "Unopened." or "From date of
  manufacturer." The card shows them next to the time, where they are clear. A later step can select or rewrite tips
  in a file that is edited by hand, as `spec/tools/food-extras.json` does for the aliases.
- The rules for what the card shows are in the Android app only (`inventory/StorageAdvice.kt`): the cleaned text, the
  unit of a time, and the lines of the general advice. Section 6.1 of the plan lists them. They go into `spec/`
  before the iOS app builds the card.
- The iOS core has the storage text of the product and the tips of the foods. The iOS app gets the card when it
  builds the add form and the screen of a food (milestones 2 and 3).
- A product that was scanned before this decision has no storage text. It gets one when the person scans it again
  and Open Food Facts has the text. The cache of the lookup on the phone must have the text also: a product that the
  cache got before ADR 0011 has none.

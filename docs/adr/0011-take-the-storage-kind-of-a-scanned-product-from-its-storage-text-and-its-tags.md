# Take the storage kind of a scanned product from its storage text and its tags

On 14 November 2026 the owner scanned a frozen pizza, and the add form selected the Fridge. The owner asked how to
improve this for all products, and said that a small language model on the phone is acceptable.

The add form selected the storage area of a scanned product from one source: the food of the table of foods that the
product name names, and its usual storage kind. This fails when the name has no English word of the table. A sample
of the 500 products with the most scans in Open Food Facts gave a storage kind for 52 of 494 products with a name
(11 %). Of 99 products with the tag `en:frozen-pizzas`, 70 got the freezer.

## Decisions

- **A looked-up product has a storage hint.** The storage hint is a storage kind and its source. It is a core rule:
  rule 8 of `spec/rules.md`, with the table `spec/storage-hints.json`.
- **The first source is the storage text.** Open Food Facts has the text on the package about how to keep the product
  (`conservation_conditions`). The rule reads only the temperatures in it. A temperature of −6 °C or lower means the
  freezer. Other temperatures mean the fridge up to 10 °C, and the pantry above that. Numbers have the same form in
  each language, so the rule needs no list of words for each language.
- **The text for an opened package is not used.** "After opening, keep at max. 7 °C" is on products from the pantry.
  The table has the phrases that start this text, in the languages of the samples. The rule uses only the text before
  the first phrase.
- **The second source is a list of category tags for each storage kind.** The lists have specific tags only, for
  example `en:frozen-pizzas` and `en:yogurts`.
- **The tag `en:frozen-foods` is not in the lists.** In the samples, 77 products with this tag had a storage text
  with a temperature. For 22 of them the temperature was for the fridge. A cola, a hazelnut spread, and a sliced
  bread have the tag. `en:frozen-breads`, `en:frozen-baking-mixes`, and `en:prepared-meats` are not in the lists for
  the same reason.
- **The storage text comes before the tags.** The text is about this one product. A tag is about a group, and a tag
  can be wrong.
- **The storage hint comes before the usual storage kind of the food.** The hint comes from data about the scanned
  product. The food comes from words in the name. An area that the person selected stays, and a product that is in
  the inventory keeps the area of its newest batch, as before.
- **No language model.** A model on the phone is not on each phone, and the two platforms have different models, so
  the two apps would not give the same result for the same barcode. A model in the app adds some hundred megabytes.
  The rule is small, it is the same in both apps, and the vectors prove it.
- **The request stays the same in what it sends.** The lookup sends the barcode only. It asks Open Food Facts for
  one more field, in the language of the device, in the main language of the product, and in English.

## How the lists were made

The samples are 1440 products from the search of Open Food Facts on 14 November 2026: the products with the most
scans in the world, in Germany, in the United Kingdom, and in the United States, and the products with the most scans
that have the tags for frozen food, frozen pizzas, ice creams, yogurts, cheeses, meats, and dairies. For each tag, the
storage kinds of the storage texts of its products were counted (rule 8.2). A tag is in a list when its products
agree, and when the tag names food that is kept in one storage kind. With the first lists, 127 products had a storage
kind from their text and a storage kind from their tags, and the two agreed for 124. The other 3 were dried sausages
with the tag `en:prepared-meats`, which then left the list. With the final lists, 113 products have the two kinds,
and they agree for all 113. This is not a test with new data: the lists were made from the same samples.

## Results

- With rule 8 before the food of the name, the sample of the 500 products with the most scans gets a storage kind
  for 283 of 494 products (57 %). The 99 products with the tag `en:frozen-pizzas` all get the freezer.
- The samples are small, and most of their storage texts are in French. A storage kind from a pantry tag has little
  proof from the texts, because a product for the pantry seldom has a temperature on its package.
- A later step can make the lists from the full data of Open Food Facts with the same method. The rule stays the
  same.
- A storage kind with no storage area of that kind does not change the form. Only Fridge and Freezer are fixed, so a
  pantry hint has an effect only after the person made a storage area of the kind pantry.
- The cache of the product lookup on the phone keeps the storage text. A product that the cache got before this
  decision has no storage text, and its hint comes from its tags.
- The iOS app has the rule in `CVKEFridgeCore`. It uses the rule when it builds the product lookup (milestone 3).
- The add form does not show the source of the hint. ADR 0012 adds the storage tips, which show the storage
  text.

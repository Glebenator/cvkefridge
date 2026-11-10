# Keep stock as products and batches

FridgeFriend kept one row for each food, with one quantity and one expiry date. When the person added new milk to old
milk, the quantity went up and the old expiry date stayed. The answer of the app was then wrong. A delete was the only
end of a row, so food that was eaten and food that was thrown away looked the same.

## Decisions

- **A product is what the food is. A batch is one purchase of it.** The product has the name, the category, the
  barcode, and the photo. The batch has the quantity, the storage area, the date added, and the expiry date. One
  product can have more than one batch at the same time.
- **Food leaves the oldest batch first.** The order is by expiry date, and then by date added.
- **An expiry date is printed or estimated.** A printed date is the date on the package, which the person entered. An
  estimated date is a suggestion from the app. The app shows an estimated date as an estimate in each place.
- **The estimate comes from a table of foods.** FridgeFriend used eight categories: one number for all meat, and one
  for all produce. The table has an entry for each common food and each storage area. The category stays, for groups
  and filters only.
- **A batch ends as used or as thrown away.** The app keeps the ended batches as the history. A delete is for a
  mistake, and it leaves no history.
- **The app keeps a change log.** Each change to the inventory is one record: the phone that made it, the time, and
  what changed. The inventory is the result of the log.
- **Identifiers are random and unique on all phones.** A product, a batch, and a change each get one when they are
  made.

## Consequences

- The use-first list is a list of batches, not of products. A product with two batches can be in the list two times.
- Undo and the history read the same change log.
- Household sharing is deferred. The change log and the random identifiers let it come later with no conversion of
  data.
- The table of foods is data that both apps read. It needs a source with a licence that permits this use.
- The storage of FridgeFriend cannot be opened by the new apps. An import from FridgeFriend is not planned.

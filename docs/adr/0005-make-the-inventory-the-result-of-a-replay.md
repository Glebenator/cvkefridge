# Make the inventory the result of a replay of the change log

ADR 0003 gave the product a change log. This ADR has the decisions of milestone 1 that make the log exact enough for
two apps. `spec/rules.md` has the full rules.

## Decisions

- **The inventory is a replay.** The core sorts the changes by instant and then by identifier, and applies each one to
  an empty inventory. It keeps no other state. Two phones with the same changes get the same inventory.
- **A change that cannot apply is rejected, not an error.** The replay records the reason and continues. A use takes
  not more than the batch has.
- **Undo is a change.** A `changeUndone` names an earlier change, and the replay skips that change. Nothing is removed
  from the log. An undo cannot be undone.
- **A quantity is a whole number of thousandths.** The core has no fractions, so Kotlin and Swift cannot round in
  different ways.
- **The unit belongs to the product.** All batches of a product have the same unit, so the core can take a quantity
  from more than one batch.
- **A storage area has a kind: pantry, fridge, or freezer.** The table of foods has days for each kind. FridgeFriend
  gave an area that the person created the values of the fridge.
- **The freshness limits stay as in FridgeFriend.** A batch is expiring with 0, 1, or 2 days left.
- **The core does not read the clock or the time zone.** The app gives the instant and the UTC offset, and the core
  calculates the date.
- **An identifier has only `a` to `z`, `0` to `9`, and `-`.** The order of identifiers is then the same in each
  language.

## Consequences

- The replay reads the full log each time. That is fast for the size of a household inventory. Storage can keep a
  result and replay only the new changes, if a measurement shows a need.
- The names of things are not checked in the core. The rules for a name (length, spaces, the same name two times) are
  for the forms of milestone 2.
- An edit replaces all values of a product or a batch. Two phones that edit the same batch give the result of the
  later change. Household sharing can make this more exact when it is built.
- The category of a food from FoodKeeper is mapped to the eight categories. Seafood and poultry are `meat`.

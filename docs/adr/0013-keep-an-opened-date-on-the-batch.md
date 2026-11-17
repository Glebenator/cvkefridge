# Keep an opened date on the batch

On 17 November 2026 the owner said to build the features of the expiry research
([expiry-dates.md](../research/expiry-dates.md)): opened food, the date type and the class of a food after its date,
tips before the date, and frozen and thawed food. This ADR has the decisions for opened food. ADR 0014, ADR 0015, and
ADR 0016 have the other parts.

The research found two facts:

- The official sources agree that the date on a package is for the package that is not opened (Health Canada, the
  CFIA, ANSES, the Voedingscentrum, the Verbraucherzentrale, and EFSA).
- The FoodKeeper data, which is the source of the table of foods (ADR 0004), has a time "after opening" for 202 of
  its 661 foods. `spec/tools/build-foods.py` did not read these values. Example: hot dogs keep 2 weeks in a closed
  package and 1 week in an opened package.

The owner wants a careful app: it must not show food as good when the food can be spoiled. At each choice in this
ADR, the decision is the more careful option.

## Decisions

- **The table of foods has opened days.** `spec/foods.json` has the key `openedDays` for a food: a number of days for
  the pantry, for the fridge, or for the two. The values come from the FoodKeeper groups `Pantry_After_Opening` and
  `Refrigerate_After_Opening`, with the conversion rules of the other days: the minimum of the range, 7 days for a
  week, 30 days for a month, and 365 days for a year. "Not Recommended", "Indefinitely", "Package use-by date", and a
  time in hours give no opened days. 74 foods have opened days for the pantry, 145 have opened days for the fridge,
  and 202 foods have one or the two. The source has no time after opening for the freezer.
- **A batch has an optional opened date.** It is the calendar date on which the person opened the package. The key
  is `openedDate` in the batch of a `batchAdded` change and in a `batchEdited` change.
- **The new change `batchOpened` sets the opened date.** It has the batch and the date, and it changes no other
  value. It is rejected for a batch that is not in the inventory (`unknownBatch`) and for an ended batch
  (`batchEnded`). A second `batchOpened` change replaces the opened date. The undo of the change is the undo of rule
  7.3: the replay skips the change, and the batch has the opened date that it had before.
- **A `batchEdited` change also has the opened date.** An edit replaces all values of a batch (ADR 0005), and the
  edit form is the place where the person corrects or removes an opened date. An edit with no `openedDate` key gives
  the batch no opened date. This is the rule of the note of a product (ADR 0010). Each `batchEdited` change that an
  app writes must thus have the opened date of the batch, also the change of "Still good?".
- **A change with no `openedDate` key has no opened date.** The change logs on the phones from before this decision
  do not have the key. Both core modules read them.
- **The opened date can be before the date added.** A person can add a jar that was opened last week. The core does
  not compare the opened date with today or with the date added.
- **The app uses the good-until date.** The good-until date of a batch is the earlier of its expiry date and its
  after-opening date. The after-opening date is the opened date plus the opened days of the food for the storage kind
  of the storage area of the batch. Rule 5.2 of `spec/rules.md` has the steps. The days left, the freshness, the
  use-first order, and the plan of a use have the good-until date as their input. A batch with no expiry date, an
  opened date, and opened days gets its good-until date from the opened date.
- **The core calculates the good-until date each time.** No change and no batch has it. `AGENTS.md` says: "Calculate
  the days left from data." A batch that moves to a storage area of a different kind gets the opened days of that
  kind with no new change. A later table of foods gives the new value to the batches that are in the inventory.
- **The good-until date has a source.** It is the source of the expiry date (`printed`, `estimated`, or `chosen`), or
  `opened` when the date comes from the opened date. A date with the source `opened` is an estimate. The app shows it
  as an estimate, for example "Opened, about 7 days", and not as a printed date. When the two dates are the same,
  the source is the source of the expiry date.
- **Only the opened days of the storage kind of the batch count.** Ketchup has opened days for the fridge and none
  for the pantry. An opened bottle in a pantry storage area thus has no after-opening date. The core does not take
  the value of a different kind, because the source has none: "Show a value that is missing as missing." An opened
  batch in a freezer has no after-opening date.
- **A chosen date does not come before the after-opening date.** The rule has no exception: the earlier date is the
  good-until date. The batch has no value that says if the person selected the chosen date before or after the
  package was opened. If a chosen date came first in each case, a carton with a chosen date of three months would
  stay "fresh" for three months after it is opened. The result of this decision: the app gives no later-date offer
  for a batch with a good-until date from the opened date (ADR 0014). The person can correct or remove the opened
  date in the edit form.
- **The core does not read the days after opening from the storage text.** Some packages say "use within 3 days of
  opening", and the storage text of a product can have these words (ADR 0011). The numbers have many forms ("2 à 3
  jours", "48 h", "une semaine"), each language needs its words for the units, and we have no count of real storage
  texts for this. A wrong number makes a wrong date. A later step can add it to rule 8 with a sample, as ADR 0011 did
  for the storage kind. A value from the package then comes before the value of the table, with its own source.

## Results

- `spec/vectors/good-until.json` has the cases for rule 5.2, for the use-first order, and for the plan of a use.
  `change-log.json` has 12 new cases for the opened date and the date type. The expected batches of all cases have
  `openedDate` and `dateType`. `food-table.json` has the number of foods with opened days and the opened days of the
  sampled foods.
- The vectors of `use-first.json` and `plan-use.json` stay as they are. Their batches have no opened date, so their
  good-until date is their expiry date.
- An earlier version of the app does not know the change type `batchOpened`. The app has no users yet, so no
  conversion is necessary.
- The rules of the reminders are in the Android app only (section 6.1 of the plan). They use the days left, so they
  must use the good-until date. A batch that is opened can thus get its reminder earlier.
- Each screen that shows the days left or the freshness of a batch uses the good-until date. A screen that shows the
  date also shows its source: a date with the source `opened` is an estimate.
- The opened days are the minimum of the range of one source from the United States. The research found that the
  sources do not agree on the numbers (section 3.5 of the research). The values are estimates.
- The values of the source for "after thawing" are not in the table. ADR 0016 has the proposal for thawed food.
- Section 8.2 of the plan has the decisions that the owner has to make: if a chosen date can come before the
  after-opening date, and if the storage text gives the days after opening.

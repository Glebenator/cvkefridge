# Give thawed food 1 day, and freeze food only up to its date

This is the fourth part of the work that ADR 0013 starts. An earlier version of this document was a proposal with
three options. On 18 November 2026 the owner selected option A, and gave the answers that are in "What the owner
decided". The rules are in `spec/rules.md` (rules 5.1, 5.2, 7.2, 9.2, 10, and 11).

## The problem

- A batch that moved from a freezer storage area to a fridge storage area kept its expiry date. That date can be an
  estimate for the freezer, which is months away. The app then showed thawed chicken as fresh for months.
- A batch could move to a freezer after its date. With an estimated date, the app then showed spoiled food as good
  frozen food.
- The app had no control for the two moves. The person changed the storage area in the edit form.

## What the sources say

- The Food Standards Agency: "Once the food has been defrosted, you need to use it within 24 hours" (GOV.UK,
  "Understanding food labelling: Best before and use-by dates"), and food can go into the freezer "right up until
  midnight" on its use-by date ("How to chill, freeze and defrost food safely"). We opened the two pages on 17
  November 2026.
- The expiry research ([expiry-dates.md](../research/expiry-dates.md), section 4): EFSA gives 24 hours for food that
  was frozen for donation. ANSES says to eat thawed food in three days. One guideline of Ireland permits 3 days.
- The FoodKeeper data has a time "after thawing" for 3 of its 661 foods: chicken nuggets (1 day), frozen edamame (7
  days), and frozen polenta (5 days).
- The table of foods has days for the freezer for 339 of its 661 foods. The lowest value that many foods have is 30
  days: 52 foods have it. The three foods with the name "Leftovers" have 30, 30, and 60 days.
- The USDA Food Safety and Inspection Service says that leftovers can be "frozen for 3 to 4 months", and that they
  are safe for longer but lose quality ("Leftovers and Food Safety"). We opened the page on 18 November 2026.

## What the owner decided

On 18 November 2026:

1. Option A: two changes and two dates.
2. "One day for each food."
3. About a move to a freezer after the date: "Does that say if a food is expired, we can freeze it to extend the
   date? If so, no. But if a food has say 2 days left, then yes, we can freeze it and extend the date. Same thing for
   strict foods."

Later on the same day, after the owner saw the two buttons on the emulator:

4. "all looks good, and your assumptions are valid". This is about the three decisions in "Decisions that the owner
   confirmed".
5. About a frozen batch of a food with no time in the freezer, for example leftovers: "It will be hard to estimate a
   freezer date for sure, but we cannot have No expiry."
6. "when we move the food to the freezer, we add 30 days, but a user should be able to easily change that date on
   that same screen."

## Decisions

- **A batch has an optional frozen date and an optional thawed date.** The frozen date is the calendar date on which
  the person moved the batch to a freezer. The thawed date is the calendar date on which the person moved the batch
  out of a freezer. The keys are `frozenDate` and `thawedDate`. The two dates are facts about the batch, as the
  opened date is (ADR 0013).
- **The new change `batchFrozen` moves a batch to a freezer.** It has the batch, the storage area, and the date. It
  sets the frozen date and removes the thawed date. It changes no other value.
- **The new change `batchThawed` moves a batch out of a freezer.** It has the same values. It sets the thawed date,
  and the batch keeps its frozen date. It changes no other value.
- **The two changes are rejected as `batchOpened` is, and for a storage area that is not there.** The reasons are
  `unknownBatch`, `batchEnded`, and `unknownStorageArea`, in this order. The undo of a change is the undo of rule
  7.3: the batch has the storage area and the two dates that it had before.
- **A `batchEdited` change and the batch of a `batchAdded` change have the two dates also.** An edit replaces all
  values of a batch (ADR 0005). A change with no key has no such date, as for the opened date (ADR 0013). Each
  `batchEdited` change that an app writes must thus have the two dates of the batch, also the change of "Still
  good?".
- **A thawed batch is good for 1 day.** The good-until date of a batch with a thawed date is the thawed date plus 1
  day, with the source `thawed`. This is the value of the Food Standards Agency, and it is the careful value. It is
  the same for each food: the table of foods does not get the three values of the FoodKeeper data. The expiry date,
  the opened date, and the frozen date of the batch have no effect.
- **A frozen batch gets the freezer time of its food from the frozen date.** The good-until date of a batch with a
  frozen date and no thawed date is the frozen date plus the days of its food for the freezer, with the source
  `frozen`. This is how the freezer extends the date. The expiry date of the package does not apply while the batch
  is frozen, and the opened date has no effect.
- **A frozen batch of a food with no days for the freezer has the default freezer days: 30.** The same applies to a
  product with no food of the table, for example leftovers that the person named. The owner said that a frozen batch
  cannot have "No expiry". 30 days is the careful value: it is the lowest value of the table for the food
  "Leftovers", and the USDA page gives a longer time. The date is an estimate with the source `frozen`, and the
  screen says that it is a general estimate. An earlier version of this decision gave such a batch no good-until
  date.
- **The person can change the date of a batch in a freezer on the screen of the food.** The time in the freezer is
  an estimate, and the person knows the food. The date that the person selects is a chosen date ("Your date", ADR
  0009). The app writes one `batchEdited` change with the chosen date as the expiry date and with no frozen date. A
  batch in a freezer with no frozen date has its expiry date (rule 5.2), so the chosen date is the date of the batch.
  This needs no new value on the batch and no new rule in `spec/`.
- **The dates `frozen` and `thawed` are estimates.** The app shows them as estimates, as a date from the opened date.
- **The freeze check says if a batch can go into a freezer (rule 11).** A batch can go into a freezer up to its
  good-until date, and on that date. An expired batch cannot. The rule is the same for a strict food and for a check
  food. A batch with no good-until date can go into a freezer: the app does not know its date.
- **The replay does not do the freeze check.** The check needs the table of foods and the date of today, and the
  replay has neither. The app does the check before it writes a `batchFrozen` change, as it does for the later-date
  offer (ADR 0014).
- **A batch that the person adds to a freezer has no frozen date.** Its date is its expiry date, as before: a
  printed date, or the estimate of the table of foods for the freezer.
- **The storage kind has no effect on the two dates.** A batch with a frozen date has its freezer time also when its
  storage area is not a freezer. The app sets the two dates each time that a batch moves into a freezer or out of a
  freezer, so the dates and the storage area agree.

## Decisions that the owner confirmed

The first answers of the owner did not include these points. Each decision here is the more careful option, as in
ADR 0013. The owner saw them with the app and said that they are valid (answer 4).

- **Thawed food does not go into a freezer again.** The freeze check does not permit a batch with a thawed date. The
  Food Standards Agency says not to freeze raw food again after it is defrosted, and the app does not know if the
  person cooked the food. Without this rule, a thawed batch could get a new freezer time on the day after it was
  thawed.
- **A frozen batch and a thawed batch get no later-date offer.** A chosen date is an expiry date, and it cannot move
  a good-until date that comes from the frozen date or from the thawed date. An offer would have no effect, as for
  the opened date (ADR 0014). The reasons are `frozen` and `thawed`. The answer "Same thing for strict foods" is
  about the freeze check. It does not say if a strict food in a freezer gets "Still good?" at the end of its freezer
  time. With "Change date", the person selects a date for a batch in a freezer at each time, also for a strict food:
  frozen food stays safe, and the date is about quality.
- **A batch that the person adds to a freezer has no frozen date.** Its date is its expiry date, as before.

## The screens

- A batch that the freeze check permits has the button "Move to freezer". A batch in a freezer has the button "Move
  to fridge". Each button writes one change with the date of today, and its message has "Undo". When the inventory
  has more than one freezer or more than one fridge, the button opens a menu with their names.
- A batch that the freeze check does not permit has no "Move to freezer". The app does not show a control that does
  nothing.
- The edit form moves a batch as the buttons do. A form that moves a batch to a freezer gives it the frozen date of
  today. A form that moves a batch out of a freezer gives it the thawed date of today. The form says so before the
  person saves it.
- The edit form does not move a batch to a freezer when the freeze check does not permit it. The form says the
  reason. Before this decision, the form gave an expired batch with an estimated date the estimate for the freezer.
- The edit form is the place where the person removes the two dates. This is for a move that was a mistake, after
  "Undo" is gone. The batch then has its expiry date again. The person cannot enter a frozen date or a thawed date.
- A batch in a freezer has the button "Change date" when its date comes from its frozen date, or is a chosen date.
  The button opens the date picker with the date of the batch, and its message has "Undo". The button is not there
  while the batch has "Still good?", which selects a chosen date also.
- A frozen batch with the default freezer days has the line "General estimate for frozen food: 1 month. You can
  change the date."
- A frozen batch and a thawed batch keep a printed date on the card, below the new date. They do not keep an
  estimated date: an old estimate for the fridge has no use on a frozen batch.
- The Android app has these rules and these screens. The iOS app does not have them yet. On 18 November 2026 the
  owner said to do the Android app first. The iOS core gets the rules later, from `spec/` and from the commits of the
  Android app.

## What this changes in ADR 0014

ADR 0014 says that the freezer is not an exception for the later-date offer, because the core does not know when a
batch went into the freezer. Now the core knows this for a batch that the person moved to a freezer. Such a batch
gets no offer, with the reason `frozen`, or `strictFood` for a strict food. The lines of ADR 0014 stay for a batch
that the person added to a freezer.

## Results

- `spec/vectors/freeze-check.json` has the cases for rule 11. `good-until.json`, `later-date-offer.json`,
  `before-date-tips.json`, and `change-log.json` have new cases. The expected batches of all cases of
  `change-log.json` have `frozenDate` and `thawedDate`.
- A freeze tip (ADR 0015) shows only for a batch that the freeze check permits. A thawed batch thus shows no freeze
  tip.
- An earlier version of the app does not know the change types `batchFrozen` and `batchThawed`. The app has no users
  yet, so no conversion is necessary.
- The reminders use the days left, so they use the new dates with no change to their rules.

## Known limits

- After "Change date", the batch has no frozen date, and the card does not say when the batch was frozen. The date
  of the batch is then "Your date".
- The default freezer days are one value for each food with no days for the freezer. A food that does not freeze
  well, for example lettuce, gets the same 30 days.
- A batch that the person adds to a freezer with a printed date expires on that date in the freezer. This decision
  does not change that. Only a move sets the frozen date.
- A batch with a frozen date gets no later-date offer, but a check food that the person added to a freezer gets the
  offer at its estimated date, as before.
- When the person changes the storage kind of a storage area, the batches in it keep their dates. The app does not
  write a frozen date or a thawed date for them.
- The edit form does the freeze check for the batch as it is in the inventory. A person who corrects a wrong expiry
  date and moves the batch to a freezer must save the form two times.
- The thawed days are one value for each food. Food that is cooked from frozen, and food that is safe for more than
  1 day after it is thawed, gets the same 1 day.

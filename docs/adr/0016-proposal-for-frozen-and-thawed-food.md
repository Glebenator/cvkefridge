# Proposal: give thawed food a short time, and freeze food only up to its date

Status: a proposal. It is not agreed, and it is not built. `spec/rules.md` and the vectors do not have it. This is the
fourth part of the work that ADR 0013 starts. On 17 November 2026 the owner said to build it, but the rule did not
stay small, and it needs decisions of the owner. This document has the options.

## The problem

- A batch that moves from a freezer storage area to a fridge storage area keeps its expiry date. That date can be an
  estimate for the freezer, which is months away. The app then shows thawed chicken as fresh for months.
- A batch can move to a freezer after its date. The app then shows spoiled food as good frozen food.

## What the sources say

- The Food Standards Agency: "Once the food has been defrosted, you need to use it within 24 hours" (GOV.UK,
  "Understanding food labelling: Best before and use-by dates"), and food can go into the freezer "right up until
  midnight" on its use-by date ("How to chill, freeze and defrost food safely"). We opened the two pages on 17
  November 2026.
- The expiry research ([expiry-dates.md](../research/expiry-dates.md), section 4): EFSA gives 24 hours for food that
  was frozen for donation. ANSES says to eat thawed food in three days. One guideline of Ireland permits 3 days.
- The FoodKeeper data has a time "after thawing" for 3 of its 661 foods: chicken nuggets (1 day), frozen edamame (7
  days), and frozen polenta (5 days).

## Why the rule is not small

- A move is a `batchEdited` change today. The change does not say that the batch came out of a freezer. The replay
  can find it only when it compares the storage kinds of the old area and the new area, and a storage area can get a
  different kind in a later change.
- The expiry date of the package does not apply while the batch is frozen, and it does not apply again after the
  batch is thawed. The batch thus needs the date on which it was frozen, the date on which it was thawed, or the
  two, and the good-until date (rule 5.2) needs lines for them.
- The rule must agree with the opened date (ADR 0013) and with the later-date offer (ADR 0014). Example: a strict
  food in a freezer could get the offer when the core knows that it was frozen before its date.
- The sources give 1 day and 3 days for the same case.

## Options

- **A. Two changes and two dates.** `batchFrozen` and `batchThawed` each have the batch, the new storage area, and a
  date. The batch gets `frozenDate` and `thawedDate`. Rule 5.2 gets two lines:
  - A batch with a frozen date and no thawed date has the frozen date plus the days of the food for the freezer, with
    the source `frozen`. The printed date does not apply. A food with no days for the freezer has no good-until date.
  - A batch with a thawed date has the thawed date plus the thawed days, with the source `thawed`. The thawed days
    are the value of the table of foods (`thawedDays`, for the 3 foods of the source), and 1 day for each other food.
  - `batchFrozen` is rejected when its date is after the good-until date of the batch. The replay then needs the
    table of foods, or the check is a rule of the app and not of the replay.
- **B. No new change.** The replay compares the storage kinds of each `batchEdited` change and sets the two dates
  itself, from the date of the instant of the change. The core then needs the UTC offset of each change, which a
  change does not have today.
- **C. A rule of the app only.** When the person moves a batch from a freezer to a fridge, the app writes a
  `batchEdited` change with an estimated date of today plus 1 day. When the person moves an expired batch to a
  freezer, the app does not permit it. The core has no new value, and the screens cannot show "thawed" later.

## Recommendation

Option A, with 1 day for thawed food. It is the careful value, and it is the value of the Food Standards Agency. The
two dates are facts about the batch, as the opened date is. The check of `batchFrozen` against the good-until date is
a rule of the core that the app calls before it writes the change, as the later-date offer is. The replay does not
reject the change.

## What the owner has to decide

1. Option A, B, or C.
2. The time for thawed food: 1 day for each food, or 3 days for food that is cooked before it is eaten.
3. If the person can freeze a batch after its date when its after-date class is `check`, for example bread.
4. If a strict food that was frozen on or before its date gets the later-date offer while it is in the freezer.

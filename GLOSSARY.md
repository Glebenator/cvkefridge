# CVKE Fridge

The shared terms of the Android app and the iOS app. This is the second draft, after the decisions of 10 November 2026
in [the plan](docs/plan.md). The owner agrees the words in milestone 1. Household sharing is deferred, so its terms
are not here. The terms Home, My Fridge, and Food are from 11 November 2026 (ADR 0006). The terms for opened food,
for the date type, for the food after its date, and for the before-date tips are from 17 November 2026 (ADR 0013,
ADR 0014, ADR 0015). The terms for frozen and thawed food are from 18 November 2026 (ADR 0016).

## Inventory

**Inventory**:
All the **batches** on the phone that are not ended.
_Avoid_: Fridge (the Fridge is one **storage area**), list, stock

**Product**:
What a food is: its name, its **category**, and its optional **barcode**, photo, **note**, and **storage text**. A
product has no quantity and no date.
_Avoid_: Item, food type

**Note**:
A text that the person writes about a **product**, for example "Opened on Sunday". A product has one note or no note.
All **batches** of the product show the same note.
_Avoid_: Comment, description, memo

**Batch**:
One purchase of a **product**: its **quantity**, its **storage area**, its **date added**, and its optional
**expiry date** and **opened date**. One **product** can have more than one batch. A batch is active while its
quantity is above 0. After that it is ended.
_Avoid_: Item, fridge item, entry, lot

**Quantity**:
How much there is of a **batch**: a number in the **unit** of its **product**. The apps keep it as whole thousandths.
_Avoid_: Count, amount

**Unit**:
The measure of the **quantities** of a **product**: pcs, g, kg, ml, l, pack, bottle, slice, cup, or none. All
**batches** of a product have the same unit.

**Category**:
The food group of a **product**. There are 13: produce; dairy & eggs; meat & fish; condiment; beverage; bakery;
pasta, rice & grains; canned & jarred; baking & spices; snacks & sweets; ready meals & deli; leftovers; and other.
Leftovers is food that the person cooked at home. Frozen is not a category: it is a **storage kind**. The category is
for groups and filters. It gives the **after-date class** of a product that has no food of the table. It does not give
the **expiry estimate**.
_Avoid_: Type, tag

**Storage area**:
A place where a **batch** is kept. Fridge and Freezer are fixed. The person can create more. Each storage area has a
**storage kind**.
_Avoid_: Area, location, zone

**Storage kind**:
How a **storage area** keeps food: pantry, fridge, or freezer. The **expiry estimate** of a food is different for
each kind.
_Avoid_: Temperature, type

**Usual storage kind**:
The **storage kind** where people usually keep a food of the table of foods when they bring it home. The add form uses
it to select a **storage area** for the food.
_Avoid_: Default location, home

**Date added**:
The calendar date on which the **batch** came into the **inventory**.
_Avoid_: Timestamp, created date

## Freshness

**Expiry date**:
The calendar date after which the **batch** is not good to eat, while its package is not opened. It has no time of
day and no time zone. It is a **printed date**, an **estimated date**, or a **chosen date**.
_Avoid_: Expiration, expires on. "Use by" and "best before" are **date types**, not other words for the expiry date.

**Printed date**:
An **expiry date** from the package, which the person entered. It can have a **date type**.
_Avoid_: Real date, exact date

**Date type**:
What the words on the package say about a **printed date**: use by, or best before. A printed date with no date type
has a type that the app does not know. An **estimated date** and a **chosen date** have no date type.
_Avoid_: Label type, date kind, date label

**Use-by date**:
A **printed date** with the **date type** use by. It is about safety: after it, the food is not safe to eat, and the
person cannot see, smell, or taste the danger. The "expiration date" on infant formula and on meal replacements is
also a use-by date.
_Avoid_: Safety date, expiry (for the label)

**Best-before date**:
A **printed date** with the **date type** best before. It is about quality: after it, the food can be less good, and
many foods are still good to eat.
_Avoid_: Quality date, sell by, display until, BBE

**Opened date**:
The calendar date on which the person opened the package of a **batch**. A batch has one opened date or none.
_Avoid_: Open date, date opened, opening date

**Opened days**:
The number of days that a food stays good after its package is opened, in a **storage kind**, from the table of
foods. A food can have no opened days.
_Avoid_: Open life, period after opening, time after opening

**After-opening date**:
The **opened date** of a **batch** plus the **opened days** of its food for the **storage kind** of its **storage
area**. The app shows it as an estimate.
_Avoid_: Opened expiry, open date

**Frozen date**:
The calendar date on which the person moved a **batch** to a freezer. A batch has one frozen date or none. A batch
that the person adds to a freezer has none.
_Avoid_: Freeze date, date frozen

**Thawed date**:
The calendar date on which the person moved a **batch** out of a freezer. A batch has one thawed date or none.
_Avoid_: Defrost date, date thawed

**Thawed days**:
The number of days that a **batch** stays good after its **thawed date**. It is 1 for each food.
_Avoid_: Defrost time, time after thawing

**Default freezer days**:
The number of days in the freezer for a frozen **batch** of a food with no **expiry estimate** for the freezer. It
is 30. A frozen batch thus has a **good-until date** for each food.
_Avoid_: Fallback time, standard freezer time

**Freeze check**:
The rule that says if a **batch** can go into a freezer. A batch can go into a freezer up to its **good-until date**
and on that date. A batch with a **thawed date** cannot go into a freezer again.
_Avoid_: Freeze rule, freezer validation

**Good-until date**:
The calendar date that the app uses for the **days left**, the **freshness**, and the **use-first list** of a
**batch**. For a batch with a **thawed date**, it is that date plus the **thawed days**. For a batch with a **frozen
date** and no thawed date, it is that date plus the **expiry estimate** of its food for the freezer, or plus the
**default freezer days**. For each other
batch, it is the earlier of its **expiry date** and its **after-opening date**. The app calculates it each time. The
app does not store it.
_Avoid_: Effective date, real expiry date, final date

**Estimated date**:
An **expiry date** that the app suggested from the **expiry estimate**. The app shows it as an estimate.
_Avoid_: Default date, guess

**Chosen date**:
A later **expiry date** that the person selected because the food is still good after its **printed date** or its
**estimated date**. It is not from the package and not from the table of foods. The app shows it as "Your date".
_Avoid_: Extended date, new date, override

**Expiry estimate**:
The number of days that a food stays good in a **storage kind**, from the table of foods. The app adds it to the
**date added** to get an **estimated date**.
_Avoid_: Shelf life (the old rule with eight categories), lifetime

**Days left**:
The number of calendar days from today to the **good-until date**. Today is the date in the time zone of the device.
It is 0 on the good-until date and negative after it.
_Avoid_: Days remaining, time left

**Freshness**:
The state of a **batch** that its **days left** give: fresh, expiring, expired, or no expiry date. The app calculates
it each time. The app does not store it.
_Avoid_: Status, condition

**After-date class**:
What the table of foods says about a food after its date: strict or check. A strict food is not good to eat after its
date, and the person cannot see, smell, or taste if it is safe: raw meat, fish, soft cheese, and prepared food are
examples. A check food is often still good after its date, and the person can look at it, smell it, and taste it:
bread, hard cheese, and jam are examples.
_Avoid_: Risk class, safety class, perishable

**Later-date offer**:
The controls of "Still good?" that let the person select a **chosen date** for a **batch**. The app shows them only
when the rule for the offer permits it.
_Avoid_: Extend, snooze, postpone

**Before-date tip**:
A short text from a named source about what to do with a food before its date: freeze it, cook it, or use it up. The
app shows it only while the **batch** is expiring. It is not advice for expired food.
_Avoid_: Rescue tip, recipe, hack. **Storage tips** say how to keep a food. They are not before-date tips.

**Use-first list**:
The **batches** of the **inventory**, with the earliest **good-until date** first. **Home** shows the start of it.
_Avoid_: Dashboard

**Home**:
The first screen of the app. It shows the totals of the **inventory**, and the first expired and expiring
**batches**.
_Avoid_: Dashboard, start screen

**My Fridge**:
The second screen of the app. It has one card for each **food** in each **storage area**. The name is the name of the
screen in FridgeFriend.
_Avoid_: All food, list

**Food**:
In the interface, a **product** with an active **batch**. The number of foods counts products, not batches. The text
of **Home** says "items", because it is the text of FridgeFriend (ADR 0006).
_Avoid_: Item, in code and in documents

**Reminder**:
A notification that the phone shows before a **batch** expires. The phone calculates it from its own copy of the
**inventory**.
_Avoid_: Alert, push

## The end of a batch

**Used**:
The end of a **batch**, or of a part of its **quantity**, because somebody ate it or cooked with it.
_Avoid_: Consumed, finished, taken out

**Thrown away**:
The end of a **batch**, or of a part of its **quantity**, because nobody used it.
_Avoid_: Wasted, discarded, binned

**History**:
The **batches** that ended, with **used** or **thrown away** for each.
_Avoid_: Archive, log

**Delete**:
To remove a **batch** or a **product** that was a mistake. A deleted batch is not in the **history**.
_Avoid_: Remove (when the food was used or thrown away)

## Product lookup

**Barcode**:
The number on a package: 8, 12, 13, or 14 digits.
_Avoid_: Code, UPC, EAN (use them only for the specific formats)

**Scan**:
To read a **barcode** with the phone camera.
_Avoid_: Capture, detect

**Product lookup**:
The request that gets a product name, a **category**, and a **storage hint** for a **barcode** from Open Food Facts.
_Avoid_: Search, barcode fetch

**Lookup pause**:
The 5 minutes after a failure of Open Food Facts in which the app sends no **product lookup** by itself. A **scan**
then opens the add form at once, with the **barcode** and no values from Open Food Facts.
_Avoid_: Offline mode, cooldown, circuit breaker

**Storage text**:
The text on the package about how to keep the product, for example "Store at -18°C". The **product lookup** gets it
from Open Food Facts, and the **product** keeps it. The person does not write it.
_Avoid_: Conservation conditions, storage instructions

**Storage tips**:
What the app shows about how to keep a food: the **storage text** of the product, with a check mark and the words
"From the package", and the **general advice** for the food.
_Avoid_: Storage guide, recommendations

**General advice**:
The part of the **storage tips** that comes from the table of foods: the **usual storage kind**, the time that the
food keeps in each **storage kind**, and the tip of the table for a storage kind. It is about the food in general, not
about one **product**.
_Avoid_: Generic tip, default advice

**Storage hint**:
The **storage kind** that the **product lookup** gives for a product, from its **storage text** or from its category
tags. The add form uses it before the **usual storage kind** to select a **storage area**.
_Avoid_: Storage guess, default storage

## Change log

**Change**:
One record of the change log: one thing that the person did to the **inventory**, and when.
_Avoid_: Event, edit, operation

**Replay**:
The calculation of the **inventory** from all **changes**, in the order of their time.
_Avoid_: Rebuild, sync

**Undo**:
A **change** that names an earlier change. The **replay** then skips the earlier change.
_Avoid_: Revert, rollback

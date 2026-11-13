# CVKE Fridge

The shared terms of the Android app and the iOS app. This is the second draft, after the decisions of 10 November 2026
in [the plan](docs/plan.md). The owner agrees the words in milestone 1. Household sharing is deferred, so its terms
are not here. The terms Home, My Fridge, and Food are from 11 November 2026 (ADR 0006).

## Inventory

**Inventory**:
All the **batches** on the phone that are not ended.
_Avoid_: Fridge (the Fridge is one **storage area**), list, stock

**Product**:
What a food is: its name, its **category**, and its optional **barcode** and photo. A product has no quantity and no
date.
_Avoid_: Item, food type

**Batch**:
One purchase of a **product**: its **quantity**, its **storage area**, its **date added**, and its optional
**expiry date**. One **product** can have more than one batch. A batch is active while its quantity is above 0. After
that it is ended.
_Avoid_: Item, fridge item, entry, lot

**Quantity**:
How much there is of a **batch**: a number in the **unit** of its **product**. The apps keep it as whole thousandths.
_Avoid_: Count, amount

**Unit**:
The measure of the **quantities** of a **product**: pcs, g, kg, ml, l, pack, bottle, slice, cup, or none. All
**batches** of a product have the same unit.

**Category**:
The food group of a **product**: produce, dairy, meat, condiment, beverage, bakery, leftovers, or other. It is for
groups and filters. It does not give the **expiry estimate**.
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
The calendar date after which the **batch** is not good to eat. It has no time of day and no time zone. It is a
**printed date**, an **estimated date**, or a **chosen date**.
_Avoid_: Expiration, best before, use by, expires on

**Printed date**:
An **expiry date** from the package, which the person entered.
_Avoid_: Real date, exact date

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
The number of calendar days from today to the **expiry date**. Today is the date in the time zone of the device. It is
0 on the expiry date and negative after it.
_Avoid_: Days remaining, time left

**Freshness**:
The state of a **batch** that its **days left** give: fresh, expiring, expired, or no expiry date. The app calculates
it each time. The app does not store it.
_Avoid_: Status, condition

**Use-first list**:
The **batches** of the **inventory**, with the fewest **days left** first. **Home** shows the start of it.
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
The request that gets a product name and a **category** for a **barcode** from Open Food Facts.
_Avoid_: Search, barcode fetch

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

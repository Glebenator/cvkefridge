# CVKE Fridge

The shared terms of the Android app and the iOS app. This is the second draft, after the decisions of 10 November 2026
in [the plan](docs/plan.md). The owner agrees the words in milestone 1. Household sharing is deferred, so its terms
are not here.

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
**expiry date**. One **product** can have more than one batch.
_Avoid_: Item, fridge item, entry, lot

**Quantity**:
How much there is of a **batch**: a number with an optional **unit**.
_Avoid_: Count, amount

**Unit**:
The measure of a **quantity**: pcs, g, kg, ml, l, pack, bottle, slice, or cup.

**Category**:
The food group of a **product**: produce, dairy, meat, condiment, beverage, bakery, leftovers, or other. It is for
groups and filters. It does not give the **expiry estimate**.
_Avoid_: Type, tag

**Storage area**:
A place where a **batch** is kept. Fridge and Freezer are fixed. The person can create more.
_Avoid_: Area, location, zone

**Date added**:
The calendar date on which the **batch** came into the **inventory**.
_Avoid_: Timestamp, created date

## Freshness

**Expiry date**:
The calendar date after which the **batch** is not good to eat. It has no time of day and no time zone. It is a
**printed date** or an **estimated date**.
_Avoid_: Expiration, best before, use by, expires on

**Printed date**:
An **expiry date** from the package, which the person entered.
_Avoid_: Real date, exact date

**Estimated date**:
An **expiry date** that the app suggested from the **expiry estimate**. The app shows it as an estimate.
_Avoid_: Default date, guess

**Expiry estimate**:
The number of days that a food stays good in a **storage area**, from the table of foods. The app adds it to the
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
The **batches** of the **inventory**, with the fewest **days left** first. It is the first screen of the app.
_Avoid_: Home, dashboard

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

# CVKE Fridge

The shared terms of the Android app and the iOS app. This is a first draft from the FridgeFriend code. Each term that
replaces an old word names that word after _Avoid_. The owner agrees the terms in milestone 1 of
[the plan](docs/plan.md).

## Inventory

**Item**:
One food in the inventory, with a name, a quantity, a **category**, a **storage area**, and an optional
**expiry date**.
_Avoid_: Fridge item, product, entry

**Quantity**:
How much there is of an **item**: a number with an optional **unit**.
_Avoid_: Count, amount

**Unit**:
The measure of a **quantity**: pcs, g, kg, ml, l, pack, bottle, slice, or cup.

**Category**:
The food group of an **item**: produce, dairy, meat, condiment, beverage, bakery, leftovers, or other. The category
and the **storage area** give the **shelf life**.
_Avoid_: Type, tag

**Storage area**:
A place where an **item** is kept. Fridge and Freezer are fixed. The person can create more.
_Avoid_: Area, location, zone

**Date added**:
The calendar date on which the **item** came into the inventory.
_Avoid_: Timestamp, created date

## Freshness

**Expiry date**:
The calendar date after which the **item** is not good to eat. It has no time of day and no time zone.
_Avoid_: Expiration, best before, use by, expires on

**Days left**:
The number of calendar days from today to the **expiry date**, in the time zone of the device. It is 0 on the expiry
date and negative after it.
_Avoid_: Days remaining, time left

**Freshness**:
The state of an **item** that its **days left** give: fresh, expiring, expired, or no expiry date. The app calculates
it each time. The app does not store it.
_Avoid_: Status, condition

**Shelf life**:
The default number of days that a **category** stays good in a **storage area**. The app uses it to suggest an
**expiry date**.
_Avoid_: Lifetime, duration

## Sessions

**Fridge device**:
The hardware in the fridge that detects the food that goes in and comes out, and sends **sessions** to the app.
_Avoid_: Sensor, camera, hardware, Pi

**Session**:
The **detections** of one use of the fridge, which the **fridge device** sends as one message.
_Avoid_: Event, batch, scan

**Detection**:
One food that the **fridge device** saw in a **session**, with an **action** and a **confidence**.
_Avoid_: Session item, item (an **item** is in the inventory; a detection is a report from the device)

**Action**:
The direction of a **detection**: put in, or taken out.
_Avoid_: In/out, direction, type

**Confidence**:
How sure the **fridge device** is of a **detection**, from 0 to 1.
_Avoid_: Score, accuracy

**Review**:
The step in which the person reads the **detections** of a **session** and corrects them.
_Avoid_: Verify, check

**Approve**:
To apply a **session** to the inventory. A "put in" **detection** adds a **quantity** or creates an **item**. A "taken
out" **detection** removes a **quantity**. An approved session does not change again.
_Avoid_: Process, verify, confirm, accept

## Product lookup

**Barcode**:
The number on a package: 8, 12, 13, or 14 digits.
_Avoid_: Code, UPC, EAN (use them only for the specific formats)

**Product lookup**:
The request that gets a product name and a **category** for a **barcode** from Open Food Facts.
_Avoid_: Scan, search, barcode fetch

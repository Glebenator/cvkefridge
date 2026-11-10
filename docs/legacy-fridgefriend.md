# FridgeFriend: what the old app does

Date: 10 November 2026. Source: the FridgeFriend code (`basic_ff`, Expo 54, React Native 0.81) at its commit of
25 March 2026. This document records behaviour. It is the reference for the rewrite, not a specification. The values
here are the values in the old code. [The plan](plan.md) says which of them change.

The rewrite has no fridge device ([ADR 0002](adr/0002-use-one-phone-and-no-fridge-device.md)). The sections on
sessions are a record only.

## Screens

| Screen | Contents |
|---|---|
| Home | A greeting, the totals (items, expiring, expired), a banner with the number of detections that are not verified in sessions that are not approved, up to five expiring or expired items (fewest days left first), and the last four sessions. |
| My Fridge | The item list with chips for storage area and category, a search field, and a sort control. A long press opens Edit and Delete. Delete has an undo for 4 seconds. |
| Item | Name, notes, quantity, category, storage area, expiry date, photo, and barcode. Each edit saves at once. |
| Add item, Edit item | One form. Save needs a name and a quantity above 0. A change of category or storage area fills the expiry date from the shelf-life default, unless the person set a date. |
| Sessions | The sessions that are not approved, with a switch to show the approved sessions, and a sort control. |
| Session | The detections of one session, the count of items in and out, and Approve session. Each detection can be edited or deleted. |
| Settings | Theme (system, light, dark), card style (seven styles), storage areas, and the switch for the live feed from the fridge device. |

## Data

**Item**: id, name, quantity, unit (optional), category, storage area, date added, expiry date (optional), notes,
barcode, photo.

- Units: pcs, g, kg, ml, l, pack, bottle, slice, cup.
- Categories: produce, dairy, meat, condiment, beverage, bakery, leftovers, other.
- Storage areas: Fridge and Freezer are fixed. The person can create more. A name has 2 to 24 characters and is unique
  without regard to case. A storage area with items cannot be deleted.

**Session**: id, time, detections, and a flag for approved. A deleted session stays in the database with a deleted
flag, so that the device cannot send it again.

**Detection**: id, name, action (in or out), time, confidence (a number, which the app does not check), a verified flag, and the optional fields
barcode, category, storage area, quantity, unit, expiry date, and notes.

Storage is one SQLite database with the tables `fridge_items`, `sessions`, `session_items`, and `storage_areas`. The
schema is at version 7. Photos are files in the app folder.

## Rules

**Days left** = expiry date minus today, in days. Both dates are cut to midnight UTC.

| Days left | Freshness |
|---|---|
| No expiry date | No expiry |
| Below 0 | Expired |
| 0 to 2 | Expiring |
| 3 or more | Fresh |

**Shelf-life defaults, in days**

| Category | Fridge | Freezer |
|---|---|---|
| Produce | 7 | 90 |
| Dairy | 14 | 30 |
| Meat | 5 | 120 |
| Condiment | 180 | 240 |
| Beverage | 30 | 60 |
| Bakery | 5 | 30 |
| Leftovers | 4 | 60 |
| Other | 30 | 60 |

A storage area that the person created uses the Fridge value.

**Sort orders**: name (A to Z), expiry date (soonest first, the start order), date added (newest first), quantity
(largest first), category (A to Z). An item without a date is last in each direction.

**Quantity steps**: 0.5 for kg and l. For g and ml: 10 below 100, 25 from 100 to 499, 50 from 500. 1 for the other
units. The minus button stops at 0.5. A typed quantity can be any number above 0.

## Sessions from the fridge device

The device publishes each session as one JSON message over MQTT (WebSocket transport, default port 9001, path `/mqtt`,
topic `fridge/sessions`, QoS 1). The app looks for the broker at the configured host, and then at three `.local` host
names on the local network. The feed runs only while the app is open.

The feed is off at start. The person can switch it on only when the app configuration has a broker host, and the
shipped configuration has none. The app keeps one client id and asks the broker for a persistent session, so the
broker can keep messages while the app is closed.

This example shows the shape of a message. Its values are samples.

```json
{
  "id": "s1",
  "timestamp": "2026-03-25T18:04:00Z",
  "items": [
    { "id": "d1", "name": "Milk", "action": "in", "timestamp": "2026-03-25T18:04:02Z", "confidence": 0.92,
      "barcode": null, "category": "dairy", "storageAreaId": "fridge", "quantity": 1, "unit": "bottle" }
  ]
}
```

A session needs an id, a time, and one detection or more. A detection needs an id, a name, an action ("in" or "out"),
and a time. A detection id must be unique across all stored sessions, or the save fails. A session can also have a
`processed` flag. The app does not check the confidence range or the time format.

**On arrival**

1. The app ignores a session that the person deleted.
2. A detection name of 8, 12, 13, or 14 digits is a barcode. The app looks up the product and replaces the name and the
   category. A failed lookup replaces the category from the device with "other".
3. The app stores the session. A session with the same id replaces the stored session and its detections. The edits of
   the person are lost. An approved session becomes not approved, unless the message has `"processed": true`. The
   person can then approve it again, and its changes apply two times.

**On approval**

- A match is an item with the same barcode, else the same name without regard to case, else a name that contains the
  other name. If some matches have the same unit, only those count. Matches in the same storage area come first, then
  the oldest.
- A detection with the action "in" adds an item. The quantity is 1 when the device sends none. If an item matches, the
  app asks: add the quantity to that item, or create a new item. A new item gets no expiry date from the shelf-life
  defaults.
- A detection with the action "out" takes the quantity from the oldest matching item, and then from the next. The
  quantity is rounded to a whole number, 1 at the minimum. The app asks when more than one item matches, or when an
  item would become empty. Without a match, the app reports that the person must remove the quantity by hand.
- The changes are not one transaction. If the person cancels a question, the earlier changes stay and the session
  stays not approved. A second approval applies them again.

## Product lookup

Open Food Facts API v2, `GET /api/v2/product/<barcode>.json`, with the fields for product name, generic name, brand,
category tags, and category hierarchy. The name becomes "brand product name". Each category has a group of words. A
group matches when one of its words occurs anywhere in the tags, also inside a longer word. The first group that
matches gives the category, in this order: produce, dairy, meat, beverage, condiment, bakery, leftovers, and then
other. Results stay in memory for
24 hours. A failed lookup gives "Product <barcode>" in the category "other", and this result also stays for 24 hours.

The app has no camera barcode scanner. A barcode comes only from the fridge device.

## Not in the old app

Notifications, a barcode scanner, cloud sync, accounts, and work in the background.

## Known defects and loose ends

- The code stores the local date as midnight UTC, and it cuts today in UTC. The days left are then wrong by one for as
  many hours each day as the UTC offset of the device.
- The app adds six sample items when My Fridge loads with no items, and two sample sessions at start when no session
  is left. Deleted samples come back. The released app does this also.
- A session that arrives again replaces the edits of the person and cancels an approval.
- Approval can stop in the middle and leave a part of its changes.
- A failed product lookup is kept for 24 hours.
- The words "processed", "approved", and "verified" name one session state. A detection has its own "verified" flag,
  and approval does not use it.
- The fridge list has seven card styles. The session cards have three.
- Storage areas cannot be renamed on Android.
- One screen and one set of filter controls are not used.

# Core rules

These are the product rules that both apps implement in their core modules: `:core` on Android and `CVKEFridgeCore`
on iOS. The files in `vectors/` give inputs and expected results for each rule. If this text and a vector disagree,
that is a defect in this folder. Correct it here first.

## 1. Values

- **Identifier.** A text of 1 to 64 characters from `a` to `z`, `0` to `9`, and `-`. Identifiers are compared
  character by character. The apps make random identifiers.
- **Calendar date.** A year, a month, and a day in the Gregorian calendar. The year is 1 to 9999. The text form is
  `YYYY-MM-DD` with 10 characters.
- **Instant.** A whole number of milliseconds from 1970-01-01T00:00:00Z.
- **Quantity.** A whole number of thousandths. `1500` is 1.5. The core does no arithmetic with fractions.
- **Unit.** `pcs`, `g`, `kg`, `ml`, `l`, `pack`, `bottle`, `slice`, `cup`, or none. The unit belongs to the product.
  All batches of a product have the same unit.
- **Note.** A text that the person writes about a product, or none. The core keeps the text as it is. It does not
  remove spaces and it has no maximum length. The app saves none in place of an empty text.
- **Storage text.** The text on the package about how to keep a product, or none. The core keeps the text as it is.
  The app gets it from the product lookup, and the person does not write it.
- **Category.** `produce`, `dairy`, `meat`, `condiment`, `beverage`, `bakery`, `leftovers`, or `other`.
- **Storage kind.** `pantry`, `fridge`, or `freezer`. Each storage area has one kind.
- **Date type.** `useBy`, `bestBefore`, or none. It is what the words on the package say about a printed expiry date.
  None means that the app does not know the type.
- **After-date class.** `strict` or `check`. It says if a food can be good after its date (rule 9.1).

## 2. Calendar dates

- **Parse.** A text is a date only if it has exactly 10 characters, a `-` at positions 5 and 8, a digit at each other
  position, a year from 0001, a month from 01 to 12, and a day that the month has. February has 29 days in a year that
  divides by 4, but not in a year that divides by 100, unless the year divides by 400. No other text is a date. Spaces
  are not removed.
- **Add days.** A date plus a whole number of days is the date that many days later, or earlier for a negative number.
  If the result is before year 1 or after year 9999, there is no result.
- **Days between.** The days from date A to date B are positive when B is later.
- **Order.** An earlier date is less than a later date.
- **Date of an instant.** The date of an instant at a UTC offset in seconds is the day number
  `floor((milliseconds + offset * 1000) / 86400000)` counted from 1970-01-01. The division rounds down for negative
  numbers also. The app gives the instant and the offset of the device time zone at that instant.

## 3. Freshness

- **Days left** are the days from today to the good-until date of the batch (rule 5.2). A batch with no good-until
  date has no days left. For a batch with no opened date, the good-until date is the expiry date.
- **Freshness** from the days left:

| Days left | Freshness |
|---|---|
| None | `noExpiryDate` |
| Below 0 | `expired` |
| 0, 1, or 2 | `expiring` |
| 3 or more | `fresh` |

## 4. Expiry estimate

- The table of foods is `foods.json`. Each food has an identifier, a name, a category, and a number of days for each
  storage kind in which the food can be kept. A storage kind can be absent.
- The estimated date for a food, a storage kind, and a date added is the date added plus the days for that kind. Its
  source is `estimated`.
- If the food is not in the table, or the food has no days for that kind, there is no estimate. The core does not use
  the category to make an estimate.
- A food can have a **usual storage kind**: the storage kind where people usually keep the food when they bring it home.
  It can be absent. It can be a kind for which the food has no days, for example milk that keeps until the date on the
  package. `tools/build-foods.py` has the rule that sets it. The usual storage kind gives no estimate.
- A food can have **tips**: for a storage kind, a short text of the source about how to keep the food in that kind.
  A food can have a tip for a kind for which it has no days. `tools/build-foods.py` has the rule that sets them. The
  tips give no estimate.
- A food can be **common**: a food that people add often. A food can have **aliases**: other names for the food, in
  lowercase. `tools/food-extras.json` has them. They are for the suggestions of the add form, and they give no
  estimate.
- A food can have **opened days** (`openedDays`): for a storage kind, the number of days that the food stays good
  after its package is opened. The table has opened days for the pantry and for the fridge only. A food with no
  `openedDays` key has none. `tools/build-foods.py` has the rule that sets them. Rule 5.2 uses them.
- A food has an **after-date class** (`afterDate`): `strict` or `check`. `tools/food-classes.json` has the classes,
  and `tools/build-foods.py` adds them. A food with no `afterDate` key is `strict`. Rule 9 uses the class.

## 5. Batches, the good-until date, and the use-first order

### 5.1 Batches

- A batch is **active** when its quantity is above 0. A batch with a quantity of 0 is **ended**.
- An expiry date has a source: `printed`, `estimated`, or `chosen`. A batch has both the date and the source, or none of
  the two.
  - `printed`: the date on the package, which the person entered.
  - `estimated`: the date from the table of foods (rule 4).
  - `chosen`: a later date that the person selected because the food is still good after its printed or estimated
    date. It is not from the package and not from the table.
- A batch can have a **date type** (`dateType`): `useBy` or `bestBefore`. Only a batch with the source `printed` can
  have one. A printed date with no date type has a type that the app does not know.
- A batch can have an **opened date** (`openedDate`): the calendar date on which the person opened the package. It
  can be before the date added. A batch with no expiry date can have an opened date.

### 5.2 The good-until date

The good-until date is the date that the days left (rule 3), the use-first order (5.3), and rules 9 and 10 use. The
core calculates it each time. No change and no batch has it.

1. Find the opened days of the batch: the opened days of the food of its product (rule 4) for the storage kind of its
   storage area. There are none when the product has no food, when the food is not in the table, or when the food has
   no opened days for that kind.
2. The **after-opening date** is the opened date plus the opened days. There is none when the batch has no opened
   date, when the batch has no opened days, or when the result is after year 9999.
3. If there is an after-opening date, and the batch has no expiry date or the after-opening date is earlier than the
   expiry date, the good-until date is the after-opening date. Its source is `opened`.
4. In each other case, the good-until date is the expiry date, with the source of the expiry date. A batch with no
   expiry date then has no good-until date and no source.

The source of a good-until date is thus `printed`, `estimated`, `chosen`, or `opened`. A date with the source `opened`
is an estimate, and the app shows it as an estimate. When the two dates are the same, the source is the source of the
expiry date. The rule has no exception for a chosen date: an after-opening date that is earlier than a chosen date
comes first.

### 5.3 The use-first order

The **use-first order** of active batches:

1. A batch with a good-until date comes before a batch without one.
2. The earlier good-until date comes first. The source of the date has no effect.
3. Then the earlier date added comes first.
4. Then the smaller batch identifier comes first.

## 6. Plan a use

To use or throw away a quantity of a product, the core makes a plan from the active batches of that product, in the
use-first order.

- The plan takes from the first batch. When that batch has not enough, the plan takes all of it and continues with the
  next batch.
- The **shortfall** is the quantity that the batches could not give. It is 0 when the batches had enough.
- A quantity of 0 or less gives an empty plan with a shortfall of 0.

## 7. The change log

The inventory is the result of the change log. A change has an identifier, an instant, the identifier of the phone
that made it, and a body with a type.

### 7.1 Replay

1. Sort the changes by instant, and then by identifier.
2. If two changes have the same identifier, keep the first and drop the others.
3. Find the changes that are undone (7.3).
4. Start with no products, no batches, no history, and the two fixed storage areas: `fridge` (name `Fridge`, kind
   `fridge`) and `freezer` (name `Freezer`, kind `freezer`).
5. Apply each change in order. Skip a change that is undone. If a change cannot apply, record it as rejected with its
   reason, and continue.

### 7.2 Change types

| Type | Fields | Effect | Rejected when |
|---|---|---|---|
| `productSaved` | `product` (identifier, name, category, unit, barcode, food, note, storage text) | Adds the product, or replaces the product with the same identifier. A product with no `note` key has no note, and a product with no `storageText` key has no storage text: changes from before these values do not have the keys. | Never |
| `productDeleted` | `productId` | Removes the product, its batches, and the history of those batches. | `unknownProduct` |
| `storageAreaSaved` | `area` (identifier, name, kind) | Adds the storage area, or replaces the one with the same identifier. | `fixedStorageArea`: the identifier is `fridge` or `freezer` |
| `storageAreaDeleted` | `storageAreaId` | Removes the storage area. | `fixedStorageArea`, `unknownStorageArea`, or `storageAreaInUse`: an active batch is in it. The checks are in this order. |
| `batchAdded` | `batch` (identifier, product, quantity, storage area, date added, expiry date, expiry source, date type, opened date) | Adds the batch. A batch with no `dateType` key has no date type, and a batch with no `openedDate` key has no opened date: changes from before these values do not have the keys. | `duplicateBatch`, `unknownProduct`, `unknownStorageArea`, or `invalidQuantity`: the quantity is 0 or less. The checks are in this order. |
| `batchEdited` | `batchId`, `quantity`, `storageAreaId`, `dateAdded`, `expiryDate`, `expirySource`, `dateType`, `openedDate` | Replaces these values of the batch. A change with no `dateType` key gives the batch no date type, and a change with no `openedDate` key gives the batch no opened date. It makes no history. It can make an ended batch active again. | `unknownBatch`, `unknownStorageArea`, or `invalidQuantity`: the quantity is 0 or less. The checks are in this order. |
| `batchOpened` | `batchId`, `date` | Sets the opened date of the batch to the date, or replaces the opened date that the batch has. It changes no other value. | `unknownBatch`, or `batchEnded`: the quantity of the batch is 0. The checks are in this order. |
| `batchUsed` | `batchId`, `quantity`, `date` | Takes the quantity from the batch, but not more than the batch has. Adds a history entry with the outcome `used`, the quantity that was taken, and the date. | `unknownBatch`, `invalidQuantity`: the quantity is 0 or less, or `batchEnded`. The checks are in this order. |
| `batchThrownAway` | `batchId`, `quantity`, `date` | The same as `batchUsed`, with the outcome `thrownAway`. | The same as `batchUsed` |
| `batchDeleted` | `batchId` | Removes the batch and its history. A delete is for a mistake. | `unknownBatch` |
| `changeUndone` | `changeId` | See 7.3. | `unknownChange`, or `cannotUndo`: the other change is a `changeUndone`. The checks are in this order. |

A history entry has the identifier of its change, the batch, the product, the quantity, the outcome, and the date.
The history is in the order of the replay.

### 7.3 Undo

- A `changeUndone` that is not rejected makes the change that it names **undone**. Its position in the log has no
  effect: it can be before or after the change that it names.
- The replay skips an undone change. A skipped change is not in the rejected list.
- An undo cannot be undone. To get the same result again, the app makes a new change.
- The undo of a `batchOpened` change gives the batch the opened date that it had before that change, or none. A later
  `batchEdited` change still sets the opened date that it has.

### 7.4 The result

The result of a replay has the products, the storage areas (each with `fixed`: true or false), all batches (active
and ended), the history, and the rejected changes. Each batch has `dateType` and `openedDate`, with `null` for no
value. In the vectors, the products, the storage areas, and the batches are in the order of their identifiers.

## 8. The storage hint of a looked-up product

A product lookup can give two values that show where the product is kept: the **storage text**, which is the text on
the package about how to keep the product, and the category tags of Open Food Facts. The **storage hint** is the
storage kind that these values give, with its source. It can be absent. The table for this rule is
`storage-hints.json`. It has the phrases that start the instructions for an opened package (`afterOpening`), and a
list of category tags for each storage kind (`tags`). ADR 0011 has the reasons.

### 8.1 The temperatures of a text

The rule reads the characters of the text as Unicode code points, after the text is made lowercase.

- A **space** is U+0020, U+00A0, or U+202F. A **digit** is `0` to `9`.
- Each degree sign `°` (U+00B0) can end one temperature. Go back from the degree sign:
  1. Skip the spaces.
  2. Take the digits. With no digit, the degree sign gives no temperature.
  3. If a `.` or a `,` is before these digits, and a digit is before that sign, these digits are a decimal part. They
     have no effect. Take the digits before the sign in their place.
  4. With more than 3 digits, the degree sign gives no temperature. In other cases the digits are the value.
  5. Skip the spaces. If the character there is a minus sign (`-`, U+2212, or U+2013), look at the character before
     it, after the spaces are skipped. The minus sign is the line between the two ends of a range when that character
     is a digit, a degree sign, or a `c` with a degree sign before it (spaces skipped). The value then stays positive.
     In each other case, also at the start of the text, the value is negative.
- A temperature in Fahrenheit is not used: after the degree sign and its spaces there is an `f`, and the character
  after the `f` is not a letter from `a` to `z`.
- The temperatures of the text are in the order of their degree signs.

### 8.2 The storage kind of a storage text

1. Make the text lowercase.
2. Find the first position at which a phrase of `afterOpening` starts. Use only the text before it. With no phrase,
   use all the text. The text after it is about the opened package.
3. Find the temperatures of this text (8.1). A temperature is **frozen** when it is −6 or lower.

| Temperatures | Storage kind |
|---|---|
| None | None |
| All are frozen | `freezer` |
| Some are frozen, but not all | None. The text names two ways to keep the product. |
| None is frozen, and the highest is 10 or lower | `fridge` |
| None is frozen, and the highest is above 10 | `pantry` |

### 8.3 The storage kind of the category tags

The result is the first storage kind, in the order `freezer`, `fridge`, `pantry`, for which the list in `tags` has a
tag of the product. A tag is compared character by character. With no such kind, there is no result.

### 8.4 The storage hint

1. If the product has a storage text and 8.2 gives a storage kind for it, the hint is that kind with the source
   `storageText`.
2. If not, and 8.3 gives a storage kind, the hint is that kind with the source `tags`.
3. If not, there is no hint.

The storage text comes before the tags because it is about this one product. A tag can be wrong, and a tag is about a
group of products.

## 9. The later-date offer

The later-date offer is the set of controls with which the person selects a chosen date for a batch ("Still good?").
This rule says if the app can show the offer. ADR 0014 has the reasons.

### 9.1 The after-date class of a product

1. If the product has a food, and the food is in the table of foods, the class is the after-date class of the food
   (rule 4).
2. If not, the category of the product gives the class:

| Category | After-date class |
|---|---|
| `condiment`, `beverage`, `bakery` | `check` |
| `produce`, `dairy`, `meat`, `leftovers`, `other` | `strict` |

### 9.2 The offer

The rule uses the good-until date of the batch and its source (rule 5.2), and the freshness that this date gives for
today (rule 3). The result is an offer, or no offer with a reason. The first line of the table that is true for the
batch gives the result.

| # | Condition | Result |
|---|---|---|
| 1 | The freshness is not `expiring` and not `expired`. | No offer, reason `notDue` |
| 2 | The source of the good-until date is `printed`, and the date type of the batch is `useBy`. | No offer, reason `useByDate` |
| 3 | The after-date class of the product is `strict`. | No offer, reason `strictFood` |
| 4 | The source of the good-until date is `opened`. | No offer, reason `opened` |
| 5 | Each other case. | Offer, no reason |

- Line 3 is also true for a strict food with the date type `bestBefore`, with no date type, and with an estimated
  date.
- Line 4: a chosen date is an expiry date, and it cannot move a good-until date that comes from the opened date
  (rule 5.2). An offer would have no effect.
- The storage kind has an effect only through the opened days. A batch in a freezer follows the same lines.

## 10. The before-date tips

A before-date tip is a short text about what to do with a food before its date. The table for this rule is
`before-date-tips.json`. It has the sources (`sources`: a name, a URL, and a licence for each) and the tips (`tips`).
A tip has an identifier, a kind (`freeze`, `cook`, or `useUp`), a list of foods of the table of foods, a text, and
the key of its source. ADR 0015 has the reasons.

The tips that a batch shows are the tips of the table, in the order of the table, for which all these lines are true:

1. The product of the batch has a food, the food is in the table of foods, and the list of foods of the tip has it.
2. The freshness of the batch for today is `expiring` (rule 3, with the good-until date of rule 5.2). A batch that is
   fresh, a batch that is expired, and a batch with no good-until date show no tip.
3. For a tip of the kind `freeze`: the food has days for the freezer (rule 4), and the storage kind of the storage
   area of the batch is not `freezer`.

- The after-date class has no effect on the tips. An expired batch shows no tip, for a strict food and for a check
  food.
- The app shows the text as it is in the table, with the name of its source.

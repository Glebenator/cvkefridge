# Plan: two native apps for CVKE Fridge

Date: 17 November 2026, seventh version. The owner agreed the scope in section 2 and the decisions in section 8.1 on
10 November 2026, the two screens of ADR 0006 on 11 November 2026, the wallpaper colours of ADR 0007 on 12 November
2026, the progress report, ADR 0008, and ADR 0009 on 13 November 2026, and the features of the expiry research on
17 November 2026. ADR 0013 to ADR 0015 record how these features work, and ADR 0016 is a proposal. The owner did not
read these four ADRs before they were written. Section 8.2 lists the decisions that are open.
[PROGRESS.html](../PROGRESS.html) records the progress of each milestone, with screenshots and test results.

CVKE Fridge is the overhaul of FridgeFriend, a React Native app. The overhaul is a full rewrite as a native Android
app and a native iOS app. [legacy-fridgefriend.md](legacy-fridgefriend.md) records what FridgeFriend does today.
The rewrite does not copy it. Section 2 says what stays.

## 1. The product in one page

A person keeps a list of the food in the fridge. The app shows what to use first, and it sends a reminder before food
expires.

One phone does each task. To add food, the person scans the barcode on the package with the phone camera, or types a
name. The app suggests an expiry date, and the person can replace it with the date on the package. When food is
finished, the person records it as used or as thrown away.

The product has no fridge device. [ADR 0002](adr/0002-use-one-phone-and-no-fridge-device.md) records that decision.

Household sharing is deferred. It is not in this plan. [household-sharing.md](household-sharing.md) keeps the design
for later.

## 2. Scope

| Keep from FridgeFriend | Change | Add | Remove |
|---|---|---|---|
| Quantity, unit, category, and storage area | One item with one expiry date becomes a product with batches. Each batch has its own quantity, date added, and expiry date. | A barcode scanner with the phone camera | The fridge device, sessions, detections, approval, and MQTT |
| Freshness from the days left, calculated each time | An expiry date is printed or estimated. The app shows an estimate as an estimate. | Reminders before food expires | The seven card styles |
| A suggested expiry date when the person adds food | The suggestion comes from a table of foods, not from eight categories. | Used and thrown away as the two ends of a batch, with a history | The list of sessions of the old Home screen. Home is the first screen, with the greeting, the totals, and the batches that need attention (ADR 0006). |
| Storage areas: Fridge, Freezer, and the areas that the person creates | An expiry date is a calendar date with no time zone. Today is the date in the device time zone. | A log of each change to the inventory | Sample items in the released app |
| Product lookup from a barcode with Open Food Facts | A failed product lookup is not kept as a result. The category rules do not match parts of words. | | The screen and the controls that nothing uses |
| The inventory on the phone, with no account | | | |
| Undo after a delete | | | |
| A note on a food (ADR 0010) | The note is on the product, not on one batch. | | |
| Oldest batch first when food is used | | | |
| | The date for the days left, the freshness, and the use-first list is the good-until date: the earlier of the expiry date and the after-opening date (ADR 0013). | An opened date on a batch, and opened days for a food in the table of foods (ADR 0013) | |
| | "Still good?" shows only when the rule for the later-date offer permits it: not for a use-by date, and not for a strict food (ADR 0014). This changes ADR 0009. | The date type of a printed date, and an after-date class for each food (ADR 0014) | |
| | | Before-date tips while a batch is expiring, each with a named source (ADR 0015) | |
| | | A short time for thawed food, and no move to a freezer after the date. Agreed as scope on 17 November 2026. Not built: ADR 0016 is a proposal with the options. | |

[ADR 0003](adr/0003-keep-stock-as-products-and-batches.md) records the product and batch model.

## 3. Repositories

[ADR 0001](adr/0001-build-two-native-apps-from-one-product-repository.md) records the setup. It is the same as for
CVKE GPS.

| Repository | Contents | CI |
|---|---|---|
| [cvkefridge](https://github.com/Glebenator/cvkefridge) | The product: this plan, the glossary, the decisions, the product identity, the shared specification in `spec/`, and the legacy reference. No app code. | `spec.yml`: the test vectors agree with the reference model. |
| [cvkefridge-android](https://github.com/Glebenator/cvkefridge-android) | The Android app: Kotlin, Jetpack Compose, Material 3. Application ID `com.cvke.fridge`. | `android.yml`: the copy of `spec/`, core tests with the vectors, debug and release builds, lint, the unit tests of the app, and the device tests on an emulator. |
| [cvkefridge-ios](https://github.com/Glebenator/cvkefridge-ios) | The iOS app: Swift, SwiftUI, XcodeGen. | `ios.yml`: the copy of `spec/`, core tests with the vectors, the simulator build, and the UI test in light and dark appearance. |

All repositories are public. GitHub Actions is then free, and that includes the macOS runners.

## 4. How the two apps stay the same

The two apps share no code. Five mechanisms keep them the same product. Milestone 1 adds mechanism 4.3.

### 4.1 One set of product documents

- `GLOSSARY.md` has each product term one time. Both apps use these words in code, in the interface, and in issues.
- `docs/adr/` has each decision that affects both apps, and each intended difference between the apps. A difference
  without an ADR is a defect.
- `design/product.md` has the product identity. `design/product.json` has the colour values. Each app copies these
  values into its theme file (`Tokens.kt`, `Theme.swift`).
- `AGENTS.md` has the shared rules. The `AGENTS.md` of each app has the platform rules.

### 4.2 Mirrored core modules

Each app keeps the product rules in a module that cannot see the platform.

| | Android | iOS |
|---|---|---|
| Module | `:core`, pure Kotlin on the JVM | `CVKEFridgeCore`, a Swift package with Foundation only |
| Contents | Products and batches, calendar dates, days left, freshness, the expiry estimate, the good-until date, the use-first order, the change log, the storage hint, the later-date offer, and the before-date tips | The same |
| Tests | `./gradlew :core:test` | `swift test` |

Rules for the two modules:

- A file in one module has a file of the same name in the other module (`Freshness.kt`, `Freshness.swift`).
- Public types and functions have the same names, in the style of each language.
- The compiler enforces the border. `:core` has no Android dependency. `CVKEFridgeCore` does not import UIKit or
  SwiftUI.
- Screens, storage, the network, the camera, and notifications stay outside the core. They are native on each platform.

Both modules have one file now, `AppVersion`, with the same two test cases. It proves the structure and the CI.

### 4.3 Shared test vectors

The same file names do not prove the same behaviour. Test vectors do.

- This repository has a `spec/` folder. It holds JSON files of inputs and expected outputs, for example
  `spec/vectors/freshness.json`: a date for today, an expiry date, the expected days left, and the expected freshness.
- `spec/` also holds the rules in words (`spec/rules.md`) and the data that both apps read: the table of foods for the
  expiry estimate.
- Each app has an exact copy of `spec/`, and a file `spec.ref` that names the commit of this repository from which
  the copy comes. The core tests run each vector through the core module. The CI of the app fails when the copy is
  different from this repository at that commit.
- A rule change is then one change here, and one change of the copy and of `spec.ref` in each app. An app that does
  not follow the rule has a red build.
- A reference model in `spec/tools/vectors.py` calculates the expected results. The workflow `spec.yml` checks each
  vector file against it.

[ADR 0004](adr/0004-prove-the-same-behaviour-with-shared-test-vectors.md) records this mechanism.

### 4.4 One feature, three issues

- A feature starts as a parent issue in `cvkefridge`. It states the behaviour in glossary terms, and it names the
  vectors and the ADRs that the feature adds.
- Each app repository gets one sub-issue.
- The parent issue closes when both sub-issues are closed and both CI runs are green on the same `spec.ref`.

### 4.5 Work order for one feature

1. Write the rule: glossary terms, an ADR if the rule is a decision, and the vectors.
2. Build the Android side first. The Android app builds and runs on the development machine (Windows), and the
   emulator gives a result in minutes.
3. Build the iOS side second, from the same vectors and the finished Android behaviour. The development machine has no
   Xcode, so each iOS build is a CI run. Only the interface needs the macOS runner. The core tests are fast.
4. Compare the screens. The iOS workflow uploads its screenshots as an artifact. The Android device test can do the
   same.

The lead platform can change for a feature that is harder on iOS. The vectors are the reference in each case, not the
first app.

## 5. Versions and releases

- Both apps have the same version name. A version name names the same feature set in both apps. Build numbers are
  separate.
- A release is a tag `v<version>` in each app repository, on a commit with a green CI run.
- `com.cvke.fridge` is the Android application ID for the life of the app. The iOS app has a development bundle ID
  (`com.example.cvkefridge`). Replace it before the first upload to App Store Connect.
- CI builds unsigned release outputs. Signing keys stay out of Git and out of CI until a release needs them.

## 6. Milestones

Each milestone is one parent issue with one sub-issue for each app. The order puts the rules before the screens.

| # | Milestone | Result |
|---|---|---|
| 0 | Scaffold | Three repositories, a start screen in each app, green CI. Done on 10 November 2026. |
| 1 | Core rules | Products and batches, calendar dates, days left, freshness, the expiry estimate from the table of foods, the use-first order, and the change log. Vectors for each. `spec/` and `spec.ref`. No screens. Done on 10 November 2026: both core modules pass the 165 vector cases at the same commit of `spec/`. |
| 2 | Inventory on one phone | Storage on the phone. Home as the first screen, and My Fridge as the second screen. Create and edit by hand. Used and thrown away, with undo. Storage areas. Empty, loading, and error states. Android: done on 12 November 2026. iOS: not started. |
| 3 | Add with a barcode | The camera scanner, the product lookup with a cache on the phone, the entry of a printed or an estimated expiry date, and the failure states. Android: done on 12 November 2026. iOS: not started. |
| 4 | Reminders | Local notifications before a batch expires, the explanation before the permission request, and the reminder settings. Android: done on 12 November 2026. iOS: not started. |
| 5 | History | What was used and what was thrown away, add a product again, and the product photo. Android: done on 12 November 2026. iOS: not started. |
| 6 | Release preparation | Large text, screen readers, rotation, store listings, privacy details, signing. Not started. |

A milestone is complete when both apps have it (section 4.4). On 13 November 2026, milestones 0 and 1 are complete.
Milestones 2 to 5 are complete on Android only:

- The Android work is on `main` of `cvkefridge-android` at commit `dce5b94`, and its CI run is green.
- The iOS app has the core rules of milestone 1 and the start screen. It has no screens of milestones 2 to 5.
- Milestones 2 to 5 have no parent issue in this repository and no sub-issue in the app repositories. Section 4.4
  says that each milestone has them.
- On 17 November 2026, `spec/` got the rules for opened food, for the later-date offer, and for the before-date tips
  (ADR 0013, ADR 0014, ADR 0015), with 348 vector cases. An app has them when its copy of `spec/` is at that commit
  and its core module passes each case. The screens for them are not in a milestone of the table yet.

### 6.1 Rules that are only in the Android app

Milestones 3 to 5 added rules that are not in `spec/`. They are in plain Kotlin in the `app` module, with unit tests.
Before the iOS app builds these milestones, move them into `spec/rules.md` and the vectors (section 4.5, step 1), and
then into `:core` and `CVKEFridgeCore`.

| Milestone | Rule | Android source |
|---|---|---|
| 3 | The one form of a barcode and its check digit | `lookup/Barcodes.kt` |
| 3 | The name, the category, the food of the table of foods, and the package quantity of a looked-up product | `lookup/ProductMapping.kt` |
| 3 | One barcode for one product | `inventory/InventoryAction.kt` |
| 4 | Which batches are in the reminder of a date, and their order | `reminder/ReminderRules.kt` |
| 4 | The lead times, their default, and the dates of the schedule | `reminder/ReminderSchedule.kt`, `reminder/ReminderSettings.kt` |
| 4 | The text of the notification | `reminder/ReminderText.kt` |
| 5 | The order, the day headers, the filter, the periods, the summary, and the most thrown-away foods of the history | `history/HistoryContent.kt` |
| 5 | The values of "Add again" and the recent foods | `inventory/AddAgain.kt` |
| 3 | The suggestions of the add form: how a text agrees with a name, an alias, a keyword, or a word with one wrong letter; the foods of the person and the common foods first; not more than 2 foods with the same name | `inventory/FoodSuggestions.kt` |
| 3 | The storage area of the add form: the area that the person selected, the area of the newest batch of the product, an area of the storage kind of the storage hint of the scan (the hint is rule 8 of `spec/rules.md`, ADR 0011), an area of the usual storage kind of the food, and the start area | `inventory/AddFoodForm.kt` |
| 3 | The fields of the product lookup that give the storage text: the language of the device, the main language of the product, and English | `lookup/OpenFoodFacts.kt` |
| 3 | The lookup pause: which failures start it, its 5 minutes, what ends it, and what "Try again" does in it (ADR 0018) | `lookup/ProductLookup.kt` |
| 5 | The product photo. The `Product` of the core has no photo, and a photo is not in the change log. | `photo/PhotoFiles.kt` |
| 3 | The storage text that the app saves: one space between words, no spaces at the ends, and not more than 500 characters. The product that gets the storage text of an add (ADR 0012). | `inventory/StorageAdvice.kt`, `inventory/InventoryAction.kt` |
| 3 | The storage tips: the storage text of the scan or of the product, and the general advice for the food (the usual storage kind, and for each storage kind the time in the largest unit that gives a whole number, and the tip) | `inventory/StorageAdvice.kt` |
| 2 | The note that the app saves: no spaces at the start and at the end, and no note for an empty text. The note of the add form for a product that exists (ADR 0010). | `inventory/Notes.kt`, `inventory/AddFoodForm.kt` |
| 3 | The GTIN and the printed date of a GS1 2D barcode: element strings (the AIs of predefined length of table 7-6, the GS separator, one separator accepted after any element string, the symbology identifier and the human-readable form), GS1 Digital Link URIs (any domain and path segments before `/01/<gtin>`, the key qualifiers 22, 10, 21, 235, `15=` and `17=` in the query string, a legacy GTIN of 8, 12, or 13 digits), the expiration date (17) before the best before date (15), day 00 as the last day of the month, the century from 49 years before to 50 years after the current year, a GTIN-8 in 14 digits as its EAN-8, and a QR Code with no GS1 data as no barcode. Not tested with a real 2D barcode. | `lookup/Gs1.kt`, `lookup/Barcodes.kt` (`fromGtin14`) |
| 3 | The dates in the text of a package (date scanner): the numeric forms, the two dates of an ambiguous day and month in the order of the locale, a month and a year as the last day of the month, the month names of six languages, the Canadian month codes, the label words of use by, best before, and expiration, the words that exclude a packaging date, a production date, a sell-by date, and a lot number, the year window, the label word that a date with no year needs, and the warning for a date more than 30 days before today. Not tested with a real package. | `inventory/PrintedDates.kt` |
| 2 | The offer to record the rest of a used batch as opened, and which batch gets the `batchOpened` change (ADR 0013) | `inventory/TakeQuantity.kt`, `inventory/InventoryAction.kt` |
| 3 | The date type of a form: only with a printed date; kept for a new printed date; removed for another date; a scan with label words sets it, and a scan with none keeps it (ADR 0014) | `inventory/AddFoodForm.kt`, `inventory/EditForms.kt`, `inventory/PrintedDates.kt` |
| 2 | What the screen of a food shows for the new rules: the expiry date below a date from the opened date, the line for a missing estimate after opening, the actions below the reason for no later-date offer, and each before-date tip one time in the order of the table | `ui/FoodDetail.kt` |
| 2 | The count of dates on a card of My Fridge and its words | `ui/InventoryContent.kt` |
| 4 | The reminder text for a date from the opened date | `reminder/ReminderRules.kt`, `reminder/ReminderText.kt` |
| 3 | The opened days as general advice in the storage tips | `inventory/StorageAdvice.kt` |
| 2 | The opened date of the edit form is not after today | `ui/FormParts.kt` |

The rules of ADR 0013 to ADR 0015 are in `spec/`, so they add no line to this table. They change two things for the
rules of this table. The reminder rules use the days left, so they must use the good-until date (rule 5.2 of
`spec/rules.md`). Each `batchEdited` change that the app writes must have the date type and the opened date of the
batch, because an edit with no key removes the value.

## 7. CI today

| Workflow | Job | What it proves |
|---|---|---|
| `spec.yml` | `check` | Each test vector agrees with the reference model. The table of foods is valid. |
| `android.yml` | `build` | The copy of `spec/` is exact. `:core` tests pass with each vector. The unit tests of the app pass. The debug app, the device tests, the release APK, and the release bundle build. Lint has no warnings. |
| `android.yml` | `device` | The device tests pass on an Android 15 emulator: the screens of the inventory, the changes to the inventory, the scanner and the product lookup, the barcode reader, the reminder, and History. |
| `ios.yml` | `core` | The copy of `spec/` is exact. `CVKEFridgeCore` tests pass with each vector. |
| `ios.yml` | `app` | The app builds for the simulator. The start screen test passes in light and dark appearance. The screenshots are an artifact. |

Each workflow runs for a push to `main`, for a pull request, and on request.

## 8. Decisions

### 8.1 Agreed on 10 November 2026

| Decision | Record |
|---|---|
| The rewrite has no fridge device. One phone does each task. | ADR 0002 |
| The app is complete on one phone: the barcode scanner and the reminders are early milestones. | Section 6 |
| Stock is products and batches. | ADR 0003 |
| An expiry date is printed or estimated, and the estimate comes from a table of foods. | ADR 0003 |
| A batch ends as used or as thrown away, and the app keeps a history. | ADR 0003 |
| Home is the first screen and My Fridge is the second screen. The two screens have the contents of FridgeFriend. The Android app shows them with Material 3 components and a colour scheme from the green of FridgeFriend. Agreed on 11 November 2026. This replaces the decision that the use-first list is the first screen. | [ADR 0006](adr/0006-put-home-first-and-list-all-food-on-a-second-screen.md) |
| On Android 12 and later, the Android app takes its colour scheme from the wallpaper. The colours of fresh, expiring, and expired, and the brand parts, do not change. Agreed on 12 November 2026. This replaces the colour scheme from the green of FridgeFriend on these versions. | [ADR 0007](adr/0007-use-the-wallpaper-colours-on-android.md) |
| The product has a progress report, `PROGRESS.html` in this repository, as in CVKE GPS. Agreed on 13 November 2026. | `AGENTS.md` |
| An expiry date can be a chosen date: a later date that the person selected because the food is still good. The screen of a food has "+1 day", "+1 week", and "Other date" for a batch that is expiring or expired. Agreed on 13 November 2026. | [ADR 0009](adr/0009-let-the-person-choose-a-later-expiry-date.md) |
| Settings is a destination of the navigation bar. A tap on My Fridge there shows the Fridge with no filter. The Android app has a switch for the wallpaper colours. A product photo comes from the camera or from the photos of the phone, also in the add form. Agreed on 13 November 2026. | [ADR 0008](adr/0008-put-settings-in-the-navigation-bar.md) |
| A product has an optional note: the text of the person about the food. The screen of the food shows it and edits it in place, the add form and the edit form have it, the card on My Fridge shows its first line, and the search of My Fridge finds it. Agreed on 14 November 2026. | [ADR 0010](adr/0010-put-a-note-on-the-product.md) |
| The app keeps a log of each change from the start. | ADR 0003, ADR 0005 |
| Shared test vectors prove the same behaviour. Each app has a copy of `spec/`. | ADR 0004 |
| The table of foods is the USDA FSIS FoodKeeper data (CC0 1.0). | ADR 0004 |
| Household sharing is deferred. The change log and the random identifiers stay, so that sharing can come later with no conversion of data. | [household-sharing.md](household-sharing.md) |
| Build the features of the expiry research ([expiry-dates.md](research/expiry-dates.md)): opened food, the date type and the class of a food after its date, tips before the date, and frozen and thawed food. The app is careful: it does not suggest that a person eats spoiled food. Agreed on 17 November 2026. | ADR 0013 to ADR 0016 |
| A batch has an optional opened date, and the table of foods has opened days. The app uses the good-until date: the earlier of the expiry date and the opened date plus the opened days. A date from the opened date is an estimate. | [ADR 0013](adr/0013-keep-an-opened-date-on-the-batch.md) |
| A printed date can have a date type: use by or best before. Each food has an after-date class: strict or check. "Still good?" shows only for a batch that is not strict, that has no use-by date, and that does not get its date from its opened date. This replaces a part of ADR 0009. | [ADR 0014](adr/0014-offer-a-later-date-only-for-food-that-the-person-can-check.md) |
| An expiring batch shows before-date tips: freeze it, cook it, or use it up. Each text has the words of a named source. An expired batch shows no tip. | [ADR 0015](adr/0015-show-before-date-tips-from-named-sources.md) |

### 8.2 Open

| # | Decision | Recommendation |
|---|---|---|
| 1 | The product name in the stores and on the screen | "CVKE Fridge", as for CVKE GPS. |
| 2 | The product identity in `design/product.md` (teal accent, the shelf line motif) | On 11 November 2026 the owner saw Home and All food with this identity and did not want them. Home and My Fridge now copy the look of FridgeFriend (ADR 0006). The identity is not used. Decide if it stays for other surfaces. |
| 3 | The words in `GLOSSARY.md`, mainly "batch", "used", and "thrown away" | Agree in milestone 1. |
| 4 | Frozen and thawed food: how a batch gets a short time after it is thawed, and how the app stops a move to a freezer after the date. [ADR 0016](adr/0016-proposal-for-frozen-and-thawed-food.md) has options A, B, and C. | Option A: the changes `batchFrozen` and `batchThawed`, with 1 day for thawed food. |
| 5 | The time for thawed food: 1 day for each food (Food Standards Agency), or 3 days for some foods (ANSES) | 1 day. |
| 6 | If the person can select a later date for a batch that gets its good-until date from its opened date. Now the app gives no offer, because a chosen date does not come before the after-opening date (ADR 0013). | Permit it for a check food, with a second chosen date on the batch that replaces the after-opening date. Until then, the person removes or corrects the opened date in the edit form. |
| 7 | If the core reads the days after opening from the storage text of a product ("use within 3 days of opening"). It is not built (ADR 0013). | Count real storage texts first, as ADR 0011 did, and then decide. |
| 8 | The after-date classes in `spec/tools/food-classes.json`. They are a selection by hand: 262 foods are strict and 399 are check. | The owner reads the classes of the 142 common foods. A person who knows food safety checks the file before a release. |
| 9 | The class of eggs. Eggs are strict, so they get no "Still good?". The Food Standards Agency says that eggs are safe for a couple of days after the best-before date if they are cooked well. | Keep eggs strict. |
| 10 | The class of a product with no food of the table. It comes from the category. Since ADR 0017, the pantry categories `grains`, `canned`, `baking`, and `snacks` are check, and `other` has few foods: 13 of 661 foods of the table, and 2 of 100 most-scanned products of Canada and of the United States. `produce`, `dairy`, `meat`, `meals`, `leftovers`, and `other` are strict. | Keep it. Check the class of `produce` with no food when the app has more scans of fresh produce. |
| 11 | If a strict food in a freezer gets "Still good?" after its estimated date. Now it gets none, because the core does not know when the batch was frozen. | Decide it with decision 4. |
| 12 | The sources of the before-date tips. Now a text must have the words of a source with a licence that permits the copy, and the table has 4 tips from the Food Standards Agency and GOV.UK. Love Food Hate Waste refused our requests. | Keep the rule. Ask Love Food Hate Waste for permission, and check the licences of Health Canada and of the Voedingscentrum. |
| 13 | If a before-date tip can be a short sentence in our own words with a link to its source. ADR 0012 does not permit a text that no source has. The two tips for meat and fish have the words "use-by date", also for a batch with a different date type. | Keep the words of the source. |

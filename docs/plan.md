# Plan: two native apps for CVKE Fridge

Date: 10 November 2026, third version. The owner agreed the scope in section 2 and the decisions in section 8.1 on
10 November 2026. Section 8.2 lists the decisions that are open.

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
| A suggested expiry date when the person adds food | The suggestion comes from a table of foods, not from eight categories. | Used and thrown away as the two ends of a batch, with a history | The Home screen with a greeting and totals. The use-first list is the first screen. |
| Storage areas: Fridge, Freezer, and the areas that the person creates | An expiry date is a calendar date with no time zone. Today is the date in the device time zone. | A log of each change to the inventory | Sample items in the released app |
| Product lookup from a barcode with Open Food Facts | A failed product lookup is not kept as a result. The category rules do not match parts of words. | | The screen and the controls that nothing uses |
| The inventory on the phone, with no account | | | |
| Undo after a delete | | | |
| Oldest batch first when food is used | | | |

[ADR 0003](adr/0003-keep-stock-as-products-and-batches.md) records the product and batch model.

## 3. Repositories

[ADR 0001](adr/0001-build-two-native-apps-from-one-product-repository.md) records the setup. It is the same as for
CVKE GPS.

| Repository | Contents | CI |
|---|---|---|
| [cvkefridge](https://github.com/Glebenator/cvkefridge) | The product: this plan, the glossary, the decisions, the product identity, and the legacy reference. No app code. | None now. Section 4.3 recommends a check of the test vectors. |
| [cvkefridge-android](https://github.com/Glebenator/cvkefridge-android) | The Android app: Kotlin, Jetpack Compose, Material 3. Application ID `com.cvke.fridge`. | `android.yml`: core tests, debug and release builds, lint, and the device test on an emulator. |
| [cvkefridge-ios](https://github.com/Glebenator/cvkefridge-ios) | The iOS app: Swift, SwiftUI, XcodeGen. | `ios.yml`: core tests, the simulator build, and the UI test in light and dark appearance. |

All repositories are public. GitHub Actions is then free, and that includes the macOS runners.

## 4. How the two apps stay the same

The two apps share no code. Five mechanisms keep them the same product. Mechanisms 4.1 and 4.2 and the parent issue
of 4.4 exist now. Mechanism 4.3 is open decision 1 in section 8.2.

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
| Contents | Products and batches, calendar dates, days left, freshness, the expiry estimate, the use-first order, and the change log | The same |
| Tests | `./gradlew :core:test` | `swift test` |

Rules for the two modules:

- A file in one module has a file of the same name in the other module (`Freshness.kt`, `Freshness.swift`).
- Public types and functions have the same names, in the style of each language.
- The compiler enforces the border. `:core` has no Android dependency. `CVKEFridgeCore` does not import UIKit or
  SwiftUI.
- Screens, storage, the network, the camera, and notifications stay outside the core. They are native on each platform.

Both modules have one file now, `AppVersion`, with the same two test cases. It proves the structure and the CI.

### 4.3 Shared test vectors (recommended)

The same file names do not prove the same behaviour. Test vectors do.

- This repository gets a `spec/` folder. It holds JSON files of inputs and expected outputs, for example
  `spec/vectors/freshness.json`: a date for today, an expiry date, the expected days left, and the expected freshness.
- `spec/` also holds the data that both apps read: the table of foods for the expiry estimate.
- Each app has a file `spec.ref` that names one commit of this repository. The CI of the app gets `spec/` at that
  commit and runs each vector through its core module.
- A rule change is then one change to a vector here, and one change of `spec.ref` in each app. An app that does not
  follow the rule has a red build.
- This repository gets a small workflow that checks that each vector file is valid JSON and agrees with its schema.

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
| 1 | Core rules | Products and batches, calendar dates, days left, freshness, the expiry estimate from the table of foods, the use-first order, and the change log. Vectors for each. `spec/` and `spec.ref`. No screens. |
| 2 | Inventory on one phone | Storage on the phone. The use-first list as the first screen. Create and edit by hand. Used and thrown away, with undo. Storage areas. Empty, loading, and error states. |
| 3 | Add with a barcode | The camera scanner, the product lookup with a cache on the phone, the entry of a printed or an estimated expiry date, and the failure states. |
| 4 | Reminders | Local notifications before a batch expires, the explanation before the permission request, and the reminder settings. |
| 5 | History | What was used and what was thrown away, add a product again, and the product photo. |
| 6 | Release preparation | Large text, screen readers, rotation, store listings, privacy details, signing. |

## 7. CI today

| Workflow | Job | What it proves |
|---|---|---|
| `android.yml` | `build` | `:core` tests pass. The debug app, the device tests, the release APK, and the release bundle build. Lint has no warnings. |
| `android.yml` | `device` | The start screen test passes on an Android 15 emulator. |
| `ios.yml` | `core` | `CVKEFridgeCore` tests pass. |
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
| The use-first list is the first screen. The app has no dashboard. | Section 2 |
| The app keeps a log of each change from the start. | ADR 0003 |
| Household sharing is deferred. The change log and the random identifiers stay, so that sharing can come later with no conversion of data. | [household-sharing.md](household-sharing.md) |

### 8.2 Open

| # | Decision | Recommendation |
|---|---|---|
| 1 | Shared test vectors (section 4.3) | Yes. Add `spec/` in milestone 1. |
| 2 | The source of the table of foods for the expiry estimate | Examine the USDA FoodKeeper data in milestone 1: its licence, its contents, and its fit. Use the FridgeFriend table of eight categories only as the last fallback. |
| 3 | The product name in the stores and on the screen | "CVKE Fridge", as for CVKE GPS. |
| 4 | The product identity in `design/product.md` (teal accent, the shelf line motif) | Agree or change it before milestone 2, the first milestone with real screens. |
| 5 | The words in `GLOSSARY.md`, mainly "batch", "used", and "thrown away" | Agree in milestone 1. |
| 6 | A progress report (`PROGRESS.html`) as in CVKE GPS | Start it with milestone 2, the first milestone with screens. |

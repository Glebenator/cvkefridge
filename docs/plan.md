# Plan: two native apps for CVKE Fridge

Date: 10 November 2026. Status: proposal. The repository setup in section 3 is done. All other sections need the
owner's agreement before work starts. Section 8 lists the decisions to make.

CVKE Fridge is the overhaul of FridgeFriend, a React Native app. The overhaul replaces it with a native Android app and
a native iOS app. [legacy-fridgefriend.md](legacy-fridgefriend.md) records what FridgeFriend does today.

## 1. The product in one page

A person keeps a list of the food in the fridge. Each item has a quantity, a category, a storage area, and an expiry
date. The app shows which items to use first.

A fridge device can be in the fridge. It detects the food that goes in and comes out each time the door opens, and it
sends the detections to the app as a session. The person reviews the session and approves it. Approval changes the item list.

The app can find a product name and a category from a barcode, with the Open Food Facts service.

## 2. Scope of the overhaul

This scope is a recommendation. It comes from the FridgeFriend code, not from an agreed requirement.

| Keep | Change | Remove |
|---|---|---|
| Items with quantity, unit, category, storage area, expiry date, notes, and a photo | Dates: an expiry date becomes a calendar date with no time zone. Today is the date in the device time zone. FridgeFriend mixes UTC and local dates, and the days left are wrong by one for some hours each day. | The seven card styles. Each app has one design, from the design language. |
| Freshness from the days left | Approval: all changes of one approval apply together, or none apply. FridgeFriend can stop in the middle. | The sample items and sample sessions that FridgeFriend adds each time the item list or the session list is empty. |
| Shelf-life defaults for each category and storage area | A session that the device sends again does not replace the edits of the person or cancel an approval. FridgeFriend does both. | The screen and the controls that nothing uses. |
| Storage areas: Fridge, Freezer, and the areas that the person creates | A failed product lookup is not kept as a result. FridgeFriend keeps the failure for 24 hours. | The name field as a place for a barcode. FridgeFriend accepts a barcode field, but it looks up only a barcode in the name. |
| Sessions from the fridge device, with review and approval | One word for each state. FridgeFriend uses "processed", "approved", and "verified" for the same state. | |
| Product lookup from a barcode | The category rules for a product lookup. FridgeFriend finds a word anywhere in the tags, and the first group wins: a tag with "fresh" gives produce, and "cream" finds ice cream. | |

Not in FridgeFriend, and not in this plan until the owner adds them: expiry notifications, a barcode scanner with the
phone camera, cloud sync, more than one household member.

## 3. Repositories

The setup is the same as for CVKE GPS. [ADR 0001](adr/0001-build-two-native-apps-from-one-product-repository.md)
records it.

| Repository | Contents | CI |
|---|---|---|
| [cvkefridge](https://github.com/Glebenator/cvkefridge) | The product: this plan, the glossary, the decisions, the product identity, and the legacy reference. No app code. | None now. Section 4.3 recommends a check of the test vectors. |
| [cvkefridge-android](https://github.com/Glebenator/cvkefridge-android) | The Android app: Kotlin, Jetpack Compose, Material 3. Application ID `com.cvke.fridge`. | `android.yml`: core tests, debug and release builds, lint, and the device test on an emulator. |
| [cvkefridge-ios](https://github.com/Glebenator/cvkefridge-ios) | The iOS app: Swift, SwiftUI, XcodeGen. | `ios.yml`: core tests, the simulator build, and the UI test in light and dark appearance. |

All three repositories are public. GitHub Actions is then free, and that includes the macOS runners.

## 4. How the two apps stay the same

The two apps share no code. Five mechanisms keep them the same product. Mechanisms 4.1 and 4.2 and the parent
issue of 4.4 exist now. The others are recommendations.

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
| Contents | Models, date rules, freshness, shelf life, sort orders, quantity rules, the session payload parser, the approval rules | The same |
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

- The hub repository gets a `spec/` folder. It holds JSON files of inputs and expected outputs, for example
  `spec/vectors/freshness.json`: a date for today, an expiry date, the expected days left, and the expected freshness.
- `spec/` also holds the contracts that both apps read: the JSON Schema of the session payload from the fridge device,
  and the table of shelf-life defaults.
- Each app has a file `spec.ref` that names one commit of the hub repository. The CI of the app gets `spec/` at that
  commit and runs each vector through its core module.
- A rule change is then one change to a vector in the hub, and one change of `spec.ref` in each app. An app that does
  not follow the rule has a red build.
- The hub gets a small workflow that checks that each vector file is valid JSON and agrees with its schema.

This mechanism costs one test runner in each app and one checkout step in each workflow. It replaces the manual
comparison of two test suites.

### 4.4 One feature, three issues

- A feature starts as a parent issue in `cvkefridge`. It states the behaviour in glossary terms, and it names the
  vectors and the ADRs that the feature adds.
- Each app repository gets one sub-issue.
- The parent issue closes when both sub-issues are closed, both CI runs are green on the same `spec.ref`, and the
  progress report has the change with both app commits as the baseline.

### 4.5 Work order for one feature

1. Write the rule: glossary terms, an ADR if the rule is a decision, and the vectors.
2. Build the Android side first. The Android app builds and runs on the development machine (Windows), and the
   emulator gives a result in minutes.
3. Build the iOS side second, from the same vectors and the finished Android behaviour. The development machine has no
   Xcode, so each iOS build is a CI run. The core tests in `CVKEFridgeCore` also run with a Swift toolchain on Windows
   or Linux, which makes the rule work fast. Only the interface needs the macOS runner.
4. Compare the screens. The iOS workflow uploads its screenshots as an artifact. The Android device test can do the
   same. The progress report shows both.

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

Each milestone is one parent issue with one sub-issue for each app. The order puts the rules before the screens, and
the device contract before the network code.

| # | Milestone | Result |
|---|---|---|
| 0 | Scaffold | Three repositories, a start screen in each app, green CI. Done on 10 November 2026. |
| 1 | Core rules | Calendar dates, days left, freshness, shelf-life defaults, sort orders, quantity steps. Vectors for each. No screens. |
| 2 | Item list | Storage on the device. List, create, edit, and delete items, with undo. Storage areas and categories. Empty, loading, and error states. |
| 3 | Item detail | The signature component, the photo, the notes, the quantity control. |
| 4 | Product lookup | Open Food Facts lookup with a cache on the device, the category rules as vectors, and the failure states. |
| 5 | Session contract | The session payload schema in `spec/`, the parser in both cores, vectors for valid and invalid payloads. |
| 6 | Session review and approval | The session list, the review screen, and approval as one transaction. The match rules for "put in" and "taken out" as vectors. |
| 7 | Device connection | The MQTT connection to the fridge device, discovery on the local network, the permission texts, and the connection states. |
| 8 | Release preparation | Settings, large text, screen readers, rotation, store listings, privacy details, signing. |

Milestone 7 comes late on purpose. Milestones 5 and 6 work from payload files, so the session screens do not wait for
the network code or for the fridge device.

## 7. CI today

| Workflow | Job | What it proves |
|---|---|---|
| `android.yml` | `build` | `:core` tests pass. The debug app, the device tests, the release APK, and the release bundle build. Lint has no warnings. |
| `android.yml` | `device` | The start screen test passes on an Android 15 emulator. |
| `ios.yml` | `core` | `CVKEFridgeCore` tests pass. |
| `ios.yml` | `app` | The app builds for the simulator. The start screen test passes in light and dark appearance. The screenshots are an artifact. |

Each workflow runs for a push to `main`, for a pull request, and on request.

## 8. Decisions to make

| # | Decision | Recommendation |
|---|---|---|
| 1 | Is the scope in section 2 correct? | Agree the Keep, Change, and Remove columns before milestone 1. |
| 2 | Shared test vectors (section 4.3)? | Yes. Record it as ADR 0002 and add `spec/` in milestone 1. |
| 3 | The product name in the stores and on the screen | "CVKE Fridge", as for CVKE GPS. The old name FridgeFriend stays in the legacy document only. |
| 4 | The product identity in `design/product.md` (teal accent, the shelf line motif) | Agree or change it before milestone 2, the first milestone with real screens. |
| 5 | The words in `GLOSSARY.md`, mainly "detection" for a session item, and "approved" as the one word for a finished session | Agree in milestone 1. The glossary is a first draft. |
| 6 | Storage: the same SQLite schema in both apps, or only the same export file? | The same logical schema, written one time in `spec/`. Each app uses its native storage library. |
| 7 | Features that FridgeFriend does not have: expiry notifications and a camera barcode scanner | Add both after milestone 6. An inventory app without a reminder gives its answer only when the person opens it. |
| 8 | The fridge device firmware: where is its code, and can the payload change? | The payload contract in `spec/` needs an owner on the device side before milestone 5. |
| 9 | A progress report (`PROGRESS.html`) as in CVKE GPS | Start it with milestone 1. The scaffold has no product behaviour to report. |

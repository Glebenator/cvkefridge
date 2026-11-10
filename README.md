# CVKE Fridge

A food inventory for the fridge, with a native Android app and a native iOS app. It is the overhaul of FridgeFriend.
This repository holds the product: the plan, the decisions, the glossary, and the product identity. It has no app code.

| Repository | Contents |
|---|---|
| [cvkefridge](https://github.com/Glebenator/cvkefridge) | This repository: the product documents and the parent issues for both apps |
| [cvkefridge-android](https://github.com/Glebenator/cvkefridge-android) | The Android app: Kotlin, Jetpack Compose, and Material 3 |
| [cvkefridge-ios](https://github.com/Glebenator/cvkefridge-ios) | The iOS app: Swift and SwiftUI |

## Status

Each app has a start screen only. The CI of each app builds it and runs its tests.

[![Android](https://github.com/Glebenator/cvkefridge-android/actions/workflows/android.yml/badge.svg)](https://github.com/Glebenator/cvkefridge-android/actions/workflows/android.yml)
[![iOS](https://github.com/Glebenator/cvkefridge-ios/actions/workflows/ios.yml/badge.svg)](https://github.com/Glebenator/cvkefridge-ios/actions/workflows/ios.yml)

## Documents

- [docs/plan.md](docs/plan.md): how the two apps stay the same product, the milestones, and the open decisions.
  The plan is a proposal.
- [docs/legacy-fridgefriend.md](docs/legacy-fridgefriend.md): what the old app does, with its rules and values.
- [GLOSSARY.md](GLOSSARY.md): the shared terms. It is a first draft.
- [docs/adr/](docs/adr/): the decisions.
- [design/product.md](design/product.md): the product identity. It is a proposal.
- [AGENTS.md](AGENTS.md): the rules for this repository and the shared rules for both apps.

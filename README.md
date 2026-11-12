# CVKE Fridge

A food inventory for the fridge, with a native Android app and a native iOS app. One phone does each task. It is the
rewrite of FridgeFriend.
This repository holds the product: the plan, the decisions, the glossary, and the product identity. It has no app code.

| Repository | Contents |
|---|---|
| [cvkefridge](https://github.com/Glebenator/cvkefridge) | This repository: the product documents and the parent issues for both apps |
| [cvkefridge-android](https://github.com/Glebenator/cvkefridge-android) | The Android app: Kotlin, Jetpack Compose, and Material 3 |
| [cvkefridge-ios](https://github.com/Glebenator/cvkefridge-ios) | The iOS app: Swift and SwiftUI |

## Status

Milestone 1 is complete. Milestone 2 is in work: the Android app has the change log on the phone and its first two
screens, Home and My Fridge. The iOS app has a start screen and the core rules. The CI of each app
builds it and runs the shared test vectors in `spec/` through its core module.

[![Android](https://github.com/Glebenator/cvkefridge-android/actions/workflows/android.yml/badge.svg)](https://github.com/Glebenator/cvkefridge-android/actions/workflows/android.yml)
[![iOS](https://github.com/Glebenator/cvkefridge-ios/actions/workflows/ios.yml/badge.svg)](https://github.com/Glebenator/cvkefridge-ios/actions/workflows/ios.yml)
[![Spec](https://github.com/Glebenator/cvkefridge/actions/workflows/spec.yml/badge.svg)](https://github.com/Glebenator/cvkefridge/actions/workflows/spec.yml)

## Documents

- [docs/plan.md](docs/plan.md): the scope, how the two apps stay the same product, the milestones, and the decisions.
- [docs/household-sharing.md](docs/household-sharing.md): a design note for a deferred feature.
- [docs/legacy-fridgefriend.md](docs/legacy-fridgefriend.md): what the old app does, with its rules and values. The
  rewrite does not copy it.
- [spec/](spec/): the core rules, the test vectors that both apps run, and the table of foods.
- [GLOSSARY.md](GLOSSARY.md): the shared terms. It is a draft.
- [docs/adr/](docs/adr/): the decisions: three repositories (0001), no fridge device (0002), products and batches
  (0003), shared test vectors (0004), the replay of the change log (0005), and Home and My Fridge (0006).
- [design/product.md](design/product.md): the product identity. It is a proposal.
- [AGENTS.md](AGENTS.md): the rules for this repository and the shared rules for both apps.

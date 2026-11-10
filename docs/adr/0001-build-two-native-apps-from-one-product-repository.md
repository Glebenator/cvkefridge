# Build two native apps from one product repository

CVKE Fridge replaces FridgeFriend, one React Native app for both platforms. We build a native Android app and a native
iOS app, each in its own repository, with a third repository for the product. CVKE GPS uses the same setup.

## Decisions

- **Three repositories.** `cvkefridge` has the product documents and no app code. `cvkefridge-android` and
  `cvkefridge-ios` each have one app, its CI workflow, and its platform rules.
- **No shared code.** The Android app is Kotlin with Jetpack Compose. The iOS app is Swift with SwiftUI. We did not
  use React Native, Flutter, or Kotlin Multiplatform. Each app uses the components, the navigation, and the storage of
  its platform.
- **Mirrored core modules.** The product rules of the Android app are in the `:core` Gradle module, which is pure
  Kotlin. The product rules of the iOS app are in the `CVKEFridgeCore` Swift package, which uses Foundation only. A
  file in one module has a file of the same name in the other module, with the same behaviour and the same test cases.
- **Public repositories.** GitHub Actions is free for public repositories. The iOS app needs macOS runners for each
  build, because the development machine has no Xcode.

## Consequences

- A rule change needs the same change and the same test in both core modules.
- Two interfaces need two sets of UI work and two sets of UI tests.
- An intended difference between the apps needs an ADR in this repository. A difference without an ADR is a defect.
- The same file names do not prove the same behaviour. [The plan](../plan.md) recommends shared test vectors in this
  repository for that. That decision is open.

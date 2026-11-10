# Project rules: CVKE Fridge product

CVKE Fridge is a food inventory for the fridge with a native Android app and a native iOS app. It has three
repositories:

- [cvkefridge](https://github.com/Glebenator/cvkefridge): this repository, the product. The plan, the decisions (ADRs),
  the glossary, the product identity, and the legacy reference. It has no app code.
- [cvkefridge-android](https://github.com/Glebenator/cvkefridge-android): the Android app. Its `AGENTS.md` has the
  Android rules.
- [cvkefridge-ios](https://github.com/Glebenator/cvkefridge-ios): the iOS app. Its `AGENTS.md` has the iOS rules.

## Product

- Build native apps for publication on Android and iOS.
- Use ASD-STE100 Simplified Technical English for instructions and documentation.
- Implement only the agreed feature scope. Do not add inactive controls or simulated production data.
- `docs/plan.md` is a proposal until the owner agrees its open decisions. Do not treat a recommendation as agreed.
- `docs/legacy-fridgefriend.md` records the old app. It is a reference, not a specification.
- Commit and push only when the user asks.

## Shared rules for both apps

- Both apps have the same product rules and product behaviour. Keep platform behaviour native, and do not force shared
  UI code.
- Keep the product rules in the core module of each app: `:core` on Android and `CVKEFridgeCore` on iOS. A file in one
  module has a file of the same name in the other module, with the same behaviour and the same test cases.
- Change a product rule in both apps in the same piece of work. A feature is complete when both apps have it.
- Record each decision that affects both apps, and each intended difference between the apps, in an ADR in `docs/adr/`.
- Define each shared term in `GLOSSARY.md`. Use these terms in code, in the interface, and in issues.
- An expiry date is a calendar date. Calculate the days left from data. Do not write a fixed value.
- Show a value that is missing as missing. Do not show a guess as a fact.
- Explain each permission before the system asks for it. Provide a recovery action when access is off.
- Support light and dark appearance, large text, screen readers, and rotation.
- Keep the item list on the device. Do not add analytics, accounts, or cloud backup without an agreed product
  requirement.
- Use the network only for a feature that needs it. State in the interface what leaves the device.
- Do not write item names, barcodes, or photos to logs or to crash reports.

## Design

- `design/product.md` has the product identity. `design/product.css` and `design/product.json` have the generated
  colour values. Do not edit the generated files by hand. The command that makes them is in `design/product.md`.
- Each app copies the colour values into its theme file. Change the values in this repository first.

## Issues

- A feature or a decision that affects both apps has a parent issue in this repository, with one sub-issue in each app
  repository.
- The parent issue closes when both sub-issues are closed and both CI runs are green.

## Agent skills

### Issue tracker

Issues are in GitHub Issues. Use the `gh` CLI. App issues are in `Glebenator/cvkefridge-android` and
`Glebenator/cvkefridge-ios`. See `docs/agents/issue-tracker.md`.

### Triage labels

Use the five default triage labels: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`.
See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `GLOSSARY.md` and one `docs/adr/` at the root of this repository. See `docs/agents/domain.md`.

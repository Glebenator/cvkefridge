# Project rules: CVKE Fridge product

CVKE Fridge is a food inventory for the fridge with a native Android app and a native iOS app. One phone does each
task. The product has no fridge device. It has three repositories:

- [cvkefridge](https://github.com/Glebenator/cvkefridge): this repository, the product. The plan, the decisions (ADRs),
  the glossary, the product identity, the shared specification (`spec/`), and the legacy reference. It has no app code.
- [cvkefridge-android](https://github.com/Glebenator/cvkefridge-android): the Android app. Its `AGENTS.md` has the
  Android rules.
- [cvkefridge-ios](https://github.com/Glebenator/cvkefridge-ios): the iOS app. Its `AGENTS.md` has the iOS rules.

## Product

- Build native apps for publication on Android and iOS.
- Use ASD-STE100 Simplified Technical English for instructions and documentation.
- Implement only the agreed feature scope. Do not add inactive controls or simulated production data.
- `docs/plan.md` has the agreed scope and the open decisions. Do not treat a recommendation or an open decision as
  agreed.
- The app is complete on one phone with no other hardware and no connection. Do not add a feature that needs a
  device, an account, or a network connection to do its main task.
- Household sharing is deferred. `docs/household-sharing.md` is a design note, not agreed scope. Do not build it.
- `docs/legacy-fridgefriend.md` records the old app. It is a reference, not a specification. The rewrite does not copy
  the old app.
- Commit and push only when the user asks.

## Shared rules for both apps

- Both apps have the same product rules and product behaviour. Keep platform behaviour native, and do not force shared
  UI code.
- Keep the product rules in the core module of each app: `:core` on Android and `CVKEFridgeCore` on iOS. A file in one
  module has a file of the same name in the other module, with the same behaviour and the same test cases.
- Change a product rule in both apps in the same piece of work. A feature is complete when both apps have it.
- Record each decision that affects both apps, and each intended difference between the apps, in an ADR in `docs/adr/`.
- Define each shared term in `GLOSSARY.md`. Use these terms in code, in the interface, and in issues.
- Stock is products and batches (ADR 0003). Each change to the inventory is one record in the change log, and the
  inventory is the replay of the log (ADR 0005).
- `spec/` is the reference for the core rules (ADR 0004). To change a rule, change `spec/rules.md` and the vectors
  first, and run `python spec/tools/vectors.py --write`. Do not write an expected result by hand.
- Do not edit the copy of `spec/` in an app repository. Update it with `python scripts/update-spec.py <commit>`.
- An expiry date is a calendar date. Calculate the days left from data. Do not write a fixed value.
- Show a value that is missing as missing. Show an estimated date as an estimate. Do not show a guess as a fact.
- Explain each permission before the system asks for it. Provide a recovery action when access is off.
- Support light and dark appearance, large text, screen readers, and rotation.
- Keep the inventory on the phone. Do not add analytics or accounts.
- Use the network only for a feature that needs it. The product lookup is the only one. State in the interface what
  leaves the phone.
- Give each product, each batch, and each change a random identifier that is unique on all phones.
- Do not write product names, barcodes, or photos to logs or to crash reports.

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

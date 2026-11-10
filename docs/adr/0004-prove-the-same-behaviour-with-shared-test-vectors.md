# Prove the same behaviour with shared test vectors

The two apps share no code. The same file names in the two core modules do not prove the same behaviour. We keep one
set of test vectors in this repository, and both apps run them.

## Decisions

- **`spec/` in this repository is the reference.** It has the rules in words, the test vectors as JSON, and the table
  of foods.
- **Each app has an exact copy of `spec/`, and a file `spec.ref` with the commit of the copy.** We did not use a Git
  submodule, and we did not download the folder at build time. A build then needs no network, a checkout of an app is
  complete, and a release build has the table of foods that its tests read.
- **The CI of each app compares its copy with this repository at `spec.ref`.** A difference fails the build.
- **A reference model calculates the expected results.** `spec/tools/vectors.py` is a small Python model of the rules.
  The workflow `spec.yml` of this repository runs it for each push. Nobody writes an expected result by hand.
- **The table of foods is the USDA FSIS FoodKeeper data.** Its catalog entry gives the licence as CC0 1.0. The days
  are the minimum of each range from the date of purchase.

## Consequences

- A rule has three implementations: the reference model, Kotlin, and Swift. A rule change needs all three.
- A rule change is one commit here, and then one change of the copy and of `spec.ref` in each app. The two apps can be
  on different commits for a short time. A feature is complete when both are on the same commit.
- The reference model is not app code. No app runs it, and it has no screens and no storage.
- A food with a "Package use-by date" in the source has no estimate. The person enters the printed date.

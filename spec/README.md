# The shared specification

This folder has the product rules of CVKE Fridge in a form that both apps test against. It is the reference. An app
that does not agree with it has a defect.

| File | Contents |
|---|---|
| [rules.md](rules.md) | The core rules in words |
| [vectors/](vectors/) | Test vectors: inputs and expected results for each rule, as JSON |
| [foods.json](foods.json) | The table of foods: the days for the expiry estimate, the opened days, the after-date class, and the tips |
| [tools/vectors.py](tools/vectors.py) | The reference model. It calculates the expected results of the vectors. |
| [tools/build-foods.py](tools/build-foods.py) | Makes `foods.json` from the USDA FSIS FoodKeeper data |
| [tools/food-extras.json](tools/food-extras.json) | The common foods and the aliases, edited by hand. `build-foods.py` adds them to `foods.json`. |
| [tools/food-classes.json](tools/food-classes.json) | The after-date class of each FoodKeeper category and of single foods, edited by hand. `build-foods.py` adds the classes to `foods.json`. |
| [storage-hints.json](storage-hints.json) | The table for the storage hint of a looked-up product (rule 8), edited by hand |
| [before-date-tips.json](before-date-tips.json) | The table of the before-date tips and their sources (rule 10), edited by hand |

## How an app uses this folder

- Each app repository has a copy of this folder at `spec/`, and a file `spec.ref` with the commit of this repository
  from which the copy comes. The copy is exact. Do not edit it in an app repository.
- The core tests of each app read the vectors from `spec/vectors/` and run each case through the core module.
- The app puts `spec/foods.json`, `spec/storage-hints.json`, and `spec/before-date-tips.json` in its build as
  resources.
- The CI of each app gets this folder at the commit in `spec.ref` and compares it with the copy. A difference fails
  the build.
- To get a new version, run `python scripts/update-spec.py <commit>` in the app repository. It replaces the copy and
  writes `spec.ref`.

## How to change a rule

1. Change `rules.md`.
2. Add or change the inputs in the vector file. Change `tools/vectors.py` if the rule itself changed.
3. Run `python spec/tools/vectors.py --write`. It writes the expected results. Read the changes.
4. Commit and push. The workflow `spec.yml` runs `python spec/tools/vectors.py`, which fails if a vector file and
   the reference model do not agree.
5. Update the copy in each app repository and make both core modules pass.

## The vector files

Each case is a JSON object. Its `expect` value is the expected result. All other values are the input.

| File | Rule | Notes |
|---|---|---|
| `calendar-date.json` | 2 | Sections `parse`, `plusDays`, `daysUntil`, `order`, `dateOfInstant` |
| `freshness.json` | 3 | |
| `expiry-estimate.json` | 4 | It has its own small table of foods, so that a change to `foods.json` does not change it |
| `use-first.json` | 5 | The batches have no opened date, so the good-until date is the expiry date |
| `plan-use.json` | 6 | |
| `change-log.json` | 7 | Each case is a full log and the result of its replay |
| `food-table.json` | 4 | Facts about `foods.json`: the count, the usual storage kinds, the tips, the opened days, the after-date classes, and some foods. It proves that an app reads the whole table. |
| `storage-hint.json` | 8 | Sections `temperatures` and `cases`. It has its own small table of hints in `hints`, so that a change to `storage-hints.json` does not change it. |
| `storage-hints-table.json` | 8 | Section `facts`: the sizes of `storage-hints.json`. Section `cases`: the storage hints of real products with that table. A change to the table can change them. |
| `good-until.json` | 3, 5.2, 5.3, 6 | Section `cases`: the good-until date of a batch and its source, with the days left and the freshness. Section `order`: the use-first order with opened batches. Section `plan`: the plan of a use with opened batches. It has its own small table of foods. |
| `later-date-offer.json` | 9 | Section `classes`: the after-date class of a product. Section `cases`: the offer, or the reason for no offer. It has its own small table of foods. |
| `before-date-tips.json` | 10 | The tips that a batch shows. It has its own small table of foods, and its own small table of tips in `table`. |
| `before-date-tips-table.json` | 10 | Section `facts`: the sizes of `before-date-tips.json`. Section `cases`: the tips of batches with that table and `foods.json`. A change to one of the two tables can change them. |

Dates are text in the form `YYYY-MM-DD`. Quantities are whole thousandths. Instants are whole milliseconds from
1970-01-01T00:00:00Z. A value of `null` means that there is no value. A batch in an input can have no `dateType` key
and no `openedDate` key. It then has no date type and no opened date.

In the cases of `good-until.json`, `later-date-offer.json`, and the two files for the before-date tips, `today` is the
date of today, `product` is the product of the batch, and `storageKind` is the storage kind of the storage area of
the batch.

## The table of foods

`foods.json` comes from "FSIS - FoodKeeper Data" of the United States Department of Agriculture, Food Safety and
Inspection Service: <https://catalog.data.gov/dataset/fsis-foodkeeper-data>. The catalog gives the licence as CC0 1.0.
`tools/build-foods.py` has the rules of the conversion. A food can have no days for a storage kind, for example when
the source says "Package use-by date". The app then makes no estimate. A food can have tips: the text of the source
about how to keep the food in a storage kind. The app shows them as general advice (ADR 0012). A food can have
opened days: the days that the food keeps after its package is opened, from the "after opening" values of the source
(ADR 0013). Each food has an after-date class, which is not from the source: `tools/food-classes.json` has it
(ADR 0014).

To make the table again, run `python spec/tools/build-foods.py <path to foodkeeper.json> 2026-11-10` with the source
file of version FMA-Data-v128. The result is the same file, byte for byte.

## The table of before-date tips

`before-date-tips.json` is edited by hand. ADR 0015 says how the tips were selected. Each text has the words of its
source. The first sources are pages of the UK Food Standards Agency and of GOV.UK. They contain public sector
information licensed under the Open Government Licence v3.0. An app that shows a tip must show this statement with
its other licences.

## The table of storage hints

`storage-hints.json` is edited by hand. ADR 0011 says how its tags were selected. The storage texts and the tags in
`vectors/storage-hints-table.json` are from Open Food Facts, <https://world.openfoodfacts.org>, under the Open Database
Licence.

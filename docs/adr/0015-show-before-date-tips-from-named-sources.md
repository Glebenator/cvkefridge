# Show before-date tips from named sources

The owner asked for small tips before the date of a food, for example "ripe bananas are good for banana bread". A tip
must come before the date. It must not be a way to eat spoiled food. This ADR is the third part of the work that
ADR 0013 starts.

The expiry research ([expiry-dates.md](../research/expiry-dates.md), section 6) found that official sources give
advice for the time before the date: freeze the food, cook it, or use it up. ADR 0012 decided that no language model
writes a tip, and that each text comes from a source.

## Decisions

- **A before-date tip is a short text with a kind, a list of foods, and a source.** The kinds are `freeze`, `cook`,
  and `useUp`. The foods are foods of the table of foods. The glossary has the term. A before-date tip is not a
  storage tip (ADR 0012): a storage tip says how to keep a food.
- **The tips are in `spec/before-date-tips.json`, which is edited by hand.** The file has the sources, each with a
  name, a URL, and a licence, and the tips, each with an identifier, a kind, the foods, the text, and the key of its
  source. Both apps put the file in their build, as they do with `spec/storage-hints.json`.
- **Each text has the words of its source.** Only the capital letter at the start and the full stop at the end can be
  different. A text is one or two whole sentences of a paragraph, or one item of a list. No language model wrote or
  changed a text. We opened each source on 17 November 2026 and found the text in it.
- **A source must have a licence that permits a copy of its words.** The first sources are three pages of the UK
  Food Standards Agency and of GOV.UK, with the Open Government Licence v3.0. The licence asks for a statement of the
  source. The file has it (`attribution`), and each app must show it with its other licences.
- **No source, no tip.** The table starts with 4 tips for 19 foods:

| Tip | Kind | Foods | Source |
|---|---|---|---|
| `freeze-by-the-date` | `freeze` | 15 common foods: raw beef, lamb, pork, sausage, chicken, turkey, fish, and shrimp | Food Standards Agency, "How to chill, freeze and defrost food safely" |
| `cook-by-the-date` | `cook` | The same 15 foods | GOV.UK, "Understanding food labelling: Best before and use-by dates" |
| `use-overripe-fruit` | `useUp` | Apples, bananas, and strawberries | Food Standards Agency, "Home food fact checker" |
| `freeze-cooked-potatoes` | `freeze` | Potatoes | Food Standards Agency, "Home food fact checker" |

- **Rule 10 of `spec/rules.md` says which tips a batch shows.**
  - Only an expiring batch shows a tip: a batch with 0, 1, or 2 days left. A fresh batch does not need one. An
    expired batch never shows one, for a strict food and for a check food, so no tip says that expired food is good
    after it is cooked.
  - A tip of the kind `freeze` needs days for the freezer in the table of foods, and a batch that is not in a
    freezer.
  - The rule uses the good-until date (ADR 0013). A batch that is expiring because it is opened shows its tips.
- **The app shows the text as it is, with the name of its source.** The texts are in English only. The app does not
  translate them, as for the tips of the table of foods (ADR 0012).

## Sources that we did not use

- **Love Food Hate Waste (WRAP).** The server refused our requests (status 403), so we did not open a page, and we
  did not check its licence. The Food Standards Agency names it as a source of advice on food in the freezer.
- **The Voedingscentrum.** Its page on dates says the same as the tip `cook-by-the-date`, with 2 days. The text is in
  Dutch, and its licence is not checked.
- **The `CookingTips` sheet of the FoodKeeper data.** It has safe minimum temperatures in degrees Fahrenheit and notes
  about cooking methods. They say how to cook a food, not what to do before its date.
- **The freezer tips of the FoodKeeper data.** They are in the table of foods as storage tips (ADR 0012).

## Tips that we did not add

- **Eggs in the freezer.** The Food Standards Agency says that eggs can be frozen out of their shells. The table of
  foods has no days for the freezer for eggs in the shell, and rule 10 does not show a freeze tip for such a food.
- **Eggs after the best-before date.** The Food Standards Agency says that eggs are safe for a couple of days after
  the date if they are cooked well. That is advice for the time after the date. It is not a before-date tip.
- **Leftovers and cooked rice in the freezer.** The Food Standards Agency says to freeze leftovers as soon as
  possible, and cooked rice in one hour after cooking. A tip that shows two days later would not agree with its
  source.

## Results

- `spec/vectors/before-date-tips.json` has the cases for rule 10 with a small table. `before-date-tips-table.json`
  has the sizes of the real table and cases with the real tables. The reference model stops when a tip names a food
  that is not in the table of foods, and when a food of a freeze tip has no days for the freezer.
- The texts of the two tips for meat and fish have the words "use-by date". The app also shows them for a batch
  with a best-before date or with an estimated date. The advice is correct for these batches also, but the words are
  those of the United Kingdom.
- The table is small. Each new tip needs a source that a person opened, with a licence that permits the copy. Section
  8.2 of the plan has the decisions that the owner has to make: which sources are acceptable, and if a text can be a
  short sentence in our own words with a link to its source.
- A tip is advice from a public body. It is not a promise that one food is safe. The screens must not show a tip as
  a result of a check of the food.

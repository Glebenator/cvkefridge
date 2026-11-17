# Pause the product lookup after Open Food Facts fails

On 17 November 2026 Open Food Facts did not answer for a time. The address of the product lookup,
`world.openfoodfacts.org/api/v2/product/<barcode>`, gave no answer in 30 to 40 seconds in four attempts in about 20
minutes. The search address of the same server gave the status 503. The owner asked what the options are when this occurs.

The app did the correct things for one barcode: it showed the failure, it kept the barcode for "Enter by hand", and
the cache on the phone answered for products that it had. But the app waited for the timeout of 10 seconds again for
each new barcode. A person who puts away 20 foods then waits 20 times for an answer that does not come.

The owner selected two changes: a pause after a failure, and a second address of Open Food Facts as a fallback. The
check of the second address showed that it is not usable (see "Not done"). The owner did not yet decide about it
again, so this ADR records only the pause.

## Decisions

- **A failure of the server starts a lookup pause of 5 minutes.** These failures start it: no answer in time, an error
  of the server, an answer that the app cannot read, and a refusal (the status 429 or 503).
- **In the pause, the app sends no lookup by itself.** A scan or a typed barcode opens the add form at once, with the
  barcode and with no values from Open Food Facts. The form says: "Open Food Facts did not answer a few minutes ago,
  so the app did not look up this barcode. Type the name." The food keeps the barcode, as after "Enter by hand".
- **The inventory and the cache answer in the pause.** A barcode of a product in the inventory, and a barcode in the
  cache on the phone, give their result with no network, as before.
- **"Try again" sends a request in the pause.** The person asks for it, so the app sends it. This agrees with the
  rule that only the person can send a lookup again.
- **An answer of the server ends the pause.** "Found" and "not found" are answers. A new failure of the server starts
  the 5 minutes again.
- **A failure of the connection of the phone starts no pause.** It shows nothing about the server, and it fails
  quickly. When the phone has a connection again, the next scan must work.
- **The pause is in memory only.** It ends when the app stops. A clock that the person moved back also ends it.
- **The 5 minutes are a judgement.** The time must be longer than one session of scans after shopping would wait, and
  short enough that the lookup comes back quickly after a short failure. One failed request in each 5 minutes is the
  cost.

## Not done

- **No fallback to `search.openfoodfacts.org`.** This service of Open Food Facts ("Search-a-licious", version 0.1.0)
  answered on 17 November 2026 in 0.5 seconds for a barcode. But its data is old: all 7 products of the check had the
  date of the index between October and December 2024. The English name of the barcode 3017620422003 (Nutella) was
  "blueberry jam" there, and the product API gave "Nutella" on 12 November 2026. The service also has no storage text
  (`conservation_conditions`), so a product from it has no storage hint from its package. A product that is newer
  than the index is not there, and the app cannot know if "no result" means "not found".
- **No use of `world.openfoodfacts.net`.** It answered, but it is the test copy of Open Food Facts.
- **No second provider.** USDA FoodData Central and UPCitemdb need a key or have a limit for all users together, they
  have mostly products of the United States, and the text "Only the barcode number goes to Open Food Facts" on the
  scanner would not be true.
- **Not decided: a second lookup at a later time.** The app could look up the barcodes that the person saved by hand,
  when Open Food Facts answers again, and offer the name and the category. This changes the rule that the app never
  sends a lookup by itself.
- **Not decided: a table of products in the app.** The barcodes with the most scans, from the data export of Open
  Food Facts, would work with no connection. It makes the app larger, the data changes only with a new version of the
  app, and the licence of the database (ODbL) has conditions that the owner must check.

## Results

- The rule is in `lookup/ProductLookup.kt` of the Android app, with unit tests in `ProductLookupTest`: the pause for
  each kind of failure, its end after 5 minutes and after an answer, "Try again", the cache, no pause for a failure
  of the connection, and a clock that went back.
- The lookup has a new result, "paused", and a scan has a new source for the text of the add form.
- A food that the person adds in the pause has no values from Open Food Facts: no category from the tags, no storage
  hint, and no storage text. The app does not add them later.
- The device tests have no case for the pause. The unit tests do not show the text of the form on a phone.
- The iOS app has no product lookup yet (milestone 3). It gets the same rule when it builds the lookup. Before that,
  the rule moves into `spec/rules.md` with the other rules of section 6.1 of [plan.md](../plan.md).

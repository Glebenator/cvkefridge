# Expiry dates: sources, opened food, and food after its date

Date: 17 November 2026, first pass. The data in this report is from this date, unless a line gives a different date.

The owner asked how the app can have expiry dates that are as accurate as possible for as many foods as possible. The
owner gave four points: the date of some foods changes when the package is opened; some foods are still safe after
their date and some are not; some foods are safe after their date only if they are cooked; and the app must not tell
a person to eat spoiled food, but it can give a small tip before the date. The owner also asked for official sources
from Canada and from Europe, not only from the United States.

This report is the evidence. It is not a specification. On 17 November 2026 the owner said to build the features of
section 7. The decisions are in the ADRs that follow ADR 0012, and the rules are in `spec/`. If this report and an
ADR disagree, the ADR is correct.

Each claim has a source. Section 10 lists the sources and says how we read each one. If we did not read a page
ourselves, the report says so.

## Summary (one page)

**The main finding.** The app has good dates when it knows three things that it does not keep now: the type of the
date on the package, the date on which the package was opened, and the date on which the food was frozen or thawed.
A larger table of foods is the smaller part of the answer.

**What the app does not use now.**

- The FoodKeeper data has a time after opening for 202 of the 661 foods. `spec/tools/build-foods.py` does not read
  these values. Example: hot dogs keep 2 weeks in a closed package and 1 week in an opened package.
- "Still good?" (ADR 0009) shows "+1 day" and "+1 week" for each expiring and each expired batch. That includes raw
  chicken and food with a safety date.
- 17 of the 142 common foods have no estimate in their usual storage kind, for example milk, sour cream, bananas,
  avocados, and tomatoes.
- Open Food Facts does not help with dates. Its `expiration_date` field is the date of one package that a person saw
  at some time. It has no field for the time after opening of a food.

**The five most important findings.**

1. **All official sources agree: the date on the package is for the closed package only.** Health Canada, the CFIA,
   ANSES, the Voedingscentrum, the Verbraucherzentrale, and EFSA say it. After opening, the food has a shorter time,
   and the package or a table gives it. (Section 4.)
2. **The label does not mean the same in each region.** In the European Union and the United Kingdom, a safety date
   and a quality date are two different labels. In Canada, almost all food has the quality label, also raw meat. The
   United States has no federal rule. The app cannot decide from the label alone. Each food needs its own class.
   (Section 5.)
3. **For a safety date, the senses do not help.** Food Standards Scotland, the Voedingscentrum, and Health Canada say
   that food can look and smell normal and still make a person ill. For a quality date, the European sources say to
   look, smell, and taste. (Section 5.2.)
4. **Official sources give tips for the time before the date, not after it.** Freeze the food before its date. Cook
   it on or before its date. We found one official case of "after the date, but only if cooked": eggs. (Section 6.)
5. **The sources do not agree on the numbers.** Health Canada gives 3 days for opened milk. FoodKeeper gives 5 to 7
   days for opened long-life milk, 7 to 10 days for opened ultra-pasteurised milk, and no value for fresh milk. A
   careful app uses the shortest value. (Section 3.5.)

**Top recommendations** (section 7 has the full ranked list):

- Keep an opened date on a batch. Use the earlier of the expiry date and the opened date plus the time after
  opening.
- Keep the type of a printed date, and give each food a class for the time after its date. Do not show "Still good?"
  for a safety date or for a food of the strict class.
- Show tips while a batch is expiring: freeze it, cook it, or use it up. Each tip has a source.
- Let the person scan the printed date with the camera, and read the date from a 2D barcode when the package has
  one.

## 1. Method

- We read the plan, the glossary, `spec/rules.md`, `spec/tools/build-foods.py`, ADR 0009, ADR 0011, ADR 0012, and the
  competitor research (`competitor-apps.md`).
- We counted values in `spec/foods.json` and in the FoodKeeper source file (version FMA-Data-v128, the file that made
  `foods.json`) with short Python scripts.
- We asked the Open Food Facts product interface for three well-known products, with the fields for dates and
  storage.
- We read official pages of Canada, the European Union, France, the Netherlands, Germany, and Scotland with the
  Scrapling library (plain HTTP requests only, no tools that get around bot protection). We read one page of the
  Dutch storage guide in a browser, because the page makes its text with JavaScript.
- We used a web search tool for the other pages. A search gives a summary and not the page. Section 10 marks these
  sources.

**Limits.**

- We did not read the page of the French DGCCRF. The server refused the request (status 403). The points from it
  come from a search summary.
- We did not read the pages of the UK Food Standards Agency directly for this report. The address that we had gave a
  general page. The points from the FSA come from search summaries of `food.gov.uk`. The pages are now at `gov.uk`.
  The later work on the tips read them there, and `spec/before-date-tips.json` has the addresses.
- We did not find the Belgian list of times after the quality date for food banks.
- We did not check the licence of the Health Canada chart or of the Dutch storage guide. Do not copy their data into
  `spec/` before that check. The FoodKeeper data has the licence CC0 1.0.
- We looked at three products of Open Food Facts. That is an example, not a measurement.
- We did not find numbers for how many packages have a 2D barcode in 2026. The pages that we found are from sellers of
  barcode equipment.
- We did not test text recognition of a printed date on a phone.

## 2. CVKE Fridge now

- An expiry date is a printed date, an estimated date, or a chosen date (rule 5 of `spec/rules.md`). The person types
  the printed date. The estimated date is the date added plus the days of the food for the storage kind (rule 4).
- The table of foods has 661 foods from the FoodKeeper data. 339 have days for the freezer. 48 have no days for any
  storage kind: the source says "Package use-by date", "When Ripe", or "Indefinitely" for them.
- The days are the minimum of the range of the source, for a closed package ("date of purchase" values). The script
  does not use the values for "after opening" and "after thawing".
- A batch has no opened date. The glossary gives "Opened on Sunday" as an example of a note, so the person can write
  it, but the app does not calculate with it.
- A batch that moves from the freezer to the fridge keeps its date.
- The freshness is `expired` for each batch after its date. The app does not know if the date was a safety date or a
  quality date.
- "Still good?" is on the screen of the food for each expiring and each expired batch (ADR 0009).
- The storage tips card shows the storage text of the package and the general advice of the table (ADR 0012). The
  app already finds the words that start the instructions for an opened package in a storage text
  (`afterOpening` in `spec/storage-hints.json`), but it uses only the text before them.

## 3. The sources of a date

The most exact source comes first. A source that is about one package is better than a source that is about one
product, and a source about one product is better than a source about a food in general.

### 3.1 The printed date

The printed date is the best source. The maker of the food set it for this package. The work is to get it into the
app with little effort and with its type.

- **Typed.** The app has this now. The competitor research found that entry effort is the main reason that people
  stop (finding 1 of `competitor-apps.md`).
- **A scan of the printed date.** Text recognition on the phone can read the date with no network connection, which
  agrees with the product rule that the app is complete with no connection. The same scan can read the words next to
  the date, and these words give the type of the date (section 5.1). Printed dates have many forms. Canada puts the
  year first and uses two-letter month codes in two languages: "Best before 27 JA 30" is 30 January 2027 (CFIA). In
  the European Union, a food that keeps 3 to 18 months can show only the month and the year, and a food that keeps
  longer can show only the year (Verbraucherzentrale). A date such as `03/04/26` has two meanings. The scan must show
  what it read, and the person must confirm it.
- **A 2D barcode.** GS1, the organisation for barcodes, has a programme named "Sunrise 2027": at the end of 2027,
  shop checkouts can read 2D barcodes (GS1 DataMatrix, or a QR code with a GS1 Digital Link). These barcodes can hold
  the expiry date of the package. Application identifier 17 is the expiration date, in the form `YYMMDD`: `261231`
  is 31 December 2026. The date is an option of the maker, not a requirement. We know identifier 15 as the best-before
  date from the GS1 General Specifications, but no page that we opened in this research confirmed it. Check the
  specification before the parser is written. In 2026 few packages have such a barcode. The cost to read one is
  small, and the number of packages will go up.

### 3.2 The storage text of the package

Some packages say how long the food keeps after opening, for example "geöffnet gekühlt drei Tage haltbar"
(Verbraucherzentrale) or "eat within x days of opening" (ANSES). Open Food Facts has this text for some products in
its field for storage conditions, which the app already gets (ADR 0011). In samples for ADR 0012, 20 % to 45 % of
the most scanned products had a storage text. We did not count how many of these texts have a time after opening.

A time from the package is about this product. It is better than a time from the table of foods.

### 3.3 The table of foods

The FoodKeeper source file has more than the app uses.

| Values of the source | Foods | Used now |
|---|---|---|
| Days from the date of purchase, or general days, for a storage kind | 613 of 661 | Yes |
| Time after opening in the pantry (`Pantry_After_Opening`) | 75: 74 in days or longer, and 1 in hours. For 6 more foods the source says "Not Recommended" | No |
| Time after opening in the fridge (`Refrigerate_After_Opening`) | 145 | No |
| A time after opening in the pantry or in the fridge | 202 | No |
| Time in the fridge after thawing (`Refrigerate_After_Thawing`) | 3 | No |
| Cooking tips (`CookingTips` sheet) | 93 rows for 92 foods, 82 with a safe minimum temperature | No |

- 49 of the 142 common foods have a time after opening.
- 106 foods have days for the closed package in their usual storage kind and also a time after opening in the
  fridge. For 89 of them, the time after opening is shorter.
- Examples, closed package and then opened package: hard cheese 180 days and 21 days; hummus with preservatives 90
  days and 7 days; pre-packaged luncheon meat 14 days and 3 days; cottage cheese 14 days and 7 days; kefir 7 days
  and 1 day.
- The three foods with a time after thawing are chicken nuggets (1 to 2 days), frozen edamame (1 week), and frozen
  polenta (5 days). The table cannot give a general rule for thawed food.
- 34 foods have "Package use-by date" for the pantry or the fridge, for example fresh milk. For these foods the
  source gives no number, and the printed date is the only good source.

### 3.4 Open Food Facts

- The field `expiration_date` is a text that a person typed for one package: "12-2024" for Nutella, "31/07/2020" for
  a biscuit, and no value for a soft drink (three requests on 17 November 2026). The Open Food Facts wiki says that
  the field is for the people who edit the data, to tell an old package from a new one. Do not use it as an expiry
  date.
- A forum answer of Open Food Facts says that the "period after opening" field is in Open Beauty Facts, for
  cosmetics, and not in the food data. Our three requests for the field got no value.
- The useful fields stay the ones that the app has: the name, the category tags, and the storage text.

### 3.5 Other tables

**Health Canada, "Safe food storage".** A chart of 55 lines with a time in the fridge at 4 °C and a time in
the freezer at -18 °C. The page says that the fridge times are for safety and the freezer times are for quality. It
has separate lines for closed and opened hot dogs, lunch meat, milk, cottage cheese, yogurt, butter, and egg
substitutes.

| Food | Health Canada | FoodKeeper |
|---|---|---|
| Opened milk | 3 days | No value for fresh milk. Long-life milk 5 to 7 days, ultra-pasteurised milk 7 to 10 days |
| Opened yogurt | 3 days | No value after opening. 1 to 2 weeks from the date of purchase |
| Opened cottage cheese | 3 days | 1 week |
| Opened lunch meat | 3 to 5 days | 3 to 5 days |
| Opened hot dogs | 1 week | 1 week |
| Eggs in the shell | 3 to 4 weeks | 3 to 5 weeks |
| Whole chicken | 2 to 3 days | 1 to 2 days |
| Ground meat | 1 to 2 days | 1 to 2 days |
| Beef: steaks and roasts | 2 to 4 days | 3 to 5 days |

Neither source is always the shorter one.

**Voedingscentrum, "Bewaarwijzer" (the Netherlands).** The Voedingscentrum is the Dutch nutrition centre, which the
government pays for. Its storage guide has advice for more than 2 000 products. One page has the parts that the owner
asked about. The page for crisps says: opened, 2 to 5 days in the kitchen cupboard; not good for the freezer; the
sign of spoilage is that the crisps are less crisp; and for a closed package with a quality date, "up to 2 months
after the date or possibly longer, if it still looks good and the package is whole". This is the best model that we
found for the data of the app: a time after opening for each storage kind, a sign of spoilage, and a time after the
quality date. The licence is not checked.

### 3.6 When two sources disagree

Use the shortest time. Keep the source of each value in the data, so that the interface can name it. This agrees
with the rule of `build-foods.py`, which already takes the minimum of a range.

## 4. Opened, frozen, and thawed food

**Opened.**

- Health Canada: "best before" dates "apply to unopened products only. Once opened, the shelf life of a food may
  change."
- ANSES: a use-by date "is no longer valid once it has been opened". Follow the time on the package.
- The Voedingscentrum and the Verbraucherzentrale say the same for both types of date. The Verbraucherzentrale gives
  the reason: oxygen, moisture, and microorganisms get into the opened package.
- The DGCCRF (search summary): the quality date has no use after the package is opened. Dry food with a date as "end
  of" a month or a year is an exception: it keeps until the date also when the package is open.
- EFSA guidance part 2 gives makers of food a decision tree with five questions. The result is one of two: the time
  after opening is the same as the date of the closed package, or it is shorter. It is the same for food in which
  pathogens cannot grow, such as fresh orange juice (pH 3.6). It is shorter when opening changes the conditions, for
  example for sliced cooked meat in a vacuum package: the vacuum is lost. EFSA gives no numbers of days.

So an opened date can make the date earlier, and it never makes it later. The app needs the date of opening and a
time after opening from the package (3.2) or from the table (3.3).

**Frozen.**

- The FSA (search summary): a person can freeze pre-packaged food "until midnight on the use by date".
- Food Standards Scotland: some foods can be frozen up to the use-by date.
- ANSES: freezing on the use-by date is possible, but it is better to freeze the food soon after it is bought.
  Freezing stops the growth of bacteria. It does not kill most of them.
- The DGCCRF (search summary) is more strict: do not freeze a food when its use-by date is near, reached, or past.
- The Voedingscentrum: freeze a food with a use-by date in time, and it keeps for months.

**Thawed.**

- The FSA (search summary): use defrosted food within 24 hours.
- EFSA: for food that was frozen for donation, use it within 24 hours after thawing. One national guideline that
  EFSA read (Food Safety Authority of Ireland) lets a person keep thawed food for 3 days.
- ANSES: eat defrosted food "quickly (within three days)". Do not freeze it again.

A careful app gives thawed food 1 day in the fridge, unless the table has a time for that food.

## 5. Food after its date

### 5.1 The labels by region

| Region | Safety date | Quality date | Other |
|---|---|---|---|
| European Union | "Use by": "te gebruiken tot" (TGT), "à consommer jusqu'au" (DLC), "zu verbrauchen bis". Food is not sold and not eaten after it. | "Best before": "ten minste houdbaar tot" (THT), "à consommer de préférence avant" (DDM), "mindestens haltbar bis" (MHD). Food can be sold and eaten after it. | No date is necessary for fresh fruit and vegetables, wine, drinks with 10 % alcohol or more, vinegar, salt, sugar, sweets, and chewing gum. |
| United Kingdom | "Use by", with the same meaning | "Best before", with the same meaning | The same list. Eggs have a "best before" date of not more than 28 days after they are laid. |
| Canada | No safety date for normal food. "Use by" can be on fresh yeast only. "Expiration date" is on infant formula, meal replacements, nutritional supplements, and formulated liquid diets: throw the food away after it. | "Best before" / "meilleur avant", a requirement only for food that keeps 90 days or less. It is also on raw meat. | "Packaged on" for food that a shop packs. Food that keeps more than 90 days needs no date. |
| United States | No federal rule, but for infant formula | Words that the maker selects | The FoodKeeper data is the federal advice for times. |

Sources: Regulation (EU) No 1169/2011 as the Voedingscentrum and the Verbraucherzentrale describe it; Food Standards
Scotland; Health Canada; the CFIA.

The result for the app: in Europe the type of the date tells much. In Canada and in the United States it tells
little, because raw chicken and crackers have the same words. The CFIA says: "Best before dates are not indicators of
food safety, neither before nor after the date."

### 5.2 What the sources say about the senses

- **Safety date.** Food Standards Scotland: "It is not suitable to use the 'sniff test'", and milk with a use-by date
  "should never be sniffed or used past the use-by date". The Voedingscentrum: a person cannot see, smell, or taste
  the pathogens.
- **Quality date.** The Voedingscentrum: "Kijk, ruik en proef" (look, smell, and taste). The Verbraucherzentrale:
  trust your senses. Food Standards Scotland: it is safe to use smell or appearance, for example mould on bread.
  ANSES: eating a product after this date "does not pose a health risk", but throw away a package that is swollen
  and a jar that does not make a sound when it opens.
- **Canada is more careful.** Health Canada: "Never use your nose, eyes or taste buds to judge the safety of food. If
  in doubt, throw it out." It says this on the same page that says a person can eat food after the "best before"
  date.
- **One exception to a safety date.** ANSES: yogurt can be eaten a few days after its use-by date, because it is
  acid and full of culture. ANSES says that this is for yogurt only, not for other fresh dairy desserts.

### 5.3 Times after the quality date

- EFSA did not give times (search summary of its guidance part 1). The text of part 2 notes that some member states
  have their own guidance.
- WRAP (United Kingdom, a press release about its guidance for the redistribution of food, 23 April 2020): bread 2
  days; other packaged bakery up to 1 week; crisps 1 month; biscuits and cereals 6 months; canned meat, canned soup,
  sweets, drinks, and pasta sauce 12 months; dried pasta up to 3 years; jam 3 to 5 years; fresh uncut fruit and
  vegetables from 1 day to 2 weeks.
- The Voedingscentrum gives a time for each product of its storage guide (3.5).
- Canada gives no times.

These times are for people who give food away and for people who look at the food. They are not promises. If the
app shows one, it must name the source and say that the person must check the food.

### 5.4 People at higher risk

ANSES and Health Canada name the same groups: pregnant women, children below 5 years, older people (Health Canada:
above 60 years), and people with a weak immune system. ANSES says that these groups must follow the dates exactly.

## 6. Tips before the date

The owner gave the example that old bananas are good for banana bread. The official sources support tips of three
kinds, all for the time before the date.

| Kind | What the source says | Source |
|---|---|---|
| Freeze | Freeze a food with a use-by date in time. It keeps for months. | Voedingscentrum; FSA (search summary); Food Standards Scotland |
| Cook | Cook a food with a use-by date on or before the date, close it well, and keep it cold. It keeps 2 more days. | Voedingscentrum |
| Cook thoroughly | Eggs can be eaten 1 or 2 days after their "best before" date if they are cooked thoroughly, for example hard-boiled or in a cake. | Food Standards Scotland |
| Use up | The quality of a food with a quality date goes down slowly: bread goes stale, biscuits go soft, the skin of a banana in the fridge goes black. | Food Standards Scotland; FoodKeeper tip for bananas |

- We did not find an official source that says that cooking makes spoiled food safe. ANSES says that cooking to 70 °C
  in the centre kills most pathogens, as advice for food that is in date. A tip must not say more than its source.
- The FoodKeeper `CookingTips` sheet has a safe minimum temperature for 82 foods. It can be the source for a "cook"
  tip.
- A tip for an idea such as banana bread needs a source also (ADR 0012: no language model writes a tip). Love Food
  Hate Waste, the consumer programme of WRAP, publishes such ideas. We did not read its pages in this pass.
- The time of a tip is important. A tip while the batch is expiring helps the person to use the food. The same tip
  after the date reads as "eat it".

## 7. Recommendations

Each item names its evidence (E) and what is judgement (J).

1. **An opened date on the batch.** The person records that a batch is opened, with one tap or when they record a
   part of the batch as used. The date that the app uses is the earlier of the expiry date and the opened date plus
   the time after opening. Take the time from the storage text of the package first, and from the table of foods
   second. Show the result as an estimate. (E: section 4, all sources; 202 foods of the source have a time. The
   competitor apps FridgeBuddy and others have "opened", see recommendation 5 of `competitor-apps.md`. J: the rule
   "the earlier of the two"; a pack of 6 yogurts is one batch, and one opened yogurt does not open the others.)
2. **The type of a printed date.** The batch keeps if its printed date is a safety date, a quality date, or not
   known. The scan of the date fills it in, or the person selects it. (E: section 5.1. J: the words for the
   glossary. The glossary now says to avoid "best before" and "use by" for the expiry date.)
3. **A class for each food of the table.** A strict class for food that is not safe after its date: raw meat,
   poultry, fish, deli meat, soft cheese, prepared food, cut produce, and infant food. A second class for food that
   the person can check. A food with no clear class is strict. The class is necessary because the label is not
   enough in Canada and in the United States. (E: sections 5.1 and 5.2. J: the list of foods in each class.)
4. **No "Still good?" for a safety date and for the strict class.** For these batches the app says to throw the food
   away. For the other batches, "Still good?" stays, with the sign of spoilage of the food. This changes ADR 0009.
   (E: section 5.2; the owner's rule that the app is careful.)
5. **Tips while a batch is expiring.** Freeze, cook, and use up, from a file that is edited by hand, each with its
   source. No tip that suggests eating a strict food after its date. (E: section 6. J: which foods get a tip
   first.)
6. **A scan of the printed date.** Text recognition on the phone, with a confirmation step. (E: section 3.1;
   finding 1 of `competitor-apps.md`. J: the forms of date that the parser reads.)
7. **The date from a 2D barcode.** Read application identifiers 15 and 17 when the barcode has them. (E: section
   3.1. J: the value in 2026 is small.)
8. **A short time for thawed food.** A batch that moves from a freezer to a fridge gets 1 day, or the time of the
   table. A batch can go to the freezer on or before its date only. (E: section 4. J: 1 day and not 3 days.)
9. **The shortest value when sources disagree, and the source with each value.** (E: section 3.5.)
10. **Do not show a time after the quality date as a promise.** If the app shows one, it names the source and tells
    the person to check the food. (E: section 5.3: EFSA and Canada give no times.)
11. **Later: a careful mode.** A setting for a household with a person of a group of section 5.4. It removes "Still
    good?" and the times after the date for all food. (E: section 5.4. J: all of it; no source asks for an app
    setting.)
12. **Do not use the `expiration_date` of Open Food Facts.** (E: section 3.4.)

## 8. Effects on the current decisions

- **ADR 0009** gives "Still good?" to each expiring and each expired batch. Recommendation 4 limits it.
- **`spec/tools/build-foods.py`** says that the values for "after opening" and "after thawing" are not used.
  Recommendations 1 and 8 use them.
- **The glossary** defines the expiry date as "the calendar date after which the batch is not good to eat". That is
  true for a safety date. For a quality date, the food is often good after it.
- **Rule 3 of `spec/rules.md`** gives `expired` to each batch below 0 days left. The interface can need different
  words for a quality date that is past.
- **Rule 4** says that the core does not use the category for an estimate. That stays. The class of recommendation 3
  is for food of the table. A product with no food of the table needs its own decision.
- **ADR 0012** says that each tip comes from a source. Recommendation 5 keeps that rule.

## 9. Open questions

- The licence of the Health Canada chart and of the Voedingscentrum storage guide, before any of their values go into
  `spec/`.
- The 17 common foods with no estimate in their usual storage kind. Fresh milk and plant milk have the package date
  only. Bananas, avocados, kiwi fruit, melons, peaches, pineapple, and tomatoes have "When Ripe" in the pantry. A
  source for a time on the counter is necessary, or the app continues to give no estimate.
- A batch with a quantity above 1 where one piece is opened.
- The class of a product that is not in the table of foods.
- How many storage texts of Open Food Facts have a time after opening.
- The Belgian and the other national lists of times after the quality date.
- A test of text recognition with real packages from Canada and from Europe.

## 10. Sources

Read directly on 17 November 2026 with the Scrapling library, if no other method is given.

**Canada**

- Health Canada, "Safe food storage":
  <https://www.canada.ca/en/health-canada/services/general-food-safety-tips/safe-food-storage.html>
- Health Canada, "How to read food date labels and packaging":
  <https://www.canada.ca/en/health-canada/services/general-food-safety-tips/how-read-food-date-labels-packaging.html>
- Canadian Food Inspection Agency (CFIA), "Best before, expiration and more" (date modified 25 March 2026):
  <https://inspection.canada.ca/en/food-labels/labelling/consumers/date-labels-food>

**European Union**

- EFSA, "Guidance on date marking and related food information: part 2 (food information)", EFSA Journal 2021:
  <https://www.efsa.europa.eu/en/efsajournal/pub/6510>
- EFSA, "Guidance on date marking and related food information: part 1 (date marking)", EFSA Journal 2020 (search
  summary): <https://efsa.europa.eu/en/efsajournal/pub/6306>
- European Commission, "Date marking and food waste prevention":
  <https://food.ec.europa.eu/food-safety/food-waste/eu-actions-against-food-waste/date-marking-and-food-waste-prevention_en>

**France**

- ANSES, "Use-by date (UBD) and date of minimum durability (DMD)":
  <https://www.anses.fr/en/article/use-date-ubd-and-date-minimum-durability-dmd>
- DGCCRF, "Date limite de consommation et date de durabilité minimale" (search summary; the server refused our
  request):
  <https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/date-limite-de-consommation-et-date-de-durabilite-minimale-ce-que-vous-devez-savoir>

**The Netherlands**

- Voedingscentrum, "Twee houdbaarheidsdatums": <https://www.voedingscentrum.nl/encyclopedie/houdbaarheidsdatums-tht-tgt.aspx>
- Voedingscentrum, "Eten bewaren (Bewaarwijzer)", and its page for crisps (read in a browser):
  <https://www.voedingscentrum.nl/nl/thema/kopen-koken-bewaren/eten-bewaren.aspx>

**Germany**

- Verbraucherzentrale, "Mindesthaltbarkeitsdatum (MHD) ist nicht gleich Verbrauchsdatum":
  <https://www.verbraucherzentrale.de/mindesthaltbarkeitsdatum>. The Verbraucherzentrale is a consumer organisation
  with public money. It is not a government office.
- Federal Ministry of Agriculture, Food and Regional Identity, "Mindesthaltbarkeits- und Verbrauchsdatum" (search
  summary):
  <https://www.bmleh.de/DE/themen/ernaehrung/lebensmittelverschwendung/mindesthaltbarkeit-kein-verfallsdatum.html>

**United Kingdom**

- Food Standards Scotland, "Use-by and best-before dates":
  <https://www.foodstandards.gov.scot/consumer-advice/food-labels/use-by-and-best-before-dates>
- Food Standards Agency, "How to chill, freeze and defrost food safely" (search summary):
  <https://www.food.gov.uk/news-updates/campaigns-0/germwatch/science-fsw/freezing>
- WRAP, "Best Before dates shouldn't be a barrier to redistribution", 23 April 2020 (read with a page fetch tool):
  <https://wrap.ngo/media-centre/press-releases/best-dates-shouldnt-be-barrier-redistribution>

**United States**

- USDA FSIS, FoodKeeper data, version FMA-Data-v128, licence CC0 1.0 (the source file, counted with a script):
  <https://catalog.data.gov/dataset/fsis-foodkeeper-data>

**Product data and barcodes**

- Open Food Facts, product interface, three requests for the barcodes 3017620422003, 5449000000996, and
  7622210449283: <https://world.openfoodfacts.org>
- Open Food Facts wiki, "Data fields" (search summary): <https://wiki.openfoodfacts.org/Data_fields>
- Open Food Facts forum, "Best before date of food items" (search summary):
  <https://forum.openfoodfacts.org/t/best-before-date-of-food-items/114>
- GS1 Digital Link and Sunrise 2027, trade pages (search summary, weak sources):
  <https://barkoder.com/blog/gs1-digital-link-explained-the-qr-code-that-replaces-your-barcode>,
  <https://www.videojet.com/us/homepage/resources/learn/gs1-sunrise-2027.html>

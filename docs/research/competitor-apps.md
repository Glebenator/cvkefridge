# Competitor apps: fridge, freezer, and pantry trackers

Date: 12 November 2026, first pass and second pass. The data in this report is from this date, unless a line gives a
different date.

This report compares CVKE Fridge with 22 apps that track food at home, and with 4 adjacent apps. It looks at the
interface and at the features. It ends with a ranked list of recommendations. The owner asked for it to help decide
the filter header of My Fridge and the next features.

Each claim has a source. A claim about a screen comes from a store screenshot that we looked at, or from a page that
shows the screen. If we did not see a screen, the report says so. Ratings and review counts change each day.

## Changes in the second pass

The owner asked for a deeper pass on four points. This is what changed.

**New evidence.**

- **Reviews.** We read about 400 user reviews and comments, not 3 or 4 for each app. Section 3A gives the themes with
  counts. Sources: the full review list on Google Play, the App Store review feed (50 reviews a page), the Wayback
  Machine for removed apps, and Hacker News. Reddit was not available: our search tool and our browser both block it.
- **Screens.** For each list screen, section 6 now says if we saw the running app or only a store image. We saw the
  running app only for Grocy (public demo) and for the add screen of KitchenPal (a video from the developer). The web
  apps of NoWaste and Expireless need a sign-in, so we did not open them.
- **Apps not seen in the first pass.** CozZo and Fridgely: archived App Store pages with screenshots and reviews. Well
  Stockd: its own product pages and a picture of its kitchen screen. Kitche: no store page found now.
- **New apps.** A search of Google Play in Germany, Japan, Korea, France, and the UK found 5 apps with real traction
  that the first pass missed: Smantry (Germany), InvenDo, MyKURA (Japan), Best Before, and My Pantry. Section 3 adds
  them.
- **The category control.** Section 6A answers the open question about rows that scroll sideways.

**Corrections to the first pass.**

| First pass said | Second pass found |
|---|---|
| Your Food Premium is $7.99 one time. | The price went up in 2026. Reviews from August 2026 give about £43 one time or £15 a year. The App Store lists $7.99 and $44.99 one-time items. |
| Well Stockd: the grouped list was not verified. | Confirmed from its own product picture: category chips, a sort dropdown, and groups for Fridge and Pantry. It is a web app that started in October 2026. |
| CozZo and Fridgely: screens not verified. | Seen in archived store images. Both use a list of storage areas first, then a screen for each area. |
| KitchenPal: tabs for each storage area are a good example. | The tabs have no "All" view. A user complains that they must open each fridge and freezer to see everything. |
| FridgeBuddy: categories "?" in the matrix. | Users ask for categories, so the app did not have them when they wrote (2024 and 2025). |
| Data loss is one complaint among others. | Data loss and lock-out are the largest complaint by count for NoWaste on iOS: 17 and 9 of 50 reviews. |
| Kitche is available on Android and iOS. | We found no Kitche page on Google Play UK or in the UK App Store on 12 November 2026. |
| Recommendation: a scrolling row of category chips. | Changed. Section 6A recommends one category menu chip. Wrapped chips are the second choice. |

## Summary (one page)

**What CVKE Fridge is now.** Two screens. Home shows the totals and the batches that need attention. My Fridge shows a
search field, one row of chips for the storage area, one row of chips for the category, and a sort menu in the top
app bar. The app cannot add or edit food yet. The plan adds the barcode scanner (milestone 3), reminders (milestone
4), and the history of used and thrown-away food (milestone 5). The app keeps all data on the phone, with no account.

**The market.** The market has many small apps and few large ones. The largest dedicated trackers that we found on
Google Play are KitchenPal (100K+ downloads, 6.7K reviews) and MyKURA in Japan (100K+ downloads, 1K reviews). Smantry
(Germany, 2.3K reviews), InvenDo (1.7K reviews), NoWaste, Your Food, Wonder Fridge, Best Before, and My Pantry each
have 50K+ downloads. A Play search for "food expiry tracker" gives more than 30 apps, and most of them are new and
have no ratings. CozZo, Fridgely, and Kitche are no longer in the stores that we checked.

**The five most important findings.**

1. **Food entry effort is the main reason that people stop.** Users complain about too many steps after a scan, about
   wrong or empty dates after a scan, and about the work to enter a whole kitchen. One writer stopped using Grocy
   after one week for this reason, and 6 Hacker News comments say the same about Grocy. Small details cost time: a
   date wheel instead of a number field (Smantry), a form that closes after each item (Smantry, Wonder Fridge), a
   slider instead of a typed number (NoWaste). The apps that users praise make entry short: a scan, a suggested date,
   and done. (Evidence: section 3A.)
2. **Most apps put the storage area first, and the good ones also have an "All" view.** KitchenPal, Expireless,
   Wonder Fridge, and MyKURA use tabs. NoWaste, FridgeBuddy, CozZo, and Fridgely use a list or a screen for each
   storage area. FridgeWise, What The Fridge?!, Smantry, and Well Stockd show one list with a storage control or
   storage groups. Users complain when there is no view of all food (KitchenPal) or no search across all lists (My
   Pantry). The category is always second: a chip row, a dropdown, a filter sheet, folders, or section headers. No app
   that we saw shows two equal rows of chips, as My Fridge does now.
3. **"Use first" is the view that users value most.** Users praise sort by expiry, "what is expiring" lists, and
   colour for days left. Expireless calls its default order "Use first". Pantry Check has a separate Expiring tab.
   What The Fridge?! and FridgeWise put the counts of expired and expiring food at the top, as CVKE Home does.
4. **Lost data and lost access are the largest complaints by count.** In 50 App Store reviews of NoWaste, 17 report
   lost data and 9 report that they cannot sign in again. Most of these came after a change to accounts and a
   subscription in November 2020. KitchenPal, Your Food, Pantry Check, and Smantry have the same kind of reports in
   smaller numbers. Paywalls and limits are the next complaint: free limits of 30 items (Smantry), 200 items (Pantry
   Check), and 500 items (NoWaste), and paid barcode scans (KitchenPal).
5. **The best ideas for a freezer and for opened food are small.** FridgeBuddy moves the date forward when food is
   opened. Expireless sets a new fridge date when food comes out of the freezer, and it sorts the freezer by age. Users
   of Your Food and FridgeBuddy ask for a "frozen on" date and for days instead of months.

**What CVKE Fridge already does well against the market.** An expiry estimate from the USDA FoodKeeper table for each
storage kind, a printed date that replaces the estimate, batches with their own dates, undo, the end of a batch as
used or thrown away, and no account. Few competitors have all of these.

**Top recommendations** (section 8 has the full ranked list):

- My Fridge: make the storage area a row of tabs ("All", Fridge, Freezer, and the created areas). Below it, put one
  row that does not scroll: a "Category" menu chip and two freshness chips, "Expiring" and "Expired". Do not use a
  filter sheet as the main control. Section 6A gives the evidence and the second choice (wrapped chips).
- Make the add flow one screen after a scan: name, storage area, and an estimated date that is already filled in, with
  "Save" and "Scan next".
- Add a swipe or one tap for used and thrown away on the card, with undo.
- Add an export of the inventory before the first release, so that a person can keep a copy.

## 1. Method

- We read the CVKE Fridge plan, the glossary, the ADRs, `design/product.md`, and the two Android screens
  (`MyFridgeScreen.kt`, `HomeScreen.kt`).
- We read the Google Play page and the App Store page of each app, when the app has one, in the US store (the UK store
  for FridgeBuddy). We read the ratings, the review counts, the downloads, the update date, the description, the
  in-app purchases, and the reviews that the page shows.
- We opened the store screenshots in a browser when the text did not show the list screen. Section 6 uses only the
  screens that we saw.
- We read independent pages: forum threads, articles, and review sites. Many search results were directory or
  marketing pages. The report marks them as weak sources.
- We did not install an app, sign in, or create an account. We did not use a paid function.

**Second pass.**

- Google Play: we opened the full review list ("See all reviews", sorted by most relevant) and read 20 to 44 reviews
  for each main app. For Smantry we read the German store.
- App Store: we read the public review feed of the App Store (`itunes.apple.com/.../rss/customerreviews`), which
  gives up to 50 recent reviews for each country.
- Removed apps: we read archived App Store pages of CozZo (February 2025) and Fridgely (October 2023) in the Wayback
  Machine.
- Hacker News: we searched the comments with the Algolia search interface.
- New apps: we searched Google Play in Germany, Japan, Korea, France, and the UK with the Scrapling library (plain HTTP
  requests only, no tools that get around bot protection), and read the pages of the apps with many reviews.
- Design evidence: Material Design documentation for chips and tabs, and Baymard Institute research on horizontal tabs.

**Limits.**

- Google Play and the App Store choose and order the reviews. These reviews are examples, not a random sample. The
  counts in section 3A show how often a theme came up in what we read. They do not measure the whole user base.
- Store screenshots are marketing images. The real app can be different.
- Reddit was not available. Our web search tool cannot read reddit.com, and the browser does not open it. We did not
  try to get around this. The report has no Reddit evidence.
- We did not read Trustpilot. Our searches found Product Hunt pages only for new apps from their makers, not reviews
  of the main apps.
- We could see only one video of a running app (KitchenPal, from the developer). The browser closed during the second
  video, and we did not open more.
- The three recent FridgeWise reviews on Google Play are all short, positive, and from the last month. Use them with
  care.
- We could not see the screens of CozZo, Fridgely, Well Stockd, Kitche, and the Samsung Food pantry.

## 2. CVKE Fridge now

| Area | CVKE Fridge (Android, 12 November 2026) |
|---|---|
| Add food | Not yet. Plan: barcode scan with Open Food Facts, or a typed name. A suggested expiry date from the table of foods. |
| Organisation | My Fridge: one card for each food in each storage area. Search field. One chip row for storage area and one chip row for category, each with "All" and only the values that have food. Sort menu: name, expiry, date added, quantity, category. |
| Expiry | Printed or estimated date. Freshness: fresh, expiring, expired, no expiry date. Days left as "Expires in 5d". Estimate shown as an estimate. |
| Home | Greeting, totals card (foods, expiring, expired), "Needs attention" row of the first 5 batches, "View all". |
| End of a batch | Plan: used or thrown away, with a history and undo. |
| Other | No account, no sync, no shopping list, no reminders yet. Household sharing deferred. |

## 3. The apps, one by one

Each entry gives: platforms, price, popularity, how food is added, organisation, expiry, other features, the
interface, and what users say.

### 3.1 NoWaste: Food Inventory Lists (KH Creations ApS)

- **Platforms and price.** Android, iOS, iPad, Mac, and a web app. Free, with NoWaste Pro: $6.99 to $14.99 a year or
  $29.99 to $69.99 one time on iOS. Free limits: 6 lists and 500 items ([chrome-stats summary](https://chrome-stats.com/d/com.khcreations.nowaste)).
- **Popularity.** Google Play: 3.0 stars, 303 reviews, 50K+ downloads, updated 11 Nov 2026. App Store: 4.2 stars,
  758 ratings. ([Play](https://play.google.com/store/apps/details?id=com.khcreations.nowaste),
  [App Store](https://apps.apple.com/us/app/nowaste-food-inventory-list/id926211004))
- **Add food.** Barcode, receipt, or photo scan. Typed entry ("Write"). Pro: CSV or text import, and a scan of the
  printed date.
- **Organisation.** A separate list for each storage area (freezer, fridge, pantry) and for each place (home, cabin,
  boat). Custom categories with 100+ icons. Sort, filter, and search.
- **Expiry.** Dates and reminders before expiry. Cards show "Expired", "Opened", and "Expires in 4 days" tags (seen in
  a store screenshot).
- **Other.** Shopping lists, recipes, meal plans in a calendar, members of a household, waste statistics ("My
  numbers"), prices from receipts.
- **Interface (seen).** The top of the list has a dropdown that shows the place and the list ("Home › Freezer +4") and
  a search button. A "Sort" link is above the cards. Each card shows the name, the days left, the storage area, and
  tags. A bar at the bottom has three add actions: Write, Scan, Photo. The tab bar has Inventory, Planning, Locations,
  Profile.
- **Users praise.** Sort by expiry date to avoid waste; many suggestions when you type a name; useful for a large
  household with many lists. ([Play reviews](https://play.google.com/store/apps/details?id=com.khcreations.nowaste),
  [App Store reviews](https://apps.apple.com/us/app/nowaste-food-inventory-list/id926211004))
- **Users complain.** A paying user lost a list of 350+ items: the count stayed, but the list was empty (41 people
  found this helpful). The scan did not find most products, so dates had to be typed. Too many steps after each scan
  (edit, quantity, amount, type, back), and the default date is "expires today". Wrong storage area from a receipt
  (dry beans in the fridge). A crash lost about 20 scanned items.

### 3.2 KitchenPal: Pantry Inventory (iCuisto Pte Ltd)

- **Platforms and price.** Android, iOS, iPad, Mac. Free, with Premium: $3.99 a month, $14.99 a year, $29.99 one time,
  or $39.99 for a family ([App Store](https://apps.apple.com/app/id1084982489)).
- **Popularity.** Google Play: 4.6 stars, 6.72K reviews, 100K+ downloads, updated 29 Oct 2026
  ([Play](https://play.google.com/store/apps/details?id=fr.icuisto.icuisto)). App Store: 4.5 stars, 720 ratings.
- **Add food.** Barcode (5M+ products, unlimited scans are Premium), voice, or text. Receipt analyser (in "What's
  new").
- **Organisation.** Storage sections: pantry, fridge, freezer, cleaning supplies, bar. Custom sections and categories
  are Premium. Filters and sort in the kitchen (version notes).
- **Expiry.** Dates, with automatic dates for some items such as produce. Alerts before expiry. "Running low"
  tracking.
- **Other.** Shared kitchen and shopping lists in real time, recipes that match the inventory, meal planner, diet
  filters, savings and waste tracker.
- **Interface (seen).** A "Kitchen" top bar with search. Below it, **tabs for each storage section** (Fridge, Freezer,
  Cellar). A "Sort by Expiry" control with a direction arrow, and a grid or list switch. The grid shows product photos,
  days left ("21d", "30d"), and − and + buttons for the quantity on each tile.
- **Users praise.** Sharing between phones stopped double purchases; barcode scanner and expiry tracking; the link from
  recipes to the shopping list.
- **Users complain.** Recipe matching is not reliable; some items have the wrong category; the automatic add picks the
  wrong shopping list; items are hard to move between lists; "buggy at times". Adding uncommon items is tedious
  ([KitchenPal summary](https://alternativeto.net/software/kitchenpal/about)).
- **Second pass.** The tabs have no view of all food. One user, who has many fridges and freezers, says that they must
  open each one to see the total. Other users say that the fixed categories are too coarse for a large pantry, and
  that custom categories are a paid function ([App Store feed](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1084982489/sortby=mostrecent/json)).
  A developer video shows the running add screen: suggested shelf lives as chips ("3 months", "6 months", "1 year")
  and the storage choice as wrapped chips (Fridge, Pantry, Freezer, Spices, Beverages, Others)
  ([YouTube](https://www.youtube.com/watch?v=UGHvBF7wbJ0)).

### 3.3 Expireless: Expiry Scanner (Mikl Labs)

- **Platforms and price.** Android, iOS, web. Free for one storage location, inventory, alerts, and a shopping list.
  Pro: $4.99 a month or $34.99 a year. Family: $54.99 a year ([site](https://food-assistant-2yi.pages.dev/)).
- **Popularity.** Google Play: 100+ downloads, no rating, updated 25 Sep 2026
  ([Play](https://play.google.com/store/apps/details?id=com.miklabs.foodgem)). Very new. No user reviews found.
- **Add food.** Receipt photo read by AI, which puts each item into fridge, freezer, or pantry. Voice and typed entry
  for many items at once. Barcode.
- **Organisation.** Fridge, freezer, pantry, and a medicine cabinet. Category defaults for 200+ food categories.
- **Expiry.** Each item gets a date from its category. A daily check sends one notification. The alert window can be
  different for each category (for example 2 days for meat, 7 days for produce). **Thaw tracking:** when food moves
  out of the freezer, the app sets a new fridge date. The freezer view is sorted by age.
- **Other.** Shared household list, spending and waste analytics (Pro).
- **Interface (seen).** Home: greeting, an "Expiring soon" line with a count, quick actions, and a list of storage
  areas with counts (Fridge 40, Freezer 49). Inventory: a title ("Freezer. 49 items, 1 expiring"), **tabs Fridge,
  Freezer, Pantry**, a search field, a "Use first" sort control, then **a row of category chips with counts** (All 49,
  Meat 18, Fish 7, Cooked 11), then a "Use first" list with days left on the right ("9d", "74d"). A floating add
  button. Swipe an item to log it as used or discarded (site).
- **Users say.** No reviews found. Its interface is the closest match to the "tabs and category chips" choice.

### 3.4 FridgeWise: Pantry Inventory (Tastebot, LLC)

- **Platforms and price.** Android and iOS. Free, with limits on active items and on monthly smart imports; Premium
  for unlimited use ([Play](https://play.google.com/store/apps/details?id=com.getfridgewise.app)).
- **Popularity.** Google Play: 4.5 stars, 95 reviews, 5K+ downloads, updated 8 Nov 2026.
- **Add food.** Receipt scan, grocery photo, imported shopping list, barcode, or typed. The app makes editable items.
  The receipt screenshot shows a suggested shelf life for each item ("Milk 7 days").
- **Organisation.** One list, filtered by fridge, freezer, pantry, or saved spaces. Search and sort.
- **Expiry.** "Freshness estimates" and use-by reminders.
- **Other.** One free, unlimited shared grocery list; household sharing; recipes from food that needs to be used.
- **Interface (seen).** A segmented control "Have / Need" at the top. Four tiles: In stock, Use today, Use soon,
  Clean out. Then **an "All storages" dropdown chip and a sort button**, then **a row of category chips** (All
  categories, Bakery, Beverages, Dairy & eggs). Rows show the name, the storage area, and a coloured pill ("Use
  Today", "In 2 days"). An "Add items" button floats at the bottom.
- **Users praise.** Receipt and barcode entry saves time; reminders; shared list. (The reviews are recent and generic.
  Treat them with care.)
- **Users complain.** None shown on the page.

### 3.5 Your Food: No Waste Inventory (Harderue)

- **Platforms and price.** Android, iOS, iPad, Mac. Free with no ads (three lists, dates, reminders, shopping list).
  The App Store lists Premium at $7.99 one time and "Supplies Manager, Lifetime" at $44.99
  ([App Store](https://apps.apple.com/app/id6473174562)). Two Google Play reviews from August 2026 say the one-time
  price went up to about £43, or £15 a year (second pass; correction).
- **Popularity.** Google Play: 4.6 stars, 820 reviews, 50K+ downloads, updated 13 Oct 2026
  ([Play](https://play.google.com/store/apps/details?id=com.HarderuesCompany.YourFood)). App Store: 4.6 stars, 25
  ratings.
- **Add food.** Typed, with product history and prefilled details. Barcode scanner. Each field is optional. 1,000+
  icons.
- **Organisation.** One inventory for each place (home, holiday flat). Inside it, **lists and sublists** (Fridge, then
  Produce drawer, Dairy; Freezer; Pharmacy). Sort by name or by a custom order.
- **Expiry.** A date and a reminder time for each item. The app shows what to use first.
- **Other.** Real-time sharing (Premium), shopping list from low items, spending charts (Premium).
- **Interface (seen).** **A grouped list:** each list is a coloured header with counts and a + button, with its items
  below it. Rows are red, yellow, or green by days left ("Tomorrow", "-1 Days", "5 Days").
- **Users praise.** Cute icons that make a long list easy to scan; the "use first" view helps to plan meals; a one-time
  price instead of a subscription; easy to share with a spouse.
- **Users complain.** Entry takes work; the app forced its own keyboard, so voice entry did not work; no "frozen on"
  date for home-cooked food, only an expiry date; picking the perfect icon is distracting.

### 3.6 FridgeBuddy: Pantry Inventory (Charles-Adrien Fournier, iOS)

- **Platforms and price.** iPhone and iPad (iOS 26 or later). Free, with Pro: weekly, monthly, yearly (£17.99 to
  £34.99), or £69.99 one time ([App Store UK](https://apps.apple.com/gb/app/id1500190823)).
- **Popularity.** App Store UK: 4.3 stars, 22 ratings. The screenshot claims 4.6 in another store. Updated in Nov 2026.
  An Android app with the same name (com.dcfdev.fridgebuddy) is a different developer.
- **Add food.** Barcode with Open Food Facts; receipt photo or PDF, checked before save; fruit and vegetables from a
  list with a USDA FoodKeeper date; a photo of a shelf for many items (Apple Intelligence); Pro: a scan of the printed
  date.
- **Organisation.** Fridge, freezer, and pantry locations (a limited number in the free version). Search and filter.
- **Expiry.** Reminders for each storage location: days ahead and time of day. Lists of "expires soon", "expired", and
  "open". **Opened food:** marking food as opened can move its date forward.
- **Other.** iCloud sync, household invitations (Pro), Siri (what is expiring, add, mark as used or thrown away),
  widgets, insights on eaten versus thrown away, CSV export.
- **Interface (seen).** A screen for one storage area ("Fridge", with a back button), a search field, and rows with a
  product photo, the name, a coloured pill ("In 1 day", "In 3 days"), and a quantity badge (x8). The storage area is a
  level of navigation, not a filter.
- **Users praise.** It finds food at the back of the fridge; good barcode data for UK food.
- **Users complain.** The free item limit is too low; the days left were rounded to months ("a month" for 7.5 weeks).
  A reviewer of the US listing says the dates must be correct for the app to be useful
  ([search summary of the US listing](https://apps.apple.com/app/id1500190823)).
- **Second pass.** 28 US App Store reviews. Two users ask for categories to sort or filter by (dairy, condiments,
  canned food, sauces), so the app had no categories when they wrote (2024, 2025). One user says the sort goes back to
  alphabetical each time the app opens, and asks for expiry as the default (2022). Four users cannot share the
  inventory with a second person.

### 3.7 Pantry Check: Grocery List (Sunroom Labs, iOS)

- **Platforms and price.** iOS. Free up to 200 items; paid storage tiers for 2,000 or 10,000 items
  ([App Store](https://apps.apple.com/us/app/pantry-check-grocery-list/id966702368)).
- **Popularity.** App Store: 4.5 stars, 1.6K ratings. Updated in Oct 2025 (version 2.9.2).
- **Add food.** Barcode with a crowd-sourced database and product photos. Expiry dates filled from usage data (a
  review).
- **Organisation.** Custom locations; automatic categories; alphabetical sort; an "unassigned" location filter.
- **Expiry.** Automatic reminders, an expiring list, and a usage timeline.
- **Other.** Family sharing in real time, smart shopping lists with prices, CSV export, long press for
  finished or spoiled.
- **Interface (seen).** **A grouped grid:** section headers by category (Canned Fruits & Vegetables 6, Cooking Oil 7,
  Dips & Spreads 5), product photos, age or days left under each photo, and a bar for the amount left. **A tab bar with
  Inventory, Shopping, Expiring, Timeline**: the expiring food has its own tab.
- **Users praise.** Many locations and easy moves between them; the scanner; automatic dates; expiring lists and sort;
  real-time family updates.
- **Users complain.** No undo for edits; the "% used" slider is too near the "finished" button; the automatic category
  cannot be checked before the item is added; the scan sometimes gives a wrong date.
- **Second pass.** 50 recent US App Store reviews (July 2025 to October 2026), mostly positive. The main complaint is
  about categories: "way too many categories", which makes the list "visually difficult", and users want to make
  their own (4 reviews). One user says that all location groups collapse each time the list refreshes, and asks for an
  "expand all" button. So the grouped list can collapse, and it does not keep its state.

### 3.8 What The Fridge?! (Michael Jandreau, iOS)

- **Platforms and price.** iPhone. 14-day trial, then $9.99 a year or $14.99 one time. An AI add-on (receipt scan)
  costs more ([App Store](https://apps.apple.com/us/app/id6759576051)).
- **Popularity.** App Store: 5.0 stars, 1 rating. Version 1.1.6, June 2026. Very new.
- **Add food.** Typed, barcode, voice (parsed on the phone, then checked), bulk entry, receipt (AI add-on). The app
  learns the usual location and category of a food.
- **Organisation.** Custom locations; categories; tags for a person.
- **Expiry.** Filter by status (expired, expiring today, tomorrow, soon); reminders for today, tomorrow, in three days,
  or expired.
- **Other.** Sharing by link, QR code, or code; optional sign-in for sync; insights (used versus wasted, waste by
  category); widget; Siri and Shortcuts.
- **Interface (seen).** Home: greeting, **three coloured tiles (Total items 170, Expiring soon 7, Expired 2)**, then
  "Expired" and "Expiring soon" groups with "View all". This is very close to CVKE Home. Inventory: a search field with
  a scan button, **a filter button** (opens filters), and **a row of location chips with counts** (All Locations 170,
  Basement 15, Bedroom 1). Rows have − and + buttons for the quantity.
- **Users say.** No written reviews yet.

### 3.9 Wonder Fridge: Food Organizer (Wonderple)

- **Platforms and price.** Android (and iOS). Free with ads; Premium.
- **Popularity.** Google Play: 3.6 stars, 441 reviews, 50K+ downloads, updated 10 Nov 2026
  ([Play](https://play.google.com/store/apps/details?id=com.meolly.fridge)).
- **Add food.** 400+ default foods to pick, barcode, AI photo and receipt scan.
- **Organisation.** Fridge, freezer, pantry. No login needed for one person; sign-in for a family fridge.
- **Expiry.** Alerts when dates come near; a list in use-by order.
- **Interface (seen).** **Tabs for Fridge, freezer, and pantry** (the last two as icons). A grid of food icons with a
  "D-day" or "D-3" badge on each tile.
- **Users praise.** Easy, use-by order, a barcode scanner that works ("I have tried a few of these apps", one paying
  user wrote).
- **Users complain.** Ads each time an item is saved; icons do not exist for local food; a request for sign-in and
  backup.

### 3.10 Expiry date tracker (shoyuland)

- **Platforms and price.** Android. Free with ads and in-app purchases.
- **Popularity.** Google Play: 4.6 stars, 317 reviews, 10K+ downloads, last updated 7 Dec 2023
  ([Play](https://play.google.com/store/apps/details?id=com.shoyuland.freshthings)).
- **Add food.** Typed: date, quantity, category, notes, a sticker or a photo.
- **Organisation.** Custom categories; one filter at a time.
- **Expiry.** A reminder 7 days before expiry.
- **Users praise.** The important details are visible at a glance; simple for a person who lives alone.
- **Users complain.** No search bar; no copy of an item with a different date; days only, where weeks and months are
  easier for long dates; no presets; one filter at a time; no filter to hide expired or empty items. Deleting one
  chocolate bar is a chore.

### 3.11 Grocy (open source, self-hosted)

- **Platforms and price.** Web app that a person hosts; community apps for Android and iOS. Free
  ([grocy.info](https://grocy.info/)).
- **Add food.** Each product must first exist in a master list. Then a purchase records amount, price, and date.
  Barcode with Open Food Facts.
- **Organisation (seen in the [demo](https://demo.grocy.info/stockoverview)).** The stock overview has **a search
  field and three dropdowns: Location, Product group, Status**. Above them, **coloured status badges** ("0 products are
  expired", "2 products are due within the next 5 days", "4 products are below min. stock"). The badges are filters.
- **Expiry.** Due dates; the oldest stock is used first; recipes that use food that is due soon.
- **Users say.** A tech writer gave up after about a week, because the setup of each product and unit was too much
  work ([Galaxus](https://www.galaxus.ch/en/page/how-i-want-to-digitise-the-contents-of-my-fridge-and-fail-to-do-so-39565)).
  A privacy forum recommends it for full control of the data
  ([Privacy Guides](https://discuss.privacyguides.net/t/looking-for-a-app-to-track-fridge-freezer-contents-and-expiry-dates/22977)).

### 3.12 Samsung Food and the Family Hub food list (adjacent: smart fridge)

- **Platforms and price.** Android, iOS, web, and Samsung fridges. Free; Samsung Food+ is paid.
- **Popularity.** Google Play: 4.4 stars, 23.2K reviews, 1M+ downloads, Editors' Choice, updated 29 Jul 2026
  ([Play](https://play.google.com/store/apps/details?id=com.foodient.whisk)).
- **Food list.** On a Family Hub fridge, the camera recognises some food and the person adds the rest. The person sets
  an expiry date for each item. The phone app shows the same list. When food leaves the fridge, the person must also
  remove it from the list ([Samsung support](https://www.samsung.com/us/support/answer/ANS10006842/)). "Automated
  pantry suggestions and food tracking" is part of the paid Food+.
- **Lesson.** Even with a camera in the fridge, the person still enters and removes most food by hand. A 2025 report
  says the camera recognises 37 foods ([Pickr](https://www.pickr.com.au/news/2024/samsung-adds-ai-food-management-to-family-hub-french-door-fridges)).
  This supports ADR 0002 (no fridge device).
- **Not verified.** We did not see the pantry screens of the phone app.

### 3.13 Well Stockd

- **Platforms and price.** Web app only (can be installed on the home screen). Free for up to 30 foods; Pro $7.99 a
  month ([site](https://wellstockd.com/), [PeerPush](https://peerpush.com/p/well-stockd)). It launched on directory
  sites in October 2026 ([BetterLaunch](https://www.betterlaunch.co/product/well-stockd)), so it is very new.
- **Features.** Fridge, freezer, and pantry; an estimated use-by date from typical shelf life, with no guessed date for
  canned and frozen food; batch barcode scan with one review; receipt photo; voice entry with a review step; used,
  tossed, or a mistake as the end of an item; undo on every change; email and phone reminders at a chosen hour;
  5,700+ recipes; meal plans ([features](https://wellstockd.com/features), [pantry inventory](https://wellstockd.com/pantry-inventory)).
- **Interface (seen in its own product picture, desktop width).** A "Kitchen" title with the count, a search field,
  **a row of category chips** (All, Produce, Protein, Dairy, Grain, Condiment, Other), **a sort dropdown** ("Use
  soon"), **links that jump to each storage area with counts** (Fridge 11, Pantry 10), and **collapsible groups by
  storage area** ("Fridge 11"). Each card has − and + for the quantity. This confirms the "grouped list" of the first
  look ([product picture](https://www.wellstockd.com/_next/image?url=%2Fproduct%2Fkitchen-desktop.png&w=1920&q=75&dpl=dpl_He17XfFobbu3qyp2nLsYEF1jqE4U)).
- **Not verified.** The phone layout, and user reviews. We did not sign up.

### 3.14 Fridgely (Justin Ehlert, iOS)

- **Status.** The App Store page gives "Not Found" on 12 Nov 2026 (US and UK). Last known update March 2021. Rating
  4.2 from about 150 ratings ([AlternativeTo](https://alternativeto.net/software/fridgely/about)).
- **Features (from directories).** Receipt scan (offline), barcode with estimated dates, alerts, recipes, sync, sharing,
  fridge, pantry, and freezer spaces, shopping list, CSV export (paid).
- **Users said.** A reviewer asked for dates from the category of a food.
- **Second pass ([archived App Store page, 9 Oct 2023](https://web.archive.org/web/20231009025759/https://apps.apple.com/us/app/fridgely/id988016972)).**
  4.2 stars from 139 ratings; Premium $2.99 one time. The iTunes lookup gives no result now, so the app is removed.
  **Interface (archived store image):** a Spaces tab, then a screen for each space ("Fridge") with the food **grouped
  by freshness: Expired, Expiring Soon, All Items**. Reviews: sync failed for a third person in a household; the
  estimated dates were good enough; the app needs regular upkeep and is "not for quick fix" people; manual updates are
  tedious.

### 3.15 CozZo: Fridge, Pantry Inventory (Cogzum Bulgaria)

- **Status.** The App Store page gives "Not Found" on 12 Nov 2026. A Google Play search does not find it. Directory
  pages list version 4.9.3 in September 2025.
- **Features (from directories).** Fridge and pantry inventory, receipt and barcode scan, expiry reminders, shopping
  lists for each store, recipes, household sync on up to 10 devices, Apple Watch.
- **Users said** ([JustUseApp, 31 reviews](https://justuseapp.com/en/app/1162606257/cozzo-food-inventory-manager/reviews)):
  praise for easy add and remove and for household sync. Complaints: crashes, **lost data after a subscription or
  update change**, a cap on receipt scans, hard to learn, search is hard in a large inventory.
- **Second pass ([archived App Store page, 8 Feb 2025](https://web.archive.org/web/20250208120319/https://apps.apple.com/us/app/cozzo-fridge-pantry-inventory/id1162606257)).**
  4.1 stars from 154 ratings. The App Store review feed and the iTunes lookup give no result now. **Interface
  (archived store image):** an "At Home" tab with a switch "Spaces | Items". Spaces is a list of storage areas with
  counts (On Order 16, Fridge 27, Freezer 6, Pantry 36, Storage Room 7, Medicine Cabinet 9) and small freshness icons
  with counts on each row; a tap opens the area. A user with 100+ items in one space could not find food, and asked
  for search and a filter inside a space (2020; the developer then added it). Swipe left or right marks food as used
  up or wasted.

### 3.16 Kitche (UK)

- **Platforms and price.** Android and iOS. Free.
- **Features (from articles).** Receipt scan for the main UK supermarkets, barcode, voice, typed; alerts before
  expiry; **swipe to "toss" a product**, with the cost of waste each week; recipes from food at home; an Impact view
  of money, water, and CO2 ([Springwise](https://www.springwise.com/innovation/food-drink/an-app-helps-families-avoid-food-waste/),
  [Buckinghamshire Council](https://buckinghamshire.gov.uk/cost-of-living/help-with-buying-or-accessing-food/toolkit-reducing-food-waste-at-home/useful-apps)).
- **Second pass.** A Google Play UK search for "Kitche food waste" and a UK App Store search for "kitche" did not find
  it on 12 November 2026. It is probably withdrawn. A 2020 review with screenshots says that a receipt scan gives a
  list to check before the food goes into the inventory, that the app groups food by type (dairy, vegetables), and
  that the person must remember to mark food as gone ([TapSmart](https://www.tapsmart.com/apps/food-drinks/review-kitche/)).
- **Not verified.** The current status and the list screen.

### 3.17 Too Good To Go (adjacent: food waste)

- **What it is.** A marketplace for unsold food from shops and restaurants. It does not track food at home.
- **Popularity.** Google Play: 4.9 stars, 2.03M reviews, 50M+ downloads, Editors' Choice, updated 2 Nov 2026
  ([Play](https://play.google.com/store/apps/details?id=com.app.tgtg)).
- **Lesson.** People who care about food waste are a very large group. A tracker can use the same message (money and
  food saved), but it is not a direct competitor.

### 3.18 Smantry, formerly "Speisekammer App" (Germany; new in the second pass)

- **Platforms and price.** Android, iOS, and a web app. Free for 30 items; reviews give €29.99 a year and €149.99 for a
  single lifetime licence.
- **Popularity.** Google Play: 4.4 stars, 2.31K reviews, 50K+ downloads, updated 12 Oct 2026
  ([Play](https://play.google.com/store/apps/details?id=app.speisekammer)). The second-largest number of reviews of a
  dedicated tracker in this report, after KitchenPal.
- **Add food.** Barcode with a database shared by users; manual entry for food with no barcode. A scan also takes food
  out of stock.
- **Organisation.** Any number of storage locations. Categories. Minimum stock levels.
- **Expiry.** A best-before date on each item; notifications; a stocktake that asks which batch leaves stock and why;
  a cleanup flow with "used up" versus "thrown away" (release notes, 2026).
- **Interface (store images).** Home has a donut chart of stock state (expired, expiring soon, fresh, no date) and the
  value of food at risk. The list: an "All locations" title, then **one toolbar with three buttons: Search, Sort
  (Date), Filter (0)**. The number shows the active filters. "Showing 14 items (14 total)". The list is **grouped by
  category with section headers** (Beverages, Dairy Products and Eggs, Other Foods). Filter opens **a bottom sheet with
  check boxes for state**: in stock, below minimum stock, expired, expiring soon, expiring soon or expired.
- **Users (20 German reviews).** Praise: the scan is fast and finds products (5), storage locations (2), household
  sharing (2), fast support and a public feedback board (4). Complaints: price and the 30-item limit (5), bugs such as
  crashes and "upgrade required" for a paying user (6), date entry with a scroll wheel instead of a number field,
  "3 times" slower (1), the form closes after each new item (1).

### 3.19 InvenDo: Home Inventory & Food (Chester Software; new)

- **Popularity and price.** Google Play: 4.7 stars, 1.74K reviews, 50K+ downloads; subscription, 7-day trial
  ([Play](https://play.google.com/store/apps/details?id=com.chestersw.homelist)).
- **Features.** Barcode; storage places with sub-places; categories with sub-categories made by the person; "Expires
  soon" and "Already expired" flags; a reminder at a chosen time of day; **mark as opened, which sets a "consume by"
  date from a shelf life that the app remembers for the next time**; minimum quantity; shopping list by store; receipt
  scan (premium beta).
- **Interface (store images).** A switch "Inventory | Shopping List". Categories are **coloured folders with a count
  and small green, orange, and red freshness badges**. A tap opens the folder.
- **Users (20 reviews).** The top review (80 people found it helpful) praises categories and sub-categories, and
  locations and sub-locations that the person makes. Others praise no ads and use for a large freezer. Complaints: the
  price and the subscription (3), "not intuitive" and lists versus categories are confusing (3), a broken widget (1).

### 3.20 MyKURA (Indoor Corgi, Japan; new)

- **Popularity.** Google Play (Japan): 4.2 stars, 1.02K reviews, 100K+ downloads; ads and in-app purchases
  ([Play](https://play.google.com/store/apps/details?id=jp.gr.java_conf.indoorcorgi.mykura)).
- **Features.** Camera photo instead of a typed name; voice input; days left on each card; alarms; "To Buy" mark.
- **Interface (store image).** **Scrollable tabs that the person names: FRIDGE, FREEZER, SHELF, SEASONINGS, and more
  off-screen.** A tab can be a place or a category. Cards in a two-column grid with a colour bar or photo and the days
  left.
- **Users (3 reviews on the page).** Voice entry is better than a weak barcode database; moving items between tabs
  helps when food goes from the freezer to the fridge. Requests: a list view instead of tabs, search, and a sort
  dropdown instead of a button that cycles through 4 orders.

### 3.21 Best Before - Food Tracker (PeytuApp; new)

- **Popularity.** Google Play: 4.1 stars, 955 reviews, 50K+ downloads; ads and in-app purchases
  ([Play](https://play.google.com/store/apps/details?id=com.peytu.bestbefore)).
- **Features.** Category and location; opened food with its own reminder; shared lists.
- **Users.** A long review asks that one entry takes no more than 3 taps and 3 seconds, that a category can be made
  from the entry form, and that the "purchase date" is not filled with today by default.

### 3.22 My Pantry: Grocery shared list and pantry (Yust Apps; new)

- **Popularity.** Google Play: 4.2 stars, 1.1K reviews, 50K+ downloads; ads
  ([Play](https://play.google.com/store/apps/details?id=com.yustapps.pantry)).
- **Features.** Lists for pantry, freezer, fridge, and shelves; colour by expiry date; voice input; cloud sync.
- **Users.** The top review (11 helpful): search works only inside one list, so the person must open each list to find
  an item. Ads with sound woke a sleeping partner.

### 3.23 Other apps with traction outside the US (not studied in depth)

- **Limiter (Japan):** 4.2 stars, 843 reviews, 10K+ downloads
  ([Play](https://play.google.com/store/apps/details?id=jp.labboy.limiterflutter)).
- **유통기한 언제지 (Korea):** 3.5 stars, 220 reviews, 10K+ downloads
  ([Play](https://play.google.com/store/apps/details?id=kr.co.ourneeds.app)).
- **Frigo Magic (France, adjacent):** recipes from what is in the fridge, 4.1 stars, 8.3K reviews, 1M+ downloads
  ([Play](https://play.google.com/store/apps/details?id=fr.haruni.frigomagic)).
- **Phenix (France, adjacent):** a marketplace for unsold food, like Too Good To Go, 4.6 stars, 63.6K reviews, 1M+
  downloads ([Play](https://play.google.com/store/apps/details?id=com.phenix.cajou)).

Note: the Play rating of one app is different in each country. KitchenPal shows 4.6 in the US and 3.9 in Germany.

## 3A. User evidence in numbers (second pass)

The counts are the number of reviews or comments that we read with each theme. A review can have more than one
theme. "Read" is the total that we read for the app in the second pass.

| App | Source and period | Read | Main praise (count) | Main complaints (count) |
|---|---|---|---|---|
| NoWaste | Google Play, most relevant, 2021–2026 | 44 | Clean and easy (5); sort by expiry (1); scan saves time (2) | Barcode scan fails or weak database (10); sign-up fails or account required (8); confusing, hard to find add or delete (7); date defaults to "today" or is wrong (6); forced full screen hides the system bar (6); paywall or 500-item limit (4); lost list (2) |
| NoWaste | App Store US feed, 2020–2026 | 50 | Inventory on all devices and at the store; family with many freezers (8) | **Lost data (17)**; locked out, password reset fails, no reply from support (9); wrong dates or scan fails (8); paid "lifetime" turned into a subscription (5); adding is clunky, "trying to be too many things" (4) |
| KitchenPal | Google Play, most relevant, 2018–2022 | 20 | Shared kitchen, barcode, recipes, fewer double purchases (7) | Barcode data wrong or missing (6); rigid items, fixed servings (4); recipe quality (4); sign-in or server errors (3); wrong storage area or category set by the app (2) |
| KitchenPal | App Store US feed, 2024–2026 | 50 | Less waste and fewer double purchases, recipes, many fridges and freezers, support, use by carers (25) | Paywall surprises, such as paid barcode scan (8); crashes, needs internet, lost entries (7); categories too coarse or not editable (4); hard for food with no barcode (4); **no view of all storage areas (1)**; after a scan, must search the whole kitchen to find the item (1) |
| Your Food | Google Play, most relevant, 2022–2026 | 20 | Icons make a long list easy to scan (6); simplest of several apps (4); one-time price (3); support (3); sharing (3) | Entry takes work (3); barcode weak or missing (3); price went up (2); crashes (2); own keyboard blocks voice typing (1) |
| Your Food | App Store US feed, 2024–2026 | 15 | Cute and organised lists and sub-lists, sort options, free tier (13) | "Too many buttons" to log food (1); sync between iPhone and iPad fails (1) |
| Wonder Fridge | Google Play, most relevant, 2022–2026 | 20 | Easy, use-by order, accurate reminders, icons (12) | Ads, some that force a close (3); no sharing or backup, now added (2); one item at a time is slow (1); empty items are not faded in list view (1) |
| Pantry Check | App Store US feed, 2025–2026 | 50 | Fewer double purchases, see what is at the back (12); easy and clean (12); long-term use for years (3); sharing (3) | **Too many automatic categories, want own categories (4)**; groups collapse after each refresh (1); items missing after days of entry (1); logged out (1); no Android (1) |
| FridgeBuddy | App Store US feed, 2020–2026 | 28 | Easy, less waste, home-canned food with own barcodes, support (14) | No sharing between two people (4); scan slow or false detections (3); **no categories (2)**; sort resets to alphabetical (1); price (2) |
| Smantry | Google Play Germany, 2021–2026 | 20 | Fast scan (5); support (4); locations and sharing (4) | Bugs (6); price and 30-item limit (5); date wheel instead of number field (1); form closes after each item (1) |
| InvenDo | Google Play, most relevant, 2025–2026 | 20 | Own categories and sub-categories, locations, no ads, freezers (16) | Price, subscription (3); not intuitive (3); widget (1) |
| Grocy | Hacker News comments, 2020–2026 | 40 (12 on topic) | Helps with frozen and long-life food; good product database (4) | Too much work to set up and keep current (6); cluttered interface (1); a partner will use a list, not an inventory (1) |
| CozZo | Archived App Store page, 2020 | 2 | Changes how one looks at the pantry | Hard to find food with 100+ items in a space; needs search and filter inside a space |
| Fridgely | Archived App Store page, 2019–2020 | 2 | Estimated dates are good enough | Sync with a third person fails; manual updates are tedious |

**What the numbers say.**

- The two largest themes in all apps are **effort of entry and upkeep**, and **trust**: lost data, lock-out, wrong
  dates, and surprise paywalls. (Evidence.)
- Complaints about the list screen are few. The ones that exist are about **too many or too coarse categories**
  (Pantry Check, KitchenPal), **no view of all food** (KitchenPal), **search only inside one list** (My Pantry,
  CozZo), and **state that resets** (Pantry Check groups, FridgeBuddy sort). (Evidence.)
- We found **no review that complains about a row of chips or tabs that scrolls sideways**. This does not prove that
  such rows work well: users rarely name a layout problem. (Evidence of absence; the reading is our judgement.)

## 4. Patterns of good apps

1. **Short entry with a suggested date.** The apps that users praise fill the date for the person: KitchenPal for
   produce, FridgeBuddy from the USDA FoodKeeper list, Expireless from categories, Pantry Check from usage data.
   Users complain most when the date is empty, wrong, or "today" (NoWaste, Pantry Check, FridgeBuddy).
2. **More than one way to add.** Nearly all apps have barcode and typed entry. Most recent apps add receipt scan and
   voice. Receipt scan is often paid or limited (FridgeWise, Expireless, What The Fridge?!, CozZo).
3. **Use-first order as the default.** Expireless ("Use first"), Wonder Fridge, Your Food, and FridgeWise put the
   soonest date first. Users name sort by expiry as a top reason to keep an app.
4. **Days left as a coloured label.** Red, amber, green or grey pills with short text ("In 2 days", "Use Today", "9d",
   "D-3"). Users want days, not months (FridgeBuddy review), but one user wants weeks for long dates (shoyuland).
5. **Counts at the top.** FridgeWise, What The Fridge?!, Expireless, and Grocy show the number of expiring and expired
   items above the list. In Grocy, the counts are also filters.
6. **Quantity in the row.** KitchenPal and What The Fridge?! put − and + on each item, so a person can use one piece
   without opening the item.
7. **A fast end of an item.** Swipe in Expireless and Kitche, long press in Pantry Check, Siri in FridgeBuddy.
8. **Waste and money statistics.** NoWaste, KitchenPal, What The Fridge?!, FridgeBuddy, Kitche, and Expireless show
   eaten versus thrown away, or money saved.
9. **Sharing with a household.** Nearly every app with more than 10K downloads has it, mostly as a paid function.

## 5. Common failures

| Failure | Evidence |
|---|---|
| Slow entry: too many steps after a scan | NoWaste review (edit, quantity, amount, type, back); Grocy write-up; KitchenPal "tedious" for uncommon items |
| Wrong or missing data after a scan | NoWaste (most products not found), Pantry Check (wrong date), Your Food (scanned items lack details), Wonder Fridge (no icons for local food) |
| Data loss | NoWaste (350+ items gone for a paying user), CozZo (lost data after an update), NoWaste crash lost 20 items |
| Limits on core functions | FridgeBuddy (free item limit "too restrictive"), Pantry Check (200 items free), FridgeWise (active item limit), NoWaste (6 lists, 500 items) |
| Ads in the core flow | Wonder Fridge (an ad each time an item is saved) |
| No undo, controls too close together | Pantry Check |
| Wrong automatic choices with no check | Pantry Check (category), NoWaste (storage area from a receipt), KitchenPal (shopping list) |
| Accessibility | Your Food (own keyboard blocked voice entry); Pantry Check had no declared accessibility features |
| Too many functions, hard to learn | CozZo; KitchenPal (recipes, diets, meal plans, nutrition in one app) |
| Notification fatigue | We found no review that complains about too many reminders. The good apps send one daily check (Expireless) or let the person set days and time for each storage area (FridgeBuddy). This is a design choice, not a problem that we saw. |

## 6. The list and filter screen

The owner is choosing between five patterns for My Fridge. This section lists what we saw. The column "Seen as" says
if we saw the running app or only a store or product image (second pass). Many storage areas or categories: what
the image shows when the values do not fit on the screen.

| App | Seen as | Storage area | Category | Search | Sort | Status | Many values |
|---|---|---|---|---|---|---|---|
| Expireless | Store image only | Tabs (Fridge, Freezer, Pantry) | Chip row with counts (All 49, Meat 18, ...) | Field | "Use first" control | Count in the title ("1 expiring") | Not shown: 4 chips fit |
| KitchenPal | Store image only (list); running app seen for the add screen | Tabs (Fridge, Freezer, Cellar), no "All" | Not on the list screen | Icon in the top bar | "Sort by Expiry" with arrow; grid or list | Days on each tile | Add screen: storage choices wrap to 2 lines |
| Wonder Fridge | Store image only | Tabs (text and icons) | Not seen | Icon | Use-by order | D-day badge | 3 tabs fit |
| MyKURA | Store image only | Scrollable tabs that the person names (place or category) | The same tabs | Not seen (users ask for it) | Button that cycles 4 orders | Days on each card | **Tabs scroll; the 5th tab is off-screen** |
| FridgeWise | Store image only | Dropdown chip ("All storages") | Chip row | Icon | Button | Four tiles above (Use today, Use soon, Clean out) | **Category chips scroll; the 4th chip is cut** |
| What The Fridge?! | Store image only | Chip row with counts (All Locations 170, ...) | In the filter sheet | Field with scan button | Not seen | Filter by status in the sheet; tiles on Home | **Location chips scroll; the 4th chip is cut** |
| Smantry | Store image only | Title "All locations" (switch) | Section headers; filter sheet | Button | Button ("Date") | Filter sheet: expired, expiring soon, below minimum | Sheet with check boxes; "Filter (0)" shows the count |
| Well Stockd | Product image (desktop) | Collapsible groups with jump links and counts | Chip row (7 categories) | Field | Dropdown ("Use soon") | Use-soon order | All 7 chips fit on a wide screen; phone not seen |
| NoWaste | Store image only | Dropdown that changes the list ("Home › Freezer +4") | Custom categories (screen not seen) | Icon | "Sort" link | Tags on the card | Dropdown with a "+4" count |
| FridgeBuddy | Store image only | Separate screen for each storage area | None (users ask for it) | Field | Not seen | Lists for "expires soon", "expired", "open" | Not shown |
| CozZo | Archived store image | List of spaces with counts, then a screen for each | Not seen | Icon | Not seen | Freshness icons with counts on each space | A vertical list: no limit |
| Fridgely | Archived store image | List of spaces, then a screen for each | Not seen | Not seen | Not seen | Groups: Expired, Expiring Soon, All Items | A vertical list: no limit |
| InvenDo | Store image only | Places and sub-places | Folders with counts and freshness badges | Icon | Not seen | Badges on each folder | Folders: no limit |
| Pantry Check | Store image only | Locations (screen not seen) | Grouped grid with section headers | Icon | Alphabetical | Separate "Expiring" tab | Groups collapse; users say there are too many |
| Your Food | Store image only | Grouped list (lists and sub-lists) | The sub-lists | Not seen | Name or custom | Row colour | A vertical list: no limit |
| Grocy | **Running app seen** (public demo) | Dropdown | Dropdown ("Product group") | Field | Column headers | Dropdown, and badges that filter | Dropdowns: no limit |
| CVKE Fridge now | Running app | Chip row | Chip row | Field | Menu in the top bar | Card colour; Home totals | Both chip rows scroll |

**Findings.**

1. **The storage area is the first level in 13 of 16 apps.** It is a tab, a separate screen, a dropdown, a group, or
   the first chip row. The category is the second level, or it is absent from the list screen. (Evidence; second pass
   count.)
2. **Tabs for the storage area are common in apps with many downloads.** KitchenPal (100K+), MyKURA (100K+), and Wonder
   Fridge (50K+) use tabs. Expireless uses tabs with a category chip row below. This is the "tabs and one category
   control" choice of the owner. But KitchenPal has no "All" tab, and a user complains about it. (Evidence.)
3. **One dropdown plus one chip row also works.** FridgeWise puts the storage area in a dropdown chip and the
   categories in a chip row. It saves height, but it hides the storage areas until the person opens the dropdown.
   (Evidence for the pattern; the comparison is our judgement.)
4. **Nobody shows two full rows of chips.** Two chip rows take vertical space and give the two filters the same weight.
   (Evidence that nobody does it; the reason is our judgement.)
5. **A filter sheet is used when there are many filters.** What The Fridge?! puts category, person, and status in a
   sheet and keeps the location chips visible. Grocy uses three dropdowns on a large screen. A sheet alone hides which
   filters are on. (Evidence for the pattern; the risk is our judgement.)
6. **Grouped lists suit a full kitchen, not a quick check.** Pantry Check and Your Food group by category or by list.
   This is good to browse a large pantry. It is less good for "what do I use first", because the soonest food can be in
   any group. (Our judgement.)
7. **Counts on filters help.** Expireless, What The Fridge?!, and Grocy show counts on the chips or badges. (Evidence.)
8. **Freshness is a filter in good apps.** What The Fridge?! (status filter), Grocy (status dropdown and badges),
   Smantry (state check boxes), FridgeWise (tiles), Pantry Check (Expiring tab), Fridgely (groups by freshness). CVKE
   Home has the totals, but My Fridge has no freshness filter. (Evidence.)
9. **A separate screen for each storage area is common in older apps, and it causes the "All" problem.** CozZo,
   Fridgely, and FridgeBuddy open one area at a time. Users of CozZo, KitchenPal, and My Pantry complain that they
   cannot see or search all food at once. (Evidence, second pass.)
10. **Rows that scroll sideways are common, and the store images show cut chips.** FridgeWise, What The Fridge?!, and
    MyKURA show a cut chip or tab at the right edge, which is the usual sign that a row scrolls. We found no user
    complaint about it (section 3A). (Evidence.)
11. **State that resets annoys users.** Pantry Check groups collapse after a refresh, and FridgeBuddy goes back to an
    alphabetical sort. A filter, a tab, and a sort must stay as the person left them. (Evidence.)

### 6A. The category control: long lists without a sideways row

The owner doubts rows that scroll sideways. This section answers: how do apps show a long list of categories without
such a row, do users comment on it, and which control fits My Fridge?

**What CVKE Fridge has.** The glossary has 8 fixed categories (produce, dairy, meat, condiment, beverage, bakery,
leftovers, other). The person cannot add more. My Fridge shows only the categories that have food, plus "All". So the
row has 2 to 9 chips. On a phone 360 dp wide, about 3 or 4 chips fit, so the row scrolls when there is a varied
inventory. Storage areas are Fridge and Freezer plus the areas that the person creates, so their number has no limit.

**What other apps do, with the evidence.**

| Pattern | Apps | Evidence about it |
|---|---|---|
| One chip row that scrolls | Expireless, FridgeWise, What The Fridge?!, Well Stockd (wide screen), CVKE now | Common. Material Design says a single-line chip group "may necessitate" a horizontal scroll, and its own picture shows the 4th chip cut ([Material Chip docs](https://github.com/material-components/material-components-android/blob/master/docs/components/Chip.md)). No user complaint found. |
| Wrapped chips (more than one line) | KitchenPal add screen (running app, storage choice) | The default of a Material chip group is to wrap (`singleLine` is false by default, same docs). All values are visible. It uses more height. No user comment found. |
| Dropdown or menu chip | FridgeWise (storage), NoWaste (list switch), Grocy (location, product group, status) | One control in little space; the chosen value stays visible in the label. The person must open it to see the values. MyKURA users ask for a sort dropdown instead of a button that cycles. |
| Filter sheet with a count | Smantry ("Filter (0)"), What The Fridge?! | Good for many filters. The count shows that a filter is on. The values are hidden until the sheet opens. |
| Section headers (grouped list) | Pantry Check, Smantry, Your Food, Well Stockd (storage groups) | All food stays visible in one scroll. Pantry Check users say there are "way too many categories" to read, and the groups collapse after a refresh. |
| Folders or a screen for each value | InvenDo, CozZo, Fridgely, FridgeBuddy | No limit on values. InvenDo users praise their own sub-categories; CozZo and KitchenPal users complain that they cannot see all food at once. |
| Tabs that scroll | MyKURA, (KitchenPal and Wonder Fridge with 3 tabs that fit) | Material says scrollable tabs leave "some tabs" off-screen until scrolled ([Material Tabs docs](https://github.com/material-components/material-components-android/blob/master/docs/components/Tabs.md)). Baymard found that people often miss content behind horizontal tabs, and that tabs cut at the edge of a phone screen need a sideways swipe that people do not expect. Baymard accepts tabs on mobile only for about 2 or 3 that fit with no scroll ([Baymard](https://baymard.com/research-articles/avoid-horizontal-tabs)). |
| Top values plus "More" | None seen | No app in this study uses it. |

**What users say.** No review that we read complains about a sideways row. The category complaints are about the
number and the size of the categories (Pantry Check: too many; KitchenPal: too coarse; FridgeBuddy: none). Baymard's
research on tabs is the only direct evidence about hidden sideways items, and it supports the owner's doubt for
primary content. Baymard also found that a horizontal list worked well for colour swatches
([Baymard](https://baymard.com/research-articles/mobile-interactive-color-swatches)), so the evidence is mixed for
small secondary choices.

**Recommendation for My Fridge.**

- **Storage area: tabs.** "All" first, then Fridge, Freezer, and the created areas. Use fixed tabs while they fit (for
  most people: All, Fridge, Freezer, and one more), and scrollable tabs only when there are more. The selected tab is
  always visible, and the storage area is the main filter at the fridge door. (Evidence: storage first in 13 of 16
  apps; KitchenPal "All" complaint. Judgement: fixed until full.)
- **Category: one menu chip.** A filter chip with a dropdown arrow, labelled "Category" or the selected category
  ("Dairy"). It opens a menu with "All" and only the categories that have food in the selected tab, each with its
  count. Put it in one row that does not scroll, with two freshness chips: "Expiring" and "Expired". Three chips fit in
  360 dp. Reasons: the category is the second filter, there are only 8 fixed values, the row never hides a value off
  the screen, and the label always shows the active choice. The cost is one extra tap to change the category.
  (Evidence: Grocy, FridgeWise, NoWaste, Smantry use a dropdown or sheet for a secondary filter; users want freshness
  filters. Judgement: the exact control and row.)
- **Second choice: wrapped chips.** Show "All" and the categories with food as a chip group that wraps to a second or
  third line. All values are visible and one tap away, with no sideways scroll, and it is the Material default. The
  cost is height: up to 3 lines (about 130 dp) above the first card when the inventory has all 8 categories. Choose
  this if the owner wants every category visible at once. (Evidence: Material default; KitchenPal add screen.
  Judgement: the height estimate.)
- **Not recommended as the main control:** a filter sheet (hides the choices and the state; better when there are
  many filters), section headers by category (users of Pantry Check find many groups hard to read; keep it as the
  "category" sort order instead), and a screen for each storage area (causes the "All" problem).

## 7. Feature matrix

Key: ● yes, ◐ partial or paid, ○ no, ? not verified. "Paid" means a paid plan is needed for the function.

| App | Barcode | Receipt | Photo / AI | Voice | Suggested date | Opened date | Storage areas | Categories | Search | Use-first sort | Reminders | Shopping list | Recipes | Household | Waste stats | Widget | No account | Export |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **CVKE Fridge (plan)** | ● (M3) | ○ | ○ | ○ | ● table of foods | ○ | ● | ● | ● | ● | ● (M4) | ○ | ○ | ○ deferred | ◐ history (M5) | ○ | ● | ○ |
| NoWaste | ● | ● | ● | ? | ? | ● tag | ● | ● | ● | ● | ● | ● | ● | ● | ● | ? | ? | ◐ import |
| KitchenPal | ◐ | ● | ? | ● | ◐ produce | ? | ● | ◐ | ● | ● | ● | ● | ● | ● | ● | ? | ? | ◐ |
| Expireless | ● | ◐ | ● | ● | ● category | ● thaw | ● | ● | ● | ● | ● | ● | ? | ◐ | ◐ | ? | ? | ? |
| FridgeWise | ● | ◐ | ● | ? | ● | ? | ● | ● | ● | ? | ● | ● | ● | ● | ? | ? | ? | ? |
| Your Food | ● | ○ | ○ | ○ | ○ | ○ | ● | ● | ◐ | ● | ● | ● | ○ | ◐ | ◐ money | ? | ? | ? |
| FridgeBuddy | ● | ● | ● | ● Siri | ● FoodKeeper | ● | ◐ | ○ asked for | ● | ? | ● | ● | ◐ | ◐ | ● | ● | ● iCloud | ● |
| Pantry Check | ● | ○ | ○ | ? | ● | ? | ● | ● | ● | ● | ● | ● | ○ | ● | ○ | ? | ? | ● |
| What The Fridge?! | ● | ◐ | ○ | ● | ? | ? | ● | ● | ● | ? | ● | ● | ○ | ● | ● | ● | ● | ? |
| Wonder Fridge | ● | ● | ● | ? | ? | ? | ● | ? | ● | ● | ● | ● | ? | ● | ? | ? | ● | ◐ backup |
| Expiry date tracker | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● | ○ | ? | ● | ● | ○ | ○ | ○ | ? | ● | ● |
| Grocy | ● | ○ | ○ | ○ | ● default days | ● | ● | ● | ● | ● | ◐ | ● | ● | ● | ? | ○ | self-host | ● |
| Samsung Food list | ? | ? | ● fridge camera | ● Bixby | ? | ? | ◐ | ? | ? | ? | ? | ● | ● | ● | ? | ? | ○ | ? |
| Well Stockd | ● | ● | ? | ● | ● | ? | ● | ● | ● | ● | ● | ● | ● | ◐ | ◐ used / tossed | ? | ○ | ? |
| Fridgely | ● | ● | ? | ? | ● | ? | ● | ? | ? | ? | ● | ● | ● | ● | ? | ? | ? | ◐ |
| CozZo | ● | ◐ | ? | ? | ? | ? | ● | ● | ● | ? | ● | ● | ● | ● | ● | ? | ? | ? |
| Kitche | ● | ● | ? | ● | ? | ? | ? | ? | ? | ? | ● | ? | ● | ? | ● | ? | ? | ? |
| Smantry | ● | ? | ? | ? | ? | ? | ● | ● | ● | ● | ● | ● | ◐ | ● | ◐ used / thrown | ? | ? account | ● print |
| InvenDo | ● | ◐ | ? | ? | ? | ● | ● | ● | ● | ? | ● | ● | ○ | ● | ? | ◐ | ? | ● Excel |
| MyKURA | ○ (2019 review) | ? | ● photo | ● | ? | ? | ● tabs | ● tabs | ○ | ? | ● | ◐ To Buy | ? | ? | ? | ? | ? | ? |
| Best Before | ? | ? | ? | ? | ? | ● | ● | ● | ? | ? | ● | ● | ? | ● | ? | ? | ? | ? |
| My Pantry (Yust) | ● | ? | ? | ● | ? | ? | ● | ● | ◐ one list | ? | ● | ● | ? | ● | ? | ? | ○ | ? |

The matrix uses the store text and the screenshots. A "?" means that the sources do not say. It does not mean "no".

## 8. Gaps, opportunities, and recommendations

### 8.1 Where CVKE Fridge can be better than the market

- **Trustworthy dates.** Most apps give one date and do not say where it comes from. CVKE marks an estimate as an
  estimate, and the person can replace it with the printed date. Users complain about wrong dates more than about any
  other data problem. This is a real advantage, if the interface shows it clearly.
- **Batches.** Few apps let one food have more than one date. A user of the shoyuland app asks for a copy of an item
  with a different date. CVKE has batches.
- **Used versus thrown away from the start.** Waste statistics are a paid or late feature in most apps. CVKE records
  the end of each batch from milestone 2.
- **No account and no limits.** Many apps limit items or locations in the free version. CVKE has no account and keeps
  the data on the phone. Privacy-minded users look for this (Privacy Guides thread; Wonder Fridge "use it without
  logging in").
- **The risk on the other side:** with no account and no sync, a lost or broken phone loses all data. Users already
  fear data loss (NoWaste, CozZo).

### 8.2 Recommendations: interface (ranked)

Each item says if it is supported by evidence (E) or if it is our judgement (J).

1. **Make the storage area a row of tabs on My Fridge, with "All" first.** Fixed tabs while they fit, scrollable tabs
   only when the person has more storage areas. Keep the order Fridge, Freezer, then the created areas. (E: storage
   first in 13 of 16 apps; KitchenPal user complains that there is no "All"; Baymard on tabs cut at the edge. J: fixed
   until full.) *Changed in the second pass: the first pass said a scrollable row.*
2. **Put the category in one menu chip, not a chip row.** "Category ▾" opens a menu with "All" and the categories that
   have food in the selected tab, with counts. The chip label shows the selected category. Second choice: wrapped
   chips. (Section 6A. E: Grocy, FridgeWise, NoWaste, Smantry; Material docs. J: the control.) *Changed in the second
   pass: the first pass said a chip row with counts.*
3. **Add a freshness filter in the same row: "Expiring" and "Expired" chips.** Let the totals on Home open My Fridge
   with the same filter on. (E: What The Fridge?!, Grocy badges, Smantry state filter, FridgeWise tiles, Pantry Check
   Expiring tab, Fridgely freshness groups. J: the exact place.)
4. **Do not use a filter sheet as the main control.** Use a sheet only later, if the screen gets more than three
   filters. Then show the number of active filters on its button, as Smantry does ("Filter (1)"). (J, with E from
   Smantry and What The Fridge?!.)
5. **Keep the tab, the filters, and the sort as the person left them**, also after a refresh and after the app
   restarts. (E: Pantry Check groups collapse after a refresh; FridgeBuddy sort goes back to alphabetical. J: also
   after a restart.)
6. **Keep "use first" (expiry) as the default sort, and name it so.** "Use first" is a clear name that Expireless
   uses, and it matches the glossary term "use-first list". (E: Expireless, user praise for sort by expiry. J: the
   label.)
7. **On the "All" tab, show the storage area on each card, and consider group headers by storage area only when the
   sort is not by expiry.** (J.)
8. **Show days left in days up to 2 or 3 weeks, then in weeks or months, and show the date on the detail screen.**
   (E: FridgeBuddy and shoyuland reviews ask for both. J: the limits.)
9. **Put the main actions on the card: − for one used, swipe for used or thrown away, with undo in a snackbar.**
   (E: KitchenPal and What The Fridge?! steppers; Expireless and Kitche swipe; Pantry Check users miss undo. J: the
   exact gestures.)
10. **Keep controls with very different results apart.** Do not put "used" next to "thrown away" or "delete" with no
   space. (E: Pantry Check review on the slider near "finished".)
11. **Use the system keyboard and support voice typing in all fields.** (E: Your Food review.)

### 8.3 Recommendations: features (ranked)

1. **One-screen add after a scan.** After the scan: the name from Open Food Facts, the category, the storage area of
   the last add, and the estimated date, already filled in. Buttons "Save" and "Scan next". The person can change the
   date to the printed date on the same screen. Never default to "today". Let the person type the printed date as
   numbers, not only with a date wheel. After "Save", stay on the add flow for the next item. (E: NoWaste review on
   many steps and on the "today" default; praise for suggested dates; Smantry reviews on the date wheel and on the
   form that closes; Best Before review that asks for 3 taps. J: the exact fields.)
2. **A good result when the lookup fails.** Let the person type the name and keep going, with no dead end. The plan
   already says that a failed lookup is not kept. (E: NoWaste, Your Food, and Wonder Fridge complaints about missing
   products.)
3. **An export, and later a backup, before the first release.** A CSV or JSON file of the inventory and the history.
   Also test that an app update never loses data: replay the change log of the old version in the new version.
   (E: 17 of 50 NoWaste App Store reviews report lost data, many after a data-format change; CozZo and Your Food
   reports; Pantry Check, FridgeBuddy, Grocy, InvenDo, Smantry have export or print. J: before release, and the update
   test.) *Second pass: the evidence is much stronger than in the first pass.*
4. **Reminders with one daily summary at a time that the person sets.** One notification a day that lists what
   expires, not one notification for each batch. Days ahead for each storage kind can come later. (E: Expireless daily
   check, FridgeBuddy time of day and days ahead per location. J: the summary design, to avoid notification fatigue.)
5. **Opened and frozen dates.** "Opened" can shorten the estimate, from the FoodKeeper data. Moving a batch from the
   freezer to the fridge gives a new estimate for the fridge. The date added in the freezer is the "frozen on" date.
   (E: FridgeBuddy opened, Expireless thaw tracking, Your Food request. J: the rules; they need vectors in `spec/`.)
6. **Quick add from recent foods.** A list of foods that the person added before, with the last storage area and
   category, to add again with one tap. Milestone 5 already has "add a product again". (E: Your Food product history,
   Wonder Fridge default foods, NoWaste suggestions. J: the priority.)
7. **Used versus thrown-away numbers in the history.** A simple count for each month and the categories that are
   thrown away most. (E: NoWaste, What The Fridge?!, FridgeBuddy, Kitche. J: the size of the feature.)
8. **A home-screen widget for expiring food.** (E: What The Fridge?!, FridgeBuddy. J: after reminders.)
9. **A shopping list from used food.** A small list that gets an item when a batch is used up. (E: nearly every app
   has a list. J: later than the other items; it is outside the agreed scope now.)
10. **Do not add receipt scan, AI photo recognition, recipes, or meal plans now.** They are expensive, often paid, and
    users report errors (wrong storage area from a receipt, unreliable recipe matching). A fast barcode and typed entry
    gives most of the value. (E: the complaints above. J: the decision.)
11. **Household sharing stays deferred, but it is the most common paid feature.** Keep the change log design that
    makes it possible later. (E: most apps with 10K+ downloads have it. J: the timing.)

## 9. What we could not verify

- The running list screen of all apps except Grocy. For the others we saw store images or, for Well Stockd, a product
  picture at desktop width. Store images are marketing images.
- How the tabs and chips of each app behave with many values, beyond what one store image shows (section 6, last
  column).
- The list screens of Kitche and of the Samsung Food pantry. We found no current store page for Kitche, and no phone
  screen of the Samsung Food list.
- The current CozZo and Fridgely apps. The iTunes lookup gives no result for either, so they are probably removed.
- The web apps of NoWaste and Expireless. Both need a sign-in.
- Reddit opinion. Our tools cannot open Reddit, and we did not try to get around this.
- Whether the FridgeWise reviews are independent.
- The phone layout and the user reviews of Well Stockd.

## 10. Sources

Store pages (read 12 November 2026):

- NoWaste: [Google Play](https://play.google.com/store/apps/details?id=com.khcreations.nowaste), [App Store](https://apps.apple.com/us/app/nowaste-food-inventory-list/id926211004)
- KitchenPal: [Google Play](https://play.google.com/store/apps/details?id=fr.icuisto.icuisto), [App Store](https://apps.apple.com/app/id1084982489)
- Expireless: [Google Play](https://play.google.com/store/apps/details?id=com.miklabs.foodgem), [site](https://food-assistant-2yi.pages.dev/)
- FridgeWise: [Google Play](https://play.google.com/store/apps/details?id=com.getfridgewise.app)
- Your Food: [Google Play](https://play.google.com/store/apps/details?id=com.HarderuesCompany.YourFood), [App Store](https://apps.apple.com/app/id6473174562)
- FridgeBuddy: [App Store UK](https://apps.apple.com/gb/app/id1500190823)
- Pantry Check: [App Store](https://apps.apple.com/us/app/pantry-check-grocery-list/id966702368)
- What The Fridge?!: [App Store](https://apps.apple.com/us/app/id6759576051)
- Wonder Fridge: [Google Play](https://play.google.com/store/apps/details?id=com.meolly.fridge)
- Expiry date tracker (shoyuland): [Google Play](https://play.google.com/store/apps/details?id=com.shoyuland.freshthings)
- Samsung Food: [Google Play](https://play.google.com/store/apps/details?id=com.foodient.whisk)
- Too Good To Go: [Google Play](https://play.google.com/store/apps/details?id=com.app.tgtg)
- Fridgely: [App Store, Not Found](https://apps.apple.com/us/app/fridgely/id988016972)
- CozZo: [App Store, Not Found](https://apps.apple.com/us/app/id1162606257)

Other sources:

- [Grocy site](https://grocy.info/) and [Grocy demo stock overview](https://demo.grocy.info/stockoverview)
- [Galaxus: a writer tries Grocy and stops](https://www.galaxus.ch/en/page/how-i-want-to-digitise-the-contents-of-my-fridge-and-fail-to-do-so-39565)
- [Privacy Guides forum thread](https://discuss.privacyguides.net/t/looking-for-a-app-to-track-fridge-freezer-contents-and-expiry-dates/22977)
- [Samsung support: Family Hub food list](https://www.samsung.com/us/support/answer/ANS10006842/)
- [Pickr: Samsung AI food management](https://www.pickr.com.au/news/2024/samsung-adds-ai-food-management-to-family-hub-french-door-fridges)
- [PeerPush: Well Stockd](https://peerpush.com/p/well-stockd)
- [AlternativeTo: Fridgely](https://alternativeto.net/software/fridgely/about), [AlternativeTo: KitchenPal](https://alternativeto.net/software/kitchenpal/about)
- [JustUseApp: CozZo reviews](https://justuseapp.com/en/app/1162606257/cozzo-food-inventory-manager/reviews) (weak source: automated summary)
- [chrome-stats: NoWaste](https://chrome-stats.com/d/com.khcreations.nowaste) (weak source: directory)
- [Springwise: Kitche](https://www.springwise.com/innovation/food-drink/an-app-helps-families-avoid-food-waste/), [Buckinghamshire Council: useful apps](https://buckinghamshire.gov.uk/cost-of-living/help-with-buying-or-accessing-food/toolkit-reducing-food-waste-at-home/useful-apps)

Second pass (read 12 November 2026):

- App Store review feeds (50 recent reviews a page): [NoWaste](https://itunes.apple.com/us/rss/customerreviews/page=1/id=926211004/sortby=mostrecent/json), [KitchenPal](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1084982489/sortby=mostrecent/json), [Pantry Check](https://itunes.apple.com/us/rss/customerreviews/page=1/id=966702368/sortby=mostrecent/json), [FridgeBuddy US](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1500190823/sortby=mostrecent/json), [FridgeBuddy UK](https://itunes.apple.com/gb/rss/customerreviews/page=1/id=1500190823/sortby=mostrecent/json), [Your Food](https://itunes.apple.com/us/rss/customerreviews/page=1/id=6473174562/sortby=mostrecent/json)
- Google Play "See all reviews" lists on the store pages of NoWaste, KitchenPal, Your Food, Wonder Fridge, InvenDo, and [Smantry (Germany)](https://play.google.com/store/apps/details?id=app.speisekammer&hl=de&gl=DE)
- New apps on Google Play: [Smantry](https://play.google.com/store/apps/details?id=app.speisekammer), [InvenDo](https://play.google.com/store/apps/details?id=com.chestersw.homelist), [MyKURA](https://play.google.com/store/apps/details?id=jp.gr.java_conf.indoorcorgi.mykura), [Best Before](https://play.google.com/store/apps/details?id=com.peytu.bestbefore), [My Pantry](https://play.google.com/store/apps/details?id=com.yustapps.pantry), [Limiter](https://play.google.com/store/apps/details?id=jp.labboy.limiterflutter), [유통기한 언제지](https://play.google.com/store/apps/details?id=kr.co.ourneeds.app), [Frigo Magic](https://play.google.com/store/apps/details?id=fr.haruni.frigomagic), [Phenix](https://play.google.com/store/apps/details?id=com.phenix.cajou)
- Archived App Store pages: [CozZo, 8 Feb 2025](https://web.archive.org/web/20250208120319/https://apps.apple.com/us/app/cozzo-fridge-pantry-inventory/id1162606257), [Fridgely, 9 Oct 2023](https://web.archive.org/web/20231009025759/https://apps.apple.com/us/app/fridgely/id988016972)
- Well Stockd: [home](https://wellstockd.com/), [features](https://wellstockd.com/features), [pantry inventory](https://wellstockd.com/pantry-inventory), [kitchen screen picture](https://www.wellstockd.com/_next/image?url=%2Fproduct%2Fkitchen-desktop.png&w=1920&q=75&dpl=dpl_He17XfFobbu3qyp2nLsYEF1jqE4U), [BetterLaunch](https://www.betterlaunch.co/product/well-stockd)
- [NoWaste site](https://www.nowasteapp.com) (4.1 stars from 2,700+ App Store ratings in all countries; up to 20 locations with Pro)
- [KitchenPal developer video: scan and add](https://www.youtube.com/watch?v=UGHvBF7wbJ0)
- [TapSmart review of Kitche (2020)](https://www.tapsmart.com/apps/food-drinks/review-kitche/)
- [Hacker News comments that name Grocy (Algolia search)](https://hn.algolia.com/api/v1/search?query=grocy&tags=comment&hitsPerPage=40)
- Design evidence: [Material Chip docs](https://github.com/material-components/material-components-android/blob/master/docs/components/Chip.md), [Material Tabs docs](https://github.com/material-components/material-components-android/blob/master/docs/components/Tabs.md), [Baymard: avoid horizontal tabs](https://baymard.com/research-articles/avoid-horizontal-tabs), [Baymard: colour swatches](https://baymard.com/research-articles/mobile-interactive-color-swatches)

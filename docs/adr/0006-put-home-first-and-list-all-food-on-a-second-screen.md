# Put Home first and list all food on a second screen

ADR 0002 removed the Home screen of FridgeFriend, with its greeting, its totals, and its list of sessions. It made the
use-first list the first screen. On 11 November 2026 the owner asked for two screens: a Home screen, and a screen that
lists all the food.

The first version of the two screens used the product identity in `design/product.md`, with each batch on a shelf
line. The owner saw it on the same day and did not want it. The owner then said to copy the two screens of
FridgeFriend (the `basic_ff` repository): Home (`app/(tabs)/index.tsx`) and My Fridge (`app/(tabs)/fridge.tsx`).

## Decisions

- **The two screens have the contents of FridgeFriend and the parts of Android.** The first copy had the layout,
  the sizes, and the colours of the FridgeFriend code. The owner saw it on 11 November 2026, and said to correct the
  colours and to make the app more native to Android. The Android app now uses Material 3 components: a navigation
  bar, a top app bar on My Fridge with the sort actions, a search field, filter chips, cards, and list items. It uses
  the type scale and the shapes of Material 3. The gradients, the glow, and the moving icon of FridgeFriend are not
  copied.
- **The colours are a Material 3 colour scheme from the green of FridgeFriend.** The seed colour is #53D181
  (`primary` in `styles/theme.ts`). The scheme is the "fidelity" scheme of material-color-utilities, which keeps this
  green as the primary container colour. The fresh green and the expiring amber of FridgeFriend are custom colours
  of the scheme, and expired has the error colours. Each pair of a text colour and its background has a contrast of
  4.5:1 or more. The app does not use the wallpaper colours of the phone, because the green is a part of the look.
  The apps follow the light and the dark appearance of the system.
- **The text starts from the text of FridgeFriend.** On 11 November 2026 the owner asked for a check of the two
  screens, and these parts changed:
  - The days left have the same words on the two screens: "Expired 3d ago", "Expired yesterday", "Expires today",
    "Expires tomorrow", and "Expires in 5d".
  - The totals card has no line "items tracked", because its label says the same.
  - A group with no batch says "All fresh", and that nothing has expired and nothing expires in the next 2 days. The
    number comes from the freshness rule. An inventory with no food says "No items yet".
  - My Fridge says "No matching items" when the chips and the search text leave no food.
  - The label of the totals card is "Total items". No text is in capital letters only.
- **The apps have the brand parts of the design system of the owner.** The owner asked for them on 11 November 2026,
  after the Material 3 version. `design/product.md` and the design system have the rules. The Android app has:
  - The signature gradient on the app icon, on the icon of the product on the totals card of Home, and on About. A
    screen has it one time, with no text on it.
  - About, which opens from Home. It shows the icon and the name of the product, the version, and "Made by" with the
    cvke letters.
  - The slice of the house brand above "No items yet", because the product has no motif of its own. The slice moves
    out and back slowly. This is the only motion for decoration.
  - A fade of 340 ms when content comes after loading, a spinner with the colours of the gradient, and a fade at
    the edge of a row that continues to the side. A tab change, a filter, a sort, and a number change have no motion.
  - No motion when the device has animations off.
- **Home is the first screen.** It has, in this order:
  1. A greeting for the time of day, and the title.
  2. A card with the totals: the number of foods, the number of expiring batches, and the number of expired batches.
  3. **Needs attention.** The first 5 expired and expiring batches, in the use-first order, in a row that scrolls
     sideways. If there is no such batch, the group says that all food is fresh. "View all" opens My Fridge.
- **My Fridge is the second screen.** It has one card for each product in each storage area. The card shows the
  freshness, the name, the sum of the quantities of the active batches there, the days left of the batch to use first,
  and the category. If the batches have more than one expiry date, the card shows how many.
- **My Fridge has chips, a search field, and a sort control.** One row of chips selects a storage area, and one row
  selects a category. Each row shows only the values that have food. The search text matches a part of the name, the
  category, the unit, or the name of the storage area, and case has no effect. The sort orders are name, expiry (the
  start order, soonest first), date added, quantity, and category. Food with no expiry date is last in both directions
  of the expiry order.
- **The app has two tabs: Home and My Fridge.** Back on My Fridge goes to Home.
- **A food is a product with an active batch.** The number of foods counts products, not batches.
- **The product rules stay.** Where FridgeFriend and a product rule differ, the rule applies:
  - An estimated expiry date shows as an estimate. The days left then end with "estimated".
  - The apps do not show sample food as real food. The debug build of the Android app can load a sample, and the
    screens then say that the food is a sample.
  - A failed load shows what failed, with Try again.
  - A touch target is 48 dp or more on Android. The Material components give this size.
- **Parts of FridgeFriend that need a function that the apps do not have yet are not on the screens:** the settings
  button, the add button, the tap and the long press on a card, and the notes of a food. They come with those
  functions. The sessions of FridgeFriend do not come back (ADR 0002), so Home has no Recent Activity group and the
  tab bar has no Sessions tab. The six other card styles of FridgeFriend are not copied.

This ADR replaces the last decision of ADR 0002.

## Consequences

- The proposed product identity (the teal accent and the shelf line motif) is not used on these screens.
  `design/product.md` records this. The generated colour files there do not give the colours of the apps now.
- The text of the two screens does not follow the glossary in each place: FridgeFriend says "items" where the glossary
  says food. The glossary records the screen names Home and My Fridge.
- The Android app does not have the exact colours of FridgeFriend. The page and the cards have a light green tint,
  and green text is darker than #53D181 in the light appearance.
- The decision about Material 3 is for the Android app. The owner has not said how the iOS app must look.
- The design system says that the signature gradient is for brand panels, and that a card stays flat. The icon of the
  product on the totals card is a small brand panel on a flat card. If the owner does not want it there, the tile
  gets the primary container colour again.
- The slice has the blue of the house brand, as the design system says, in an app that is green. It leaves when the
  product gets a motif.
- The use-first order stays a core rule with vectors. Which batches Home shows, and the cards, the search, and the sort
  orders of My Fridge, are rules of the screens. They have no vectors now. The Android app has them in
  `InventoryContent`, with unit tests. The iOS app must give the same result for the same inventory. If the two apps
  differ, move these rules to `spec/` with vectors.
- The term use-first list stays for the order of the batches.

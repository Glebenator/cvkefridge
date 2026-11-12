# CVKE Fridge: product identity

Follows My Design Language (version 7). Every UI, copy or styling session on this product reads this file first and follows it. Change it on purpose only, with a dated line under Decisions.

**Status: the accent and the brand parts are in the Android app. The motif is not agreed.** On 11 November 2026 the owner did not want the first screens with the teal accent and the shelf line. The accent is now the green of FridgeFriend. The Android app shows the contents of FridgeFriend with Material 3 components (ADR 0006). The owner then said to add the parts of the design system: the signature gradient, the cvke letters, and motion. The shelf line and the signature component below are a proposal that the apps do not use. Until the product has a motif, the slice of the house brand is in its place.

## The product

- **What it is:** A list of the food in the fridge that shows what to use first, on one phone.
- **Who uses it, and where:** A person at the open fridge door, phone in one hand, who puts the shopping away or decides what to cook. Also the same person in a shop, who wants to know what is at home.
- **The question they arrive with:** "What do I need to use before it goes off?"
- **The subject:** Food on a shelf, and the days it has left.

## Identity

| Part | Choice | Where it comes from |
| --- | --- | --- |
| Accent | `#53d181`; generated values in `design/product.css` | The green of FridgeFriend, which the owner wants to keep. The generator makes it darker for text and buttons on a light background. The Android app uses a Material 3 colour scheme from the same green. |
| Grounds | `#e9f1f0`, `#12343a` | Frosted glass, and the inside of the fridge with the door almost closed. |
| Frame | neutral | Short visits at the fridge door. The content carries the identity. |
| Display face | system, until the landing page | Not chosen. Choose it with the landing page, from the subject. |
| Motif (proposal, not used) | The shelf line: a fridge shelf drawn as a time line. It starts at the date added and ends at the expiry date. The batch stands on it at today. A printed date ends the line with a solid mark. An estimated date ends it with an open mark. | "Shelf life", drawn as a shelf. It shows how much of its life a batch has used, and how sure the end is. The number of days alone shows neither. |
| Signature component (app; proposal, not used) | Each batch on its shelf line, in the batch detail and in the Use first and Next groups of Home. It shows the product name, the quantity, the storage area, the days left, the position of today between the two dates, and printed or estimated. The part of the line before today is in the accent. An expired batch stands after the end of the shelf, on a dashed line. | |
| Signature moment (landing page) | The visitor picks a food and a storage area. The shelf line gets the length of the expiry estimate for that food, from the table of foods in the app. | |
| App icon | A fridge in the ink colour on the signature gradient, until the motif is agreed. The gradient uses the accent and `gradient-end` of the dark appearance, because the green of the light appearance is too dark to show the look. | |
| Signature gradient | On the app icon, on the icon of the product on Home, and on About. The spinner uses its colours. | `references/brand-layer.md` of the design system. |
| Maker mark | "Made by" with the cvke letters, on About. | `references/brand-layer.md` of the design system. |

Generated with:

```
node <skill>/scripts/product-css.mjs --name "CVKE Fridge" --accent "#53d181" --ground "#e9f1f0" --ground "#12343a" --frame neutral --out design/product.css --json design/product.json
```

Notes from the generator: the seed `#53d181` is too light for text and buttons on a light background, so the light accent is `#008343`. Use the seed as a ground or in the motif. On ground 1 (light), accent buttons pass but accent text does not, so links there use the ground text colour, underlined. On ground 2, primary buttons use the inverse style. The generator also warns that the hue of the accent is near the hue of the success colour. A status always has an icon or a word. The two grounds come from the teal proposal. Choose them again with the landing page.

## Words

House verbs (Create, Add, Edit, Delete, Remove, Archive, Save changes, Cancel, Close, Try again, Filter, Settings, Sign in) never change. The product's own nouns are in [GLOSSARY.md](../GLOSSARY.md). The ones that the interface shows:

| Use | Meaning | Don't use |
| --- | --- | --- |
| Storage area | Fridge, Freezer, or a storage area that the person created | Location, zone |
| Expiry date | The calendar date after which the food is not good | Expiration, best before |
| Estimated | An expiry date that the app suggested | Default, guess |
| Days left | Calendar days from today to the expiry date | Days remaining |
| Used | The food was eaten or cooked | Consumed, finished |
| Thrown away | Nobody used the food | Wasted, discarded |
| History | The food that was used or thrown away | Archive, log |
| Scan | Read a barcode with the camera | Capture |
| Reminder | The notification before food expires | Alert |

"Product" and "batch" are words for code and documents. The interface shows the name of the food and its quantity.

## Facts

The only facts, figures, prices, policies, names and claims the interface may state. Each has a source. Anything not listed here or in the product's live data is not stated.

| Fact | Value | Source |
| --- | --- | --- |
| Product name | CVKE Fridge (proposed) | An open decision in `docs/plan.md` |
| Maker | cvke | House |
| Product lookup service | Open Food Facts | FridgeFriend code |
| Expiry estimates | The days in `spec/foods.json` | USDA FSIS FoodKeeper Data, CC0 1.0 |

**Sample data** used in demos and screenshots: `SampleInventory` in the debug source set of the Android app. Its dates are a number of days from today, so each screen calculates the days left. It is not in the release build. It is labelled "Sample" wherever it appears.

## Decisions

Dated choices that switch on a house default's condition or change this identity.

- 2026-11-10: Identity proposed with the repository setup. Not agreed.
- 2026-11-10: The fridge device left the product (ADR 0002). The words for sessions left this file. The motif now stands for a batch, and it shows printed or estimated.
- 2026-11-10: Household sharing deferred. Its words are not in this file.
- 2026-11-11: The owner said to follow the design system for the first screens. Home and All food use the accent and the shelf line motif as proposed. The frame is not used: a phone app has a tab bar on `surface`, not a sidebar.
- 2026-11-11: Home is the first screen and All food is the second (ADR 0006). The signature component is in the Use first and Next groups of Home.
- 2026-11-11: The owner did not want the screens with this identity, and said to copy the Home and My Fridge screens of FridgeFriend. The Android app has no shelf line now, and it uses the colours of `styles/theme.ts` in the `basic_ff` repository.
- 2026-11-11: The owner said to correct the colours and to make the Android app native. The app uses Material 3 components and a Material 3 colour scheme from `#53d181`.
- 2026-11-11: The owner said to add the parts of the design system. The accent of this file is now `#53d181`. The Android app has the signature gradient on the app icon, on the icon of the product on Home, and on About. About has the maker mark. An empty state has the slice of the house brand, with the brand loop. Content after loading comes with a fade of 340 ms. The spinner has the colours of the gradient.

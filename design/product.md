# CVKE Fridge: product identity

Follows My Design Language (version 7). Every UI, copy or styling session on this product reads this file first and follows it. Change it on purpose only, with a dated line under Decisions.

**Status: proposal of 10 November 2026. The owner has not agreed it.** The start screens of both apps use the accent only. Agree or change this file before the first real screen.

## The product

- **What it is:** A list of the food in the fridge that shows what to use first, on one phone.
- **Who uses it, and where:** A person at the open fridge door, phone in one hand, who puts the shopping away or decides what to cook. Also the same person in a shop, who wants to know what is at home.
- **The question they arrive with:** "What do I need to use before it goes off?"
- **The subject:** Food on a shelf, and the days it has left.

## Identity

| Part | Choice | Where it comes from |
| --- | --- | --- |
| Accent | `#0e7c86`; generated values in `design/product.css` | The green-blue edge of a glass fridge shelf. Freshness uses the status colours green, amber and red in this product, so the accent stays cold and clear of all three. |
| Grounds | `#e9f1f0`, `#12343a` | Frosted glass, and the inside of the fridge with the door almost closed. |
| Frame | neutral | Short visits at the fridge door. The content carries the identity. |
| Display face | system, until the landing page | Not chosen. Choose it with the landing page, from the subject. |
| Motif | The shelf line: a fridge shelf drawn as a time line. It starts at the date added and ends at the expiry date. The batch stands on it at today. A printed date ends the line with a solid mark. An estimated date ends it with an open mark. | "Shelf life", drawn as a shelf. It shows how much of its life a batch has used, and how sure the end is. The number of days alone shows neither. |
| Signature component (app) | Each batch on its shelf line, in the batch detail and at the top of the use-first list. It shows the product name, the quantity, the days left, the position of today between the two dates, and printed or estimated. | |
| Signature moment (landing page) | The visitor picks a food and a storage area. The shelf line gets the length of the expiry estimate for that food, from the table of foods in the app. | |
| App icon | The shelf line on the accent. The scaffold uses a fridge outline until the motif is agreed. | |

Generated with:

```
node <skill>/scripts/product-css.mjs --name "CVKE Fridge" --accent "#0e7c86" --ground "#e9f1f0" --ground "#12343a" --frame neutral --out design/product.css --json design/product.json
```

Notes from the generator: on ground 1 (light), accent buttons pass but accent text does not, so links there use the ground text colour, underlined. On ground 2, primary buttons use the inverse style.

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
| Product name | CVKE Fridge (proposed) | Decision 3 in `docs/plan.md`, open |
| Maker | cvke | House |
| Product lookup service | Open Food Facts | FridgeFriend code |
| Expiry estimates | None yet. The table of foods has no agreed source (decision 2 in `docs/plan.md`). | |

**Sample data** used in demos and screenshots: none yet. It is labelled "Sample" wherever it appears.

## Decisions

Dated choices that switch on a house default's condition or change this identity.

- 2026-11-10: Identity proposed with the repository setup. Not agreed.
- 2026-11-10: The fridge device left the product (ADR 0002). The words for sessions left this file. The motif now stands for a batch, and it shows printed or estimated.
- 2026-11-10: Household sharing deferred. Its words are not in this file.

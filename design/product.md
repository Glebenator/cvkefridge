# CVKE Fridge: product identity

Follows My Design Language (version 7). Every UI, copy or styling session on this product reads this file first and follows it. Change it on purpose only, with a dated line under Decisions.

**Status: proposal of 10 November 2026. The owner has not agreed it.** The start screens of both apps use the accent only. Agree or change this file before the first real screen.

## The product

- **What it is:** A list of the food in the fridge that shows what to use first.
- **Who uses it, and where:** A person at the open fridge door, phone in one hand, who decides what to cook or what to buy.
- **The question they arrive with:** "What do I need to use before it goes off?"
- **The subject:** Food on a shelf, and the days it has left.

## Identity

| Part | Choice | Where it comes from |
| --- | --- | --- |
| Accent | `#0e7c86`; generated values in `design/product.css` | The green-blue edge of a glass fridge shelf. Freshness uses the status colours green, amber and red in this product, so the accent stays cold and clear of all three. |
| Grounds | `#e9f1f0`, `#12343a` | Frosted glass, and the inside of the fridge with the door almost closed. |
| Frame | neutral | Short sessions at the fridge door. The content carries the identity. |
| Display face | system, until the landing page | Not chosen. Choose it with the landing page, from the subject. |
| Motif | The shelf line: a fridge shelf drawn as a time line. It starts at the date added and ends at the expiry date. The item stands on it at today. | "Shelf life", drawn as a shelf. It shows how much of its life an item has used, which the number of days alone does not. |
| Signature component (app) | Each item on its shelf line, in the item detail and at the top of the list for the item to use first. It shows the name, the quantity, the days left, and the position of today between the two dates. | |
| Signature moment (landing page) | The visitor picks a category and a storage area. The shelf line gets the length of that shelf life, from the table of defaults in the app. | |
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
| Item | One food in the inventory | Product, entry |
| Storage area | Fridge, Freezer, or a storage area that the person created | Location, zone |
| Expiry date | The calendar date after which the item is not good | Expiration, best before |
| Days left | Calendar days from today to the expiry date | Days remaining |
| Session | The detections of one use of the fridge | Event, scan |
| Detection | One food that the fridge device saw | Session item |
| Approve | Apply a session to the inventory | Process, verify, confirm |

## Facts

The only facts, figures, prices, policies, names and claims the interface may state. Each has a source. Anything not listed here or in the product's live data is not stated.

| Fact | Value | Source |
| --- | --- | --- |
| Product name | CVKE Fridge (proposed) | Decision 3 in `docs/plan.md`, open |
| Maker | cvke | House |
| Product lookup service | Open Food Facts | FridgeFriend code |
| Shelf-life defaults | The table in `docs/legacy-fridgefriend.md`, until milestone 1 confirms it | FridgeFriend code |

**Sample data** used in demos and screenshots: none yet. It is labelled "Sample" wherever it appears.

## Decisions

Dated choices that switch on a house default's condition or change this identity.

- 2026-11-10: Identity proposed with the repository setup. Not agreed.

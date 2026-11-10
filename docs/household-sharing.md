# Household sharing: a design note for later

Date: 10 November 2026. Status: deferred. The owner wants household sharing in the product, and deferred it on
10 November 2026. It is not in the milestones of [the plan](plan.md). This note keeps the recommended design, so that
the work can start from it later. Nothing here is agreed.

The aim: the phones of one household show the same inventory, Android and iOS together, and no service can read it.

## What the apps do now for it

- The app keeps a change log from the first milestone ([ADR 0003](adr/0003-keep-stock-as-products-and-batches.md)).
- Each product, each batch, and each change gets a random identifier that is unique on all phones.

Sharing can then send a log that the app already keeps, and no data needs a conversion.

## The recommended design

- **No account.** The app asks for no e-mail address, no name, no telephone number, and no password.
- **A household is a random identifier and a random key.** The first phone makes them. The key stays in the secure
  storage of the phone (Android Keystore, iOS Keychain).
- **A person joins with a QR code.** A member shows the code on a phone, and the new member scans it. The code carries
  the identifier and the key. The key goes from screen to camera. It does not go through the network.
- **Each change is encrypted on the phone.** The app encrypts each record of the change log with the household key
  before the record leaves the phone. It uses the authenticated encryption of the platform libraries. It has no
  cryptography of its own.
- **A relay stores and passes the encrypted changes.** The relay is a small service. It cannot read a food name, a
  date, a barcode, or a quantity, because it does not have the key.
- **Each phone has the full inventory.** The app works in full without a connection. It sends and gets changes when
  it has a connection again. The core modules merge the changes with fixed rules, which test vectors define.
- **Reminders stay local.** Each phone calculates its reminders from its copy of the inventory. No push service gets
  inventory data.
- **Sharing is optional.** A person who does not make or join a household uses no relay.

## What the relay can see

| The relay sees | The relay does not see |
|---|---|
| A random household identifier | Who the members are |
| The size and the time of each encrypted change | Food names, barcodes, dates, quantities, storage areas |
| The network address of a request, as each server does | The household key |

The relay keeps no logs of network addresses longer than it needs for protection against misuse. A phone proves that
it is a member with a token that it calculates from the household key, so the relay needs no accounts.

## What this design costs

- **No recovery.** No account means that nobody can restore a household. If each phone of a household is lost, the
  inventory is lost. An export file is the backup.
- **Removal needs a new key.** To remove a member, the other members make a new key and share a new QR code.
- **A QR code is a secret.** A person who gets a picture of it can read the inventory until the key changes.
- **A fourth component.** The relay needs a repository, a deployment, and a small running cost.
- **Changes arrive at the next sync, not at once.** A first version syncs when the app opens and when the system
  gives it background time. Instant updates need push messages.
- **Photos do not sync in a first version.** They are large.
- **Shared test vectors become necessary.** An Android phone and an iPhone in one household must read the changes of
  each other, byte for byte.

## The alternatives

| Alternative | Why not |
|---|---|
| iCloud or a Google account | Each works on one platform only. A household with an iPhone and an Android phone cannot share. |
| A usual backend with sign-in (for example Firebase) | It needs an e-mail address, and the service can read each inventory. |
| Sync on the home Wi-Fi only, with no server | Both apps must be open at the same time on the same network. The person in the shop does not see what the person at home changed. |

## Decisions to make when the work starts

- This design, or another.
- Where the relay runs.
- The terms for the glossary: household, member, relay.

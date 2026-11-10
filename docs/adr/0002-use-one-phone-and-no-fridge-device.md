# Use one phone and no fridge device

FridgeFriend got a part of its data from a fridge device: a camera in the fridge that detected the food that went in
and came out, and sent sessions to the app. The rewrite has no fridge device. One phone does each task.

The device link did not work from end to end. The app listened for sessions on MQTT, with a broker address that the
released build did not have. The device software sent barcodes with HTTP, in a different format. An app that needs
hardware that one person owns has no users in a store.

## Decisions

- **No fridge device.** We removed sessions, detections, approval, the MQTT connection, and the search for a device on
  the local network. The apps ask for no permission for the local network.
- **The phone camera reads barcodes.** FridgeFriend had no scanner in the app. A barcode came only from the device.
- **The app reminds the person.** FridgeFriend had no notifications. The answer of the app was visible only when the
  person opened it.
- **The use-first list is the first screen.** We removed the Home screen with its greeting, its totals, and its list of
  sessions.

## Consequences

- Each change to the inventory comes from a person. The app must make adding food and finishing food fast, because
  nothing else keeps the inventory correct.
- The glossary has no terms for sessions. `docs/legacy-fridgefriend.md` keeps the record of the old session rules.
- A later product can add a device as one more way to add food. It then goes through the same change log as a person.

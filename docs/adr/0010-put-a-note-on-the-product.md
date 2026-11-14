# Put a note on the product

On 14 November 2026 the owner asked for notes on food. FridgeFriend had one note on each item
([legacy-fridgefriend.md](../legacy-fridgefriend.md)). The rewrite has products and batches (ADR 0003), so a note can
be on the product or on a batch. The owner selected the product.

## Decisions

- **A product has one optional note.** It is a text, or no note. All batches of the product show the same note. A
  note for one purchase, for example "opened on Tuesday", is also on the product.
- **The note is in the `productSaved` change.** Rule 7.2 of `spec/rules.md` has the key `note`. A save of the product
  with no note removes the note. The note needs no new change type.
- **A change with no `note` key has no note.** The change logs on the phones from before this decision have no `note`
  key. Both core modules read these changes. They write the key `note` in each new `productSaved` change.
- **The core keeps the text as it is.** The app removes the spaces at the start and at the end before it saves, and it
  saves no note in place of an empty text.
- **The screens:**
  - The screen of the food shows the note below the product. A tap on the note edits it in place, with "Save" and
    "Cancel". A product with no note has "Add a note".
  - The form that edits a product has a note field.
  - The add form has a note field. See the next decision.
  - The card on My Fridge shows the first line of the note.
  - The search of My Fridge also compares the text with the note.
- **The note field of the add form does not remove a note.** The add form can add a batch to a product that exists.
  For a new product, the note is the text of the field. When the person selects a product from the suggestions, or
  uses "Add again", the field shows the note of that product. For a product that exists, a different text replaces
  the note, and an empty field keeps the note. Only the screen of the food and the edit form remove a note. The undo of
  the add also brings back the earlier note, because the note is in the same changes as the batch.

## Results

- The vectors of `change-log.json` have a case with a note and a product with no `note` key, and a case that removes
  a note. The expected products of all cases have `note`.
- An earlier version of the app reads a change log with a note, but it does not keep the note: both codecs ignore a
  key that they do not know. The app has no users yet, so no conversion is necessary.
- A note is text from the person. Like a product name, it does not go to logs or to crash reports.
- The iOS app gets the screens of the note when it builds the screen of a food and My Fridge (milestone 2).

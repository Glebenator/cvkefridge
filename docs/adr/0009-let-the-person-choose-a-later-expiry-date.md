# Let the person choose a later expiry date

On 13 November 2026 the owner asked: a food is expiring or expired, but the date was not right and the food is still
good to eat. The screen of the food must have quick buttons that give it more time: one day, one week, or another date.

The core had two sources of an expiry date: `printed` and `estimated`. A later date from the person is neither. If the
app keeps it as a printed date, the screen says "Printed date" for a date that is not on the package. The product
rule "Do not show a guess as a fact" does not permit that.

## Decisions

- **An expiry date has a third source: `chosen`.** A chosen date is a later date that the person selected because the
  food is still good. Rule 5 of `spec/rules.md` and the glossary have it. The use-first order, the days left, and the
  freshness use the date in the same way for each source.
- **The screens show a chosen date as "Your date".** It is not shown as an estimate, and not as a printed date.
- **A batch that is expiring or expired has "Still good?" on the screen of the food,** with "+1 day", "+1 week", and
  "Other date". The quick buttons add days to the expiry date. An expired batch starts from today, not from its expiry
  date, so "+1 day" means good until tomorrow. The change is one `batchEdited` change, and the message has "Undo".
- **The edit form keeps a chosen date** while the person does not select another date. A date that the person selects
  in the form is a printed date, as before.

## Results

- Both core modules read and write the source `chosen`. A change log with `chosen` cannot be read by an earlier version
  of the app. The app has no users yet, so no conversion is necessary.
- The vectors have a case for a `batchEdited` change with a chosen date, and a case for the use-first order with a
  chosen date.
- The iOS app gets the quick buttons when it builds the screen of a food (milestone 2).

# Put Settings in the navigation bar, and take a product photo with the camera

On 13 November 2026 the owner used the Android app and asked for four changes:

- A product photo can come only from the gallery. The person cannot take a picture of the food.
- The add form has no photo.
- When the person opens My Fridge from the navigation bar, the filters of an earlier visit stay. My Fridge must start
  again: the Fridge, with no filter.
- The navigation bar will probably not get other destinations, so Settings goes there. The person must be able to turn
  off the wallpaper colours, as in CVKE GPS.

## Decisions

- **Settings is a destination of the navigation bar.** The bar has Home, My Fridge, the add button, History, and
  Settings. The settings button at the top of Home goes. About stays on Home. The Material navigation bar is for three
  to five destinations, so the bar is now full.
- **A tap on My Fridge in the navigation bar starts My Fridge again.** It shows the Fridge, with no category, no
  freshness, and no search text. The sort order stays, because it is a preference and not a filter. The other ways to
  open My Fridge do not change: "View all" and the numbers on Home, and a tap on the reminder, show all storage areas
  with their filter.
- **The Android app has the setting "Wallpaper colours".** It is in Settings, in the group "Appearance", and it is on
  at the start. Off gives the colour scheme from the green of FridgeFriend, as on Android 10 and 11. The colours of
  fresh, expiring, and expired, and the brand parts, do not change. Android 10 and 11 have no wallpaper colours, so the
  switch is not there. This replaces one sentence of ADR 0007: "The app has no setting for this." The other decisions
  of ADR 0007 stay.
- **A product photo has two sources: the camera and the photos of the phone.** The screen of a food has "Take a photo"
  and "Choose a photo", and "Change photo" has the same two. The add form has the same field, at its end, for a new
  food and for a food in the inventory with no photo. The product gets the photo of the form when the form saves.
- **The camera needs the camera permission.** The app explains it before the system asks. When the system does not ask
  again, the app says so and opens the settings of the app. "Choose a photo" needs no permission and is always there.
  With no camera, only "Choose a photo" is there.

## Differences between the apps

- iOS has no wallpaper colours, so the iOS app has no switch for them. This is an intended difference (ADR 0007).
- The Android app takes the picture with the camera app of the phone (`ACTION_IMAGE_CAPTURE`). The iOS app uses the
  camera of the system in the way that is usual on iOS. The result is the same: a photo of the product that stays on
  the phone.

## Results

- The navigation bar has no place for a new destination. A new destination needs a new decision.
- The photo of a product is still not in the change log, and the shared specification has no rule for it (plan,
  section 6.1).
- A picture of the camera app stays in the cache of the app for a short time. The app deletes it after it makes the
  photo, and deletes the files of a stopped capture at the next start.

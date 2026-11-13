# Use the wallpaper colours on Android

ADR 0006 gave the Android app one Material 3 colour scheme from the green of FridgeFriend (#53D181). It said that the
app does not use the wallpaper colours of the phone, because the green is a part of the look.

On 12 November 2026 the owner used the app on a phone with a blue wallpaper. All of the app was green, and it did not
agree with the other apps on the phone. The owner said to use the wallpaper colours.

## Decisions

- **On Android 12 and later, the colour scheme comes from the wallpaper colours of the phone.** This is the dynamic
  colour of Material 3. The surfaces, the navigation bar, the tabs, the chips, and the buttons have these colours. The
  apps follow the light and the dark appearance of the system, as before.
- **On Android 10 and 11, the colour scheme is the scheme from the green of FridgeFriend.** These versions have no
  wallpaper colours. The scheme is the one that ADR 0006 describes.
- **Colours with a fixed meaning do not follow the wallpaper.** Fresh is green and expiring is amber with each
  wallpaper. They are the custom colours of ADR 0006. Expired has the error colours of the scheme, which are red with
  each wallpaper.
- **The brand parts do not follow the wallpaper.** The signature gradient, the slice, and the app icon keep their
  colours.
- **The app has no setting for this.** A person changes the colours with the wallpaper and the colour settings of the
  phone.

This replaces one sentence of ADR 0006: "The app does not use the wallpaper colours of the phone, because the green is
a part of the look." The other decisions of ADR 0006 stay.

## Difference between the apps

iOS has no wallpaper colours. The iOS app keeps the green of FridgeFriend as its accent colour. This is an intended
difference.

## Results

- The green of FridgeFriend is not the main colour of the Android app on most phones. It stays in the fresh status,
  in the signature gradient, and in the app icon.
- A screen can have a status colour next to a scheme colour of any hue. The status colours are not adjusted to the
  wallpaper. Check a new screen with more than one wallpaper colour.
- Code must not use a role of the colour scheme for a meaning that needs one hue. For example, `primary` is not
  "fresh".
- Screenshots of the Android app are different from phone to phone.

---
type: category-product-strategy
category: universal-tv-remote
member: harshil
updated: 2026-10-06
status: draft
sources: [context.md, screenshots:66 across 7 apps (+ 1 analysis PDF, 7 pages), knowledge:sanibha-app-factory-knowledge-base.md;us_ios_app_factory_knowledge_base_2026-10-04.md (grep only, no benchmarks used in this note), web:2]
---

# Universal TV Remote — final recommendations (v1)

Built from [[research/categories/universal-tv-remote/context]] and the team's in-app captures of seven remote apps. Every capture is from an India storefront (₹ prices, +91 account). Nothing here converts ₹ to US prices. All our prices are UNKNOWN until s5-monetization sets them. No capture shows a TV actually connected or a command succeeding in any app (see Before build), so everything below about the connected state is our design, not a copy of a competitor.

## Positioning

**Line:** For anyone whose TV remote is lost, dead or out of reach. Find your TV, test that it responds, then use a clean remote with no ads and no pop-ups on the basic buttons. We tell you which controls work on your TV before you pay for anything.

**Positioning statement:** For people who just reached for the remote and it is not there, Remote Ready is the TV remote app that proves it works with your TV before it asks for money. Unlike the seven apps we captured, it never puts a paywall between you and a connected TV, never shows "Device found" before a TV has answered, and never shows a button that your TV can't act on.

| Layer | Call |
|---|---|
| Acquisition hook | "Will a remote app actually work with your TV? Test it first." |
| Product differentiator | A Connection Test where the user sees their own TV respond, a per-TV list of which controls work, and basic buttons that are never paywalled or interrupted. |
| Emotional benefit | Confidence that the remote will work when the user reaches for it. |
| Retention reason | The app reopens already connected to the last TV, and when it can't, it says why and what to try. |

**Who it's for:**
- Primary: a US adult in a household with a smart TV or streaming player (Roku, Samsung, LG first) whose physical remote is missing, broken, out of batteries or just not within reach.
- Trigger moment: the TV is on or needs to be turned on, and there is no remote.
- Searches: "tv remote", "universal remote", "remote for [brand] tv", "roku remote", "lost tv remote".
- Fears: paying and finding it doesn't work with their TV, subscription pop-ups when they only want the volume, a weekly charge they forget, the app not reconnecting tomorrow.
- Secondary: households with two TVs, and people who prefer a phone remote for typing and app launching (Plus).

**Job to be done:** "Make my TV respond to my phone, right now, and every time after."

**Name placeholder:** Remote Ready. Name territory: ready, ready-to-go, prove, connected. Treat it as a placeholder until the name is cleared.

**Proof points that must be visible in the product:**
- A discovered TV is listed by its name and brand, and only becomes "Connected" after a command has been sent and the user has confirmed the TV responded.
- The result card lists each control as Verified, Not confirmed or Not available on this TV.
- The remote only shows buttons the connected TV can act on. Unsupported buttons are hidden or shown as unavailable, never live-looking.
- When the TV isn't reachable the app says what it checked (iPhone Wi-Fi, TV found, TV responding) and what to try.
- No banner ads anywhere in the app.
- Cold launch to a verified command needs no onboarding slides, no tracking prompt, no sign-in, no paywall.

**App Store screenshots 1–3 (one story: find → prove → stay connected):**

| # | Headline | Shows |
|---|---|---|
| 1 | "Find your TV. Test the remote." | The TV list with one TV found and the Connection Test question "Did your TV move right?" |
| 2 | "Know exactly what works on your TV." | The result card: Navigation verified, Volume verified, Keyboard available, Power on not available on this setup |
| 3 | "Reconnect without the hassle." | The reconnect screen with iPhone Wi-Fi, TV found, TV responding checks and the Try again button |

Screens 4–6: "One swipe pad for the couch." (Touchpad, Plus), "Type on your phone, not your TV." (Keyboard, Plus), "No ads. No pop-ups on the basic buttons." (Classic remote and Settings). In the first storefront test, run this order against an order with the Touchpad as shot 2.

**Ad angles:**
1. **Proof (lead):** screen recording. A TV is on, the app finds it, the user taps Send test, the real TV highlight moves, the user taps Yes, the result card appears. End card: "Test it before you pay."
2. **Control:** "Lost your TV remote?" A person searches the sofa, opens the app, the TV answers. Same first screens as angle 1.
3. **Reconnect:** "It worked yesterday." A TV that was asleep, then the app reconnecting and the volume changing. End card: "Reconnects when you do."
4. **Brand (test after 1–3 have a baseline):** "Control your Samsung TV from iPhone.", "Find and connect your LG TV.", "A simple remote for your Roku TV." Same screens as angle 1 with the brand's pairing step.

Each angle gets its own Custom Product Page whose screenshots match the ad. Brand ads deep link to the brand's pairing screen where the OS allows it; otherwise to the Find my TV screen.

| Angle | Custom Product Page headline (shot 1) | First action in app | Paywall moment it leads to |
|---|---|---|---|
| 1 Proof | "Find your TV. Test the remote." | Find my TV | none until a Plus feature is tapped |
| 2 Control | "Turn your iPhone into a TV remote." | Find my TV | none until a Plus feature is tapped |
| 3 Reconnect | "Reconnect without the hassle." | Find my TV | none until a Plus feature is tapped |
| 4 Brand | "Control your [Samsung / LG / Roku] TV from iPhone." | Brand pairing screen | none until a Plus feature is tapped |

Channel call: Apple Search Ads and organic search first (high-intent: someone needs a remote now). Meta proof and reconnect creatives run second on the same screens.

**Messaging table (placeholder copy for the ASO agent; store limits apply):**

| Surface | Line |
|---|---|
| App name (placeholder) | "Remote Ready: TV Remote" |
| Subtitle (placeholder) | "Test it with your TV first" |
| Promotional text | "Find your TV, test that it responds, and see which controls work. No ads. No pop-ups on the basic buttons." |
| First line of description | "Use your iPhone as a TV remote and test it with your TV before you pay for anything." |
| Ad end card | "Test it before you pay." |
| Icon direction | A rounded square with a single check mark inside a rounded remote-button shape, on deep graphite. No brand logos, no purple gradient, no crown. |

**We will never claim:**
- "Works with all TVs", "universal", "all major brands", "compatible with every model". Compatibility is shown per TV, after a test.
- "Official", "licensed" or any relationship with Roku, Samsung, LG, Amazon, Apple, Google, Sony, TCL, Hisense or Vizio. Brand names appear as text, with "Not affiliated with any TV brand." in the description.
- "Works without Wi-Fi", "infrared", "IR", "no Wi-Fi needed". The iPhone talks to the TV over the local network.
- "Turns on any TV." Power on works only where the TV allows it, and we say which.
- "Unlimited" anything, "100% no ads" in a way that implies a competitor, "no risk", "free" next to anything that costs money.
- "#1", "Top remote", "15M+ users", "4.8 rating", rating counts, laurels, "trusted by" lines, press logos.
- "Replaces your remote" without "when your TV supports it".
- "Screen mirroring", "casting", "AirPlay" or "voice control" in v1.
- "Free trial" without the price after the trial next to it.
- "Mega sale", "limited time offer", any percentage-off or "SAVE n%" badge.

## UI/UX

**Design principles (tie-breakers):**
1. The first ask is local network access, and it comes after one sentence of explanation. No tracking prompt, no sign-in, no slides, no notification ask, no rating ask and no paywall before the user has seen their own TV respond.
2. "Connected" means a command was sent and the user confirmed it. A discovered TV is "Found", never "Connected".
3. The remote reflects the TV. A button that this TV can't act on is hidden or marked unavailable.
4. Basic buttons are never interrupted. Volume, mute, arrows, OK, Back, Home, Play/Pause and Power off never trigger a paywall, ad, offer or rating prompt.
5. Failure has a next step, never just a red error. Every failure shows what we checked, what is likely, and one button to try.
6. One surface for use: the remote. The TV switcher, Apps and Settings are one tap away and nothing else is a tab.
7. Say what we know and what we don't. We state what was checked and use "may" for causes we can't confirm.

**Structure (no tab bar):**
- **Remote (home):** header chip with the TV name and a status dot (tap opens the TV switcher sheet); Classic remote below; a mode switch (Buttons, Touchpad [Plus], Numbers); a Keyboard button [Plus]; an Apps button [Plus]; a gear icon for Settings.
- **TV switcher (sheet):** saved TVs with Ready, Not reachable on this Wi-Fi or Asleep status; Add a TV.
- **Settings:** Plus (status and Manage subscription), Restore purchases, My TVs (Rename, Forget), Power on from phone, Haptics, Large buttons, Help and troubleshooting, What works on my TV, Privacy, Terms, Version, Contact support.
- No Cast, Mirroring, Channels, Browser, IPTV, AI, "More Apps", Share-with-friends, Twitter or Change App Icon items.

**First five minutes:**

| # | Screen | Purpose | What's on it | Primary action | Copy direction | Asks | Given so far |
|---|---|---|---|---|---|---|---|
| 1 | Find your TV (cold launch) | Start the job at once | One headline, one sentence on why local network access is needed, one button; no slides | Find my TV | "Let's find your TV." | nothing | the app |
| 2 | iOS local network prompt | Permission | System prompt with our purpose string | Allow | system | local network | a stated reason |
| 3 | Searching | Show progress and what we check | Spinner, "Looking for TVs on this Wi-Fi", check rows (iPhone Wi-Fi, TVs found), "I don't see my TV" link | wait | "Looking for TVs on this Wi-Fi…" | nothing | live status |
| 4 | TVs found | Choose | List of found TVs with name and brand, "Not here? Pick your brand" | tap a TV | "Which one is yours?" | a choice | the list |
| 5 | Pairing | Authorize | Brand-specific one-line instruction, a code field only if the TV shows a code, a live "Waiting for your TV…" state | Accept on TV / enter code | "Look at your TV. Accept the request." | TV-side accept or a code | nothing more |
| 6 | **Connection Test: first win** | Prove it | "Press the right arrow" step: the app sends one Right command and asks "Did the highlight on your TV move right?" with Yes / No; volume step optional | Yes | "Did your TV respond?" | a yes/no | the TV moved |
| 7 | Result card | Show what works | Rows: Navigation, Volume, Keyboard, Apps, Power on, each Verified / Not confirmed / Not available on this TV; "Open my remote" | Open my remote | "Here's what works on your TV." | nothing | a per-TV capability list |
| 8 | Remote | Use it | Classic remote, state chip "Living Room TV · Connected" | any button | none | notification ask: none | a working remote |

- First win is screen 6. From cold launch to a confirmed command is 5 taps in the app: Find my TV, Allow, the TV, Send test, Yes. Pairing on the TV itself is outside the app. No tap is spent on slides, tracking, sign-in or a paywall.
- No onboarding carousel, no launch paywall, no brand grid that the user must pick before search. The brand list appears only if discovery fails or the user taps "Pick your brand".
- If the user taps No in the test, go to the Not confirmed state (below).

**Copy deck by screen (exact lines; [brackets] are filled live; nothing in brackets is hard-coded):**

| Screen | Element | Copy |
|---|---|---|
| Find your TV | Headline | "Let's find your TV." |
| Find your TV | Body | "Remote Ready looks for TVs on your Wi-Fi so it can send them button presses." |
| Find your TV | Button | "Find my TV" |
| Find your TV | Under button | "Not affiliated with any TV brand." |
| iOS permission string | NSLocalNetworkUsageDescription | "Remote Ready looks for your TV on this Wi-Fi so it can send it button presses." |
| Searching | Title | "Looking for TVs on this Wi-Fi…" |
| Searching | Check rows | "iPhone is on Wi-Fi" / "Looking for your TV" |
| Searching | Link | "I don't see my TV" |
| TVs found | Title | "Which one is yours?" |
| TVs found | Row sublabel | "[Brand] · Found on this Wi-Fi" |
| TVs found | Footer | "Not here? Pick your brand" |
| Pairing | Generic | "Look at your TV. Accept the request, or enter the code it shows." |
| Pairing | Waiting | "Waiting for your TV…" |
| Pairing | Code field | "Code from your TV" |
| Pairing | Roku | "On your Roku, allow control from mobile apps: [Roku setting path UNKNOWN until verified on a device]." |
| Test | Title | "Let's check it works." |
| Test | Step 1 | "We'll press Right once. Watch your TV." |
| Test | Question | "Did the highlight on your TV move right?" |
| Test | Buttons | "Yes" / "No" |
| Test | Volume step | "We'll turn the volume up one step. Okay?" with "Test volume" / "Skip" |
| Test | Success | "Navigation verified. You confirmed your TV responded." |
| Result card | Title | "Here's what works on your TV." |
| Result card | Row labels | "Navigation: Verified", "Volume: Verified", "Keyboard: Available with Plus", "Apps: Available with Plus", "Power on: Not available on this setup" |
| Result card | Row if untested | "[Control]: Not tested yet" |
| Result card | Button | "Open my remote" |
| Result card | Link | "See what Plus adds" |
| Remote | State chip | "[TV name] · Connected" |
| Remote | Locked control | a lock chip on the control; no text pop-up |
| Reconnect | Title | "Let's reconnect your TV." |
| Reconnect | Body | "[TV name] isn't responding." |
| Reconnect | Check rows | "iPhone Wi-Fi: Connected" / "Local network access: Allowed" / "TV responding: Not yet" |
| Reconnect | Explainer | "Your TV may be off, asleep, or on a different network." |
| Reconnect | Buttons | "Try again" / "Show me how to fix it" |
| Plus sheet | Title | "Remote Ready Plus" |
| Plus sheet | Free line | "Your basic remote stays free." |
| Settings | Power on | "Power on from phone" |
| Settings | Forget | "Forget this TV" |

**Permissions:**
- Local network: asked once on the first Find my TV tap, after the explanation on screen 1. If denied, every later Find my TV shows the Local network off card (below); the app never re-triggers the system prompt and offers "Open Settings". Detection method for a denied permission is [UNKNOWN: feasibility; verify in a build].
- Notifications: not asked in v1.
- App Tracking Transparency: not shown in v1. Whether attribution needs it is a decision in Before build.
- Rating: system review request only, after the third successful session on a Verified TV, never right after a failure, never near a paywall. No custom "Enjoying?" or "App improvements" sheet.
- Camera, location, photos, microphone, contacts: not requested in v1.

**Core loop and repeat use:**
- Day 2 and later: open the app, it reconnects to the last TV by itself, the chip shows "Ready" within a few seconds [UNKNOWN: target time, set after first cohort], the remote works. If it can't, the Reconnect screen opens.
- Day 2 and later with two TVs: the switcher chip shows both; tap to switch.
- Week 2: nothing prompts the user. No streaks, reminders or guilt copy. Siri Shortcuts and widgets are in Later.
- What brings users back: the next time the physical remote isn't in reach.

**Key screens:**

*Remote (Classic)*
```
Living Room TV · Connected          [gear]
[Buttons] [Touchpad 🔒] [Numbers]
 [Power]      [Home]       [Back]
          [   ^   ]
          [<  OK  >]
          [   v   ]
 [Vol -] [Mute] [Vol +]
 [Rewind] [Play/Pause] [Fast fwd]
 [Keyboard 🔒]      [Apps 🔒]
```
- States:
  - Connected: all verified controls live.
  - Connected, a control unavailable on this TV: the control is hidden or dimmed with an "Unavailable" label on tap-and-hold.
  - Reconnecting: chip reads "Reconnecting…", buttons stay visible and show a brief "Not sent" toast if pressed.
  - Not reachable: the remote dims and the Reconnect screen's check rows appear as a bottom card with Try again.
  - No TV saved: the remote is replaced by Find your TV.
  - Plus control tapped by a free user: the Plus sheet opens (see Paywall rules).
  - Offline iPhone (no Wi-Fi): "Your iPhone isn't on Wi-Fi."
- Most important element: the state chip and the OK/arrow cluster beside it.

*Connection Test*
```
Let's check it works.
We'll press Right once. Watch your TV.
[ Send test ]
Did the highlight on your TV move right?
[ Yes ]   [ No ]
```
- States:
  - Ready: Send test is the only action.
  - Sent: "Sent. Did the highlight on your TV move right?" with Yes / No.
  - Yes: row becomes Verified; next step is Volume (optional) then the result card.
  - No: Not confirmed state with three actions.
  - Command failed to send: "We couldn't send that to your TV." with Try again and Show me how to fix it.
  - TV not on a screen that shows a highlight (a video is playing): "If a video is playing, press Home first." with a Send Home button.
- Most important element: the Yes / No question.

*Result card*
- Layout: title, one row per control with an icon and a word (not colour alone), then Open my remote, then the See what Plus adds link.
- States:
  - All verified.
  - Some Not confirmed: row says "Not confirmed. Try again" with a Retry on that row.
  - Not available on this TV: row says "Not available on this setup" with a "Why?" sheet.
  - Test skipped: row says "Not tested yet".
- Most important element: the row for Navigation.

*Reconnect*
- Layout: title, TV name, three check rows, one explainer line, Try again, Show me how to fix it.
- States:
  - Checking: rows animate one at a time.
  - iPhone not on Wi-Fi: first row reads "iPhone Wi-Fi: Not connected".
  - On Wi-Fi, TV not found: third row reads "TV responding: Not yet".
  - Local network off: second row reads "Local network access: Off" with Open Settings.
  - Found again: the screen closes and the remote opens with "Reconnected."
- Most important element: the three check rows.

*TV switcher*
- Layout: rows for each saved TV with name, brand and status; Add a TV; Rename and Forget on swipe.
- States: Ready, Not reachable on this Wi-Fi ("Bedroom TV · Not on this Wi-Fi"), Asleep, Needs pairing again.
- A TV that is not reachable looks unavailable; selecting it opens the Reconnect screen instead of a remote.
- Most important element: the status word on each row.

**Edge cases and states (every one ships in v1):**

| Case | Trigger | What the app does | Copy |
|---|---|---|---|
| No TV found | Search finishes (or [UNKNOWN: timeout, set from device testing]) with no results | No-TV card with the three checks, Try again, Pick your brand, Show me how to fix it | "We couldn't find a TV on this Wi-Fi." / "Your TV may be off, asleep, or on a different network." |
| iPhone not on Wi-Fi | Network path shows no Wi-Fi (cellular only or offline) | Searching is not started; one button | "Your iPhone isn't on Wi-Fi. Connect to the same Wi-Fi as your TV, then try again." |
| Wrong Wi-Fi (iPhone on Wi-Fi, TV elsewhere) | No TV found while on Wi-Fi; app can't know the TV's network | Same as No TV found; adds a hint about two networks | "Some homes have more than one network, such as a guest network. Your iPhone and TV need to be on the same one." |
| Local network access off | The OS denies local network access | Local network off card; Open Settings; no re-prompt | "Local network access is off. Remote Ready needs it to find your TV." / "Open Settings" |
| Pairing failed (TV declined) | The TV reports a rejected or cancelled request | Pairing failed state, Try again | "Your TV didn't accept the request. Try again and choose Allow on your TV." |
| Pairing timed out | No answer from the TV within [UNKNOWN: timeout] | Pairing failed state | "We didn't hear back from your TV. Check the screen for a request and try again." |
| Wrong code | Code rejected | Field error, three tries allowed [UNKNOWN: confirm per brand], then restart | "That code didn't match. Check your TV screen and try again." |
| Found but unsupported | The TV is a brand or model we can't control | Not supported card, no remote opened, no paywall | "We found [TV name], but we can't control it yet." |
| Test answered No | User taps No on the Connection Test | Not confirmed state with Try again, Send Home first, and Show me how to fix it; the connection is not marked Connected | "Your TV may not have responded. Make sure it's on and showing a menu, then try again." |
| Test sent but command failed | The send call errors | Failure state | "We couldn't send that to your TV." |
| TV off or asleep | TV found earlier, now not reachable | Reconnect screen with Asleep hint; if Power on is supported and verified, a Power on button | "Your TV may be asleep." / "Turn on TV" (only when verified) |
| Power on unavailable | Power on not supported on this TV or setup | The button is not shown; the result card says why | "Power on: Not available on this setup." |
| Power off | User taps Power while TV is on | Sends power off with no confirmation | none |
| Connection lost mid-use | A command fails after Connected | Chip changes to Reconnecting, tries again, then the Reconnect card | "Reconnecting…" then "[TV name] isn't responding." |
| Wi-Fi changed | iPhone joins a different Wi-Fi | Saved TV shows Not reachable on this Wi-Fi | "[TV name] · Not on this Wi-Fi" |
| TV address changed | Saved TV found at a new address | App rediscovers by name, reconnects silently | "Reconnected." |
| Two TVs with the same name | Duplicate names in discovery | Show brand and the last four characters of the TV's identifier | "[Name] · [Brand] · ending [xxxx]" |
| Control unavailable | A control not supported by the connected TV | Control hidden or dimmed | Unavailable label on press and hold |
| Keyboard unsupported | TV or app doesn't accept text | Keyboard button hidden | none |
| Keyboard open, no text field | User opens keyboard when the TV has no text field | Keyboard stays but warns | "Open a search box on your TV first." |
| Plus control tapped (free) | Touchpad, Keyboard, Apps, second TV | Plus sheet opens | see Plus sheet copy |
| Plus purchased, TV doesn't support the feature | Keyboard or Apps not supported on this TV | The Plus sheet is not shown at all for that control; the control is hidden | none |
| Purchase cancelled | User closes the Apple sheet | Back to the remote; nothing lost, no message | none |
| Purchase failed | StoreKit error | Stay on the sheet | "That didn't go through. You haven't been charged." only when StoreKit reports no transaction; otherwise "Something went wrong. Check Settings › Apple Account › Purchase History before trying again." |
| Purchase pending | Ask to Buy | Sheet closes with a note | "Waiting for approval. Your basic remote still works." |
| Prices fail to load | StoreKit products unavailable | Skeleton, then Retry | "Couldn't load the price. Try again." |
| Restore with a purchase | Restore tapped | Plus unlocks | "Plus restored." |
| Restore with none | Restore tapped | Nothing changes | "No purchases to restore on this Apple Account." |
| App opened with no TV in range | Launch while away from home | Remote with dimmed controls and the Reconnect card | "[TV name] isn't on this Wi-Fi." |
| Forget a TV | Settings › My TVs › Forget | Confirm, remove pairing data on the iPhone | "Forget [TV name]? You'll need to pair it again." |

**Paywall rules:**
- Placement:
  - No paywall at launch, in the find or pairing flow, in the Connection Test, on the result card, or on any basic button.
  - The Plus sheet opens only from: tapping a Plus control (Touchpad mode, Keyboard, Apps, adding a second TV), Settings › Plus, or the "See what Plus adds" link on the result card.
  - Once the user dismisses the sheet, the control keeps a lock chip; it does not pop the sheet again except when the user taps that control again. No sheet on foreground, no timer-based sheet, no gift or offer badge on the remote.
- Type: soft. Close is visible from the first frame, at least 44 pt, AA contrast, never delayed. Closing leaves the remote as it was.
- What is free (never paywalled): find, pair and test a TV; one saved TV; the Classic remote with Navigation, OK, Back, Home, Volume, Mute, Play/Pause, Rewind, Fast forward and Power off; the Reconnect screen; the Result card; Power on from phone where verified; no ads.
- What Plus unlocks: Touchpad mode, Keyboard, Apps launcher with pinned apps, more than one saved TV, custom button size layouts beyond the Large buttons setting.
- Plans to test first (structure only; prices UNKNOWN until s5-monetization):
  - Plus annual, auto-renewing, with a 3-day free trial.
  - Plus lifetime, one-time.
  - Test A: annual plus lifetime. Test B: annual only. Test C: monthly plus annual.
  - No weekly plan in v1 launch. A weekly plan is a later experiment (see Later).
- Paywall timing test (context experiment 2): arm A (default) keeps the Classic remote free as above. Arm B puts the Plus sheet after the first Verified command and before "Open my remote", closable, with the Classic remote still working after close. Compare on D30 net proceeds per install, refunds and next-day reconnect success.
- Trial framing: the CTA reads "Try 3 days free" with the line "Free until [date]. Then [price] per year. Cancel anytime in Settings › Apple Account › Subscriptions." The end date and price are computed from StoreKit and sit directly above the CTA. The trial toggle pattern ("Enable Free Trial") is not used; the plan row the user picks is the plan they get.
- Price display: every price is StoreKit's localized price. The billed price is the largest price on its row. No per-week equivalent for an annual plan. No "Save n%", no strike-through, no "Best offer", no "Most popular".
- Restore Purchases, Terms of Use and Privacy Policy on the sheet and in Settings.
- Disclosure meets App Review Guideline 3.1.2 on the sheet: what the user gets, duration, price per period, auto-renewal and how to cancel.
- Never:
  - A downsell, "Mega Sale", "Limited Time Offer" or discount after closing.
  - A countdown, gift icon or "Exclusive Offer" badge on the remote.
  - "No Risk", "No Payment Now", "Continue for Free" next to a price that bills.
  - A trial that renews weekly without the weekly price shown next to the CTA.
  - Ratings, user counts or laurels on the sheet.
  - A rating prompt or feedback sheet before or right after payment.
  - Banner ads, in any tier.

**Plus sheet states and copy:**

| State | What the user sees |
|---|---|
| Opened from a control | Title "Remote Ready Plus", the control the user tapped highlighted in a short list of Plus features, plan rows, CTA, terms text, Restore, Terms, Privacy, Close |
| Prices loading | Skeleton rows, CTA disabled. On failure: "Couldn't load the price. Try again." with Retry |
| Plan selected | CTA reads "Try 3 days free" (annual) or "Buy lifetime" (lifetime) |
| Purchase pending | "Waiting for approval. Your basic remote still works." |
| Purchase succeeded | Sheet closes, the tapped control works, toast "Plus is on." |
| Already on Plus | Settings shows "Plus · renews on [date]" with Manage subscription |
| Plus ended | Settings shows "Plus ended [date]"; Classic remote unchanged; Plus controls lock again |
| Free line | "Your basic remote stays free." appears on every sheet |

**Visual language:**
- Competitor map: purple gradients and a glossy purple d-pad (the purple interface, the blue-button app, the Roku-style remote), a blue illustrated dark theme (the Kraftwerk app), a dark navy glass look (the blue interface app), an orange-on-black remote (iMote), and stock-photo or AI-image paywalls in most apps.
- Our territory: dark graphite by default with full light mode. Slate surfaces, one cool accent (teal-green) reserved for Connected and Verified, amber for Not confirmed, plain red only for failures and Power. No purple gradient, no gift or crown imagery.
- Low density, one primary action per screen, large buttons, generous spacing. State is carried by an icon plus a word, never colour alone.
- Real UI only. No stock people, no AI-generated TV scenes, no brand logos in the app (brand names in text).
- Motion only for real progress (searching, sending, reconnecting) and a short haptic on every button press with a Haptics setting.
- The Result card and the Connection Test question are the signature visuals for the product and the ads. Final tokens belong to brand-designer.

**Voice:**
- Tone: calm, plain, exact. Never cute.
- Lines we would ship:
  1. "Let's find your TV."
  2. "Did your TV respond?"
  3. "Power on: Not available on this setup."
  4. "Your TV may be asleep."
  5. "Your basic remote stays free."
- Lines from competitor screens we would never ship:
  1. "Device found" with "Enjoy your TV now" (tvremote by, p5), shown before a TV was connected; the same app shows "No TV Found" (p9).
  2. "3 Days Free No Risk" / "No Payment Now" (tvremote by, p6).
  3. "Mega Sale" and "Limited Time Offer" (tvremote by, p8).
  4. "Trusted by over 15M+" and "Average Rating 4.8" (tvremote by, p14).
  5. "Continue for Free" next to "3-Day Full Access ₹0.00" (iMote, p7).
  6. "The One-and-Only TV Remote Control" (tvremoteapp, p2).

**Accessibility:**
- Dynamic Type on every screen, including paywall terms (no fixed-size legal text). The Large buttons setting scales the Classic remote and keeps the cluster centered.
- VoiceOver: every remote button has a label and a hint ("Volume up, button"); the state chip reads "Living Room TV, connected"; Result rows read "Navigation, verified"; a locked control reads "Touchpad, requires Plus".
- Targets are at least 44 pt, including the Plus sheet close.
- Contrast is WCAG AA for all text including amber and grey helper text.
- Haptics on by default and optional; the Reduce Motion setting replaces the searching animation with a static line.
- State is never by colour alone: every status has an icon and a word.
- The touchpad has a button-mode alternative at all times; gestures are never the only way to act.

**Refuse list (seen in team screens):**
- Tracking prompt as the first screen: tvremoteapp p1.
- Intro slides before any value: Kraftwerk p2–p5; tvremoteapp p2–p4.
- Hard paywall straight after onboarding slides: Kraftwerk p6; tvremoteapp p5.
- Paywall before a TV has answered: tvremote by p5 ("Device found"); Kraftwerk p6; remote p4.
- Paywall repeated in the same session: Tvremote p2, p4, p5; remote p4, p6.
- "Device found" shown while no TV is connected: tvremote by p5 against p9 ("No TV Found").
- A fake-looking progress bar before any TV is chosen: tvremote by p2 ("We're connecting to your TV. Please wait a moment", 78%).
- A feedback pre-sheet ("App improvements", "Ohh, no!" / "Good") before the paywall: tvremote by p3, p4.
- Limited-time or percentage-off offer with a gift icon on the remote: tvremote by p7, p8, p10.
- Trial toggle that is off by default on one screen and on by default on another: tvremote by p5 (off), remotetv p6 and p8 (on), remotetv p9 (off).
- "Enable Free Trial" toggle: tvremote by p5; remotetv p6, p8, p9.
- Price shown per week for an annual plan: tvremote by p5 (₹190.38 per week), remotetv p6 (₹48.06/wk), remote p4 (₹38.33 per week), iMote p7 (₹76.90 Per week).
- "SAVE 77%" / "SAVE 91%" badges: Kraftwerk p6; tvremoteapp p7.
- Laurels, user counts and ratings: tvremote by p14 ("15M+", "4.8").
- Banner ads inside the app: Tvremote p1, p3, p6, p7, p8, p9 (Google Gemini ad); iMote p5, p6, p8–p14 (QR & Barcode Scan ad); remote p2, p3 (Groww ad).
- Cross-promotion inside the app: tvremote by p11 (Food & Cosmetic Scanner, Healthy) and p12 (Remote Roku Free, Authenticator App, Cleaner: CleanUp Storage, Printer App); Tvremote p7, p8, p9 (AI Chatbot, More Apps).
- Casting, mirroring, IPTV, web browser and AI chatbot as top-level features: Tvremote p7; tvremote by p11; remotetv p3.
- Locked touchpad on the basic remote: remote p3 ("Touchpad" with Unlock).
- Faint or absent close control on the paywall: Tvremote p2, p4, p5 (faint X); remote p4, p6 (faint X); iMote p7 (no close control visible).
- Unclear weekly renewal on the main row: iMote p7 ("3-Day Full Access ₹0.00" with the weekly price in small type below).
- A rating or share item in the first-level Settings list: iMote p14 ("Rate the App").
- A Twitter link and an app-icon changer in Settings: tvremote by p13.

## v1 product features

| # | Feature | What it does | Depends on | Free / Paid |
|---|---|---|---|---|
| 1 | Find my TV | Searches the local network for supported TVs and lists them by name and brand; manual brand pick if nothing is found | Local network permission, NSBonjourServices, per-brand discovery (SSDP, mDNS or brand method) [UNKNOWN: per-brand method until spikes] | Free |
| 2 | Local network pre-prompt | One screen that explains the permission, then triggers the system prompt; Local network off card on denial | Info.plist keys, a denial-detection method [UNKNOWN: feasibility] | Free |
| 3 | Pairing | Brand-specific pairing flow with live TV-side accept or code entry | Per-brand adapter; TV-side setting (Roku mobile control setting UNKNOWN until verified) | Free |
| 4 | Connection Test | Sends a harmless command (Right), asks the user to confirm, optional volume step; never tests power | Adapter command support | Free |
| 5 | Capability map ("What works on my TV") | Per-TV record of Verified, Not confirmed and Not available controls; drives which buttons show | Test results, per-brand capability data | Free |
| 6 | Classic remote | Arrows, OK, Back, Home, Volume, Mute, Play/Pause, Rewind, Fast forward, Power off; haptics; no ads | Adapter commands, capability map | Free |
| 7 | Saved TV and auto-reconnect | Remembers one TV, reconnects on foreground, rediscovers if the address changes | Local store, network-path monitor, adapter | Free (1 TV) |
| 8 | Reconnect screen | Check rows (iPhone Wi-Fi, local network, TV responding), Try again, Show me how to fix it | Network-path monitor, adapter | Free |
| 9 | Power on from phone | Turns the TV on where the TV allows it; hidden where it doesn't | Per-TV feature (Wake or equivalent) [UNKNOWN: feasibility by brand] | Free where verified |
| 10 | Touchpad mode | Large gesture surface for swipe and tap with haptics; button mode always available | Adapter touch or arrow mapping [UNKNOWN: per-brand] | Plus |
| 11 | Keyboard | Types text into the TV where the TV supports text entry | Adapter text input [UNKNOWN: per-brand] | Plus |
| 12 | Apps launcher | Lists TV apps, pin favourites, launch with one tap | Adapter app list and launch [UNKNOWN: per-brand] | Plus |
| 13 | More than one saved TV | Name and switch between TVs, with status per TV | Local store, adapters | Plus |
| 14 | Numbers mode | Number pad for channels | Adapter numeric keys | Free |
| 15 | Plus purchase | Annual with trial, lifetime; restore; manage; Family Sharing off in v1 | StoreKit 2 | Paid |
| 16 | Settings | Plus status, Restore, My TVs (rename, forget), Power on from phone, Haptics, Large buttons, Help, Privacy, Terms, Contact support | StoreKit 2, local store | Free |
| 17 | Large buttons and accessibility | Scaled remote, VoiceOver labels, Dynamic Type | SwiftUI | Free |
| 18 | Help and troubleshooting | In-app how-to fixes for no TV found, wrong Wi-Fi, pairing failed, TV asleep | none | Free |

v1 supported TV ecosystems, in spike order: Roku, Samsung, LG. Each is in v1 only if its week-1 spike shows a stable discover, pair and command path with no server. Whatever fails the spike is cut, not delayed. Fire TV, Google TV and Android TV, Vizio, Sony, TCL and Hisense are in Later. Effort overall is bounded by the adapter spikes, not by UI.

**Paid unlocks (Plus):**
- Touchpad mode.
- Keyboard.
- Apps launcher with pins.
- More than one saved TV.

**Free covers:** find, pair and test a TV, the Result card, one saved TV, the Classic remote with Power off and Power on where verified, Numbers mode, reconnect help, no ads.

**Later (v1.1 / v2) and the trigger for each:**

| Feature | Trigger to build |
|---|---|
| Fire TV adapter | Fire TV is a visible share of installs or search terms, and a spike shows a stable command path without Amazon-only dependencies [UNKNOWN: feasibility] |
| Google TV and Android TV adapter | Same as Fire TV |
| Vizio, Sony, TCL, Hisense adapters | A brand's install or search share is visible and one adapter spike passes; each brand is its own decision |
| Siri Shortcuts and App Intents ("Volume up") | Users repeat the same two or three buttons, or support asks for hands-free |
| Lock Screen and Control Center controls | Day-2 reconnect success is stable and users open the app for the same one action |
| Widget | Same as Lock Screen controls |
| Apple Watch remote | Watch requests in support or reviews |
| Voice (microphone) button | Users ask for voice search, and the adapter supports it [UNKNOWN: feasibility by brand] |
| Custom layouts and macros | Plus users ask for specific button arrangements |
| Family Sharing for Plus | Multi-user households appear in support or reviews |
| Weekly plan test | Annual and lifetime paywall view to trial is below target and exit answers cite cost, and the weekly price can be shown next to the CTA without a trial trap [UNKNOWN: target, set after first cohort] |
| Free first month of Plus | Paywall view to trial is below target and users say they want to try before paying |
| Casting photos and videos, screen mirroring | Users in support or reviews ask for it after the remote is stable; platform check needed for mirroring [UNKNOWN: feasibility] |
| Find my remote / TV sound ping | Users ask for it; no platform proof yet [UNKNOWN: feasibility] |
| Web-based compatibility page for each TV model | Brand custom product pages beat the generic page and users ask about a specific model |
| In-app tip for the TV's own settings per brand | Pairing failures cluster on one brand |

**Not building:**
- Casting, mirroring, IPTV, web browser, AI chatbot, "More Apps", Share-with-friends, app-icon changer, Twitter link.
- A brand grid as the first screen.
- Slides, a quiz or an intent picker before the first search.
- A tracking prompt or sign-in in v1.
- Accounts, passwords and email sign-in.
- Banner ads and any third-party ads, in any tier.
- A weekly plan or an "Enable Free Trial" toggle in v1.
- "Power on" for any TV where we haven't verified it works.
- Any control that the connected TV can't act on.
- Per-TV online compatibility database in v1.
- A server for relaying commands. Control is on the local network, from the phone.

**Success metrics for v1:** (targets UNKNOWN; set after the first cohort)
- Verified remote activation: installs that complete the Connection Test with a Yes, by TV ecosystem, channel and app version.
- Funnel steps: install to local network allowed, allowed to TV discovered, discovered to paired, paired to Verified. Target UNKNOWN; set after the first cohort.
- Next-day reconnect success: installs with a Verified TV that open the app on a later day and send a command without re-pairing.
- Plus: paywall view to purchase and Plus control tap to purchase, with refunds per paying user by TV ecosystem.
- D30 net proceeds per install by acquisition angle (proof, control, reconnect, brand) and channel (Apple Search Ads vs Meta).

## New recommendations

1. Make "Did your TV respond?" a user-confirmed step, not an automatic check. Test whether showing the Result card in ads and shot 2 lifts install to Verified. Kill it if Test No answers are a large share of tests for one brand and the adapter can't be fixed in the first sprint [UNKNOWN: threshold, set after first cohort].
2. Show only the controls the TV can act on, and say why when something is missing. Test by comparing "button did nothing" support contacts and Not confirmed rate before and after the capability map. Kill it if users report a missing button more than a dead one in support.
3. Keep every tier ad-free and put "No ads. No pop-ups on the basic buttons." in shot 6 and a Meta creative. Three of seven captured apps show banner ads (Tvremote, iMote, remote). Test against angle 1. Kill it if the ad-free line doesn't change install to Verified or paywall view to purchase.
4. Make a reconnect check part of every foreground, with the Reconnect card as the product's answer to "it worked yesterday". Test by tracking next-day reconnect success and "Try again" taps. Kill it if the automatic reconnect adds a visible delay on most launches.
5. Add an in-app "This doesn't work with my TV" link that goes to Apple's refund request page [UNKNOWN: confirm the exact URL and whether the link is allowed in App Review]. Test by comparing refund requests per paying user with and without. Kill it if refunds rise and support can't resolve cases first.
6. Split paywall timing as a first-week experiment: Classic remote free (arm A) vs Plus sheet after the first Verified command (arm B). Kill arm B if paid conversion net of refunds and D30 net proceeds per install don't beat arm A.
7. Use the Result card as the thing every brand custom product page shows, so that each brand page proves its own pairing step. Kill it if brand pages don't beat the generic page on install to Verified.

## Before build

**Captures still missing:**
- Any connected-TV state in any app. In all 66 captures the TV is never connected, so no first win, no working remote, no Result-style screen and no state after a successful command is seen.
- Any pairing-failed, wrong-Wi-Fi or "TV declined" state. The captures show only searching, "No TV Found", "Not connected", "TV Not Connected", "TV is not connected" and "Oops! No TV found".
- Local network denied state in any app (only iMote p2 shows the permission prompt).
- What stays free after the paywall is closed. No capture shows a working free button.
- A US storefront capture of every app. Every price is ₹ and the Apple sheet shows an India account.
- EVOLLY, BEGAMOB, RoByte, Rokie, Smartify, Remotie and the official Roku, Fire TV, SmartThings and ThinQ apps have no screenshots.
- Which ecosystem each captured app was tested against. The brand-select screen (tvremote by p1) lists Roku, Samsung, LG, TCL, Hisense, Fire TV, Vizio and Sony; the connection used in the captures is not shown.
- Publisher and store names of the captured apps. The file names stand in for app names (see Competitor reference).

**Decisions still open (next agents):**
- Per-brand protocol, pairing flow, command coverage and terms for Roku, Samsung and LG. Roku: the Roku developer page fetched for this note says commands may not be sent from third-party platforms such as mobile apps and that keypress commands need "Control by mobile apps" enabled from Roku OS 14.1. This is a fetched summary and unverified; the Roku adapter stays in v1 only if a hands-on test shows a stable path (s3-engineering). Source fetched: https://developer.roku.com/docs/developer-program/dev-tools/external-control-api.md.
- Apple local network: NSLocalNetworkUsageDescription and NSBonjourServices are required for local discovery. Source fetched: https://developer.apple.com/documentation/bundleresources/information-property-list/nslocalnetworkusagedescription. How to detect a denial is UNKNOWN.
- Power on feasibility per brand (s3-engineering, with hardware).
- Prices, plan structure test and trial length (s5-monetization).
- ATT: whether attribution needs it (s4-analytics).
- Brand name use in listings and ads, trademark rules for TV brand names, name clearance (s6-legal; questions only).
- Privacy label: local network use, no tracking, no accounts (s6-legal and s7-submission).
- A small hardware lab with representative US TVs and streaming players (Harshil and Bharat; a lab was proposed in context §14).

**Next agents to run on this note:**
- brand-designer: tokens, the Result card and the Connection Test question as signature visuals.
- ux-designer: wireframes for Find your TV, Searching, TVs found, Pairing, Connection Test, Result card, Remote, Reconnect, TV switcher and the Plus sheet.
- s1-spec: screen states and edge cases.
- s3-engineering: week-1 spikes per brand (discover, pair, command, power on, keyboard, apps) on real hardware.
- s5-monetization: plan structure, prices, trial.
- s4-analytics: the verified-activation funnel events.

## Competitor reference

Facts only, from the team's captures. "p" is the PDF page number in the app's file. All prices are ₹ (India storefront) as shown. File-to-app names follow the analysis PDF "TV_Remote_App_Analysis.pdf" (7 pages), which names each app by its source file. Screens never show a publisher name, so the link to context's publishers (for example "Kraftwerk 9") comes from the file name and the analysis PDF only. Version strings seen: tvremote by 4.9.3 (p13); Tvremote 2.1.4 (p8); iMote 2.6.4 (2270) (p14).

**Page counts:** tvremote by kraftwerk 7; tvremote by 14; Tvremote 9; tvremoteapp 7; remotetv 9; remote 6; remoteControl (iMote) 14. Total 66 across 7 apps, plus the 7-page analysis PDF.

**TV Remote by Kraftwerk (file "tvremote by kraftwerk.pdf", 7 pages)**
- Key pages: p1 "Select a device to connect:" with "Searching for devices..." and "Make sure your mobile device and TV are connected to the same Wi-Fi network."; p2 to p5 four intro slides ("Your TV Remote, Now on iPhone", "The Remote You Know", "Smart When You Need It", "Made for Your Device"), each with Skip and CONTINUE; p6 paywall "Get Access to All Features" with a Touchpad feature highlight; p7 the same searching screen.
- Paywall placement: after the intro slides and before the device search result (p5 to p6). Close X at top left (p6). Terms of Use, Privacy Policy, Restore Purchases at the foot.
- Plans as seen: ₹3,499.00/year with "3-day free trial" and a "SAVE 77%" badge (selected); ₹299.00/week with "3-day free trial". CTA "CONTINUE". "Try for free" text above the feature.
- Dark patterns: "Try for free"; intro slides before search; "SAVE 77%". No connected state captured.

**TV Remote, purple interface (file "tvremote by.pdf", 14 pages)**
- Key pages: p1 "Please select your TV brand:" (Roku, Samsung, LG, TCL, Hisense, fire tv, Vizio, Sony) with Continue; p2 "We're connecting to your TV. Please wait a moment" with "Connecting 78%"; p3 and p4 "App improvements" with "Ohh, no!" and "Good"; p5 paywall over a "Device found / Enjoy your TV now" image; p6 "3 Days Free No Risk"; p7 and p10 remote with an "Exclusive Offer" gift badge; p8 "Mega Sale"; p9 Channels tab "No TV Found / Connect your TV to continue" with "Connect TV"; p11 Cast grid (Screen Mirroring, Cast Photos, Cast Videos, Cast Youtube, Food & Cosmetic Scanner, Healthy); p12 and p13 Settings; p14 "Trusted by over 15M+" and "Average Rating 4.8" with Continue.
- Paywall placement: p5 after the "App improvements" screens and before the main remote; p6 as a second screen when the first is closed or continued; p8 "Mega Sale"; Settings "Unlock Premium" (p12); a gift badge on the remote (p7, p10).
- Plans as seen: p5 "YEARLY ACCESS ₹190.38 per week" with "Just ₹ 9,900 per year" and "BEST OFFER"; "WEEKLY ACCESS ₹ 999 per week"; "Enable Free Trial" toggle off; "BEST VALUE" under Continue; "Unlimited Remote & Channel", "High quality Screen Mirroring & Cast TV", "Ads Free experience". p6 "3-Day free Trial, then ₹ 999 per week", "Start Free Trial", "No Payment Now". p8 "Limited Time Offer" "95%" "Only ₹ 599/week. Cancel anytime." Close X on p5, p6, p8; Restore on p5.
- Dark patterns: "Device found" before a TV is connected; a progress bar before a TV is chosen; a feedback pre-sheet; "3 Days Free No Risk"; "Mega Sale" with a 95% badge; a gift "Exclusive Offer" badge on the remote; laurels "15M+", "4.8"; per-week figure under a yearly plan; cross-promotion in Cast and Settings (Food & Cosmetic Scanner, Healthy, Remote Roku Free, Authenticator App, Cleaner: CleanUp Storage, Printer App, Follow on Twitter). Settings also has "Find Remote", "Change App Icon", "Vibrate", "Click Sound".

**TV Remote, blue subscription buttons (file "Tvremote.pdf", 9 pages)**
- Key pages: p1 "Select a TV Device / Searching..." with a banner ad; p2, p4, p5 paywall "Unlock Full Access"; p3 Remote (keyboard, home, power, d-pad and touchpad toggle, Netflix, YouTube, Apple tv tiles, "VOL") with a banner ad; p6 Apps "TV Not Connected / Connect to your TV to see the list of applications here." with "Connect"; p7 Cast (Photo, Video, IPTV, Web Browser, Screen Mirroring, AI Chatbot); p8 and p9 Settings (Upgrade to Premium, Haptic Feedback, Frequently Asked Questions, Restore Purchase, Screen Mirroring, AI Chatbot, More Apps, Privacy Policy, Terms of Use, Contact Us, Tell Friends).
- Paywall placement: p2 during device search; again at p4 and p5; "Upgrade to Premium" in Settings (p8); a crown icon on Apps and Cast (p6, p7).
- Plans as seen: "3-DAY FREE TRIAL, auto-renewal. Then ₹ 699/week, cancel anytime." with "Start Free Trial"; Yearly ₹ 1,799 "Auto-renewal, cancel anytime."; Lifetime ₹ 4,999 "Onetime payment." Features: "Unlock Remote Control", "Unlock Channels Switching", "Cast All Media to TV", "100% No Ads". Close X faint at top left.
- Dark patterns: the same paywall three times; a banner ad (Google Gemini) on every screen; cross-promotion (AI Chatbot, More Apps); a faint X.

**TV Remote Control, illustrated onboarding (file "tvremoteapp.pdf", 7 pages)**
- Key pages: p1 App Tracking Transparency prompt for "TV Remote"; p2 to p4 three slides ("TURN YOUR PHONE INTO A SMART TV CONTROLLER", "MAKE TV SEARCHING A NO-BRAINER", "FULLY CUSTOMIZABLE QUICK & EASY TO USE"); p5 paywall "GET FULL ACCESS TO UNIVERSAL TV REMOTE"; p6 Apple In-App Purchase sheet "TV Remote Control / Universal Remote TV Control Subscription"; p7 "CHOOSE YOUR PLAN TO UNIVERSAL TV REMOTE".
- Paywall placement: right after the three slides, before any search (p4 to p5). A small X at top left over the TV image (p5).
- Plans as seen: "Try 3 days for free, then ₹ 999/week" "Auto-renewable. Cancel Anytime" (p5); p6 sheet: "3-day free trial Starting today", "₹ 999 per week Starting on 6 Oct 2026", "Plan automatically renews until cancelled."; p7: "First 3 days free then ₹ 999/week" (selected), "Monthly ₹ 1,999/month", "Yearly ₹ 4,999/year" with "SAVE 91%"; CTA "START MY FREE TRIAL"; "Hide Options", RESTORE, PRIVACY. The sheet in p6 shows the account's phone number; this note does not repeat it.
- Dark patterns: ATT first; slides before paywall; "The One-and-Only TV Remote Control"; "SAVE 91%".

**Universal Remote Control, blue interface (file "remotetv.pdf", 9 pages)**
- Key pages: p1 and p5 "Connect your TV / Select the device you want to connect to or activate a previously connected one" with "Refreshing..." and "I don't see the device"; p2 remote with "TV is not connected" and greyed Ch and Vol; p3 Cast tab ("Try Screen Mirroring / Watch TikTok, Instagram & YouTube on your TV", "Cast media from your gallery"); p4 Settings (Unlock Premium Features, App Icon, Help, Share the app, Terms of Use, Privacy Policy, Restore purchases); p6 and p8 "Unlock Full TV Control"; p7 "My Apps" list (Netflix, Youtube, Prime Video, HBO Max, Apple TV+, Disney+, Spotify, Youtube Music) with a pin on each; p9 "Remote Control PRO".
- Paywall placement: after exploring the remote and apps (p6, p8), and a second design (p9); "Unlock Premium Features" in Settings (p4). Exact trigger not visible. X at top right.
- Plans as seen: p6 and p8: "Enable Free Trial" toggle on; "3-day free trial then billed weekly at ₹699.00/wk" (selected); "12 Months: ₹48.06/wk billed yearly at ₹2,499.00/yr"; "No payments now!"; Continue. p9: toggle off; "Yearly: ₹48.06/week Billed yearly. Total: ₹2,499.00" (selected); "3-day free trial then ₹699.00/week". Features: "Control Power, Volume, and More", "Access All Apps and Channels", "Fast Text Input with Your Phone", "Touchpad Navigation"; callouts "Power On/Off", "Keyboard", "TouchPad".
- Dark patterns: the trial toggle default differs between p6 or p8 and p9; a per-week figure under a yearly plan; "No payments now!"; a "My Apps" list shown while the remote reads "TV is not connected" (p2, p7).

**Remote, purple directional pad (file "remote.pdf", 6 pages)**
- Key pages: p1 Remote screen (Back, Home, d-pad with OK, volume row) with tabs Remote, Apps, Settings; p2 Apps "Not connected / Please connect to your television." with Connect and a banner ad; p3 Settings (Unlock Premium, Haptic Feedback, "Touchpad" with Unlock, "Power On with Mobile", "Forget Paired Devices", Frequently Asked Questions, Restore Purchases, Share with Friends); p4 and p6 paywall "GET PRO ACCESS"; p5 "Connect to your TV" loading with X and ?.
- Paywall placement: during exploration (p4) and again after the connect screen (p6). Touchpad is shown as locked in Settings (p3).
- Plans as seen: "YEARLY ACCESS Just ₹ 1,999 per year ₹38.33 per week" with "BEST OFFER"; "3-DAY FREE TRIAL then ₹499.00 per week"; Continue; "CANCEL ANYTIME". Features: "UNLOCK REMOTE CONTROL", "HANDY TV KEYBOARD", "SWITCH APPS & CHANNELS", "FAMILY SHARING (UP TO 6)", "AD-FREE EXPERIENCE". Faint X at top left.
- Dark patterns: banner ad (Groww) on p2 and p3; a faint X; per-week figure under a yearly plan; a paywall repeated.

**iMote / Remote Control (file "remoteControl.pdf", 14 pages)**
- Key pages: p1 iMote splash; p2 local network prompt: Allow "Remote Control" to find devices on local networks, with the app's own line "iMote needs access to your Wi-Fi network to discover and sync with your TV." and a map; p3 "Step 1 Make sure your TV is on"; p4 "Step 2 Confirm the pairing" ("Press "OK" on the pop-up that appears on your TV, or enter the numeric code shown on your TV screen."), button "Go to search!"; p5 "Connect to your TV / Check that your phone and TV share the same Wi-Fi network." with "Searching for your TV..." and "Troubles finding your TV?"; p6 remote (d-pad mode) with an orange "Connect to your TV" banner and a banner ad (QR & Barcode Scan); p7 paywall "Simplify your TV time"; p8 touchpad mode ("Swipe to explore, tap to select."); p9 number pad; p10 Apps "Oops! No TV found / Connect to your TV to start browsing apps"; p11 Cast (Photos, Videos); p12 to p14 Settings.
- Paywall placement: after the pairing steps, search and the first remote screen (p6 to p7); a crown icon on the Remote, Apps and Cast headers; "GO PRO" in Settings (p12). The exact trigger is not shown.
- Plans as seen: "3-Day Full Access ₹0.00" "MOST POPULAR" (selected); "Yearly Access ₹76.90 Per week"; "₹999.00/week, auto-renewable. Cancel anytime."; "Free Trial Enabled" toggle on; CTA "Continue for Free"; "Secured by Apple". Features: "Enjoy limitless use", "Easy app access", "Phone casting", "Compatibility with all major TV brands". "Restore purchase" at top left. The yearly total is not stated.
- Dark patterns: "Continue for Free" and "₹0.00" next to a weekly renewal in small type; no close control visible on the paywall (p7); a banner ad on p5, p6 and p8 to p14; "Compatibility with all major TV brands". The remote shows an orange "Connect to your TV" overlay that persists above the controls (p6, p8, p9).
- Settings items seen (p12 to p14): Go PRO, Restore Purchase, Haptic Feedback, Touch Feedback, Change Remote Skin, My Devices, FAQs, Contact Us, Rate the App, Share the App, Terms of Use, Privacy Policy.

**Analysis PDF (7 pages)**
- Covers seven apps in this order: TV Remote by Kraftwerk (source tvremote by kraftwerk.pdf), TV Remote - purple interface (tvremote by.pdf), TV Remote - blue subscription buttons (Tvremote.pdf), TV Remote Control - illustrated onboarding (tvremoteapp.pdf), Universal Remote Control - blue interface (remotetv.pdf), Remote - purple directional pad (remote.pdf), iMote / Remote Control (remoteControl.pdf). Review date 3 October 2026. Each has onboarding, paywall timing, offer and what is free. Prices are INR and match the screens above. The analysis states that no screenshot shows a connected TV, and that the free control allowance cannot be established in any of the seven apps.

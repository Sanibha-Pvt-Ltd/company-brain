---
type: category-product-strategy
category: fax
member: harshil
updated: 2026-10-06
status: draft
sources: [context.md, screenshots:121 across 8 apps (+ 1 analysis PDF, 5 pages), knowledge:organic-growth-knowledge-base.md;consumer_app_venture_knowledge_base_2026-10-04.md;sanibha-app-factory-knowledge-base.md (grep only, no benchmarks used), web:1]
---

# Fax — final recommendations (v1)

Built from [[research/categories/fax/context]] and the team's in-app captures of Municorn, iFax, Fax.Plus, Tiny Fax, Genius Fax, Faxer, FaxFree and mFax. Every capture is from an India storefront (₹ prices, +91 default). Nothing here converts ₹ to US prices. All our prices are UNKNOWN until s5-monetization sets them.

## Positioning

**Line:** For anyone who has to send paperwork by fax once in a while. Scan it, see the exact price for this fax before you pay, send it, and get a delivery report. No weekly plan, no account.

**Positioning statement:** For people who just got told "fax it to us" (insurer, doctor's office, DMV, landlord, HR), OneFax is the fax app that shows you the price of this fax before you pay and tells you plainly what happened after you send it. Unlike Municorn, iFax, Tiny Fax, Faxer, FaxFree and mFax, there is no weekly plan and no sign-up wall. Unlike Genius Fax, there is no account and no credit balance to work out first.

| Layer | Call |
|---|---|
| Acquisition hook | "Need to send one fax? Pay for one." |
| Product differentiator | The exact price of this fax on the review screen before payment, a faithful black-and-white preview, status in plain words, and a failed fax that is never charged. |
| Emotional benefit | Knowing what it will cost, what they will see, and what happened. |
| Retention reason | The next fax takes the same few taps. History and delivery reports stay on the phone. A monthly plan exists for people who fax often. |

**Who it's for:**
- Primary: a US adult with a one-off or occasional task (medical or insurance form, DMV or government paperwork, signed lease pages, HR or school form) and a fax number from the other side.
- Trigger moment: an office says "send it by fax", and they have a phone and no machine.
- Searches: "fax from iPhone", "send fax", "free fax", "fax app".
- Fears: a weekly subscription they forget to cancel, paying and the fax not going through, not knowing if it arrived, their documents sitting on a stranger's server.
- Secondary: small-office and part-time users who fax weekly. They use the monthly plan.

**Job to be done:** "I need to get these pages to that number, now, and know it went through."

**Name placeholder:** OneFax. Name territory: one, once, send, clear. Treat it as a placeholder until the name is cleared.

**Proof points that must be visible in the product:**
- The review screen shows page count, recipient number and the exact price in the same view as the Pay and send button.
- A black-and-white preview of every page, zoomable, is shown before payment. It is the page as the recipient's machine will print it.
- The status screen uses plain steps and a final line that says what "Delivered" does and does not mean.
- A downloadable delivery report (PDF) is attached to every delivered or failed fax.
- A failed fax shows the reason and three actions, and says the pass is back.
- Cold launch to review screen needs no account, no sign-in, no tracking prompt and no onboarding.

**App Store screenshots 1–3 (one story: price → preview → outcome):**

| # | Headline | Shows |
|---|---|---|
| 1 | "Need to send one fax? Pay for one." | The review screen: 3 pages, recipient, one price, Pay and send |
| 2 | "Scan it. See what they'll get." | The scan, then the black-and-white preview with a zoomed page |
| 3 | "Know exactly what happened." | The status screen at Delivered, the report button, the one-line note on what Delivered means |

Screens 4–6: "If it fails, you're not charged" (failure recovery), "No account. No weekly plan." (Settings and Paywall), "Your fax history, on your phone." In the first storefront test, run this order against an order with shot 3 first.

**Ad angles:**
1. **Price first (lead):** screen recording. Open the app, scan a form, type a number, see one price, pay, see Delivered. End card: "One fax. One price."
2. **Outcome:** a form is scanned and sent, then the status screen and the delivery report. End card: "Know exactly what happened."
3. **Control:** "Send a fax from your iPhone." Scan, number, send.
4. **Use case (test after 1–3 have a baseline):** "Insurance form? Doctor's office? Send it in minutes." Same screens as angle 2.

Each angle gets its own Custom Product Page whose screenshots match the ad. The deep link opens the Home screen with the Scan sheet ready.

| Angle | Custom Product Page headline (shot 1) | First action in app | Paywall moment it leads to |
|---|---|---|---|
| 1 Price first | "Need to send one fax? Pay for one." | Scan | Pay and send |
| 2 Outcome | "Know exactly what happened." | Scan | Pay and send |
| 3 Control | "Send a fax from your iPhone." | Scan | Pay and send |
| 4 Use case | "Send your insurance or medical form." | Scan | Pay and send |

Channel call: Apple Search Ads and organic search are the first channel. Meta use-case creatives run second, on the same screens.

**Messaging table (placeholder copy for the ASO agent; store limits apply):**

| Surface | Line |
|---|---|
| App name (placeholder) | "OneFax: Send Fax from iPhone" |
| Subtitle (placeholder) | "Pay per fax. No weekly plan." |
| Promotional text | "Scan a document, see the exact price before you pay, and get a delivery report. No account." |
| First line of description | "Send a fax from your iPhone and see the price before you pay." |
| Ad end card | "One fax. One price." |
| Icon direction | A single page with a check mark on a navy field. No fax-machine, no phone handset, no crown. |

**We will never claim:**
- "HIPAA compliant", "secure", "encrypted", "private", "your files never leave your phone" or any compliance or security claim beyond what the build and legal review support. A fax leaves the phone by definition.
- "Guaranteed delivery", "never fails", "instant".
- That a fax was "received", "read", "accepted", "filed" or "processed" by the organization. We say "Delivered to the recipient's fax line".
- That the report is legal proof, or that it meets a filing deadline.
- That we verified who owns a number. We only check its format.
- "Free fax" or "free" next to anything that costs money. Preparing a fax is free. Sending is paid.
- "Unlimited" anything. The monthly plan has a stated page allowance.
- "#1", "Top fax app", "App of the Day", "Editors' Choice", user counts, rating counts, press logos, company logos (Lyft, 3M) or any "trusted by" line.
- "Cheaper than FedEx or the copy store" unless a sourced price comparison exists.
- "Works with [named insurer, agency, DMV or hospital]".
- "Send to 90+ countries" or "international". v1 sends to US and Canada numbers only.
- "Receive faxes" or "your own fax number". Not in v1.
- "No subscription" without "monthly plan optional" nearby.

## UI/UX

**Design principles (tie-breakers):**
1. Value before asks. The first ask is the camera, when the user taps Scan. No consent wall, tracking prompt, sign-in, notification ask or rating ask before a fax is paid for.
2. Say the price for this fax before any payment step. The price is on the same screen as the button that charges it.
3. Show what the recipient will see. Faxes are black and white. We show that, with a zoom, before the user pays.
4. Say what we know and what we don't. Delivered means the recipient's fax line accepted the pages. A number check is a format check. Never imply either is more.
5. A failed fax has a next step, not just a red error. Every failure shows the reason, the action, and what happened to the pass.
6. One job per screen. Send is the home screen. History and Settings are the only other places.
7. Documents are sensitive. No third-party ads, no cross-promotion, no stock photos of people, and plain words about where files go.

**Structure (3 tabs):**
- **Send (home):** recipient field with a country chip fixed to +1 and a Paste button, then a Pages card (Scan, Photos, Files), then a Review button.
- **History:** every fax with status (Draft, Sending, Delivered, Not delivered), recipient, pages and date. Search by number or name. Tapping a row opens the Status screen.
- **Settings:** Plan, Manage subscription, Restore purchases, Sender details for the cover page, Lock with Face ID, Where your files are, Delete my data, Support, Privacy, Terms, Version.
- No Inbox, Contacts, Folders, Templates, Account or Tools tab.

**First five minutes:**

| # | Screen | Purpose | What's on it | Primary action | Copy direction | Asks | Given so far |
|---|---|---|---|---|---|---|---|
| 1 | Send (cold launch) | Start the job at once | Number field (+1), Paste button, Pages card with Scan / Photos / Files, disabled Review button, History and Settings tabs | Scan | "Who are you faxing, and what?" | nothing | the app |
| 2 | Camera pre-prompt (inline card, first Scan tap only) | Explain the camera ask | One line and a Continue button that triggers the system prompt | Continue | "The camera is only used to scan your pages." | camera | nothing yet |
| 3 | Document camera (VisionKit) | Capture | Auto edge detection, auto-capture, page counter, Add page, Save | Save | system UI | nothing | live capture |
| 4 | Send, pages filled | Confirm what's attached | Page thumbnails (reorder, delete, rotate), number field, Cover page toggle, Review button turns active once number and one page exist | Review | "3 pages ready." | a number | the pages |
| 5 | **Review: first win** | Show exactly what will happen | Black-and-white preview strip (tap to zoom), recipient with format check, cover page toggle, page count, the exact price, Pay and send, "Sending often? See the monthly plan." | Pay and send | "One fax. One price. [price]." | payment | **the preview and the price, before paying** |
| 6 | Apple payment sheet | Pay | System sheet | Confirm | system | payment | nothing more |
| 7 | Status | Show progress, then the outcome | Steps, recipient, page count, Delivered or Not delivered banner, Download report, Done | Done | "Delivered to (212) 555-0100." | notifications (see Permissions) | the delivery report |

- First win is screen 5. Cold launch to a fax that is fully prepared and priced takes 3 taps plus typing a number plus the system camera permission: Scan, Save, Review. There is no tap for onboarding, consent or sign-in.
- There is no onboarding carousel, sign-in screen, consent wall or launch paywall.
- Photos and Files routes skip the camera permission and reach the same Review screen in the same count.

**Copy deck by screen (exact lines; [brackets] are filled live; nothing in brackets is hard-coded):**

| Screen | Element | Copy |
|---|---|---|
| Send | Number field placeholder | "Fax number" |
| Send | Paste button | "Paste number" |
| Send | Pages card, empty | "Add pages to fax" with "Scan", "Photos", "Files" |
| Send | Country note (tap +1) | "OneFax sends to US and Canada fax numbers." |
| Send | Review button disabled | "Review" |
| Send | Non +1 number typed | "OneFax sends to US and Canada numbers for now." |
| Camera pre-prompt | Body / button | "The camera is only used to scan your pages." / "Continue" |
| Camera denied | Card | "Camera is off. Open Settings, or add pages from Photos or Files." Buttons "Open Settings", "Photos", "Files" |
| Camera restricted | Card | "The camera is restricted on this iPhone. Add pages from Photos or Files." |
| Pages | Count line | "[N] pages ready." |
| Pages | Page limit reached | "That's the most pages OneFax can send in one fax: [L]. Send the rest as a second fax." |
| Number check | Valid format | "Looks like a US number. We can't tell who it belongs to." |
| Number check | Invalid | "That doesn't look like a complete US or Canada number." |
| Cover page | Toggle / note | "Cover page" / "Free. Shows who it's from and who it's for." |
| Preview | Caption | "This is how the page will print on their machine. Zoom in to check the text." |
| Preview | Hard-to-read page | "Page [n] is very dark. The text may not be readable. Retake it or brighten it." Buttons "Retake", "Brighten", "Keep as is" |
| Review | Price line | "[N] pages · [price]" |
| Review | Button | "Pay [price] and send" |
| Review | Under button | "You pay once for this fax. If it can't be delivered, your pass stays in your balance." |
| Review | Monthly link | "Sending often? See the monthly plan." |
| Status | Step 1 | "Getting your fax ready" |
| Status | Step 2 | "Sending to [number]" |
| Status | Step 3 (only if the provider reports it) | "Page [n] of [N] sent" |
| Status | Retrying | "[Number] was busy. Trying again in a few minutes (try [k] of [K])." |
| Status | Delivered | "Delivered to [number]." |
| Status | Delivered note | "Delivered means their fax line accepted every page. It doesn't tell us whether anyone has read it." |
| Status | Report button | "Download delivery report" |
| Failure | Headline | "Your fax couldn't be delivered." |
| Failure | Reason line | "Reason: [reason from the provider, in plain words]." |
| Failure | Buttons | "Try the same number again", "Check or change the number", "Get help" |
| Failure | Pass line | "You weren't charged for this fax. Your pass is back in your balance." |
| Notification pre-prompt | Body / buttons | "Want a ping when this fax is delivered or fails? We only send notifications about your faxes." "Allow notifications" / "Not now" |
| Settings | Where your files are | "Your fax history is stored on this iPhone. Pages are sent to our fax provider to deliver them and deleted after [UNKNOWN: retention period]." |
| Settings | Delete my data | "Delete my data" |

**Permissions:**
- Camera: asked on the first Scan tap after the inline pre-prompt. If denied, every later Scan tap shows the denied card; the app never re-triggers the system prompt. Photos (system picker) and Files (system document picker) need no permission.
- Notifications: asked once, on the Status screen of the user's first paid fax, after the pre-prompt. If the user says Not now or denies, the Status screen and History carry the result; nothing nags.
- App Tracking Transparency: not shown in v1. Attribution that needs it is a decision in Before build.
- Rating: system review request only, after the second Delivered fax. Never before payment, never after a failure. No custom "Enjoying?" sheet.
- Face ID: an optional setting. No prompt until the user turns it on.

**Core loop and repeat use:**
- Day 2 and later: open the app, History shows past faxes, tap a row to resend to the same number or Send for a new one. A returning user's recent numbers appear as chips under the number field.
- Week 2: repeat senders see "Sending often? See the monthly plan." after their second paid fax in 30 days. The monthly plan is also in Settings.
- What brings users back: the next fax. There are no streaks, reminders or guilt or fear copy. The only notifications are about their own faxes.

**Key screens:**

*Send*
```
Send a fax
To  [+1] [ (212) 555-0100 ]   [Paste number]
Pages
 [Scan] [Photos] [Files]
 [thumb][thumb][thumb]   3 pages ready.
Cover page  (o)   Free.
[ Review ]
```
- States:
  - Empty: Review disabled, helper line "Add pages and a number to review."
  - Draft restored: "Continue your draft to [number]?" with Continue and Discard.
  - Camera denied: replaced by the denied card; Photos and Files stay live.
  - Offline: "You're offline. You can prepare the fax. We'll need a connection to send it." Review and Pay stay enabled; Pay and send is disabled while offline.
  - Number invalid: inline error under the field after the user leaves it, not while typing.
- Most important element: the Pages card.

*Review*
- Layout: preview strip first, then recipient line with the format check, then the cover page toggle, then the price line, then Pay and send, then the monthly link, then the one-line terms.
- States:
  - Loading preview: "Preparing preview…" with per-page progress.
  - Preview ready: pages tap to zoom; unreadable-page flags show on the thumbnail.
  - Price unavailable: "Couldn't load the price. Try again." with Retry. A price is never shown unless it came from StoreKit.
  - Over the page limit: Pay disabled, inline "Remove pages or send the rest as a second fax."
  - Purchase pending (Ask to Buy): "Waiting for approval. We'll send the fax once it's approved."
- Most important element: the price next to the preview.

*Status*
- Layout: recipient and page count at the top, one step list, one result banner, the report button, Done.
- States:
  - Preparing, Sending, Retrying, Delivered, Not delivered, Partly delivered, Provider unavailable.
  - Partly delivered: "[x] of [N] pages went through." Actions: "Send the missing pages" only if the provider supports it [UNKNOWN: provider feasibility]; otherwise "Send the whole fax again" and the pass note.
  - Provider unavailable: "We couldn't reach our fax service. Your pass is safe. Try again in a few minutes."
  - Closed mid-send: the fax keeps sending on the server. On next open the row in History shows the current status.
- Most important element: the result banner and its one-line note.

*History*
- Row: thumbnail, recipient, "[N] pages · [date]", status chip.
- Empty: "No faxes yet. Send one from the Send tab."
- Search empty: "No faxes match that."
- Swipe: Delete (with Undo toast for 5 seconds) and Resend.

*Paywall (Review is the paywall; the monthly sheet is secondary)*
- Monthly sheet layout:
  - Close (X) visible from the first frame.
  - Plan name and page allowance per month.
  - One price row, billed monthly, in the largest type.
  - CTA.
  - Full terms text under the CTA.
  - Restore, Terms and Privacy links.
- Most important element: the page allowance and the price per month, stated in the same type size.

**Edge cases and states (every one ships in v1):**

| Case | Trigger | What the app does | Copy |
|---|---|---|---|
| Number is busy | Provider reports busy | Automatic retries up to [K] over [T] (both [UNKNOWN: provider spec]); shows each retry; if all fail, Failure screen | "[Number] was busy. Trying again in a few minutes (try [k] of [K])." |
| No answer | Provider reports no answer | Same as busy | "Nobody answered at [number]. Trying again in a few minutes." |
| Not a fax line | A voice answered or no fax tone | Failure screen, no retry beyond the same rules | "[Number] doesn't look like a fax line. Check the number with the recipient." |
| Number disconnected | Provider reports invalid | Failure screen, Change number focused | "[Number] isn't in service." |
| Partly delivered | Some pages accepted | Partly delivered state | "[x] of [N] pages went through." |
| Duplicate send | User taps Pay twice, or resends the same fax within minutes | One purchase, one send; a resend within [UNKNOWN: window] asks first | "You sent this fax a moment ago. Send it again?" |
| Paid, upload failed | Network drops after payment | The paid fax is held; the app retries the upload; the Status screen shows "Waiting for a connection"; never charge twice | "You've paid. We'll send as soon as you're back online." |
| App closed after paying | Swipe-away or memory pressure | On next open the fax resumes from History | "Resuming your fax to [number]." |
| Purchase cancelled | User closes the Apple sheet | Back to Review, nothing lost, no message | none |
| Purchase failed | StoreKit error | Stay on Review | "That didn't go through. You haven't been charged." only when StoreKit reports no transaction; otherwise "Something went wrong. Check Settings › Apple Account › Purchase History before trying again." |
| Restore with a purchase | Restore tapped | Plan unlocks | "Plan restored." |
| Restore with none | Restore tapped | Nothing changes | "No purchases to restore on this Apple Account." |
| Huge file or many pages | Import of a long PDF | Page-by-page progress with Cancel; the original is never changed | "Preparing page [n] of [N]…" |
| Pages too dark or too light | Pre-send check on the black-and-white result | Amber badge on the thumbnail; export is never blocked | "Page [n] is very dark. The text may not be readable." |
| Password-protected PDF | Import of a locked PDF | Password field; the app never removes a password | "This PDF is locked. Enter its password to open it." / "That password didn't work." |
| Unsupported file | Word, Excel, ZIP | Not importable in v1 | "OneFax sends PDFs and photos. Convert this file to PDF first." |
| Not enough storage | Write fails | Stop and keep drafts | "Not enough space on this iPhone. Free up space and try again." |
| Camera denied or restricted | See Permissions | Denied or restricted card, Photos and Files stay live | See copy deck |
| Non US or Canada number | Country code not +1 | Review disabled | "OneFax sends to US and Canada numbers for now." |
| Notification denied | User denied | Nothing re-asked | none |
| Face ID not set up | Toggle on without biometrics | Toggle stays off | "Set up Face ID or a passcode in iPhone Settings first." |
| Delete my data | Tapped in Settings | Confirm, then delete history and drafts from the phone and request deletion at the provider | "This deletes your fax history from this iPhone and asks our fax provider to delete your pages. It can't be undone." |

**Paywall rules:**
- Placement:
  - No paywall at launch, in onboarding, before scanning, or before the Review screen.
  - Payment happens on the Review screen when the user taps Pay and send, after the preview and price are visible.
  - The monthly sheet opens only from the Review link, from Settings › Plan, or from the Status screen after a second paid fax in 30 days.
- Type: soft. The user can always back out of Review or the monthly sheet. Close is visible from the first frame and never delayed. Closing leaves the draft intact.
- Plans to test first (structure only; prices UNKNOWN until s5-monetization):
  - Per-fax pass in page bands (consumable). Band edges UNKNOWN, set from the cost per delivered page.
  - Monthly plan with a stated page allowance per month (allowance UNKNOWN). Never labeled unlimited.
  - No weekly plan, no annual plan, no free trial in v1.
- Pay-once vs monthly-first test (context experiment 2): arm A shows the per-fax price as the primary action with the monthly link; arm B shows the monthly plan row first with the per-fax row below it. Both rows are the same size and neither is preselected without the user seeing both prices.
- Price display: every price is StoreKit's localized price. The price charged is the largest price on its row. No per-week equivalent for monthly. No "Save N%", no strike-through, no "Best value".
- Cancel clarity: under the monthly CTA, "Cancel anytime in Settings › Apple Account › Subscriptions." Settings › Plan shows plan, renews on [date], and a Manage subscription button that opens the system sheet.
- Restore is on the monthly sheet and in Settings.
- Disclosure meets App Review Guideline 3.1.2: what the user gets, duration, price per period, auto-renewal and how to cancel, in the same sheet as the CTA.
- Failed fax: the pass returns to the user's balance and is used first on the next send. A failed fax is never billed again.
- Never:
  - A downsell, "special offer" or discount after closing.
  - A paid intro that renews weekly.
  - "Start 7-Day Access" style labels on a paid week.
  - A selectable "Try it for free" row.
  - "$" or "free" symbols next to prices that bill.
  - Countdown timers.
  - Ratings, user counts or logos.
  - A rating prompt or custom "Enjoying?" sheet before payment.
- Free users keep: preparing the fax (scan, import, reorder, cover page), the black-and-white preview with warnings, the exact price, drafts, and History. A free user cannot send. Sending is the only paid action.

**Monthly sheet states and copy:**

| State | What the user sees |
|---|---|
| Prices loading | Skeleton row, CTA disabled. After a failure: "Couldn't load the price. Try again." with Retry. |
| Purchase pending | "Waiting for approval. You can keep preparing faxes. We'll unlock the plan when it's approved." |
| Purchase succeeded | Sheet closes, the Review screen shows "Plan is on. This fax uses [n] of your [A] pages this month." |
| Allowance used | "You've used your [A] pages this month. Pay per fax, or wait until [date]." |
| Plan ended | Settings shows "Plan ended [date]". History and drafts are unchanged. |
| Already on plan | Pay and send shows "Send · uses [n] of [A] pages" and never a price. |

**Visual language:**
- Competitor map: the dominant mix is dark near-black UI with blue (Municorn, mFax, Faxer, Fax.Plus dark), stock-photo paywalls (FaxFree, Tiny Fax), laurels and logo strips (iFax, Tiny Fax, Faxer), and orange or purple accent sets (Genius Fax, iFax).
- Our territory: light by default with full dark mode. Navy and cloud (light grey) as the base, teal for primary actions, one success colour for Delivered, amber for warnings, and a plain red only for Not delivered.
- Low density, one primary action per screen, large type for numbers and price.
- Real UI and real page thumbnails. No people, no globes, no laurels.
- Motion only for real progress (preparing, sending). No fake "preparing your workspace".
- The Review screen (preview beside the price) and the Delivered banner are the signature visuals for the product and the ads. Final tokens belong to brand-designer.

**Voice:**
- Tone: calm, exact, plain. Never cute.
- Lines we would ship:
  1. "One fax. One price."
  2. "This is how the page will print on their machine."
  3. "Delivered means their fax line accepted every page. It doesn't tell us whether anyone has read it."
  4. "You weren't charged for this fax. Your pass is back in your balance."
  5. "Looks like a US number. We can't tell who it belongs to."
- Lines from competitor screens we would never ship:
  1. "Try for $0.00" / "Pay nothing for now!" (iFax, p1 and p4)
  2. "Special offer — Try for a full week just for ₹99.00" and "Start 7-Day Access" (Faxer, p8)
  3. "Not sure yet? Try it for free!" (FaxFree, p13 and p16)
  4. "Your data will be used to measure ad attribution for marketing purposes." (Faxer, p1)
  5. "Your sent and received files will remain private and will not be uploaded." (Tiny Fax, p4)

**Accessibility:**
- Dynamic Type on every screen, including the Review price line and all paywall terms (no fixed-size legal text).
- VoiceOver: page thumbnails read "Page 2 of 3, very dark, may be hard to read"; the status banner reads "Delivered to 2 1 2 5 5 5 0 1 0 0"; the price reads "Four dollars and ninety-nine cents" style full currency in the user's locale.
- State never by colour alone: every status chip has an icon and a word.
- Contrast is WCAG AA for all text, including the amber warning and grey helper text.
- Reduce Motion replaces progress animation with a static step list.
- The VisionKit camera keeps its system accessibility. Photos and Files are always offered beside Scan.

**Refuse list (seen in team screens):**
- Full-screen hard paywall on cold launch: iFax p1.
- Consent wall before any value: Municorn p1.
- ATT prompt before the user has a fax: Municorn p2, Faxer p1, FaxFree p2, iFax p6.
- Sign-up or sign-in wall: Tiny Fax p1, p4, p5; Genius Fax p6; FaxFree p15 (Sign in with Apple needed for the inbox).
- Weekly plans: Municorn p7, iFax p10, Tiny Fax p2, Faxer p7, FaxFree p7, mFax p4.
- Preselected weekly plan: Municorn p7 (1 week), Tiny Fax p2 (Weekly "Popular"), Faxer p7 (1 week full access).
- "SAVE 89%" and "SAVE 92%" badges on the same app with different numbers: FaxFree p7 and p13.
- Selectable "Not sure yet? Try it for free!" row: FaxFree p13, p16.
- Downsell after closing the paywall: Faxer p8, p9.
- "Try for $0.00" in a ₹ storefront: iFax p1, p4.
- Laurels, user counts and logo strips: iFax p1 (Lyft, 3M, "TOP FAX APP"), Municorn p7, Tiny Fax p1 and p2, Faxer p8, FaxFree p4, Fax.Plus p10.
- Custom review pre-sheet right before payment: Faxer p6.
- Third-party banner ads on every tab: Faxer p2, p3, p6, p12.
- Cross-promotion inside Settings or the editor: iFax p14, Tiny Fax p13, Tiny Fax p15, Genius Fax p16.
- A paywall that forces a number choice before the user can pay to send: Fax.Plus p3, p5.
- "Unlimited" labels: Municorn p7, iFax p1, FaxFree p7, Faxer p7, mFax p4 ("No fax limits").
- Faint or missing close button on the paywall: FaxFree p7 and p13 (X low contrast), Municorn p7 (no close, only Restore), mFax p4 and p9 (no close visible).
- "$ Only ₹76.90 per week" under a yearly plan: FaxFree p7.

## v1 product features

| # | Feature | What it does | Depends on | Free / Paid |
|---|---|---|---|---|
| 1 | Send screen | Number field fixed to +1, Paste button (SwiftUI PasteButton, no paste prompt), recent-number chips, Pages card | none | Free |
| 2 | Scan | VisionKit document camera with auto edge detection, auto-capture, multi-page | Camera permission | Free |
| 3 | Photos and Files import | System photo picker and document picker; PDFs, JPG, PNG, HEIC; share-sheet "Open in OneFax" | none | Free |
| 4 | Page tools | Reorder, rotate, delete, retake, crop | VisionKit, PDFKit | Free |
| 5 | Fax preview | On-device conversion to a fax-ready black-and-white image per page; pinch zoom; dark and light page warnings with Retake, Brighten, Keep as is | Core Image or Accelerate; week-1 spike on real forms | Free |
| 6 | Number check | Format check for US and Canada numbers; says it is a format check only | none | Free |
| 7 | Cover page | One simple cover page (to, from, subject, note) built from sender details; free to the user | Sender details (feature 14) | Free |
| 8 | Price on Review | Exact StoreKit price for this fax, shown with the preview | StoreKit 2 products and page-band mapping | Free to see |
| 9 | Pay and send | Consumable per-fax pass in page bands; the fax is submitted after the transaction is verified | StoreKit 2, backend, fax provider | Paid |
| 10 | Monthly plan | Auto-renewing subscription with a stated page allowance; sheet reached from the Review link, Settings, or after a second paid fax | StoreKit 2, backend ledger of pages used | Paid |
| 11 | Status screen | Steps from provider events only (Preparing, Sending, Retrying, Delivered, Not delivered, Partly delivered); one-line note on what Delivered means | Backend with provider webhooks | Free (included with a sent fax) |
| 12 | Failure recovery | Reason in plain words, retry same number, check or change number, get help; pass returned to the balance | Backend ledger, provider error codes mapped to copy | Free |
| 13 | Delivery report | PDF with date and time, recipient number, page count, result and the provider's reference; shareable; says what it does not prove | Backend, PDF generation | Free (with a sent fax) |
| 14 | Settings | Sender details, Plan, Manage subscription, Restore, Lock with Face ID, Where your files are, Delete my data, Support, Privacy, Terms | LocalAuthentication, StoreKit 2 | Free |
| 15 | History | On-device list of faxes with status, search, resend, swipe to delete; status refreshed from the backend | Local store (SwiftData or Core Data), backend | Free |
| 16 | Notifications | One ask after the first paid fax; pushes only about the user's own faxes | APNs, backend | Free |
| 17 | Draft autosave | Drafts persist across app launches until sent or discarded | Local store | Free |

Effort overall is bounded by two unknowns: the fax provider's API and error codes, and the preview quality on real pages. Both are week-1 spikes.

**Paid unlocks:**
- Sending a fax (a per-fax pass for this fax, or a page from the monthly allowance).
- Nothing else is paid. Preview, number check, cover page and History are free.

**Free covers:** everything up to the moment of sending, plus the status and delivery report of any fax the user has paid for. A free user can scan a form, see the black-and-white preview, see the exact price and save a draft.

**Later (v1.1 / v2) and the trigger for each:**

| Feature | Trigger to build |
|---|---|
| Fax packs (a bundle of passes at a lower per-fax price) | Users buy a second per-fax pass within 14 days at a rate worth acting on [UNKNOWN: set after first cohort] |
| Receiving faxes / own fax number | More than a small share of paywall-exit answers or support tickets ask to receive faxes [UNKNOWN: set after first cohort], and the number-compliance question is answered (Before build) |
| International destinations | Support tickets or search terms asking for non-US/Canada numbers; the provider's international price is known |
| Free first fax or first page | Paywall view → purchase is below target and exit answers say "want to try it first"; abuse controls (see Before build) are designed |
| Live Activity for sending status (Lock Screen and Dynamic Island) | Notification opt-in after the first paid fax is low, or users open History repeatedly to check status |
| Send missing pages only after a partial delivery | Partly delivered is a visible share of sends and the provider supports it |
| Saved recipients with a label ("Dr. Patel's office") | Users send to the same number twice within 14 days |
| Sign in with Apple to restore history and pass balance across phones | Support tickets about lost history or a lost pass balance |
| E-signature before send | Users export pages to sign elsewhere and return |
| Cloud-drive import (Drive, Dropbox, Box) | Support or review asks; the Files picker already reaches these on most phones |
| Annual plan | Monthly plan retention shows a repeat-sender segment |
| Free trial on the monthly plan | Plan view → purchase is below target and exit answers cite price risk |
| Medical or insurance workflow, BAA | A business buyer asks for it and legal review is done; not a v1 claim |

**Not building:**
- Receiving faxes and fax numbers in v1.
- Weekly plans, annual plan and free trials in v1.
- Accounts, passwords and email sign-in.
- International destinations in v1.
- Intent picker ("What are you sending: Medical, Insurance, Government, Other") as a home screen gate.
- HIPAA, BAA and "medical fax" positioning.
- Cloud-drive connectors, Mail import and "From URL".
- Nine cover page templates, company logo upload.
- Folders and contacts sync.
- OCR, AI summary, AI chat.
- Third-party ads and cross-promotion.
- A "Free Fax Week" or any time-limited offer.
- App Clip.

**Success metrics for v1:**
- Reached Review per new install (Scan or import → Review). Target UNKNOWN; set after the first cohort.
- Review → paid fax (the paywall conversion). Target UNKNOWN; set after the first cohort.
- Delivered faxes per paid transaction, with failure share by reason. Target UNKNOWN; set after the first cohort.
- Failed fax → retry success, and support and refund requests per paying user. Target UNKNOWN; set after the first cohort.
- D30 net proceeds per install, by acquisition angle (price first, outcome, control, use case) and channel (Apple Search Ads vs Meta). Target UNKNOWN; set after the first cohort.

## New recommendations

1. Make the black-and-white preview a product feature, not a hidden step. Faxer p5 says "We always use black and white to guarantee reception with any fax machine", and the thresholded pages in Tiny Fax p15, FaxFree p11 and Faxer p5 look noisy. Test whether a clean preview before payment lifts Review → paid. Kill it if the week-1 spike cannot keep text on real forms readable.
2. Show the price of this fax before any payment step, with the preview beside it. No competitor screen shows a total for the fax before the paywall (Genius Fax p13 shows credits required, not a price). Test it as ad angle 1 against the outcome angle. Kill it if outcome-led creative beats it on cost per paying customer.
3. Send to US and Canada only in v1, and say so in the field. Fax.Plus p5 shows a country that was "on backorder" for numbers, and p17 shows "Regulatory documents". Test by tracking how many users type a non +1 number. Kill it if non +1 attempts exceed what the team will accept [UNKNOWN: set after first cohort].
4. A Live Activity for the send status. Apple Developer Relations says a Live Activity started locally can be updated by push without extra prompts (https://developer.apple.com/forums/thread/825419). Test on a small cohort against the notification pre-prompt. Kill it if opt-in to notifications is not lower than Live Activity use, or if the feasibility check fails [UNKNOWN: feasibility; verify with Apple docs and a build].
5. Offer a pass back on any failed fax and show it. Cheapfax advertises refunds for failed sends (context §2); no captured app shows this on a failure screen. Test by comparing refund requests per paying user before and after the line ships. Kill it if the provider cannot separate failed from delivered reliably.
6. A "Why didn't you send?" one-tap on Review close (Too expensive / Wanted to try first / Wrong number / Other) to choose between a free first page, packs and the monthly plan. Kill it if it measurably lowers Review → paid.
7. Drop the intent picker from the home screen and use its four categories only as ad and Custom Product Page segments. Test the use-case angle (ad 4) against ad 1. Kill it if the use-case page does not beat the generic page on qualified installs.

## Before build

**Captures still missing:**
- Any completed send in any app: queued, sending, delivered and failed states, and any delivery report. Every History in the captures is empty or a draft, so the status screens are unseen.
- A US storefront capture of every app. Every price in the captures is ₹ (India); every default country is +91.
- Municorn's "Free Test Fax" fallback modal on closing the paywall (named in the analysis PDF page 4, not in the 12 captured pages).
- Fax.Plus Basic tier and its price (the analysis PDF page 2 lists ₹999/month for Basic, but the plan screens p3 to p9 show Premium, Business and Enterprise; p7 shows part of a 200-page tier without its price).
- iFax with a US Apple ID, and a real notification of delivery.
- Tiny Fax receive pricing: the captured Receive paywall shows two sets of prices (p3: Monthly ₹999, Yearly ₹9,900; p9: Weekly ₹999, Monthly ₹2,499, Yearly ₹19,900).
- eFax, MyFax and the other context apps have no screenshots at all.

**Decisions still open (next agents):**
- Fax provider choice, per-page and per-attempt cost, retry rules, error codes, page limits, retention, and whether partial-page resend exists (s3-engineering, s0-validation).
- Prices, page bands and the monthly page allowance (s5-monetization).
- ATT: whether attribution needs it (s4-analytics).
- Number compliance for receiving numbers, junk-fax and abuse rules for sending, delete-on-request at the provider, privacy labels, and name clearance (s6-legal; questions only).
- Whether passes live on the device and a server ledger, and how a returned pass survives a reinstall (s3-engineering).

**Next agents to run on this note:**
- brand-designer: tokens, the Review screen and the Delivered banner as the signature visuals.
- ux-designer: wireframes for Send, Review, Status, Failure, History and the monthly sheet.
- s1-spec: screen states and edge cases.
- s5-monetization: page bands, monthly allowance, prices.
- s3-engineering: week-1 spikes on (a) fax-ready black-and-white rendering of real forms and (b) the provider's events and error codes.

## Competitor reference

Facts only, from the team's captures. "p" is the PDF page number within the app's file. All prices are ₹ (India storefront) as shown. Analysis PDF = "Fax_category analysis.pdf" (5 pages). File-to-app mapping: Municorn = "Fax by municorn.pdf"; mFax = "faxapp.pdf"; FaxFree = "faxx.pdf". The mapping for mFax and FaxFree comes from the in-app text (p5 "Fax from iPhone - Send Docs" and the logo; the ATT and camera text "FaxFree") and the analysis PDF.

**Page counts:** Municorn 12, iFax 17, Fax.Plus 17, Tiny Fax 16, Genius Fax 18, Faxer 13, FaxFree 17, mFax 11. Total 121 across 8 apps, plus the 5-page analysis PDF.

**Municorn (12 pages)**
- Key pages: p1 consent wall (Usercentrics, "Deny" / "Accept All"); p2 ATT over New Fax; p3 New Fax form; p4 camera permission; p5 crop; p6 document attached; p7 and p11 paywall; p8 number entered, Send active; p9 Sent empty; p10 area code list; p12 Info tab.
- Paywall placement: on tapping Send after a document and number are ready (p6 to p7), on choosing an area code (p10 to p11), and under Info › Buy Subscription (p12). Analysis PDF p4 also lists these triggers.
- Plans as seen: 1 week ₹949.00 (preselected), 1 month ₹2,799.00, 1 year ₹23,900.00 "SAVE 52%". Per-week figures shown for each (₹949.00, ₹632.03, ₹458.36). Headline "Send and Receive Unlimited Faxes". "Cancel anytime."
- Dark patterns: consent wall and ATT before any value (p1, p2); weekly plan preselected; "Over 200,000 people rated us" and a 5-star row (p7); "Unlimited"; no close button visible on the paywall (only Restore).

**iFax (17 pages)**
- Key pages: p1 paywall on launch; p2 Apple sheet "Send Only Monthly"; p3 select fax number; p4 "Send & Receive" paywall; p5 notification prompt over Home; p6 ATT; p7 New Fax composer ("Delivery by 9:36 PM"); p8 Add Document sources; p9 Edit Document; p10 "Send Your Fax Now" paywall; p11 Apple sheet "Send Only Weekly"; p13 Folders; p14 Settings; p15 login; p16 Cover Page Details; p17 template picker.
- Paywall placement: full-screen on cold launch (p1); again after the number picker (p4); and on Send of a draft (p10). Analysis PDF p2 also lists "Get a Free Number".
- Plans as seen: Send Only Monthly ₹3,499 per month with a 1-week free trial (p2, trial ends and billing starts 9 Oct 2026); Send & Receive "Free for 7 days, then only ₹1,999.00/month" (p4); "Only ₹999.00/week" with no trial (p10, p11). Analysis PDF p2 lists the same three.
- Dark patterns: hard paywall on launch; "Try for $0.00" and "Pay nothing for now!" in a ₹ storefront (p1, p4); laurels "SINCE 2008 TOP FAX APP", "10M+", "100M+", Lyft and 3M logos; ATT after the first screen (p6); "Get a free number" button (p5) leading to a paywall.

**Fax.Plus (17 pages)**
- Key pages: p1 Send Fax screen; p2 onboarding modal; p3, p4, p6 to p9 plan sheets; p5 number choice and "India on backorder"; p10 welcome fax with security badges; p11 add sheet (Scan, Photos, Files, Google, Box, Dropbox); p12 attached file with plan sheet on top; p14 Contacts; p15 Settings; p16, p17 My Info (Regulatory documents).
- Paywall placement: during initial entry flow (p2 to p3), on Send after a file is attached (p12), and from Settings › Upgrade Account (p15). Analysis PDF p2 also lists a persistent sticky banner.
- Plans as seen: Annual-23%-off toggle, then Premium ₹1,491.66/mo (₹17,900.00 billed annually, "26% OFF", 500 pages, 1 number); Business ₹2,908.33/mo (₹34,900.00 annually, "17% OFF", 1000 pages, 2 numbers); Enterprise ₹8,325.00/mo (₹99,900.00 annually, "16% OFF", 4000 pages). Monthly toggle: Premium ₹1,999.00; Business ₹3,499.00; Enterprise ₹9,900.00. A 200-page tier with Email to Fax and Cover Sheets is partly visible (p7). No trial seen.
- Dark patterns: plan choice forced to include a fax number before subscribing ("Your Number", p3 to p9; the number changes between captures); "Most Popular | Regular Use" tag; the "23% off" toggle label differs from the 26%, 17% and 16% badges; "#1 Rated Online Fax" badge (p10); a "My Credit $0.00" row in a ₹ storefront (p15).

**Tiny Fax (16 pages)**
- Key pages: p1 splash ("Sign up or sign in" / "Later"); p2 and p3 Send and Receive paywall; p4 account modal; p5 email entry; p6 notification pre-prompt ("Stay Updated"); p7 New Fax; p8 Inbox ("Get my fax number ₹999/month"); p9 Receive paywall; p11 to p13 Info; p14 scanner; p15 editor ("Not clear enough? Try TinyScan."); p16 Send paywall.
- Paywall placement: right after the splash (p1 to p2), on Send, on "Get my fax number" in Inbox (p8 to p9), and from the "Go Pro" button (p7). Analysis PDF p4 lists the same.
- Plans as seen: Send tab: Weekly ₹499 (preselected, "Popular"), Monthly ₹1,499, Yearly ₹12,900 (₹247.40/week) (p2, p16). Receive tab: two versions: Monthly ₹999 and Yearly ₹9,900 (₹189.86/week) (p3); Weekly ₹999, Monthly ₹2,499, Yearly ₹19,900 (₹381.64/week) (p9). "This plan only allows sending faxes." (p2).
- Dark patterns: "1.3M+ Satisfied users worldwide", "20K+ Countless 5-star ratings", "TOP Among the best in faxing", "10 Years Trusted Legacy" (p1); "App of the Day" and "Loved by millions of users" (p2); a quoted review (p3); "Later" leads to a paywall; sign-in modal on first New Fax (p4); cross-promotion for Tiny Scanner (p13) and TinyScan (p15).

**Genius Fax (18 pages)**
- Key pages: p1 to p5 welcome slides; p6 sign-up (email, confirm email, password at least 6 characters); p7 My Faxes with notification prompt; p8 My Faxes ("0 page credits available", "No fax number"); p9 and p10 Add Credits; p11 and p12 Fax Number; p13 New fax (Credits Required / You have); p14 Pick document; p15 scan editor; p16 and p17 Settings and Help; p18 Settings.
- Paywall placement: no paywall screen; credits and number are reached from Add Credits and Get Number on the My Faxes screen (p8) and from the New fax screen's credit count (p13). Analysis PDF p5 lists the same. No completed send is shown.
- Plans as seen: 1 fax page ₹99.00; 10 fax pages ₹699.00; 50 fax pages ₹1,999.00 (orange header) (p9, p10); "Never expires", "Use for sending faxes", "Use for receiving faxes with a number". US/Canada fax number: 1 month ₹399.00; 3 months ₹999.00; 6 months ₹1,999.00 (p11, p12); "Expires in 1 month, no auto renewal", "You have to purchase credits to receive faxes". "The cover page is free." "One page costs one credit." (p13).
- Dark patterns / notes: account required before the main screen (p5, p6); the notification prompt arrives after sign-up (p7); slide 4 says "Genius Fax is cheaper than the copy store"; "43,914 people have rated this version." and "Please rate Genius Fax" in Settings (p16, p17).

**Faxer (13 pages)**
- Key pages: p1 ATT (with an "Editors' Choice" laurel); p2 New fax with a banner ad; p3 History empty; p4 add options (Cover page recommended, Scan, gallery, files, other apps); p5 Adjust image ("We always use black and white to guarantee reception with any fax machine"); p6 New fax filled, rating pre-sheet; p7 paywall; p8 downsell; p9 Apple sheet "1 Week Lite"; p10 "Discard draft?"; p11 paywall again; p12 Settings; p13 Themes.
- Paywall placement: on Send fax after a draft is ready (p6 to p7), and again after closing the paywall (p8 downsell). Analysis PDF p3 lists Send, "Get your fax number" and the downsell on close.
- Plans as seen: 1 week full access ₹999.00 (selected), 1 month access ₹2,999.00 (₹692.07/week), 1 year access ₹24,900.00 (₹478.84/week, "SAVE 52%"); "Then ₹999.00/week. Cancel anytime" (p7, p11). Downsell: "Try for a full week just for ₹99.00" and "Start 7-Day Access", "Then ₹999.00/week" (p8); the Apple sheet shows ₹99 per week (1-week offer), then ₹999 per week starting 9 Oct 2026 (p9). Draft limit line "Files (1/500mb max.)" (p6).
- Dark patterns: ATT before value (p1); third-party banner ads on every main tab (p2, p3, p6, p12); a custom "Enjoying Faxer? Tap a star to rate it on the App Store." sheet over the send screen before the paywall (p6); downsell after close; "50K+ 5 star ratings" and "3.8M+ USERS" (p8); the paywall's marketing montage shows "Preparing fax… It should arrive in under a minute, up to 20 for bigger files" and "Cancel delivery" (p8) but no real status screen was captured.

**FaxFree (17 pages)**
- Key pages: p1 splash; p2 ATT over slide 1; p3 to p6 onboarding slides (Skip top left); p7 "Choose Your Plan"; p8 Send Fax screen; p9 camera permission; p10 camera ("Automatic border detection"); p11 editor (crop, brightness); p12 "1 page added." and Send Fax; p13 "Unlock Full Access"; p14 My Faxes (Draft); p15 Inbox with notification prompt and "Sign in with Apple"; p16 paywall; p17 Settings (Upgrade banner).
- Paywall placement: right after the onboarding carousel (p6 to p7), on Send Fax after a document is added (p12 to p13), and on Inbox (p15 to p16). Settings has an "Upgrade" banner (p17). Analysis PDF p1 lists the same.
- Plans as seen: p7: Yearly ₹3,999.00/year (₹76.90/week, "SAVE 89%", preselected), Monthly ₹1,199.00/month (₹276.08/week, "SAVE 67%"), Weekly ₹999.00/week; "$ Only ₹76.90 per week". p13: Weekly ₹999.00/week; Monthly ₹1,199.00 (₹276.08/week, "SAVE 72%"); Yearly ₹3,999.00/year (₹76.66/week, "SAVE 92%", preselected); "Not sure yet? Try it for free!" row; "Auto-renews. Cancel anytime."
- Dark patterns: ATT during onboarding (p2); stock-photo background; "1.7M+ USERS TRUST US" and a 5-star review "Thank you so much for the free fax !!!!!!" (p4); inconsistent SAVE % and per-week figures between two paywalls; faint close X; "Not sure yet?" trial row; "NEW Receive faxes" tag; a notification prompt and a Sign in with Apple wall on Inbox (p15).

**mFax (11 pages)**
- Key pages: p1 Faxes list; p2 Incoming filter ("Receive faxes", "Get a Number"); p3 loading sheet; p4 "Receive Faxes" paywall; p5 Apple sheet "Pro for one week"; p6 Drafts; p7 New Fax; p8 attached "Scan_46899244.pdf · 0 bytes · 1 page · ~40s"; p9 "Your Fax is Ready" paywall; p10 and p11 Settings (Guest Account, Link Email, Incoming Faxes Enable, For Business, Delete account).
- Paywall placement: on "Get a Number" in the Incoming filter (p2 to p4), and on the send arrow after a document is attached (p8 to p9). Settings › Incoming Faxes › Enable (p10). Analysis PDF p3 lists the same.
- Plans as seen: "Only ₹199.00 per 1 week. Cancel anytime." (p4, p9); Apple sheet "Pro for one week ₹199 per week" (p5). "Show all plans" link (p4, p9). No other price captured.
- Dark patterns / notes: no onboarding, ATT or consent before the main screen; both paywalls open as sheets with no visible close; "No fax limits" and "Highest priority" and "HIPAA compliant" (p9); a guest account with "Your data is only stored on this device. Link an email to keep it safe." (p10); the attached document shows "0 bytes" (p8).

**Analysis PDF (5 pages)**
- Covers eight apps in this order: FaxFree (BPMobile), iFax, Fax.Plus, Faxer, mFax, Municorn, Tiny Fax, Genius Fax. Each has onboarding, paywall triggers, offers and free features. Prices are ₹. Where its facts match the screens they are used above; where they add a fact not visible in a capture (Fax.Plus Basic ₹999/mo, Municorn "Free Test Fax", mFax "Guest account setup via local device limits") the fact is listed under Before build as not yet seen on a screen.

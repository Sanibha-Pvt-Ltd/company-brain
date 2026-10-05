---
type: category-product-strategy
category: document-scanner
member: harshil
updated: 2026-10-05
status: draft
sources: [context.md, screenshots:34 across 4 apps, knowledge:consumer_app_venture_knowledge_base_2026-10-04.md;organic-growth-knowledge-base.md;sanibha-app-factory-knowledge-base.md;us_consumer_utility_apps_knowledge_base_2026-10-04.md, web:2]
---

# Document Scanner — final recommendations (v1)

Built from [[research/categories/document-scanner/context]] and the team's in-app captures of Adobe Acrobat Reader, Adobe Scan, Scanner App and iScanner.

## Positioning

**Line:** For anyone who has to send a document somewhere that has rules. Scan it or open it, see whether it is ready, and fix what isn't, all before you hit send.

**Positioning statement:** For people who have to submit paperwork from their iPhone and have just hit a file-size limit or have to send several pages as one file, ReadyPDF is the document scanner that checks your file before you send it. Unlike Adobe Scan, Acrobat Reader, iScanner and Scanner App, it scans with no account or paywall, shows the file size and readiness of every document up front, and shrinks a PDF to the exact limit you type in, showing the result before you pay.

| Layer | Call |
|---|---|
| Acquisition hook | "PDF too big to upload? Make it fit." |
| Product differentiator | A Ready Check on every document: size, pages, format, blurry pages, empty form fields. Each item is marked Passed, Needs your review or Not checked. |
| Emotional benefit | Knowing the file will go through before you send it. |
| Retention reason | Scanning is free with no account and no watermark, and every later document gets the same check. |

**Who it's for:**
- Primary: a US adult in the middle of a one-off paperwork task (rental application, school or job application, insurance claim, benefits or HR form). They have a deadline and a portal or email address that limits file size, format or page count.
- Trigger moment: an upload is rejected for size, or they are told to "send everything as one PDF".
- Searches: "compress pdf", "make pdf smaller", "scanner app", "combine pdf", "sign pdf".
- Fears: the file is rejected again, they get charged for a subscription they didn't want, their personal documents end up on someone else's server.
- Secondary: people who regularly scan receipts, invoices and forms. They stay for free, account-free scanning.

**Job to be done:** "I need to get these pages to them as one file they'll accept, now."

**Name placeholder:** ReadyPDF. The name territory is ready, fit and send. Treat it as a placeholder until the name is cleared.

**Proof points that must be visible in the product:**
- The file size shows on every document thumbnail and on the export button.
- The Ready Check card appears on the document screen before Share. Each row shows its state.
- Fit to size shows "before → after" sizes and a full-page preview at real zoom before any paywall.
- Cold launch to first saved scan with no account, no onboarding carousel and no tracking prompt.
- Settings shows where files are stored, in plain words.

**App Store screenshots 1–3 (one story: check → fit → done):**

| # | Headline | Shows |
|---|---|---|
| 1 | "Check your PDF before you send it." | A real document with the Ready Check card: size, pages, format, one "Needs your review" row |
| 2 | "Too big? Fit it to the limit." | The Fit to size screen with a typed limit and before → after sizes from a reproducible demo file |
| 3 | "Scan in one tap. No account." | The camera capturing a page, then the saved document with its size shown |

Screens 4–6: combine into one PDF, sign, and where your files live. In the first storefront test, run this order against a camera-first order (shot 3 first).

**Ad angles:**
1. **Size rejection (lead):** an upload fails with "file too large" → open the app → type the limit → it fits → upload. Use real screen capture and real numbers from the demo file.
2. **One PDF:** three loose documents → scanned and imported → reordered → signed → one file, Ready Check passed.
3. **Control:** "Scan paperwork in seconds. No account."

Each angle gets its own Custom Product Page whose screenshots match the ad. That page's deep link opens the matching first screen: Open a PDF for angle 1, Scan for angles 2 and 3.

| Angle | Custom Product Page headline (shot 1) | Deep link opens | First action in app | Paywall moment it leads to |
|---|---|---|---|---|
| 1 Size rejection | "PDF too big to upload? Make it fit." | Open a PDF or photo | Pick the file, type the limit | Export of the fitted file |
| 2 One PDF | "Three documents. One PDF." | Scan | Scan or import pages, then Combine | Export of the combined file |
| 3 Control | "Scan paperwork in seconds. No account." | Scan | Scan, Save | None expected on the first document |

**Messaging table (placeholder copy for the ASO agent; store limits apply):**

| Surface | Line |
|---|---|
| App name (placeholder) | "ReadyPDF: Scan & Fit PDFs" |
| Subtitle (placeholder) | "Check, fit and send PDFs" |
| Promotional text | "Scan with no account. See your file size and a Ready Check on every PDF. Fit it to the limit you type." |
| First line of description | "Know your PDF will go through before you send it." |
| Ad end card | "Check it. Fit it. Send it." |
| Icon direction | A page with a check mark. No scanner-beam, no camera, no crown. |

**We will never claim:**
- "Guaranteed accepted", "approved", "submitted" or "meets IRS/USCIS/[institution] requirements".
- "#1", "130M+ users", ratings or review counts, or any "trusted by" line.
- "AI" as the headline promise.
- "Secure", "encrypted" or "never leaves your phone" beyond what the build actually does. A shared file has left the app.
- "Unlimited" or "Free" next to anything that is limited or paywalled.
- That a signature is valid or legally binding.
- "Backed up" or "cloud" unless files actually sync.
- "Lossless", "no quality loss" or "same quality" for a fitted file. Say "Text stays readable" only when the Fit to size quality line says so for that file.
- "Works with [portal or bank name]" or any named institution's logo in the store page or ads.
- "Free trial" or "No payment now" without the renewal price next to it.

## UI/UX

**Design principles (tie-breakers):**
1. Value before asks. The first scan or the first opened PDF comes before any account, paywall, tracking, notification or rating ask.
2. Show the number. File size, page count and target limit are always visible. The user never has to guess.
3. Say what we checked and what we didn't. Every check is Passed, Needs your review or Not checked. Nothing is shown as "verified" by default.
4. Show the result before the price. A paid action previews its output (size, pages, quality) before the paywall.
5. One document, one screen. Every action starts from the document screen. There is no tools grid.
6. Paperwork, not a stock photo. Show real documents and real UI. No people, 3D hands, globes or laurels.
7. Every flow ends in a file the user can find. Sharing or saving always ends with where the file went.

**Structure (no tab bar):**
- **Home:** two large buttons, "Scan" and "Open a PDF or photo", above a document list. Each row shows a thumbnail, name, page count, size and Ready Check badge. The Settings gear sits top right.
- **Document screen:** the core screen. It holds the page strip, the Ready Check card and an action row: Fit to size, Combine, Sign, Fill, Pages. The Share/Save button is at the bottom.
- **Settings:** Pro status, Manage subscription, Restore purchases, Where your files are, Default scan size, Saved signature, Support, Privacy, Terms.
- There are no Tools, Files, Account or AI tabs.

**First five minutes:**

| # | Screen | Purpose | What's on it | Primary action | Copy direction | Asks | Given so far |
|---|---|---|---|---|---|---|---|
| 1 | Home (cold launch) | Get to a task at once | Scan and Open buttons, empty-state line, Settings | Scan | "Scan a document or open one you already have." | nothing | the app |
| 2 | Camera permission pre-prompt (inline card, first Scan tap only) | Explain the camera ask | One line plus a Continue button that triggers the system prompt | Continue | "The camera is only used to scan pages." | camera | nothing yet |
| 3 | Document camera (VisionKit) | Capture | Auto edge detection, auto-capture, page counter | Save | system UI | nothing | live capture |
| 4 | **Document screen: first win** | Show a finished PDF and its readiness | Page strip, name field, "1 page · X MB", Ready Check card, actions, Share | Share / Save | "Your PDF is ready. Here's what we checked." | nothing | **a saved PDF with its size and checks** |
| 5 | Ready Check detail (tap the card) | Explain each row | Rows: Format, File size, Pages, Readability per page, Orientation, Empty form fields, Signature, "Accepted by recipient: not checked" | "Set a size limit" | Plain row labels with a one-line reason each | optional limit | full check results |
| 6 | Fit to size | Fit to the limit | Limit field (MB) with presets 1, 2, 5 and 10 MB, before → after sizes, zoomable page preview | Export fitted PDF | "Fits 5 MB. Zoom in to check the text." | a typed limit | the fitted preview |
| 7 | Paywall (only when exporting a Pro result) | Sell the outcome they just saw | The fitted result in a header strip, what Pro includes, plans, terms | Start plan | "Export this file and every fitted file after it." | payment | the result preview |
| 8 | Export sheet → confirmation | Finish | System share sheet / Save to Files, then "Saved to Files › ReadyPDF" or "Shared" | Done | "Saved. You'll find it in Files › On My iPhone › ReadyPDF." | nothing | the delivered file |

- First win is screen 4. Cold launch to first saved PDF takes 3 taps plus the system camera permission: Scan → Continue/Allow → Save. Auto-capture means no shutter tap.
- There is no onboarding carousel, sign-in screen or launch paywall.

**Copy deck by screen (exact lines; [brackets] are filled live; nothing in brackets is ever hard-coded):**

| Screen | Element | Copy |
|---|---|---|
| Home | Buttons | "Scan" / "Open a PDF or photo" |
| Home | Empty | "No documents yet. Scan one or open a PDF you already have." |
| Home | Row meta | "[N] pages · [X] MB" |
| Home | Row badge | "Checks passed" or "[N] to review" |
| Camera pre-prompt | Body / button | "The camera is only used to scan pages." / "Continue" |
| Camera denied | Card | "Camera is off. Open Settings, or import photos instead." Buttons "Open Settings", "Import photos" |
| Camera restricted (Screen Time or device policy) | Card | "The camera is restricted on this iPhone. Import a photo or PDF instead." Button "Import" |
| Document screen | First view after capture | "Your PDF is ready. Here's what we checked." Later opens: name only |
| Document screen | Sticky button | "Share · [X] MB". Secondary: "Save to Files" |
| Ready Check | Row: Format | "PDF. Opens as a standard PDF." |
| Ready Check | Row: File size, with limit, under | "[X] MB. Under your [L] MB limit." |
| Ready Check | Row: File size, with limit, over | "[X] MB. [Y] MB over your [L] MB limit." Link "Fit to size" |
| Ready Check | Row: File size, no limit | "[X] MB · Set a limit" |
| Ready Check | Row: Pages | "[N] pages. Count only. We can't tell if the right pages are included." |
| Ready Check | Row: Readability, ok | "All [N] pages look sharp (estimate)." |
| Ready Check | Row: Readability, review | "Page [n] may be blurry (estimate)." Link "Go to page" |
| Ready Check | Row: Readability, not checked | "Couldn't check page [n]." |
| Ready Check | Row: Orientation, review | "Page [n] is landscape. Fine if that's intended." |
| Ready Check | Row: Fillable fields (only on fillable PDFs) | "[N] fillable fields are empty." / "No empty fillable fields." |
| Ready Check | Row: Signature, placed | "Signature placed on page [n]. We can't tell if it's valid." |
| Ready Check | Row: Signature, none | "No signature added. Add one if the recipient asks for it." (grey, Not checked) |
| Ready Check | Row: Recipient acceptance | "Not checked. Only they can confirm it." (always grey) |
| Fit to size | Field / presets | "Limit (MB)" / "1 MB", "2 MB", "5 MB", "10 MB" |
| Fit to size | Before and after | "[A] MB → [B] MB" |
| Fit to size | Quality line | "Text sharp at 100% zoom." or "Text may blur at 100%. Review before sending." |
| Fit to size | Export button (Pro result) | "Export fitted PDF · Pro". The Pro label shows before the tap. |
| Fit to size | Already fits | "Already fits. No change needed." Button "Share" |
| Export | Confirmation | "Saved to Files › On My iPhone › ReadyPDF." or "Shared." |
| Export | Share sheet dismissed | No message. The user stays on the document. |

**Permissions:**
- Camera: asked on the first Scan tap after the inline pre-prompt. If denied, the camera screen is replaced by a card ("Camera is off. Open Settings, or import photos instead.") with Open Settings and Import buttons.
- Photos: use the system photo picker. No library permission is asked.
- Files: use the system document picker. No permission needed.
- Notifications: not asked in v1.
- Camera permission is asked once. After a deny, every later Scan or Retake tap shows the denied card; the app never re-triggers the system prompt (iOS will not show it twice).
- App Tracking Transparency: not shown at launch. If attribution needs it, show it only after the first completed export, with a neutral pre-prompt (decision in Before build).
- Rating: system review request only, after the second successful export or share. Never after the first scan. No custom "love it?" sheet.

**Core loop:**
- Day 2: open the app → the document list shows yesterday's file with its size and check badge → Scan or Open → Ready Check → Share. That is 3 taps from launch to the next scan.
- Week 2: repeat paperwork reuses the saved signature, the last size limit (offered as a one-tap chip) and a default name pattern.
- What brings users back: the next document task. There are no streaks, notification nags or guilt or fear copy.

**Key screens:**

*Home*
```
ReadyPDF                                   [gear]
[  Scan  ]          [ Open a PDF or photo ]
Recent
[thumb] Lease_Application.pdf  3 pages · 2.1 MB  ● Checks passed
[thumb] Scan Oct 5              1 page · 0.4 MB   ◐ 1 to review
```
- Empty: "No documents yet. Scan one or open a PDF you already have."
- Loading: skeleton rows.
- Permission denied: the Scan button stays live and leads to the denied card.
- Most important element: the two entry buttons.

*Document screen*
- Layout: name, then the horizontal page strip (tap to zoom, long-press to reorder), then the Ready Check card (one line per row, with a state icon and text), then the action row (Fit to size, Combine, Sign, Fill, Pages), then a sticky Share/Save button showing the size ("Share · 2.1 MB").
- States:
  - Processing: "Checking pages…" with real per-page progress.
  - Partial: rows fill in as each check finishes.
  - Error: "Couldn't read page 2. Retake or remove it."
  - Nothing to fix: all rows Passed, plus "Recipient acceptance: not checked".
- Most important element: the Ready Check card.

*Ready Check detail*
- Row states: Passed (green), Needs your review (amber, with a jump-to-page link), Not checked (grey, with a reason).
- Rows: Format = PDF; File size vs the limit if one is set; Page count; Readability per page (blur estimate); Orientation (landscape pages flagged for review, not as errors); Empty form fields (only for fillable PDFs); Signature placed yes/no ("validity not checked"); Recipient acceptance = Not checked, always.
- With no limit set, the size row reads "2.1 MB · Set a limit".
- Most important element: the always-grey "Recipient acceptance: not checked" row.

*Fit to size*
- Layout: limit field with presets; a quality line showing what the output will be ("Text sharp at 100% zoom" or "Text may blur at 100%: review"); before → after sizes; page preview with pinch zoom; an Export button.
- States:
  - Working: "Fitting…" with per-page progress.
  - Can't fit without hurting readability: "Smallest readable size is X MB. Remove a page or split the file." with Split and Remove options.
  - Already under the limit: "Already fits. No change needed." Free, no paywall.
- Most important element: before → after sizes next to the zoomable preview.

*Combine*
- Layout: pick documents or pages from the library or Files, drag to order, see the total size live.
- States: empty pick list, over the limit (shows an inline Fit to size link), done.
- Most important element: the running total size against the limit.

*Paywall*
- Layout:
  - Close (X) visible from the first frame, top left.
  - A strip showing the result just previewed ("Lease_Application.pdf · fits 5 MB").
  - Three plain bullets of what Pro does.
  - Two plan rows.
  - CTA.
  - Full terms text under the CTA.
  - Restore, Terms and Privacy links.
- Most important element: the result strip.

**Edge cases and states (every one ships in v1):**

| Case | Trigger | What the app does | Copy |
|---|---|---|---|
| Blurry page | Per-page blur estimate runs after capture or import | Amber badge on the page thumbnail, the Readability row goes amber, "Go to page" opens that page at zoom with two buttons. Export is never blocked. | Banner: "Page [n] may be blurry. Zoom in to check." Buttons: "Retake page" (scans) or "Replace page" (imported PDF), and "Keep as is" |
| Blur check cannot run | Page cannot be rendered | Row shows Not checked for that page | "Couldn't check page [n]." |
| Camera permission denied | User denied the system prompt | Camera screen replaced by the denied card; Import stays live | See copy deck |
| Camera restricted | Device policy | Restricted card, Import stays live | See copy deck |
| Huge file or many pages | Large import or Fit | Work runs page by page with a real progress count and a Cancel button; the original is never changed. The size at which a "large file" notice appears is [UNKNOWN: set in the week-1 spike from test devices]. | "Working on page [n] of [N]…" Button "Cancel" |
| Not enough storage | Write fails | Stop, keep the original, show the notice | "Not enough space on this iPhone to make this file. Free up space or remove pages." |
| App closed mid-work | Memory pressure or user swipe | Original untouched; on next open the document shows the notice | "ReadyPDF closed while working. Your original file is safe. Try again." |
| Multi-page reorder | Pages action opens a grid; long-press on the page strip is a shortcut | Long-press lifts a page with a haptic, drag, drop; page numbers renumber live; Ready Check re-runs. Undo stays until the user leaves the screen. VoiceOver users get actions "Move earlier", "Move later", "Move to start", "Move to end". | Toast: "Moved page [a] to position [b]. Undo" |
| Delete pages | Select, then Delete | No confirmation dialog; Undo toast. The last remaining page cannot be deleted. | "Deleted [n] pages. Undo" / "A PDF needs at least one page. Delete the document instead." |
| Edit after Fit | User reorders, deletes or signs after previewing a fit | The fitted preview is discarded | "Pages changed. Fit again to update the size." |
| Combine over the limit | Running total exceeds the limit | Total turns amber; inline link to Fit to size | "[X] MB. [Y] MB over your [L] MB limit. Fit to size" |
| Password-protected PDF | Import of a locked PDF | Password field; the app never removes a password. Combined or fitted output has no password, said before export. | "This PDF is locked. Enter its password to open it." / "That password didn't work." / "The new file won't have a password." |
| Unreadable or damaged PDF | Import fails | No partial document is created | "This file can't be opened. It may be damaged. Try exporting it again from where you got it." |
| Unsupported file | Word, Excel, ZIP, etc. | Not importable; no conversion in v1 | "ReadyPDF opens PDFs and photos. Convert this file to PDF first." |
| Photo import | HEIC, JPEG, PNG from the system picker | Each photo becomes one page, in picked order | none |
| Landscape page | Orientation check | Flagged for review, never an error; a Rotate button sits on the row | "Page [n] is landscape. Fine if that's intended." |
| No fillable fields | Fill on a PDF without AcroForm | Text box and checkmark placement stay available; the Fillable fields row is hidden | none |
| Name collision | Same name exists | Append " 2", " 3" | none |
| Share sheet dismissed | User cancels | Back to the document with nothing changed | none |

**Paywall triggers:**

| Trigger | Header strip shows | If the user closes it |
|---|---|---|
| Export of a fitted file that did not already fit | "[name] · fits [L] MB · [A] MB → [B] MB" | Back to Fit to size with the preview intact, plus a link "Share the original instead" |
| Export of a combined file | "[N] documents · [P] pages · [X] MB" | Back to Combine with the order intact, plus a link "Share the files separately" |
| Settings › Upgrade | No strip. Plain header "ReadyPDF Pro". | Back to Settings |

- No other trigger exists: not app open, scan save, sign, fill, page edits, Ready Check, a Home banner or a tool tile.
- After a close, the paywall comes back only when the user taps a Pro export again.

**Paywall states and copy:**

| State | What the user sees |
|---|---|
| Prices loading | Plan rows as skeletons, CTA disabled. After a failure: "Couldn't load prices. Try again." with a Retry button. A price is never shown unless it came from StoreKit. |
| Trial not available to this Apple ID | Trial wording is removed and the CTA reads "Subscribe · [price]/[period]". |
| Purchase pending (Ask to Buy or Apple's own approval step) | "Waiting for approval. You can keep working. Pro unlocks when it's approved." The user can close the paywall. |
| Purchase succeeded | Paywall closes, the export continues, and a banner reads "Pro is on. Exporting your file." |
| Purchase cancelled by the user | Stay on the paywall, no message. |
| Purchase failed | "That didn't go through. You haven't been charged." only when StoreKit reports no transaction; otherwise "Something went wrong. Check Settings › Apple ID › Subscriptions before trying again." |
| Restore with a purchase | "Pro restored." |
| Restore with none | "No purchases to restore on this Apple ID." |
| Already Pro | A Pro export never shows a paywall. |
| Pro ended | Settings shows "Pro ended [date]". Documents and free tools are unchanged. Fitted or combined files already exported stay exported. |

**Price display rules:**
- Every price is StoreKit's localized price. None is typed into the app.
- The price actually charged per billing period is the largest price on the row. A per-month equivalent for the annual plan may appear as smaller secondary text.
- No "Save N%" badge, no strike-through price, no "Best offer" label.
- Annual is preselected only if the annual row carries the full price and trial terms in the same size as the monthly row.
- Product names in App Store Connect and the app match: "ReadyPDF Pro Annual" and "ReadyPDF Pro Monthly" (placeholder until the name is cleared).

**Paywall rules:**
- Placement:
  - No paywall at launch, in onboarding or before the first scan.
  - The paywall appears only when the user exports a Pro result they have already previewed, or taps Pro in Settings.
- Type: soft. Close is always visible and never delayed. Closing returns to the document with the free result still available (for example, the unfitted original).
- Plans to test first: annual and monthly. No weekly plan. Test a free trial on annual only, and on annual vs no trial; the trial length comes from s5-monetization. Prices are UNKNOWN until s5-monetization sets them.
- Trial framing:
  - The CTA states trial length, renewal price and billing period in the same type size as the CTA.
  - "No payment now" never appears without the renewal price beside it.
- Cancel clarity:
  - Under the CTA: "Cancel anytime in Settings › Apple ID › Subscriptions."
  - Settings has a Manage subscription button that opens the system subscription sheet.
  - Settings shows Pro status in plain words: plan, renews on <date>, or "Trial ends <date>".
- Restore is on the paywall and in Settings. After a purchase or restore, Pro unlocks at once and shows a confirmation.
- Disclosure meets App Review Guideline 3.1.2: what the user gets, duration, price per period, auto-renewal and how to cancel.
- Never:
  - A downsell or "exclusive discount" after closing.
  - Countdown timers.
  - "Offer expires once dismissed".
  - Strike-through anchor prices.
  - "Save 94%" style badges.
  - A selectable "Try it for free" row.
  - A paid intro that renews weekly.
  - Ratings or user counts.
- Free users keep:
  - Unlimited scanning and importing.
  - Page edits.
  - Sign and fill.
  - The full Ready Check.
  - Exporting originals with no watermark.

**Settings screen (all copy):**

| Row | Copy and behavior |
|---|---|
| Pro status | "Free plan" with button "Upgrade"; or "Pro · Annual · renews [date]"; or "Pro trial · ends [date]"; or "Pro ended [date]". Buttons "Manage subscription" (opens the system subscription sheet) and "Restore purchases". |
| Where your files are | "Your documents are stored on this iPhone, in Files › On My iPhone › ReadyPDF. ReadyPDF doesn't back them up or sync them. Export a copy to keep it safe." |
| Default scan size | Three choices: "Smaller files", "Balanced" (default), "Sharpest text". What each does is set by the week-1 spike [UNKNOWN until then]. |
| Saved signature | View, redraw, delete. "Your signature is stored only on this iPhone." |
| Support | Opens mail composer or support page. |
| Privacy, Terms | Open in-app. |
| Version | Last row. |
- Not in Settings: Rate the app, Share the app, a user ID, a Pro upsell card.

**Visual language:**
- Competitor map: three of four apps open on near-black UI (Acrobat, Adobe Scan, Scanner App), and iScanner uses a blue gradient with stock photos of models. Paywalls are crowded with laurels, crowns and badges.
- Our territory:
  - Light by default (full dark mode supported): paper white and ink.
  - Two status colours, Ready green and Review amber, plus a neutral grey for Not checked.
  - One accent colour for primary actions.
- Low density: large touch targets and one primary action per screen.
- Type: SF Pro. Sizes and page counts in tabular numerals.
- Real document thumbnails everywhere. No illustration except the empty state.
- Motion: only for real progress (per-page checks, fitting). No confetti, sparkles or fake "preparing your workspace".
- Final tokens belong to brand-designer. The Ready Check card is the signature visual for the product and the ads.

**Voice:**
- Tone: calm, exact, plain.
- Lines we would ship:
  1. "Your PDF is ready. Here's what we checked."
  2. "Fits 5 MB. Zoom in to check the text."
  3. "Recipient acceptance: not checked. Only they can confirm it."
  4. "Smallest readable size is [X] MB. Remove a page or split the file." ([X] is filled in by the live computation)
  5. "Saved to Files › On My iPhone › ReadyPDF."
- Lines from competitor screens we would never ship:
  1. "This offer expires once dismissed." (iScanner, IMG_5347)
  2. "Miss This Offer" (iScanner, IMG_5347)
  3. "For a better personalized experience you can approve IDFA sharing." (Scanner App, IMG_5328)
  4. "Go paper - free with #1 scanner app." (Scanner App, IMG_5332)
  5. "Not sure yet? Try it for free!" (iScanner, IMG_5344)

**Accessibility:**
- Dynamic Type on every screen, including the Ready Check rows and the paywall terms (no fixed-size legal text).
- VoiceOver:
  - Each page thumbnail reads "Page 2 of 3, needs review: may be blurry".
  - Check rows read their state in words.
  - Size reads as "2.1 megabytes".
- State is never shown by colour alone: every status has an icon and a word.
- Contrast is WCAG AA for all text, including grey "Not checked" rows.
- Reduce Motion replaces progress animation with a static per-page count.
- The VisionKit camera keeps its system accessibility. The Import route is always offered beside Scan.

**Refuse list (seen in team screens):**
- Sign-in wall before any value: Acrobat IMG_5315, Adobe Scan IMG_5323.
- Paywall before any value: Acrobat IMG_5316, Adobe Scan IMG_5324, iScanner IMG_5344.
- Bundled camera and notification permission ask before the first scan: Adobe Scan IMG_5325.
- ATT prompt on launch behind a fake "Preparing your workspace…": Scanner App IMG_5328.
- Five-screen onboarding carousel with ratings, laurels and a quoted review: Scanner App IMG_5329–IMG_5333.
- Rating prompt right after the first scan: Scanner App IMG_5335.
- Custom review pre-sheet with emoji face: Scanner App IMG_5340.
- Paid intro renewing weekly: Scanner App IMG_5336.
- "Trusted by thousands" shown next to "3.5M total rating" claims: Scanner App IMG_5336, IMG_5329.
- Weekly plan, a selectable "try it for free" row, "SAVE 94%", and three different yearly prices across paywalls: iScanner IMG_5344, IMG_5345, IMG_5346, IMG_5347.
- Post-dismiss discount with countdown and strike-through anchor: iScanner IMG_5347.
- Crown badges scattered across the home screen and tool tiles: Acrobat IMG_5317, IMG_5322.
- Promo banners and cloud-connect upsells on home: Acrobat IMG_5317.
- AI summary and podcast upsells inside a document: Acrobat IMG_5318, IMG_5322.
- Watermark on free exports: Scanner App IMG_5337 (Pro "Remove Watermark").
- Default "cloud storage" processing without a choice: Adobe Scan IMG_5323, IMG_5325.

## v1 product features

| # | Feature | What it does | Free / Paid |
|---|---|---|---|
| 1 | Scan | VisionKit document camera with auto edge detection, auto-capture, multi-page. Saves a PDF with size shown. No watermark. | Free |
| 2 | Open / import | Open a PDF from Files, the share sheet or "Open in"; import photos with the system picker. | Free |
| 3 | Pages | Reorder, rotate, delete, add pages, retake a page. | Free |
| 4 | Ready Check | Automatic per-document check: format, size vs limit, page count, per-page blur estimate, landscape flag, empty fillable fields, signature placed, recipient acceptance always "Not checked". Three states. | Free |
| 5 | Size limit | User types or picks a limit (1/2/5/10 MB or custom). It is stored per document, and the last one is offered as a chip. | Free |
| 6 | Fit to size | On-device recompression and downsampling to hit the typed limit. Shows before → after sizes and a zoomable preview, and reports the smallest readable size if the target can't be met. | Preview free. Exporting the fitted file is Pro, unless the file already fits. |
| 7 | Combine | Merge several documents or pages into one PDF, with drag order and a live total size. | Pro |
| 8 | Sign | Draw a signature once, save it on device, place and resize it on any page. | Free |
| 9 | Fill | Fill AcroForm fields where the PDF has them; place text boxes and checkmarks anywhere else. | Free |
| 10 | Export | Share sheet, Save to Files, rename with a suggested name pattern. Confirmation names where the file went. | Free |
| 11 | Library | Local document list: thumbnails, pages, size, check badge, search by name. Files are visible in Files › On My iPhone › ReadyPDF. | Free |
| 12 | Settings and billing | Pro status in words, Manage subscription, Restore, Where your files are, default scan size, saved signature, support. | Free |
| 13 | Paywall | Soft paywall shown only at a Pro export, with the previewed result in the header. Annual and monthly. Guideline 3.1.2 disclosure. | — |

**Pro unlocks:**
- Exporting fitted-to-size files.
- Combining documents into one PDF.
- From v1.1: searchable PDF (OCR) and saved requirement presets.

**Free covers:** scanning, importing, page edits, sign, fill, the full Ready Check, previewing any fit, and exporting originals without a watermark. A free user can scan a form, sign it, see exactly how big it is and send it.

**Later (v1.1 / v2) and the trigger for each:**

| Feature | Trigger to build |
|---|---|
| Searchable PDF (on-device OCR text layer) | Paywall-exit answers, support tickets or reviews from the first cohort name text search or OCR |
| "Check & fit" share/action extension (fix a PDF from Mail or Files without opening the app) | More than half of Fit to size sessions start from an imported PDF rather than a scan |
| Requirement presets ("Rental application: one PDF, under 5 MB, signed") | Users set a size limit on a second document within 14 days |
| Paste-the-instructions (paste the portal's rules; the app reads the size, format and page rules on device) | Presets get used and users still type the limits by hand |
| Face ID / passcode lock | Support or review requests for it |
| iCloud Drive sync of the library | Support tickets about moving phones or lost documents |
| One-document pass (single non-subscription purchase) | Paywall view → purchase is below target and exit answers say "only need it once" |
| Page split ("split into files under X MB") | Fit to size often hits "can't fit without hurting readability" |

**Not building:**
- AI summary, AI chat, "Ask AI" and podcast generation.
- Converting to Word, Excel or PowerPoint.
- Full PDF text editing.
- Accounts and cloud storage.
- Fax.
- CV/resume builder.
- Book, ID and business-card capture modes.
- Cloud-drive connectors.
- Stamps.
- Collaboration and comments.
- Watermark on free exports.
- An onboarding carousel.
- Push notifications.

**Success metrics for v1:**
- Document completion rate (started a document → exported a file that passes every check the user set). Target UNKNOWN; set after the first cohort.
- Cold launch → first saved PDF: share of new installs and median time. Target UNKNOWN; set after the first cohort.
- Fit to size preview → Pro export start (paywall view → trial or purchase). Target UNKNOWN; set after the first cohort.
- Refund and support-ticket rate per paying user. Target UNKNOWN; set after the first cohort.
- D30 net proceeds per install, by acquisition angle (size rejection vs one PDF vs control). Target UNKNOWN; set after the first cohort.

## New recommendations

1. Make Ready Check the default document screen for every file, not a "Submission Mode" the user has to choose. Drop the four-task home menu.
2. Make scans small by default (sensible capture resolution and compression), and show the size on every thumbnail so oversized files never happen silently.
3. Spend week 1 on a technical spike: run Fit to size on a set of real US forms, IDs and receipts and test whether text stays legible at 1, 2 and 5 MB before any UI is built. Kill or reshape the hook if it can't.
4. Run a "no account, no AI" storefront variant (Custom Product Page) against the size-rejection page to see which promise pulls installs.
5. Keep a tiny "why did you close?" one-tap survey on paywall dismissal (Only need it once / Too expensive / Didn't fit well / Other) to choose between subscription and a one-document pass.
6. Ship a share/action extension ("Check & fit") in v1.1, so a PDF that bounced from a portal can be fixed straight from Mail or Files.

## Before build

**Captures still missing (take these before the s1-spec):**
- US storefront paywalls for all four apps. Every captured price is ₹ (India storefront).
- iScanner past the paywall: home, first scan, export, and where the compressor gate appears.
- Acrobat Reader's New scan flow and the Combine/Compress gate inside a document.
- Adobe Scan after the first capture: review screen, export, and the "Resize scans" gate.
- Scanner App: what triggers the paywall at IMG_5336 (auto or the PRO tap), what the "7-day trial is enabled" screen (IMG_5342) is, and whether free exports carry a watermark.
- Genius Scan and CamScanner: full first-run flows. Context relies on Genius Scan as the trust benchmark, but no screens were captured.
- One real "file too large" rejection from a common US portal, for the ad and the demo file.

**Decisions still open:**
- Whether to ask for ATT at all, given the attribution plan (s4-analytics).
- Prices and trial length for annual and monthly (s5-monetization).
- Name clearance for the placeholder (s6-legal).

**Next agents to run on this note:**
- brand-designer: tokens and the Ready Check card as the visual signature.
- ux-designer: wireframes for Home, Document, Ready Check, Fit to size and Paywall.
- s1-spec: screen states and edge cases.
- s5-monetization: plan structure and prices.
- Then s3-engineering for the week-1 Fit to size spike.

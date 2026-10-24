# ISH Student Housing — Audit by application

**Start with the journey, then explore each application.** Help students understand their next steps and help staff manage applications, housing, and charges as one connected journey.

Public edition: production screenshots and identifying transaction details are omitted. Review date: **October 23, 2026 · Read-only production review**. Follow-up review: October 24, 2026, covering stakeholder messages from October 23 at 23:00 through October 24 at 14:21 (Vietnam time), their screenshots, and legacy Figma references. No new production transactions or record changes were performed. The main sections focus on essential work; supporting detail is collapsed below.

## 0. The full journey — what happens next?

The **Application Form** collects applications → **Admin** reviews them and manages housing → the **Student Portal** lets students track progress, complete requirements, and pay. Staff manage rates, invoices, and requests throughout the stay.

This is a **proposed target journey** for design and storytelling. Screens and records were inspected; submission, approval, placement and payment were not tested end to end.

| Step | Who acts, and where? | Expected result | Who acts next? |
|---|---|---|---|
| J01 — Apply | Student · Application Form | Application submitted; fee result tracked separately | Admin receives the application |
| J02 — Review | Staff · Admin | Accepted, more information needed, or waitlisted | Student receives next steps |
| J03 — Complete requirements | Student · Portal; entry point to confirm | Documents/agreement complete; hold deadline visible | Admin checks requirements and housing |
| J04 — Select/confirm housing | Staff assignment or authorized student selection in Portal | Clear room/bed, dates, price, status | Student views the Portal |
| J05 — Issue invoice | Staff · Admin | Issued charge with service period and due date | Student receives a payment task |
| J06 — Pay | Student · Portal | Processing/success/failure; receipt after success | Admin monitors and reconciles |
| J07 — During the stay | Student · Portal; staff · Admin | Access information, submit requests, track progress | Responsible staff process and respond |

**Three key distinctions:** Applying does not secure a room. An estimated cost is not necessarily payable now. One student can have multiple reservations; money and documents need the correct stay context.

### October 24 clarification — separate two placement paths

**Product-owner clarification:** staff reject applications or convert them into reservations. A separate use case allows approved students to choose housing in the Portal; this is not Request Room Change. Whether this is enabled on current ISH production, and when Portal credentials are sent, remain unconfirmed.

**Observed in the older Student Portal Figma file:** New Reservation shows Booking Term, room-type cards, pictures, pricing, amenities, Select and Proceed. This is a reference image on the OLD page; NEW Design is empty. It adds design evidence, not proof of live production behavior. [F05]

**Impact:** J04 needs configurable staff-assigned and approved-student selection paths. Retain quote/review and the post-booking outcome. The video can demonstrate student selection once that path is verified.

### One sample record connects all screens

Use **Alex Morgan — Demo House — Fall Demo 2027** in design and video. This is proposed fictional data. Use the same application, reservation, room, dates and invoices across all three applications. Finance should validate sample rates and schedules first.

### Reading the evidence

**Verified:** directly observed in production/Figma. **To confirm:** behavior/rules not yet tested. **Proposed:** target design. E references production, F references Figma, S references stakeholder clarification/screenshots, V references the video description; see references below.

## 1. Application Form — starting an application

**Who uses it?** Prospective residents. **Their questions:** Am I eligible, what should I prepare, what does it cost, and what happens after submission?

**Input:** housing needs and requested dates. **Output:** an application for Admin review, with its fee outcome. Journey: **J01 → J02**.

### Current experience

Published guidance explains admissions, a non-refundable fee, processing within two business days, a five-day post-acceptance requirements window and a waitlist when unavailable. The form has six steps. Personal Information and the $50 fee screen were inspected; steps 2–5 and submission were not tested. [E01–E03]

### What to improve first

| Required improvement | Why? | Desired result |
|---|---|---|
| Name steps and explain documents/fees upfront | Students know what to prepare | Understand the process without staff assistance |
| Review before payment/submission | A fee must not imply guaranteed housing | Clear fee, entered information and next steps |
| Show submission results and recovery instructions | Avoid uncertainty about application/payment completion | Reference number and separate fee/submission outcomes |

### Proposed flow and screens

Before-you-apply guidance → named steps → review → pay/submit → result → tracking. Carry information into Admin and the Portal without re-entry.

Core screens: Before you apply; form; Review & fee; success/processing/failure; tracking instructions. Inventory: A01–A09.

**Confirm first:** steps 2–5, save/resume, reservation creation and Portal provisioning. Do not treat an application as a confirmed reservation.

**Handoff to Admin:** staff receive the right application and fee outcome and can identify missing information. **Video:** Alex submits and gets a reference → staff open that same application.

## 2. Student Management — staff operations

**Who uses it?** Admissions, housing operations and Finance. **Their questions:** Who needs attention, what is missing, is space available, and which charges need issuing or reconciliation?

**Input:** applications from the form; documents/requests from the Portal. **Output:** review decisions, housing, invoices and responses for students. Journey: **J02, J04, J05 and staff actions in J07**.

### Current experience

Resident Applications, Reservations, Availability, Rate Controller and BN Invoices exist. Reservations show room/bed, dates, totals, deposit and related invoices. Invoice states include Draft/Partial/Paid; rate tabs include Nightly/X Nights/Monthly. Approval, assignment, rate changes and issuance were not executed. [E07–E10, E14–E16]

### Follow-up evidence: the All view already has useful columns

A stakeholder screenshot shows Resident Applications in the **All** view with application reference, Created Date, Contact, Start Date, End Date and Status. Visible states include **Booked** and **Turned Down**. The earlier IDs-only observation applies to Recently Viewed, not every application view. Improve saved-view consistency and action queues; do not rebuild columns that already exist. The screenshot does not demonstrate conversion actions or prove that Booked means a confirmed room. [S02]

### What to improve first

| Required improvement | Why? | Desired result |
|---|---|---|
| Queue for pending applications, missing documents and expiring holds | Recently Viewed was sparse; All already includes applicant, dates and status | Know who needs action and what to do next |
| Related reservation/room/rate/invoice/payment in one context | Avoid repeated searching and mixing stays | Navigate without losing the record context |
| Dates, availability and pricing during placement | Avoid confirmation with incomplete information | Preview outcome/conflicts before confirmation |
| Clear review → issue → reconcile | Students receive the correct payment task | Matching amounts, statuses and history |

### Proposed flow and screens

Receive → review → reject/waitlist/request information or authorized conversion → check hold requirements → staff assignment or eligible student selection → pending/confirmed result → review price/schedule → issue invoice → monitor payment. ISH must confirm the exact order between application, hold and placement.

Core screens: Work queue; Application review; Reservation detail; Availability/placement; Rates/preview; Invoice list/detail/review; Payments/reconciliation. Inventory: D01–D09.

**Confirm before financial implementation:** partial-month calculations, deposit ownership across stays, semester/fixed-term mapping, approval permissions and student invoice visibility. A sampled invoice has date/rate-unit presentation requiring Finance review; incorrect billing has not been established. [E04, E06, E09, E10]

**Handoff to the Portal:** students see results, next tasks and payable charges. Staff see student payment/document outcomes. **Video:** open Alex's application, confirm housing, issue invoice → Alex sees the result.

## 3. Student Portal — tracking and self-service

**Who uses it?** Students with access. **Their questions:** What is my application/housing status, what should I do next, and what do I need to pay?

**Input:** Admin decisions and housing information. **Output:** documents/payments/requests routed to staff. Journey: **J03, J06, J07**, plus results from J02/J04/J05.

### Current experience

Dashboard, multiple stays, invoice/payment history, overnight guests and resident information exist. Figma already contains Payments, Add Payment Method and mobile screens. Complete reservation, payable-invoice and checkout-result flows were not found in the inspected inventory. [E04–E06, E12–E13, F01–F04]

### Approved-student booking — essential design work

The older reference lets students choose a **room type for a booking term**. It does not prove exact room/bed selection. A related reservation-list reference shows **Pending Approval**; the transition between these static images was not executed. [F05, F06, S01]

| Required step | What must be clear? |
|---|---|
| Eligibility and access | Is the application approved, can this student book, and what remains required? Keep Portal access separate from booking permission. |
| Term and room-type selection | Term dates, room-type availability, occupancy, bathroom and included amenities; clear selected/unavailable states. |
| Quote and review | Price basis, covered period, total, deposit, amount payable now and applicable cancellation terms. |
| Submit and outcome | Avoid duplicate requests; say Pending Approval where applicable, explain who acts next, and distinguish it from Confirmed. |
| Unavailable or interrupted | No results, sold out during selection, expired eligibility and a safe return/retry path. |

**Keep three actions separate:** first booking, renewal, and Request Room Change. Confirm which selection mode ISH currently permits. Do not promise a specific bed or immediate confirmation from these references alone.

### What to improve first

| Required improvement | Why? | Desired result |
|---|---|---|
| Tasks, housing/application status, documents and payments first | Avoid searching through news/maps | Immediately understand the next step |
| Separate current/upcoming/previous stays | Students may have multiple reservations | Clear stay context for rooms, dates, money and deposits |
| Complete invoice → payment → receipt | History alone does not resolve a new payment task | Clear period, balance, outcome and recovery |
| Preserve guests/documents/help and verify mobile | Practical resident needs | Working Handbook, trackable requests, usable mobile tasks |

### Proposed flow and screens

Home shows next task → open relevant checklist/reservation/invoice → complete → see result → return to updated Home. News/maps move lower or elsewhere.

**Interpret correctly:** no upcoming amount due in the sampled Portal coexisted with Admin draft invoices. This alone does not establish an incorrect balance. Separate payable and estimated costs under policy; do not expose raw drafts without authorization. [E05, E08, V01]

Core screens: Task home; application checklist/status; reservations; price/schedule; invoices; checkout; processing/success/failure/receipt; Guests; Documents/Help. Inventory: S01–S07, T01–T06, R01–R02.

**Confirm first:** when Portal access begins, room choice versus preferences, payment/deposit policy, and whether maintenance/scholarships/contract changes already exist or are new.

**Handoff back to Admin:** every document/payment/request links to the right application/reservation and responsible team. **Video:** Alex opens the issued invoice, pays in sandbox, gets receipt → staff see that transaction.

## 4. Shared work and delivery order

**Priority:** application/review → placement → prices/invoices → payment. Preserve existing functions; confirm demand before adding scholarships, advanced community or contract changes.

| Phase | Work | Outcome |
|---|---|---|
| 1 — Agree the journey | Confirm rules; connect three applications with one sample record | Clear actor, status and handoff |
| 2 — Design | Application, Admin and Portal with shared components/data | Complete J01–J07, including waiting/errors |
| 3 — Build/verify | Sandbox, financial reconciliation, permissions/mobile/migration | Correct charges/status; no lost functions/relationships |
| 4 — Pilot/video | ISH trial; record verified flows using fictional data | Ready to explain and reuse the package |

**Reusable design:** shared buttons, forms, tables, statuses, money/dates and templates. Configure branding, periods, prices and policy per client. Admin/Portal suit their users while sharing concepts/data.

**Release checks:** distinguish fee/submission outcomes; prevent duplicate charges on retry; correct deposit context; no overdue debt warning on paid invoices; authorized student data only; preserve existing functions/history.

## 5. Turn the journey into a video story

One complete task per episode, with a beginning and outcome. Change applications when the next actor takes over. Keep Alex, reservation/invoice references and amounts consistent.

| Episode | Beginning → outcome | Applications | Steps |
|---|---|---|---|
| 1 — Apply and get a decision | Submit → decision/next steps | Application → Admin → Portal if access exists | J01–J02 |
| 2 — Acceptance to housing | Requirements → room/dates confirmed | Portal → Admin → Portal | J03–J04 |
| 3 — Invoice to receipt | Issue → pay → staff see result | Admin → Portal → Admin | J05–J06 |
| 4 — During the stay | Information/guest request → progress | Portal → Admin → Portal | J07 |
| 5 — One package, multiple properties | Same journey, changed demo configuration/theme | Configuration and three applications | Full journey |

Add a rates episode after mapping monthly/semester/fixed-term. Earlier detailed storyboards below support this revised grouping.

**Sandbox and fictional data only.** Label unimplemented screens Prototype/Proposed experience. Exclude credentials, access codes, resident documents and production transactions.

## 6. Evidence and detailed analysis

Expand references for sources, inventory, reuse and storyboards. These are existing audit findings, not new research. The main sections above provide the revised reading and delivery structure.

:::details 1. Product decisions

Refresh the entire admissions → placement → rates → invoice → payment journey. A dashboard is only part of the solution. Preserve working relationships and distinct states before adding features.

Application is not reservation: published guidance describes application, acceptance/temporary hold, requirements and a secured outcome. Figma already has Payments and mobile; the gap is complete application/booking/payable-invoice/checkout flows. A zero due amount alongside draft invoices is not proof of a balance defect.

Release 1: application and acceptance checklist; task-focused Portal; staff placement workspace; clear rates; invoice review/payment states. Preserve Guests, Handbook and essential information. Confirm maintenance, scholarships and contract-change scope separately.

:::enddetails

:::details 2. Method, evidence and limits

| Label | Meaning |
|---|---|
| Verified | Direct observation of production screens/records or Figma |
| Source description | User requirement or video description/chapter, not reproduced behavior |
| Inference | Plausible interpretation requiring confirmation |
| Proposed | Target design, not implemented |
| Not tested | Insufficient access/state or outside read-only scope |

Existing authenticated Salesforce/Portal sessions were used. Navigation, display searches, tabs and viewing dialogs only. No submissions, card entry, payments, approvals, rate updates, check-in/out, business-record changes or Figma edits. Normal access logs/Recently Viewed can still update.

Sampling covered one account and its related reservations/finance, plus lists, rates and availability. This was not a database-wide audit. Private identity documents and agreements were not downloaded.

Not tested: application steps 2–5, entered-data validation, save/resume, submission, approval/rejection, actual placement changes, checkout/failures/refunds, other roles, notifications or private document contents. A mobile viewport request did not change measured desktop width, so deployed mobile remains unverified. Figma mobile frames do not prove responsive/accessibility behavior.

No YouTube transcript was available. Description and chapters were reviewed; no claim of complete audio/frame-by-frame verification.

| ID | Observation |
|---|---|
| E01 | Public admissions guidance: non-refundable fee, two-business-day processing, acceptance/temporary hold, five-day requirements window, waitlist when unavailable |
| E02 | Personal Information and six numbered steps; identity/contact/address/citizenship/background fields; no fabricated-data progression |
| E03 | $50 fee screen with Stripe input and Pay and Submit; inputs untouched |
| E04 | Portal reservation selector, dates/status, deposit, Pay, resident information, feedback/emergency contact |
| E05 | Paid invoice history with zero remaining, disabled Pay and Download; downloaded document contents not tested |
| E06 | Payment history linking room charges, deposit and application fee to related references |
| E07 | Admin reservation source/status, dates/room/bed, total, separate deposit status, related invoices/files/activity and check-in/out entries |
| E08 | Rate details and draft invoices align in total; Approved label in dialog requires interpretation |
| E09 | Invoice header/line dates differ; quantity/unit/rate display needs Finance interpretation, not an assumed billing-error claim |
| E10 | Nightly/X Nights/Monthly manager, monthly ranges, base rate/refundability, room/property/bed filters; no rates applied |
| E11 | Handbook link opens Page not found; HTTP status not checked |
| E12 | Guest list/form, dates, roommate, gender option, linen/dietary/health fields, post-approval ID guidance; not submitted |
| E13 | Multiple confirmed stays; no new-booking CTA in sampled account/state |
| E14 | Invoice search shows Draft/Partial/Paid; visible rows contradict displayed record count; a paid row retains negative Days Due |
| E15 | Availability filters/calendar/legend; no assignment or reservation creation attempted |
| E16 | Earlier live Recently Viewed showed IDs only. The supplied All-view screenshot has Created Date, Contact, stay dates and Booked/Turned Down. These are distinct views; conversion behavior remains untested |
| E17 | Long resident-information page with rules/community/safety/guests/support; other external links not individually checked |
| F01 | Student Portal plus empty Cover; 29 top-level frames in seven sections; no application/Admin page found |
| F02 | Dashboard/news/map hierarchy; hamburger navigation; inconsistent sample dates/copy; reservation entry without a matching complete flow in inventory |
| F03 | Payments/Add Method, methods/paid history/Receipt; complete due-invoice and checkout outcomes not found; nested reactions not fully audited |
| F04 | Nine 393px mobile frames; local variables/text styles empty, but instances exist and external libraries were not ruled out |
| F05 | Older Student Portal, OLD page, New Reservation image (node 2:47): Booking Term, room-type cards/pictures/pricing/amenities, Select and Proceed; NEW Design empty. Historical reference, not verified current ISH functionality. |
| F06 | Legacy reservation-list reference (node 2:53) shows a selected room type and Pending Approval. Static screenshot; transition not tested. |
| S01 | Stakeholder clarification: staff reject or convert applications; approved-student selection is a separate use case, not room change. Access timing uncertain; ISH activation unverified. |
| S02 | Stakeholder screenshots: Admin All view includes application/contact/date/status columns; separate image corroborates term-based room-type selection. No identities or screenshots published. |
| V01 | Video describes placements, rates, finance, academic periods, student booking and approved transactions; full ISH parity not established |

Record-level evidence remains in the internal Vietnamese report. Public sharing omits production images, resident/record identifiers, internal record URLs and transaction details.

:::enddetails

:::details 3. Requirements and reference video

| Requirement | Current evidence | Needed outcome |
|---|---|---|
| Modernize Admin, Portal and application | Figma mainly covers Portal; Admin has substantial scope | Application/Admin screens and task-based review |
| Preserve functionality | Admissions, holds, waitlist, reservations, finance, guests/documents | Trace current functions to target screens; do not silently remove unverified behavior |
| Simplify navigation | Current sidebar explicit; proposed hamburger/dashboard can hide tasks | Visible frequent desktop navigation and appropriate mobile navigation |
| Standardized reusable package | Instances exist; local tokens/styles not found | Shared data/state contracts, configurable policy and themes |
| Validate ISH then reuse | No UAT or deployment in this audit | Sandbox, financial/permission/migration checks, second demo tenant |
| Niche video series | Reference covers both roles | One fictional record across staff/student tasks |

| Video chapter | Described scope | Validation |
|---|---|---|
| 00:08–01:52 | Reservations/placement | Bed/detail/availability screens observed; transitions untested |
| 01:52–02:26 | Finance | Related records observed; approvals/issuance require sandbox |
| 02:26–03:56 | Semester/monthly | Monthly observed; semester mapping unverified |
| 03:56–04:59 | Fixed-term | X Nights exists; equivalence not established |
| 04:59–06:35 | Portal | Housing/history observed; no booking CTA in sampled state |
| 06:35–07:16 | Payment collection | Pay entry/history observed; no checkout/charge |

The Portal chapter begins at 4:59. A 2025 demonstration is not a full specification of 2026 production.

:::enddetails

:::details 4. Findings and priorities

P0: financial/data-integrity or preservation release gate. P1: core task. P2: efficiency/expansion. These priorities do not prove that every risk already occurs.

| Finding | Evidence | Improvement and acceptance |
|---|---|---|
| UX01 · P1 · Application vs reservation | E01/E16 | Distinct application/hold/secured states, linked IDs and deadlines |
| UX02 · P1 · Number-only progress | E02 | Named steps, required/optional labels, pre-payment review; confirm save/resume |
| UX03 · P1 · Fee/submission ambiguity | E01/E03 | Explain assessment fee; separate outcomes and recovery reference |
| UX04 · P1 · Deposit context | E04/E06/E07 | Required/collected/allocated/transfer and stay context; confirm ledger rules |
| UX05 · P1 · Due vs expected charges | E05/E08/V01 | Separate payable and permitted estimates; respect draft policy |
| UX06 · P0 gate · Date/unit display | E09 | Finance validates dates/basis/quantity/rate/proration; no unsupported misbilling conclusion |
| UX07 · P1 · Current/upcoming stay | E04/E13 | Date/lifecycle-based grouping and room-change boundaries |
| UX08 · P1 · Booking flow | E13/V01/F02 | Applicant/resident/staff-assisted paths, configurable selection |
| UX09 · P1 · Invoice-centered payment | E05/E06/F03 | Due/partial/detail, checkout/result/receipt; separate invoice/payment |
| UX10 · P1 · Admin/application gap | F01 | Review, placement, rates, invoice and reconciliation workspaces |
| UX11 · P1 · Broken Handbook | E11 | Version/owner, link health, fallback support |
| UX12 · P2 · Count/due language | E14 | Correct query count, loading/empty/error; no debt alert on paid rows |
| UX13 · P1 · Saved views and actionable queues | E16/S02 | Preserve existing All-view columns; align Recently Viewed and task views; verify missing-items/deadline/owner coverage |
| UX14 · P2 · Dashboard hierarchy | F02/F04 | Tasks, due, checklist and stay first; news/map secondary |
| UX15 · P1 · Fixtures/copy | F02 | One dataset, valid dates, consistent money/names, expiring notices |
| UX16 · P1 · Reuse foundations | F04 | Audit external library, then tokens/type/components/state contracts |
| UX17 · P2 · Personal fields/accessibility | E02/E12 | Confirm purpose/required status/permissions; investigate accessible names versus visible copy |
| UX18 · P1 gate · Mobile/accessibility | Limits | Test keyboard/screen reader, widths, zoom and form/payment errors |

Keep useful current patterns: explicit Portal sections, separate finance histories, disabled Pay when paid, bed-level details, independent deposits, Draft/Partial/Paid and inventory-scope filters.

:::enddetails

:::details 5. Current and proposed workflows

### Admissions and securing housing

Observed: guidance → Start → Personal Information → untested middle → fee entry. Published process describes review/acceptance/hold or waitlist, then agreement, identity, school/internship letter, photo and emergency contact. Actual submission/notifications/conversion were not reproduced.

Proposed: eligibility/documents/fee → named steps → requested dates/preferences → supporting information → review → payment/submission → tracking. Accepted students see deadlines/checklist/review status. Waitlisted students must not infer secured inventory. Show secured only after agreed requirements are satisfied.

Payment and application creation need separate outcomes: a paid fee plus submission timeout requires a reference/recovery path rather than another immediate charge.

### Reservation and placement

Observed: multiple stays, bed/date/rate/invoice details and availability calendar; Pending Approval appears in a list. Assignment/confirmation untested.

Proposed: queue → completeness/preferences → availability by dates/period → authorized room-type/bed choice → price/conflict preview → confirm → student result/next steps. Tenant modes may be preference-only, room-type/room/bed selection, or staff assignment. Confirm ISH's mode.

### Rates and schedules

Observed Nightly/X Nights/Monthly; semester/fixed-term/academic period only partly mapped.

Proposed: period/range → basis → property/room/bed scope → proration/inclusions/deposit/cancellation → representative previews → overlaps → authorized publish. Preserve rate snapshots so new prices do not silently change old bookings. Pricing basis and installments are separate; fixed-term totals can be paid in installments.

### Invoices and payments

Observed drafts for upcoming housing and paid history for an earlier stay. Approved-only visibility is consistent with the sample/video but not transition-tested.

Proposed staff: charge schedule → Draft → review dates/units/lines/adjustments → approve/issue → notify → attempts/allocations → reconcile. Separate lifecycle, settlement and overdue.

Proposed student: Transactions → service period/lines/paid/remaining/due → amount/method/fee review → checkout → processing/action required/success/failure → receipt. Repeated clicks/provider events must not duplicate charges; closing a processing page must not erase its status.

### Guests and services

Observed guest request/history, post-approval ID guidance, long house information and broken Handbook. Proposed: eligible room/dates → policy review → request → pending/approved/declined with reason → document checklist. Maintenance/renewal/change/termination are controlled requests, not direct contract edits. Figma's 14-day notice is not a verified ISH policy.

:::enddetails

:::details 6. Experience architecture and logical data model

Proposed Portal: Home; Applications/Reservations; Transactions; Requests; Documents; Community/House info; Profile/Help. Display authorized tenant modules; adapt Home for applicant, accepted, current and upcoming stages.

Proposed Admin: Work queue; Applications; Reservations/Placement; Availability; Rates; Invoices; Payments/Reconciliation; Configuration. Keep ID, separate statuses, next action, timeline, documents and related records in context.

This is a proposed logical model, not a verified Salesforce schema:

| Entity | Important relationships |
|---|---|
| Student/Contact | Many applications/reservations; do not rely on free-text email in payment descriptions |
| Application | Dates/preferences, admissions/completeness, fee outcome, hold deadline, related reservations |
| AcademicPeriod | Tenant, dates, property timezone, deadlines where relevant |
| Reservation | Student, dates/status, rate snapshot/version, total |
| Placement/StaySegment | Reservation → property/room/bed with dates; supports room changes |
| RatePlan/Version | Basis/scope/effective dates, proration/inclusions, approval |
| Invoice/Line | Reservation, service period, quantity/unit/rate/amount, issue/due date, lifecycle/balance |
| Payment/Attempt/Allocation | Provider reference/result/amount and invoice/deposit/fee allocation |
| DepositLedger | Required/collected/allocated/transferred/refunded and stay context |
| Document/Request/Activity | Owner, record link, permissions, status/version/deadline |

One connected record means traceable related objects, not one object replacing all lifecycles. Map actual enums before migration. Separate application (Draft/Submitted/Review/Waitlisted/Accepted/Declined/Withdrawn), hold (Active/Expiring/Expired/Secured), reservation/stay lifecycle, invoice (Draft/Issued/Void), settlement (Unpaid/Partial/Paid), and payment attempt (Initiated/Processing/Action required/Succeeded/Failed/Refunded). Derive overdue from issued balance/due date.

:::enddetails

:::details 7. Reusable design system and configuration

Direction from the brief: Admin uses SLDS patterns; Portal/public follows intended O:live/ISH branding. SLDS version and original O:live source were not verified.

| Layer | Reusable foundation |
|---|---|
| Primitive | Palette, spacing, radius, type scale, elevation |
| Semantic | Text/surface/border/action/focus/status tokens |
| Component | Field, Stepper, buttons, alerts, badges, Money, DateRange, tables/filters, empty/loading/error, modal/drawer, tasks |
| Domain | Reservation selector/summary, placement, rate breakdown, invoice lines, payment/receipt, deposit, document checklist, hold deadline |
| Template | Application wizard, task Home, Admin queue/workspace, finance review, responsive list/detail |

Define default/hover/focus/disabled/loading/error and keyboard behavior. Fields need labels/help/errors; statuses need words, not color only. Money needs currency, basis and period. Accessible names must not fall back to raw field tokens.

Suggested targets to verify: 16px Portal body, at least 14px dense table with zoom, common 44px touch controls, normal/large text contrast 4.5:1/3:1, visible unobscured focus. These are design targets, not a compliance certification.

Mobile: single-column forms, named progress, unobscured CTA, invoice cards with amount/due/status, usable tables where appropriate, on-demand map, accessible scrolling dialogs/focus return.

Core: IDs/relations/state contracts, permissions, financial integrity and accessibility. Configurable: branding, locale/currency/timezone, periods, application fields, fees/deposits, basis/selection/approval/documents/content/modules. Extensions: specialized scholarships, SSO, contract/accounting integrations when justified.

The config example is a non-deployable blueprint. Unverified rules stay null with confirmation requirements; no secrets. Audit external libraries first; then tokens, primitives, Money/Date/Status, domain components, templates, fixtures/state coverage and two themes. Demonstrate reuse with a second tenant using shared components/logic and different configuration.

:::enddetails

:::details 8. Screen inventory

Inspected Figma: **29 frames — 20 desktop and nine mobile**, seven sections and an empty Cover page. Missing from this inventory does not prove missing from another file/branch or the product.

| Section | Screens |
|---|---|
| Dashboard | Login; Dashboard; Navigation; Map; Dining selected; Add Guest; Request Room Change; Terminate Contract |
| Scholarships | Empty; List; Adding |
| Profile | Profile |
| Payments | Payments; Add New Payment Method |
| Documentation | Documentation; Important Information |
| Maintenance | List; Detail; New; Submitted |
| Mobile | Login; Navigation; Payments; Maintenance; Scholarship empty/form; Profile; Documentation; Dashboard |

| Target group | Scope |
|---|---|
| A01–A09 | Before apply, form, review/fee, result/recovery, tracking/hold/waitlist/checklist |
| S01–S07 | Login/recovery, task Home, reservation list/detail, booking/preferences, rates/schedule, documents |
| T01–T06 | Invoice list/detail, checkout, processing/action required, receipt, failure/retry/history |
| D01–D09 | Staff queue/review, reservation, availability/placement, rate configuration/preview, invoices/approval, reconciliation |
| C01–C03 | Tenant config, roles/policies, components/themes |
| R01–R04 | Guests, Handbook/info/help, maintenance, room change/renewal/termination |
| X01–X02 | Scholarships, Community/map if confirmed |

The CSV has 40 screen groups, not a committed artboard count. Include loading/empty/error/access-denied/mobile, invoice partial/paid/overdue/draft visibility, unavailable/waitlist/current/upcoming, and pending/failed payments.

:::enddetails

:::details 9. Roadmap and release criteria

Indicative working weeks after SME/sandbox/configuration access, not a committed schedule:

| Stage | Timing | Deliverables and gate |
|---|---|---|
| Validate rules | Week 1 | Function traceability, application middle steps, object/enums, fee/deposit/proration/approval; Product/Admissions/Finance agreement |
| Foundations/core prototype | Weeks 2–3 | Tokens/components/config/fixtures; full application → placement → invoice → payment, including empty/error |
| Core/ISH pilot build | Weeks 4–7 | Core flows, guests/info preservation; finance/roles/migration/mobile/accessibility/UAT checks |
| Pilot/rollout | Weeks 8–9 | Small cohort, support, monitoring, rollback; no incorrect balances, duplicate payment or lost links |
| Reuse/content | Weeks 10–11 | Second demo tenant, confirmed modules, sandbox series; prove reuse and marketing claims |

Release gates: explain/reconcile dates/units/amounts, no duplicate retry charge, retained history/references, owner-scoped access, authorized draft visibility, migration/rollback. Required checks do not establish current defects.

| Sandbox scenario | Required outcome |
|---|---|
| Fee succeeds, submission times out | One payment reference, recovery, no immediate duplicate charge |
| Acceptance requirements expire | Policy-correct hold/next action, no incorrect confirmation |
| No requested inventory | Explicit waitlist, no implied secured bed |
| Multiple stays | Correct current/upcoming, invoice and deposit context |
| Partial months/leap year/room change | Finance-approved service dates/calculation and stable rate snapshot |
| Draft → Issued → Partial → Paid | Correct visibility, balance/history/receipt |
| Pending/failure/double click/repeated provider event | No duplication, clear recovery, reconciled balance |
| Paid invoice after due date | Paid, not a debt warning |
| Resident accesses another's record | Denied, no document/record exposure |
| Keyboard/mobile/zoom | Complete core tasks with usable focus/errors/CTA |
| Migration | Matching counts/IDs/balances/documents/allocations |

No analytics baseline in this audit. Measure completion/drop-off, review time, on-time hold completion, placement time, invoice discovery, payment completion/duplicates, billing tickets, document-link health, tenant onboarding and component reuse. No percentage savings claims before measurement. Keep personal data, documents and card details out of analytics.

:::enddetails

:::details 10. Decisions requiring confirmation

| Question | Suggested owner | Dependency |
|---|---|---|
| Conversion conditions, real acceptance/hold/secured states, and Portal invitation timing? | Admissions + Salesforce | Journey/migration |
| Student room/bed choice or preference; renewal entry? | Housing Operations | Booking/permissions |
| Deposit ownership/carry-forward/transfer? | Finance | Deposit/allocations |
| Line date/quantity/rate-unit meaning? | Finance + Engineering | Financial release gate |
| Approval and student invoice visibility? | Finance + Salesforce | Invoice lifecycle |
| Semester/fixed-term/academic mapping? | Product + Salesforce | Pricing |
| Proration, tax, refunds/cancellation, partial payment? | Finance | Quote/checkout |
| O:live source and SLDS target? | Design Lead | Tokens/components |
| Existing maintenance/scholarship/contract-change features? | Product + ISH | Preservation/later scope |
| Termination notice and personal/health-field policies? | ISH policy owner | Copy/validation |

Fixture copy, queues, tokens and prototypes can progress while relevant questions are resolved. Financial logic, transitions and migration depend on these decisions.

:::enddetails

:::details 11. Detailed video storyboards

Use Alex Morgan/Demo House/Fall Demo 2027. Each episode: problem → action → outcome → next step. Keep a visible Prototype/Proposed experience label for unimplemented screens. Use no production records or access codes.

### Episode 1 — Application to move-in readiness · 75 seconds

| Time | Screen/action | Narration | Proof before recording |
|---|---|---|---|
| 0–8s | Before apply, fee, milestones | Know what to prepare. | Demo fee/policy |
| 8–23s | Named steps/preferences/review | Enter once; review before submitting. | No unbuilt save/resume claim |
| 23–35s | Sandbox fee/result/reference | Payment and admission are separate outcomes. | Sandbox result |
| 35–51s | Admin queue → application | Staff see missing items and next steps. | Working sandbox review |
| 51–67s | Acceptance, deadline, checklist | Track requirements to secure housing. | Verified deadline/checklist |
| 67–75s | Ready and CTA | A clear journey for students and staff. | Prototype label if needed |

### Episode 2 — Clear bed-level placement · 60 seconds

| Time | Screen/action | Narration | Proof before recording |
|---|---|---|---|
| 0–7s | Dates/type preference | A preference is not confirmed housing. | Consistent fixture |
| 7–24s | Workspace → availability | Check dates and space in context. | Sandbox inventory |
| 24–40s | Placement/rate/conflict preview | Review impact before confirming. | Working preview or prototype label |
| 40–53s | Pending review or confirmation → upcoming stay | Students see dates and status. | Verified state transitions; do not skip approval |
| 53–60s | Related record, CTA | Trace placement through the stay. | No automatic-allocation claim |

### Episode 3 — Monthly, semester or fixed-term? · 70 seconds

| Time | Screen/action | Narration | Proof before recording |
|---|---|---|---|
| 0–9s | Three pricing bases | Different models need different prices. | Supported bases |
| 9–28s | Period/scope/plan | Configure periods and room types. | Verified mappings |
| 28–45s | Full/partial preview | Preview costs and collection schedules. | Finance-approved proration |
| 45–61s | Portal basis/schedule | Separate term total and amount due. | Matching data |
| 61–70s | Second theme | One foundation, configured per operator. | Working reuse or concept label |

### Episode 4 — Approved invoice to receipt · 75 seconds

| Time | Screen/action | Narration | Proof before recording |
|---|---|---|---|
| 0–8s | Draft service period/lines | Review before issuing. | Finance-approved UI |
| 8–24s | Review → issue | Issued charges become payment tasks under policy. | Visibility rules |
| 24–42s | Due/detail/payment review | Know the period, paid amount and balance. | Correct allocation |
| 42–56s | Processing → success | Track the outcome even when processing takes time. | Sandbox only |
| 56–68s | Receipt and links | Connect receipt, charge and reservation. | Demo provider reference |
| 68–75s | Failure/recovery, CTA | A clear next step when incomplete. | Tested retry |

### Episode 5 — Self-service during the stay · 55 seconds

| Time | Screen/action | Narration | Proof before recording |
|---|---|---|---|
| 0–10s | Mobile task Home | Required tasks are easy to find. | Tested mobile |
| 10–27s | Guest/pending/document step | Submit and know what happens next. | Sandbox guest flow |
| 27–43s | Handbook/info/contact | Essential information when needed. | Valid content/version |
| 43–55s | Maintenance status, CTA | Track requests in one Portal. | Only if supported; otherwise guest history |

### Episode 6 — ISH and reusable housing · 60 seconds

| Time | Screen/action | Narration | Proof before recording |
|---|---|---|---|
| 0–10s | Connected journey | Link application, placement and payment. | End-to-end demo |
| 10–27s | Change demo brand/locale/period | Configure brand and policy per property. | Working config |
| 27–43s | Two Portals, shared components | Reuse a validated experience. | Real reuse, not only pictures |
| 43–53s | Sourced metric or unmeasured label | ISH validates the package first. | Measured claims only |
| 53–60s | Product CTA | Find your housing workflow. | Agreed destination |

Cut 15–25-second clips around one action/outcome. Combine application/placement/payment into a 2–3-minute overview. Keep both Admin and Portal in the longer buyer walkthrough. Use legible text and purposeful cursor movement.

Claim ledger: history, related finance, bed detail and fee entry have production evidence. Semester/fixed-term and approval visibility are partly verified/described. Savings percentages, zero errors, automated placement and fixed onboarding-time claims are unsupported.

:::enddetails

:::details 12. Handoff

Start with coherent fixture dates/copy, invoice/checkout states, application/hold/checklist, staff review/placement and tokens. Finance resolves unit/date and deposit context before financial implementation. Validate sandbox scenarios and migration reconciliation before rollout.

Deliverables: report, HTML, 40-group inventory, config blueprint and internal evidence. No production business record or Figma edits were made in the audit. Public editions omit original record-level evidence.

:::enddetails

:::details Evidence images

The internal Vietnamese report retains selected screenshots of the application form/fee, Portal invoice history, draft invoices, invoice date/unit display and broken Handbook destination. Public editions omit production images and identifiers. Screenshots show one moment, not proof of every workflow transition.

:::enddetails

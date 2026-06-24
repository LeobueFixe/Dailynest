# IAusage — DailyNest

Record of AI usage in the development of the DailyNest project.

---
## Frontend — AI Usage
---

## Task #01 — Frontend UI: Layout & All Pages

**Date:** 29 May 2026  
**Model:** GitHub Copilot (Claude Sonnet 4.6)  
**Session:** Autonomous agent

### What was generated with AI

| File | Description |
|---|---|
| `frontend/style.css` | Complete design system: CSS variables, reset, sidebar, layout, buttons, stat cards, task table, modal, auth pages, landing page, notepad, agenda, responsiveness |
| `frontend/app.js` | Interactivity: modal open/close, sidebar toggle (mobile), workspace toggle, password visibility, task CRUD, task filter/search, automatic stats, notepad word count / save / clear |
| `frontend/index.html` | Split-screen landing page (left: hero + about, right: real Unsplash photo of laptop/desk with glassmorphism stats card + dark panel with 5-dot slider) |
| `frontend/login.html` | Login page with blue topbar, centred card, fields with icons, password toggle, remember me |
| `frontend/register.html` | Registration page with 4 fields, privacy policy checkbox, password validation |
| `frontend/tasks.html` | Main page: sidebar, stat cards (4), table with search + filters + pagination, Create New Task modal |
| `frontend/notepad.html` | Note editor with title, body, stats (words/chars/read time), save/clear with localStorage |
| `frontend/agenda.html` | Weekly agenda (20–26 May 2026) with hour grid, 4 coloured events, mini calendar, upcoming list |


### Criteria met (Task #01)

- [x] Sidebar with DailyNest logo (house icon + text)
- [x] Workspace toggle: Work / Personal (pills)
- [x] 4 nav links with icons: Tasks (active), Agenda, Notepad, Files
- [x] User avatar at the bottom: circular black "RD" + name + email
- [x] 4 stat cards with coloured icons (blue, grey, orange, green)
- [x] Search bar + dropdowns in the table
- [x] Table with uppercase headers: TASK NAME, STATUS, DUE DATE, CREATED
- [x] Task rows with coloured status dot + calendar icon + timestamp
- [x] Pagination `< 1 >` at the bottom
- [x] "Create New Task" modal functional (open/close, Escape, click outside)
- [x] Modal with fields: Task Name, Status, Priority, Due Date, Description
- [x] Faithful design: background #f5f5f5, white sidebar, black buttons
- [x] Inter font loaded (Google Fonts)
- [x] Responsive (mobile: sidebar collapses with toggle)

---

## Fix #01 — Landing Page: visual correction to match the Figma

**Date:** 29 May 2026  
**Model:** GitHub Copilot (Claude Sonnet 4.6)

### What was fixed

| File | Change |
|---|---|
| `frontend/index.html` | Stats restructured from individual pills to a single glassmorphism card with 3 columns (12k+ / 98% / 4.9★) and separators; slider updated to 5 dots; "About us" section with correct title and 6 paragraphs from Figma; bottom panel with correct text |
| `frontend/style.css` | `.landing-right` converted from `position:relative` to `flex-column`; `.landing-photo` added with real photo (Unsplash) + `background-size:cover`; added `.stats-card`, `.stats-item`, `.stats-number`, `.stats-label`, `.stats-sep`; `.landing-panel` updated to solid `background:#111` without blur |

---

## Fix #02 — Landing Page: responsiveness without scroll

**Date:** 29 May 2026  
**Model:** GitHub Copilot (Claude Sonnet 4.6)

### What was changed

| File | Change |
|---|---|
| `frontend/style.css` | `.landing-page` and `.landing-left` changed to `height: 100vh; overflow: hidden` — page locked to viewport without external scroll; `.landing-content` with `scrollbar-width: none` and `::-webkit-scrollbar { display: none }` for invisible internal scroll; reduced spacing: `landing-content` padding `56px→32px`, `landing-h1` `3.5rem→3rem`, `landing-desc` margin `32px→20px`, `landing-actions` margin `40px→20px`, `landing-divider` margin `28px→16px`, `about-section p` padding `14px→9px`, `landing-eyebrow` margin `18px→12px`; 768px breakpoint updated to restore `height: auto` and `overflow: visible` on mobile |

---

## Task #02 — Tasks Page: Edit Modal + POST/PUT API Wiring

**Date:** 29 May 2026  
**Model:** GitHub Copilot (Claude Sonnet 4.6)

### What was created / changed

| File | Change |
|---|---|
| `frontend/app.js` | Added `apiPost`, `apiPut`, `apiDelete` functions with `fetch` to `http://localhost:8000`; `buildRow()` updated to include `data-id`, `data-name`, `data-due`, `data-desc` on the `<tr>` and an actions column with Edit/Delete buttons (SVG icons); added `_editingRow` state and `_taskIdCounter` variable; new `openNewTaskModal()` function clears state and opens modal in create mode; new `openEditModal(btn)` function pre-fills the form with row data and opens modal in edit mode; new `deleteTask(btn)` function with confirm + `DELETE /tasks/{id}` call + local removal; `submitCreateTask()` refactored to support both modes: in edit mode does `PUT /tasks/{id}` and updates the row locally; in create mode does `POST /tasks` with local fallback if API is unavailable |
| `frontend/tasks.html` | Added `<th>Actions</th>` to the table; example row updated with `data-id`, `data-name`, `data-due`, `data-desc` and an actions cell with Edit/Delete buttons; "New Task" button changed to `openNewTaskModal()`; modal submit button with `id="taskSubmitBtn"` for JS to dynamically change the text (Create Task / Save Changes) |
| `frontend/style.css` | Added styles `td.task-actions`, `.task-actions`, `.action-btn`, `.action-btn.edit-btn:hover` (blue), `.action-btn.delete-btn:hover` (red) |

---

## Task #03 — Task Filters & Search

**Date:** 1 June 2026  
**Model:** GitHub Copilot (Claude Sonnet 4.6)  
**Session:** Autonomous agent

### What was changed

| File | Change |
|---|---|
| `frontend/tasks.html` | Select `#statusFilter` updated to three options: **All / Pending / Done**; search input event changed from `oninput="filterTasks()"` to `oninput="onSearchInput(this.value)"`; status select event changed to `onchange="onStatusFilterChange(this.value)"` |
| `frontend/js/modules/tasks.js` | Added state variables `filterSearch` and `filterStatus` that store the current value of each control; added handler functions `onSearchInput(value)` and `onStatusFilterChange(value)` that update state and call `filterTasks()`; `filterTasks()` refactored to read values from JS state variables instead of the DOM, and to map `pending` → `not-started \| in-progress` and `done` → `completed` |

### Criteria met (Task #03)

- [x] Status filter with options: All / Pending / Done
- [x] "Pending" filters `not-started` and `in-progress` tasks; "Done" filters `completed`
- [x] Search field filters by title in real time (via `oninput`)
- [x] State maintained in JS variables (`filterSearch`, `filterStatus`)
- [x] Pure client-side logic — no server calls

---

## Task #04 — Task Mark Complete & Delete

**Date:** 1 June 2026  
**Model:** GitHub Copilot (Claude Sonnet 4.6)  
**Session:** Autonomous agent

### What was changed

| File | Change |
|---|---|
| `frontend/js/api.js` | Added `apiPatch(path, body)` function that does a `PATCH` with JSON body, to support the `PATCH /tasks/{id}` endpoint |
| `frontend/js/modules/tasks.js` | `buildRow()` updated: added checkbox column (`<td class="task-check-cell">`) as the first cell of each row, with `checked` if status is `completed` and `onchange="markComplete(this)"` attribute; task name with `text-decoration:line-through` when completed; added `markComplete(cb)` function that reads the checkbox state, calculates the new status (`completed` or `not-started`), calls `apiPatch('/tasks/{id}', {status})` (with local fallback), updates `data-status`, the status badge and the task name style in the row, and calls `updateStatCards()` |
| `frontend/tasks.html` | Added empty `<th></th>` as the first table header (checkbox column); static example row updated with `<td class="task-check-cell"><input type="checkbox" ...></td>` as the first cell |
| `frontend/css/modules/tasks.css` | Added styles `td.task-check-cell` (40px width, centred) and `.task-check` (16×16px, cursor pointer, `accent-color: #111`) |

### Criteria met (Task #04)

- [x] Checkbox in the first column of each table row
- [x] Checkbox pre-checked if the task already has status `completed`
- [x] Clicking the checkbox calls `PATCH /tasks/{id}` with `{status: "completed" | "not-started"}`
- [x] Local fallback if the backend is unavailable
- [x] Status badge updated instantly (without reload)
- [x] Task name with strikethrough + muted colour when completed
- [x] Delete button with native `confirm()` and `DELETE /tasks/{id}` call (already existed, maintained)
- [x] `updateStatCards()` called after both actions to reflect the counters

---

## Task #05 — Agenda Calendar: Month View

**Date:** 1 June 2026  
**Model:** GitHub Copilot (Claude Sonnet 4.6)  
**Session:** Autonomous agent

### What was changed

| File | Change |
|---|---|
| `frontend/js/modules/agenda.js` | File created from scratch; `EVENTS` array with 8 example events for June 2026; `buildMonthGrid()` function that dynamically generates the current month's grid (Monday-based offset, cells for other months' days, today's marking, coloured dots by event); `selectDay(dateStr, date)` function that selects a day, re-renders the grid with highlight and populates the sidebar panel with the day's events; `prevMonth()` / `nextMonth()` functions for navigation between months (with selection reset); `resetDayPanel()` to clear the panel; `setView(btn)` redefined to manage the switch between Week View and Month View (shows/hides `#week-view`, `#month-view`, `#mini-cal-card`, `#upcoming-panel`, `#day-events-panel`) |
| `frontend/agenda.html` | Week header + week grid wrapped in `<div id="week-view">`; added `<div id="month-view">` with internal nav (prev/next + `#month-nav-title` title), row of day names and `<div id="month-grid-body">`; added `<div id="day-events-panel">` in the sidebar with `.day-events-title` and `.day-events-list`; IDs `mini-cal-card` and `upcoming-panel` added to existing sidebar panels; inline `<script>` block with `setView` removed (function moved to `agenda.js`) |
| `frontend/css/modules/agenda.css` | Added classes: `.month-nav`, `.month-nav-title`, `.month-weekdays`, `.month-grid-body`, `.month-day-cell`, `.month-day-cell.other-month`, `.month-day-cell.is-today`, `.month-day-cell.is-selected`, `.month-day-num`, `.month-day-dots`, `.event-dot` (`.blue`, `.yellow`, `.green`, `.purple`), `.day-events-title`, `.no-events-msg`, `.day-event-item` |

### Criteria met (Task #05)

- [x] Monthly calendar grid dynamically generated in vanilla JS from the current month
- [x] Correct Monday-based offset (first days of the month aligned to the right weekday)
- [x] Days from other months rendered with muted colour
- [x] Today marked with a black circle
- [x] Coloured dots on days with events (max 3 dots per day)
- [x] Clicking a day highlights it (`.is-selected`) and populates the sidebar panel with that day's events
- [x] Sidebar panel shows selected day title + event list with coloured dot and time
- [x] "No events for this day." message when the day has no events
- [x] Prev/next month navigation with selection reset and grid rebuild
- [x] "Month" button in view-toggle activates Month View; "Week"/"Day" returns to Week View
- [x] Week View and Month View mutually exclusive (show/hide via JS)
- [x] Mini calendar and Upcoming panel hidden in Month View

---

## Task #06 — Agenda: Day & Week Views + Navigation

**Date:** 1 June 2026  
**Model:** GitHub Copilot (Claude Sonnet 4.6)  
**Session:** Autonomous agent

### What was changed

| File | Change |
|---|---|
| `frontend/js/modules/agenda.js` | Added state variables `weekViewDate` and `dayViewDate`; `setView()` refactored to manage three views (day/week/month) with correct show/hide of panels; added `buildWeekView()` that dynamically generates the week header (Mon–Sun with today marked) and the hour grid (7h–17h) with events filtered by date and time from the `EVENTS` array; added `buildDayView()` that renders the selected day's event list sorted by time, with "No events" message when empty; added `updateDateRangeLabel()` that updates the toolbar text according to the active view (weekly range, single date, or month); added `prevPeriod()` and `nextPeriod()` that dispatch navigation to the correct function depending on `currentView` (-7/+7 days in week view, -1/+1 day in day view, prevMonth/nextMonth in month view); `prevMonth()` and `nextMonth()` updated to call `updateDateRangeLabel()`; `init()` block added at the end of the file that calculates the Monday of the current week, initializes `weekViewDate` and `dayViewDate`, and calls `buildWeekView()` + `updateDateRangeLabel()` to render the initial state |
| `frontend/agenda.html` | Toolbar navigation buttons changed from static to `onclick="prevPeriod()"` / `onclick="nextPeriod()"`; static date range text replaced by `<span id="agenda-date-range-text"></span>` (dynamically populated by JS); static week header content (7 fixed day columns) removed and replaced by `<div class="week-header" id="week-header"></div>`; static week grid content (11 hardcoded hourly rows) removed and replaced by `<div class="week-grid" id="week-grid"></div>`; added `<div id="day-view">` with `#day-view-title` and `#day-view-list` as the Day View container |
| `frontend/css/modules/agenda.css` | Added classes: `.day-view-header`, `.day-view-title`, `.day-view-list`, `.day-view-event`, `.day-view-event-time`, `.day-view-event-body`, `.day-view-event-title` |

### Criteria met (Task #06)

- [x] "Day" button in view-toggle activates Day View; "Week" activates Week View; "Month" activates Month View
- [x] Day View shows the selected day's event list, sorted by time, with coloured badge
- [x] Day View shows "No events for this day." message when there are no events
- [x] Week View dynamically rendered (7 Mon–Sun columns) from `weekViewDate`
- [x] Week View marks today with a brand colour circle in the header
- [x] Week View places events in the correct hour cell (parsing the event's `time`)
- [x] Toolbar `‹` / `›` arrows call `prevPeriod()` / `nextPeriod()`
- [x] In Week View, arrows shift the period by ±7 days and re-render
- [x] In Day View, arrows shift the period by ±1 day and re-render
- [x] In Month View, arrows delegate to `prevMonth()` / `nextMonth()` (previous behaviour maintained)
- [x] Date range label in the toolbar dynamically updated for each view and period
- [x] Automatic initialisation on page load (current week with Monday-offset)

---

## Task #07 — Agenda Event Form: Create & Edit

**Date:** 2 June 2026  
**Model:** GitHub Copilot (Claude Sonnet 4.6)  
**Session:** Autonomous agent

### What was created / changed

| File | Change |
|---|---|
| `frontend/js/api.js` | Added `apiGet(path)` function that does a `GET` and returns JSON, used to load events from the backend |
| `frontend/agenda.html` | Event modal replaced: `eventName`/`eventDate`/`eventTime`/`eventColor` fields removed; new fields `eventTitle` (text), `eventDescription` (textarea), `eventStartDate` (datetime-local), `eventEndDate` (datetime-local) and hidden `editingEventId`; form `onsubmit` points to `submitEventForm(event)`; submit button with `id="eventSubmitBtn"` (dynamic text: *Create Event* / *Save Changes*); "New Event" button changed to `openEventModal('create')`; `#upcoming-panel` simplified to contain only `<div id="upcoming-list">` (dynamically populated by JS) |
| `frontend/js/modules/agenda.js` | `EVENTS` array converted from static `const` to dynamic `var` (initially empty); added helpers `evtColor(id)`, `evtDate(isoStr)`, `evtTime(isoStr)` to convert events from API format; added state variable `_editingEventId`; added `loadEvents()` that calls `GET /events` and on failure uses example data with `start_date`/`end_date` in ISO format; added `rebuildViews()` that dispatches to the active view; added `openEventModal(mode, eventId)` and `closeEventModal()` that manage the create/edit state of the modal (title, submit button, field pre-filling); added `submitEventForm(e)` that does `POST /events` (create) or `PUT /events/{id}` (edit) with local fallback in both cases; added `renderUpcomingPanel()` that filters future events, sorts by ascending `start_date`, and renders the first 5 in `#upcoming-list`; `buildMonthGrid()`, `selectDay()`, `buildWeekView()` and `buildDayView()` updated to use `evtDate(e.start_date)`, `evtTime(e.start_date)` and `evtColor(e.id)` instead of the old model's `date`, `time`, `color` fields; events in the Week View and Day View get `onclick="openEventModal('edit', id)"` for direct editing; events in the Month View sidebar panel get an `event-edit-btn` edit button; `init()` updated to call `loadEvents()` on startup |
| `frontend/css/modules/agenda.css` | Added classes: `.form-textarea` (vertical resize, min-height 72px, font-family inherit); `.event-edit-btn` (inline edit button on sidebar panel event items, with hover in brand colour) |

### Criteria met (Task #07)

- [x] Modal with fields: Title (text), Description (textarea), Start (datetime-local), End (datetime-local)
- [x] "New Event" button opens modal in create mode (title "New Event", button "Create Event")
- [x] Clicking an event in Week View / Day View / sidebar panel opens pre-filled modal in edit mode
- [x] Edit mode shows title "Edit Event" and button "Save Changes"
- [x] `submitEventForm()` does `POST /events` in create mode; `PUT /events/{id}` in edit mode
- [x] Local fallback if the backend is unavailable (creates/updates `EVENTS` in memory)
- [x] `renderUpcomingPanel()` filters events with `start_date >= now`, sorts by ascending `start_date`, shows the first 5 in the "Upcoming" panel
- [x] "Upcoming" panel rendered dynamically (replaced static HTML)
- [x] `loadEvents()` called on startup: tries `GET /events`; on failure uses example data in the new format
- [x] All views (Week, Day, Month) updated to use the new data model with `start_date`/`end_date`

---

## Fix #03 — Agenda: missing api.js + event creation + Day View

**Date:** 2 June 2026  
**Model:** GitHub Copilot (Claude Sonnet 4.6)

### What was fixed

| File | Change |
|---|---|
| `frontend/agenda.html` | Added `<script src="js/api.js"></script>` before the other scripts — it was missing, making `apiPost`/`apiGet` undefined and blocking all event operations |
| `frontend/js/modules/agenda.js` | `submitEventForm()` rewritten with **synchronous-first** logic: the event is added/edited in `EVENTS` immediately, the modal closes and views rebuild before any API call; the API call runs in the background (fire-and-forget) without blocking the UI |
| `frontend/js/modules/agenda.js` | `setView()` fixed: the `else` branch was treating "day" and "week" identically, always showing `#week-view` and never calling `buildDayView()`; replaced with three explicit branches (`month` / `day` / `week`) each with its own correct show/hide and call to the corresponding build function |

### Bugs fixed

- [x] Event creation was not working — `api.js` was not loaded in `agenda.html`
- [x] Local fallback also was not running — the error was synchronous, before the `.catch()`
- [x] `submitEventForm()` now applies the change locally immediately (without depending on async callbacks)
- [x] Day View was showing the same content as Week View — `setView()` never activated `#day-view` or called `buildDayView()`

---

## Task #08 — Notepad: Note List & Editor

**Date:** 2 June 2026  
**Model:** GitHub Copilot (Claude Sonnet 4.6)  
**Session:** Autonomous agent

### What was created / changed

| File | Change |
|---|---|
| `frontend/notepad.html` | Page restructured with two-panel layout: left panel (note list with title + truncated preview) and right panel (editor with toolbar); removed the stats block (words/chars/read time) and the previous Save/Clear buttons; added `.notepad-layout` block with `aside.notes-list-panel` (header with note count + `#notesList` list) and `section.notes-editor-panel` (empty state `#editorEmptyState` + content `#editorContent` with toolbar and editor); editor toolbar contains: status indicator (`#saveStatus`), word counter (`#wordCount`), Delete button and Save button; added `<script src="js/api.js"></script>` before the other scripts |
| `frontend/js/modules/notepad.js` | File rewritten from scratch; global state variables: `NOTES` (array), `_selectedNoteId`, `_localIdCounter`, `_isDirty`; `loadNotes()` tries `GET /notes` and on failure loads from `localStorage` (with 2 example notes if empty); `renderNoteList()` renders the left list items with title and truncated preview (80 chars), highlighting the active note; `selectNote(id)` populates the editor and shows the right panel; `newNote()` creates a blank note locally (with `POST /notes` in background), adds it to the top of the list and opens it in the editor; `saveNote()` updates `NOTES` and `localStorage` immediately, then does `PUT /notes/{id}` in background; `deleteNote()` with native `confirm()` — captures the `id` before nullifying it, removes from list, updates `localStorage` and calls `DELETE /notes/{id}` in background; `onEditorInput()` marks `_isDirty = true` and updates the word counter in real time; `setSaveStatus()` updates the indicator with ✓ icon (saved), "Saving…" or orange dot (unsaved); `persistLocal()` and `loadFromLocal()` manage `localStorage` persistence as fallback |
| `frontend/css/modules/notepad.css` | File rewritten: added classes `.notepad-main` (flex column, min-height calc), `.notepad-layout` (flex row, min-height 560px, border + radius + shadow), `.notes-list-panel` (width 280px, border-right, background surface-alt), `.notes-list-header`, `.notes-list-count`, `.notes-list-items` (overflow-y auto), `.note-list-item` (hover + active state with brand border-left), `.note-item-title`, `.note-item-preview`, `.notes-empty-msg`, `.notes-editor-panel` (flex: 1), `.editor-empty-state` (centred SVG + text), `.editor-content` (flex column), `.editor-toolbar` (space-between), `.editor-status`, `.editor-actions`, `.editor-wordcount`, `.btn-sm`, `.unsaved-dot`; internal editor styles maintained and adapted to flex |

### Criteria met (Task #08)

- [x] Two-panel layout: note list on the left, editor on the right
- [x] List shows title + truncated preview of each note
- [x] Active note highlighted with black border-left + white background
- [x] Empty state (SVG + message) when no note is selected
- [x] "New Note" button in the page header creates a blank note, opens it in the editor and focuses the title
- [x] `POST /notes` called on creation (with local fallback)
- [x] `PUT /notes/{id}` called on save (with local fallback)
- [x] `DELETE /notes/{id}` called on delete (with confirm + local fallback)
- [x] Word counter updated in real time (`oninput`)
- [x] Status indicator: "Unsaved changes" (orange dot) → "Saving…" → ✓ Saved
- [x] `localStorage` persistence as fallback when backend is unavailable
- [x] Responsive: on mobile the two panels stack vertically

---

## Task #09 — Mobile Responsiveness

**Date:** 8 June 2026
**Model:** Claude Sonnet 4.6
**Session:** Autonomous agent

### What was created / changed

| File | Change |
|---|---|
| `frontend/css/reset.css` | Added `overflow-x: hidden` on `html` and `body` to prevent horizontal scroll at the page level |
| `frontend/css/layout.css` | Added `overflow-x: hidden` on `.app-layout` and `min-width: 0` on `.main-content` (prevents flex child from expanding the container); replaced floating `.sidebar-toggle` with `.mobile-topbar` (fixed top bar, 54 px height, with integrated logo + hamburger button); added `.sidebar-backdrop` (semi-transparent dark overlay behind the open sidebar); `padding-top` of `.main-content` on mobile adjusted to `calc(54px + 20px)` to compensate for the topbar; modal redesigned as a bottom sheet on mobile (`align-items: flex-end`, `border-radius` only on top corners, `max-height: 90vh` with internal scroll); reduced `.auth-topbar` padding on mobile; added rules for landing page at 480 px (smaller photo, more compact stats card) |
| `frontend/js/router.js` | `toggleSidebar()` refactored to manage `.sidebar-backdrop`: creates the element via JS on startup, shows it when opening the sidebar and hides it when closing; click outside sidebar handler updated to also hide the backdrop |
| `frontend/css/modules/tasks.css` | At `≤640 px`: table converted to cards with CSS Grid (`grid-template-columns: auto minmax(0,1fr) auto`, 3 rows); checkbox and actions span all 3 rows; task name with `overflow-wrap: break-word`; status badge on row 2; due date visible on row 3; "Created" column hidden; action buttons with 36×36 px for touch comfort; search bar takes 100% on the first row; footer stacks vertically |
| `frontend/css/modules/agenda.css` | At `≤768 px`: `.agenda-layout` uses `minmax(0,1fr)` instead of `1fr` to prevent grid expansion beyond the viewport; `.calendar-wrap` with `overflow-x: auto` and `min-width: 0` (horizontal scroll contained within the card); week header and week grid with `min-width: 560 px`; smaller month cells; mini calendar in a row when there is space |
| `frontend/css/modules/notepad.css` | At `≤700 px`: layout changes to single-panel; by default only the list panel is visible; when selecting a note, the `.mobile-editor-open` class on `.notepad-layout` hides the list and shows only the editor; added `.mobile-back-btn` (hidden on desktop, visible on mobile) |
| `frontend/notepad.html` | Added "← Notes" button (class `mobile-back-btn`) in the editor toolbar, before the status indicator; replaced the standalone `<button class="sidebar-toggle">` with the new `<header class="mobile-topbar">` with integrated logo |
| `frontend/js/modules/notepad.js` | Added `mobileBackToList()` (removes `.mobile-editor-open` from layout) and `_mobileOpenEditor()` (adds the class when `window.innerWidth ≤ 700`); `selectNote()` and `newNote()` call `_mobileOpenEditor()` when opening the editor; `deleteNote()` calls `mobileBackToList()` after deletion |
| `frontend/tasks.html` | `<button class="sidebar-toggle">` replaced by `<header class="mobile-topbar">` with hamburger button + logo |
| `frontend/agenda.html` | Same |

### Criteria met (Task #09)

- [x] Sidebar opens over a dark backdrop on mobile; closing on the backdrop or outside the panel works
- [x] Fixed mobile topbar (54 px) with hamburger and logo on all app pages
- [x] Task table converts to readable cards on screens ≤ 640 px (name + status + date)
- [x] Weekly calendar scrolls horizontally within its card without causing page scroll
- [x] Notepad switches between list panel and editor panel on mobile ("← Notes" button)
- [x] Modal appears as bottom sheet on mobile (slides from the bottom of the screen)
- [x] No element causes horizontal page scroll (`overflow-x: hidden` on html/body/app-layout)

---

## Fix #04 — Stat Cards: CSS cascade bug

**Date:** 8 June 2026
**Model:** Claude Sonnet 4.6

### What was fixed

| File | Change |
|---|---|
| `frontend/css/components.css` | Added responsive media queries for stat cards **inside** `components.css`, immediately after the base definition: `≤1024 px → repeat(2,1fr)` and `≤480 px → 1fr`; padding and icon size reduced at `≤480 px` for better readability; on mobile the cards take 1 column (full width) |
| `frontend/css/layout.css` | Removed `stat-cards` rules from `layout.css` (they were being overridden by `components.css` which loads afterwards) |

### Bug fixed

`components.css` is loaded after `layout.css` in the HTML. Therefore the base rule `.stat-cards { grid-template-columns: repeat(4,1fr) }` in `components.css` was overriding the `layout.css` media queries at any screen width, even at 430 px. The solution was to move the media queries to `components.css`, after the base definition, ensuring they take priority in the cascade.

- [x] Stat cards show 2 columns on tablet (≤1024 px) and 1 column on mobile (≤480 px)
- [x] Cards are not cut off on iPhone screens (430 px)

---

## Task #10 — Files Page: Layout, New Panel & Upload Modal

**Date:** 8 June 2026  
**Model:** Claude Sonnet 4.6  
**Session:** Autonomous agent

### What was created / changed

| File | Change |
|---|---|
| `frontend/files.html` | Page created from scratch: standard sidebar with Files marked as active + count badge; main content with header ("Files" + subtitle + "+ New" button); body split into two panels — `files-content` (toolbar + breadcrumb + table + grid view) and `files-new-panel` (name field + 4 type cards + Create button); "Upload File" modal with drag-and-drop dropzone, File Name / Category / Description fields and Cancel / Upload File buttons; floating action menu per file (Rename / Download / Delete) |
| `frontend/css/modules/files.css` | File created from scratch (~280 lines): styles for `.files-body` (flex row), `.files-content` (card with border + shadow), `.files-toolbar` (search + view toggle), `.files-breadcrumb`, `.files-table` (list view with hover), `.file-icon` with colour variants by type (`fi-folder` orange, `fi-doc` blue, `fi-sheet` green, `fi-pdf` red, `fi-code` dark green, `fi-image` purple), `.files-grid` (auto-fill grid view), `.files-new-panel` (fixed right panel), `.type-card` (selectable with double border when active), `.upload-dropzone` (dashed border + drag-over state), `.file-actions-menu` (floating menu), `.nav-badge` (circular badge on nav link); breakpoints at 1024 px, 860 px and 600 px |
| `frontend/js/modules/files.js` | File created from scratch: `_files` array with 8 example entries marked with `example: true`; `renderFiles()` dispatches to `renderListView()` and `renderGridView()`; `setView()` toggles between list and grid with active button toggle; `filterFiles()` filters in real time by name; `selectType()` and `onNewNameInput()` manage the New panel state (Create button disabled until name + type are filled); `createItem()` calls `clearExamples()` on first creation and adds the new item to the top; `uploadFile()` same, detects type by file name extension; `openActionsMenu()` positions the floating menu next to the "..." button; `renameFile()` and `deleteFile()` store the `id` before calling `hideActionsMenu()` (avoids race with `_activeMenuFileId = null`); dropzone with `onDragOver`, `onDragLeave`, `onDrop` handlers; `updateNavBadge()` updates the badge with the total file count |
| `frontend/tasks.html` | Files nav link updated from `href="#"` to `href="files.html"` |
| `frontend/agenda.html` | Same |
| `frontend/notepad.html` | Same |

### Criteria met (Task #10)

- [x] Sidebar with Files active and badge with file count
- [x] List view with Name / Modified / Size columns and "..." button per row
- [x] Grid view with file cards (icon + name + meta)
- [x] List/grid toggle functional with active button highlighted
- [x] Real-time search by file name
- [x] Breadcrumb "All Files › My Files" (clickable to reset)
- [x] Coloured icons by file type (folder, doc, spreadsheet, pdf, code, image)
- [x] "New" panel always visible: name field + 4 selectable type cards + Create button
- [x] Create button disabled until name and type are filled
- [x] "Upload File" modal with dropzone (click + drag-and-drop), fields and Upload button
- [x] Upload detects file type by extension
- [x] "..." menu with Rename (native prompt), Download (stub) and Delete (native confirm)
- [x] Responsive: New panel moves below at ≤860 px; Modified/Size columns hidden at ≤600 px
- [x] Files nav links fixed on all pages

---

## Fix #05 — Files: delete and rename were not working

**Date:** 8 June 2026  
**Model:** Claude Sonnet 4.6

### What was fixed

| File | Change |
|---|---|
| `frontend/js/modules/files.js` | `deleteFile()` and `renameFile()` now store `_activeMenuFileId` in a local variable `id` **before** calling `hideActionsMenu()`, which was zeroing the global variable; without this fix, `_files.find(...)` received `null` and returned immediately without executing the action |

### Bug fixed

- [x] Delete and Rename in the "..." menu started working correctly after preserving the `id` before closing the menu

---

## Fix #06 — Files: clear examples when creating the first real item

**Date:** 8 June 2026  
**Model:** Claude Sonnet 4.6

### What was changed

| File | Change |
|---|---|
| `frontend/js/modules/files.js` | All example files now have `example: true` in the `_files` array; added `clearExamples()` function that filters `_files` removing all entries with `example: true`; `createItem()` and `uploadFile()` call `clearExamples()` before inserting the new item, ensuring examples disappear on first real use |

### Behaviour fixed

- [x] Example files are automatically removed when the user creates or uploads the first real file

---

## Task #11 — Authentication: Guard & "Remember Me"

**Date:** 18 June 2026  
**Model:** Claude Sonnet 4.6  
**Session:** Autonomous agent

### What was created / changed

| File | Change |
|---|---|
| `frontend/js/auth.js` | File rewritten from scratch (was empty): `checkAuth()` redirects to `login.html` if there is no token in `localStorage`; `logout()` clears `dn_token` and `dn_user_id` and redirects to login; `getInitials(name)` generates initials from the name; `loadSidebarUser()` does `GET /users/profile`, fills `#sidebarAvatar`, `#sidebarName`, `#sidebarEmail` with the real user data and calls `logout()` on error (invalid/expired token); `checkAuth()` and `loadSidebarUser()` run automatically on loading any app page |
| `frontend/login.html` | Added redirect to `tasks.html` if a token already exists (prevents double login); added IIFE `loadRemembered()` that fills email + password and activates the "Remember me" checkbox if there is saved data; `handleLogin()` updated to save/clear `dn_remember_email` and `dn_remember_pwd` in `localStorage` according to the checkbox state |
| `frontend/register.html` | Added redirect to `tasks.html` if a token already exists |
| `frontend/tasks.html` | Sidebar footer replaced: hardcoded `RD` avatar → `<a href="profile.html">` with dynamic `#sidebarAvatar / #sidebarName / #sidebarEmail`; added logout button with SVG icon and `onclick="logout()"`; added `<script src="js/auth.js"></script>` |
| `frontend/agenda.html` | Same |
| `frontend/files.html` | Same |
| `frontend/notepad.html` | Same |
| `frontend/css/layout.css` | `.sidebar-footer` with `gap: 6px` and `padding: 12px 16px`; added `.sidebar-user-link` (flex, hover, link without underline for profile), `.sidebar-user-meta` (min-width 0 to truncate long text), `.sidebar-logout-btn` (32×32 px, ghost, red hover) |

### Criteria met (Task #11)

- [x] All app pages check for token on startup — without token they redirect to login
- [x] Login and Register redirect to tasks.html if there is already an active session
- [x] "Remember me" saves email + password and pre-fills the form on the next visit
- [x] Sidebar shows real name, email and initials loaded from the API
- [x] Invalid/expired token → `loadSidebarUser()` calls `logout()` automatically
- [x] Logout button in the sidebar footer on all app pages

---

## Fix #07 — Tasks: status synchronisation between frontend and backend

**Date:** 18 June 2026  
**Model:** Claude Sonnet 4.6

### What was fixed

| File | Change |
|---|---|
| `backend/app/services/task_service.py` | `create_task()` now includes `status=data.status` when creating the model — the field was being ignored and the task was always created without status; `update_task()` now applies `task.status = data.status` if `data.status is not None` — status updates via `PUT` had no effect |
| `frontend/js/modules/tasks.js` | `statusMap` moved to the top of the file; added `dbToFrontend(s)` (converts `'Not-Started'` → `'not-started'`, etc.) and `frontendToDb(s)` (reverse conversion); `loadTasks()` uses `dbToFrontend(t.status)` when building each row — tasks loaded from the API always showed `not-started`; `markComplete()` passes `frontendToDb(newStatus)` to `apiPatch` — the backend was receiving `'completed'` instead of `'Completed'` and rejecting it; `submitCreateTask()` includes `status: frontendToDb(status)` in the `POST` and edit `PATCH` payload |

### Bugs fixed

- [x] Tasks created with a specific status always remained as `not-started` in the backend
- [x] Marking a task as complete was sending `'completed'` (frontend format) instead of `'Completed'` (backend format)
- [x] Editing a task did not persist status changes
- [x] On page reload, all tasks appeared as `not-started` regardless of the saved status

---

## Task #12 — Agenda: Dynamic Mini Calendar

**Date:** 18 June 2026  
**Model:** Claude Sonnet 4.6  
**Session:** Autonomous agent

### What was created / changed

| File | Change |
|---|---|
| `frontend/js/modules/agenda.js` | Added state variable `miniCalDate` (initialised to day 1 of the current month); added `buildMiniCal()` that dynamically generates the sidebar mini calendar: month/year title, 7 day name columns (M–S), grid with Monday-based offset, marking of days from other months (`.other-month`), today (`.today`), days with events (`.has-event`) and selected/active-week days (`.selected`); clicking a day calls `miniCalSelectDay(date)` which navigates the week/day view to the corresponding period and rebuilds the calendar; added `miniCalPrev()` and `miniCalNext()` to navigate the mini calendar independently from the main views; `buildMiniCal()` called in `rebuildViews()`, `loadEvents()` (after load and fallback) and `init()` |
| `frontend/agenda.html` | `<span class="mini-cal-title">May 2026</span>` replaced by `<span id="mini-cal-title"></span>` (populated by JS); mini calendar prev/next buttons with `onclick="miniCalPrev()"` and `onclick="miniCalNext()"`; static block of 35 `<div class="day-num">` removed and replaced by `<div class="mini-cal-grid" id="mini-cal-grid"></div>` |

### Criteria met (Task #12)

- [x] Mini calendar dynamically generated from the current month (not hardcoded for May 2026)
- [x] Month/year title automatically updated
- [x] Days with events marked with `.has-event`
- [x] Today marked with `.today`
- [x] Active week (week view) / active day (day view) marked with `.selected`
- [x] Clicking a day in the mini calendar navigates the main view to that day/week
- [x] Mini calendar arrows navigate its month independently from the main views
- [x] Mini calendar rebuilt whenever events are loaded or views are changed

---

## Task #13 — Profile Page / Account Settings

**Date:** 18 June 2026  
**Model:** Claude Sonnet 4.6  
**Session:** Autonomous agent

### What was created / changed

| File | Change |
|---|---|
| `frontend/profile.html` | Page created from scratch: standard sidebar with profile link and logout; main content with three cards — **Profile** (avatar with initials + name/email form), **Change Password** (new password + confirmation form with visibility toggle), **Danger Zone** (delete account button); account deletion confirmation modal; loads `auth.js` and `profile.js` |
| `frontend/js/modules/profile.js` | File created from scratch: IIFE `init()` does `GET /users/profile` and fills the form + header + sidebar, calling `logout()` on failure; `getInitials(name)` for the avatar; `updateProfileHeader()` and `updateSidebarMeta()` update the visual elements; `submitProfile(e)` does `PATCH /users/profile` with `{name, email}` and shows success/error message; `submitPassword(e)` validates minimum length (6 chars) and match before doing `PATCH /users/profile` with `{password}`; `confirmDeleteAccount()` does `DELETE /users/profile` and calls `logout()` on success |
| `frontend/css/components.css` | Added profile page styles: `.settings-content` (max-width 640px), `.settings-card` (card with border + shadow), `.settings-danger` (red border and title), `.profile-avatar-row` (flex with gap), `.avatar-lg` (56×56 px), `.profile-avatar-name`, `.profile-avatar-email`, `.btn-danger` (red), `.form-msg` with variants `.success` (green) and `.error` (red) |

### Criteria met (Task #13)

- [x] `profile.html` page accessible from the avatar in the sidebar footer (link on all pages)
- [x] Avatar, name and email loaded from the API (`GET /users/profile`) on startup
- [x] Profile form pre-filled with current data; `PATCH /users/profile` on submit
- [x] Inline success/error message on each form
- [x] Password change with validation (minimum 6 chars, matching confirmation)
- [x] Danger Zone with confirmation modal before deleting the account
- [x] Account deletion calls `DELETE /users/profile` and auto-logs out
- [x] Sidebar shows real user data instead of hardcoded `RD` / `Rodrigo Dias`

---

## Task #14 — Tasks: Priority Field

**Date:** 18 June 2026  
**Model:** Claude Sonnet 4.6  
**Session:** Autonomous agent

### What was created / changed

| File | Change |
|---|---|
| `backend/app/models/task_models.py` | Added field `priority: str = Field(default="medium", max_length=20)` to the `Task` model |
| `backend/app/schemas/task_schema.py` | Field `priority: str = "medium"` added to `TaskBase`; field `priority: Optional[str] = None` added to `TaskUpdate`; `TaskPublic` inherits automatically from `TaskBase` |
| `backend/app/services/task_service.py` | `create_task()` passes `priority=data.priority` when building the model; `update_task()` applies `task.priority = data.priority` if `data.priority is not None` |
| Database (PostgreSQL) | Column `priority VARCHAR(20) NOT NULL DEFAULT 'medium'` added to the `tasks` table via `ALTER TABLE` |
| `frontend/tasks.html` | `<th>Priority</th>` header added to the table (between Status and Due Date); static example row updated with `<td><span class="priority-badge medium">Medium</span></td>` |
| `frontend/js/modules/tasks.js` | Added `var priorityLabel` with mapping `{high, medium, low}`; `buildRow()` generates `<span class="priority-badge {priority}">` in the priority column; `loadTasks()` passes `priority: t.priority || 'medium'` when building each row (instead of hardcoded `'medium'`); `submitCreateTask()` includes `priority` in the `POST` and `PATCH` payload; edit mode updates the `.priority-badge` cell of the row after saving |
| `frontend/css/modules/tasks.css` | Added `.priority-badge` classes with colour variants: `.high` (light red background / red text), `.medium` (light yellow background / amber text), `.low` (light green background / green text); mobile layout updated — priority occupies row 3 of the card; "Due Date" hidden on mobile to keep the layout compact |

### Criteria met (Task #14)

- [x] `priority` field persisted in the database with default `"medium"`
- [x] API accepts `priority` on creation (`POST /tasks/`) and on edit (`PATCH /tasks/{id}`)
- [x] "Priority" column visible in the table between Status and Due Date
- [x] Coloured badge by level: red (High), amber (Medium), green (Low)
- [x] Create and edit modal was already sending the field; it is now effectively saved in the backend
- [x] "All priorities / High / Medium / Low" toolbar filter already existed and works with real data
- [x] When editing a task, the badge in the row is updated immediately without reload
- [x] Responsive: on mobile the priority badge appears in row 3 of the card

---

## Task #15 — Toast Notifications: Global Popup System

**Date:** 19 June 2026  
**Model:** Claude Sonnet 4.6  
**Session:** Autonomous agent

### What was created / changed

| File | Change |
|---|---|
| `frontend/js/toast.js` | File created from scratch: `toast` module (IIFE) with four public methods — `toast.success()`, `toast.error()`, `toast.warning()`, `toast.info()`; the `#dn-toast-container` is dynamically created in `<body>` on the first call; each toast is a `<div>` with SVG icon, message and ✕ button; animated progress bar (`@keyframes dn-progress`) with configurable duration (default 4 s); hover pauses the timer and animation; `transitionend` removes the element from the DOM after the exit animation; message escaped via `createTextNode` to prevent XSS |
| `frontend/css/components.css` | Added "Toast Notifications" section: `#dn-toast-container` fixed in the bottom-right corner with `z-index: 9999`, vertical stacking with `gap: 10px` and `pointer-events: none` (passes clicks to the background); `.dn-toast` with slide-in via `transform: translateX(calc(100% + 24px))` → `translateX(0)` + `opacity` (cubic-bezier with overshoot); `.dn-toast-hide` reverses the animation; coloured left border + icon colour + progress bar colour by type (`success` green, `error` red, `warning` orange, `info` blue); 480 px breakpoint — toast takes full screen width |
| `frontend/login.html` | Added `<script src="js/toast.js"></script>` (first script); `alert('Login failed…')` replaced by `toast.error(…)` |
| `frontend/register.html` | Added `<script src="js/toast.js"></script>` |
| `frontend/tasks.html` | Added `<script src="js/toast.js"></script>` |
| `frontend/agenda.html` | Added `<script src="js/toast.js"></script>` |
| `frontend/notepad.html` | Added `<script src="js/toast.js"></script>` |
| `frontend/files.html` | Added `<script src="js/toast.js"></script>` |
| `frontend/profile.html` | Added `<script src="js/toast.js"></script>` |
| `frontend/js/modules/validations.js` | Two `alert()` calls replaced by `toast.error()`: registration form validation error and registration failure via API |
| `frontend/js/modules/profile.js` | `alert('Failed to delete account…')` replaced by `toast.error(…)`; added `toast.success()` in `submitProfile()` (successful profile update) and `submitPassword()` (password updated); added `toast.error()` in the respective `.catch()` |
| `frontend/js/modules/tasks.js` | Added `toast.success('Task created.')` after successful creation and after local fallback; added `toast.success('Task updated.')` after editing in edit mode |

### Criteria met (Task #15)

- [x] Global system available on all app pages via `window.toast`
- [x] Four types: `success` (green), `error` (red), `warning` (orange), `info` (blue)
- [x] SVG icon per type, coloured left border and animated progress bar
- [x] Auto-dismiss after 4 s (configurable per call)
- [x] Hover pauses the timer and progress animation; on mouse leave resumes the remaining time
- [x] ✕ button closes the toast immediately
- [x] Multiple toasts stacked vertically, without blocking the UI (`pointer-events: none` on container)
- [x] Entry animation with smooth overshoot (cubic-bezier); fast exit (ease-in)
- [x] No `alert()` remaining anywhere in the frontend
- [x] Message escaped to prevent XSS
- [x] Responsive: takes full screen width on mobile (≤ 480 px)

---

## Fix #08 — Workspace: Work and Personal profiles with separate data

**Date:** 19 June 2026  
**Model:** Claude Sonnet 4.6

### What was fixed

| File | Change |
|---|---|
| `backend/app/services/task_service.py` | `get_tasks()` accepts optional `category` parameter; when provided, the query filters by `Task.category == category` |
| `backend/app/services/agenda_service.py` | `get_agendas()` same with `Agenda.category` |
| `backend/app/services/notepad_service.py` | `get_notepads()` same with `Notepad.category` |
| `backend/app/services/file_service.py` | `get_files()` same with `File.category` |
| `backend/app/routers/task_router.py` | `GET /tasks/` accepts `?category=` as query param (`Query(None)`); passes it to `get_tasks()` |
| `backend/app/routers/agenda_router.py` | `GET /agendas/` same |
| `backend/app/routers/notepad_router.py` | `GET /notepads/` same |
| `backend/app/routers/file_router.py` | `GET /files/` same |
| `frontend/js/router.js` | Added `getWorkspace()` that reads `localStorage.dn_workspace` (default `'Work'`); `toggleWorkspace()` now saves the choice in `dn_workspace` and calls `reloadWorkspace()` (if available on the page); IIFE `restoreWorkspacePill()` restores the active pill from `localStorage` on page load |
| `frontend/js/modules/tasks.js` | `loadTasks()` refactored to use `_fetchTasks()` that passes `?category=<workspace>` to the endpoint; added `reloadWorkspace()` that clears the table and re-loads the tasks of the active workspace; `submitCreateTask()` uses `getWorkspace()` as category when creating tasks (instead of hardcoded `'Personal'`) |
| `frontend/js/modules/agenda.js` | `loadEvents()` passes `?category=<workspace>` to the endpoint; added `reloadWorkspace()` that calls `loadEvents()`; `submitEventForm()` uses `getWorkspace()` as category when creating/editing events |
| `frontend/js/modules/notepad.js` | `loadNotes()` passes `?category=<workspace>` to the endpoint; added `reloadWorkspace()` that clears the selected note state and re-loads the notes; `_persistPendingNew()` uses `getWorkspace()` as category |
| `frontend/js/modules/files.js` | `loadFiles()` passes `?category=<workspace>` to the endpoint; added `reloadWorkspace()` that calls `loadFiles()`; `createItem()` uses `getWorkspace()` as category |

### Bug fixed

The Work/Personal toggle in the sidebar only changed the visual style of the pills (`.active` class) but had no effect on the data displayed — all modules loaded and created items without workspace distinction. The solution implemented a complete workspace separation cycle:

1. The active workspace is saved in `localStorage` (`dn_workspace`)
2. When switching workspace, `reloadWorkspace()` is called, reloading the filtered data from the backend
3. The backend filters results by the `category` field when the query param is provided
4. When creating items, the category matches the workspace active at the time of creation

- [x] Work and Personal show only their own data (tasks, events, notes, files)
- [x] Switching workspace immediately reloads the filtered data without page reload
- [x] Created items are associated with the active workspace at the time of creation
- [x] Pill state (Work/Personal) persists between navigations via `localStorage`
- [x] Backend: all listing endpoints accept `?category=` as an optional filter (backwards-compatible — without parameter returns all user items)

---

## Fix #09 — Remove example data for new users

**Date:** 19 June 2026  
**Model:** Claude Sonnet 4.6

### What was changed

| File | Change |
|---|---|
| `frontend/js/modules/agenda.js` | `loadEvents()` `.catch()` fallback changed: array of 8 example events (Team Meeting, Project Review, Lunch Break, etc.) replaced by `EVENTS = []`; the agenda now starts empty when the backend is unavailable |
| `frontend/js/modules/files.js` | `_files` array with 8 hardcoded example entries (Work Projects, Design Assets, Meeting Notes.doc, Q2 Report.xlsx, Brand Guidelines.pdf, index.tsx, Screenshots, App Mockup.png) replaced by `var _files = []`; comment in `loadFiles()` `.catch()` updated to remove mention of "keep example data" |
| `frontend/js/modules/notepad.js` | Block in the `loadNotes()` `.catch()` fallback that created 2 example notes ("Welcome to Notepad" and "Meeting notes") when `NOTES` was empty was removed; the notepad now starts with an empty list |

### Behaviour fixed

- [x] New users see all modules completely empty (no pre-filled data)
- [x] Agenda does not show fictional events when the backend is offline
- [x] Files does not show fictional files and folders when opening the page
- [x] Notepad does not automatically create welcome notes

---

## Task #16 — Files: Cloud Storage with size limits

**Date:** 19 June 2026  
**Model:** Claude Sonnet 4.6  
**Session:** Autonomous agent

### What was created / changed

| File | Change |
|---|---|
| `frontend/files.html` | "New" button (called `openUploadModal`) renamed to "Upload" with cloud upload icon (SVG); subtitle changed from "Manage your documents and folders" to "Your cloud storage"; storage bar added in the page header (`storage-bar-wrap` with track + fill + label "X used of 10 GB"); right sidebar panel `aside.files-new-panel` completely removed (contained name field, 4 type-cards and Create button); upload modal simplified — Category and Description fields removed, dropzone hint changed to "Max 1 GB per file" |
| `frontend/js/modules/files.js` | File rewritten: added constants `MAX_FILE_BYTES = 1 GB` and `MAX_TOTAL_BYTES = 10 GB`; added variables `_pendingFile` (reference to the selected File object) and `_usedBytes` (total bytes used in session); `applyDroppedFile(file)` validates `file.size > MAX_FILE_BYTES` before accepting — shows `toast.error` and cancels if exceeded; `uploadFile()` validates `_usedBytes + file.size > MAX_TOTAL_BYTES` before saving; on confirmation, adds `file.size` to `_usedBytes` and calls `updateStorageBar()`; `deleteFile()` subtracts `f.sizeBytes` from `_usedBytes` and updates the bar; `openUploadModal()` calls `resetUploadModal()` to clear pending state; added functions `formatBytes(bytes)` (formats B/KB/MB/GB with 1 decimal place), `guessType(name)` (detects type by extension), `updateStorageBar()` (calculates percentage and updates the DOM), `resetUploadModal()` (clears `_pendingFile`, input and dropzone text); removed all functions from the previous "New" flow (`selectType`, `onNewNameInput`, `updateCreateBtn`, `clearExamples`, `createItem`); `loadFiles()` updated to read `f.size_bytes` from the API, convert with `formatBytes()` and recalculate `_usedBytes` after loading |
| `frontend/css/modules/files.css` | Removed all New panel styles (`.files-new-panel`, `.new-panel-header`, `.new-panel-title`, `.new-panel-subtitle`, `.new-panel-body`, `.new-panel-field`, `.new-panel-label`, `.type-cards`, `.type-card`, `.type-card-icon`, `.icon-doc`, `.icon-sheet`, `.icon-folder`, `.icon-code`, `.type-card-text`, `.type-card-name`, `.type-card-desc`, `.new-panel-footer`, `.new-create-btn`); added storage bar styles: `.storage-bar-wrap` (flex row + gap), `.storage-bar-track` (200 px, 6 px height, border-radius), `.storage-bar-fill` (brand colour background, smooth width transition), `.storage-label` (muted text, nowrap); responsive breakpoints updated — removed references to the New panel; `.storage-bar-track` reduced to 120 px at `≤600 px` |

### Criteria met (Task #16)

- [x] "Upload" button in the header opens the upload modal (without "New" side panel)
- [x] Storage bar visible in the header: "X used of 10 GB"
- [x] Individual file validation: rejects files > 1 GB with `toast.error`
- [x] Total storage validation: rejects upload if total exceeds 10 GB
- [x] `_usedBytes` updated on upload and on file deletion
- [x] `formatBytes()` formats the size in B, KB, MB or GB with 1 decimal place
- [x] File size displayed in the dropzone after selection ("name.ext (X.X MB)")
- [x] "Size" column in the table filled with the real file size after upload
- [x] "New" panel with type-cards completely removed from HTML and CSS
- [x] Simplified modal: dropzone + name field only (no Category/Description)

---

## Task #17 — Animations: Global System with Framer Motion

**Date:** 19 June 2026  
**Model:** Claude Sonnet 4.6  
**Session:** Autonomous agent

### What was created / changed

| File | Change |
|---|---|
| `frontend/css/animations.css` | File created from scratch (~444 lines): keyframes `dn-fade-up`, `dn-fade-down`, `dn-fade-left`, `dn-pop-in`, `dn-dot-pulse`, `dn-shimmer`; landing page entry animations (topbar, eyebrow, h1, desc, actions, divider, right panel, stats card, panel); auth page entry animations (topbar, card); modal override — `display:flex !important` + `visibility:hidden/opacity:0` + transitions to allow open AND close animation without touching JS; hover effects for all interactive elements (btns, nav links, stat cards, settings cards, action btns, workspace pills, avatar, pagination, nav arrows, view toggles, upload dropzone, storage bar, note items, week events, mini cal days, file action items, sidebar logout); initial hidden states for staggered elements (`.stats-item`, `#about h2/p`); `prefers-reduced-motion` support |
| `frontend/js/animations.js` | File created from scratch (ES module): imports `animate`, `inView`, `stagger` from `https://esm.sh/framer-motion@11`; easing presets (`ease`, `spring`, `springB`); landing page block: stagger of stats items, `inView('#about')` for scroll reveal of paragraphs, press feedback on buttons; auth block: stagger of form fields with `startDelay: 0.3`, press feedback on submit button; app pages block: sidebar slide x, sidebar-footer y, nav links stagger x, workspace pills scale stagger, page-header y, stat cards stagger y+scale, task section y, agenda layout (toolbar+calendar+mini panels), notepad (list+editor), files (toolbar+content), settings cards stagger, press feedback on all `.btn`, workspace toggle bounce `scale:[0.9,1.06,1]`, action buttons spring |
| `frontend/index.html` | Added `<link>` and `<script type="module">` for `animations.css` and `animations.js` |
| `frontend/login.html` | Same |
| `frontend/register.html` | Same |
| `frontend/tasks.html` | Same |
| `frontend/agenda.html` | Same |
| `frontend/notepad.html` | Same |
| `frontend/files.html` | Same |
| `frontend/profile.html` | Same |

### Criteria met (Task #17)

- [x] Entry animations (fade-up/down/left, pop-in) on all 8 pages
- [x] Stagger on lists: nav links, stat cards, form fields, settings cards, workspace pills
- [x] Scroll reveal with `inView` on the "About" section of the landing page
- [x] Hover micro-interactions on all interactive elements (lift, slide, scale, spring)
- [x] Press feedback on buttons with spring physics
- [x] Modal with open AND close animation via CSS `visibility/opacity` (without changing JS)
- [x] `<script type="module">` executes after classic scripts — no conflict with app.js/auth.js
- [x] `prefers-reduced-motion` cancels all durations
- [x] Framer Motion v11 via CDN ESM (no npm, no build step)

---

## Task #18 — Landing Page: Carousel with 5 Slides and Auto-rotation

**Date:** 19 June 2026  
**Model:** Claude Sonnet 4.6  
**Session:** Autonomous agent

### What was created / changed

| File | Change |
|---|---|
| `frontend/index.html` | `.landing-panel` restructured: static content replaced by `<div class="slider-track" id="sliderTrack">` with 5 `<div class="slide">` (Tasks, Agenda, Notepad, Files, Workspaces), each with label, `<h3>` and descriptive `<p>`; dots updated with `data-index="0"…"4"` attributes; buttons with `id="sliderPrev"` and `id="sliderNext"`; added IIFE carousel script with 5 s auto-rotation, prev/next navigation, dot click, pause on hover |
| `frontend/css/animations.css` | Added carousel styles: `.slider-track` with `position:relative; min-height:138px; overflow:hidden`; `.slide` absolute with `opacity:0; pointer-events:none; transform:translateY(10px)`; `.slide.active` visible with cubic-bezier transition; `.slide.leaving` with fast exit `translateY(-8px)`; `.slider-dot` with `cursor:pointer` and width/colour transition |

### Criteria met (Task #18)

- [x] 5 slides with unique content per app module (Tasks, Agenda, Notepad, Files, Workspaces)
- [x] Auto-rotation every 5 seconds via `setInterval`
- [x] Functional prev/next arrows with timer reset
- [x] Clickable dots with direct navigation to any slide
- [x] Entry animation (fade-up) and exit animation (fade-up upwards) with CSS classes `.active`/`.leaving`
- [x] `.leaving` class cleanup after 300 ms via `setTimeout`
- [x] Automatic pause on hover over the panel; resumes on `mouseleave`
- [x] Active dot with continuous pulse animation (`dn-dot-pulse`)

---

## Task #19 — "See how it works" Page

**Date:** 19 June 2026  
**Model:** Claude Sonnet 4.6  
**Session:** Autonomous agent

### What was created / changed

| File | Change |
|---|---|
| `frontend/how-it-works.html` | Page created from scratch (standalone marketing page, without sidebar): sticky topbar with blur backdrop + logo + nav links + CTA buttons; hero with "How it works" badge + H1 + subtitle + CTAs; "3 steps" section (create account, choose workspace, start organising) with numbered cards; 5 feature sections (Tasks, Agenda, Notepad, Files, Workspaces) in two-column alternating layout (`.feature-row` and `.feature-row.flip` with `direction:rtl`); visual mockups for each module — Tasks (table with rows, checkboxes, status and priority badges), Agenda (weekly grid with coloured events), Notepad (two panels: list + editor), Files (table with type icons + storage bar), Workspaces (interactive demo card with Work/Personal pills); stats section (12k+ users, 98% uptime, 4.9★, 0 integrations); dark CTA section; footer; scroll reveal with IntersectionObserver on 28 `[data-reveal]` elements; Framer Motion for press feedback on buttons and click animation on workspace demo pills; "See how it works" link in `index.html` changed from `href="#about"` to `href="how-it-works.html"` |
| `frontend/css/howto.css` | File created from scratch (~420 lines) after extraction from inline `<style>` block: base styles, scroll-reveal utility, topbar, common sections, hero, steps grid, feature rows, mockup windows (tasks, agenda, notepad, files), workspace section (dark), stats grid, CTA section, footer; breakpoints at 960 px and 540 px |

### Criteria met (Task #19)

- [x] Standalone page accessible at `how-it-works.html` (without sidebar, without auth guard)
- [x] "See how it works" link on the landing page points to the new page
- [x] Sticky topbar with backdrop blur, logo and Login/Sign up buttons
- [x] 3 onboarding steps with numbered cards and coloured icons
- [x] 5 feature sections with text + visual mockup (alternating left/right layout)
- [x] Pixel-perfect mockups for Tasks, Agenda, Notepad, Files and Workspaces
- [x] Interactive Workspaces demo card (clickable pills with Framer Motion animation)
- [x] Smooth scroll reveal (`[data-reveal]` + IntersectionObserver + delays via `data-delay`)
- [x] Press feedback on CTAs with Framer Motion
- [x] Stats section, dark CTA and footer with links
- [x] Responsive at 960 px (columns stack) and 540 px (font and layout adjustments)
- [x] CSS extracted to separate file `css/howto.css`

---

## Fix #10 — how-it-works.html: extraction of inline CSS to separate file

**Date:** 19 June 2026  
**Model:** Claude Sonnet 4.6

### What was changed

| File | Change |
|---|---|
| `frontend/css/howto.css` | File created with all the CSS that was in the inline `<style>` block of `how-it-works.html` (861 lines → dedicated file in the `css/` folder) |
| `frontend/how-it-works.html` | `<style>…</style>` block (lines 11–873) removed; replaced by `<link rel="stylesheet" href="css/howto.css" />` in the `<head>` |

### Behaviour after fix

- [x] `how-it-works.html` no longer has inline CSS — all styling is in `css/howto.css`
- [x] No visual changes — the CSS is exactly the same, just moved to a different file
- [x] File permissions fixed (the `sed -i` had created the file with 0400; recreated with 0644 via Python for Nginx to be able to read)

---

## Backend — AI Usage

### Project Overview and AI Integration

AI was primarily used as an auxiliary tool throughout the entire codebase, serving to better understand certain logic, navigate application flows, and debug errors.

### Frontend and Backend Integration

AI played a direct role in the code within the Docker Compose setup to connect the frontend and backend services. Although I initially needed assistance, I was able to successfully configure it by combining AI guidance with Stack Overflow resources.

On the frontend, AI was heavily utilized within the JavaScript codebase to accelerate the understanding of existing code and to manipulate its functions effectively. It was used interchangeably to generate, correct, and explain code.

### Core Architecture and Database Management

AI was deeply integrated into the development of the core, models, schemas, services, and routers, as well as the Docker Compose file. It helped set up the database, configurations, and various other components.

Additionally, AI helped me decide between using the VS Code PostgreSQL extension or pgAdmin. I ultimately chose pgAdmin because the VS Code extension was not working well for my workflow, making pgAdmin the better choice for the time being.

The initial idea for working with PostgreSQL came from a TikTok video. From there, I began modifying the code to fit my specific tables. However, the implementation shown in the video did not scale well for multiple tables and complex relationships. To resolve this, I used AI to fix imports, correct endpoints, and resolve errors within the models and schemas.

### Project Structure and Data Flow

The AI suggested the following project structure:

```
project/
│
├── core/
│   └── database.py        ← Engine, SessionLocal, Base
│
├── models/
│   └── user.py            ← SQLAlchemy ORM models
│
├── schemas/
│   └── user.py            ← Pydantic request/response models
│
├── services/
│   ├── user_service.py    ← Business logic (uses CRUD)
│
└── routers/
    └── user.py            ← API endpoints
```

### Execution Progression

The correct data flow and request progression follow this sequence:

```
Router → Schema (Validation) → Service (Queries) → Model (Structure) → Database
```

### Reference Material and Resources

The following documentation and Stack Overflow resources were utilized during development to address specific configuration and validation requirements:

- Multiple Dockerfile configs — https://stackoverflow.com/questions/27409761/docker-multiple-dockerfiles-in-project
- Register validations (password strength) — https://stackoverflow.com/questions/5142103/regex-to-validate-password-strength
- Register validations (email) — https://stackoverflow.com/questions/46155/how-can-i-validate-an-email-address-in-javascript

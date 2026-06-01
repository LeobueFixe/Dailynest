/* ============================================================
   Agenda — Month View
   ============================================================ */

/* ── Sample Events ──────────────────────────────────────── */
const EVENTS = [
  { id: 1, title: 'Team Meeting',    date: '2026-06-01', time: '9:00',  color: 'blue'   },
  { id: 2, title: 'Project Review',  date: '2026-06-05', time: '10:00', color: 'yellow' },
  { id: 3, title: 'Lunch Break',     date: '2026-06-05', time: '12:00', color: 'green'  },
  { id: 4, title: 'Client Call',     date: '2026-06-10', time: '14:00', color: 'purple' },
  { id: 5, title: 'Sprint Planning', date: '2026-06-15', time: '9:30',  color: 'blue'   },
  { id: 6, title: 'Design Review',   date: '2026-06-20', time: '11:00', color: 'yellow' },
  { id: 7, title: '1:1 Meeting',     date: '2026-06-22', time: '16:00', color: 'green'  },
  { id: 8, title: 'Release Demo',    date: '2026-06-28', time: '15:00', color: 'purple' },
];

/* ── State ──────────────────────────────────────────────── */
let monthViewDate = new Date();
monthViewDate.setDate(1);
let selectedDay   = null;
let currentView   = 'week';

/* ── View toggle ────────────────────────────────────────── */
function setView(btn) {
  var parent = btn.closest('.view-toggle');
  if (!parent) return;
  parent.querySelectorAll('button').forEach(function (b) { b.classList.remove('active'); });
  btn.classList.add('active');

  var view = btn.textContent.trim().toLowerCase();
  currentView = view;

  var weekView      = document.getElementById('week-view');
  var monthView     = document.getElementById('month-view');
  var miniCalPanel  = document.getElementById('mini-cal-card');
  var upcomingPanel = document.getElementById('upcoming-panel');
  var dayEvtPanel   = document.getElementById('day-events-panel');

  if (view === 'month') {
    if (weekView)      weekView.style.display      = 'none';
    if (monthView)     monthView.style.display     = '';
    if (miniCalPanel)  miniCalPanel.style.display  = 'none';
    if (upcomingPanel) upcomingPanel.style.display = 'none';
    if (dayEvtPanel)   dayEvtPanel.style.display   = '';
    buildMonthGrid();
  } else {
    if (weekView)      weekView.style.display      = '';
    if (monthView)     monthView.style.display     = 'none';
    if (miniCalPanel)  miniCalPanel.style.display  = '';
    if (upcomingPanel) upcomingPanel.style.display = '';
    if (dayEvtPanel)   dayEvtPanel.style.display   = 'none';
  }
}

/* ── Build month grid ───────────────────────────────────── */
function buildMonthGrid() {
  var year  = monthViewDate.getFullYear();
  var month = monthViewDate.getMonth();

  var titleEl = document.getElementById('month-nav-title');
  if (titleEl) {
    titleEl.textContent = monthViewDate.toLocaleDateString('en-US', { month: 'long', year: 'numeric' });
  }

  var grid = document.getElementById('month-grid-body');
  if (!grid) return;
  grid.innerHTML = '';

  var today     = new Date();
  var firstDay  = new Date(year, month, 1);
  var lastDate  = new Date(year, month + 1, 0).getDate();

  // Monday-based offset (0=Mon … 6=Sun)
  var startDow = firstDay.getDay();
  startDow = startDow === 0 ? 6 : startDow - 1;

  var totalCells = Math.ceil((startDow + lastDate) / 7) * 7;

  for (var i = 0; i < totalCells; i++) {
    var dayOffset  = i - startDow;
    var cellDate   = new Date(year, month, 1 + dayOffset);
    var cellMonth  = cellDate.getMonth();
    var cellDay    = cellDate.getDate();
    var cellYear   = cellDate.getFullYear();
    var dateStr    = cellYear + '-' +
                     String(cellMonth + 1).padStart(2, '0') + '-' +
                     String(cellDay).padStart(2, '0');

    var isToday         = cellDate.toDateString() === today.toDateString();
    var isCurrentMonth  = cellMonth === month;
    var isSelected      = selectedDay === dateStr;
    var dayEvents       = EVENTS.filter(function (e) { return e.date === dateStr; });

    var cls = 'month-day-cell';
    if (!isCurrentMonth) cls += ' other-month';
    if (isToday)         cls += ' is-today';
    if (isSelected)      cls += ' is-selected';

    var dotsHtml = dayEvents.slice(0, 3).map(function (e) {
      return '<span class="event-dot ' + e.color + '"></span>';
    }).join('');

    var cell = document.createElement('div');
    cell.className       = cls;
    cell.dataset.date    = dateStr;
    cell.innerHTML =
      '<div class="month-day-num">' + cellDay + '</div>' +
      '<div class="month-day-dots">' + dotsHtml + '</div>';

    (function (ds, cd) {
      cell.addEventListener('click', function () { selectDay(ds, cd); });
    }(dateStr, cellDate));

    grid.appendChild(cell);
  }
}

/* ── Select day ─────────────────────────────────────────── */
function selectDay(dateStr, date) {
  selectedDay = dateStr;
  buildMonthGrid();

  var panel = document.getElementById('day-events-panel');
  if (!panel) return;

  var titleEl = panel.querySelector('.day-events-title');
  var listEl  = panel.querySelector('.day-events-list');

  if (titleEl) {
    titleEl.textContent = date.toLocaleDateString('en-US', {
      weekday: 'long', day: 'numeric', month: 'long'
    });
  }

  var dayEvents = EVENTS.filter(function (e) { return e.date === dateStr; });

  if (listEl) {
    if (dayEvents.length === 0) {
      listEl.innerHTML = '<p class="no-events-msg">No events for this day.</p>';
    } else {
      listEl.innerHTML = dayEvents.map(function (e) {
        var solid = { blue: '#3b82f6', yellow: '#f59e0b', green: '#22c55e', purple: '#a855f7' };
        return '<div class="day-event-item">' +
          '<div class="upcoming-event-dot" style="background:' + (solid[e.color] || '#999') + ';"></div>' +
          '<div>' +
            '<div class="upcoming-event-name">' + e.title + '</div>' +
            '<div class="upcoming-event-time">' + e.time + '</div>' +
          '</div>' +
        '</div>';
      }).join('');
    }
  }
}

/* ── Month navigation ───────────────────────────────────── */
function prevMonth() {
  monthViewDate.setMonth(monthViewDate.getMonth() - 1);
  selectedDay = null;
  buildMonthGrid();
  resetDayPanel();
}

function nextMonth() {
  monthViewDate.setMonth(monthViewDate.getMonth() + 1);
  selectedDay = null;
  buildMonthGrid();
  resetDayPanel();
}

function resetDayPanel() {
  var panel = document.getElementById('day-events-panel');
  if (!panel) return;
  var titleEl = panel.querySelector('.day-events-title');
  var listEl  = panel.querySelector('.day-events-list');
  if (titleEl) titleEl.textContent = 'Select a day';
  if (listEl)  listEl.innerHTML    = '<p class="no-events-msg">Click on a day to see its events.</p>';
}

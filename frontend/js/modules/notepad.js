/* ── Notepad ────────────────────────────────────────────── */
(function initNotepad() {
  var noteTitle = document.getElementById('noteTitle');
  var noteBody  = document.getElementById('noteBody');
  if (!noteTitle && !noteBody) return;

  // Restore saved content
  var savedTitle = localStorage.getItem('dn_note_title');
  var savedBody  = localStorage.getItem('dn_note_body');
  if (noteTitle && savedTitle) noteTitle.value = savedTitle;
  if (noteBody  && savedBody)  noteBody.value  = savedBody;

  function updateStats() {
    if (!noteBody) return;
    var text  = noteBody.value.trim();
    var words = text ? text.split(/\s+/).length : 0;
    var chars = noteBody.value.length;
    var read  = Math.max(1, Math.ceil(words / 200));

    var set = function (id, v) { var el = document.getElementById(id); if (el) el.textContent = v; };
    set('wordCount', words);
    set('charCount', chars);
    set('readTime',  words === 0 ? 0 : read);

    var saveStatus = document.getElementById('saveStatus');
    if (saveStatus) {
      saveStatus.innerHTML = '<span class="unsaved-dot"></span> Unsaved changes';
    }
  }

  if (noteBody)  noteBody.addEventListener('input',  updateStats);
  if (noteTitle) noteTitle.addEventListener('input', updateStats);

  // Run once on load to update stats if restored
  updateStats();

  // Save
  var saveBtn = document.getElementById('saveNoteBtn');
  if (saveBtn) {
    saveBtn.addEventListener('click', function () {
      var title = noteTitle ? noteTitle.value : '';
      var body  = noteBody  ? noteBody.value  : '';
      localStorage.setItem('dn_note_title', title);
      localStorage.setItem('dn_note_body',  body);

      var saveStatus = document.getElementById('saveStatus');
      if (saveStatus) {
        saveStatus.innerHTML = '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle"><polyline points="20 6 9 17 4 12"/></svg> Saved';
      }
    });
  }

  // Clear
  var clearBtn = document.getElementById('clearNoteBtn');
  if (clearBtn) {
    clearBtn.addEventListener('click', function () {
      if (!window.confirm('Clear the note? This cannot be undone.')) return;
      if (noteTitle) noteTitle.value = '';
      if (noteBody)  noteBody.value  = '';
      localStorage.removeItem('dn_note_title');
      localStorage.removeItem('dn_note_body');
      updateStats();
      var saveStatus = document.getElementById('saveStatus');
      if (saveStatus) saveStatus.textContent = 'Not saved yet';
    });
  }
})();

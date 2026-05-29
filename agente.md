# Agente — Task #01: Task List UI — Layout & Sidebar
# DailyNest · Design Real (Figma Screenshots)

## Contexto do Projeto
**Projecto:** DailyNest  
**Responsável:** Rodrigo — Frontend  
**Stack:** HTML + CSS + JS (sem frameworks externos)  
**Fase:** 2 · **Prioridade:** 🔴 High · **Categoria:** Must Do · **Estimativa:** 5h  

---

## DESIGN SYSTEM — Extraído do Figma

### Paleta de Cores
```css
:root {
  /* Brand */
  --color-brand:        #1a1a1a;   /* preto quase puro — botões primários, nav activa */
  --color-brand-text:   #ffffff;

  /* Backgrounds */
  --color-bg:           #f5f5f5;   /* fundo geral da app (cinza muito claro) */
  --color-surface:      #ffffff;   /* cards, sidebar, modais */
  --color-surface-alt:  #f8f8f8;   /* fundo alternativo leve */

  /* Borders */
  --color-border:       #e5e5e5;   /* bordas padrão */
  --color-border-light: #eeeeee;

  /* Text */
  --color-text:         #1a1a1a;   /* títulos e texto principal */
  --color-text-secondary: #6b7280; /* subtítulos, labels */
  --color-text-muted:   #9ca3af;   /* placeholders, meta-info */

  /* Nav / Sidebar */
  --color-nav-active-bg:   #1a1a1a;  /* pill preto quando activo */
  --color-nav-active-text: #ffffff;
  --color-nav-idle-text:   #374151;

  /* Accent — apenas no header azul do topbar */
  --color-topbar-accent:   #3b82f6;  /* linha azul no topo do login/signup */

  /* Status colors (task badges) */
  --status-not-started-bg:   #f3f4f6;
  --status-not-started-text: #6b7280;
  --status-not-started-dot:  #9ca3af;

  --status-in-progress-bg:   #fff7ed;
  --status-in-progress-text: #ea580c;
  --status-in-progress-dot:  #f97316;

  --status-completed-bg:     #f0fdf4;
  --status-completed-text:   #16a34a;
  --status-completed-dot:    #22c55e;

  /* Stat card icons */
  --icon-all-tasks:      #3b82f6;   /* azul */
  --icon-not-started:    #6b7280;   /* cinza */
  --icon-in-progress:    #f97316;   /* laranja */
  --icon-completed:      #22c55e;   /* verde */

  /* Agenda event colors */
  --event-blue:    #dbeafe;  /* Team Meeting */
  --event-yellow:  #fef9c3;  /* Project Review */
  --event-green:   #dcfce7;  /* Lunch Break */
  --event-purple:  #ede9fe;  /* Client Call */

  /* Layout */
  --sidebar-width:   284px;
  --topbar-height:   72px;

  /* Typography */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

  /* Radius */
  --radius-sm:   6px;
  --radius:      10px;
  --radius-md:   12px;
  --radius-lg:   16px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-card: 0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.04);
  --shadow-modal: 0 20px 60px rgba(0,0,0,0.15);
}
```

### Tipografia
- **Font:** Inter (Google Fonts)
- **Logo:** "Daily**nest**" — "Daily" bold, "nest" regular — tamanho ~22px
- **Títulos de página:** `font-size: 2rem; font-weight: 700;` (ex: "Tasks", "Notepad", "Agenda")
- **Subtítulos:** `font-size: 0.875rem; color: var(--color-text-secondary);`
- **Body:** `font-size: 0.9375rem;`
- **Labels uppercase:** `font-size: 0.75rem; font-weight: 600; letter-spacing: 0.06em; color: var(--color-text-muted);` (ex: "WORKSPACE", "NAVIGATION", "TASK NAME", "STATUS")

---

## Páginas a Implementar

### 1. Landing Page (`index.html`)

**Layout:** Split-screen horizontal
- **Esquerda (44%):** fundo branco
  - Topbar: logo DailyNest + botões "Login" (ghost) e "Sign up free" (preto, rounded-full)
  - Eyebrow: `PRODUCTIVITY · SIMPLIFIED` em uppercase pequeno cinza
  - H1: `"One nest for every task."` — bold, ~3.5rem, preto
  - Subtítulo: `"Tasks, agenda, notes, and files — all in one focused workspace. Stop juggling apps."`
  - Botões: `"Get started →"` (preto, pill) + `"See how it works"` (link azul sublinhado)
  - Divisória horizontal cinza
  - Secção About us: título + 5 parágrafos separados por linhas
- **Direita (56%):** imagem de fundo (laptop/secretária, tom escuro)
  - Overlay de stats: 3 badges `12k+ Active users`, `98% Uptime`, `4.9★ Avg. rating`
  - Painel preto em baixo: label "TASKS" uppercase + "Stay ahead of everything." + descrição
  - Dots de navegação + setas `<` `>` em baixo à direita

---

### 2. Login Page (`login.html`)

**Layout:** Página branca, topbar com linha azul no topo (`border-top: 3px solid #3b82f6`)
- Topbar: logo DailyNest à esquerda, sem outros elementos
- Linha divisória horizontal abaixo do topbar
- Card centrado (max-width: 420px, padding 40px, border-radius: 16px, box-shadow leve)
  - Título: `"Login"` — bold, ~2rem
  - Campo Email: ícone envelope + placeholder "Enter your email"
  - Campo Password: ícone cadeado + placeholder "Create a password" + ícone olho à direita
  - Row: checkbox "Remember me" + link "Forgot Password?" à direita
  - Botão: `"Login"` — preto, full-width, border-radius: 10px
  - Link em baixo: `"Don't have an account? Sign up"` — "Sign up" em bold

---

### 3. Register Page (`register.html`)

**Layout:** Idêntico ao Login mas com mais campos
- Card centrado
  - Título: `"Create Account"`
  - Subtítulo: `"Sign up to get started with your account."`
  - Campo Username: ícone pessoa
  - Campo Email: ícone envelope
  - Campo Password: ícone cadeado + olho
  - Campo Confirm Password: ícone cadeado + olho
  - Checkbox: `"I accept the Privacy Policy"` — "Privacy Policy" sublinhado
  - Botão: `"Create Account"` — preto, full-width
  - Link: `"Already have an account? Sign in"` — "Sign in" bold

---

### 4. Tasks Page (`tasks.html`) ← FOCO PRINCIPAL da Task #01

**Layout:** Sidebar fixa à esquerda + conteúdo principal

#### SIDEBAR (284px, fundo branco, border-right)
```
Logo DailyNest (topo, padding 24px)
─────────────────────────────────────
WORKSPACE  ← label uppercase cinza muted
[ Work ]  [ Personal ]  ← pills toggle, Work = preto activo
─────────────────────────────────────
NAVIGATION  ← label uppercase cinza muted
[■] Tasks    ← pill preto (activo)
[▣] Agenda
[▤] Notepad
[□] Files
─────────────────────────────────────
(bottom) Avatar circular "RD" + "Rodrigo Dias" + "rodrigoDias@gmail.com"
```

#### MAIN CONTENT
**Topbar do conteúdo:**
- H1: `"Tasks"` (bold, 2rem)
- Subtítulo: `"Manage and track your daily tasks"`
- Botão top-right: `"+ New Task"` (preto, border-radius: 10px)

**Stat Cards Row (4 cards, iguais em largura):**
| Card | Ícone (fundo colorido, radius: 12px) | Número | Label |
|------|--------------------------------------|--------|-------|
| All tasks | azul (clipboard) | 1 | All tasks |
| Not started | cinza (circle) | 1 | Not started |
| In progress | laranja (circle-dashed) | 0 | In progress |
| Completed | verde (checkmark) | 0 | Completed |

**Task Table Section (border azul dashed — nota de design no Figma):**
- Search bar: `🔍 Search tasks...` + 2 dropdowns à direita (sem label visível no mockup)
- Table headers uppercase cinza: `TASK NAME · STATUS · DUE DATE · CREATED`
- Task row exemplo:
  - **New Task** (título)
  - `● Not started` (ponto cinza + texto)
  - `📅 Today` (ícone calendário + texto)
  - `Just now` (timestamp)
- Footer: `Showing 1 of 1 tasks` + paginação `< 1 >`

**Modal "Create New Task"** (trigger: botão "+ New Task"):
- Overlay escuro atrás
- Card branco centrado (max-width: 500px)
- Título `"Create New Task"` + X para fechar
- Campos: TASK NAME (input full), STATUS (dropdown, metade), PRIORITY (dropdown, metade), DUE DATE (input full), DESCRIPTION (textarea)
- Botões: `Cancel` (ghost) + `Create Task` (preto)

---

### 5. Notepad Page (`notepad.html`)

**Topbar conteúdo:**
- H1: `"Notepad"`
- Meta: `🕐 Not saved yet  ● Unsaved changes`
- Botões: `🗑 Clear` (ghost, borda cinza) + `💾 Save Note` (preto)

**Stats bar (abaixo do topbar):**
`T 0 words | ≡ 0 characters | 🕐 0 min read`

**Editor area (card branco com border azul — design Figma):**
- Campo título: `"Untitled Note"` (placeholder cinza claro, font grande ~2rem)
- Linha divisória
- Área de texto: `"Start writing your thoughts..."` (placeholder)
- Altura mínima: ~500px

---

### 6. Agenda Page (`agenda.html`)

**Topbar conteúdo:**
- Navegação: `<` `>` + H1: `"Agenda"` 
- Data range: `📅 20 – 26 maio de 2026`
- Botão: `"+ New Event"` (preto)
- Toggle views: `Dia | Semana | Mês` (Semana activo com underline/destaque)

**Layout 3 colunas:**
1. **Grelha de horas** (coluna estreita, labels 7:00–17:00+)
2. **Calendário semanal** (7 colunas — S T Q Q S S D, datas)
   - Dia actual (20) = círculo preto com número branco
   - Eventos coloridos posicionados por hora:
     - `Team Meeting 9:00` — azul claro
     - `Project Review 10:00` — amarelo claro (na quarta-feira)
     - `Lunch Break 12:00` — verde claro
     - `Client Call 14:00` — roxo claro
3. **Mini calendário** (direita) — mês Maio 2026 + secção "PRÓXIMOS" com lista de eventos

---

## Estrutura de Ficheiros

```
dailynest/
├── index.html        ← Landing page
├── login.html        ← Auth: Login
├── register.html     ← Auth: Register
├── tasks.html        ← App: Task List (FOCO TASK #01)
├── notepad.html      ← App: Notepad
├── agenda.html       ← App: Agenda
├── style.css         ← Design system global
└── app.js            ← Interactividade
```

---

## Regras de Design (obrigatórias)

1. **Font:** Inter (Google Fonts) — não usar DM Sans nem outra
2. **Cor primária botões/nav activo:** `#1a1a1a` (preto) com texto branco — nunca azul
3. **Sidebar:** fundo branco (`#fff`), não azul escuro
4. **Fundo da app:** `#f5f5f5` cinza muito claro, não branco nem azul
5. **Logo:** ícone casinha SVG + texto "Daily**nest**" (Daily em bold, nest em regular)
6. **Nav links activos:** pill preto arredondado (border-radius: 10px), ícone + texto
7. **Nav links inativos:** sem fundo, só ícone + texto cinza escuro
8. **Workspace toggle:** "Work" e "Personal" — pills cinza claro, activo = preto
9. **Topbar Login/Register:** `border-top: 3px solid #3b82f6` (linha azul no topo da página)
10. **Botão primário:** fundo preto (#1a1a1a), texto branco, border-radius: 10px, sem sombra grande
11. **Cards stat:** fundo branco, border suave, ícone em quadrado colorido (radius: 12px)
12. **Table:** sem bordas por célula, só border-bottom nas rows; headers uppercase cinza muted
13. **Modal:** overlay rgba(0,0,0,0.4), card branco, shadow grande

---

## Critérios de Aceitação — Task #01

- [ ] Sidebar com logo DailyNest (ícone + texto)
- [ ] Workspace toggle: Work / Personal (pills)
- [ ] 4 nav links com ícones: Tasks (activo, preto), Agenda, Notepad, Files
- [ ] Avatar utilizador em baixo: "RD" circular preto + nome + email
- [ ] 4 stat cards com ícones coloridos (azul, cinza, laranja, verde)
- [ ] Search bar + dropdowns na tabela
- [ ] Tabela com headers uppercase: TASK NAME, STATUS, DUE DATE, CREATED
- [ ] Task rows com ponto de status colorido + ícone calendário + timestamp
- [ ] Paginação `< 1 >` em baixo
- [ ] Modal "Create New Task" funcional (abrir/fechar)
- [ ] Modal com campos: Task Name, Status, Priority, Due Date, Description
- [ ] Design fiel ao Figma: fundo #f5f5f5, sidebar branca, botões pretos
- [ ] Font Inter carregada
- [ ] Responsivo (mobile: sidebar colapsa)

---

## Passos de Execução

1. Criar `style.css` com todas as CSS variables do design real
2. Criar componentes partilhados: sidebar, topbar de conteúdo
3. Implementar `tasks.html` (foco da task #01)
4. Implementar `login.html` e `register.html`
5. Implementar `notepad.html`
6. Implementar `agenda.html`
7. Implementar `index.html` (landing)
8. Testar responsividade
9. Actualizar `IAusage.md`

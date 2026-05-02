**User:**

<task>
You are replacing ALL the results page CSS in E:\codecompass\index.html to exactly match the design system of E:\IBM Bob\index.html. Do NOT touch any JavaScript, HTML structure, IDs, or class names. Only replace CSS inside the <style> tag for the results page classes listed below.
First, add these CSS variables to the :root block that already exists (merge, don't duplicate):
--blue-400: #60a5fa;
--blue-500: #3b82f6;
--blue-600: #2563eb;
--blue-700: #1d4ed8;
--teal-500: #14b8a6;
--slate-300: #cbd5e1;
--slate-400: #94a3b8;
--slate-500: #64748b;
--slate-600: #475569;
--slate-700: #334155;
--slate-800: #1e293b;
--slate-850: #172033;
--slate-900: #0f172a;
--slate-950: #080c14;
Now replace/add these exact CSS rules:
/* ── RESULTS PAGE ── */
.results-page {
  background: #080c14;
  background-image: radial-gradient(circle, rgba(37,99,235,.05) 1px, transparent 1px);
  background-size: 28px 28px;
  min-height: 100vh;
  padding: 48px 72px;
  font-family: 'Inter', sans-serif;
  -webkit-font-smoothing: antialiased;
}
.results-container {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 28px;
}
/* ── HEADER ── */
.results-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px 32px;
  background: #111827;
  border-radius: 18px;
  border: 1px solid rgba(255,255,255,.06);
  box-shadow: 0 1px 3px rgba(0,0,0,.3);
}
.results-title {
  display: flex;
  align-items: center;
  gap: 16px;
}
.results-title h1 {
  font-size: 22px;
  font-weight: 800;
  color: #f1f5f9;
  letter-spacing: -0.5px;
}
.results-title .powered-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(37,99,235,.1);
  border: 1px solid rgba(37,99,235,.2);
  border-radius: 20px;
  padding: 6px 14px;
  font-size: 12px;
  font-weight: 600;
  color: #60a5fa;
}
.back-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.08);
  color: #94a3b8;
  padding: 10px 20px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 600;
  font-family: 'Inter', sans-serif;
  cursor: pointer;
  transition: background .18s, color .18s, border-color .18s;
}
.back-btn:hover {
  background: rgba(255,255,255,.08);
  color: #f1f5f9;
  border-color: rgba(255,255,255,.15);
}
/* ── SCORE CARDS ── */
.score-cards {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
}
.score-card {
  background: linear-gradient(145deg, #111827, #0d1424);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 20px;
  padding: 28px 20px;
  text-align: center;
  transition: transform .2s, box-shadow .2s;
  position: relative;
  overflow: hidden;
}
.score-card::before {
  content: '';
  position: absolute;
  top: -40px; left: 50%;
  transform: translateX(-50%);
  width: 120px; height: 120px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(37,99,235,.07), transparent 70%);
  pointer-events: none;
}
.score-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 48px rgba(0,0,0,.4);
}
.score-card-title {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .6px;
  text-transform: uppercase;
  color: #475569;
  margin-bottom: 20px;
}
.score-circle {
  width: 100px;
  height: 100px;
  margin: 0 auto 14px;
  position: relative;
}
.score-circle svg { transform: rotate(-90deg); }
.score-value {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -1px;
}
.score-label {
  font-size: 11px;
  color: #334155;
  margin-top: 4px;
}
/* ── SECTION WRAPPER ── */
.section {
  background: #111827;
  border: 1px solid rgba(255,255,255,.06);
  border-radius: 20px;
  padding: 36px 40px;
}
.section-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 28px;
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(255,255,255,.05);
}
.section-header svg {
  width: 20px; height: 20px;
  flex-shrink: 0;
}
.section-title {
  font-size: 18px;
  font-weight: 700;
  letter-spacing: -.3px;
  color: #f1f5f9;
}
/* ── QUICK WINS ── */
.quick-win-card {
  background: rgba(255,255,255,.02);
  border: 1px solid rgba(255,255,255,.05);
  border-left: 3px solid;
  border-radius: 12px;
  padding: 18px 22px;
  margin-bottom: 10px;
  transition: background .15s;
}
.quick-win-card:hover { background: rgba(255,255,255,.04); }
.quick-win-card.easy   { border-left-color: #10b981; }
.quick-win-card.medium { border-left-color: #f59e0b; }
.quick-win-card.hard   { border-left-color: #ef4444; }
.quick-win-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 12px;
}
.quick-win-title {
  font-size: 14px;
  font-weight: 600;
  color: #e2e8f0;
  line-height: 1.4;
}
.quick-win-description {
  font-size: 12.5px;
  color: #64748b;
  margin-top: 6px;
  line-height: 1.55;
}
.quick-win-file {
  display: inline-block;
  font-family: 'Courier New', monospace;
  font-size: 11px;
  color: #475569;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.06);
  padding: 2px 8px;
  border-radius: 5px;
  margin-top: 8px;
}
.quick-win-badges { display: flex; gap: 6px; flex-shrink: 0; }
.badge {
  font-size: 11px;
  font-weight: 600;
  padding: 3px 10px;
  border-radius: 8px;
  white-space: nowrap;
  letter-spacing: .3px;
}
.badge.easy   { background: rgba(16,185,129,.1);  color: #34d399; border: 1px solid rgba(52,211,153,.2); }
.badge.medium { background: rgba(245,158,11,.1);  color: #fbbf24; border: 1px solid rgba(251,191,36,.2); }
.badge.hard   { background: rgba(239,68,68,.1);   color: #f87171; border: 1px solid rgba(248,113,113,.2); }
/* ── AI SUMMARY ── */
.ai-summary {
  color: #94a3b8;
  font-size: 14px;
  line-height: 1.85;
}
.ai-summary h2 {
  font-size: 15px;
  font-weight: 700;
  color: #f1f5f9;
  margin: 28px 0 10px;
  padding-left: 14px;
  border-left: 3px solid #2563eb;
  letter-spacing: -.2px;
}
.ai-summary h3 { font-size: 14px; font-weight: 600; color: #cbd5e1; margin: 16px 0 8px; }
.ai-summary strong { color: #e2e8f0; }
.ai-summary ul { padding-left: 20px; margin: 10px 0; }
.ai-summary li { margin-bottom: 7px; color: #94a3b8; }
/* ── FILE EXPLORER ── */
#fileSearchInput {
  width: 100%;
  background: #0d1424;
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 12px;
  padding: 12px 16px;
  color: #e2e8f0;
  font-size: 13px;
  font-family: 'Inter', sans-serif;
  margin-bottom: 16px;
  transition: border-color .2s, box-shadow .2s;
}
#fileSearchInput:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59,130,246,.1);
}
#fileSearchInput::placeholder { color: #334155; }
.file-list { display: flex; flex-direction: column; gap: 1px; }
.file-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 9px 12px;
  border-radius: 8px;
  transition: background .12s;
}
.file-item:hover { background: rgba(255,255,255,.04); }
.file-info {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: 1;
  min-width: 0;
}
.file-icon { width: 15px; height: 15px; flex-shrink: 0; opacity: .8; }
.file-path {
  font-size: 12.5px;
  color: #64748b;
  font-family: 'Courier New', monospace;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.file-item:hover .file-path { color: #94a3b8; }
.file-actions {
  display: flex;
  gap: 2px;
  flex-shrink: 0;
  opacity: 0;
  transition: opacity .15s;
}
.file-item:hover .file-actions { opacity: 1; }
.icon-btn {
  width: 28px; height: 28px;
  background: transparent;
  border: 1px solid transparent;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #475569;
  transition: all .15s;
}
.icon-btn svg { width: 13px; height: 13px; stroke: currentColor; }
.icon-btn:hover {
  background: rgba(37,99,235,.1);
  border-color: rgba(37,99,235,.2);
  color: #60a5fa;
}
.icon-btn.success {
  color: #10b981;
  background: rgba(16,185,129,.1);
  border-color: rgba(16,185,129,.2);
}
/* ── FILE VIEWER MODAL ── */
.file-viewer-modal {
  position: fixed; inset: 0;
  background: rgba(0,0,0,.72);
  backdrop-filter: blur(8px);
  z-index: 2000;
  display: none;
  align-items: center;
  justify-content: center;
}
.file-viewer-modal.active { display: flex; }
.file-viewer {
  width: 80vw; height: 80vh;
  background: #0d1424;
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 18px;
  box-shadow: 0 40px 80px rgba(0,0,0,.6);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  animation: modalIn .25s cubic-bezier(.16,1,.3,1);
}
@keyframes modalIn {
  from { opacity:0; transform: scale(.96) translateY(12px); }
  to   { opacity:1; transform: scale(1)   translateY(0); }
}
.file-viewer-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  background: #111827;
  border-bottom: 1px solid rgba(255,255,255,.06);
  flex-shrink: 0;
}
.file-viewer-title {
  font-family: 'Courier New', monospace;
  font-size: 13px;
  color: #64748b;
}
.file-viewer-actions { display: flex; gap: 6px; }
.file-viewer-content {
  flex: 1;
  overflow: auto;
  padding: 24px;
}
.file-viewer-code {
  font-family: 'Courier New', monospace;
  font-size: 12.5px;
  line-height: 1.7;
  color: #e2e8f0;
  background: transparent;
  white-space: pre-wrap;
  word-break: break-all;
}
/* ── ANSWER PANEL ── */
.answer-panel {
  background: #0d1424;
  border: 1px solid rgba(16,185,129,.15);
  border-radius: 14px;
  padding: 28px 32px;
  margin-top: 20px;
}
.answer-title {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .6px;
  text-transform: uppercase;
  color: #10b981;
  margin-bottom: 16px;
}
.answer-content {
  font-size: 14px;
  color: #94a3b8;
  line-height: 1.8;
}
/* ── SPINNER ── */
.spinner {
  width: 16px; height: 16px;
  border: 2px solid rgba(255,255,255,.25);
  border-top-color: #fff;
  border-radius: 50%;
  animation: spin .6s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
/* ── RESPONSIVE ── */
@media (max-width: 1024px) {
  .score-cards { grid-template-columns: repeat(3, 1fr); }
  .results-page { padding: 32px 24px; }
}
@media (max-width: 640px) {
  .score-cards { grid-template-columns: repeat(2, 1fr); }
  .file-viewer { width: 95vw; height: 90vh; }
}
</task>
<environment_details>
# VSCode Visible Files
index.html

# VSCode Open Tabs
requirements.txt,ui.py,analyzer.py,main.py,update_html.py,generate_html.py,index.html,.gitignore,.env

# Current Time
Current time in ISO 8601 UTC format: 2026-05-01T20:49:29.927Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.00

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>


# Current Workspace Directory (e:/codecompass) Files
.gitignore
analyzer.py
generate_html.py
index_backup.html
index.html
main.py
README.md
requirements.txt
ui.py
update_html.py
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

I'll help you replace the CSS in the results page of `E:\codecompass\index.html` to match the design system from `E:\IBM Bob\index.html`. Let me start by reading both files to understand the current structure.

<read_file>
<args>
<file>
<path>E:\codecompass\index.html</path>
</file>
<file>
<path>E:\IBM Bob\index.html</path>
</file>
</args>
</read_file>

---

**User:**

[read_file for 'E:\codecompass\index.html', 'E:\IBM Bob\index.html'] Result:
<files>
<file><path>E:\codecompass\index.html</path><file_outline>File: index.html (1909 lines)

Fields: html
</file_outline>
<notice>This file is large (1909 lines). You will use the following strategy to understand this file:
- Inform the user you are going to use large file strategy, to efficiently understand the file
- Use the file_outline provided to get an overview of the file structure to help decide next action. This is not the full file. It is not the full depth of the contents.
- If you read the file, use precise file reads with line ranges for specific sections of interest
- Consider if other commands/tools are better suited for extracting information from that file type
- Use ask_followup_question tool if needed to identify the best next action
</notice></file>
<file><path>E:\IBM Bob\index.html</path><file_outline>File: index.html (1102 lines)

Fields: html
</file_outline>
<notice>This file is large (1101 lines). You will use the following strategy to understand this file:
- Inform the user you are going to use large file strategy, to efficiently understand the file
- Use the file_outline provided to get an overview of the file structure to help decide next action. This is not the full file. It is not the full depth of the contents.
- If you read the file, use precise file reads with line ranges for specific sections of interest
- Consider if other commands/tools are better suited for extracting information from that file type
- Use ask_followup_question tool if needed to identify the best next action
</notice></file>
</files>
<environment_details>
# VSCode Visible Files
index.html

# VSCode Open Tabs
requirements.txt,ui.py,analyzer.py,main.py,update_html.py,generate_html.py,index.html,.gitignore,.env

# Current Time
Current time in ISO 8601 UTC format: 2026-05-01T20:49:42.580Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.02

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

I'll use a large file strategy to efficiently understand both files. Let me search for the `<style>` tag sections to locate the CSS that needs to be replaced.

<search_files>
<path>E:\codecompass\index.html</path>
<regex>:root\s*\{</regex>
</search_files>

---

**User:**

[search_files for ':root\s*\{'] Result:
Found 0 results.
<environment_details>
# VSCode Visible Files
index.html

# VSCode Open Tabs
requirements.txt,ui.py,analyzer.py,main.py,update_html.py,generate_html.py,index.html,.gitignore,.env

# Current Time
Current time in ISO 8601 UTC format: 2026-05-01T20:49:59.785Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.04

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

<search_files>
<path>E:\codecompass\index.html</path>
<regex><style></regex>
</search_files>

---

**User:**

[search_files for '<style>'] Result:
Found 1 result.

# index.html
  9 |     <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
 10 |     <style>
 11 | 
----
<environment_details>
# VSCode Visible Files
index.html

# VSCode Open Tabs
requirements.txt,ui.py,analyzer.py,main.py,update_html.py,generate_html.py,index.html,.gitignore,.env

# Current Time
Current time in ISO 8601 UTC format: 2026-05-01T20:50:03.872Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.06

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

<search_files>
<path>E:\codecompass\index.html</path>
<regex></style></regex>
</search_files>

---

**User:**

[search_files for '</style>'] Result:
Found 1 result.

# index.html
1220 |         .btn:disabled { opacity: 0.6; cursor: not-allowed; }
1221 |     </style>
1222 | </head>
----
<environment_details>
# VSCode Visible Files
index.html

# VSCode Open Tabs
requirements.txt,ui.py,analyzer.py,main.py,update_html.py,generate_html.py,index.html,.gitignore,.env

# Current Time
Current time in ISO 8601 UTC format: 2026-05-01T20:50:07.199Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.08

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

Now let me read the CSS section from both files to understand the current structure and what needs to be replaced.

<read_file>
<args>
<file>
<path>E:\codecompass\index.html</path>
<line_range>10-1221</line_range>
</file>
</args>
</read_file>

---

**User:**

[read_file for 'E:\codecompass\index.html'. Reading multiple files at once is more efficient for the LLM. If other files are relevant to your current task, please read them simultaneously.] Result:
<files>
<file><path>E:\codecompass\index.html</path>
<content lines="10-1221">
  10 |     <style>
  11 | 
  12 |         * {
  13 |             margin: 0;
  14 |             padding: 0;
  15 |             box-sizing: border-box;
  16 |         }
  17 | 
  18 |         body {
  19 |             font-family: 'Inter', sans-serif;
  20 |             background: #000;
  21 |             color: #fff;
  22 |             overflow-x: hidden;
  23 |             -webkit-font-smoothing: antialiased;
  24 |         }
  25 | 
  26 |         /* Hero Section */
  27 |         .hero {
  28 |             min-height: 100vh;
  29 |             background: linear-gradient(135deg, #dbeafe 0%, #ffffff 100%);
  30 |             position: relative;
  31 |             overflow: hidden;
  32 |             padding: 80px 40px;
  33 |         }
  34 | 
  35 |         .hero::before {
  36 |             content: '';
  37 |             position: absolute;
  38 |             top: 0;
  39 |             left: 0;
  40 |             right: 0;
  41 |             bottom: 0;
  42 |             background-image: radial-gradient(circle, rgba(37, 99, 235, 0.15) 1px, transparent 1px);
  43 |             background-size: 24px 24px;
  44 |             pointer-events: none;
  45 |         }
  46 | 
  47 |         .hero-container {
  48 |             max-width: 1280px;
  49 |             margin: 0 auto;
  50 |             display: grid;
  51 |             grid-template-columns: 1fr 1fr;
  52 |             gap: 80px;
  53 |             align-items: center;
  54 |             position: relative;
  55 |             z-index: 1;
  56 |         }
  57 | 
  58 |         .hero-left {
  59 |             display: flex;
  60 |             flex-direction: column;
  61 |             gap: 24px;
  62 |         }
  63 | 
  64 |         .logo-container {
  65 |             display: flex;
  66 |             align-items: center;
  67 |             gap: 16px;
  68 |         }
  69 | 
  70 |         .logo {
  71 |             width: 64px;
  72 |             height: 64px;
  73 |             background: #2563eb;
  74 |             border-radius: 12px;
  75 |             display: flex;
  76 |             align-items: center;
  77 |             justify-content: center;
  78 |         }
  79 | 
  80 |         .logo svg {
  81 |             width: 36px;
  82 |             height: 36px;
  83 |         }
  84 | 
  85 |         .hero-title {
  86 |             font-size: 56px;
  87 |             font-weight: 800;
  88 |             color: #111827;
  89 |             line-height: 1.1;
  90 |         }
  91 | 
  92 |         .hero-subtitle {
  93 |             font-size: 24px;
  94 |             color: #4b5563;
  95 |             font-weight: 500;
  96 |             line-height: 1.4;
  97 |         }
  98 | 
  99 |         .powered-badge {
 100 |             display: inline-flex;
 101 |             align-items: center;
 102 |             gap: 8px;
 103 |             background: rgba(37, 99, 235, 0.1);
 104 |             border: 1px solid rgba(37, 99, 235, 0.2);
 105 |             padding: 8px 16px;
 106 |             border-radius: 24px;
 107 |             font-size: 14px;
 108 |             font-weight: 600;
 109 |             color: #2563eb;
 110 |             width: fit-content;
 111 |         }
 112 | 
 113 |         .dot-grid {
 114 |             display: grid;
 115 |             grid-template-columns: repeat(3, 4px);
 116 |             gap: 3px;
 117 |         }
 118 | 
 119 |         .dot-grid span {
 120 |             width: 4px;
 121 |             height: 4px;
 122 |             background: #2563eb;
 123 |             border-radius: 50%;
 124 |         }
 125 | 
 126 |         /* Hero Right - Floating Cards */
 127 |         .hero-right {
 128 |             position: relative;
 129 |             height: 500px;
 130 |         }
 131 | 
 132 |         .floating-card {
 133 |             position: absolute;
 134 |             background: #1e293b;
 135 |             border-radius: 12px;
 136 |             border: 1px solid rgba(255, 255, 255, 0.07);
 137 |             box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
 138 |             animation: float 6s ease-in-out infinite;
 139 |         }
 140 | 
 141 |         @keyframes float {
 142 |             0%, 100% { transform: translateY(0px); }
 143 |             50% { transform: translateY(-20px); }
 144 |         }
 145 | 
 146 |         .code-editor-card {
 147 |             width: 320px;
 148 |             padding: 20px;
 149 |             top: 50px;
 150 |             left: 0;
 151 |             animation-delay: 0s;
 152 |         }
 153 | 
 154 |         .code-line {
 155 |             height: 8px;
 156 |             border-radius: 4px;
 157 |             margin-bottom: 8px;
 158 |         }
 159 | 
 160 |         .code-line:nth-child(1) { background: #ef4444; width: 60%; }
 161 |         .code-line:nth-child(2) { background: #3b82f6; width: 80%; }
 162 |         .code-line:nth-child(3) { background: #10b981; width: 50%; }
 163 |         .code-line:nth-child(4) { background: #f59e0b; width: 70%; }
 164 | 
 165 |         .chart-card {
 166 |             width: 140px;
 167 |             height: 120px;
 168 |             padding: 16px;
 169 |             top: 0;
 170 |             right: 80px;
 171 |             animation-delay: 1s;
 172 |             display: flex;
 173 |             align-items: flex-end;
 174 |             gap: 8px;
 175 |         }
 176 | 
 177 |         .bar {
 178 |             flex: 1;
 179 |             background: #2563eb;
 180 |             border-radius: 4px 4px 0 0;
 181 |         }
 182 | 
 183 |         .bar:nth-child(1) { height: 40%; }
 184 |         .bar:nth-child(2) { height: 70%; }
 185 |         .bar:nth-child(3) { height: 55%; }
 186 | 
 187 |         .list-card {
 188 |             width: 180px;
 189 |             padding: 16px;
 190 |             top: 280px;
 191 |             right: 0;
 192 |             animation-delay: 2s;
 193 |         }
 194 | 
 195 |         .list-item {
 196 |             display: flex;
 197 |             align-items: center;
 198 |             gap: 8px;
 199 |             margin-bottom: 10px;
 200 |         }
 201 | 
 202 |         .list-dot {
 203 |             width: 6px;
 204 |             height: 6px;
 205 |             background: #10b981;
 206 |             border-radius: 50%;
 207 |         }
 208 | 
 209 |         .list-line {
 210 |             flex: 1;
 211 |             height: 4px;
 212 |             background: rgba(255, 255, 255, 0.1);
 213 |             border-radius: 2px;
 214 |         }
 215 | 
 216 |         .icon-tile {
 217 |             width: 56px;
 218 |             height: 56px;
 219 |             background: #1e293b;
 220 |             border-radius: 10px;
 221 |             border: 1px solid rgba(255, 255, 255, 0.07);
 222 |             display: flex;
 223 |             align-items: center;
 224 |             justify-content: center;
 225 |             position: absolute;
 226 |             animation: float 5s ease-in-out infinite;
 227 |         }
 228 | 
 229 |         .icon-tile svg {
 230 |             width: 24px;
 231 |             height: 24px;
 232 |         }
 233 | 
 234 |         .icon-tile:nth-child(5) { top: 180px; left: 280px; animation-delay: 0.5s; }
 235 |         .icon-tile:nth-child(6) { top: 340px; left: 100px; animation-delay: 1.5s; }
 236 |         .icon-tile:nth-child(7) { top: 420px; right: 140px; animation-delay: 2.5s; }
 237 | 
 238 |         /* Feature Cards */
 239 |         .feature-section {
 240 |             padding: 80px 40px;
 241 |         }
 242 | 
 243 |         .feature-card {
 244 |             max-width: 1280px;
 245 |             margin: 0 auto 60px;
 246 |             background: #1e293b;
 247 |             border-radius: 24px;
 248 |             border: 1px solid rgba(255, 255, 255, 0.07);
 249 |             padding: 60px;
 250 |             display: grid;
 251 |             grid-template-columns: 1fr 1fr;
 252 |             gap: 60px;
 253 |             align-items: center;
 254 |         }
 255 | 
 256 |         .feature-card.dark-01 {
 257 |             background: #111827;
 258 |         }
 259 | 
 260 |         .feature-card.dark-02 {
 261 |             background: #0d1424;
 262 |         }
 263 | 
 264 |         .feature-left {
 265 |             display: flex;
 266 |             flex-direction: column;
 267 |             gap: 24px;
 268 |         }
 269 | 
 270 |         .step-badge {
 271 |             display: inline-flex;
 272 |             align-items: center;
 273 |             gap: 12px;
 274 |             width: fit-content;
 275 |         }
 276 | 
 277 |         .step-number {
 278 |             font-size: 14px;
 279 |             font-weight: 700;
 280 |             color: #6b7280;
 281 |             background: rgba(255, 255, 255, 0.05);
 282 |             padding: 6px 12px;
 283 |             border-radius: 8px;
 284 |         }
 285 | 
 286 |         .icon-box {
 287 |             width: 48px;
 288 |             height: 48px;
 289 |             border-radius: 12px;
 290 |             display: flex;
 291 |             align-items: center;
 292 |             justify-content: center;
 293 |         }
 294 | 
 295 |         .icon-box.blue-tint {
 296 |             background: rgba(37, 99, 235, 0.1);
 297 |         }
 298 | 
 299 |         .icon-box.teal-tint {
 300 |             background: rgba(20, 184, 166, 0.1);
 301 |         }
 302 | 
 303 |         .icon-box svg {
 304 |             width: 24px;
 305 |             height: 24px;
 306 |         }
 307 | 
 308 |         .feature-header {
 309 |             display: flex;
 310 |             align-items: center;
 311 |             gap: 12px;
 312 |             flex-wrap: wrap;
 313 |         }
 314 | 
 315 |         .feature-title {
 316 |             font-size: 36px;
 317 |             font-weight: 700;
 318 |             color: #fff;
 319 |         }
 320 | 
 321 |         .status-pill {
 322 |             padding: 6px 14px;
 323 |             border-radius: 20px;
 324 |             font-size: 13px;
 325 |             font-weight: 600;
 326 |         }
 327 | 
 328 |         .status-pill.green {
 329 |             background: rgba(16, 185, 129, 0.1);
 330 |             color: #10b981;
 331 |             border: 1px solid rgba(16, 185, 129, 0.2);
 332 |         }
 333 | 
 334 |         .status-pill.blue {
 335 |             background: rgba(37, 99, 235, 0.1);
 336 |             color: #3b82f6;
 337 |             border: 1px solid rgba(37, 99, 235, 0.2);
 338 |         }
 339 | 
 340 |         .feature-description {
 341 |             font-size: 18px;
 342 |             color: #9ca3af;
 343 |             line-height: 1.6;
 344 |         }
 345 | 
 346 |         .input-group {
 347 |             display: flex;
 348 |             gap: 12px;
 349 |         }
 350 | 
 351 |         .input-wrapper {
 352 |             flex: 1;
 353 |             position: relative;
 354 |         }
 355 | 
 356 |         .input-icon {
 357 |             position: absolute;
 358 |             left: 16px;
 359 |             top: 50%;
 360 |             transform: translateY(-50%);
 361 |             width: 20px;
 362 |             height: 20px;
 363 |             opacity: 0.5;
 364 |         }
 365 | 
 366 |         input[type="text"], textarea {
 367 |             width: 100%;
 368 |             background: rgba(0, 0, 0, 0.3);
 369 |             border: 1px solid rgba(255, 255, 255, 0.1);
 370 |             border-radius: 12px;
 371 |             padding: 16px 16px 16px 48px;
 372 |             color: #fff;
 373 |             font-size: 15px;
 374 |             font-family: 'Inter', sans-serif;
 375 |             transition: all 0.2s;
 376 |         }
 377 | 
 378 |         textarea {
 379 |             padding: 16px;
 380 |             resize: none;
 381 |             height: 140px;
 382 |             line-height: 1.6;
 383 |         }
 384 | 
 385 |         input[type="text"]:focus, textarea:focus {
 386 |             outline: none;
 387 |             border-color: #2563eb;
 388 |             box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
 389 |         }
 390 | 
 391 |         input::placeholder, textarea::placeholder {
 392 |             color: #6b7280;
 393 |         }
 394 | 
 395 |         .btn {
 396 |             background: #2563eb;
 397 |             color: #fff;
 398 |             border: none;
 399 |             border-radius: 12px;
 400 |             padding: 16px 32px;
 401 |             font-size: 15px;
 402 |             font-weight: 600;
 403 |             font-family: 'Inter', sans-serif;
 404 |             cursor: pointer;
 405 |             display: inline-flex;
 406 |             align-items: center;
 407 |             gap: 8px;
 408 |             transition: all 0.2s;
 409 |         }
 410 | 
 411 |         .btn:hover {
 412 |             background: #1d4ed8;
 413 |             transform: translateY(-1px);
 414 |             box-shadow: 0 10px 30px rgba(37, 99, 235, 0.4);
 415 |         }
 416 | 
 417 |         .btn svg {
 418 |             width: 18px;
 419 |             height: 18px;
 420 |         }
 421 | 
 422 |         .btn-tall {
 423 |             height: 140px;
 424 |             padding: 16px 24px;
 425 |         }
 426 | 
 427 |         .tags {
 428 |             display: flex;
 429 |             flex-wrap: wrap;
 430 |             gap: 10px;
 431 |         }
 432 | 
 433 |         .tag {
 434 |             padding: 10px 18px;
 435 |             background: rgba(255, 255, 255, 0.03);
 436 |             border: 1px solid rgba(255, 255, 255, 0.1);
 437 |             border-radius: 20px;
 438 |             font-size: 14px;
 439 |             color: #9ca3af;
 440 |             cursor: pointer;
 441 |             transition: all 0.2s;
 442 |         }
 443 | 
 444 |         .tag:hover {
 445 |             border-color: #2563eb;
 446 |             color: #3b82f6;
 447 |         }
 448 | 
 449 |         /* Feature Right - 3D Cubes */
 450 |         .feature-right {
 451 |             position: relative;
 452 |             height: 400px;
 453 |         }
 454 | 
 455 |         .cube-cluster {
 456 |             position: absolute;
 457 |             left: 50%;
 458 |             top: 50%;
 459 |             transform: translate(-50%, -50%);
 460 |         }
 461 | 
 462 |         .cube {
 463 |             position: absolute;
 464 |             transform-style: preserve-3d;
 465 |         }
 466 | 
 467 |         .cube-face {
 468 |             position: absolute;
 469 |             background: rgba(255, 255, 255, 0.9);
 470 |             border: 1px solid rgba(0, 0, 0, 0.1);
 471 |         }
 472 | 
 473 |         .cube-1 {
 474 |             width: 80px;
 475 |             height: 160px;
 476 |             left: 0;
 477 |             top: -40px;
 478 |         }
 479 | 
 480 |         .cube-1 .front { width: 80px; height: 160px; transform: translateZ(40px); }
 481 |         .cube-1 .back { width: 80px; height: 160px; transform: translateZ(-40px) rotateY(180deg); }
 482 |         .cube-1 .right { width: 80px; height: 160px; transform: rotateY(90deg) translateZ(40px); }
 483 |         .cube-1 .left { width: 80px; height: 160px; transform: rotateY(-90deg) translateZ(40px); }
 484 |         .cube-1 .top { width: 80px; height: 80px; transform: rotateX(90deg) translateZ(160px); }
 485 |         .cube-1 .bottom { width: 80px; height: 80px; transform: rotateX(-90deg) translateZ(0); }
 486 | 
 487 |         .cube-2 {
 488 |             width: 80px;
 489 |             height: 100px;
 490 |             left: 100px;
 491 |             top: 20px;
 492 |         }
 493 | 
 494 |         .cube-2 .front { width: 80px; height: 100px; transform: translateZ(40px); }
 495 |         .cube-2 .back { width: 80px; height: 100px; transform: translateZ(-40px) rotateY(180deg); }
 496 |         .cube-2 .right { width: 80px; height: 100px; transform: rotateY(90deg) translateZ(40px); }
 497 |         .cube-2 .left { width: 80px; height: 100px; transform: rotateY(-90deg) translateZ(40px); }
 498 |         .cube-2 .top { width: 80px; height: 80px; transform: rotateX(90deg) translateZ(100px); }
 499 |         .cube-2 .bottom { width: 80px; height: 80px; transform: rotateX(-90deg) translateZ(0); }
 500 | 
 501 |         .cube-3 {
 502 |             width: 80px;
 503 |             height: 120px;
 504 |             left: 200px;
 505 |             top: 0;
 506 |         }
 507 | 
 508 |         .cube-3 .front, .cube-3 .back, .cube-3 .right, .cube-3 .left { background: rgba(20, 184, 166, 0.9); }
 509 |         .cube-3 .front { width: 80px; height: 120px; transform: translateZ(40px); }
 510 |         .cube-3 .back { width: 80px; height: 120px; transform: translateZ(-40px) rotateY(180deg); }
 511 |         .cube-3 .right { width: 80px; height: 120px; transform: rotateY(90deg) translateZ(40px); }
 512 |         .cube-3 .left { width: 80px; height: 120px; transform: rotateY(-90deg) translateZ(40px); }
 513 |         .cube-3 .top { width: 80px; height: 80px; transform: rotateX(90deg) translateZ(120px); background: rgba(20, 184, 166, 0.9); }
 514 |         .cube-3 .bottom { width: 80px; height: 80px; transform: rotateX(-90deg) translateZ(0); background: rgba(20, 184, 166, 0.9); }
 515 | 
 516 |         .cube-4 {
 517 |             width: 80px;
 518 |             height: 140px;
 519 |             left: 300px;
 520 |             top: -20px;
 521 |         }
 522 | 
 523 |         .cube-4 .front, .cube-4 .back, .cube-4 .right, .cube-4 .left { background: rgba(37, 99, 235, 0.9); }
 524 |         .cube-4 .front { width: 80px; height: 140px; transform: translateZ(40px); }
 525 |         .cube-4 .back { width: 80px; height: 140px; transform: translateZ(-40px) rotateY(180deg); }
 526 |         .cube-4 .right { width: 80px; height: 140px; transform: rotateY(90deg) translateZ(40px); }
 527 |         .cube-4 .left { width: 80px; height: 140px; transform: rotateY(-90deg) translateZ(40px); }
 528 |         .cube-4 .top { width: 80px; height: 80px; transform: rotateX(90deg) translateZ(140px); background: rgba(37, 99, 235, 0.9); }
 529 |         .cube-4 .bottom { width: 80px; height: 80px; transform: rotateX(-90deg) translateZ(0); background: rgba(37, 99, 235, 0.9); }
 530 | 
 531 |         .orbit-ellipse {
 532 |             position: absolute;
 533 |             left: 50%;
 534 |             top: 50%;
 535 |             transform: translate(-50%, -50%);
 536 |         }
 537 | 
 538 |         .diamond-marker {
 539 |             position: absolute;
 540 |             width: 12px;
 541 |             height: 12px;
 542 |             background: #3b82f6;
 543 |             transform: rotate(45deg);
 544 |         }
 545 | 
 546 |         .diamond-1 { left: 100px; top: -60px; }
 547 |         .diamond-2 { right: 80px; bottom: -40px; }
 548 | 
 549 |         /* Code Panel */
 550 |         .code-panel {
 551 |             background: #0f172a;
 552 |             border-radius: 16px;
 553 |             padding: 24px;
 554 |             border: 1px solid rgba(255, 255, 255, 0.07);
 555 |             position: relative;
 556 |         }
 557 | 
 558 |         .code-row {
 559 |             display: flex;
 560 |             align-items: center;
 561 |             gap: 12px;
 562 |             margin-bottom: 12px;
 563 |         }
 564 | 
 565 |         .indicator-bar {
 566 |             width: 4px;
 567 |             height: 20px;
 568 |             border-radius: 2px;
 569 |         }
 570 | 
 571 |         .indicator-bar.red { background: #ef4444; }
 572 |         .indicator-bar.blue { background: #3b82f6; }
 573 |         .indicator-bar.green { background: #10b981; }
 574 |         .indicator-bar.yellow { background: #f59e0b; }
 575 | 
 576 |         .code-text {
 577 |             flex: 1;
 578 |             height: 8px;
 579 |             background: rgba(255, 255, 255, 0.1);
 580 |             border-radius: 4px;
 581 |         }
 582 | 
 583 |         .code-badges {
 584 |             position: absolute;
 585 |             top: 24px;
 586 |             right: 24px;
 587 |             display: flex;
 588 |             gap: 8px;
 589 |         }
 590 | 
 591 |         .code-badge {
 592 |             padding: 6px 12px;
 593 |             background: rgba(255, 255, 255, 0.05);
 594 |             border: 1px solid rgba(255, 255, 255, 0.1);
 595 |             border-radius: 8px;
 596 |             font-size: 12px;
 597 |             font-weight: 600;
 598 |             color: #9ca3af;
 599 |         }
 600 | 
 601 |         /* Footer */
 602 |         .footer {
 603 |             background: #0a0a0a;
 604 |             padding: 60px 40px;
 605 |             border-top: 1px solid rgba(255, 255, 255, 0.05);
 606 |         }
 607 | 
 608 |         .footer-container {
 609 |             max-width: 1280px;
 610 |             margin: 0 auto;
 611 |             display: flex;
 612 |             justify-content: space-between;
 613 |             align-items: center;
 614 |         }
 615 | 
 616 |         .footer-item {
 617 |             display: flex;
 618 |             align-items: center;
 619 |             gap: 12px;
 620 |             font-size: 16px;
 621 |             color: #9ca3af;
 622 |         }
 623 | 
 624 |         .footer-item svg {
 625 |             width: 24px;
 626 |             height: 24px;
 627 |         }
 628 | 
 629 |         /* Modal */
 630 |         .modal-overlay {
 631 |             position: fixed;
 632 |             top: 0;
 633 |             left: 0;
 634 |             right: 0;
 635 |             bottom: 0;
 636 |             background: rgba(0, 0, 0, 0.8);
 637 |             display: none;
 638 |             align-items: center;
 639 |             justify-content: center;
 640 |             z-index: 1000;
 641 |             backdrop-filter: blur(4px);
 642 |         }
 643 | 
 644 |         .modal-overlay.active {
 645 |             display: flex;
 646 |             animation: fadeIn 0.2s ease;
 647 |         }
 648 | 
 649 |         @keyframes fadeIn {
 650 |             from { opacity: 0; }
 651 |             to { opacity: 1; }
 652 |         }
 653 | 
 654 |         .modal {
 655 |             background: #1e293b;
 656 |             border-radius: 24px;
 657 |             border: 1px solid rgba(255, 255, 255, 0.1);
 658 |             padding: 40px;
 659 |             max-width: 500px;
 660 |             width: 90%;
 661 |             position: relative;
 662 |             animation: modalSlide 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
 663 |         }
 664 | 
 665 |         @keyframes modalSlide {
 666 |             from {
 667 |                 opacity: 0;
 668 |                 transform: scale(0.9) translateY(20px);
 669 |             }
 670 |             to {
 671 |                 opacity: 1;
 672 |                 transform: scale(1) translateY(0);
 673 |             }
 674 |         }
 675 | 
 676 |         .modal-close {
 677 |             position: absolute;
 678 |             top: 20px;
 679 |             right: 20px;
 680 |             width: 32px;
 681 |             height: 32px;
 682 |             background: rgba(255, 255, 255, 0.05);
 683 |             border: 1px solid rgba(255, 255, 255, 0.1);
 684 |             border-radius: 8px;
 685 |             display: flex;
 686 |             align-items: center;
 687 |             justify-content: center;
 688 |             cursor: pointer;
 689 |             transition: all 0.2s;
 690 |         }
 691 | 
 692 |         .modal-close:hover {
 693 |             background: rgba(255, 255, 255, 0.1);
 694 |         }
 695 | 
 696 |         .modal-close svg {
 697 |             width: 20px;
 698 |             height: 20px;
 699 |         }
 700 | 
 701 |         .modal-title {
 702 |             font-size: 28px;
 703 |             font-weight: 700;
 704 |             margin-bottom: 16px;
 705 |         }
 706 | 
 707 |         .modal-text {
 708 |             font-size: 16px;
 709 |             color: #9ca3af;
 710 |             line-height: 1.6;
 711 |         }
 712 | 
 713 |         /* Responsive */
 714 |         @media (max-width: 960px) {
 715 |             .hero-container {
 716 |                 grid-template-columns: 1fr;
 717 |                 gap: 60px;
 718 |             }
 719 | 
 720 |             .hero-right {
 721 |                 height: 400px;
 722 |             }
 723 | 
 724 |             .hero-title {
 725 |                 font-size: 42px;
 726 |             }
 727 | 
 728 |             .hero-subtitle {
 729 |                 font-size: 20px;
 730 |             }
 731 | 
 732 |             .feature-card {
 733 |                 grid-template-columns: 1fr;
 734 |                 gap: 40px;
 735 |                 padding: 40px;
 736 |             }
 737 | 
 738 |             .feature-title {
 739 |                 font-size: 28px;
 740 |             }
 741 | 
 742 |             .input-group {
 743 |                 flex-direction: column;
 744 |             }
 745 | 
 746 |             .btn-tall {
 747 |                 height: auto;
 748 |             }
 749 | 
 750 |             .footer-container {
 751 |                 flex-direction: column;
 752 |                 gap: 24px;
 753 |                 text-align: center;
 754 |             }
 755 | 
 756 |             .cube-cluster {
 757 |                 transform: translate(-50%, -50%) scale(0.7);
 758 |             }
 759 |         }
 760 |     
 761 |         
 762 |         /* NEW STYLES FOR RESULTS PAGE */
 763 |         .hidden { display: none !important; }
 764 |         
 765 |         .results-page {
 766 |             min-height: 100vh;
 767 |             background: #080c14;
 768 |             background-image: radial-gradient(circle, rgba(37,99,235,0.06) 1px, transparent 1px);
 769 |             background-size: 28px 28px;
 770 |             padding: 40px;
 771 |             font-family: 'Inter', sans-serif;
 772 |         }
 773 |         
 774 |         .results-container {
 775 |             max-width: 1400px;
 776 |             margin: 0 auto;
 777 |             font-family: 'Inter', sans-serif;
 778 |         }
 779 |         
 780 |         .results-header {
 781 |             display: flex;
 782 |             justify-content: space-between;
 783 |             align-items: center;
 784 |             margin-bottom: 40px;
 785 |             flex-wrap: wrap;
 786 |             gap: 20px;
 787 |         }
 788 |         
 789 |         .results-title {
 790 |             display: flex;
 791 |             align-items: center;
 792 |             gap: 16px;
 793 |         }
 794 |         
 795 |         .results-title h1 {
 796 |             font-size: 28px;
 797 |             font-weight: 800;
 798 |             letter-spacing: -0.5px;
 799 |         }
 800 |         
 801 |         .back-btn {
 802 |             background: rgba(255, 255, 255, 0.05);
 803 |             color: #94a3b8;
 804 |             border: 1px solid rgba(255, 255, 255, 0.1);
 805 |             padding: 10px 20px;
 806 |             border-radius: 10px;
 807 |             cursor: pointer;
 808 |             font-size: 13px;
 809 |             font-weight: 600;
 810 |             transition: all 0.2s;
 811 |         }
 812 |         
 813 |         .back-btn:hover {
 814 |             background: rgba(255, 255, 255, 0.1);
 815 |             color: #fff;
 816 |         }
 817 |         
 818 |         .score-cards {
 819 |             display: grid;
 820 |             grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
 821 |             gap: 20px;
 822 |             margin-bottom: 40px;
 823 |         }
 824 |         
 825 |         .score-card {
 826 |             background: linear-gradient(145deg, #1a2235, #111827);
 827 |             border-radius: 20px;
 828 |             padding: 28px 20px;
 829 |             border: 1px solid rgba(255, 255, 255, 0.07);
 830 |             text-align: center;
 831 |             transition: transform 0.2s, box-shadow 0.2s;
 832 |         }
 833 |         
 834 |         .score-card:hover {
 835 |             transform: translateY(-3px);
 836 |             box-shadow: 0 12px 40px rgba(0,0,0,0.4);
 837 |         }
 838 |         
 839 |         .score-card-title {
 840 |             font-size: 12px;
 841 |             color: #64748b;
 842 |             margin-bottom: 20px;
 843 |             font-weight: 600;
 844 |             letter-spacing: 0.5px;
 845 |             text-transform: uppercase;
 846 |         }
 847 |         
 848 |         .score-circle {
 849 |             width: 100px;
 850 |             height: 100px;
 851 |             margin: 0 auto 16px;
 852 |             position: relative;
 853 |         }
 854 |         
 855 |         .score-circle svg {
 856 |             transform: rotate(-90deg);
 857 |         }
 858 |         
 859 |         .score-value {
 860 |             position: absolute;
 861 |             top: 50%;
 862 |             left: 50%;
 863 |             transform: translate(-50%, -50%);
 864 |             font-size: 22px;
 865 |             font-weight: 800;
 866 |         }
 867 |         
 868 |         .score-label {
 869 |             font-size: 11px;
 870 |             color: #475569;
 871 |             margin-top: 8px;
 872 |         }
 873 |         
 874 |         .section {
 875 |             background: #111827;
 876 |             border-radius: 20px;
 877 |             padding: 36px;
 878 |             margin-bottom: 32px;
 879 |             border: 1px solid rgba(255, 255, 255, 0.06);
 880 |         }
 881 |         
 882 |         .section-header {
 883 |             display: flex;
 884 |             align-items: center;
 885 |             gap: 12px;
 886 |             margin-bottom: 24px;
 887 |         }
 888 |         
 889 |         .section-header svg {
 890 |             width: 24px;
 891 |             height: 24px;
 892 |         }
 893 |         
 894 |         .section-title {
 895 |             font-size: 20px;
 896 |             font-weight: 700;
 897 |             letter-spacing: -0.3px;
 898 |         }
 899 |         
 900 |         .quick-win-card {
 901 |             background: rgba(255, 255, 255, 0.02);
 902 |             border-radius: 14px;
 903 |             padding: 20px 24px;
 904 |             margin-bottom: 12px;
 905 |             border: 1px solid rgba(255, 255, 255, 0.06);
 906 |             border-left: 4px solid;
 907 |             transition: background 0.2s;
 908 |         }
 909 |         
 910 |         .quick-win-card:hover {
 911 |             background: rgba(255, 255, 255, 0.04);
 912 |         }
 913 |         
 914 |         .quick-win-card.easy { border-left-color: #10b981; }
 915 |         .quick-win-card.medium { border-left-color: #f59e0b; }
 916 |         .quick-win-card.hard { border-left-color: #ef4444; }
 917 |         
 918 |         .quick-win-header {
 919 |             display: flex;
 920 |             justify-content: space-between;
 921 |             align-items: start;
 922 |             margin-bottom: 12px;
 923 |         }
 924 |         
 925 |         .quick-win-title {
 926 |             font-size: 15px;
 927 |             font-weight: 600;
 928 |             color: #fff;
 929 |         }
 930 |         
 931 |         .quick-win-badges {
 932 |             display: flex;
 933 |             gap: 8px;
 934 |         }
 935 |         
 936 |         .badge {
 937 |             padding: 3px 10px;
 938 |             border-radius: 8px;
 939 |             font-size: 11px;
 940 |             font-weight: 600;
 941 |         }
 942 |         
 943 |         .badge.easy {
 944 |             background: rgba(16, 185, 129, 0.1);
 945 |             color: #34d399;
 946 |             border: 1px solid rgba(52, 211, 153, 0.2);
 947 |         }
 948 |         
 949 |         .badge.medium {
 950 |             background: rgba(245, 158, 11, 0.1);
 951 |             color: #fbbf24;
 952 |             border: 1px solid rgba(251, 191, 36, 0.2);
 953 |         }
 954 |         
 955 |         .badge.hard {
 956 |             background: rgba(239, 68, 68, 0.1);
 957 |             color: #f87171;
 958 |             border: 1px solid rgba(248, 113, 113, 0.2);
 959 |         }
 960 |         
 961 |         .quick-win-description {
 962 |             color: #64748b;
 963 |             margin-top: 6px;
 964 |             font-size: 13px;
 965 |             line-height: 1.5;
 966 |         }
 967 |         
 968 |         .quick-win-file {
 969 |             font-family: 'Courier New', monospace;
 970 |             font-size: 11px;
 971 |             color: #475569;
 972 |             background: rgba(255, 255, 255, 0.04);
 973 |             padding: 3px 10px;
 974 |             border-radius: 6px;
 975 |             display: inline-block;
 976 |             margin-top: 10px;
 977 |         }
 978 |         
 979 |         .ai-summary {
 980 |             color: #94a3b8;
 981 |             font-size: 14px;
 982 |             line-height: 1.8;
 983 |         }
 984 |         
 985 |         .ai-summary h2 {
 986 |             font-size: 16px;
 987 |             font-weight: 700;
 988 |             margin: 24px 0 10px;
 989 |             color: #f1f5f9;
 990 |             padding-left: 12px;
 991 |             border-left: 3px solid #2563eb;
 992 |             letter-spacing: -0.2px;
 993 |         }
 994 |         
 995 |         .ai-summary h3 {
 996 |             font-size: 14px;
 997 |             font-weight: 600;
 998 |             margin: 16px 0 8px;
 999 |             color: #cbd5e1;
1000 |         }
1001 |         
1002 |         .ai-summary p {
1003 |             margin-bottom: 12px;
1004 |         }
1005 |         
1006 |         .ai-summary ul {
1007 |             margin: 8px 0;
1008 |             padding-left: 20px;
1009 |         }
1010 |         
1011 |         .ai-summary li {
1012 |             margin-bottom: 6px;
1013 |             color: #94a3b8;
1014 |         }
1015 |         
1016 |         .ai-summary strong {
1017 |             color: #e2e8f0;
1018 |             font-weight: 600;
1019 |         }
1020 |         
1021 |         .file-search {
1022 |             margin-bottom: 16px;
1023 |         }
1024 |         
1025 |         .file-search input {
1026 |             width: 100%;
1027 |             background: #0f172a;
1028 |             border: 1px solid #1e293b;
1029 |             border-radius: 10px;
1030 |             padding: 12px 16px;
1031 |             color: #fff;
1032 |             font-size: 13px;
1033 |             font-family: 'Inter', sans-serif;
1034 |             transition: border-color 0.2s, box-shadow 0.2s;
1035 |         }
1036 |         
1037 |         .file-search input:focus {
1038 |             border-color: #3b82f6;
1039 |             box-shadow: 0 0 0 3px rgba(59,130,246,0.1);
1040 |             outline: none;
1041 |         }
1042 |         
1043 |         .file-list {
1044 |             max-height: 500px;
1045 |             overflow-y: auto;
1046 |             display: flex;
1047 |             flex-direction: column;
1048 |             gap: 2px;
1049 |         }
1050 |         
1051 |         .file-item {
1052 |             display: flex;
1053 |             align-items: center;
1054 |             justify-content: space-between;
1055 |             padding: 10px 14px;
1056 |             border-radius: 10px;
1057 |             transition: background 0.15s;
1058 |             cursor: default;
1059 |         }
1060 |         
1061 |         .file-item:hover {
1062 |             background: rgba(255, 255, 255, 0.04);
1063 |         }
1064 |         
1065 |         .file-info {
1066 |             display: flex;
1067 |             align-items: center;
1068 |             gap: 10px;
1069 |             flex: 1;
1070 |             min-width: 0;
1071 |         }
1072 |         
1073 |         .file-icon {
1074 |             width: 16px;
1075 |             height: 16px;
1076 |             flex-shrink: 0;
1077 |         }
1078 |         
1079 |         .file-path {
1080 |             font-size: 13px;
1081 |             color: #94a3b8;
1082 |             font-family: 'Courier New', monospace;
1083 |             white-space: nowrap;
1084 |             overflow: hidden;
1085 |             text-overflow: ellipsis;
1086 |         }
1087 |         
1088 |         .file-actions {
1089 |             display: flex;
1090 |             gap: 4px;
1091 |             flex-shrink: 0;
1092 |         }
1093 |         
1094 |         .icon-btn {
1095 |             width: 30px;
1096 |             height: 30px;
1097 |             background: transparent;
1098 |             border: 1px solid transparent;
1099 |             border-radius: 7px;
1100 |             display: flex;
1101 |             align-items: center;
1102 |             justify-content: center;
1103 |             cursor: pointer;
1104 |             transition: all 0.15s;
1105 |             color: #475569;
1106 |         }
1107 |         
1108 |         .icon-btn:hover {
1109 |             background: rgba(59, 130, 246, 0.1);
1110 |             border-color: rgba(59, 130, 246, 0.2);
1111 |             color: #60a5fa;
1112 |         }
1113 |         
1114 |         .icon-btn svg {
1115 |             width: 14px;
1116 |             height: 14px;
1117 |             stroke: currentColor;
1118 |         }
1119 |         
1120 |         .icon-btn.success {
1121 |             color: #10b981;
1122 |             border-color: rgba(16, 185, 129, 0.3);
1123 |             background: rgba(16, 185, 129, 0.1);
1124 |         }
1125 |         
1126 |         .file-viewer-modal {
1127 |             position: fixed;
1128 |             top: 0;
1129 |             left: 0;
1130 |             right: 0;
1131 |             bottom: 0;
1132 |             background: rgba(0, 0, 0, 0.75);
1133 |             backdrop-filter: blur(8px);
1134 |             display: none;
1135 |             align-items: center;
1136 |             justify-content: center;
1137 |             z-index: 2000;
1138 |             padding: 20px;
1139 |         }
1140 |         
1141 |         .file-viewer-modal.active {
1142 |             display: flex;
1143 |         }
1144 |         
1145 |         .file-viewer {
1146 |             background: #0d1424;
1147 |             border-radius: 18px;
1148 |             width: 80vw;
1149 |             height: 80vh;
1150 |             display: flex;
1151 |             flex-direction: column;
1152 |             border: 1px solid rgba(255, 255, 255, 0.08);
1153 |             box-shadow: 0 40px 80px rgba(0,0,0,0.6);
1154 |         }
1155 |         
1156 |         .file-viewer-header {
1157 |             display: flex;
1158 |             justify-content: space-between;
1159 |             align-items: center;
1160 |             padding: 16px 24px;
1161 |             border-bottom: 1px solid rgba(255, 255, 255, 0.06);
1162 |             background: #111827;
1163 |             border-radius: 18px 18px 0 0;
1164 |         }
1165 |         
1166 |         .file-viewer-title {
1167 |             font-size: 13px;
1168 |             font-weight: 600;
1169 |             font-family: 'Courier New', monospace;
1170 |             color: #94a3b8;
1171 |         }
1172 |         
1173 |         .file-viewer-actions {
1174 |             display: flex;
1175 |             gap: 12px;
1176 |         }
1177 |         
1178 |         .file-viewer-content {
1179 |             flex: 1;
1180 |             overflow: auto;
1181 |             padding: 24px;
1182 |         }
1183 |         
1184 |         .file-viewer-code {
1185 |             background: transparent;
1186 |             border-radius: 8px;
1187 |             padding: 0;
1188 |             font-family: 'Courier New', monospace;
1189 |             font-size: 12.5px;
1190 |             line-height: 1.7;
1191 |             color: #e2e8f0;
1192 |             white-space: pre-wrap;
1193 |             word-break: break-all;
1194 |         }
1195 |         
1196 |         .answer-panel {
1197 |             background: #111827;
1198 |             border-radius: 16px;
1199 |             padding: 28px;
1200 |             margin-top: 24px;
1201 |             border: 1px solid rgba(255, 255, 255, 0.07);
1202 |         }
1203 |         
1204 |         .answer-title {
1205 |             font-size: 13px;
1206 |             font-weight: 700;
1207 |             margin-bottom: 16px;
1208 |             color: #10b981;
1209 |             letter-spacing: 0.5px;
1210 |             text-transform: uppercase;
1211 |         }
1212 |         
1213 |         .answer-content {
1214 |             color: #94a3b8;
1215 |             font-size: 14px;
1216 |             line-height: 1.8;
1217 |         }
1218 |         .spinner { width: 18px; height: 18px; border: 2px solid rgba(255, 255, 255, 0.3); border-top-color: #fff; border-radius: 50%; animation: spin 0.6s linear infinite; }
1219 |         @keyframes spin { to { transform: rotate(360deg); } }
1220 |         .btn:disabled { opacity: 0.6; cursor: not-allowed; }
1221 |     </style>
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files
index.html

# VSCode Open Tabs
requirements.txt,ui.py,analyzer.py,main.py,update_html.py,generate_html.py,index.html,.gitignore,.env

# Current Time
Current time in ISO 8601 UTC format: 2026-05-01T20:50:11.865Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.10

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

Now I'll apply the CSS changes to replace the results page styles with the exact design system provided. I'll need to:

1. First, check if there's a `:root` block to add the CSS variables to
2. Replace all the results page CSS (lines 762-1220) with the new styles

Let me search for the `:root` block:

<search_files>
<path>E:\codecompass\index.html</path>
<regex>^\s*body\s*\{</regex>
</search_files>

---

**User:**

[search_files for '^\s*body\s*\{'] Result:
Found 1 result.

# index.html
 17 | 
 18 |         body {
 19 |             font-family: 'Inter', sans-serif;
----
<environment_details>
# VSCode Visible Files
index.html

# VSCode Open Tabs
requirements.txt,ui.py,analyzer.py,main.py,update_html.py,generate_html.py,index.html,.gitignore,.env

# Current Time
Current time in ISO 8601 UTC format: 2026-05-01T20:50:18.321Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.16

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

Perfect! Now I'll apply the changes. I need to:
1. Add a `:root` block with CSS variables after the `*` reset and before `body`
2. Replace all the results page CSS (from line 762 onwards)

<apply_diff>
<path>E:\codecompass\index.html</path>
<diff>
<<<<<<< SEARCH
:start_line:12
-------
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
=======
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --blue-400: #60a5fa;
            --blue-500: #3b82f6;
            --blue-600: #2563eb;
            --blue-700: #1d4ed8;
            --teal-500: #14b8a6;
            --slate-300: #cbd5e1;
            --slate-400: #94a3b8;
            --slate-500: #64748b;
            --slate-600: #475569;
            --slate-700: #334155;
            --slate-800: #1e293b;
            --slate-850: #172033;
            --slate-900: #0f172a;
            --slate-950: #080c14;
        }

        body {
>>>>>>> REPLACE
</diff>
</apply_diff>

---

**User:**

[apply_diff for 'E:\codecompass\index.html'] Result:
<file_write_result>
<path>E:\codecompass\index.html</path>
<operation>modified</operation>
<notice>
<i>You do not need to re-read the file, as you have seen all changes</i>
<i>Proceed with the task using these changes as the new baseline.</i>
</notice>
</file_write_result>

<notice>Making multiple related changes in a single apply_diff is more efficient. If other changes are needed in this file, please include them as additional SEARCH/REPLACE blocks.</notice>
<environment_details>
# VSCode Visible Files
index.html

# VSCode Open Tabs
requirements.txt,ui.py,analyzer.py,main.py,update_html.py,generate_html.py,index.html,.gitignore,.env

# Current Time
Current time in ISO 8601 UTC format: 2026-05-01T20:50:27.987Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.23

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

Now I'll replace all the results page CSS (from line 762 to 1220) with the new design system styles:

<apply_diff>
<path>E:\codecompass\index.html</path>
<diff>
<<<<<<< SEARCH
:start_line:776
-------
        
        /* NEW STYLES FOR RESULTS PAGE */
        .hidden { display: none !important; }
        
        .results-page {
            min-height: 100vh;
            background: #080c14;
            background-image: radial-gradient(circle, rgba(37,99,235,0.06) 1px, transparent 1px);
            background-size: 28px 28px;
            padding: 40px;
            font-family: 'Inter', sans-serif;
        }
        
        .results-container {
            max-width: 1400px;
            margin: 0 auto;
            font-family: 'Inter', sans-serif;
        }
        
        .results-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 40px;
            flex-wrap: wrap;
            gap: 20px;
        }
        
        .results-title {
            display: flex;
            align-items: center;
            gap: 16px;
        }
        
        .results-title h1 {
            font-size: 28px;
            font-weight: 800;
            letter-spacing: -0.5px;
        }
        
        .back-btn {
            background: rgba(255, 255, 255, 0.05);
            color: #94a3b8;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 10px 20px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 13px;
            font-weight: 600;
            transition: all 0.2s;
        }
        
        .back-btn:hover {
            background: rgba(255, 255, 255, 0.1);
            color: #fff;
        }
        
        .score-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        
        .score-card {
            background: linear-gradient(145deg, #1a2235, #111827);
            border-radius: 20px;
            padding: 28px 20px;
            border: 1px solid rgba(255, 255, 255, 0.07);
            text-align: center;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        .score-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 40px rgba(0,0,0,0.4);
        }
        
        .score-card-title {
            font-size: 12px;
            color: #64748b;
            margin-bottom: 20px;
            font-weight: 600;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }
        
        .score-circle {
            width: 100px;
            height: 100px;
            margin: 0 auto 16px;
            position: relative;
        }
        
        .score-circle svg {
            transform: rotate(-90deg);
        }
        
        .score-value {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 22px;
            font-weight: 800;
        }
        
        .score-label {
            font-size: 11px;
            color: #475569;
            margin-top: 8px;
        }
        
        .section {
            background: #111827;
            border-radius: 20px;
            padding: 36px;
            margin-bottom: 32px;
            border: 1px solid rgba(255, 255, 255, 0.06);
        }
        
        .section-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 24px;
        }
        
        .section-header svg {
            width: 24px;
            height: 24px;
        }
        
        .section-title {
            font-size: 20px;
            font-weight: 700;
            letter-spacing: -0.3px;
        }
        
        .quick-win-card {
            background: rgba(255, 255, 255, 0.02);
            border-radius: 14px;
            padding: 20px 24px;
            margin-bottom: 12px;
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-left: 4px solid;
            transition: background 0.2s;
        }
        
        .quick-win-card:hover {
            background: rgba(255, 255, 255, 0.04);
        }
        
        .quick-win-card.easy { border-left-color: #10b981; }
        .quick-win-card.medium { border-left-color: #f59e0b; }
        .quick-win-card.hard { border-left-color: #ef4444; }
        
        .quick-win-header {
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 12px;
        }
        
        .quick-win-title {
            font-size: 15px;
            font-weight: 600;
            color: #fff;
        }
        
        .quick-win-badges {
            display: flex;
            gap: 8px;
        }
        
        .badge {
            padding: 3px 10px;
            border-radius: 8px;
            font-size: 11px;
            font-weight: 600;
        }
        
        .badge.easy {
            background: rgba(16, 185, 129, 0.1);
            color: #34d399;
            border: 1px solid rgba(52, 211, 153, 0.2);
        }
        
        .badge.medium {
            background: rgba(245, 158, 11, 0.1);
            color: #fbbf24;
            border: 1px solid rgba(251, 191, 36, 0.2);
        }
        
        .badge.hard {
            background: rgba(239, 68, 68, 0.1);
            color: #f87171;
            border: 1px solid rgba(248, 113, 113, 0.2);
        }
        
        .quick-win-description {
            color: #64748b;
            margin-top: 6px;
            font-size: 13px;
            line-height: 1.5;
        }
        
        .quick-win-file {
            font-family: 'Courier New', monospace;
            font-size: 11px;
            color: #475569;
            background: rgba(255, 255, 255, 0.04);
            padding: 3px 10px;
            border-radius: 6px;
            display: inline-block;
            margin-top: 10px;
        }
        
        .ai-summary {
            color: #94a3b8;
            font-size: 14px;
            line-height: 1.8;
        }
        
        .ai-summary h2 {
            font-size: 16px;
            font-weight: 700;
            margin: 24px 0 10px;
            color: #f1f5f9;
            padding-left: 12px;
            border-left: 3px solid #2563eb;
            letter-spacing: -0.2px;
        }
        
        .ai-summary h3 {
            font-size: 14px;
            font-weight: 600;
            margin: 16px 0 8px;
            color: #cbd5e1;
        }
        
        .ai-summary p {
            margin-bottom: 12px;
        }
        
        .ai-summary ul {
            margin: 8px 0;
            padding-left: 20px;
        }
        
        .ai-summary li {
            margin-bottom: 6px;
            color: #94a3b8;
        }
        
        .ai-summary strong {
            color: #e2e8f0;
            font-weight: 600;
        }
        
        .file-search {
            margin-bottom: 16px;
        }
        
        .file-search input {
            width: 100%;
            background: #0f172a;
            border: 1px solid #1e293b;
            border-radius: 10px;
            padding: 12px 16px;
            color: #fff;
            font-size: 13px;
            font-family: 'Inter', sans-serif;
            transition: border-color 0.2s, box-shadow 0.2s;
        }
        
        .file-search input:focus {
            border-color: #3b82f6;
            box-shadow: 0 0 0 3px rgba(59,130,246,0.1);
            outline: none;
        }
        
        .file-list {
            max-height: 500px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 2px;
        }
        
        .file-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 14px;
            border-radius: 10px;
            transition: background 0.15s;
            cursor: default;
        }
        
        .file-item:hover {
            background: rgba(255, 255, 255, 0.04);
        }
        
        .file-info {
            display: flex;
            align-items: center;
            gap: 10px;
            flex: 1;
            min-width: 0;
        }
        
        .file-icon {
            width: 16px;
            height: 16px;
            flex-shrink: 0;
        }
        
        .file-path {
            font-size: 13px;
            color: #94a3b8;
            font-family: 'Courier New', monospace;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        
        .file-actions {
            display: flex;
            gap: 4px;
            flex-shrink: 0;
        }
        
        .icon-btn {
            width: 30px;
            height: 30px;
            background: transparent;
            border: 1px solid transparent;
            border-radius: 7px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.15s;
            color: #475569;
        }
        
        .icon-btn:hover {
            background: rgba(59, 130, 246, 0.1);
            border-color: rgba(59, 130, 246, 0.2);
            color: #60a5fa;
        }
        
        .icon-btn svg {
            width: 14px;
            height: 14px;
            stroke: currentColor;
        }
        
        .icon-btn.success {
            color: #10b981;
            border-color: rgba(16, 185, 129, 0.3);
            background: rgba(16, 185, 129, 0.1);
        }
        
        .file-viewer-modal {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(8px);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 2000;
            padding: 20px;
        }
        
        .file-viewer-modal.active {
            display: flex;
        }
        
        .file-viewer {
            background: #0d1424;
            border-radius: 18px;
            width: 80vw;
            height: 80vh;
            display: flex;
            flex-direction: column;
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 40px 80px rgba(0,0,0,0.6);
        }
        
        .file-viewer-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px 24px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            background: #111827;
            border-radius: 18px 18px 0 0;
        }
        
        .file-viewer-title {
            font-size: 13px;
            font-weight: 600;
            font-family: 'Courier New', monospace;
            color: #94a3b8;
        }
        
        .file-viewer-actions {
            display: flex;
            gap: 12px;
        }
        
        .file-viewer-content {
            flex: 1;
            overflow: auto;
            padding: 24px;
        }
        
        .file-viewer-code {
            background: transparent;
            border-radius: 8px;
            padding: 0;
            font-family: 'Courier New', monospace;
            font-size: 12.5px;
            line-height: 1.7;
            color: #e2e8f0;
            white-space: pre-wrap;
            word-break: break-all;
        }
        
        .answer-panel {
            background: #111827;
            border-radius: 16px;
            padding: 28px;
            margin-top: 24px;
            border: 1px solid rgba(255, 255, 255, 0.07);
        }
        
        .answer-title {
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 16px;
            color: #10b981;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }
        
        .answer-content {
            color: #94a3b8;
            font-size: 14px;
            line-height: 1.8;
        }
        .spinner { width: 18px; height: 18px; border: 2px solid rgba(255, 255, 255, 0.3); border-top-color: #fff; border-radius: 50%; animation: spin 0.6s linear infinite; }
        @keyframes spin { to { transform: rotate(360deg); } }
        .btn:disabled { opacity: 0.6; cursor: not-allowed; }
=======
        
        /* ── RESULTS PAGE ── */
        .hidden { display: none !important; }
        
        .results-page {
            background: #080c14;
            background-image: radial-gradient(circle, rgba(37,99,235,.05) 1px, transparent 1px);
            background-size: 28px 28px;
            min-height: 100vh;
            padding: 48px 72px;
            font-family: 'Inter', sans-serif;
            -webkit-font-smoothing: antialiased;
        }
        
        .results-container {
            max-width: 1280px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 28px;
        }
        
        /* ── HEADER ── */
        .results-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 24px 32px;
            background: #111827;
            border-radius: 18px;
            border: 1px solid rgba(255,255,255,.06);
            box-shadow: 0 1px 3px rgba(0,0,0,.3);
        }
        
        .results-title {
            display: flex;
            align-items: center;
            gap: 16px;
        }
        
        .results-title h1 {
            font-size: 22px;
            font-weight: 800;
            color: #f1f5f9;
            letter-spacing: -0.5px;
        }
        
        .results-title .powered-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(37,99,235,.1);
            border: 1px solid rgba(37,99,235,.2);
            border-radius: 20px;
            padding: 6px 14px;
            font-size: 12px;
            font-weight: 600;
            color: #60a5fa;
        }
        
        .back-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255,255,255,.04);
            border: 1px solid rgba(255,255,255,.08);
            color: #94a3b8;
            padding: 10px 20px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: 600;
            font-family: 'Inter', sans-serif;
            cursor: pointer;
            transition: background .18s, color .18s, border-color .18s;
        }
        
        .back-btn:hover {
            background: rgba(255,255,255,.08);
            color: #f1f5f9;
            border-color: rgba(255,255,255,.15);
        }
        
        /* ── SCORE CARDS ── */
        .score-cards {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 16px;
        }
        
        .score-card {
            background: linear-gradient(145deg, #111827, #0d1424);
            border: 1px solid rgba(255,255,255,.07);
            border-radius: 20px;
            padding: 28px 20px;
            text-align: center;
            transition: transform .2s, box-shadow .2s;
            position: relative;
            overflow: hidden;
        }
        
        .score-card::before {
            content: '';
            position: absolute;
            top: -40px; left: 50%;
            transform: translateX(-50%);
            width: 120px; height: 120px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(37,99,235,.07), transparent 70%);
            pointer-events: none;
        }
        
        .score-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 16px 48px rgba(0,0,0,.4);
        }
        
        .score-card-title {
            font-size: 11px;
            font-weight: 700;
            letter-spacing: .6px;
            text-transform: uppercase;
            color: #475569;
            margin-bottom: 20px;
        }
        
        .score-circle {
            width: 100px;
            height: 100px;
            margin: 0 auto 14px;
            position: relative;
        }
        
        .score-circle svg { transform: rotate(-90deg); }
        
        .score-value {
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            font-size: 26px;
            font-weight: 800;
            letter-spacing: -1px;
        }
        
        .score-label {
            font-size: 11px;
            color: #334155;
            margin-top: 4px;
        }
        
        /* ── SECTION WRAPPER ── */
        .section {
            background: #111827;
            border: 1px solid rgba(255,255,255,.06);
            border-radius: 20px;
            padding: 36px 40px;
        }
        
        .section-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 28px;
            padding-bottom: 20px;
            border-bottom: 1px solid rgba(255,255,255,.05);
        }
        
        .section-header svg {
            width: 20px; height: 20px;
            flex-shrink: 0;
        }
        
        .section-title {
            font-size: 18px;
            font-weight: 700;
            letter-spacing: -.3px;
            color: #f1f5f9;
        }
        
        /* ── QUICK WINS ── */
        .quick-win-card {
            background: rgba(255,255,255,.02);
            border: 1px solid rgba(255,255,255,.05);
            border-left: 3px solid;
            border-radius: 12px;
            padding: 18px 22px;
            margin-bottom: 10px;
            transition: background .15s;
        }
        
        .quick-win-card:hover { background: rgba(255,255,255,.04); }
        
        .quick-win-card.easy   { border-left-color: #10b981; }
        .quick-win-card.medium { border-left-color: #f59e0b; }
        .quick-win-card.hard   { border-left-color: #ef4444; }
        
        .quick-win-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 12px;
        }
        
        .quick-win-title {
            font-size: 14px;
            font-weight: 600;
            color: #e2e8f0;
            line-height: 1.4;
        }
        
        .quick-win-description {
            font-size: 12.5px;
            color: #64748b;
            margin-top: 6px;
            line-height: 1.55;
        }
        
        .quick-win-file {
            display: inline-block;
            font-family: 'Courier New', monospace;
            font-size: 11px;
            color: #475569;
            background: rgba(255,255,255,.04);
            border: 1px solid rgba(255,255,255,.06);
            padding: 2px 8px;
            border-radius: 5px;
            margin-top: 8px;
        }
        
        .quick-win-badges { display: flex; gap: 6px; flex-shrink: 0; }
        
        .badge {
            font-size: 11px;
            font-weight: 600;
            padding: 3px 10px;
            border-radius: 8px;
            white-space: nowrap;
            letter-spacing: .3px;
        }
        
        .badge.easy   { background: rgba(16,185,129,.1);  color: #34d399; border: 1px solid rgba(52,211,153,.2); }
        .badge.medium { background: rgba(245,158,11,.1);  color: #fbbf24; border: 1px solid rgba(251,191,36,.2); }
        .badge.hard   { background: rgba(239,68,68,.1);   color: #f87171; border: 1px solid rgba(248,113,113,.2); }
        
        /* ── AI SUMMARY ── */
        .ai-summary {
            color: #94a3b8;
            font-size: 14px;
            line-height: 1.85;
        }
        
        .ai-summary h2 {
            font-size: 15px;
            font-weight: 700;
            color: #f1f5f9;
            margin: 28px 0 10px;
            padding-left: 14px;
            border-left: 3px solid #2563eb;
            letter-spacing: -.2px;
        }
        
        .ai-summary h3 { font-size: 14px; font-weight: 600; color: #cbd5e1; margin: 16px 0 8px; }
        .ai-summary strong { color: #e2e8f0; }
        .ai-summary ul { padding-left: 20px; margin: 10px 0; }
        .ai-summary li { margin-bottom: 7px; color: #94a3b8; }
        
        /* ── FILE EXPLORER ── */
        #fileSearchInput {
            width: 100%;
            background: #0d1424;
            border: 1px solid rgba(255,255,255,.08);
            border-radius: 12px;
            padding: 12px 16px;
            color: #e2e8f0;
            font-size: 13px;
            font-family: 'Inter', sans-serif;
            margin-bottom: 16px;
            transition: border-color .2s, box-shadow .2s;
        }
        
        #fileSearchInput:focus {
            outline: none;
            border-color: #3b82f6;
            box-shadow: 0 0 0 3px rgba(59,130,246,.1);
        }
        
        #fileSearchInput::placeholder { color: #334155; }
        
        .file-list { display: flex; flex-direction: column; gap: 1px; }
        
        .file-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 9px 12px;
            border-radius: 8px;
            transition: background .12s;
        }
        
        .file-item:hover { background: rgba(255,255,255,.04); }
        
        .file-info {
            display: flex;
            align-items: center;
            gap: 10px;
            flex: 1;
            min-width: 0;
        }
        
        .file-icon { width: 15px; height: 15px; flex-shrink: 0; opacity: .8; }
        
        .file-path {
            font-size: 12.5px;
            color: #64748b;
            font-family: 'Courier New', monospace;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        
        .file-item:hover .file-path { color: #94a3b8; }
        
        .file-actions {
            display: flex;
            gap: 2px;
            flex-shrink: 0;
            opacity: 0;
            transition: opacity .15s;
        }
        
        .file-item:hover .file-actions { opacity: 1; }
        
        .icon-btn {
            width: 28px; height: 28px;
            background: transparent;
            border: 1px solid transparent;
            border-radius: 6px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #475569;
            transition: all .15s;
        }
        
        .icon-btn svg { width: 13px; height: 13px; stroke: currentColor; }
        
        .icon-btn:hover {
            background: rgba(37,99,235,.1);
            border-color: rgba(37,99,235,.2);
            color: #60a5fa;
        }
        
        .icon-btn.success {
            color: #10b981;
            background: rgba(16,185,129,.1);
            border-color: rgba(16,185,129,.2);
        }
        
        /* ── FILE VIEWER MODAL ── */
        .file-viewer-modal {
            position: fixed; inset: 0;
            background: rgba(0,0,0,.72);
            backdrop-filter: blur(8px);
            z-index: 2000;
            display: none;
            align-items: center;
            justify-content: center;
        }
        
        .file-viewer-modal.active { display: flex; }
        
        .file-viewer {
            width: 80vw; height: 80vh;
            background: #0d1424;
            border: 1px solid rgba(255,255,255,.08);
            border-radius: 18px;
            box-shadow: 0 40px 80px rgba(0,0,0,.6);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            animation: modalIn .25s cubic-bezier(.16,1,.3,1);
        }
        
        @keyframes modalIn {
            from { opacity:0; transform: scale(.96) translateY(12px); }
            to   { opacity:1; transform: scale(1)   translateY(0); }
        }
        
        .file-viewer-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px 24px;
            background: #111827;
            border-bottom: 1px solid rgba(255,255,255,.06);
            flex-shrink: 0;
        }
        
        .file-viewer-title {
            font-family: 'Courier New', monospace;
            font-size: 13px;
            color: #64748b;
        }
        
        .file-viewer-actions { display: flex; gap: 6px; }
        
        .file-viewer-content {
            flex: 1;
            overflow: auto;
            padding: 24px;
        }
        
        .file-viewer-code {
            font-family: 'Courier New', monospace;
            font-size: 12.5px;
            line-height: 1.7;
            color: #e2e8f0;
            background: transparent;
            white-space: pre-wrap;
            word-break: break-all;
        }
        
        /* ── ANSWER PANEL ── */
        .answer-panel {
            background: #0d1424;
            border: 1px solid rgba(16,185,129,.15);
            border-radius: 14px;
            padding: 28px 32px;
            margin-top: 20px;
        }
        
        .answer-title {
            font-size: 11px;
            font-weight: 700;
            letter-spacing: .6px;
            text-transform: uppercase;
            color: #10b981;
            margin-bottom: 16px;
        }
        
        .answer-content {
            font-size: 14px;
            color: #94a3b8;
            line-height: 1.8;
        }
        
        /* ── SPINNER ── */
        .spinner {
            width: 16px; height: 16px;
            border: 2px solid rgba(255,255,255,.25);
            border-top-color: #fff;
            border-radius: 50%;
            animation: spin .6s linear infinite;
        }
        
        @keyframes spin { to { transform: rotate(360deg); } }
        
        /* ── RESPONSIVE ── */
        @media (max-width: 1024px) {
            .score-cards { grid-template-columns: repeat(3, 1fr); }
            .results-page { padding: 32px 24px; }
        }
        
        @media (max-width: 640px) {
            .score-cards { grid-template-columns: repeat(2, 1fr); }
            .file-viewer { width: 95vw; height: 90vh; }
        }
        
        .btn:disabled { opacity: 0.6; cursor: not-allowed; }
>>>>>>> REPLACE
</diff>
</apply_diff>

---

**User:**

[apply_diff for 'E:\codecompass\index.html'] Result:
<file_write_result>
<path>E:\codecompass\index.html</path>
<operation>modified</operation>
<notice>
<i>You do not need to re-read the file, as you have seen all changes</i>
<i>Proceed with the task using these changes as the new baseline.</i>
</notice>
</file_write_result>

<notice>Making multiple related changes in a single apply_diff is more efficient. If other changes are needed in this file, please include them as additional SEARCH/REPLACE blocks.</notice>
<environment_details>
# VSCode Visible Files
index_backup.html

# VSCode Open Tabs
requirements.txt,ui.py,analyzer.py,main.py,update_html.py,index.html,index_backup.html,.gitignore,.env

# Current Time
Current time in ISO 8601 UTC format: 2026-05-01T20:51:58.594Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.31

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

<attempt_completion>
<result>
Successfully replaced ALL results page CSS in E:\codecompass\index.html to match the IBM Bob design system:

✅ **Added CSS Variables to :root:**
- Added 14 new color variables (--blue-400 through --slate-950)
- Merged into existing style structure without duplication

✅ **Replaced Complete Results Page CSS:**
- Updated .results-page with refined padding (48px 72px) and background
- Enhanced .results-header with card-style design and shadow
- Refined .score-cards grid (5 columns) with gradient backgrounds and ::before pseudo-element
- Updated all section styling with proper spacing and borders
- Improved .quick-win-card with 3px left border and refined hover states
- Enhanced .ai-summary with better typography and spacing
- Refined file explorer (#fileSearchInput, .file-item) with improved interactions
- Updated .file-viewer-modal with new animation (modalIn)
- Styled .answer-panel with green accent border
- Added responsive breakpoints for tablets and mobile

✅ **Preserved:**
- All JavaScript functionality intact
- All HTML structure and IDs unchanged
- All class names unchanged
- Hero section and other page styles untouched

The results page now matches the exact design system from E:\IBM Bob\index.html with refined colors, spacing, typography, and interactions.
</result>
</attempt_completion>


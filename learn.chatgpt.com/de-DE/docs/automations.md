<!-- source: https://learn.chatgpt.com/de-DE/docs/automations -->

Plane wiederkehrende Aufgaben, die im Hintergrund ausgeführt werden. In ChatGPT im Web und auf Mobilgeräten
können auch unterstützte App-Ereignisse Aufgaben auslösen, sofern dein Tarif dies unterstützt. Prüfe aktive,
pausierte und abgeschlossene Aufgaben sowie die letzten Ausführungen unter **Geplant**. Für komplexere Arbeiten kannst du
geplante Aufgaben mit [Skills](/de-DE/codex/build-skills) kombinieren.

In der ChatGPT-Desktop-App können geplante Aufgaben mit lokalen Projekten arbeiten und
im Projektverzeichnis oder in einem isolierten Worktree ausgeführt werden. Lass den Computer eingeschaltet und
die App laufen, wenn eine geplante Aufgabe lokale Dateien benötigt.

Wenn geplante Aufgaben für deinen Workspace aktiviert sind, erstelle sie im Web über Chat oder
ChatGPT Work und verwalte ihre Ausführungen unter **Geplant**. Aufgaben im Web
können hochgeladenen Kontext und verbundene Tools nutzen, aber nicht direkt in
einem Ordner auf deinem Computer arbeiten.

Die Verwaltungsoberfläche „Geplant“ ist in Codex CLI nicht verfügbar. Verwende ChatGPT im Web
oder die Desktop-App, um geplante Aufgaben zu erstellen und zu verwalten. Mit der CLI kannst du zunächst
einen Prompt, einen Skill oder ein Skript vorbereiten und testen.

Die Verwaltungsoberfläche „Geplant“ ist in der IDE-Erweiterung nicht verfügbar. Verwende
ChatGPT im Web oder die Desktop-App, um geplante Aufgaben zu erstellen und zu verwalten. Mit
der IDE-Erweiterung kannst du zunächst einen Prompt, einen Skill oder eine Änderung am Workspace
vorbereiten und testen.

<a id="managing-tasks"></a>
<a id="ask-codex-to-create-or-update-automations"></a>
<a id="ask-chatgpt-to-create-or-update-scheduled-tasks"></a>
<a id="thread-automations"></a>
<a id="scheduled-tasks-in-threads"></a>
<a id="scheduled-tasks-in-chats"></a>
<a id="schedule-work-from-a-task"></a>
<a id="schedule-a-task-inside-a-chat"></a>
<a id="test-automations"></a>
<a id="test-scheduled-tasks"></a>
<a id="worktree-cleanup-for-automations"></a>
<a id="worktree-cleanup-for-scheduled-tasks"></a>
<a id="permissions-and-security-model"></a>
<a id="examples"></a>
<a id="automatically-create-new-skills"></a>
<a id="stay-up-to-date-with-your-project"></a>
<a id="combining-automations-with-skills-to-fix-your-own-bugs"></a>
<a id="combining-scheduled-tasks-with-skills-to-fix-your-own-bugs"></a>

## Geplante Aufgaben im Web verwalten

Öffne **Geplant** , um den Aufgabenstatus und die letzten Ausführungen zu prüfen. Verwende eine eigenständige geplante Aufgabe,
wenn jede Ausführung mit dem gespeicherten Prompt beginnen soll. Verwende eine geplante Aufgabe in einem Chat,
wenn ChatGPT in denselben Chat zurückkehren und dessen vorhandenen
Kontext weiterverwenden soll.

Geplante Aufgaben im Web können hochgeladene Dateien, verbundene Tools, Skills und
Plug-ins verwenden, die für diesen Chat verfügbar sind. Sie halten zwischen den Ausführungen keinen lokalen Ordner oder
Worktree bereit. Hinterlege dauerhaft gültige Anweisungen im Prompt der Aufgabe
oder in einem angehängten Skill. Halte benötigtes Ausgangsmaterial in einem zugänglichen
Projekt, als Upload oder in einem verbundenen Dienst bereit.

Bevor du eine Aufgabe planst, teste ihren Prompt in einem normalen Web-Chat.
Prüfe die ersten Ausführungen und passe dann Prompt, Tools oder Ausführungsrhythmus an, wenn die
Ergebnisse zu allgemein ausfallen oder zusätzlichen Kontext benötigen.

## Aufgaben durch App-Ereignisse auslösen

Wenn dein Tarif dies unterstützt, können geplante Aufgaben ausgeführt werden, sobald ein unterstütztes
Ereignis in Gmail, Slack oder GitHub eintritt. Ereignisgesteuerte Aufgaben sind in ChatGPT im Web
und auf Mobilgeräten verfügbar. In der ChatGPT-Desktop-App, in Codex CLI und in der
IDE-Erweiterung sind sie nicht verfügbar.

Bitte ChatGPT, die Aufgabe zu erstellen. Beschreibe dann das auslösende Ereignis und was
bei dessen Eintreten geschehen soll. Der Auslöser legt fest, wann die Aufgabe ausgeführt wird; der gespeicherte
Prompt bestimmt, was bei jeder Ausführung geschieht. Eine Aufgabe kann mehrere Ereignisauslöser verwenden,
aber Ereignisauslöser nicht mit einem Zeitplan kombinieren.

Zu den unterstützten Ereignisauslösern gehören:

- **Gmail:** Neu eingehende Nachrichten, optional danach gefiltert, wer sie gesendet hat oder welchen Betreff sie haben.
- **Slack:** Neue Nachrichten in ausgewählten Kanälen, optional danach gefiltert, wer sie verfasst hat
  und ob Antworten in Threads einbezogen werden. Reaktionen, Bearbeitungen, Löschungen und
  Direktnachrichten werden nicht unterstützt.
- **GitHub:** Aktivitäten rund um Pull Requests in einem Repository. Filtere nach Pull Request,
  Titel, Label oder danach, wer ihn erstellt hat, und lege fest, ob Reviews, Kommentare, Commit-Updates
  oder nur Merges die Aufgabe auslösen sollen.

Verbinde und autorisiere die App, bevor du die Aufgabe erstellst. Füge in Slack
`@ChatGPT` zu jedem Kanal hinzu, den die Aufgabe überwacht. Bei GitHub muss die verbundene App
Zugriff auf das Repository haben.

Wenn mehrere passende Ereignisse kurz hintereinander eintreten, kann ChatGPT sie
in einer Ausführung zusammenfassen. Öffne **Geplant** , um ausstehende Ereignisse zu prüfen, oder wähle **Jetzt ausführen**,
um sie zu verarbeiten.

Die Verfügbarkeit hängt von deinem Tarif und den Workspace-Einstellungen ab. In verwalteten
Workspaces können Administrierende den Zugriff über die Berechtigung **Ereignisgesteuerte geplante
Aufgaben zulassen** steuern.

Plane beispielsweise eine Aufgabe, die Telemetriefehler auswertet und Korrekturen einreicht,
oder Berichte über aktuelle Änderungen an der Codebasis erstellt. Für fortlaufende Arbeiten, die
weiterhin denselben Kontext verwenden sollen, [plane eine Aufgabe in einem bestehenden Chat](#schedule-a-task-inside-a-chat).

Lass bei projektbezogenen geplanten Aufgaben den Computer eingeschaltet und die ChatGPT-Desktop-App
laufen. Das ausgewählte Projekt muss zum geplanten Ausführungszeitpunkt
noch auf dem Datenträger verfügbar sein.

In Git-Repositorys kannst du wählen, ob eine geplante Aufgabe in deinem lokalen
Projekt oder in einem neuen [Worktree](/de-DE/codex/environments/git-worktrees) ausgeführt wird. Beide Varianten laufen im
Hintergrund. Worktrees trennen Änderungen geplanter Aufgaben von noch nicht abgeschlossenen lokalen
Arbeiten. Bei der Ausführung in deinem lokalen Projekt können dagegen Dateien geändert werden, an denen du noch
arbeitest. In Projekten ohne Versionskontrolle werden geplante Aufgaben direkt im
Projektverzeichnis ausgeführt.

Du kannst für Modell und Reasoning-Aufwand auch die Standardeinstellungen beibehalten oder
beides explizit auswählen, wenn du mehr Kontrolle über die Ausführung der geplanten Aufgabe möchtest.

Wenn eine geplante Aufgabe `gpt-5.4` oder `gpt-5.4-mini` mit ChatGPT-Anmeldung verwendet,
aktualisiere sie, bevor diese Modelle am 31. August 2026 eingestellt werden. Ersetze `gpt-5.4` durch
`gpt-5.6-terra` und `gpt-5.4-mini` durch `gpt-5.6-luna`.

  

Geplante Aufgaben werden unbeaufsichtigt mit deinen standardmäßigen Sandbox-Einstellungen ausgeführt. Beginne mit den
geringsten Zugriffsrechten, mit denen die Aufgabe erfolgreich ausgeführt werden kann, und gewähre Netzwerkzugriff oder weitergehenden Dateizugriff
nur bei Bedarf. [Sandboxing verstehen](/de-DE/codex/sandboxing).

## Geplante Aufgaben verwalten

Alle geplanten Aufgaben und ihre Ausführungen findest du unter **Geplant** in der
Seitenleiste der ChatGPT-Desktop-App.

Die Ansicht **Geplant** dient als Posteingang. Dort erscheinen Ausführungen geplanter Aufgaben mit Ergebnissen.
Eine Ungelesen-Markierung zeigt an, wenn eine Ausführung deine Aufmerksamkeit erfordert.

  

Eigenständige geplante Aufgaben starten für jede geplante Ausführung einen neuen Chat und zeigen die
Ergebnisse unter **Geplant** an. Verwende sie, wenn jede Ausführung unabhängig sein oder eine
geplante Aufgabe in einem oder mehreren Projekten ausgeführt werden soll. Wenn du einen eigenen
Ausführungsrhythmus benötigst, nutze die Bedienelemente für benutzerdefinierte Zeitpläne. Bearbeite für komplexere Zeitpläne die
Wiederholungsregel (RRULE) nach RFC 5545, zum Beispiel
`RRULE:FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0`.

Bei Git-Repositorys kann jede geplante Aufgabe entweder in deinem lokalen Projekt oder
in einem eigenen [Worktree](/de-DE/codex/environments/git-worktrees) im Hintergrund ausgeführt werden. Verwende
Worktrees, wenn du Änderungen geplanter Aufgaben von noch nicht abgeschlossenen lokalen
Arbeiten trennen möchtest. Verwende den lokalen Modus, wenn die geplante Aufgabe direkt in deinem
Haupt-Checkout arbeiten soll. Beachte dabei, dass sie Dateien ändern kann, die du gerade bearbeitest.
In Projekten ohne Versionskontrolle werden geplante Aufgaben direkt im
Projektverzeichnis ausgeführt. Du kannst dieselbe geplante Aufgabe in mehreren Projekten ausführen lassen.

Geplante Aufgaben, die du mit ChatGPT Work im Web oder mit ChatGPT Work oder
Codex in der Desktop-App erstellst, können Plug-ins verwenden. Geplante Aufgaben können auch Skills verwenden.
Damit geplante Aufgaben wartbar bleiben und sich teamübergreifend teilen lassen, verwende
[Skills](/de-DE/codex/build-skills), um die Aktion festzulegen sowie Tools und Kontext bereitzustellen.
Wähle im Prompt der Aufgabe einen bestimmten Skill aus oder rufe ihn dort auf, wenn der Ablauf
nicht von der automatischen Tool-Auswahl abhängen soll.

## Bitte ChatGPT, geplante Aufgaben zu erstellen oder zu aktualisieren

Du kannst geplante Aufgaben in einem Chat mit ChatGPT oder Codex erstellen und aktualisieren.
Beschreibe, was erledigt werden soll, wann die Aufgabe laufen soll und ob jede Ausführung zum
aktuellen Chat zurückkehren oder einen neuen Chat starten soll. ChatGPT kann den Prompt entwerfen, das
passende Ziel auswählen und die Aufgabe aktualisieren, wenn sich ihr Umfang oder ihr Ausführungsrhythmus
ändert.

Bitte ChatGPT beispielsweise, eine Fortsetzung im aktuellen Chat zu planen, während ein
Deployment noch läuft, oder eine eigenständige geplante Aufgabe zu erstellen, die
ein Projekt regelmäßig prüft.

Skills können geplante Aufgaben ebenfalls erstellen oder aktualisieren. Ein Skill, der
einen Pull Request betreut, könnte beispielsweise eine geplante Aufgabe einrichten, die den
PR-Status mit dem GitHub-Plug-in prüft und neue Review-Rückmeldungen umsetzt.

## Eine Aufgabe in einem Chat planen

Plane eine Aufgabe in einem bestehenden Chat, wenn ChatGPT nach einem Zeitplan in diesen Chat
zurückkehren soll. Die geplante Aufgabe nutzt den vorhandenen Kontext des Chats, statt
jedes Mal mit einem neuen Prompt zu beginnen.

Geplante Aufgaben in einem Chat können für die laufende Nachverfolgung in Minutenintervallen
ausgeführt werden. Wenn du eine Rückmeldung zu einer bestimmten Uhrzeit brauchst, sind auch tägliche und wöchentliche
Zeitpläne möglich.

Plane eine Aufgabe in einem Chat für folgende Zwecke:

- einen lang laufenden Vorgang bis zu seinem Abschluss überwachen
- eine verbundene Quelle in festen Abständen prüfen, wenn du regelmäßig eine Momentaufnahme
statt einer Reaktion auf ein einzelnes unterstütztes App-Ereignis benötigst
- ChatGPT daran erinnern, eine Review-Schleife in einem festen Rhythmus fortzusetzen
- einen von einem Skill gesteuerten Ablauf mit Plug-ins ausführen, etwa um den PR-Status zu prüfen
und neue Rückmeldungen umzusetzen
- einen laufenden Recherche- oder Triage-Chat fortsetzen, ohne dessen Kontext zu verlieren

Verwende eine eigenständige geplante Aufgabe, wenn jede Ausführung unabhängig sein soll oder
Ergebnisse unter **Geplant** als separate Ausführungen erscheinen sollen.

Wenn du eine Aufgabe in einem Chat planst, formuliere den Prompt so, dass er dauerhaft verwendbar bleibt. Beschreibe darin,
was ChatGPT bei jeder geplanten Ausführung tun soll, wie es entscheiden soll, ob es
etwas Wichtiges zu melden gibt, und wann es aufhören oder dich um eine Eingabe bitten soll.

## Geplante Aufgaben testen

Bevor du eine Aufgabe planst, teste den Prompt zunächst manuell in einem normalen Chat.
So kannst du Folgendes prüfen:

- Der Prompt ist klar formuliert und legt den Aufgabenumfang korrekt fest.
- Mit der gewählten oder standardmäßigen Kombination aus Modell, Reasoning-Aufwand und Tools verhält sich die Aufgabe wie erwartet.
- Die erzeugte Ausgabe lässt sich überprüfen.

Wenn du mit geplanten Ausführungen beginnst, prüfe die ersten Ausgaben und passe den
Prompt oder den Ausführungsrhythmus bei Bedarf an.

In der ChatGPT-Desktop-App kannst du einen Skill im Prompt einer geplanten Aufgabe
mit `$skill-name` explizit auslösen.

## Worktrees für geplante Aufgaben bereinigen

Wenn du für Git-Repositorys Worktrees verwendest, können bei häufigen Ausführungen mit der Zeit
viele Worktrees entstehen. Archiviere geplante Ausführungen, die du nicht mehr benötigst, und hefte
Ausführungen nur an, wenn du ihre Worktrees behalten möchtest.

## Berechtigungen und Sicherheitsmodell

Geplante Aufgaben werden unbeaufsichtigt ausgeführt und verwenden deine standardmäßigen Sandbox-Einstellungen.

Eine leicht verständliche Erklärung dieser Grenzen findest du in der
[Übersicht zum Sandboxing](/de-DE/codex/sandboxing). Regeln für Dateisystem und Netzwerk
findest du unter [Berechtigungen](/de-DE/codex/permissions).

- Wenn dein Sandbox-Modus auf **Schreibgeschützt** eingestellt ist, schlagen Tool-Aufrufe fehl, wenn sie
  Dateien ändern, auf das Netzwerk zugreifen oder mit Apps auf deinem Computer arbeiten müssen.
  Erwäge, die Sandbox-Einstellungen auf Workspace-Schreibzugriff umzustellen.
- Wenn dein Sandbox-Modus auf **workspace-write** eingestellt ist, schlagen Tool-Aufrufe fehl, wenn sie
  Dateien außerhalb des Workspaces ändern, auf das Netzwerk zugreifen oder mit Apps
  auf deinem Computer arbeiten müssen. Du kannst bestimmte Befehle für die Ausführung außerhalb der
  Sandbox mithilfe von [Regeln](/de-DE/codex/agent-configuration/rules) freigeben.
- Wenn dein Sandbox-Modus auf **Vollzugriff** eingestellt ist, bergen geplante Aufgaben im Hintergrund
  ein erhöhtes Risiko: ChatGPT kann Dateien ändern, Befehle ausführen und auf das Netzwerk zugreifen,
  ohne nachzufragen. Erwäge, die Sandbox-Einstellungen auf Workspace-Schreibzugriff umzustellen und
  mithilfe von [Regeln](/de-DE/codex/agent-configuration/rules) gezielt festzulegen, welche Befehle der Agent
  mit Vollzugriff ausführen darf.

Wenn du in einer verwalteten Umgebung arbeitest, können Admins dieses Verhalten mit
verbindlichen Vorgaben einschränken. Beispielsweise können sie `approval_policy =
"never"` verbieten oder die zulässigen Sandbox-Modi einschränken. Siehe
[Von Admins durchgesetzte Anforderungen (`requirements.toml`)](/de-DE/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

Geplante Aufgaben verwenden `approval_policy = "never"`, wenn die Richtlinie deiner Organisation
dies zulässt. Falls die Vorgaben der Admins `approval_policy = "never"` untersagen,
gelten für geplante Aufgaben stattdessen die Genehmigungsregeln
deines ausgewählten Berechtigungsmodus.

## Beispiele

### Automatisch neue Skills erstellen

```markdown
Scan all of the `~/.codex/sessions` files from the past day and if there have been any issues using particular skills, update the skills to be more helpful. Personal skills only, no repo skills.

If there’s anything we’ve been doing often and struggle with that we should save as a skill to speed up future work, let’s do it.

Definitely don't feel like you need to update any- only if there's a good reason!

Let me know if you make any.

### Bei deinem Projekt auf dem Laufenden bleiben

```markdown
Look at the latest remote origin/master or origin/main . Then produce an exec briefing for the last 24 hours of commits that touch 

Formatting + structure:

- Use rich Markdown (H1 workstream sections, italics for the subtitle, horizontal rules as needed).
- Preamble can read something like “Here’s the last 24h brief for <directory>:”
- Subtitle should read: “Narrative walkthrough with owners; grouped by workstream.”
- Group by workstream rather than listing each commit. Workstream titles should be H1.
- Write a short narrative per workstream that explains the changes in plain language.
- Use bullet points and bolding when it makes things more readable
- Feel free to make bullets per person, but bold their name

Content requirements:

- Include PR links inline (e.g., [#123](...)) without a “PRs:” label.
- Do NOT include commit hashes or a “Key commits” section.
- It’s fine if multiple PRs appear under one workstream, but avoid per‑commit bullet lists.

Scope rules:

- Only include changes within the current cwd (or main checkout equivalent)
- Only include the last 24h of commits.
- Use `gh` to fetch PR titles and descriptions if it helps.
  Also feel free to pull PR reviews and comments

### Geplante Aufgaben mit Skills kombinieren, um eigene Bugs zu beheben

Erstelle einen neuen Skill namens `$recent-code-bugfix`, der versucht, einen durch deine eigenen Commits verursachten Bug zu beheben, und [speichere ihn in deinen persönlichen Skills](/de-DE/codex/build-skills#where-to-save-skills).

```markdown
---
name: recent-code-bugfix
description: Find and fix a bug introduced by the current author within the last week in the current working directory. Use when a user wants a proactive bugfix from their recent changes, when the prompt is empty, or when asked to triage/fix issues caused by their recent commits. Root cause must map directly to the author’s own changes.
---

# Recent Code Bugfix

## Overview

Find a bug introduced by the current author in the last week, implement a fix, and verify it when possible. Operate in the current working directory, assume the code is local, and ensure the root cause is tied directly to the author’s own edits.

## Workflow

### 1) Establish the recent-change scope

Use Git to identify the author and changed files from the last week.

- Determine the author from `git config user.name`/`user.email`. If unavailable, use the current user’s name from the environment or ask once.
- Use `git log --since=1.week --author=<author>` to list recent commits and files. Focus on files touched by those commits.
- If the user’s prompt is empty, proceed directly with this default scope.

### 2) Find a concrete failure tied to recent changes

Prioritize defects that are directly attributable to the author’s edits.

- Look for recent failures (tests, lint, runtime errors) if logs or CI outputs are available locally.
- If no failures are provided, run the smallest relevant verification (single test, file-level lint, or targeted repro) that touches the edited files.
- Confirm the root cause is directly connected to the author’s changes, not unrelated legacy issues. If only unrelated failures are found, stop and report that no qualifying bug was detected.

### 3) Implement the fix

Make a minimal fix that aligns with project conventions.

- Update only the files needed to resolve the issue.
- Avoid adding extra defensive checks or unrelated refactors.
- Keep changes consistent with local style and tests.

### 4) Verify

Attempt verification when possible.

- Prefer the smallest validation step (targeted test, focused lint, or direct repro command).
- If verification cannot be run, state what would be run and why it wasn’t executed.

### 5) Report

Summarize the root cause, the fix, and the verification performed. Make it explicit how the root cause ties to the author’s recent changes.

Erstelle anschließend eine neue geplante Aufgabe:

```markdown
Check my commits from the last 24h and submit a $recent-code-bugfix.

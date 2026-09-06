<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/admin-plugin -->

Dieser Leitfaden erklärt, wie das Admin-Plug-in bei gängigen Administrationsaufgaben hilft. Er zeigt dir, wie du dich auf eine Aufgabe vorbereitest und Prompts für wichtige Anwendungsfälle mit den passenden Genehmigungen und dem nötigen Kontext ausprobierst.

## 1. Verstehen, wofür das Admin-Plug-in gedacht ist

Das Admin-Plug-in soll dir helfen, Einstellungen, Berechtigungen und Kontrollmechanismen direkt in ChatGPT Work zu verwalten. Du beschreibst das Ziel in Alltagssprache. Das Plug-in trägt die passenden Angaben zusammen, liest den aktuellen Zustand aus, erklärt seine Ergebnisse und führt dich durch den nächsten unterstützten Schritt.

### Welche Aufgaben das Admin-Plug-in unterstützen soll

- Eine administrative Anfrage in einen klaren Ablauf übersetzen, ohne dass du eine API-Anfrage schreiben musst.
- Den aktuellen Zustand des Workspaces prüfen, bevor du eine Entscheidung triffst oder eine Änderung genehmigst.
- Anzeigen, welche autorisierten Quellen und Felder die Antwort stützen und was das Plug-in nicht verifizieren konnte.
- Vor einer unterstützten Änderung zur Überprüfung pausieren und anschließend den Datensatz erneut lesen, um das Ergebnis zu bestätigen.

Das Plug-in nutzt im Hintergrund ausgewählte Admin-APIs und genehmigte, angebundene Datenquellen. Es führt nicht alle Administrationssysteme zusammen, erweitert deine Berechtigungen nicht und macht nicht jede API-Aktion in ChatGPT verfügbar. Das für die Daten zuständige System bestimmt weiterhin, was das Plug-in lesen oder ändern darf.

### Welche Aufgaben Admin-APIs unterstützen sollen

Eine Admin-API bietet Software eine strukturierte Möglichkeit, Daten oder eine unterstützte Aktion anzufordern. Organisationen können mit den Admin-APIs interne Prozesse oder externe Tools entwickeln. Typische Beispiele sind geplante Berichte, wiederkehrende Aufgaben für viele Datensätze und Verbindungen zu genehmigten Systemen. Diese Arbeitsabläufe erfordern in der Regel eine Prüfung durch die Bereiche Engineering, Sicherheit und Governance.

Du musst keinen API-Ablauf entwickeln, um diesen Leitfaden zu nutzen. Im weiteren Verlauf steht das Admin-Plug-in im Mittelpunkt. Die Administration von ChatGPT-Workspaces und die Administration der API-Plattform bleiben ebenfalls getrennt, jeweils mit eigenen Berechtigungen und Anforderungen an die Authentifizierung.

### Zugangsdaten vertraulich behandeln

Verwende nur Verbindungen und Systeme zur Speicherung von Secrets, die deine Organisation genehmigt hat. Füge niemals einen echten Admin-API-Schlüssel in ChatGPT, Codex, ein Dokument oder eine Quelldatei ein.

## 2. Vorbereitung auf die Nutzung des Admin-Plug-ins

Verwende das Admin-Plug-in für eine unterstützte, einmalige Aufgabe, wenn du die Anfrage in Alltagssprache bearbeiten möchtest. Beschreibe das Ziel und gib die stabilen IDs oder den genehmigten Kontext für die Berichterstattung an. Das Plug-in zeigt dir seine Ergebnisse oder die geplanten Änderungen, bevor du entscheidest, ob du fortfahren möchtest.

Das Plug-in verwendet nur die Quellen, Zugangsdaten und Aktionen, die für diese Aufgabe autorisiert sind. Es führt nicht alle Administrationssysteme zusammen und gibt dir keine weitergehenden Berechtigungen. Das ursprüngliche System bleibt die maßgebliche Datenquelle.

### Bevor du beginnst

1. Finde den Administrationsbereich, in dem die Datensätze gespeichert sind.
2. Trage die erforderlichen Angaben zusammen und hole die nötige Genehmigung ein.
3. Beginne mit einer Anfrage ohne Schreibzugriff.
4. Frage das Plug-in, welche Quellen und Felder es verwendet hat und was es nicht verifizieren konnte.
5. Prüfe bei einer unterstützten Änderung den Plan, bevor du ihn genehmigst. Bitte das Plug-in anschließend, den Datensatz erneut zu lesen und das Ergebnis zu bestätigen.

Stelle sicher, dass das Plug-in in deinem Workspace verfügbar ist und du die erforderlichen Berechtigungen hast. Die folgenden Anwendungsfälle zu Rollen und Zugriff entsprechen dem derzeit dokumentierten Funktionsumfang des Plug-ins. Das Plug-in kann Rollen, Funktionsberechtigungen und Zuweisungen an Personen oder Gruppen prüfen. Nach deiner Bestätigung kann es außerdem einer bestehenden Gruppe eine bestehende Rolle zuweisen.

Das Plug-in kann keine Rollen erstellen, keine Berechtigungen einer Rolle ändern und keinen Zugriff auf einen bestimmten Konnektor bestätigen.

Für die Analyse-Anwendungsfälle ist Zugriff auf angebundene, genehmigte Datenquellen erforderlich. Die ROI-Analyse benötigt außerdem freigegebene Ergebnisse aus dem Geschäftsbetrieb oder Engineering. Nutzungsdaten allein reichen nicht aus.

## 3. Wichtige Anwendungsfälle des Admin-Plug-ins kennenlernen

Wähle einen Anwendungsfall aus, ersetze jeden Platzhalter durch einen Wert aus deiner genehmigten Anfrage und führe die Schritte der Reihe nach aus. Beginne mit einer Anfrage ohne Schreibzugriff, es sei denn, die Aufgabe ist eine unterstützte Änderung, für die bereits eine Genehmigung vorliegt.

### Workspace-Rollen auflisten

**Prompt zum Ausprobieren**

```text
List the roles in workspace {workspace_id}. Separate built-in and custom roles. For each role, explain which features it can use and show the users or groups assigned to it. Don’t make changes.

**Schritte**

1. **Zusammentragen:** Bestätige die Workspace-ID und stelle sicher, dass du diese Informationen einsehen darfst.
2. **Ausführen:** Fordere die Rollenliste ohne Schreibzugriff an.
3. **Review:** Prüfe die Rollentypen, den Zugriff auf Funktionen und die Zuweisungen.
4. **Nachprüfen:** Gehe unerwarteten Ergebnissen nach, ohne Änderungen vorzunehmen.

### Eine Rolle prüfen

**Prompt zum Ausprobieren**

```text
Review role {role_id}. Explain its permissions in plain language, show who has it, and flag anything that looks broader than expected. Don’t edit the role.

**Schritte**

1. **Zusammentragen:** Bestätige die Rollen-ID und den Workspace.
2. **Ausführen:** Fordere eine Prüfung der Rolle ohne Schreibzugriff an.
3. **Review:** Prüfe, ob die Berechtigungen und Zuweisungen dem vorgesehenen Zweck der Rolle entsprechen.
4. **Nachprüfen:** Notiere alle Fragen an die für die Rolle verantwortliche Person. Denk daran: Das Plug-in kann die Rolle weder erstellen noch ihre Berechtigungen bearbeiten.

### Den Zugriff einer Person oder Gruppe nachvollziehen

**Prompt zum Ausprobieren**

```text
Help me understand the access for user {user_id} or group {group_id}. Show their assigned roles, explain what access those roles provide, and point out overlaps or gaps. Clearly say what you can’t verify.

**Schritte**

1. **Zusammentragen:** Verwende die stabile ID der Person oder Gruppe.
2. **Ausführen:** Bitte das Plug-in, den Zugriff zu erklären.
3. **Review:** Prüfe, welche Rollen zugewiesen sind und welchen Zugriff sie gewähren. Notiere etwaige Überschneidungen oder Lücken.
4. **Nachprüfen:** Wenn das Plug-in etwas nicht einsehen kann, kennzeichne es als unbekannt, statt zu raten.

### Einer Gruppe eine bestehende Rolle zuweisen

**Prompt zum Ausprobieren**

```text
Before making a change, show the current roles for group {group_id} and explain what role {role_id} would add. Confirm the recorded approver and wait for my explicit approval. After the assignment, verify the group’s updated roles.

**Schritte**

1. **Zusammentragen:** Bestätige die Gruppen- und Rollen-IDs. Prüfe die genehmigte Anfrage und wer als genehmigende Person dokumentiert ist.
2. **Ausführen:** Bitte das Plug-in, die aktuellen Rollen und die vorgesehenen Änderungen anzuzeigen.
3. **Review:** Erteile die Genehmigung nur, wenn der Plan mit der genehmigten Anfrage übereinstimmt.
4. **Nachprüfen:** Prüfe die Gruppe nach der Zuweisung erneut, um zu bestätigen, dass die bestehende Rolle wie genehmigt hinzugefügt wurde.

### Allgemeine Berechtigung für Konnektoren prüfen

**Prompt zum Ausprobieren**

```text
Check whether user {user_id} has general connector access through their assigned roles. Ask the plugin to show which permissions support its answer. If it can’t verify access to a specific connector, have it say so clearly.

**Schritte**

1. **Zusammentragen:** Bestätige die Benutzer-ID und deine Berechtigung, den Zugriff dieser Person zu prüfen.
2. **Ausführen:** Fordere die allgemeine Berechtigungsprüfung an.
3. **Review:** Prüfe die zugewiesene Rolle und die Berechtigung, auf der die Antwort beruht.
4. **Überprüfen:** Nutze dies nur als allgemeine Prüfung. Sie belegt keinen Zugriff auf einen bestimmten Konnektor oder ein verbundenes Element.

### Probleme bei einer genehmigten Änderung beheben

**Prompt zum Ausprobieren**

```text
Review approved change {change_record_id}. Compare the requested result with the current workspace. If it failed, check the workspace and role first. Then confirm who owns the record, explain the issue, and suggest the safest next step.

**Schritte**

1. **Zusammentragen:** Bestätige den Eintrag zur genehmigten Änderung und das angestrebte Ergebnis.
2. **Ausführen:** Bitte das Plug-in, die Anfrage mit dem aktuellen Zustand des Workspace zu vergleichen.
3. **Review:** Prüfe den Workspace und die Rolle. Prüfe anschließend, wer für den Eintrag verantwortlich ist.
4. **Überprüfen:** Nutze den aktuellen Zustand des Workspace als maßgebliche Grundlage, bevor du den nächsten Schritt festlegst.

### Kosten und Modellmix optimieren

**Prompt zum Ausprobieren**

```text
For {date_range} in workspace {workspace_id}, group verified token use and cost by use case. Compare models and reasoning modes using the speed and quality information available. Flag costly workflows when the data shows little evidence of value. Recommend where spending could be reduced or redirected toward work with stronger productivity or cost results. Include any approved revenue or quality signals. Estimate possible savings, explain tradeoffs, and separate verified observations from assumptions or missing inputs. Keep this read-only.

**Schritte**

1. **Zusammentragen:** Bestätige den Workspace und den Zeitraum und stelle sicher, dass die Kostendaten den gesamten Zeitraum abdecken. Prüfe, welche freigegebenen Felder zu Leistung oder Ergebnissen verfügbar sind.
2. **Ausführen:** Fordere den Kosten- und Modellvergleich an.
3. **Review:** Unterscheide zwischen den Erkenntnissen aus den Daten, Annahmen, fehlenden Angaben und Zielkonflikten.
4. **Überprüfen:** Prüfe mögliche Einsparungen gemeinsam mit Finance und den Verantwortlichen für den Ablauf, bevor du handelst.

### Nutzung und Verbreitung ermitteln

**Prompt zum Ausprobieren**

```text
Analyze workspace {workspace_id} during {date_range}. Show tasks and token use by team and business function. Group cost by use case. Summarize what teams use ChatGPT and Codex to accomplish. Include examples from Legal, Marketing, and Sales. Compare available use of skills and plugins. Only report tool calls, connected apps, and multi-tool workflows if those fields are available. Show where teams use more advanced workflows and where there may be room to expand. Rank the top {5_or_10} use cases and show whether a small group of highly active users accounts for most usage. Don’t guess about activity that is not in the data.

**Schritte**

1. **Zusammentragen:** Prüfe den Workspace, den Zeitraum und die Teamzuordnungen. Stelle sicher, dass Berichte auf Ebene einzelner Nutzender genehmigt sind.
2. **Ausführen:** Fordere die Analyse zu Nutzung und Verbreitung an.
3. **Review:** Prüfe, welche der angeforderten Felder verfügbar sind. Lass Aktivitäten, zu denen Daten fehlen, unberücksichtigt, statt Vermutungen anzustellen.
4. **Überprüfen:** Intensive Nutzung belegt weder eine fortgeschrittene Anwendung noch geschäftlichen Nutzen oder die Leistung einzelner Personen.

### Geschäftlichen Nutzen und ROI messen

**Prompt zum Ausprobieren**

```text
For workspace {workspace_id} in {date_range}, combine verified usage and cost with approved outcomes. Estimate value by team and use case. Include approved Sales measures for productivity, revenue, and quality. Compare teams and models, as well as workflows and user segments. Rank returns against cost. Show the sources and formula. Clearly state assumptions, limits, and missing inputs. Don’t claim ChatGPT caused the outcomes. Keep this read-only.

**Schritte**

1. **Zusammentragen:** Prüfe den Workspace und den Zeitraum und bestätige anschließend die freigegebenen Ergebnisse. Prüfe die Formel und die Datenschutzregeln.
2. **Ausführen:** Fordere die ROI-Analyse an.
3. **Review:** Prüfe jede Quelle und jede Annahme. Halte alle Einschränkungen und fehlenden Angaben fest.
4. **Überprüfen:** Die Nutzung allein kann weder den ROI noch einen kausalen Zusammenhang belegen. Prüfe das Ergebnis gemeinsam mit Finance und den Verantwortlichen der Fachbereiche.

### ROI von Codex bewerten

**Prompt zum Ausprobieren**

```text
For workspace {workspace_id}, combine verified Codex usage and cost from {date_range} with approved engineering outcomes. Estimate ROI by team, repository, and workflow. Compare productivity and delivery speed with code quality and engineering cost. Identify workflows that show high value or use many resources. Recommend changes to the model, reasoning mode, or workflow. Explain the tradeoffs and uncertainty. Present the findings as patterns in the available data, not proof that Codex caused the outcome. Return findings only; do not make changes.

**Schritte**

1. **Zusammentragen:** Bestätige den Workspace und den Berichtszeitraum. Prüfe die Team- und Repository-Zuordnungen sowie die freigegebenen Referenzdaten.
2. **Ausführen:** Fordere die ROI-Analyse für Codex an.
3. **Review:** Unterscheide beobachtete Muster von Annahmen. Schütze die Daten der Nutzenden und der Repositorys.
4. **Überprüfen:** Prüfe die Empfehlungen und die Referenzwerte für die Ergebnisse gemeinsam mit Engineering.

## 4. Wann ein API-basierter Ablauf sinnvoll sein kann

Manche Organisationen entwickeln mit den APIs eigene Administrationsprozesse oder externe Tools. Dieser Ansatz kann zeitgesteuerte oder kontinuierlich laufende Aufgaben unterstützen. Er kann auch hilfreich sein, wenn ein Prozess viele Datensätze umfasst oder an ein freigegebenes internes System angebunden werden muss. Dies ist unabhängig von der geführten Nutzung des Admin-Plug-ins.

Beginne mit einer klar definierten Administrationsaufgabe: Bestimme die erforderlichen Angaben und Berechtigungen, die Prüfschritte, das erwartete Ergebnis und wie dieses dokumentiert wird. Wenn deine Organisation die Aufgabe automatisiert, beziehe die zuständigen Teams für Engineering, Sicherheit und Governance ein, speichere Zugangsdaten in einem freigegebenen Secret-Speicher und teste den Ablauf vor der Bereitstellung.

### Weiterführende Ressourcen

- [Referenz der Admin API für ChatGPT-Workspaces](https://chatgpt.com/public/admin/api-reference)
- [Grenzen der Administration](/de-DE/codex/enterprise/roles-and-workspace-permissions#understand-the-control-boundaries)
- [Analytics API für ChatGPT-Workspaces](/de-DE/codex/enterprise/analytics-api)
- [Compliance API für ChatGPT-Workspaces](/de-DE/codex/enterprise/compliance-api)

<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/prisma-airs -->

Verbinde Prisma AIRS von Palo Alto Networks, um deine Sicherheitsrichtlinien auf
Codex-Prompts anzuwenden, bevor die Prompts das Modell erreichen. Personen mit Berechtigungen zur Workspace-Administration konfigurieren die
Integration einmal für ihren Workspace.

Prisma AIRS kann die in deinem Sicherheitsprofil konfigurierten Schutzmaßnahmen anwenden, zum
Beispiel zur Verhinderung von Datenverlusten sowie zur Erkennung von Prompt Injection und schädlichen
URLs.

## Bevor du beginnst

Du benötigst:

- Einen ChatGPT-Workspace mit aktiviertem Zugriff auf Prisma AIRS. Wende dich an dein
OpenAI-Account-Team, um Zugriff anzufordern.
- Berechtigungen zur Workspace-Administration.
- Einen API-Schlüssel für Prisma AIRS, ein konfiguriertes Sicherheitsprofil und den Dienstendpunkt
für deine Bereitstellung.

## Prisma AIRS verbinden

1. Öffne [Codex-Datenkontrollen](https://chatgpt.com/codex/cloud/settings/data) mit
   Berechtigungen zur Workspace-Administration.
2. Unter **Externe Schutzmechanismen** findest du **Prisma AIRS**. Wenn dieser Abschnitt nicht
   verfügbar ist, bitte dein OpenAI-Account-Team, den Zugriff für deinen Workspace zu aktivieren.
3. Gib deinen **API-Schlüssel**, den Namen oder die ID für das **Sicherheitsprofil** und die **Endpunkt-
   URL** ein.
4. Wähle einen **Durchsetzungsmodus** aus und lege unter **Bei AIRS-Ausfall** das Verhalten fest.
5. Wähle **Verbindung speichern** aus. Codex überprüft die Verbindung und verschlüsselt deinen
   API-Schlüssel.
6. Wähle **Verbindung testen** aus, um die gespeicherte Konfiguration zu überprüfen.
7. Schalte die Option **Prisma AIRS aktivieren** ein, damit Prompts im gesamten
   Workspace gescannt werden.

Durch das Speichern der Verbindung wird das Scannen nicht aktiviert. Du musst zusätzlich die Option **Prisma AIRS
aktivieren** einschalten.

## Endpunkt auswählen

Verwende den freigegebenen Endpunkt für deine Bereitstellung von Prisma AIRS:

| Region        | Endpunkt                                                 |
| ------------- | -------------------------------------------------------- |
| Vereinigte Staaten | `https://service.api.aisecurity.paloaltonetworks.com`    |
| Deutschland       | `https://service-de.api.aisecurity.paloaltonetworks.com` |
| Indien         | `https://service-in.api.aisecurity.paloaltonetworks.com` |
| Singapur     | `https://service-sg.api.aisecurity.paloaltonetworks.com` |

Codex verwendet standardmäßig den Endpunkt in den Vereinigten Staaten. Vorgaben zur Datenresidenz
für den Workspace können einschränken, welchen Endpunkt du verwenden kannst.

## Umgang mit Prompts festlegen

Der **Durchsetzungsmodus** legt fest, was geschieht, wenn Prisma AIRS einen Prompt als auffällig kennzeichnet:

- **Blockieren**: Der Prompt wird blockiert, bevor er das Modell erreicht. Das ist die Standardeinstellung.
- **Nur Warnung**: Die Erkennung wird protokolliert und der Prompt wird weiterverarbeitet.

**Bei AIRS-Ausfall** legt fest, was geschieht, wenn Prisma AIRS nicht verfügbar ist oder
nicht antwortet:

- **Prompts zulassen**: Der Prompt wird ohne abgeschlossenen Scan weiterverarbeitet. Das ist die Standardeinstellung.
- **Prompts blockieren**: Der Prompt wird angehalten, bis Prisma AIRS ihn scannen kann.

Wähle **Prompts blockieren** , wenn deine Sicherheitsrichtlinie verlangt, dass für jeden erfassten Prompt
eine Scanentscheidung vorliegt.

## Welche Inhalte gescannt werden

Codex sendet neu übermittelten Prompt-Text zur Prüfung an den konfigurierten Prisma AIRS-Endpunkt.
Dies gilt für die von der Integration erfassten Codex-Arbeitsabläufe, darunter App, CLI,
IDE-Erweiterung und Cloud, wenn sich Nutzende beim konfigurierten
ChatGPT-Workspace authentifizieren. Sitzungen, die über einen Platform-API-Schlüssel authentifiziert werden, sind davon ausgenommen. Unter
[Anmeldemethode oder Workspace erzwingen](/de-DE/codex/auth#enforce-a-login-method-or-workspace)
erfährst du, wie du die vorgesehene Anmeldemethode und den vorgesehenen Workspace durchsetzt.

Über diese Integration scannt Prisma AIRS keine Antworten des Assistenten, Tool-Aufrufe, Tool-Ergebnisse, Dateien
oder Bilder. Dein konfiguriertes Sicherheitsprofil legt fest,
welche Bedrohungen und sensiblen Daten Prisma AIRS erkennt.

Codex verschlüsselt deinen API-Schlüssel und zeigt ihn nach dem Speichern nie wieder an. Prüfe die Richtlinien von Palo
Alto Networks zur Datenverarbeitung, Aufbewahrung und Datenresidenz, bevor du die
Prompt-Prüfung aktivierst. Diese Richtlinien gelten für Prompts, die an Prisma AIRS gesendet werden.

## Verbindung verwalten

Kehre zu [Codex-Datenkontrollen](https://chatgpt.com/codex/cloud/settings/data)
zurück, um die Integration zu verwalten:

- Wähle **Verbindung testen** aus, um deinen gespeicherten API-Schlüssel, dein Sicherheitsprofil
  und deinen Endpunkt zu überprüfen.
- Gib einen neuen API-Schlüssel ein und wähle **API-Schlüssel rotieren** aus, um den gespeicherten Schlüssel
  zu ersetzen, ohne die übrigen Einstellungen zu ändern.
- Schalte **Prisma AIRS aktivieren** aus, um das Scannen zu beenden und die gespeicherte
  Konfiguration beizubehalten.
- Wähle **Verbindung trennen** aus und bestätige anschließend, um das Scannen zu beenden und die gespeicherte
  Verbindung sowie den API-Schlüssel zu löschen.

Für eine umfassendere Einrichtung des Workspaces und die Richtlinienverwaltung findest du weitere Informationen im
[Einführungsleitfaden für Administrierende](/de-DE/codex/enterprise/admin-setup) sowie unter
[Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration).

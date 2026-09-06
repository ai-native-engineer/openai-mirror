<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/access-tokens -->

Codex-Zugriffstoken sind Anmeldedaten für ChatGPT-Workspaces, die auf Codex-Berechtigungen beschränkt sind. Sie authentifizieren vertrauenswürdige, nicht interaktive lokale Arbeitsabläufe, einschließlich Codex CLI und Automatisierungen auf Basis von App Server, mit einer ChatGPT-Workspace-Identität. Verwende sie, wenn ein Skript, ein geplanter Job oder ein CI-Runner wiederholbaren lokalen Zugriff benötigt.

  Codex-Zugriffstoken werden derzeit für Workspaces von ChatGPT Business und ChatGPT Enterprise unterstützt.

Erstelle persönliche Zugriffstoken in der ChatGPT-Administrationskonsole unter [Zugriffstoken](https://chatgpt.com/admin/access-tokens). Jedes Token gehört der Person, die es erstellt hat, und deren ChatGPT-Workspace. Token dienen als Agentenidentitäten für programmgesteuerte lokale Arbeitsabläufe. Informationen zu Token, die über die Detailseite einer eigens eingerichteten nichtmenschlichen Workspace-Identität erstellt werden, findest du unter [Dienstkonten](/de-DE/codex/enterprise/service-accounts).

  Wenn ein API-Schlüssel der Plattform für deine Automatisierung ausreicht, verwende weiterhin die Authentifizierung per API-Schlüssel. Nutze Codex-Zugriffstoken, wenn ein vertrauenswürdiger lokaler Ablauf gezielt Zugriff auf einen ChatGPT-Workspace, im Workspace verwaltete Nutzungsberechtigungen oder Kontrollmechanismen für Unternehmen benötigt.

  Möchtest du einen veröffentlichten ChatGPT-Workspace-Agenten aus deinem eigenen System auslösen? Dieser
  Ablauf erfordert Zugriff auf **Agenten im Workspace** . Ein reines Codex-Token kann
  Aufrufe zum Auslösen von Workspace-Agenten nicht authentifizieren. Wenn dein Token-Dialog
**Berechtigungsbereiche** anbietet, wähle **Agenten im Workspace** zum Auslösen eines Agenten und **Codex** für
  Codex-Automatisierungen. Gewähre mehrere Berechtigungsbereiche nur dann, wenn der Ablauf
  jeden davon erfordert. Siehe [Authentifizierung mit Zugriffstoken
  für Workspace-Agenten](/workspace-agents/authentication).

## Funktionsweise von Zugriffstoken

Verwende ein Zugriffstoken, wenn Codex CLI oder ein Client für App Server ausgeführt werden soll, ohne dass sich jemand im Browser anmelden muss. Das Token steht für das Benutzerkonto im ChatGPT-Workspace, mit dem es erstellt wurde. So können Ausführungen die Zugriffsrechte dieses Kontos nutzen und in den Governance-Daten des Workspaces erscheinen.

Der Client prüft das Token beim Start einer Ausführung und ordnet die Ausführung dieser Workspace-Identität zu. Behandle das Token wie jedes andere Secret für Automatisierungen: Speichere es in einem Secret Manager, protokolliere es nicht und rotiere es gemäß den Richtlinien deiner Organisation.

Verwende Zugriffstoken für:

- Jobs mit `codex exec`, die von vertrauenswürdigen Automatisierungen ausgeführt werden.
- Lokale Skripte, die Codex CLI wiederholt und nicht interaktiv ausführen müssen.
- Vertrauenswürdige Automatisierungen auf Basis von App Server.
- Arbeitsabläufe in Unternehmen, bei denen die Nutzung einem Benutzerkonto im ChatGPT-Workspace statt einem API-Schlüssel einer Organisation zugeordnet wird.

Wichtige Risiken, die du vermeiden solltest:

- **Offengelegte Zugangsdaten:** Jede Person, die über das Token verfügt, kann über Codex CLI oder einen Client für App Server lokale Ausführungen unter der Identität der Person starten, die das Token erstellt hat. Speichere Token in einem Secret Manager, protokolliere sie nicht und rotiere sie gemäß den Richtlinien deiner Organisation.
- **Vertrauenswürdigkeit von Runnern:** Öffentliche CI-Systeme, Pull Requests aus Forks oder gemeinsam genutzte Rechner können Token für Personen außerhalb deines Workspaces zugänglich machen. Verwende Zugriffstoken nur auf vertrauenswürdigen Runnern.
- **Gemeinsam genutzte Identitäten:** Wenn voneinander unabhängige Teams das Token einer Person verwenden, lassen sich Verantwortlichkeiten und Audit-Trails schwerer nachvollziehen. Erstelle Token jeweils für die Person, die für den betreffenden Ablauf verantwortlich ist.
- **Veraltete Anmeldedaten:** Token mit langer Gültigkeitsdauer können auch nach Änderungen am Ablauf aktiv bleiben. Bevorzuge zeitlich begrenzte Token und widerrufe Token, die nicht mehr verwendet werden.
- **Falscher Berechtigungsbereich oder falsche Art von Anmeldedaten:** Codex-Automatisierungen erfordern Zugriff auf Codex,
  das Auslösen von Workspace-Agenten erfordert Zugriff auf Agenten im Workspace und allgemeine Aufrufe der OpenAI API
  erfordern API-Schlüssel der Plattform. Wenn **Berechtigungsbereiche** angezeigt wird, gewähre nur die
  Berechtigungen, die der Ablauf erfordert.

## Erstellung von Zugriffstoken aktivieren

Aktiviere in den Workspace-Einstellungen die Berechtigung für Zugriffstoken, damit berechtigte Mitglieder Zugriffstoken erstellen können.

Die Berechtigung für Zugriffstoken steuert die Token-Erstellung. Sie gewährt keinen Zugriff auf die ChatGPT-Desktop-App, Codex CLI oder die IDE-Erweiterung und ändert weder den Lizenztyp eines Mitglieds noch dessen vordefinierte Workspace-Rolle oder das Berechtigungsprofil der lokalen Laufzeitumgebung. Mit Token authentifizierte Arbeitsabläufe über Codex CLI und App Server erfordern außerdem, dass die jeweilige Person die Berechtigung zur lokalen Codex-Nutzung hat.

Weitere Informationen zum Zusammenspiel dieser Einstellungen findest du unter
[Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions).

  
    
  

1. Bitte eine Person mit Inhaberrolle im Workspace,
[Workspace-Einstellungen \> Berechtigungen und Rollen](https://chatgpt.com/admin/permissions) zu öffnen.
2. Wenn der Abschnitt **Zugriffstoken** angezeigt wird, aktiviere **Nutzenden erlauben, persönliche
   Zugriffstoken zu erstellen**. Wenn dieser Abschnitt nicht verfügbar ist, aktiviere **Mitgliedern erlauben,
   Codex-Zugriffstoken zu verwenden** unter **Codex und Work Lokal** oder
**Codex Lokal**.
3. Aktiviere für die Person, die für den Ablauf verantwortlich ist, die entsprechende Berechtigung zur lokalen Codex-Nutzung:
**Mitgliedern erlauben, Codex und Work lokal zu verwenden** unter **Codex und Work Lokal**
   oder **Mitgliedern erlauben, Codex lokal zu verwenden** unter **Codex Lokal**. Wenn **Work
   Lokal** einen eigenen Abschnitt hat, steuert **Work lokal verwenden** die Nutzung von Work und ist
   für Codex-Token nicht erforderlich.

Erlaube nur Personen oder Serviceverantwortlichen, Zugriffstoken zu erstellen, die den Speicherort des Tokens, die vorgesehene Automatisierung und den Zeitplan für die Token-Rotation kennen.

Wenn du die Berechtigung zur lokalen Codex-Nutzung deaktivierst, werden aktive Codex-Token der betroffenen Mitglieder vorübergehend deaktiviert, aber nicht widerrufen. Wird der lokale Codex-Zugriff wiederhergestellt, werden diese Token reaktiviert. Widerrufe Token, wenn ihr Zugriff dauerhaft enden muss.

## Maximale Gültigkeitsdauer für Zugriffstoken festlegen

Wer die Inhaberrolle im Workspace hat, kann die maximale Gültigkeitsdauer festlegen, die Mitglieder
für neue Zugriffstoken wählen können. Öffne
[Workspace-Einstellungen \> Berechtigungen und Rollen](https://chatgpt.com/admin/permissions).
Wenn der Abschnitt **Zugriffstoken** angezeigt wird, lege dort die **Maximale Gültigkeitsdauer für Zugriffstoken**
fest. Suche andernfalls unter **Codex und Work Lokal** oder
**Codex Lokal** nach dieser Einstellung.

  
    
  

Die Begrenzung gilt für neue Zugriffstoken. Bestehende Token behalten ihre bisherige Gültigkeitsdauer.

## Zugriffstoken erstellen

Benenne das Token auf der Seite „Zugriffstoken“, prüfe gegebenenfalls die verfügbaren produktspezifischen Berechtigungsbereiche und wähle eine passende Gültigkeitsdauer.

1. Rufe [Zugriffstoken](https://chatgpt.com/admin/access-tokens) auf.
2. Wähle **Erstellen** aus.

  
    
  

3. Gib einen aussagekräftigen Namen ein, zum Beispiel `release-ci` oder `nightly-docs-check`.

  
    
  

4. Wenn der Dialog **Berechtigungsbereiche** anzeigt, wähle **Codex** aus. Wähle **Agenten im
   Workspace** nur aus, wenn derselbe Ablauf auch einen Workspace-Agenten auslösen muss.
   Wenn der Dialog keine Auswahl für Berechtigungsbereiche bietet, erstellt er ein reines Codex-Token.
5. Wähle eine begrenzte Gültigkeitsdauer von beispielsweise 7, 30, 60 oder 90 Tagen. Persönliche Zugriffstoken
   mit festgelegten Berechtigungsbereichen müssen ein Ablaufdatum haben. Eine ältere Dialogversion für reine Codex-Token
   kann die Option **Kein Ablaufdatum** anbieten. Vermeide diese Option, es sei denn, deine Organisation
   genehmigt sie und rotiert das Token nach einem festgelegten Zeitplan.
6. Wähle **Erstellen** aus.
7. Kopiere das erstellte Zugriffstoken sofort. Nach dem Schließen des Dialogs kannst du es nicht erneut anzeigen.
8. Speichere das Token in deinem Secret Manager oder im Secret-Speicher deines CI-Systems.

Die kürzeste benutzerdefinierte Gültigkeitsdauer beträgt einen Tag. Mit widerrufenen oder abgelaufenen Token kannst du keine neuen authentifizierten Ausführungen starten.

## Zugriffstoken mit Codex CLI verwenden

Wenn der Dialog zur Token-Erstellung eine erforderliche Version von Codex CLI angibt, aktualisiere die CLI auf diese oder eine neuere Version, bevor du das Token verwendest.

Speichere das Token für temporäre Automatisierungen in `CODEX_ACCESS_TOKEN` und führe Codex CLI wie gewohnt aus:

```bash

codex exec --json "review this repository and summarize the top risks"

Leite das Token für eine dauerhafte lokale Anmeldung per Pipe an `codex login --with-access-token` weiter:

```bash
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "summarize the last release diff"

`codex login --with-access-token` speichert Anmeldedaten für eine Agentenidentität im Authentifizierungsspeicher von Codex CLI. Wenn du keine Anmeldedaten dauerhaft auf dem Rechner speichern möchtest, verwende stattdessen die Umgebungsvariable `CODEX_ACCESS_TOKEN`.

`codex app-server` kann dieselben Anmeldedaten über `CODEX_ACCESS_TOKEN` oder
eine mit `codex login --with-access-token` erstellte Anmeldung verwenden, um damit
seine OpenAI-Anfragen zu authentifizieren. Diese Anmeldedaten sind von der
Transportauthentifizierung zwischen Client und App Server getrennt. Konfiguriere für eine entfernte WebSocket-Verbindung ein
separates Bearer- oder Capability-Token wie unter
[App Server](/de-DE/codex/app-server) beschrieben. Verwende das Codex-Zugriffstoken nicht als
Transport-Token. Siehe
[Umgebungsvariablen für Authentifizierung und Netzwerk](/de-DE/codex/config-file/environment-variables#authentication-and-network).

## Token rotieren oder widerrufen

Rotiere Zugriffstoken genauso wie andere Secrets für Automatisierungen:

1. Erstelle ein Ersatztoken.
2. Aktualisiere das Secret im Runner, Scheduler oder Secret Manager.
3. Führe mit dem neuen Token einen Smoke-Test aus.
4. Widerrufe das alte Token auf der Seite [Zugriffstoken](https://chatgpt.com/admin/access-tokens).

Auf der Seite „Zugriffstoken“ können Personen mit Inhaber- oder Adminrolle im Workspace jedes Token des Workspace widerrufen. Mitglieder mit Zugriffstoken-Berechtigung können nur selbst erstellte Token widerrufen.

## Berechtigungsmodell

Die Zugriffstoken-Berechtigung im Workspace steuert, wer Token erstellen darf. Je nach
Aufbau der Workspace-Einstellungen regelt **Mitgliedern erlauben, Codex und Work lokal zu nutzen** unter
**Codex und Work Lokal** oder **Mitgliedern erlauben, Codex lokal zu nutzen** unter **Codex
Lokal** den lokalen Zugriff auf Codex. Wenn **Work Lokal** einen eigenen Abschnitt hat,
regelt **Work lokal nutzen** den Zugriff auf Work und gewährt keinen Zugriff auf Codex. Für Codex-Arbeitsabläufe mit Token-Authentifizierung
benötigt ein Mitglied sowohl lokalen Zugriff auf Codex als auch
die Zugriffstoken-Berechtigung. Ein Mitglied kann lokalen Zugriff auf Codex haben, ohne
Zugriffstoken erstellen zu dürfen.

| Funktion                                                    | Personen mit Inhaber- oder Adminrolle im Workspace                      | Mitglied mit Zugriffstoken-Berechtigung           | Mitglied ohne Zugriffstoken-Berechtigung |
| ------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------- | -------------------------------------- |
| [Zugriffstoken](https://chatgpt.com/admin/access-tokens) öffnen | Ja                                              | Ja                                           | Nein                                     |
| Zugriffstoken erstellen                                          | Ja, für die eigene Identität im ChatGPT-Workspace    | Ja, für die eigene Identität im ChatGPT-Workspace | Nein                                     |
| Zugriffstoken auflisten                                            | Alle Token im Workspace mit Angabe, wer sie jeweils erstellt hat | Nur selbst erstellte Token                      | Nein                                     |
| Zugriffstoken auf der Seite „Zugriffstoken“ widerrufen              | Jedes Token im Workspace                       | Nur selbst erstellte Token                      | Kein Zugriff auf die Seite                         |
| Zugriffstoken-Berechtigung erteilen oder entziehen                       | Nur Personen mit Inhaberrolle im Workspace                             | Nein                                            | Nein                                     |
| Weitere Einstellungen für lokale Clients oder Codex Cloud verwalten             | Ja, entsprechend den Adminberechtigungen im Workspace        | Nein, außer wenn eine Person mit Inhaberrolle Zugriff gewährt             | Nein                                     |

Zusammengefasst: Personen mit Inhaber- oder Adminrolle im Workspace verwalten den Zugriff auf Workspace-Ebene. Mitglieder benötigen die Zugriffstoken-Berechtigung, um eigene Token zu erstellen und zu verwalten. Diese Berechtigung gewährt ihnen jedoch weder Adminrechte noch Zugriff auf die Token anderer Mitglieder.

## Fehlerbehebung

### Die Seite „Zugriffstoken“ gibt 404 zurück oder meldet „Zugriff verweigert“

Bitte eine Person mit Inhaberrolle im Workspace, zu bestätigen, dass deine Rolle je nach verfügbarer Oberfläche die Berechtigung **Nutzenden erlauben,
persönliche Zugriffstoken zu erstellen** oder **Mitgliedern erlauben,
Codex-Zugriffstoken zu nutzen** umfasst. Vergewissere dich bei einem
Codex-Ablauf mit Token-Authentifizierung außerdem, dass **Mitgliedern erlauben, Codex und Work
lokal zu nutzen** oder **Mitgliedern erlauben, Codex lokal zu nutzen** aktiviert ist.

### `codex login --with-access-token` schlägt fehl

Vergewissere dich, dass du das generierte Zugriffstoken und nicht ein Browser-Sitzungstoken oder einen API-Schlüssel der Plattform kopiert hast. Stelle außerdem sicher, dass das Token aktiv ist, noch nicht abgelaufen ist und einer Person mit der erforderlichen Berechtigung für die lokale Nutzung von Codex gehört.

## Verwandte Dokumentation

- [Authentifizierung](/de-DE/codex/auth)
- [Dienstkonten](/de-DE/codex/enterprise/service-accounts)
- [Nicht interaktiver Modus](/de-DE/codex/non-interactive-mode)
- [Leitfaden für den administrativen Rollout](/de-DE/codex/enterprise/admin-setup)
- [Gruppen und Provisionierung](/de-DE/codex/enterprise/groups-and-provisioning)
- [Verwaltung des Lebenszyklus von Nutzerkonten](/de-DE/codex/enterprise/user-lifecycle)
- [Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions)
- [Governance](/de-DE/codex/enterprise/governance)

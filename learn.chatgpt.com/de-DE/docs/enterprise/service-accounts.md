<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/service-accounts -->

Mit Dienstkonten kannst du Codex-Arbeitsabläufe ohne Benutzeroberfläche in deiner gesamten Organisation ausführen und skalieren, ohne auf das Konto einer mitarbeitenden Person angewiesen zu sein. Jeder Runner für Continuous Integration (CI), jeder geplante Job und jede gemeinsam genutzte Integration erhält eine eigene Identität im ChatGPT-Workspace, mit denselben Gruppen, Rollen, Zugriffskontrollen und derselben Nachvollziehbarkeit wie bei persönlichen Konten.

Nur Personen mit einer Inhaber- oder Admin-Rolle im Workspace können Dienstkonten erstellen. Sie können anderen Personen oder Gruppen erlauben, ein Konto zu verwalten, Plug-ins zu konfigurieren oder Zugriffstoken zu erstellen.

Dienstkonten sind nur bei Tarifen mit nutzungsbasierter Abrechnung verfügbar.

Ein Dienstkonto steht für eine nichtmenschliche Identität im Workspace. Ein [persönliches Zugriffstoken](/de-DE/codex/enterprise/access-tokens) steht für das Workspace-Mitglied, das es erstellt. Projekt-Dienstkonten und API-Schlüssel der API-Plattform haben einen separaten Projektzugriff und eine separate Abrechnung.

## Dienstkonto erstellen und einrichten

Diese interaktive Anleitung zeigt am Beispiel von GitHub, wie du ein Konto erstellst, ein Plug-in konfigurierst, ein Token erstellst und Gruppen sowie Rollen zuweist.

1. Öffne in deinen Workspace-Einstellungen den Bereich [Dienstkonten](https://chatgpt.com/admin/service-accounts).
2. Wähle die Plus-Schaltfläche (**+**) aus und gib einen aussagekräftigen Namen ein, etwa `release-automation`.
3. Wähle **Erstellen** aus.

## Ein Plug-in verbinden

Konfiguriere die Plug-ins für das Dienstkonto selbst. Es übernimmt weder die Plug-ins noch die verbundenen Apps der Person, die es erstellt hat.

1. Öffne im Konto den Bereich **Plug-ins** und wähle **Plug-in hinzufügen** aus.
2. Wähle ein Plug-in aus und vergewissere dich, dass es als konfiguriert oder aktiviert angezeigt wird.

Mit den Rollen **Konfigurieren** und **Manager** kannst du Plug-ins einrichten. Mit der Rolle **Nutzende** ist das nicht möglich.

## Ein Zugriffstoken erstellen

Erstelle auf der Detailseite des Dienstkontos ein Token. Das Token repräsentiert das Dienstkonto, nicht die Person, die es erstellt.

1. Öffne das Konto und wähle **Token erstellen** im Bereich **Zugriffstoken** aus.
2. Gib dem Token einen Namen, bestätige den Berechtigungsbereich **Codex** und wähle eine Gültigkeitsdauer.
3. Wähle **Erstellen** aus und speichere das Token in deinem Secret-Manager.

Das vollständige Token wird nur einmal angezeigt. Die Workspace-Richtlinien bestimmen, welche Gültigkeitsdauern verfügbar sind.

## Rollen und Gruppen zuweisen

Ein Dienstkonto kann wie ein menschliches Workspace-Mitglied Workspace-Rollen erhalten und Gruppen beitreten. Weise ihm seine Zugriffsrechte direkt zu. Es übernimmt keine Berechtigungen der Person, die es erstellt hat.

Damit Personen oder Gruppen das Konto verwalten können, wähle **Freigeben** und anschließend **Personen oder Gruppen hinzufügen** aus. Weise dann eine Rolle zu:

| Rolle für das freigegebene Konto | Konto und zugehörige Plug-ins konfigurieren | Zugriffstoken für das Dienstkonto erstellen |
| ------------------- | ------------------------------------- | ------------------------------------ |
| **Nutzende**            | Nein                                    | Ja                                  |
| **Konfigurieren**       | Ja                                   | Nein                                   |
| **Manager**         | Ja                                   | Ja                                  |

Diese Rollen gelten für Personen, die das Konto verwalten. Sie sind von den Workspace-Rollen und Gruppen getrennt, die dem Dienstkonto zugewiesen sind.

Personen mit der Rolle **Konfigurieren** oder **Manager** können das Konto aktivieren oder deaktivieren. Nur Personen mit Eigentümer- oder Administratorrechten für den Workspace können Konten erstellen, löschen oder freigeben. Die zuständigen Personen verwalten freigegebene Konten, während sie mit ihren eigenen ChatGPT-Konten angemeldet sind.

Weitere Informationen zu Berechtigungen im Workspace findest du unter [Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions).

## Codex ohne Anmeldung ausführen

Für Zugriffstoken von Dienstkonten ist Codex CLI ab Version `0.142.0` erforderlich. Setze `CODEX_ACCESS_TOKEN` und führe Codex aus, ohne einen Browser zu öffnen:

```bash

codex exec --json "Inspect this repository and summarize its current state."

Stelle das Token in CI über einen Secret-Manager oder ein Runner-Secret bereit.

Um eine Anmeldung auf einem vertrauenswürdigen Rechner zu speichern, übergib das Token über die Standardeingabe:

```bash
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "Summarize the changes in the current branch."

Dadurch werden die Zugangsdaten lokal gespeichert. Verwende auf gemeinsam genutzten oder temporären Runnern `CODEX_ACCESS_TOKEN`, ohne eine Anmeldung zu speichern.

## Dienstkonten mit SCIM provisionieren

Wenn dein Workspace die Provisionierung von Dienstkonten über das Protokoll System for Cross-domain Identity Management (SCIM) unterstützt, setze bei deinem Identitätsanbieter `userType` auf `ServiceAccount`:

```json
{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "userName": "svc-codex-release@company.example",
  "displayName": "Codex release automation",
  "active": true,
  "userType": "ServiceAccount"
}

Weise die Identität dem Workspace und den erforderlichen Gruppen zu und synchronisiere sie anschließend. Der Identitätsanbieter verwaltet den Namen, die Gruppenzugehörigkeit und den Lebenszyklus des Kontos. Über SCIM verwaltete Konten lassen sich in ChatGPT weder umbenennen noch löschen. Weitere Informationen findest du unter [Gruppen und Provisionierung](/de-DE/codex/enterprise/groups-and-provisioning).

## Dienstkonten mit der Admin API verwalten

Wenn dein Workspace Zugriff hat, verwende einen API-Schlüssel für die ChatGPT Admin API, um Konten, Token und Freigaben zu verwalten. Für Lesevorgänge ist `chatgpt.enterprise.service_account.read` erforderlich, für Änderungen `chatgpt.enterprise.service_account.write`. Mit einem Dienstkonto-Token lassen sich Anfragen an die Admin API nicht authentifizieren.

Die verfügbaren Operationen und aktuellen Anfragepfade findest du in der [Admin API-Referenz](https://chatgpt.com/public/admin/api-reference).

### Konten

| Operation                    | Methode   | Funktion                               |
| ---------------------------- | -------- | ------------------------------------------ |
| Konten auflisten                | `GET`    | Gibt die Dienstkonten im Workspace zurück         |
| Konto erstellen            | `POST`   | Erstellt ein Dienstkonto mit dem angegebenen Namen            |
| Konto abrufen               | `GET`    | Gibt ein einzelnes Dienstkonto zurück                |
| Konto aktivieren oder deaktivieren | `PATCH`  | Aktualisiert den Wert von `enabled` für das Konto      |
| Konto löschen            | `DELETE` | Entfernt das Konto und widerruft seine Token |

Erstelle Konten mit `POST /v1/manage/workspaces/{workspace_id}/service-accounts`. Kontoaktualisierungen ändern nur `enabled`.

### Token

| Operation      | Methode   | Funktion                         |
| -------------- | -------- | ------------------------------------ |
| Token auflisten    | `GET`    | Gibt die Token-Metadaten des Kontos zurück |
| Token erstellen | `POST`   | Erstellt ein Zugriffstoken mit festgelegtem Berechtigungsumfang        |
| Token widerrufen | `DELETE` | Widerruft ein einzelnes Token dauerhaft        |

Erstelle beispielsweise ein Codex-Token, das nach 30 Tagen abläuft:

```json
{
  "name": "production-release-runner",
  "ttl": 2592000,
  "scopes": ["chatgpt.workspace.feature.allow-codex-local-access.access"]
}

`ttl` gibt die Gültigkeitsdauer des Tokens in Sekunden an. Eine begrenzte Gültigkeitsdauer muss weniger als ein Jahr betragen und der Richtlinie deines Workspace für Ablaufdaten entsprechen. `access_token` wird nur beim Erstellen des Tokens vollständig zurückgegeben.

Die Admin API kann außerdem Kontofreigaben auflisten, hinzufügen, aktualisieren und entfernen. Die Rollenwerte sind `manager`, `configurer` und `user`. In ChatGPT wird `configurer` als **Konfigurieren** angezeigt.

## Dienstkonten absichern und verwalten

- Weise nur die Rollen, Gruppen, Plug-ins und Verbindungen zu, die der Ablauf benötigt.
- Speichere Token in einem Secret-Manager und verwende vertrauenswürdige Runner.
- Achte darauf, dass keine Zugangsdaten in Protokollen, Chatnachrichten oder der Versionsverwaltung landen.
- Begrenze die Gültigkeitsdauer und überprüfe regelmäßig den Zugriff auf das Konto sowie dessen Aktivitäten.
- Tausche ein Token aus, indem du ein neues Token erstellst, den Ablauf aktualisierst, den Zugriff überprüfst und das alte Token im Workspace oder über die Admin API widerrufst.
- Widerrufe offengelegte Token sofort und untersuche die jüngsten Aktivitäten des Kontos.
- Deaktiviere oder lösche ungenutzte Konten im Workspace oder über die Admin API. In beiden Fällen werden alle aktiven Token widerrufen. Deaktivierte Konten kannst du wieder aktivieren und mit neuen Token verwenden. Eine Löschung lässt sich nicht rückgängig machen.

Ausführungen werden dem Dienstkonto zugeordnet. Aus den verfügbaren Workspace-Analysen und Audit-Protokollen kann außerdem hervorgehen, wer Token erstellt oder Kontoeinstellungen geändert hat. Prüfe in der [Admin API-Referenz](https://chatgpt.com/public/admin/api-reference), welche Ereignisse erfasst werden.

## Weiterführende Dokumentation

- [Authentifizierung](/de-DE/codex/auth)
- [Persönliche Zugriffstoken](/de-DE/codex/enterprise/access-tokens)
- [Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions)
- [Gruppen und Provisionierung](/de-DE/codex/enterprise/groups-and-provisioning)
- [Governance](/de-DE/codex/enterprise/governance)
- [Compliance API und Audit-Ereignisse](/de-DE/codex/enterprise/compliance-api)
- [Nicht interaktiver Modus](/de-DE/codex/non-interactive-mode)

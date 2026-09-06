<!-- source: https://learn.chatgpt.com/de-DE/docs/agent-approvals-security -->

Codex hilft dir, deinen Code und deine Daten zu schützen, und verringert das Risiko von Missbrauch.

  Auf dieser Seite erfährst du, wie du Codex sicher betreibst. Dazu gehören Sandboxing, Genehmigungen
  und Netzwerkzugriff. Informationen zu Codex Security, dem Produkt zum
  Scannen verbundener GitHub-Repositories, findest du unter [Codex Security](/de-DE/codex/security).

Standardmäßig wird der Agent ohne Netzwerkzugriff ausgeführt. Lokal verwendet Codex eine vom Betriebssystem durchgesetzte Sandbox, die seinen Zugriff in der Regel auf den aktuellen Workspace beschränkt. Außerdem legt eine Genehmigungsrichtlinie fest, wann Codex anhalten und vor einer Aktion deine Genehmigung einholen muss.

Wie Sandboxing in der ChatGPT-Desktop-App,
der Codex CLI und der IDE-Erweiterung grundsätzlich funktioniert, erfährst du unter [Sandboxing](/de-DE/codex/sandboxing).
Einen umfassenderen Überblick über die Sicherheit in Unternehmen findest du im [Codex-Sicherheits-Whitepaper](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click).

## Sandbox und Genehmigungen

Die Sicherheitsmechanismen von Codex bestehen aus zwei Ebenen, die zusammenwirken:

- **Sandbox-Modus**: Legt fest, was Codex technisch tun kann, wenn es vom Modell generierte Befehle ausführt, etwa wo es schreiben und ob es auf das Netzwerk zugreifen kann.
- **Genehmigungsrichtlinie**: Legt fest, wann Codex vor einer Aktion deine Genehmigung einholen muss, etwa wenn es die Sandbox verlässt, das Netzwerk nutzt oder Befehle außerhalb einer als vertrauenswürdig eingestuften Auswahl ausführt.

Codex verwendet je nach Ausführungsort unterschiedliche Sandbox-Modi:

- **Codex Cloud**: Wird in isolierten, von OpenAI verwalteten Containern ausgeführt und kann daher weder auf dein Hostsystem noch auf nicht zugehörige Daten zugreifen. Codex verwendet ein zweiphasiges Laufzeitmodell: Das Setup läuft vor der Agentenphase und kann auf das Netzwerk zugreifen, um die angegebenen Abhängigkeiten zu installieren. Anschließend läuft die Agentenphase standardmäßig offline, sofern du für diese Umgebung keinen Internetzugang aktivierst. Für Cloud-Umgebungen konfigurierte Secrets sind nur während des Setups verfügbar und werden vor Beginn der Agentenphase entfernt.
- **Codex CLI / IDE-Erweiterung**: Mechanismen auf Betriebssystemebene setzen die Sandbox-Richtlinien durch. Standardmäßig ist der Netzwerkzugriff deaktiviert und der Schreibzugriff auf den aktiven Workspace beschränkt. Du kannst die Sandbox, die Genehmigungsrichtlinie und die Netzwerkeinstellungen entsprechend deiner Risikobereitschaft konfigurieren.

In der Voreinstellung `Auto` (zum Beispiel `--sandbox workspace-write --ask-for-approval on-request`) kann Codex automatisch Dateien lesen, Änderungen vornehmen und Befehle im Arbeitsverzeichnis ausführen.

Codex fordert eine Genehmigung an, wenn es Dateien außerhalb des Workspaces bearbeiten oder Befehle ausführen soll, die Netzwerkzugriff erfordern. Wenn du chatten oder planen möchtest, ohne Änderungen vorzunehmen, wechsle mit dem Befehl `/permissions` in den Modus `read-only`.

Codex kann auch für Toolaufrufe von Apps (Konnektoren) eine Genehmigung anfordern, wenn das Tool Nebeneffekte ausweist. Das gilt selbst dann, wenn die Aktion weder ein Shell-Befehl noch eine Dateiänderung ist. Destruktive Toolaufrufe über Apps oder MCP erfordern immer eine Genehmigung, wenn das Tool eine destruktive Annotation ausweist. Eine Ausnahme besteht, wenn es eine Annotation für Lesezugriff ausweist, da diese Vorrang hat.

## Sicherheitsüberwachung und pausierte Aufgaben

GPT-6 Astra umfasst Sicherheitsüberwachung in Codex und ChatGPT Work. Die Überwachung läuft asynchron und kann eine Aufgabe pausieren, wenn sie potenziell unsicheres Modellverhalten erkennt. Die Aufgabe kann erst nach der Aktivität pausiert werden, die dies ausgelöst hat. Die Überwachung ersetzt weder Sandboxing noch Berechtigungen oder die Überprüfung des Ergebnisses.

Wenn eine Aufgabe pausiert wird, lies den Hinweis und prüfe die Ergebnisse der Überwachung, sofern sie verfügbar sind. Setze die Aufgabe erst fort, nachdem du geprüft hast, dass sie sicher weiterlaufen kann. Wenn der Hinweis besagt, dass die Aufgabe beendet wurde, oder keine Option zum Fortsetzen anbietet, kannst du sie über diese Oberfläche nicht fortsetzen.

| Oberfläche und Datenkontrollen                                                                               | Prüfergebnisse und Fortsetzen                                       |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Codex- und ChatGPT Work-Clients mit Funktionen zum Anzeigen der Prüfergebnisse und Fortsetzen der Aufgabe, ohne die hier aufgeführten Datenkontrollen | Prüfe die Ergebnisse, bevor du die Aufgabe fortsetzt.                      |
| Codex CLI und Codex mobile                                                                                    | Vollständige Prüfergebnisse und das Fortsetzen sind nicht verfügbar. Die Aufgabe endet. |
| Keine Datenaufbewahrung, modifizierte Missbrauchsüberwachung oder Datenresidenz für die Speicherung außerhalb der USA                        | Vollständige Prüfergebnisse und das Fortsetzen sind nicht verfügbar. Die Aufgabe endet. |

Die Sicherheitsüberwachung bewertet das Modellverhalten während einer Aufgabe.
Die [automatische Überprüfung von Genehmigungen](/de-DE/codex/sandboxing/auto-review) bewertet einzelne Aktionen, die
bereits eine Genehmigung erfordern, bevor sie ausgeführt werden. Auch eine durch die
automatische Überprüfung genehmigte Aktion kann Teil einer Aufgabe sein, die die Überwachung später pausiert.

## Netzwerkzugriff 

Unter [Internetzugang für Agenten](/de-DE/codex/cloud/internet-access) erfährst du, wie du für Codex Cloud vollständigen Internetzugang oder eine Zulassungsliste für Domains aktivierst.

In der ChatGPT-Desktop-App, der Codex CLI oder der IDE-Erweiterung bleibt der Netzwerkzugriff im standardmäßigen Sandbox-Modus `workspace-write` deaktiviert, sofern du ihn nicht in deiner Konfiguration aktivierst:

```toml
[sandbox_workspace_write]
network_access = true

### Netzwerkisolierung

Der Netzwerkzugriff wird über Zielregeln gesteuert, die für Skripte,
Programme und von Befehlen gestartete Unterprozesse gelten. Wenn der Netzwerkzugriff für Befehle
bereits aktiviert ist, aktiviere die Funktion `network_proxy`, damit dieser Datenverkehr
der von dir konfigurierten Netzwerkrichtlinie unterliegt. Allein durch das Hinzufügen von Domainregeln
wird der Proxy nicht aktiviert.

```toml
[features.network_proxy]
enabled = true
domains = { "api.openai.com" = "allow", "example.com" = "deny" }

Verwende für eine einmalige CLI-Sitzung die boolesche Kurzform, wenn du die Funktion nur ein- oder ausschalten möchtest, und die Tabellenform, wenn du außerdem Richtlinienoptionen festlegen möchtest:

```bash
codex \
  -c 'features.network_proxy=true' \
  -c 'sandbox_workspace_write.network_access=true'

codex \
  -c 'features.network_proxy.enabled=true' \
  -c 'features.network_proxy.domains={ "api.openai.com" = "allow", "example.com" = "deny" }' \
  -c 'sandbox_workspace_write.network_access=true'

Die Funktion verändert, wie aktivierter Netzwerkzugriff durchgesetzt wird. Sie gewährt
selbst keinen Netzwerkzugriff. Lege mit `sandbox_workspace_write.network_access` in der Konfiguration für
`workspace-write` fest, ob Befehle überhaupt Netzwerkzugriff haben:

- Netzwerk aus + `network_proxy` ein: Der Netzwerkzugriff bleibt deaktiviert und die Funktion hat keine Wirkung.
- Netzwerk ein + `network_proxy` aus: Der Netzwerkzugriff bleibt aktiviert und direkte ausgehende
  Verbindungen sind uneingeschränkt möglich.
- Netzwerk ein + `network_proxy` ein: Der Netzwerkzugriff bleibt aktiviert und ausgehender Datenverkehr wird
  durch die konfigurierte Netzwerkrichtlinie begrenzt.

Die Proxy-Funktion gilt auch für [Berechtigungsprofile](/de-DE/codex/permissions#network-permissions).
Die Einstellung `network.enabled = true` eines Profils gewährt Befehlen Netzwerkzugriff,
während `features.network_proxy = true` die Durchsetzung der Domainregeln
dieses Profils aktiviert:

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
extends = ":workspace"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

Wenn du die Proxy-Funktion in diesem Beispiel weglässt, haben Befehle direkten
Netzwerkzugriff und die Zulassungsregel für `api.openai.com` schränkt ihre Ziele nicht ein.

Administrativ verwaltete Anforderungen für `experimental_network` sind unabhängig davon,
ob Nutzende die Funktion ein- oder ausschalten. Sie können den Netzwerkbetrieb in der Sandbox ohne
`features.network_proxy` konfigurieren und starten. Ist der Netzwerkzugriff in der aktiven
Sandbox deaktiviert, schalten sie ihn jedoch nicht ein. Unter [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration#configure-network-access-requirements)
erfährst du, wie `requirements.toml` für die Administration aufgebaut ist.

#### Netzwerkrichtlinie

Domainregeln folgen dem Prinzip der Zulassungsliste:

- Exakte Hostangaben stimmen nur mit dem jeweils angegebenen Host überein.
- `*.example.com` erfasst Subdomains wie `api.example.com`, jedoch nicht
`example.com`.
- `**.example.com` erfasst sowohl die Apex-Domain als auch ihre Subdomains.
- Eine globale Zulassungsregel mit `*` erfasst jeden öffentlichen Host, der nicht gesperrt ist. Betrachte `*`
  als weitreichenden Netzwerkzugriff und bevorzuge nach Möglichkeit eng begrenzte Regeln.
- `deny` hat immer Vorrang vor `allow`; ein globales `*` ist nur für Zulassungsregeln gültig.

#### Lokale und private Ziele

Standardmäßig blockiert `allow_local_binding = false` Loopback-, Link-Local- und
private Ziele:

- Gezielte Ausnahmen: Füge eine Zulassungsregel mit einer exakt angegebenen lokalen IP-Adresse oder `localhost` hinzu,
  wenn ein Befehl ein einzelnes lokales Ziel benötigt.
- Erweiterter Zugriff: Setze `allow_local_binding = true` nur, wenn du bewusst
  einen umfassenderen Zugriff auf lokale oder private Ziele zulassen möchtest.
- Platzhalter: Regeln mit Platzhaltern gelten nicht als explizite lokale Ausnahmen.
- Aufgelöste Adressen: Hostnamen, die in lokale oder private IP-Adressen aufgelöst werden, bleiben blockiert, selbst wenn sie mit der Zulassungsliste übereinstimmen.

#### Schutz vor DNS-Rebinding

Bevor Codex einen Hostnamen zulässt, prüft es nach Möglichkeit die DNS-Auflösung und die IP-Klassifizierung:

- Abfragen, die fehlschlagen oder das Zeitlimit überschreiten, werden blockiert.
- Hostnamen, die in nicht öffentliche Adressen aufgelöst werden, werden blockiert.
- Die Prüfung verringert das Risiko von DNS-Rebinding, beseitigt es jedoch nicht. Um Rebinding vollständig zu verhindern, müssten die aufgelösten IP-Adressen bis in die Transportschicht hinein fest gebunden werden.

Wenn manipuliertes DNS zu deinem Bedrohungsmodell gehört, setze zusätzlich Kontrollen für ausgehenden Datenverkehr auf einer niedrigeren Ebene durch.

#### Gefährliche Einstellungen

Zwei Einstellungen erweitern bewusst die Vertrauensgrenze:

- `dangerously_allow_non_loopback_proxy = true` kann Proxy-Listener
  auch außerhalb der Loopback-Schnittstelle zugänglich machen.
- `dangerously_allow_all_unix_sockets = true` umgeht die Zulassungsliste für Unix-Sockets.

Verwende sie nur in streng kontrollierten Umgebungen. Wenn Proxying für Unix-Sockets aktiviert ist, bleiben Listener auf Loopback beschränkt, selbst wenn eine Bindung an eine andere Adresse angefordert wurde. So wird der Netzwerkzugriff in der Sandbox nicht zu einer Brücke für Fernzugriffe auf lokale Daemons.

`network_proxy` ist standardmäßig deaktiviert. Wenn du es aktivierst, gilt Folgendes:

| Einstellung                                | Standardwert | Verhalten                                                                                                                                                                              |
| -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                              | `false` | Startet den Netzwerkzugriff in der Sandbox nur, wenn der Netzwerkzugriff für Befehle bereits aktiviert ist.                                                                                                           |
| `domains`                              | nicht gesetzt   | Verwendet eine Zulassungsliste. Externe Ziele sind daher erst erlaubt, wenn du `allow`-Regeln hinzufügst. Unterstützt exakte Hosts, auf bestimmte Bereiche begrenzte Platzhalter und globale Zulassungsregeln mit `*`. `deny` hat immer Vorrang. |
| `unix_sockets`                         | nicht gesetzt   | Ziele für Unix-Sockets sind erst erlaubt, wenn du explizite `allow`-Regeln hinzufügst.                                                                                                         |
| `allow_local_binding`                  | `false` | Blockiert lokale Ziele und Ziele in privaten Netzwerken, sofern du nicht eine Zulassungsregel für eine exakte lokale IP-Adresse oder `localhost` hinzufügst oder ausdrücklich einen umfassenderen Zugriff auf lokale und private Ziele aktivierst.                |
| `enable_socks5`                        | `true`  | Stellt SOCKS5-Unterstützung bereit, wenn die Richtlinie dies erlaubt.                                                                                                                                         |
| `enable_socks5_udp`                    | `true`  | Erlaubt UDP über SOCKS5, wenn SOCKS5 verfügbar ist.                                                                                                                                      |
| `allow_upstream_proxy`                 | `true`  | Ermöglicht es dem Netzwerkzugriff in der Sandbox, einen in der Umgebung festgelegten Upstream-Proxy zu berücksichtigen.                                                                                                               |
| `dangerously_allow_non_loopback_proxy` | `false` | Beschränkt Listener-Endpunkte auf Loopback, sofern du sie nicht bewusst über localhost hinaus zugänglich machst.                                                                                            |
| `dangerously_allow_all_unix_sockets`   | `false` | Beschränkt den Zugriff auf Unix-Sockets weiterhin auf eine Zulassungsliste, sofern du diesen Schutz nicht bewusst umgehst.                                                                                              |

### Datenverkehr außerhalb des Netzwerk-Proxys für Befehle

Der Netzwerk-Proxy filtert Skripte, Programme und untergeordnete Prozesse, die in der lokalen Befehls-Sandbox ausgeführt werden. Er filtert weder die Websuche noch Toolaufrufe von Apps oder Konnektoren, Verbindungen zu MCP-Servern, Aktivitäten im Browser oder bei der Computernutzung, Aufgaben in Codex Cloud oder Modell- und Authentifizierungsanfragen des Clients. Diese Bereiche verwenden separate Dienstverbindungen, Funktionseinstellungen, Workspace-Richtlinien oder Steuerungsmechanismen der jeweiligen Umgebung.

Browser-Tools prüfen verwaltete Netzwerksperren und exklusive Zulassungslisten separat,
bevor sie auf einen Origin zugreifen. Richtlinien für Browser-Origins können den Zugriff auf Websites,
Uploads, Downloads und Entwicklungstools zusätzlich einschränken. Siehe
[verwaltete Browser-Steuerung](/de-DE/codex/enterprise/managed-configuration#control-browser-and-computer-use).

Kombiniere für verwaltete Benutzerkonten die Netzwerkrichtlinie für Befehle mit Einstellungen wie
`allowed_web_search_modes`, genehmigten `mcp_servers` und Funktionsvorgaben
für Apps, Plug-ins, Browser oder die Computernutzung. Siehe
[Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration).

Du kannst auch das [Tool für die Websuche](https://platform.openai.com/docs/guides/tools-web-search) steuern, ohne gestarteten Befehlen vollständigen Netzwerkzugriff zu gewähren. Standardmäßig greift Codex über einen Cache für die Websuche auf Ergebnisse zu. Dieser Cache ist ein von OpenAI gepflegter Index mit Webergebnissen. Daher gibt der Cache-Modus bereits indexierte Ergebnisse zurück, statt Webseiten live abzurufen. Das verringert das Risiko von Prompt Injection durch beliebige Live-Inhalte. Behandle Webergebnisse dennoch als nicht vertrauenswürdig. Wenn du `--yolo` oder eine andere [Sandbox-Einstellung für Vollzugriff](#common-sandbox-and-approval-combinations) verwendest, liefert die Websuche standardmäßig Live-Ergebnisse. Verwende `--search` oder setze `web_search = "live"`, um Live-Browsing zuzulassen. Setze den Wert auf `"disabled"`, um das Tool zu deaktivieren:

```toml
web_search = "cached"  # default
# web_search = "disabled"
# web_search = "live"  # same as --search

Setze `web_search = "indexed"`, wenn der Suchindex den externen Webzugriff
begrenzen soll. Aktiviere Netzwerkzugriff oder Websuche in Codex nur mit Bedacht.
Prompt Injection kann dazu führen, dass der Agent nicht vertrauenswürdige Anweisungen abruft und befolgt.

## Standardeinstellungen und Empfehlungen

- Beim Start erkennt Codex, ob der Ordner versionsverwaltet ist, und empfiehlt:
  - Versionsverwaltete Ordner: `Auto` (Workspace-Schreibzugriff + Genehmigungen auf Anfrage)
  - Nicht versionsverwaltete Ordner: `read-only`
- Je nach Setup startet Codex möglicherweise auch im Modus `read-only`, bis du das Arbeitsverzeichnis ausdrücklich als vertrauenswürdig einstufst, etwa über eine Abfrage beim Onboarding oder `/permissions`.
- Der Workspace umfasst das aktuelle Verzeichnis sowie temporäre Verzeichnisse wie `/tmp`. Mit dem Befehl `/status` kannst du prüfen, welche Verzeichnisse zum Workspace gehören.
- Um die Standardeinstellungen zu übernehmen, führe `codex` aus.
- Du kannst diese Einstellungen auch explizit festlegen:
  - `codex --sandbox workspace-write --ask-for-approval on-request`
  - `codex --sandbox read-only --ask-for-approval on-request`

### Geschützte Pfade in beschreibbaren Stammverzeichnissen

Auch bei der standardmäßigen Sandbox-Richtlinie `workspace-write` enthalten beschreibbare Stammverzeichnisse geschützte Pfade:

- `<writable_root>/.git` ist vor Schreibzugriffen geschützt, unabhängig davon, ob es sich um ein Verzeichnis oder eine Datei handelt.
- Wenn `<writable_root>/.git` eine Verweisdatei (`gitdir: ...`) ist, ist auch der aufgelöste Pfad zum Git-Verzeichnis vor Schreibzugriffen geschützt.
- `<writable_root>/.agents` ist vor Schreibzugriffen geschützt, sofern es als Verzeichnis vorhanden ist.
- `<writable_root>/.codex` ist vor Schreibzugriffen geschützt, sofern es als Verzeichnis vorhanden ist.
- Der Schutz gilt rekursiv, sodass für alle Inhalte unter diesen Pfaden kein Schreibzugriff besteht.

### Ohne Genehmigungsabfragen ausführen

Du kannst Genehmigungsabfragen mit `--ask-for-approval never` oder `-a never` (Kurzform) deaktivieren.

Diese Option funktioniert mit allen Modi von `--sandbox`, sodass du weiterhin bestimmst, wie autonom Codex arbeitet. Codex arbeitet innerhalb der von dir festgelegten Grenzen so gut wie möglich.

Wenn Codex ohne Genehmigungsabfragen Dateien lesen, Änderungen vornehmen und Befehle mit Netzwerkzugriff ausführen soll, verwende `--sandbox danger-full-access` (oder das Flag `--dangerously-bypass-approvals-and-sandbox`). Gehe dabei mit Bedacht vor.

Als Mittelweg kannst du mit `approval_policy = { granular = { ... } }` für bestimmte Kategorien von Genehmigungsabfragen weiterhin interaktive Entscheidungen vorsehen und andere automatisch ablehnen lassen. Die granulare Richtlinie umfasst Sandbox-Genehmigungen, Abfragen zu execpolicy-Regeln, MCP-Abfragen, Abfragen zu `request_permissions` und Genehmigungen für Skill-Skripte.

### Automatische Überprüfung von Genehmigungsanfragen

Standardmäßig werden Genehmigungsanfragen an dich weitergeleitet:

```toml
approvals_reviewer = "user"

Automatische Überprüfungen von Genehmigungsanfragen greifen bei interaktiven Genehmigungen, etwa bei
`approval_policy = "on-request"` oder einer granularen Genehmigungsrichtlinie. Setze
`approvals_reviewer = "auto_review"`, damit dafür infrage kommende Genehmigungsanfragen
von einem Prüfagenten bewertet werden, bevor Codex die angeforderte Aktion ausführt:

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"

Informationen zum gesamten Lebenszyklus des Prüfagenten, zu Auslösebedingungen, zur Rangfolge der Konfigurationseinstellungen
und zum Verhalten bei Fehlern findest du unter
[Automatische Überprüfung](/de-DE/codex/sandboxing/auto-review).

Der Prüfagent bewertet nur Aktionen, die bereits genehmigungspflichtig sind, etwa
Sandbox-Eskalationen, blockierte Netzwerkanfragen, Abfragen zu `request_permissions` oder
Toolaufrufe von Apps und MCP mit Nebeneffekten. Aktionen innerhalb der Sandbox
werden ohne zusätzlichen Prüfschritt fortgesetzt.

Die Richtlinie des Prüfagenten prüft auf Datenexfiltration, das Ausspähen von Zugangsdaten, dauerhafte Schwächungen der Sicherheit und destruktive Aktionen. Aktionen mit niedrigem oder mittlerem Risiko können ausgeführt werden, wenn die Richtlinie sie zulässt. Aktionen mit kritischem Risiko werden abgelehnt. Aktionen mit hohem Risiko erfordern eine ausreichende Autorisierung durch dich und dürfen unter keine Ablehnungsregel fallen. Bei Fehlern beim Erstellen des Prompts, während der Prüfsitzung oder beim Parsen wird die Aktion aus Sicherheitsgründen blockiert. Zeitüberschreitungen werden gesondert angezeigt, aber auch dann wird die Aktion nicht ausgeführt.

Die [Standardrichtlinie für den Prüfagenten](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)
befindet sich im Open-Source-Repository von Codex. Unternehmen können den
mandantenspezifischen Abschnitt mithilfe von `guardian_policy_config` in den verwalteten Anforderungen ersetzen.
Lokaler Richtlinientext in `[auto_review].policy` wird ebenfalls unterstützt, aber verwaltete Anforderungen haben
Vorrang. Weitere Informationen zum Setup findest du unter
[Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration#configure-automatic-review-policy).

In der ChatGPT-Desktop-App erscheinen diese Überprüfungen als Einträge der automatischen Überprüfung mit einem Status wie „Wird geprüft“, „Genehmigt“, „Abgelehnt“, „Abgebrochen“ oder „Zeitüberschreitung“. Sie können außerdem eine Risikostufe und eine Bewertung deiner Autorisierung für die geprüfte Anfrage enthalten.

Die automatische Überprüfung erfordert zusätzliche Modellaufrufe und kann dadurch die Codex-Nutzung erhöhen. Administrierende
können sie mit `allowed_approvals_reviewers` einschränken.

### Gängige Kombinationen aus Sandbox und Genehmigungen

| Zweck                                                            | Flags / Konfiguration                                                                                                                      | Auswirkung                                                                                                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Auto (Voreinstellung)                                                     | _keine Flags erforderlich_ oder `--sandbox workspace-write --ask-for-approval on-request`                                                      | Codex kann im Workspace Dateien lesen, Änderungen vornehmen und Befehle ausführen. Für Änderungen außerhalb des Workspaces oder für Netzwerkzugriff benötigt Codex eine Genehmigung. |
| Sicheres Durchsuchen ohne Schreibzugriff                                           | `--sandbox read-only --ask-for-approval on-request`                                                                                 | Codex kann Dateien lesen und Fragen beantworten. Für Änderungen, die Ausführung von Befehlen oder Netzwerkzugriff benötigt Codex eine Genehmigung.                               |
| Nicht interaktiv und ohne Schreibzugriff (CI)                                    | `--sandbox read-only --ask-for-approval never`                                                                                      | Codex kann nur Dateien lesen und fordert niemals eine Genehmigung an.                                                                                              |
| Automatisch bearbeiten, aber vor der Ausführung nicht vertrauenswürdiger Befehle eine Genehmigung anfordern | `--sandbox workspace-write --ask-for-approval untrusted`                                                                            | Codex kann Dateien lesen und bearbeiten, fordert aber vor der Ausführung nicht vertrauenswürdiger Befehle eine Genehmigung an.                                                           |
| Auto-Prüfmodus                                                  | `--sandbox workspace-write --ask-for-approval on-request -c approvals_reviewer=auto_review` oder `approvals_reviewer = "auto_review"` | Dieselbe Sandbox-Grenze wie im standardmäßigen Modus mit Genehmigungen auf Anfrage. Geeignete Genehmigungsanfragen werden jedoch von der Automatischen Überprüfung geprüft, statt dir angezeigt zu werden.  |
| Gefährlicher Vollzugriff                                             | `--dangerously-bypass-approvals-and-sandbox` (Alias: `--yolo`)                                                                      |  Keine Sandbox; keine Genehmigungen _(nicht empfohlen)_                                                                               |

Verwende für nicht interaktive Ausführungen `codex exec --sandbox workspace-write`. Ältere Aufrufe mit `codex exec --full-auto` unterstützt Codex aus Kompatibilitätsgründen weiterhin, stuft sie aber als veraltet ein und gibt eine Warnung aus.

Mit `--ask-for-approval untrusted` führt Codex nur Leseoperationen automatisch aus, die als sicher bekannt sind. Befehle, die den Zustand verändern oder externe Ausführungspfade auslösen können, erfordern eine Genehmigung. Dazu gehören beispielsweise destruktive Git-Operationen oder Git-Flags für die Ausgabe oder zum Überschreiben der Konfiguration.

#### Konfiguration in `config.toml`

Weitere Informationen zum Konfigurationsablauf findest du unter [Grundlagen der Konfiguration](/de-DE/codex/config-file/config-basic), [Erweiterte Konfiguration](/de-DE/codex/config-file/config-advanced#approval-policies-and-sandbox-modes) und in der [Konfigurationsreferenz](/de-DE/codex/config-file/config-reference).

```toml
# Always ask for approval mode
approval_policy = "untrusted"
sandbox_mode    = "read-only"
allow_login_shell = false # optional hardening: disallow login shells for shell-based tools

# Optional: Allow network in workspace-write mode
[sandbox_workspace_write]
network_access = true

# Optional: granular approval policy
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

Du kannst Voreinstellungen auch als [Profildateien](/de-DE/codex/config-file/config-advanced#profiles) speichern und anschließend mit `codex --profile profile-name` auswählen:

```toml
# ~/.codex/full_auto.config.toml
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

```toml
# ~/.codex/readonly_quiet.config.toml
approval_policy = "never"
sandbox_mode    = "read-only"

### Sandbox lokal testen

Mit diesen Befehlen der Codex CLI kannst du prüfen, was passiert, wenn ein Befehl in der Codex-Sandbox ausgeführt wird:

```bash
# macOS
codex sandbox macos [--permissions-profile <name>] [--log-denials] [COMMAND]...
# Linux
codex sandbox linux [--permissions-profile <name>] [COMMAND]...
# Windows
codex sandbox windows [--permissions-profile <name>] [COMMAND]...

Der Befehl `sandbox` ist auch als `codex debug` verfügbar. Für die plattformspezifischen Hilfsprogramme gibt es außerdem Aliase, zum Beispiel `codex sandbox seatbelt` und `codex sandbox landlock`.

## Sandbox auf Betriebssystemebene

Je nach Betriebssystem setzt Codex die Sandbox unterschiedlich durch:

- **macOS** verwendet Seatbelt-Richtlinien und führt Befehle über `sandbox-exec` mit einem Profil (`-p`) aus, das dem gewählten `--sandbox`-Modus entspricht. Wenn bei eingeschränktem Lesezugriff die Plattformstandards aktiviert sind, ergänzt Codex eine speziell zusammengestellte macOS-Plattformrichtlinie, statt `/System` pauschal freizugeben. So bleiben gängige Tools kompatibel.
- **Linux** verwendet standardmäßig `bwrap` und `seccomp`.
- **Windows** verwendet bei der Ausführung im [Windows Subsystem for Linux 2 (WSL2)](/de-DE/codex/windows/wsl) die Linux-Implementierung der Sandbox. WSL1 wurde bis einschließlich Codex `0.114` unterstützt. Seit `0.115` basiert die Linux-Sandbox auf `bwrap`, sodass WSL1 nicht mehr unterstützt wird. Bei nativer Ausführung unter Windows verwendet Codex eine Implementierung der [Windows-Sandbox](/de-DE/codex/windows/windows-sandbox#windows-sandbox).

Wenn du die Codex IDE-Erweiterung unter Windows verwendest, unterstützt sie WSL2 direkt. Lege in deinen VS Code-Einstellungen Folgendes fest, damit der Agent immer in WSL2 ausgeführt wird, wenn es verfügbar ist:

```json
{
  "chatgpt.runCodexInWindowsSubsystemForLinux": true
}

Dadurch übernimmt die IDE-Erweiterung die Sandbox-Semantik von Linux für Befehle, Genehmigungen und den Dateisystemzugriff, selbst wenn Windows das Host-Betriebssystem ist. Weitere Informationen findest du im [WSL-Leitfaden](/de-DE/codex/windows/wsl).

Konfiguriere bei nativer Ausführung unter Windows den nativen Sandbox-Modus in `config.toml`:

```toml
[windows]
sandbox = "unelevated" # or "elevated"
# sandbox_private_desktop = true  # default; set false only for compatibility

Weitere Informationen findest du im [Windows-Setup-Leitfaden](/de-DE/codex/windows/windows-sandbox#windows-sandbox).

Wenn du Linux in einer containerisierten Umgebung wie Docker ausführst, funktioniert die Sandbox möglicherweise nicht, falls die Host- oder Containerkonfiguration die von Codex benötigten Operationen für Namespaces, setuid `bwrap` oder `seccomp` blockiert.

Konfiguriere deinen Docker-Container in diesem Fall so, dass er die erforderliche Isolation bietet. Führe anschließend `codex` im Container mit `--sandbox danger-full-access` oder dem Flag `--dangerously-bypass-approvals-and-sandbox` aus.

### Codex in Dev Containers ausführen

Wenn dein Host die Linux-Sandbox nicht direkt ausführen kann oder deine Organisation für die Entwicklung bereits standardmäßig Container nutzt, führe Codex mit Dev Containers aus und nutze Docker als äußere Isolationsgrenze. Das funktioniert mit Visual Studio Code Dev Containers und kompatiblen Tools.

Verwende das [Beispiel für einen sicheren Codex-Devcontainer](https://github.com/openai/codex/tree/main/.devcontainer) als Referenzimplementierung. Das Beispiel installiert Codex, gängige Entwicklungstools, `bubblewrap` und firewallbasierte Kontrollen für ausgehenden Datenverkehr.

  Devcontainer bieten umfassenden Schutz, verhindern aber nicht jeden
  Angriff. Wenn du Codex im Container mit `--sandbox danger-full-access` oder
`--dangerously-bypass-approvals-and-sandbox` ausführst, kann ein schädliches Projekt
  alle im Devcontainer verfügbaren Daten nach außen übertragen, einschließlich
  der Codex-Anmeldedaten. Verwende diesen Ansatz nur mit vertrauenswürdigen Repositorys und
  überwache die Aktivitäten von Codex wie in jeder anderen Umgebung mit erhöhten Berechtigungen.

Die Referenzimplementierung umfasst:

- ein Basis-Image von Ubuntu 24.04, auf dem Codex und gängige Entwicklungstools installiert sind;
- ein Firewallprofil mit Zulassungsliste für ausgehenden Zugriff;
- VS Code-Einstellungen und Empfehlungen für Erweiterungen, um den Workspace erneut in einem Container zu öffnen;
- persistente Mounts für den Befehlsverlauf und die Codex-Konfiguration;
- `bubblewrap`, damit Codex seine Linux-Sandbox weiterhin verwenden kann, wenn der Container die erforderlichen Berechtigungen gewährt.

So probierst du es aus:

1. Installiere Visual Studio Code und die [Dev Containers-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
2. Kopiere das `.devcontainer`-Setup aus dem Codex-Beispiel in dein Repository oder starte direkt mit dem Codex-Repository.
3. Führe in VS Code **Dev Containers: Open Folder in Container...** aus und wähle `.devcontainer/devcontainer.secure.json`.
4. Öffne nach dem Start des Containers ein Terminal und führe `codex` aus.

Du kannst den Container auch über die CLI starten:

```bash
devcontainer up --workspace-folder . --config .devcontainer/devcontainer.secure.json

Das Beispiel besteht aus drei Hauptbestandteilen:

- `.devcontainer/devcontainer.secure.json` steuert die Containereinstellungen, Berechtigungen, Mounts, Umgebungsvariablen und VS Code-Erweiterungen.
- `.devcontainer/Dockerfile.secure` definiert das Ubuntu-basierte Image und die installierten Tools.
- `.devcontainer/init-firewall.sh` wendet die Netzwerkrichtlinie für ausgehenden Datenverkehr an.

Die Referenz-Firewall ist bewusst nur als Ausgangspunkt gedacht. Wenn du zur Isolation auf Domain-Zulassungslisten angewiesen bist, implementiere für deine Umgebung geeignete Schutzmaßnahmen gegen DNS-Rebinding und für die DNS-Aktualisierung, etwa Aktualisierungen unter Berücksichtigung der TTL oder eine DNS-fähige Firewall.

Wähle im Container einen dieser Modi:

- Lass die Linux-Sandbox von Codex aktiviert, wenn das Dev-Container-Profil die Berechtigungen gewährt, die `bwrap` zum Erstellen der inneren Sandbox benötigt.
- Wenn der Container deine vorgesehene Sicherheitsgrenze bildet, führe Codex im Container mit `--sandbox danger-full-access` aus, damit Codex nicht versucht, eine zweite Sandbox-Ebene zu erstellen.

## Versionskontrolle

Codex funktioniert am besten, wenn du Versionskontrolle in deinen Arbeitsablauf integrierst:

- Arbeite in einem Feature-Branch und achte vor dem Delegieren darauf, dass `git status` keine ausstehenden Änderungen anzeigt. So lassen sich Codex-Patches leichter isolieren und rückgängig machen.
- Bevorzuge patchbasierte Arbeitsabläufe (zum Beispiel `git diff`/`git apply`), statt versionierte Dateien direkt zu bearbeiten. Erstelle häufig Commits, damit du Änderungen in kleinen Schritten rückgängig machen kannst.
- Behandle Vorschläge von Codex wie jeden anderen PR: Führe gezielte Prüfungen durch, überprüfe Diffs und dokumentiere Entscheidungen für Audits in Commit-Nachrichten.

## Monitoring und Telemetrie

Codex unterstützt optionales Monitoring über OpenTelemetry (OTel). So können Teams die Nutzung prüfen, Probleme untersuchen und Compliance-Anforderungen erfüllen, ohne die standardmäßigen lokalen Sicherheitseinstellungen zu schwächen. Die Telemetrie ist standardmäßig deaktiviert. Aktiviere sie ausdrücklich in deiner Konfiguration.

### Übersicht

- Codex deaktiviert den OTel-Export standardmäßig, damit lokale Ausführungen in sich geschlossen bleiben.
- Ist die Funktion aktiviert, erzeugt Codex strukturierte Protokollereignisse zu Chats, API-Anfragen, Streamaktivitäten über SSE/WebSocket, Prompts von Nutzenden (standardmäßig unkenntlich gemacht), Entscheidungen über Tool-Genehmigungen und Tool-Ergebnissen.
- Codex versieht exportierte Ereignisse mit `service.name` (Ursprung), der CLI-Version und einer Umgebungskennzeichnung, um den Datenverkehr aus Entwicklung, Staging und Produktion zu trennen.

### OTel aktivieren (Opt-in)

Füge einen `[otel]`-Block zu deiner Codex-Konfiguration hinzu, die sich üblicherweise unter `~/.codex/config.toml` befindet. Wähle einen Exporter und lege fest, ob Prompt-Text protokolliert werden soll.

```toml
[otel]
environment = "staging"   # dev | staging | prod
exporter = "none"          # none | otlp-http | otlp-grpc
log_user_prompt = false     # redact prompt text unless policy allows

- `exporter = "none"` lässt die Instrumentierung aktiviert, sendet aber keine Daten.
- Um Ereignisse an deinen eigenen Collector zu senden, wähle eine der folgenden Optionen:

```toml
[otel]
exporter = { otlp-http = {
  endpoint = "https://otel.example.com/v1/logs",
  protocol = "binary",
  headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
}}

```toml
[otel]
exporter = { otlp-grpc = {
  endpoint = "https://otel.example.com:4317",
  headers = { "x-otlp-meta" = "abc123" }
}}

Codex bündelt Ereignisse und sendet sie beim Beenden. Codex exportiert ausschließlich Telemetriedaten, die sein OTel-Modul erzeugt.

### Ereigniskategorien

Zu den typischen Ereignistypen gehören:

- `codex.conversation_starts` (Modell, Einstellungen zum Reasoning-Aufwand, Sandbox- und Genehmigungsrichtlinie)
- `codex.api_request` (Versuch, Status/Erfolg, Dauer und Fehlerdetails)
- `codex.sse_event` (Art des Stream-Ereignisses, Erfolg/Fehlschlag, Dauer sowie Token-Anzahlen bei `response.completed`)
- `codex.websocket_request` und `codex.websocket_event` (Anfragedauer sowie Art/Erfolg/Fehler je Nachricht)
- `codex.user_prompt` (Länge; Inhalt maskiert, sofern dessen Protokollierung nicht ausdrücklich aktiviert ist)
- `codex.tool_decision` (genehmigt/abgelehnt, Quelle: Konfiguration oder nutzende Person)
- `codex.tool_result` (Dauer, Erfolg, Auszug aus der Ausgabe)

Zu den zugehörigen OTel-Metriken (jeweils ein Zähler und ein Histogramm für die Dauer) gehören `codex.api_request`, `codex.sse_event`, `codex.websocket.request`, `codex.websocket.event` und `codex.tool.call` (mit den entsprechenden `.duration_ms`-Instrumenten).

Den vollständigen Ereigniskatalog und die Konfigurationsreferenz findest du in der [Dokumentation zur Codex-Konfiguration auf GitHub](https://github.com/openai/codex/blob/main/docs/config.md#otel).

### Hinweise zu Sicherheit und Datenschutz

- Behalte `log_user_prompt = false` bei, sofern die geltenden Richtlinien das Speichern von Prompt-Inhalten nicht ausdrücklich erlauben. Prompts können Quellcode und sensible Daten enthalten.
- Leite Telemetriedaten nur an Collectors weiter, die du kontrollierst. Lege Aufbewahrungsfristen und Zugriffskontrollen fest, die deinen Compliance-Anforderungen entsprechen.
- Behandle Tool-Argumente und -Ausgaben als sensible Daten. Maskiere sie nach Möglichkeit direkt im Collector oder SIEM.
- Überprüfe die Einstellungen zur lokalen Datenaufbewahrung (z. B. `history.persistence` / `history.max_bytes`), wenn Codex keine Sitzungsprotokolle unter `CODEX_HOME` speichern soll. Weitere Informationen findest du unter [Erweiterte Konfiguration](/de-DE/codex/config-file/config-advanced#history-persistence) und [Konfigurationsreferenz](/de-DE/codex/config-file/config-reference).
- Wenn du die CLI ohne Netzwerkzugriff ausführst, kann der OTel-Export deinen Collector nicht erreichen. Erlaube für den Export im Modus `workspace-write` den Netzwerkzugriff auf den OTel-Endpunkt oder exportiere aus Codex Cloud, sofern die Domain des Collectors auf deiner Liste zugelassener Domains steht.
- Überprüfe Ereignisse regelmäßig auf Änderungen an Genehmigungen oder der Sandbox sowie auf unerwartete Toolausführungen.

OTel ist optional und soll die oben beschriebenen Schutzmechanismen für Sandbox und Genehmigungen ergänzen, nicht ersetzen.

## Verwaltete Konfiguration

Administrierende in Unternehmen können die Codex-Sicherheitseinstellungen für ihren Workspace unter [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration) konfigurieren. Einzelheiten zum Setup und zu Richtlinien findest du auf dieser Seite.

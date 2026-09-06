<!-- source: https://learn.chatgpt.com/de-DE/docs/permissions -->

Beta. Berechtigungsprofile werden aktiv weiterentwickelt und können sich ändern.

  Berechtigungsprofile lassen sich nicht mit den älteren Sandbox-Einstellungen kombinieren. Konfiguriere
  entweder `default_permissions` und `[permissions]` oder `sandbox_mode` /
`sandbox_workspace_write`, aber nicht beides. Wenn `sandbox_mode` in einer
  geladenen Konfigurationsdatei vorkommt, du `--sandbox` übergibst oder das ausgewählte Konfigurationsprofil
`sandbox_mode` festlegt, verwendet Codex statt
`default_permissions` diese älteren Sandbox-Einstellungen.

Die verwaltete Einstellung `allowed_permission_profiles` ist die Ausnahme: Dadurch verwendet Codex
Berechtigungsprofile. Entferne ältere Einstellungen wie
`sandbox_mode` und `[sandbox_workspace_write]`, bevor du eine verwaltete
Zulassungsliste für Profile bereitstellst. Bei einem Rollout mit gemischten Versionen in einem Unternehmen kannst du die
verwaltete Anforderung `allowed_sandbox_modes` vorübergehend
als Kompatibilitätsvorgabe beibehalten, bis auf jedem Client Codex 0.138.0 oder höher läuft.

Mit Berechtigungsprofilen kannst du Zugriffsgrenzen nach dem Prinzip der geringsten Rechte für lokale Befehle
festlegen, die Codex in deinem Auftrag ausführt. Ein Profil ist eine benannte Richtlinie, die Dateisystemregeln
mit Netzwerkregeln kombiniert. Die Dateisystemregeln bestimmen, was Befehle lesen oder schreiben dürfen; die Netzwerkregeln
legen fest, welche Ziele Befehle erreichen dürfen.

  Die Profileinstellung `network.enabled = true` erlaubt Befehlen den Netzwerkzugriff, startet aber
  nicht den Netzwerkproxy. Damit die Domainregeln des Profils durchgesetzt werden, setze zusätzlich
`features.network_proxy = true` in `config.toml` oder verwende aktivierte,
  administrativ verwaltete Anforderungen für `[experimental_network]`. Ohne aktiven
  Proxy schränken die Domainregeln des Profils den direkten Netzwerkzugriff nicht ein.

Verwende Profile, damit Codex im aktuellen Chat die nötigen Zugriffsrechte erhält, ohne ihm
weitreichenden Zugriff auf deinen Computer oder dein Netzwerk zu gewähren. Ein Profil ohne Schreibzugriff kann
Codex beispielsweise ein Projekt prüfen lassen, ohne es zu bearbeiten. Ein Profil mit Schreibzugriff
kann Änderungen auf ausgewählte Workspace-Stammverzeichnisse beschränken.

Lokale Berechtigungsprofile werden unter macOS, Linux, WSL und nativem
Windows unterstützt. Unter [Geltungsbereich und Durchsetzung](#scope-and-enforcement) findest du plattformspezifische
Details und Einschränkungen.

Informationen zu den Netzwerkeinstellungen für Codex Cloud findest du unter [Internetzugang](/de-DE/codex/cloud/internet-access).

## Profil definieren und auswählen

Codex enthält drei integrierte Berechtigungsprofile:

- `:read-only` beschränkt die lokale Befehlsausführung auf Vorgänge ohne Schreibzugriff.
- `:workspace` erlaubt Schreibzugriffe innerhalb der aktiven Workspace-Stammverzeichnisse und der temporären Systemverzeichnisse.
- `:danger-full-access` hebt lokale Sandbox-Einschränkungen auf und sollte
  nur verwendet werden, wenn dieser weitreichende Zugriff beabsichtigt ist.

Erstelle unter `[permissions.<name>]` ein benanntes Profil. Lege anschließend den Profilnamen oder einen der oben genannten integrierten Werte für den Schlüssel
`default_permissions` auf oberster Ebene fest.
In diesem Beispiel ist `project-edit` ein benutzerdefinierter Profilname und kein integrierter
Wert.

Administrierende in Unternehmen können Profile definieren und einschränken, welche Profile
über die verwaltete Datei `requirements.toml` ausgewählt werden dürfen. Sobald
`allowed_permission_profiles` vorhanden ist, sind nicht aufgeführte Profile unzulässig.
Das gilt auch für nicht aufgeführte integrierte Profile und Profile, die in künftigen Codex-Versionen hinzukommen. Unter
[Verfügbare Berechtigungsprofile steuern](/de-DE/codex/enterprise/managed-configuration#control-available-permission-profiles)
findest du die empfohlene verwaltete Konfiguration.

Benutzerdefinierte Profile verwenden zwei miteinander verbundene Konzepte:

- `[permissions.<name>.workspace_roots]` fügt konkrete Verzeichnisse hinzu, die
  für dieses Profil als Workspace-Stammverzeichnisse gelten sollen.
- `[permissions.<name>.filesystem.":workspace_roots"]` definiert die Dateisystemregeln, die Codex
  in jedem maßgeblichen Workspace-Stammverzeichnis anwendet. Dazu gehören die zur Laufzeit ermittelten Workspace-Stammverzeichnisse der aktuellen
  Sitzung und die oben für das Profil definierten Stammverzeichnisse.

Profile verwenden außerdem das übliche Modell der Konfigurationsebenen. Ebenen mit höherer Priorität können
unter demselben Profilnamen Einträge hinzufügen oder ersetzen, ohne das gesamte
Profil erneut anzugeben.

So können beispielsweise eine Konfiguration auf Organisationsebene und eine Konfiguration auf Nutzerebene
dasselbe Profil unabhängig voneinander erweitern:

```toml
# /etc/codex/config.toml
[permissions.server.workspace_roots]
"~/code/server" = true

```toml
# ~/.codex/config.toml
[permissions.server.workspace_roots]
"~/code/mobile-app" = true

Wenn `server` aktiv ist, fließen beide Workspace-Stammverzeichnisse in das resultierende
Profil ein.

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"
"objects.githubusercontent.com" = "allow"
"*.github.com" = "allow"
"tracking.example.com" = "deny"

Dieses Profil:

- Gewährt Lesezugriff auf die mindestens erforderlichen Laufzeitpfade für gängige Entwicklungstools.
- Wendet dieselben Regeln für Workspace-Stammverzeichnisse auf die aktuelle Sitzung und die
für das Profil definierten Stammverzeichnisse an.
- Verhindert Schreibzugriffe auf IDE-bezogene Einstellungen wie `.devcontainer/` in jedem
  Stammverzeichnis.
- Verweigert mithilfe einer Glob-Regel den Zugriff auf passende Umgebungsdateien.
- Erlaubt Netzwerkzugriff nur gemäß der konfigurierten Domainrichtlinie.

In einem aktiven Profil bleiben spezifischere Verweigerungsregeln in Kraft, auch wenn für einen allgemeineren
Pfad Lese- oder Schreibzugriff erlaubt ist. Ein Profil kann beispielsweise Schreibzugriff auf Workspace-Stammverzeichnisse
gewähren und zugleich für einen Pfad, der `.env` entspricht, den Wert `deny` festlegen.

## Profil erweitern

Verwende `extends`, wenn ein Profil weitgehend einem integrierten oder einem anderen benannten
Profil entspricht. Erweitere vorzugsweise ein integriertes Profil, statt von Grund auf zu beginnen, damit
die grundlegenden Schutzmaßnahmen erhalten bleiben. Wenn ein Profil beispielsweise `:workspace` erweitert, bleibt
das Verzeichnis `.codex` im Workspace-Stammverzeichnis ohne Schreibzugriff, sofern du dies nicht ausdrücklich
überschreibst. Lege das übergeordnete Profil einmal fest. Füge anschließend nur abweichende Regeln hinzu oder
überschreibe sie.

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
description = "Project editing with OpenAI API access."
extends = ":workspace"

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

Dieses Profil leitet sich von `:workspace` ab, verweigert weiterhin den Zugriff auf Dateien, die `.env` entsprechen, und
erlaubt Anfragen an `api.openai.com`. Ein Profil kann `:read-only`,
`:workspace` oder ein anderes benanntes Profil erweitern. Es kann
`:danger-full-access` nicht erweitern. Codex lehnt außerdem unbekannte übergeordnete Profile und
Vererbungszyklen ab.

## Konfigurationsspezifikation

| Eintrag                                                             | Typ / Werte              | Standardwert                 | Details                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------- | -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default_permissions`                                             | Profilname als String        | Keiner                    | Benennt das Berechtigungsprofil, das Codex standardmäßig anwendet. Es muss einem Profil unter `[permissions]` oder einem integrierten Profil wie `:workspace` entsprechen. Lege es für vorhersehbares Verhalten ausdrücklich fest. In verwalteten Anforderungen darf die Angabe nur fehlen, wenn sowohl `:workspace` als auch `:read-only` ausdrücklich zulässig sind. Codex verwendet ältere Sandbox-Einstellungen, es sei denn, die verwaltete Einstellung `allowed_permission_profiles` weist Codex in diesem Setup an, Berechtigungsprofile zu verwenden. |
| `[permissions.<name>]`                                            | Tabelle                      | Keiner                    | Definiert ein benanntes Profil. `default_permissions` legt ein Profil als Standard fest; weitere Einstellungen für Berechtigungsprofile verwenden ebenfalls den Profilnamen.                                                                                                                                                                                                                                                                               |
| `permissions.<name>.description`                                  | String                     | Keiner                    | Gibt eine verständliche Beschreibung des Profils an. Ein Profil erbt die Beschreibung seines übergeordneten Profils nicht über `extends`.                                                                                                                                                                                                                                                                                                 |
| `permissions.<name>.extends`                                      | Profilname als String        | Keiner                    | Leitet dieses Profil von einem anderen benannten Profil oder einem der integrierten Profile `:read-only` oder `:workspace` ab. Codex lehnt `:danger-full-access`, unbekannte übergeordnete Profile und Vererbungszyklen ab.                                                                                                                                                                                                                                            |
| `[permissions.<name>.workspace_roots]`                            | Tabelle                      | Keiner                    | Fügt für das Profil definierte Workspace-Stammverzeichnisse hinzu. Auf sie und die zur Laufzeit ermittelten Workspace-Stammverzeichnisse der aktuellen Sitzung werden die Dateisystemregeln für `:workspace_roots` angewendet.                                                                                                                                                                                                                                                                                |
| `permissions.<name>.workspace_roots."<path>"`                     | Boolescher Wert                    | `false`                 | Fügt den Pfad bei `true` zur Menge der Workspace-Stammverzeichnisse des Profils hinzu. Auf `false` gesetzte Einträge bleiben inaktiv.                                                                                                                                                                                                                                                                                                                        |
| `[permissions.<name>.filesystem]`                                 | Tabelle                      | Keiner                    | Ordnet Dateisystempfaden Zugriffswerte oder Zuordnungen für abgegrenzte Unterpfade zu. Bei fehlenden oder leeren Dateisystemtabellen bleibt der Dateisystemzugriff eingeschränkt und beim Start wird eine Warnung ausgegeben.                                                                                                                                                                                                                                                               |
| `permissions.<name>.filesystem.glob_scan_max_depth`               | Zahl                     | Keiner                    | Begrenzt die Expansion von Glob-Mustern für verweigerte Lesezugriffe unter Linux, WSL und nativem Windows, wenn Codex vor dem Start der Sandbox eine Momentaufnahme der Treffer erstellt. Höhere Werte können den Scanaufwand beim Start erhöhen. Verwende einen Wert von mindestens `1`, wenn ein unbeschränktes Muster wie `**` eine begrenzte Vorab-Expansion erfordert.                                                                                                                                                              |
| `[permissions.<name>.filesystem]."<path>"`                        | `read`, `write` oder `deny` | Keiner                    | Gewährt direkten Zugriff auf einen unterstützten Pfad. `deny` verweigert den Zugriff und hat Vorrang vor gleich spezifischen Einträgen mit `write` oder `read`. Codex lehnt direkte Schreibregeln ab, die die aktive Laufzeitumgebung nicht durchsetzen kann.                                                                                                                                                                                                                            |
| `[permissions.<name>.filesystem."<path>"]."<subpath>"`            | `read`, `write` oder `deny` | Keine                    | Gewährt Zugriff auf einen untergeordneten Pfad von `<path>`. Verwende `.` für den Basispfad. Weitere Unterpfade müssen relativ zum Basispfad angegeben werden und unterhalb davon liegen; sie dürfen `.` oder `..` nicht als Pfadkomponenten enthalten.                                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network]`                                    | Tabelle                      | Keine                    | Konfiguriert den Netzwerkzugriff für Befehle und die Richtlinie, die ein aktiver Netzwerk-Proxy durchsetzt. Aktiviere `features.network_proxy`, sofern der Proxy nicht durch administrativ verwaltete Netzwerkanforderungen gestartet wird.                                                                                                                                                                                                                                    |
| `permissions.<name>.network.enabled`                              | Boolescher Wert                    | `false`                 | Aktiviert den Netzwerkzugriff für Befehle im Profil. Der Netzwerk-Proxy wird dadurch nicht gestartet; ohne aktiven Proxy können Befehle direkte Verbindungen ohne Domain-Einschränkungen herstellen.                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network.domains]`                            | Tabelle                      | Keine                    | Ordnet Hostmustern `allow` oder `deny` zu. Die Regeln gelten nur bei aktivem Netzwerk-Proxy. Der aktive Proxy blockiert Domain-Anfragen, wenn keine `allow`-Einträge vorhanden sind; Einträge zum Verweigern haben Vorrang vor Einträgen zum Zulassen.                                                                                                                                                                                                                 |
| `permissions.<name>.network.domains."<pattern>"`                  | `allow` oder `deny`          | Keine                    | Unterstützt exakte Hosts, `*.example.com` für Subdomains, `**.example.com` für die Apex-Domain und ihre Subdomains sowie `*` als globalen Platzhalter, der ausschließlich in Zulassungsregeln verwendet werden darf. Hostmuster werden normalisiert, indem führender und nachgestellter Leerraum entfernt, alle Zeichen in Kleinbuchstaben umgewandelt sowie ein abschließender Punkt und einfache Portangaben oder Klammern entfernt werden.                                                                                                                                                           |
| `[permissions.<name>.network.unix_sockets]`                       | Tabelle                      | Keine                    | Konfiguriert Überschreibungen für die Zulassungsliste von Unix-Sockets. Verwende dies nur für lokale Integrationen wie Docker.                                                                                                                                                                                                                                                                                                                                         |
| `permissions.<name>.network.unix_sockets."<path>"`                | `allow` oder `deny`          | Keine                    | Fügt mit `allow` einen absoluten Unix-Socket-Pfad zur wirksamen Zulassungsliste hinzu oder lehnt ihn mit `deny` ab. Abgelehnte Einträge werden nicht in die wirksame Zulassungsliste aufgenommen.                                                                                                                                                                                                                                                                |
| `permissions.<name>.network.proxy_url`                            | URL-Zeichenfolge                 | `http://127.0.0.1:3128` | HTTP-Proxy-Listener für `HTTP_PROXY`, `HTTPS_PROXY`, WebSocket-Proxy-Variablen und zugehörige Proxy-Umgebungsvariablen von Tools.                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.enable_socks5`                        | Boolescher Wert                    | `true`                  | Aktiviert den für `ALL_PROXY` und FTP-Proxy-Variablen verwendeten SOCKS5-Listener.                                                                                                                                                                                                                                                                                                                                                     |
| `permissions.<name>.network.socks_url`                            | URL-Zeichenfolge                 | `http://127.0.0.1:8081` | Adresse des SOCKS5-Listeners.                                                                                                                                                                                                                                                                                                                                                                                                      |
| `permissions.<name>.network.enable_socks5_udp`                    | Boolescher Wert                    | `true`                  | Aktiviert die SOCKS5-UDP-Unterstützung, wenn der SOCKS5-Listener aktiviert ist.                                                                                                                                                                                                                                                                                                                                                               |
| `permissions.<name>.network.allow_upstream_proxy`                 | Boolescher Wert                    | `true`                  | Erlaubt dem Netzwerk-Sandbox-Proxy, bei ausgehenden Anfragen vorgelagerte Einstellungen für `HTTP(S)_PROXY` und `ALL_PROXY` zu berücksichtigen.                                                                                                                                                                                                                                                                                                          |
| `permissions.<name>.network.allow_local_binding`                  | Boolescher Wert                    | `false`                 | Deaktiviert bei `true` den Schutzmechanismus für lokale und private Netzwerke. Bei `false` müssen exakte lokale Angaben wie `localhost` oder `127.0.0.1` ausdrücklich in die Zulassungsliste aufgenommen werden; Hostnamen, die zu lokalen oder privaten IP-Adressen aufgelöst werden, bleiben blockiert.                                                                                                                                                                                                |
| `permissions.<name>.network.dangerously_allow_non_loopback_proxy` | Boolescher Wert                    | `false`                 | Erlaubt Proxy-Listenern die Bindung an Adressen außerhalb des Loopback-Bereichs. Lege diese Einstellung bei der üblichen lokalen Entwicklung nicht fest.                                                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.dangerously_allow_all_unix_sockets`   | Boolescher Wert                    | `false`                 | Umgeht die Zulassungsliste für Unix-Sockets, sofern die Weiterleitung von Unix-Sockets über einen Proxy unterstützt wird. Dies eröffnet eine weitreichende Möglichkeit, lokale Beschränkungen zu umgehen.                                                                                                                                                                                                                                                                                                               |

## Dateisystemberechtigungen

Dateisystemeinträge verwenden `read`, `write` oder `deny`:

| Zugriff  | Bedeutung                                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `read`  | Erlaubt Befehlen, Dateien unterhalb des Pfads zu lesen und Verzeichnisse aufzulisten. Sie können dort keine Dateien erstellen, ändern, umbenennen oder löschen. |
| `write` | Erlaubt Befehlen, Dateien unterhalb des Pfads zu lesen und zu ändern. Sofern das Betriebssystem dies zulässt, können sie dort auch Dateien erstellen, umbenennen und löschen.  |
| `deny`  | Verweigert unterhalb des Pfads sowohl Lese- als auch Schreibzugriffe. Verwende diese Einstellung, um innerhalb einer allgemeineren `read`- oder `write`-Berechtigung einen Unterpfad zu sperren.         |

Spezifischere Einträge haben Vorrang vor allgemeineren. Wenn zwei Einträge denselben
Pfad betreffen, hat `deny` Vorrang vor `write` und `write` wiederum Vorrang
vor `read`.

Diese Rangfolge ermöglicht es, in einem Profil zunächst einen umfassenden Arbeitsbereich festzulegen und anschließend
Dateien oder Verzeichnisse auszunehmen, auf die weiterhin kein Lesezugriff möglich sein soll:

```toml
[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

In diesem Beispiel bleibt das Workspace-Stammverzeichnis beschreibbar, `.devcontainer/` bleibt
lesbar, ohne beschreibbar zu werden, und Umgebungsdateien, die dem Muster entsprechen, bleiben
für Befehle in der Sandbox unzugänglich.

Eine spezifischere Pfadangabe kann auch einen enger gefassten Teilbaum innerhalb einer umfassenderen Sperrregel wieder freigeben:

```toml
[permissions.project-edit.filesystem]
"~/Documents" = "deny"
"~/Documents/codex" = "write"

Unterstützte Pfadformen:

| Pfad               | Bedeutung                                                                                     | Eingrenzung auf Unterpfade |
| ------------------ | ------------------------------------------------------------------------------------------- | --------------- |
| `:root`            | Das Stammverzeichnis des Dateisystems                                                                         | Nur `.`        |
| `:minimal`         | Von gängigen Tools benötigte Plattform- und Laufzeitpfade                                           | Nur `.`        |
| `:workspace_roots` | Die Workspace-Stammverzeichnisse der aktuellen Sitzung sowie alle aktivierten und im Profil definierten Workspace-Stammverzeichnisse      | Ja             |
| `:tmpdir`          | Der durch `$TMPDIR` angegebene Speicherort, sofern verfügbar                                               | Nur `.`        |
| `:slash_tmp`       | Der Ordner `/tmp`, sofern vorhanden                                                             | Nur `.`        |
| `/absolute/path`   | Ein absoluter Pfad für die jeweilige Plattform, beispielsweise `/path` unter macOS/Linux/WSL oder `C:\path` unter nativem Windows | Ja             |
| `~/path`           | Ein Pfad unterhalb des Home-Verzeichnisses des aktuellen Benutzerkontos                                              | Ja             |

Unter nativem Windows können Pfade relativ zum Home-Verzeichnis auch umgekehrte Schrägstriche enthalten, zum Beispiel
`~\work`.

Verwende `:root` nur, wenn ein Profil bewusst umfassenden Lesezugriff benötigt:

```toml
[permissions.audit.filesystem]
":root" = "read"

Verwende verschachtelte Einträge unter `:workspace_roots`, um den Zugriff auf Unterpfade
relativ zum Workspace-Stammverzeichnis einzugrenzen:

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"          # each workspace root
"docs" = "read"        # each workspace-root docs directory
"generated" = "deny"   # each workspace-root generated directory

Verschachtelte Unterpfade müssen innerhalb ihres Workspace-Stammverzeichnisses bleiben. Verweise auf übergeordnete Verzeichnisse wie
`../other-repo` werden abgelehnt.

### Lesezugriff mit exakten Pfaden oder Globs verweigern

Verwende `deny` für Dateien oder Verzeichnisbäume, die Codex nicht lesen soll, selbst wenn eine weiter gefasste
Profilregel den Zugriff auf benachbarte Bereiche erlaubt. Exakte Pfade eignen sich für feste Speicherorte
wie `~/.ssh`. Glob-Muster sind besser geeignet, wenn ein Profil eine
Gruppe sensibler Dateien abdecken soll, deren genaue Speicherorte sich je nach Repository unterscheiden.

Wenn sich ein Glob-Muster unter `:workspace_roots` befindet, interpretiert Codex es relativ zu jedem
effektiven Workspace-Stammverzeichnis. Beispiel:

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

Diese Regel verweigert den Lesezugriff auf passende `.env`-Dateien in jedem zur Laufzeit oder
im Profil festgelegten Workspace-Stammverzeichnis. Verwende sie, wenn normale
Schreibzugriffe im Workspace weiterhin möglich sein sollen, Umgebungsdateien, generierte Secrets oder ähnliche
Dateien mit Zugangsdaten aber nicht lesbar sein dürfen.

`deny`-Glob-Muster werden als Regeln zum Verweigern des Lesezugriffs unterstützt. Globs mit `read` oder `write`
sind beim Sandboxing unter Linux, WSL und nativem Windows weniger portabel. Verwende daher möglichst exakte
Pfade oder Regeln für Unterverzeichnisse wie `"docs/**" = "read"`.

Unter Linux, WSL und nativem Windows kann bei einem unbegrenzten `**`-Muster zum Verweigern des Lesezugriffs
vor dem Start der Sandbox eine begrenzte Vorabexpansion erforderlich sein. Lege `glob_scan_max_depth` fest, wenn
du ein unbegrenztes Muster wie `"**/*.env" = "deny"` verwendest:

```toml
[permissions.project-edit.filesystem]
glob_scan_max_depth = 3

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

`glob_scan_max_depth` muss mindestens `1` betragen. Bei höheren Werten werden vor
dem Start der Sandbox tiefere Ebenen durchsucht. Das kann unter Linux, WSL und nativem Windows zusätzlichen Aufwand beim Start verursachen.
Wenn du keine begrenzte Expansion verwenden möchtest, gib konkrete Tiefen an, zum Beispiel
`*.env`, `*/*.env` und `*/*/*.env`.

Füge dem Profil wiederverwendbare Workspace-Stammverzeichnisse hinzu, wenn dieselben Regeln nicht nur für
das Stammverzeichnis der aktuellen Sitzung gelten sollen:

```toml
[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

Wenn dieses Profil aktiv ist, wendet Codex die Regeln unter `:workspace_roots` auf die
zur Laufzeit festgelegten Workspace-Stammverzeichnisse der aktuellen Sitzung sowie auf jedes aktivierte
Workspace-Stammverzeichnis aus der Profildefinition an.

Unter nativem Windows werden Pfade mit Laufwerkbuchstaben wie `D:\work` und UNC-Pfade wie
`\\server\share` als absolute Pfade unterstützt.

## Netzwerkberechtigungen

Netzwerkzugriff und Netzwerkfilterung werden getrennt konfiguriert. Lege
`permissions.<name>.network.enabled = true` fest, damit Befehle auf das Netzwerk zugreifen können,
und aktiviere `features.network_proxy`, um die Domänenregeln des Profils durchzusetzen:

```toml
[features]
network_proxy = true

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"example.com" = "allow"      # exact host
"*.example.com" = "allow"    # subdomains only
"**.example.com" = "allow"   # apex and subdomains
"ads.example.com" = "deny"   # deny wins over allow

Das jeweilige Verhalten hängt von beiden Einstellungen ab:

- Netzwerk aus: Befehle können unabhängig von der Proxy-Funktion nicht auf das Netzwerk
zugreifen.
- Netzwerk ein, Proxy aus: Befehle haben direkten, uneingeschränkten Zugriff auf das
Netzwerk. Die Domänenregeln im Berechtigungsprofil werden nicht durchgesetzt.
- Netzwerk ein, Proxy ein: Befehle verwenden den Proxy, der die Domänenregeln
des Profils durchsetzt. Wenn für den aktiven Proxy keine Domänen zugelassen sind, blockiert er externe
Ziele.

Weder das Hinzufügen von `[permissions.<name>.network.domains]` noch die Einstellung
`permissions.<name>.network.enabled = true` aktiviert
`features.network_proxy`. Alternativ können Administrierende den
Proxy mit `[experimental_network]` in `requirements.toml` aktivieren. Weitere Informationen findest du unter
[Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration#configure-network-access-requirements).

Ein aktiver Netzwerk-Sandbox-Proxy bindet standardmäßig an lokale Listener:

```toml
[permissions.project-edit.network]
enabled = true
proxy_url = "http://127.0.0.1:3128"
enable_socks5 = true
socks_url = "http://127.0.0.1:8081"
enable_socks5_udp = true

Belasse diese Listener-Einstellungen auf ihren Standardwerten, sofern du Codex nicht in eine bestimmte
Laufzeitumgebung integrierst. Die Netzwerkschlüssel `dangerously_*` sind Ausweichmechanismen für
spezialisierte Umgebungen und sollten nicht für die normale lokale Entwicklung verwendet werden.

### Lokale und private Netzwerke

Wenn der Netzwerk-Proxy aktiv ist, aktiviert Codex standardmäßig einen Schutz für lokale und private
Netzwerke, um DNS-Rebinding und unbeabsichtigten Zugriff auf lokale Dienste zu verhindern. Um ein
lokales Ziel bewusst direkt zuzulassen, nimm den exakten Hostnamen oder die exakte IP-Adresse in die
Zulassungsliste auf:

```toml
[permissions.project-edit.network.domains]
"localhost" = "allow"
"127.0.0.1" = "allow"

Lege `allow_local_binding = true` nur fest, wenn das Profil auf der Zulassungsliste stehende
Hostnamen erreichen muss, die in lokale oder private Adressen aufgelöst werden:

```toml
[permissions.project-edit.network]
enabled = true
allow_local_binding = true

[permissions.project-edit.network.domains]
"localhost" = "allow"

### Unix-Sockets

Die Weiterleitung von Unix-Sockets über einen Proxy ist ein lokaler Ausweichmechanismus für Tools wie Docker. Setze sie
sparsam ein:

```toml
[permissions.project-edit.network.unix_sockets]
"/var/run/docker.sock" = "allow"
"/tmp/old.sock" = "deny"

Verwende `deny`, um einen Socket-Pfad abzulehnen, auch wenn ein Zulassungseintrag geerbt wurde. Abgelehnte
Socket-Pfade werden nicht in die effektive Zulassungsliste aufgenommen.

Wenn Unix-Sockets aktiviert sind, binde Proxy-Listener weiterhin ausschließlich an Loopback-Adressen.

## Migration von älteren Sandbox-Einstellungen

Berechtigungsprofile ersetzen die frühere Kombination aus `sandbox_mode` und
`sandbox_workspace_write`, wenn ein wiederverwendbares Profil sowohl
Dateisystem- als auch Netzwerkzugriffe regeln soll. Verwende für eine Sitzung entweder das eine oder das andere System,
nicht beide.

Empfohlene Einstiegskonfigurationen:

- Verwende für einen Ablauf ohne Schreibzugriff das integrierte Profil `:read-only` oder definiere ein
  benutzerdefiniertes Profil, das nur dort Lesezugriff gewährt, wo er benötigt wird.
- Verwende zum Bearbeiten des Workspace das integrierte Profil `:workspace` oder definiere ein
  benutzerdefiniertes Profil, das über `:workspace_roots` Schreibzugriff gewährt und nur die zusätzlichen
  temporären Pfade oder Cache-Pfade hinzufügt, die für den Ablauf benötigt werden.
- Verwende `:danger-full-access` für die uneingeschränkte lokale Ausführung nur, wenn du
  bewusst das weitreichendste lokale Zugriffsmodell einsetzen möchtest.

Profile legen die lokale Standardkonfiguration einer Sitzung fest. Von der Organisation verwaltete
Vorgaben können zusätzliche Einschränkungen festlegen, die eine Benutzerkonfiguration nicht
lockern darf. Unter [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration)
findest du Informationen zu administrativ erzwungenen Einschränkungen für Dateisystem und Netzwerk.

## Geltungsbereich und Durchsetzung

Berechtigungsprofile legen die Grenzen für die lokale Ausführung von Befehlen in einer
Sandbox fest. Verwende sie zusammen mit Genehmigungsrichtlinien und den separaten Kontrollmechanismen
für die Websuche, Konnektoren, MCP-Server, den integrierten Browser, die Computernutzung
und Codex Cloud.

### Was Profile regeln

- **Lokale Befehlsausführung:** Berechtigungsprofile regeln die Ausführung von Befehlen in der Sandbox
  auf deinem Computer. Für Konnektoren, MCP-Server, Browser- und
  Computernutzungsfunktionen, Umgebungseinstellungen von Codex Cloud sowie genehmigte
  Berechtigungsausweitungen gelten eigene Kontrollmechanismen.
- **Schreibzugriffe auf das Dateisystem:** Ein Profil mit Schreibzugriff kann dauerhafte Änderungen verursachen.
  Behandle Schreibzugriffe auf Skripte, Build-Schritte, Paketmanager-Hooks, Shell-Startdateien
  und gemeinsam genutzte Verzeichnisse als sicherheitskritisch, da Tools oder andere Personen diese Dateien später
  außerhalb des ursprünglichen Sandbox-Kontexts ausführen können.
- **Ziele ausgehender Verbindungen:** Domänenregeln begrenzen die Ziele des Netzwerkverkehrs von Befehlen in der Sandbox
  nur, solange der Netzwerk-Proxy aktiv ist. Sie geben keinen Aufschluss darüber,
  ob ein zugelassenes Ziel vertrauenswürdig ist. Zulassungsregeln mit Platzhaltern bleiben
  weit gefasst.
- **Lokale Dienste:** Ein aktiver Netzwerk-Proxy blockiert Ziele in lokalen und privaten Netzwerken
  standardmäßig. Wenn du `localhost`, private IP-Adressen oder Unix-Sockets zur Zulassungsliste hinzufügst oder
`allow_local_binding = true` festlegst, erlaubst du ausdrücklich den Zugriff auf lokale Dienste.

### Was der Netzwerk-Proxy nicht regelt

Der Netzwerk-Proxy filtert nur den Datenverkehr lokaler Befehle, die innerhalb der
Sandbox ausgeführt werden. Die Domänen-Zulassungsliste des Profils gilt nicht für:

- **Websuche:** Das gehostete Suchtool verwendet eigene Zugriffseinstellungen. Steuere es mit
`web_search` und bei verwalteten Clients zusätzlich mit `allowed_web_search_modes`.
  `tools.web_search.allowed_domains` filtert Suchergebnisse, aber nicht den Netzwerkzugriff von
  Befehlen.
- **Apps und Konnektoren:** Konnektorbasierte Tools verwenden eigene dienstseitige
  Verbindungen, Workspace-Berechtigungen sowie App- oder Tool-Einstellungen.
- **MCP-Server:** Lokale und entfernte MCP-Server verwenden eigene Prozesse oder
  Transportmechanismen. Steuere sie über die Konfiguration `mcp_servers` und verwaltete
  Zulassungslisten für Server.
- **Browser und Computernutzung:** Für die Navigation im Browser und Aktionen der Computernutzung
  gelten eigene Einstellungen für Funktionen und Genehmigungen.
- **Datenverkehr der Codex-Dienste:** Anfragen an Modelle, zur Authentifizierung und an andere Client-Dienste
  verwenden die separaten HTTP- und System-Proxy-Einstellungen des Clients.
- **Codex Cloud:** Diese Aufgaben verwenden die eigenen
[Einstellungen für den Internetzugang](/de-DE/codex/cloud/internet-access) ihrer Umgebung.

Um diese Bereiche einzuschränken, konfiguriere jede Funktion direkt. Eine Zulassungsliste
für den Netzwerkzugriff von Befehlen ist keine globale Netzwerkrichtlinie für alle Aktionen, die Codex ausführen kann.

### So funktioniert die Durchsetzung

- Unter macOS verwendet Codex Seatbelt-Sandbox-Profile. Wenn die ausgewählte Richtlinie von der Plattform-Sandbox nicht
durchgesetzt werden kann, verweigert Codex die Ausführung des Befehls, anstatt ihn stillschweigend
ohne Sandbox auszuführen.
- Unter Linux und WSL verwendet Codex [bubblewrap](https://github.com/containers/bubblewrap)
  und [seccomp](https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html).
  Für kompatible Ausweichlösungen steht Landlock zur Verfügung. Die wirksamste
  Methode zur Durchsetzung hängt von Benutzer-Namespaces und der Kernel-Unterstützung ab. Eingeschränkte
  Container-Hosts können kompatible Ausweichlösungen erforderlich machen. Nicht unterstützte Richtlinien mit getrennten Zugriffsregeln
  werden abgelehnt.
- Unter nativem Windows bietet [Sandboxing mit `elevated`](/de-DE/codex/windows/windows-sandbox#windows-sandbox)
  den stärksten Schutz, weil dabei eigene Sandbox-Benutzerkonten mit eingeschränkten Berechtigungen,
  Berechtigungsgrenzen im Dateisystem und Firewallregeln genutzt werden können. Sandboxing mit `unelevated`
  ist eine Ausweichlösung mit schwächerer Netzwerkisolierung und kann nicht alle getrennten Ausnahmen für Lese- und Schreibzugriffe
  durchsetzen. Nicht unterstützte Richtlinien werden daher abgelehnt. Verwende WSL,
  wenn du das Sandbox-Modell von Linux benötigst.

### Hinweise zum Betrieb

Wähle das restriktivste Profil, mit dem sich die Aufgabe noch abschließen lässt, insbesondere wenn
du Schreibzugriffe oder ausgehenden Netzwerkzugriff gewährst. Stimme Genehmigungsrichtlinie, Umgang mit Secrets
und Zulassungsregeln auf diese Zugriffsebene ab.

## Gängige Profile

### Ohne Schreibzugriff mit Netzwerk-Zulassungsliste

```toml
default_permissions = "readonly-net"

[features]
network_proxy = true

[permissions.readonly-net.filesystem]
":minimal" = "read"

[permissions.readonly-net.filesystem.":workspace_roots"]
"." = "read"

[permissions.readonly-net.network]
enabled = true

[permissions.readonly-net.network.domains]
"api.openai.com" = "allow"

### Dateizugriff auf den Workspace beschränkt

Das folgende Beispiel zeigt ein Berechtigungsprofil, das Codex Schreibzugriff auf deine Workspace-Ordner gewährt und Lesezugriffe auf das übrige Dateisystem verweigert (mit begrenzten Ausnahmen gemäß `:minimal`).

```toml
default_permissions = "workspace-only"

[permissions.workspace-only]
# By extending the :workspace profile, you get Codex's safeguards to ensure
# subfolders such as .codex/ and .git/ within a workspace root are read-only
# while the rest of the folder is writable.
extends = ":workspace"

[permissions.workspace-only.filesystem]
# By default, deny read access to all files on disk.
":root" = "deny"

# Though in practice, a software agent needs to be able to read folders that
# contain common tools, such as `/usr/bin`, to get work done, so grant access
# to a "minimal" set of files and folders, as determined by Codex.
":minimal" = "read"

# By extending the :workspace profile, :tmpdir and :slash_tmp are "write" by
# default, though you can deny access to them altogether, if desired.
":tmpdir" = "deny"
":slash_tmp" = "deny"

### Workspace-Schreibzugriff ohne Netzwerkzugriff

```toml
default_permissions = "project-edit"

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"

[permissions.project-edit.network]
enabled = false

### Workspace-Schreibzugriff mit öffentlichem Webzugriff

```toml
default_permissions = "workspace-net"

[features]
network_proxy = true

[permissions.workspace-net.filesystem]
":minimal" = "read"

[permissions.workspace-net.filesystem.":workspace_roots"]
"." = "write"

[permissions.workspace-net.network]
enabled = true

[permissions.workspace-net.network.domains]
"*" = "allow"

Verwende die globale Zulassungsregel `"*"` nur, wenn du öffentlichen Netzwerkzugriff
erlauben möchtest. Sperrregeln können eine weit gefasste Zulassungsliste einschränken.

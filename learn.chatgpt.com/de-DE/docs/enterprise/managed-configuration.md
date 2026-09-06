<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/managed-configuration -->

Die verwaltete Konfiguration steuert für die abgedeckten Funktionen das unterstützte lokale Laufzeitverhalten in der ChatGPT-Desktop-App, der Codex CLI und der IDE-Erweiterung. Welche Anforderungen unterstützt werden, kann je nach Client und Version variieren. Die verwaltete Konfiguration gewährt keinen Zugriff auf den ChatGPT-Workspace, weist keine Lizenzen zu und ersetzt nicht die rollenbasierte Zugriffskontrolle (RBAC) für den Workspace. Informationen zum Zugriff auf Workspace-Funktionen findest du unter [Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions). Diese Seite behandelt Richtlinien für die lokale Laufzeit.

Administrierende in Unternehmen können das Verhalten unterstützter lokaler Clients auf zwei Arten steuern:

- **Anforderungen**: von der Administration durchgesetzte Einschränkungen, die Nutzende nicht überschreiben können.
- **Verwaltete Standardwerte**: Ausgangswerte, die beim Start eines unterstützten Clients angewendet werden. Nutzende können die Einstellungen während einer Ausführung weiterhin ändern. Beim nächsten Start wendet der Client die verwalteten Standardwerte erneut an.

## Von der Administration durchgesetzte Anforderungen (requirements.toml)

Anforderungen schränken sicherheitsrelevante Einstellungen ein: die Genehmigungsrichtlinie, die Prüfinstanz für Genehmigungen, die Richtlinie für die automatische Überprüfung, den Sandbox-Modus, Berechtigungsprofile, den Websuchmodus und verwaltete Hooks. Sie regeln außerdem, welche MCP-Server Nutzende aktivieren dürfen und welche selbst konfigurierten Marketplace-Quellen für Plug-ins sie hinzufügen, für Installationen verwenden oder aktualisieren dürfen. Wenn beim Auflösen der Konfiguration, beispielsweise anhand von `config.toml`, [Profildateien](/de-DE/codex/config-file/config-advanced#profiles) oder Überschreibungen der CLI-Konfiguration, ein Wert einer durchgesetzten Regel widerspricht, greift der lokale Client auf einen kompatiblen Wert zurück und benachrichtigt die Nutzenden. Wenn du eine Zulassungsliste für `mcp_servers` konfigurierst, aktiviert der Client einen MCP-Server nur, wenn sowohl sein Name als auch seine Identität einem genehmigten Eintrag entsprechen. Andernfalls deaktiviert er ihn.

Anforderungen können auch [Feature-Flags](/de-DE/codex/config-file/config-basic/#feature-flags) über die Tabelle `[features]` in `requirements.toml` einschränken. Funktionen sind nicht immer sicherheitsrelevant. Unternehmen können Werte jedoch bei Bedarf fest vorgeben. Nicht angegebene Schlüssel bleiben uneingeschränkt.

Verwende ab Codex 0.138.0 vorzugsweise [Berechtigungsprofile](/de-DE/codex/permissions)
mit `allowed_permission_profiles` und der verwalteten Einstellung `default_permissions`. Verwende
`allowed_sandbox_modes` nur für ältere Bereitstellungen, die weiterhin
`sandbox_mode` konfigurieren.

Die genaue Liste der Schlüssel findest du im [Abschnitt zu `requirements.toml` in der Konfigurationsreferenz](/de-DE/codex/config-file/config-reference#requirementstoml).

### Speicherorte und Prioritätsreihenfolge

Jeder unterstützte lokale Client setzt die Anforderungen aus folgenden Quellen zusammen, von niedriger zu höherer Priorität:

1. Systemweite Datei `requirements.toml` (`/etc/codex/requirements.toml` auf Unix-Systemen,
   einschließlich Linux und macOS, oder `%ProgramData%\OpenAI\Codex\requirements.toml`
   unter Windows).
2. Vom Unternehmen verwaltete Anforderungen, die im Cloud-Konfigurationspaket bereitgestellt werden.
3. Veraltete Felder in `managed_config.toml`, die der lokale Client als Anforderungen interpretiert.
4. Verwaltete macOS-Einstellungen (MDM), bereitgestellt über
`com.openai.codex:requirements_toml_base64`.

Ebenen mit höherer Priorität überschreiben reguläre skalare Werte und Listenwerte aus niedriger priorisierten
Ebenen. Tabellen werden anhand ihrer Schlüssel zusammengeführt. Für Anforderungen wie Regeln, Hooks und
Dateisystemeinschränkungen gelten dagegen feldspezifische Regeln für die Zusammenführung. Das aktuelle Schema findest du in der
[Referenz zu `requirements.toml`](/de-DE/codex/config-file/config-reference#requirementstoml).
Gehe nicht davon aus, dass alle Felder auf dieselbe
Weise zusammengeführt werden.

Aus Gründen der Abwärtskompatibilität interpretieren unterstützte lokale Clients die veralteten Felder
`approval_policy`, `approvals_reviewer` und `sandbox_mode` als
Anforderungen. Diese Umwandlung ergänzt bei Bedarf Kompatibilitätsoptionen. Verwende
`requirements.toml` für explizite Zulassungslisten.

### Über die Cloud verwaltete Anforderungen

Wenn sich Nutzende mit ChatGPT anmelden und einen unterstützten Tarif verwenden, können unterstützte lokale Clients
die mit dem Workspace verknüpften, von der Administration durchgesetzten Anforderungen empfangen. Dies ist
ein Bereitstellungskanal für Richtlinien, die mit `requirements.toml` kompatibel sind. Dadurch wird weder
Zugriff auf den Workspace gewährt noch die RBAC des Workspace ersetzt.

Öffne [Verwaltete Konfiguration](https://chatgpt.com/codex/settings/managed-configs),
um über die Cloud verwaltete Anforderungen zu erstellen und zuzuweisen. Diese Richtlinie schränkt beispielsweise
die Auswahlmöglichkeiten für Genehmigungen und die Sandbox ein und fordert vor der Ausführung
eines unterstützten Shell-Einstiegspunkts zur Bestätigung auf:

```toml
allowed_approval_policies = ["on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

[rules]
prefix_rules = [
  { pattern = [{ any_of = ["bash", "sh", "zsh"] }], decision = "prompt", justification = "Require explicit approval for shell entry points" },
]

Vergewissere dich, dass jede verwaltete Clientversion die ausgewählten Schlüssel unterstützt, und
teste die Richtlinie mit einer kleinen Gruppe, bevor du sie der gesamten Organisation zuweist. Das aktuelle Schema findest du
in der Konfigurationsreferenz. In der Administrationsoberfläche kannst du prüfen,
wie Zuweisungen derzeit funktionieren.

Der Dienst wählt die vom Unternehmen verwalteten Anforderungsebenen aus, die für die
angemeldete Identität gelten. Der lokale Client wertet diese Ebenen zusammen mit den übrigen
Anforderungsquellen aus, die unter [Speicherorte und Prioritätsreihenfolge](#locations-and-precedence) beschrieben sind.
Verwende die aktuelle Administrationsoberfläche, um Richtlinien im Workspace zu erstellen und
zuzuweisen. Verlass dich nicht auf einen kopierten Algorithmus zur Gruppenzuordnung. Der Administrationsdienst
steuert dieses Verhalten und kann es unabhängig vom lokalen
Anforderungsformat ändern.

Unterstützte Schlüssel und Beispiele findest du unter
[Beispiel für requirements.toml](#example-requirementstoml) und in der
[Referenz zu `requirements.toml`](/de-DE/codex/config-file/config-reference#requirementstoml).

#### So wenden lokale Clients über die Cloud verwaltete Anforderungen an

Wenn Nutzende einen unterstützten lokalen Client starten, sich mit ChatGPT anmelden und einen
unterstützten Tarif verwenden, sucht der Client zunächst nach einem gültigen, zur Identität passenden
Cache-Eintrag. Ist kein gültiger Eintrag vorhanden, ruft der Client das passende Paket ab, wiederholt den
Abruf bei Bedarf und schreibt bei Erfolg einen signierten Cache-Eintrag. Wenn kein gültiger Cache
vorhanden ist und die Anfrage entweder fehlschlägt oder das Zeitlimit überschreitet, gibt das Laden des
Cloud-Konfigurationspakets einen Fehler zurück. Der Client startet nicht unbemerkt ohne die Ebene mit
den über die Cloud verwalteten Anforderungen.

Nachdem der Cache-Eintrag ermittelt wurde, führt der Client die Cloud-Anforderungen mit den
oben beschriebenen anderen Anforderungsebenen zusammen. Eine Hintergrundaktualisierung kann den
Cache für einen späteren Start aktualisieren. Sie ersetzt jedoch nicht die Anforderungen, die bereits
in den aktuellen Prozess geladen wurden.

### Abläufe für Administration und Mitarbeitende überprüfen

Benenne für jede verwaltete Richtlinie eine verantwortliche Person und halte fest, welche Nutzenden oder Gruppen
sie erhalten sollen. Dokumentiere außerdem den geschäftlichen Grund für jede Einschränkung des Dateisystems, des Netzwerks,
der Genehmigungen oder der Berechtigungsprofile.

Bevor du den Rollout ausweitest, teste mit einer repräsentativen Person aus der Zielgruppe einen genehmigten und einen bewusst
unzulässigen Ablauf. Überprüfe die tatsächlich wirksamen Einstellungen im unterstützten Client,
statt davon auszugehen, dass eine Workspace-Rolle oder Gruppe allein die lokale Einschränkung
durchsetzt.

### Beispiel für requirements.toml

Dieses Beispiel blockiert `--ask-for-approval never` und `--sandbox danger-full-access` (einschließlich `--yolo`):

```toml
allowed_approval_policies = ["untrusted", "on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

### Appshots deaktivieren

Um Appshots für verwaltete Nutzende zu deaktivieren, lege auf oberster Ebene die Anforderung `allow_appshots` fest:

```toml
allow_appshots = false

Wo Appshots verfügbar sind, werden sie durch `allow_appshots = false` deaktiviert. Wenn du
den Schlüssel weglässt, schränken die Anforderungen Appshots nicht ein und es gelten die üblichen
Prüfungen der Produktverfügbarkeit. Clients des App Server, die die geltenden Anforderungen
über `configRequirements/read` auslesen, erhalten dieselbe Einschränkung in Form von
`allowAppshots`. Ein nicht angegebener Wert oder der Wert `null` für `allowAppshots` deaktiviert
Appshots nicht.

### Gerätefernsteuerung deaktivieren

Um die [Gerätefernsteuerung](/de-DE/codex/remote-connections#pick-up-work-from-another-device)
für verwaltete Nutzende zu deaktivieren, lege auf oberster Ebene die Anforderung `allow_remote_control` fest:

```toml
allow_remote_control = false

Sofern die Gerätefernsteuerung unterstützt wird, wird sie durch `allow_remote_control = false`
deaktiviert. Wenn du den Schlüssel weglässt, schränken die Anforderungen die Gerätefernsteuerung nicht ein
und es gelten die üblichen Prüfungen der Produktverfügbarkeit. Diese Anforderung deaktiviert
Remote-Verbindungen über SSH nicht.

### Verfügbare Berechtigungsprofile steuern

Mit `allowed_permission_profiles` steuerst du, welche integrierten und benutzerdefinierten
[Berechtigungsprofile](/de-DE/codex/permissions) Nutzende auswählen können. Für Berechtigungsprofile ist dies das Gegenstück
zu `allowed_sandbox_modes`. Verwende die Zulassungsliste, die dazu passt,
wie deine Nutzenden Berechtigungen auswählen.

Zulassungslisten für Berechtigungsprofile erfordern Codex 0.138.0 oder neuer. Codex 0.137.0 und
ältere Versionen ignorieren `allowed_permission_profiles` und die verwaltete Einstellung
`default_permissions`.

Verwende die folgenden Beispiele für Berechtigungsprofile erst, wenn auf allen verwalteten Clients eine
Version mit entsprechender Unterstützung läuft. Stelle verwaltete benutzerdefinierte Profile erst bereit, wenn das Upgrade
aller Clients abgeschlossen ist.

Wenn die Tabelle vorhanden ist, enthält sie die vollständige Liste der zulässigen Profile. Sie erlaubt
Profile mit dem Wert `true` und sperrt nicht aufgeführte oder auf `false` gesetzte Profile, einschließlich
integrierter Profile, die erst in zukünftigen Codex-Versionen hinzukommen.

#### Standardprofile zulassen

Diese Richtlinie erlaubt die Nutzung ohne Schreibzugriff und den Zugriff auf den Workspace, aber keinen Vollzugriff:

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

#### Einen verwalteten Standardwert mit minimalen Berechtigungen hinzufügen

Administrierende können in derselben Anforderungsquelle ein benutzerdefiniertes Profil definieren. Verwende
organisationsspezifische Profilnamen, die nicht mit Namen aus den geladenen Konfigurationen der Nutzenden
kollidieren. Benutzerdefinierte Namen dürfen weder mit `:` beginnen noch den reservierten Namen `filesystem`
verwenden.

Stelle verwaltete benutzerdefinierte Profile nicht auf Clients bereit, auf denen Codex 0.137.0 oder
eine ältere Version läuft. Diese Clients erkennen zwar die Profiltabelle, nicht aber den verwalteten Standardwert,
der dieses Profil auswählt.

Zum Beispiel:

```toml
default_permissions = "acme_review_only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
acme_review_only = true
# ":danger-full-access" is intentionally omitted, so it is denied.

[permissions.acme_review_only]
description = "Review code without modifying the workspace."
extends = ":read-only"

#### Nur vom Unternehmen definierte Profile zulassen

Lasse alle integrierten Profile weg, wenn Nutzende nur von der Administration definierte Profile auswählen sollen:

```toml
default_permissions = "acme_workspace"

[allowed_permission_profiles]
acme_workspace = true

[permissions.acme_workspace]
description = "Workspace access with sensitive files denied."
extends = ":workspace"

[permissions.acme_workspace.filesystem]
glob_scan_max_depth = 3

[permissions.acme_workspace.filesystem.":workspace_roots"]
"**/*.env" = "deny"

Das benutzerdefinierte Profil kann `:workspace` erweitern, obwohl Nutzende das
integrierte Profil `:workspace` nicht direkt auswählen können.

#### Ein von einer anderen Quelle zugelassenes Profil deaktivieren

Zulassungslisten für Berechtigungsprofile werden nach Profilnamen zusammengeführt. Da Cloud-Anforderungen
eine höhere Priorität als systemweite Anforderungen haben, können Cloud-Anforderungen mit `false`
ein durch die Systemdatei zugelassenes Profil deaktivieren.

Cloud-Anforderungen:

```toml
default_permissions = ":read-only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = false

Systemweite Anforderungen:

```toml
[allowed_permission_profiles]
":read-only" = true
":workspace" = true  # Not honored because cloud requirements set this to false.

Setze `default_permissions` explizit auf ein zulässiges Profil. Wenn der Wert fehlt,
verwendet die lokale Laufzeit standardmäßig nur dann `:workspace`, wenn sowohl `:workspace` als auch
`:read-only` explizit zugelassen sind. Wenn `allowed_permission_profiles`
fehlt, schränken verwaltete Anforderungen nicht ein, welche Profilnamen Nutzende
auswählen können. Jeder Eintrag muss ein integriertes Profil oder ein benutzerdefiniertes Profil benennen, das in
einer geladenen Konfiguration oder Anforderungsquelle definiert ist. Definiere benutzerdefinierte Profile in verwalteten
Anforderungen, um ihr Verhalten zentral zu steuern.

### Sandbox-Anforderungen je nach Host überschreiben

Verwende `[[remote_sandbox_config]]`, wenn eine verwaltete Richtlinie auf verschiedenen Hosts unterschiedliche
Sandbox-Anforderungen anwenden soll. Du kannst beispielsweise für Laptops einen strengeren
Standard beibehalten und auf passenden Entwicklungsrechnern oder CI-Runnern
Schreibzugriff auf den Workspace zulassen. Hostspezifische Einträge überschreiben derzeit nur `allowed_sandbox_modes`:

```toml
allowed_sandbox_modes = ["read-only"]

[[remote_sandbox_config]]
hostname_patterns = ["*.devbox.example.com", "runner-??.ci.example.com"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

Die lokale Laufzeit vergleicht jeden Eintrag in `hostname_patterns` mit dem
bestmöglich ermittelten Hostnamen. Wenn verfügbar, bevorzugt sie den vollqualifizierten Domainnamen
und greift andernfalls auf den lokalen Hostnamen zurück. Beim Abgleich wird nicht zwischen Groß- und Kleinschreibung unterschieden.
`*` entspricht einer beliebigen Zeichenfolge und `?` genau einem Zeichen.

Innerhalb derselben Anforderungsquelle gilt der erste passende Eintrag in `[[remote_sandbox_config]]`.
Stimmt kein Eintrag überein, behält die lokale Laufzeit den auf oberster Ebene festgelegten Wert für
`allowed_sandbox_modes` bei. Der Abgleich von Hostnamen dient ausschließlich der Auswahl einer Richtlinie. Betrachte ihn
nicht als authentifizierten Gerätenachweis.

Du kannst auch den Websuchmodus einschränken:

```toml
allowed_web_search_modes = ["cached"] # "disabled" remains implicitly allowed

`allowed_web_search_modes = []` lässt nur `"disabled"` zu.
`allowed_web_search_modes = ["cached"]` verhindert beispielsweise die Live-Websuche selbst in Sitzungen mit `danger-full-access`.

### Vorgaben für den Netzwerkzugriff konfigurieren

  `[experimental_network]` ist experimentell und kann sich ändern. Aktiviere diese
  Vorgaben nicht unternehmensweit, ohne sie zuvor mit den lokalen Client-Versionen und
  Betriebssystemen zu prüfen, die deine Nutzenden einsetzen. Windows
  wird bisher nur eingeschränkt unterstützt. Wende diese Richtlinie nur dann auf Windows-Nutzende an,
  wenn du sie in deiner Umgebung getestet hast.

Verwende `[experimental_network]` in `requirements.toml`, wenn Administrierende
Vorgaben für den Netzwerkzugriff zentral festlegen sollen. Diese Vorgaben sind
unabhängig vom Schalter `features.network_proxy` für Nutzende: Sie können den Netzwerkzugriff
der Sandbox ohne dieses Feature-Flag konfigurieren, gewähren Befehlen jedoch
keinen Netzwerkzugriff, wenn die aktive Sandbox diesen deaktiviert. Setze
`experimental_network.enabled = true`, um den verwalteten Proxy zu aktivieren.
Domainregeln allein aktivieren den Proxy nicht.

```toml
[experimental_network]
enabled = true
managed_allowed_domains_only = true

[experimental_network.domains]
"api.openai.com" = "allow"
"**.example.com" = "allow"
"blocked.example.com" = "deny"
"**.exfil.example.com" = "deny"

Verwende `experimental_network.managed_allowed_domains_only = true` nur, wenn du
auch administrativ verwaltete Einträge mit `"allow"` in
`[experimental_network.domains]` definierst und möchtest, dass ausschließlich diese Regeln gelten. Ist die Option
ohne verwaltete Zulassungsregeln auf `true` gesetzt, sind von Nutzenden hinzugefügte Domain-Zulassungsregeln
nicht mehr wirksam. Kombiniere die kanonische Map `domains` nicht mit den älteren
Listen `allowed_domains` oder `denied_domains`.

`*.example.com` erfasst nur Subdomains. `**.example.com` erfasst die Hauptdomain
und ihre Subdomains. Eine zutreffende Verweigerungsregel hat Vorrang vor einer Zulassungsregel.

Die Domain-Syntax, die Regeln für lokale und private Ziele, der Vorrang von Verweigerungs- vor Zulassungsregeln
und die Einschränkungen beim DNS-Rebinding entsprechen dem Verhalten des Sandbox-Netzwerks,
das unter [Agentenfreigaben und Sicherheit](/de-DE/codex/agent-approvals-security#network-isolation) beschrieben ist.

Der Proxy leitet den Netzwerkverkehr lokaler Befehle weiter, die innerhalb der Sandbox ausgeführt werden. Browsertools
prüfen vor dem Zugriff auf einen Origin ebenfalls verwaltete Netzwerksperren und exklusive Zulassungslisten.
Dabei handelt es sich um eine separate Richtlinienprüfung; der Browserdatenverkehr wird nicht durch
den Befehlsproxy geleitet. Der Proxy filtert weder Websuche, Apps und Konnektoren noch MCP-Server,
den Datenverkehr nativer Apps, Anfragen an Codex-Dienste oder den Datenverkehr von Codex Cloud.
Verwende für jeden Bereich die entsprechenden Steuerungsmöglichkeiten:

- Verwende `allowed_web_search_modes`, um die Websuche einzuschränken.
- Verwende `features.apps = false`, um Integrationen von Apps und Konnektoren zu deaktivieren, und
`features.plugins = false`, um Plug-ins zu deaktivieren, sofern dies unterstützt wird.
- Verwende die verwaltete Zulassungsliste `mcp_servers`, um MCP-Server einzuschränken.
- Verwende Funktionsvorgaben wie `browser_use`, `in_app_browser` und
`computer_use`, um Browserfunktionen und die Computernutzung einzuschränken.
- Konfiguriere den Netzwerkzugriff für Codex Cloud in den Einstellungen der zugehörigen Cloud-Umgebung.

Eine Domain-Zulassungsliste für Befehle ersetzt diese funktionsspezifischen
Steuerungsmöglichkeiten nicht.

### Browser und Computernutzung steuern

Verwende die Tabellen `[browser_use]` und `[computer_use]` in `requirements.toml`, um
unterstützte Desktop-Clients einzuschränken. Prüfe die Richtlinie mit den Client-Versionen
und Betriebssystemen, die du einsetzt. Eine konfigurierte Zulassungsregel
installiert kein Plug-in, erteilt keine Betriebssystemberechtigung und genehmigt keine Aktion,
die weiterhin überprüft werden muss.

Konfiguriere für den Browserzugriff eine Origin-Richtlinie. Ein Origin umfasst das Schema,
den Host und optional den Port, zum Beispiel `https://example.com` oder
`https://*.example.com:8443`. Gib keinen Pfad, keine Abfrage und kein Fragment an.
Anders als Domainregeln für den Netzwerkzugriff von Befehlen unterscheiden Origin-Regeln für Browser zwischen HTTP und HTTPS
und gleichen den Port ab.

Dieses Beispiel beschränkt den Browserzugriff auf eine zugelassene Website und verhindert dort Uploads
sowie den vollständigen Zugriff über das Chrome DevTools Protocol (CDP):

```toml
[browser_use]
allow_history_access = false
allow_global_persistent_approval = false

[browser_use.default_origin_policy]
access = "deny"

[browser_use.origins."https://example.com"]
access = "allow"
uploads = "deny"
downloads = "allow"
full_cdp_access = "deny"
persistent_approval = false
access_approval_lifetime = "turn"

Zutreffende Origin-Regeln werden für jedes Feld einzeln ausgewertet. Eine zutreffende Verweigerung hat Vorrang.
Für Felder, die in den zutreffenden Regeln nicht festgelegt sind, gilt ansonsten die Standardrichtlinie für Origins.
Die lokale Konfiguration kann zusätzliche Einschränkungen festlegen, aber keine verwaltete Verweigerung lockern.
Netzwerksperren und exklusive verwaltete Netzwerk-Zulassungslisten gelten weiterhin.

Setze `browser_use.disable_auto_review = true`, um die automatische Überprüfung von Genehmigungen
für Browseraktionen zu deaktivieren, oder setze `auto_review = "deny"` in einer Origin-Richtlinie,
um sie für diesen Origin einzuschränken. Dies steuert die Handhabung von Genehmigungen;
die Sicherheitsüberwachung des Modells wird dadurch nicht deaktiviert.

Lege für native Apps eine Standardrichtlinie für den Zugriff fest und gib die zulässigen Apps an.
Diese macOS-Richtlinie erlaubt beispielsweise die App „Rechner“ und verhindert das Speichern von Genehmigungen:

```toml
[computer_use]
default_app_access = "deny"
allow_persistent_approval = false

[computer_use.macos.bundle_ids]
"com.apple.calculator" = "allow"

Windows-Richtlinien können paketierte Apps anhand von
`computer_use.windows.aumids` oder ausführbare Dateien anhand von
`computer_use.windows.exes` identifizieren. Regeln für ausführbare Dateien erfordern `publisher_name`,
`product_name` und `access`; `binary_name` ist optional. Verwende die verifizierte Identität der App
und nicht nur ihren Anzeigenamen.

Alle Felder findest du in der [Konfigurationsreferenz](/de-DE/codex/config-file/config-reference#requirementstoml).
Beachte außerdem die [Einschränkungen für die Nutzung im gesperrten Zustand](#restrict-locked-computer-use)
auf verwalteten macOS-Geräten.

### Feature-Flags fest vorgeben

Du kannst auch [Feature-Flags](/de-DE/codex/config-file/config-basic/#feature-flags) für Nutzende fest vorgeben,
die eine verwaltete Datei `requirements.toml` erhalten:

```toml
[features]
personality = true
unified_exec = false

# Disable surface-specific features when needed.
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
in_app_updates = false
computer_use = false

Verwende für Laufzeitfunktionen die kanonischen Funktionsschlüssel aus `config.toml`,
die in der Tabelle `[features]` stehen. Die lokale Laufzeitumgebung normalisiert erkannte Funktionen gemäß diesen
Vorgaben und lehnt widersprüchliche Änderungen an `config.toml` oder an den Funktionseinstellungen
in Profildateien ab.

<a id="disable-codex-feature-surfaces"></a>

- `in_app_browser = false` deaktiviert den integrierten Browserbereich.
- `in_app_updates = false` deaktiviert die eigene Updatefunktion der ChatGPT-Desktop-App beim
  Neustart, sofern dies unterstützt wird. Die Einstellung wirkt sich nicht auf externe Paketbereitstellungen aus und
  verlängert auch nicht die Unterstützung älterer App-Versionen. Hinweise zu Setup und Rollout findest du unter
[App-Updates verwalten](/de-DE/codex/enterprise/manage-app-updates).
- `browser_use = false` deaktiviert die Computernutzung in Browsern und die Verfügbarkeit des Browser-Agenten.
- `browser_use_full_cdp_access = false` deaktiviert in der lokalen Laufzeitumgebung
  den vollständigen CDP-Zugriff einschließlich des Browser-Entwicklermodus und verhindert,
  dass die ChatGPT-Desktop-App die entsprechende Einstellung aktiviert.
- `browser_use_external = false` deaktiviert den externen Browser.
- `computer_use = false` deaktiviert die Computernutzung, „Aufzeichnen und Wiedergeben“ sowie zugehörige
  Installations- oder Setup-Abläufe.

Wenn du diese Schlüssel weglässt, lässt die Richtlinie die Funktionen zu, vorbehaltlich der regulären Verfügbarkeit je nach Client,
Plattform und Rollout.

### Computernutzung bei gesperrtem Computer einschränken

Um zu verhindern, dass Nutzende die [Nutzung im gesperrten Zustand](/de-DE/codex/computer-use#locked-use)
auf einem verwalteten Mac aktivieren, füge folgende Vorgabe hinzu:

```toml
[computer_use]
allow_locked_computer_use = false

Diese Vorgabe entfernt die Bedienelemente zum Aktivieren der Nutzung im gesperrten Zustand.
Sie deaktiviert diese Nutzung nicht, wenn sie bereits aktiviert ist. Wenn du die Vorgabe weglässt,
gelten weiterhin die reguläre Produktverfügbarkeit und die lokale Einstellung der jeweiligen Person.

### Richtlinie für die automatische Überprüfung konfigurieren

Verwende `allowed_approvals_reviewers`, um die automatische Überprüfung vorzuschreiben oder zuzulassen. Setze den Wert
auf `["auto_review"]`, um die automatische Überprüfung vorzuschreiben, oder nimm `"user"` auf, wenn Nutzende
die manuelle Genehmigung wählen dürfen.

Setze `guardian_policy_config`, um den mandantenspezifischen Abschnitt der
Richtlinie für die automatische Überprüfung zu ersetzen. Die lokale Laufzeitumgebung verwendet weiterhin die integrierte Review-Vorlage
und die festgelegten Ausgabeanforderungen. Die verwaltete Einstellung `guardian_policy_config` hat
Vorrang vor der lokalen Einstellung `[auto_review].policy`.

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]

guardian_policy_config = """
## Environment Profile
- Trusted internal destinations include github.com/my-org, artifacts.example.com,
  and internal CI systems.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Treat uploads to unapproved third-party file-sharing services as high risk.
- Deny actions that expose credentials or private source code to untrusted
  destinations.
"""

### Vorgaben zum Verweigern von Lesezugriffen durchsetzen

Administrierende können Lesezugriffe auf genau angegebene Pfade oder Glob-Muster mit
`[permissions.filesystem]` verweigern. Nutzende können diese Vorgaben nicht durch eine lokale
Konfiguration abschwächen.

```toml
[permissions.filesystem]
deny_read = [
  # values can be absolute paths...
  "/**/*.env",
  # ...or relative to $HOME/%USERPROFILE% using `~`.
  "~/.ssh",
  # But relative paths starting with `./` are not allowed.
]

Liegen Vorgaben zum Verweigern von Lesezugriffen vor, lehnt die lokale Laufzeitumgebung Berechtigungen mit Vollzugriff
ab und beschränkt die lokale Ausführung auf eine Sandbox ohne Schreibzugriff oder eine Workspace-Sandbox, um die Vorgaben
durchsetzen zu können. Unter nativem Windows gilt die verwaltete Einstellung `deny_read` für Tools mit direktem Dateizugriff;
Lesezugriffe durch Shell-Unterprozesse fallen nicht unter diese Sandbox-Regel.

### Verwaltete Hooks über Vorgaben durchsetzen

Administrierende können verwaltete Lebenszyklus-Hooks auch direkt in `requirements.toml` definieren.
Verwende `[hooks]` für die Hook-Konfiguration selbst und lege mit `managed_dir` das Verzeichnis fest,
in dem deine MDM- oder Endpunktverwaltungslösung
die referenzierten Skripte installiert.

Um verwaltete Hooks auch für Nutzende durchzusetzen, die Hooks lokal deaktiviert haben, lege
`[features].hooks = true` zusammen mit `[hooks]` fest. Um Hooks von Nutzenden, Projekten, Sitzungen
und Plug-ins zu überspringen und verwaltete Hooks weiterhin zuzulassen, setze
`allow_managed_hooks_only = true`.

```toml
allow_managed_hooks_only = true

[features]
hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
command_windows = 'py -3 C:\enterprise\hooks\pre_tool_use_policy.py'
timeout = 30
statusMessage = "Checking managed Bash command"

Hinweise:

- Die lokale Laufzeitumgebung setzt die Hook-Konfiguration aus `requirements.toml` durch,
  verteilt aber die Skripte in `managed_dir` nicht.
- Verteile diese Skripte mit deiner MDM- oder Geräteverwaltungslösung.
- Befehle für verwaltete Hooks sollten auf absolute Skriptpfade unterhalb des
konfigurierten verwalteten Verzeichnisses verweisen.
- `allow_managed_hooks_only = true` überspringt Hooks von Nutzenden, Projekten, Sitzungen und
  Plug-ins, lädt aber weiterhin Hooks aus `requirements.toml` und anderen
  verwalteten Konfigurationsebenen.

### Befehlsregeln über Vorgaben durchsetzen

Administrierende können in `requirements.toml`
über eine Tabelle `[rules]` auch restriktive Befehlsregeln durchsetzen. Diese Regeln werden mit regulären Dateien des Typs `.rules` zusammengeführt;
nach wie vor setzt sich die restriktivste Entscheidung durch.

Anders als bei `.rules` müssen Regeln in den Vorgaben `decision` angeben; diese Entscheidung
muss `"prompt"` oder `"forbidden"` lauten (nicht `"allow"`).

```toml
[rules]
prefix_rules = [
  { pattern = [{ token = "rm" }], decision = "forbidden", justification = "Use git clean -fd instead." },
  { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating history." },
]

Um einzuschränken, welche MCP-Server ein lokaler Client aktivieren kann, füge unter `mcp_servers`
eine Zulassungsliste hinzu. Bei stdio-Servern erfolgt der Abgleich über `command`,
bei Servern mit Streamable HTTP über `url`:

```toml
[mcp_servers.docs]
identity = { command = "codex-mcp" }

[mcp_servers.remote]
identity = { url = "https://example.com/mcp" }

Die Zeichenkettenform von `identity.command` gleicht nur den konfigurierten Wert von `command` ab.
Sie prüft weder `args`, `cwd`, `env` noch `env_vars`.

Um einen vollständigen stdio-Aufruf einzuschränken, gleiche die ausführbare Datei und jedes
Positionsargument ab:

```toml
[mcp_servers.internal.identity]
command = { executable = "/usr/local/bin/codex-mcp", args = [
  { match = "exact", value = "serve" },
  { match = "prefix", value = "--workspace=" },
] }

Die ausführbare Datei, die Anzahl der Argumente und ihre Reihenfolge müssen übereinstimmen.
Regeln für Argumente und URLs unterstützen die Abgleichsarten `exact` und `prefix` sowie einen Abgleich des vollständigen Werts mit `regex`.
Strukturierte Befehlsregeln prüfen weiterhin weder `cwd`, `env` noch `env_vars`.
In Plug-ins enthaltene MCP-Server verwenden dieselben Identitätsstrukturen unter
`plugins.<plugin>.mcp_servers.<server>`.

Ist `mcp_servers` vorhanden, aber leer, deaktiviert der lokale Client alle MCP-Server.

### Verfügbarkeit von Plug-ins steuern

Um Plug-ins in unterstützten lokalen Clients zu deaktivieren, setze `features.plugins` in `requirements.toml`
auf `false`:

```toml
features.plugins = false

Diese Einstellung gilt auch, wenn sich Nutzende mit einem API-Schlüssel bei Codex anmelden.
Der [Eintrag zu `features.plugins`
in der Referenz](/de-DE/codex/config-file/config-reference#requirementstoml) beschreibt
die unterstützte Konfiguration.

### Marketplace-Quellen für Plug-ins einschränken

Um Vorgänge mit von Nutzenden konfigurierten Marketplace-Quellen einzuschränken, setze
`restrict_to_allowed_sources = true` und definiere mindestens eine Quellenregel:

```toml
[marketplaces]
restrict_to_allowed_sources = true

[marketplaces.allowed_sources.company_plugins]
source = "git"
url = "https://github.com/example/company-plugins.git"
ref = "main"

[marketplaces.allowed_sources.internal_git]
source = "host_pattern"
host_pattern = '^git\.example\.com$'

[marketplaces.allowed_sources.local_plugins]
source = "local"
path = "/opt/company/codex-plugins"

Git-Regeln gleichen die normalisierte Repository-URL und, sofern vorhanden, den exakten Wert von
`ref` ab. Host-Muster sind reguläre Ausdrücke, die mit dem kleingeschriebenen Git-Host
abgeglichen werden. Verwende `^` und `$`, um den gesamten Host abzugleichen. Lokale Regeln erfordern
einen absoluten, normalisierten Pfad. Die [Referenz zu `requirements.toml`](/de-DE/codex/config-file/config-reference#requirementstoml)
enthält das vollständige Schema und beschreibt das Verhalten beim Zusammenführen.

Diese Vorgaben lehnen bei von Nutzenden konfigurierten Quellen Vorgänge ab, die keiner Regel entsprechen: das Hinzufügen eines Marketplaces, die Installation eines Plug-ins und
die Aktualisierung konfigurierter Git-Marketplaces.
Von Codex verwaltete OpenAI-Marketplaces bleiben verfügbar, wenn ihre Quelle und ihr
reservierter Name übereinstimmen. Die Vorgaben filtern zur Laufzeit weder bereits konfigurierte
Marketplaces von Nutzenden noch deren Plug-ins.

Diese Einschränkungen für Quellen gelten nur dort, wo ein lokaler Client Vorgänge für Plug-in-Marketplaces unterstützt: bei ChatGPT und Codex in der Desktop-App sowie bei Codex CLI.
Sie steuern weder die Nutzung von Plug-ins in ChatGPT im Web noch auf Mobilgeräten und fügen der IDE-Erweiterung keine Plug-ins hinzu.

## Verwaltete Standardwerte (`managed_config.toml`)

Verwaltete Standardwerte legen fest, mit welcher Konfiguration ein unterstützter lokaler Client startet. Beim
Start überschreiben sie die lokale Datei `config.toml` der Nutzenden sowie alle per CLI mit `--config`
angegebenen Werte. Nutzende können diese Einstellungen während des aktuellen Durchlaufs weiterhin ändern.
Beim nächsten Start des Clients gelten wieder die Standardwerte.

Wenn ein verwalteter Standardwert, ein macOS-MDM-Profil oder eine gespeicherte Konfiguration `gpt-5.4`
oder `gpt-5.4-mini` für Personen fest vorgibt, die mit ChatGPT angemeldet sind, aktualisiere die entsprechende Vorgabe vor dem 31. August 2026. Ersetze `gpt-5.4` durch `gpt-5.6-terra` und `gpt-5.4-mini` durch
`gpt-5.6-luna`. Die OpenAI API und Codex mit Authentifizierung über deinen eigenen API-Schlüssel
sind nicht betroffen. Siehe [Modellverfügbarkeit im
Workspace](/de-DE/codex/enterprise/workspace-model-availability#prepare-for-the-gpt-54-retirement).

Stelle sicher, dass deine verwalteten Standardwerte deinen Anforderungen entsprechen. Die lokale Laufzeitumgebung
weist unzulässige Werte zurück.

### Priorität und Ebenen

Die lokale Laufzeitumgebung setzt die wirksame Konfiguration in dieser Reihenfolge zusammen (obere Ebenen
überschreiben untere):

- Verwaltete Einstellungen (macOS MDM; höchste Priorität)
- `managed_config.toml` (Systemdatei/verwaltete Datei)
- `config.toml` (Basiskonfiguration der Nutzenden)

CLI-Überschreibungen mit `--config key=value` gelten für die Basiskonfiguration, werden jedoch von verwalteten Ebenen überschrieben. Dadurch startet jeder Durchlauf mit den verwalteten Standardwerten, selbst wenn du lokale Flags angibst.

Über die Cloud verwaltete Anforderungen betreffen die Anforderungsebene, nicht die verwalteten Standardwerte. Informationen zur Prioritätsreihenfolge findest du oben im Abschnitt über administrativ durchgesetzte Anforderungen.

### Speicherorte

- Linux/macOS (Unix): `/etc/codex/managed_config.toml`
- Windows/Nicht-Unix: `~/.codex/managed_config.toml`

Fehlt die Datei, überspringt die lokale Laufzeitumgebung die verwaltete Ebene.

### Verwaltete macOS-Einstellungen (MDM)

Unter macOS können Admins ein Geräteprofil verteilen, das base64-kodierte TOML-Payloads an folgenden Stellen bereitstellt:

- Einstellungsdomäne: `com.openai.codex`
- Schlüssel:
  - `config_toml_base64` (verwaltete Standardwerte)
  - `requirements_toml_base64` (Anforderungen)

Die lokale Laufzeitumgebung liest diese Payloads für „verwaltete Einstellungen“ als TOML ein. Für
verwaltete Standardwerte (`config_toml_base64`) haben verwaltete Einstellungen die höchste
Priorität. Für Anforderungen (`requirements_toml_base64`) gilt
die oben beschriebene Prioritätsreihenfolge für über die Cloud verwaltete Anforderungen. Dieselbe
Tabelle `[features]` für Anforderungen funktioniert auch in `requirements_toml_base64`. Verwende
auch dort die kanonischen Feature-Schlüssel.

### Ablauf für das MDM-Setup

Die lokale Laufzeitumgebung unterstützt standardmäßige macOS-MDM-Payloads, sodass du
Einstellungen mit Tools wie `Jamf Pro`, `Fleet` oder `Kandji` verteilen kannst. Eine einfache
Bereitstellung läuft so ab:

1. Erstelle die verwaltete TOML-Payload und kodiere sie mit `base64` (ohne Zeilenumbrüche).
2. Trage die Zeichenfolge in deinem MDM-Profil in der Domäne `com.openai.codex` unter `config_toml_base64` (verwaltete Standardwerte) oder `requirements_toml_base64` (Anforderungen) ein.
3. Verteile das Profil. Bitte die Nutzenden anschließend, den unterstützten lokalen Client neu zu starten und
zu bestätigen, dass die Konfigurationsübersicht beim Start die verwalteten Werte anzeigt.
4. Wenn du eine Richtlinie widerrufst oder änderst, aktualisiere die verwaltete Payload. Der Client
liest die aktualisierte Einstellung beim nächsten Start ein.

Nimm keine geheimen Daten oder dynamischen Werte, die sich häufig ändern, in die Payload auf. Behandle die verwaltete TOML-Konfiguration wie jede andere MDM-Einstellung im Rahmen der Änderungskontrolle.

### Beispiel für managed\_config.toml

```toml
# Set conservative defaults
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

[sandbox_workspace_write]
network_access = false             # keep network disabled unless explicitly allowed

[otel]
environment = "prod"
exporter = "otlp-http"            # point at your collector
log_user_prompt = false            # keep prompts redacted
# exporter details live under exporter tables; see Monitoring and telemetry above

### Empfohlene Schutzmaßnahmen

- Bevorzuge für die meisten Nutzenden `workspace-write` mit Genehmigungen. Gewähre Vollzugriff nur in kontrollierten Containern.
- Behalte `network_access = false` bei, es sei denn, dein Sicherheits-Review lässt einen Collector oder die für deine Arbeitsabläufe erforderlichen Domains zu.
- Verwende die verwaltete Konfiguration, um OTel-Einstellungen (Exporter, Umgebung) fest vorzugeben. Behalte `log_user_prompt = false` jedoch bei, es sei denn, deine Richtlinie erlaubt ausdrücklich das Speichern von Prompt-Inhalten.
- Prüfe regelmäßig die Unterschiede zwischen der lokalen Datei `config.toml` und der verwalteten Richtlinie, um Konfigurationsabweichungen zu erkennen. Verwaltete Ebenen sollten Vorrang vor lokalen Flags und Dateien haben.

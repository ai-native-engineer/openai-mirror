<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/workload-identity -->

Die Föderation von Workload-Identitäten ermöglicht vertrauenswürdigen Automatisierungen die Nutzung von Codex, ohne ein persönliches Zugriffstoken oder andere langlebige OpenAI-Zugangsdaten zu speichern. Dein Workload legt ein kurzlebiges Identitätstoken eines bereits von dir betriebenen Anbieters vor. OpenAI überprüft dieses Token und stellt ein kurzlebiges Zugriffstoken für ein Nutzerkonto oder Dienstkonto in deinem verwalteten ChatGPT-Workspace aus.

Nutze Workload-Identitäten für unbeaufsichtigte Codex-Prozesse auf Cloud-Plattformen,
in Kubernetes, CI-Systemen und anderen Umgebungen, die OIDC-Token oder
SPIFFE JWT-SVIDs ausstellen können. Informationen zum gemeinsamen Vertrauensmodell und zum separaten Ablauf für die OpenAI API
findest du in der [Übersicht zu Workload-Identitäten](/api/docs/guides/workload-identity-federation).

  Die Föderation von Workload-Identitäten für Codex befindet sich in der Betaphase und muss für deinen
  Workspace aktiviert werden. Um Zugriff zu beantragen, wende dich an deine Ansprechperson bei OpenAI oder den [OpenAI
  Support](https://help.openai.com/en/articles/6614161-how-can-i-contact-support).

## Bevor du beginnst

Du benötigst:

- Die Berechtigung, Workload-Identitäten im OpenAI Admin Portal zu verwalten.
- Einen verwalteten ChatGPT-Workspace.
- Ein ChatGPT-Nutzerkonto oder Dienstkonto, das aktives Mitglied dieses Workspaces ist, oder die Berechtigung, beim Setup ein solches Konto zu erstellen.
- Ein OIDC-Token oder SPIFFE JWT-SVID, bei dem du Aussteller, Audience und identifizierende Claims kennst.
- Eine Laufzeitumgebung, die dieses Token in einer geschützten Datei unter einem absoluten Pfad aktuell hält.
- Codex 0.148.0 oder höher.
- Eine geltende Codex-Authentifizierungsrichtlinie, die die ChatGPT-Authentifizierung
  und den durch die Föderationsregel ausgewählten Workspace zulässt. Siehe [Anmeldemethode oder
  Workspace erzwingen](/de-DE/codex/auth#enforce-a-login-method-or-workspace).

Während des Tokenaustauschs erstellt OpenAI weder einen Principal noch eine Workspace-Mitgliedschaft. Eine Person mit Administrationsrechten wählt den Principal aus oder erstellt ihn, bevor sich der Workload verbindet. Das Erstellen eines persönlichen Nutzerkontos belegt einen Platz im Workspace und unterliegt dessen Mitgliedschaftsregeln.

Unter nativem Windows musst du die **mit erhöhten Rechten ausgeführte**
[Windows-Sandbox](/de-DE/codex/windows/windows-sandbox) verwenden. Andere Windows-Sandbox-Modi
können die Datei mit dem Identitätstoken nicht vor modellgesteuerten Befehlen schützen.

## Identitätstoken abrufen

Die Laufzeitumgebung deines Workloads ruft das vorgelagerte Identitätstoken ab und erneuert es. Codex ruft weder Cloud-Metadatendienste noch Clientbibliotheken von Identitätsanbietern in deinem Namen auf.

| Laufzeitumgebung                          | Empfohlene Quelle für die Tokendatei                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Kubernetes, AKS, EKS oder GKE     | Binde ein projiziertes Dienstkonto-Token ein und verweise Codex auf diese Datei. Die Plattform erneuert das Token.                                  |
| Verwaltete Identität von Microsoft Entra | Führe einen vertrauenswürdigen Host-Prozess oder Sidecar aus, der bei Azure IMDS ein Token anfordert und die Datei vor dessen Ablauf ersetzt.                |
| Ausgehende AWS-Identitätsföderation | Führe einen vertrauenswürdigen Host-Prozess aus, der `GetWebIdentityToken` beim regionalen STS aufruft und die Datei vor Ablauf der Gültigkeit ersetzt.                   |
| Google Cloud                     | Führe einen vertrauenswürdigen Host-Prozess aus, der beim Metadatenserver ein Identitätstoken anfordert und die Datei vor dessen Ablauf ersetzt.        |
| Oracle Cloud Infrastructure      | Führe einen vertrauenswürdigen Host-Prozess aus, der über einen Instanz-Principal ein IDCS-Zugriffstoken anfordert und die Datei vor dessen Ablauf ersetzt. |
| GitHub Actions                   | Fordere das OIDC-Token des Jobs an, schreibe es in eine geschützte Datei und fordere vor einem späteren Tokenaustausch ein neues Token an.                    |
| SPIFFE                           | Nutze die SPIFFE Workload API oder ein genehmigtes Hilfsprogramm, um ein aktuelles JWT-SVID in die Datei zu schreiben.                                      |
| Benutzerdefinierter OIDC-Anbieter             | Nutze den Workload-Ablauf des Ausstellers, um ein JWT abzurufen, und aktualisiere die geschützte Datei, bevor das JWT abläuft.                            |

Befolge die Anleitung deines Anbieters, um die Tokenausgabe zu konfigurieren und ein Beispieltoken zu prüfen:

- [Microsoft Azure](/api/docs/guides/workload-identity-federation/microsoft-azure)
- [AWS](/api/docs/guides/workload-identity-federation/aws)
- [Google Cloud](/api/docs/guides/workload-identity-federation/google-cloud)
- [Oracle Cloud Infrastructure](/api/docs/guides/workload-identity-federation/oracle-cloud)
- [GitHub Actions](/api/docs/guides/workload-identity-federation/github-actions)
- [Kubernetes](/api/docs/guides/workload-identity-federation/kubernetes)
- [SPIFFE](/api/docs/guides/workload-identity-federation/spiffe)

Dekodiere ein Beispieltoken lokal und notiere seine Werte für `iss`, `aud`, `sub` sowie alle weiteren
Claims, denen du vertrauen möchtest. Beim Dekodieren wird die Signatur nicht überprüft. Füge niemals ein
Token aus der Produktionsumgebung auf einer Website ein und schreibe es nicht in Logs.

## Workload verbinden

Eine Person mit Administrationsrechten erstellt den Anbieter und die Föderationsregel, bevor sie Codex startet.

1. Öffne [Workload-Identität](https://admin.openai.com/workload-identity) im
   OpenAI Admin Portal und wähle anschließend **Workload verbinden**.
2. Verwende einen bereits für Codex konfigurierten Anbieter oder erstelle einen neuen. Anbietervorlagen ergänzen die üblichen Einstellungen für GitHub Actions, Microsoft Entra ID, Google Cloud, AWS, Kubernetes, SPIFFE und benutzerdefinierte OIDC-Anbieter.
3. Wähle **Codex** und den verwalteten Workspace aus, den der Workload verwenden darf.
4. Füge möglichst eng gefasste Bedingungen hinzu, die den Workload identifizieren. Gleiche ein Subject, exakte Claims, eine CEL-Bedingung oder eine Kombination daraus ab. Füge akzeptierte Audiences hinzu, um einzuschränken, welche Token die Regel akzeptiert. Alle konfigurierten Matcher müssen zutreffen.
5. Ordne die Regel einem vorhandenen ChatGPT-Nutzerkonto oder Dienstkonto zu oder erstelle beim Setup ein entsprechendes Konto.
6. Überprüfe den Anbieter, die Bedingungen, den Workspace, den Principal, die Scopes und die Gültigkeitsdauer des
   Zugriffstokens. Wähle zuerst **Workload verbinden** und anschließend **Konfiguration herunterladen**.

Die heruntergeladene Datei enthält eine nicht geheime ID der Föderationsregel und den Pfad, aus dem Codex das Identitätstoken liest. Sie enthält keine Zugangsdaten.

Nutze die [Admin
API für Workload-Identitäten](/api/docs/guides/workload-identity-federation/admin-api), um das Setup zu automatisieren. Informationen zum Matcher-Verhalten
und Beispiele findest du in der [Referenz zu
Föderationsregeln](/api/docs/guides/workload-identity-federation/federation-rules).

## Codex-Prozess konfigurieren

Der Prozess, der Codex startet, benötigt diese beiden Variablen für die Workload-Identität:

```bash

`OPENAI_FEDERATION_RULE_ID` ist kein Geheimnis. Die Tokendatei dagegen schon. Verwende einen absoluten
Pfad in einem separaten Verzeichnis, etwa `/var/run/secrets/openai.com`. Dieses Verzeichnis muss dem
Workload-Konto gehören und den Modus `0700` haben. Nur vertrauenswürdige Host-Prozesse dürfen dort
Dateien schreiben. Das Verzeichnis darf sich weder in Repositorys noch in anderen für
Codex-Tools zugänglichen Pfaden befinden. Halte Zugangsdaten von Logs, dem Shell-Verlauf und Build-Artefakten fern.

### Audit-Zuordnung hinzufügen

Wenn mehrere Laufzeitinstanzen dieselbe Föderationsregel verwenden, kannst du jede Instanz
in Audit-Ereignissen zur Tokenausgabe identifizieren. Setze die optionale
Variable `OPENAI_WORKLOAD_IDENTITY_CONTEXT` auf ein als Zeichenkette
kodiertes JSON-Objekt:

```bash

  "instance_id": "runner-42",
  "display_name": "payments-prod",
  "labels": {
    "environment": "production",
    "region": "us-west-2"
  }
}'

Das Objekt erfordert `instance_id`. Es kann außerdem `display_name` und bis zu
acht Labels enthalten. Das kodierte Objekt darf höchstens 1.024 Byte groß sein. `instance_id` und
`display_name` dürfen jeweils bis zu 128 Zeichen lang sein. Label-Schlüssel dürfen höchstens 64
Zeichen und Label-Werte höchstens 256 Zeichen lang sein.

Kennungen müssen mit einem ASCII-Buchstaben oder einer Ziffer beginnen. Danach dürfen Werte
Buchstaben, Ziffern, `.`, `_`, `:`, `/`, `@` und `-` enthalten. Label-Schlüssel unterstützen Buchstaben,
Ziffern, `.`, `_` und `-`.

OpenAI behandelt diesen Kontext als vom Client gemeldete Audit-Zuordnung und nicht als überprüfte Workload-Identität. Er hat keinen Einfluss auf Authentifizierung, Autorisierung, Regelabgleich, Scopes, Ratenlimits, Widerrufe, Feature-Gates oder Metriken. Hinterlege darin keine Zugangsdaten, Geheimnisse, personenbezogenen Daten, Prompts, Modellausgaben oder sonstige Kundeninhalte.

Bei gültigem Kontext leitet OpenAI eine stabile Zuordnungs-ID ab, deren Geltungsbereich auf den Mandanten,
den Anbieter, die Föderationsregel und `instance_id` begrenzt ist. Zur Zuordnung enthält das Zugriffstoken
die ID, nicht jedoch den Kontext. Das Audit-Ereignis zur erfolgreichen Token-Ausstellung
enthält die ID und den normalisierten Kontext. Überschreitet der Kontext einen Grenzwert oder
verstößt er gegen dieses Schema, schlägt der Austausch mit `invalid_grant` fehl.

Codex liest den Kontext beim Start des Prozesses und gibt weder ihn noch die Regel-ID oder den Pfad zur Token-Datei an modellgesteuerte Shells, Hooks oder MCP-Server weiter. Starte Codex nach einer Änderung des Kontexts neu.

### Token-Datei schützen und regelmäßig austauschen

Trage bei verwalteten Bereitstellungen unter Linux, macOS und WSL das gesamte Token-Verzeichnis
in den verwalteten Vorgaben unter [`permissions.filesystem.deny_read`](/de-DE/codex/enterprise/managed-configuration#enforce-deny-read-requirements)
ein:

```toml
[permissions.filesystem]
deny_read = ["/var/run/secrets/openai.com"]

Dadurch wird verhindert, dass modellgesteuerte Befehle das aktive Token oder dessen vorübergehenden Ersatz lesen, während der Codex-Hostprozess das Token weiterhin für den Austausch verwenden kann. Sperre bei Volumes für projizierte Token den gesamten Token-Mount sowie sämtliche zugrunde liegenden oder aufgelösten Zielpfade außerhalb dieses Mounts. Dateiberechtigungen und das Bereinigen von Umgebungsvariablen allein schützen Zugangsdaten nicht vor einem anderen Prozess, der unter demselben Benutzerkonto ausgeführt wird. Verwende unter nativem Windows die oben beschriebene Sandbox mit erhöhten Rechten.

Bei Token-Quellen, die keine Datei projizieren, muss ein vertrauenswürdiger Hostprozess jede Ersatzdatei in diesem geschützten Verzeichnis schreiben und anschließend auf den vorgesehenen Dateinamen umbenennen. Eine atomare Umbenennung verhindert, dass Codex ein unvollständiges Token liest. Passe beispielsweise dieses hostseitige Aktualisierungsskript an den Token-Befehl deines Anbieters an. Richte das Verzeichnis ein, bevor du das Skript ausführst:

```bash
set -eu
TOKEN_DIR="/var/run/secrets/openai.com"
TOKEN_FILE="$TOKEN_DIR/identity-token"
umask 077
TOKEN_TEMP="$(mktemp "$TOKEN_DIR/.identity-token.XXXXXX")"
trap 'rm -f -- "$TOKEN_TEMP"' EXIT
trap 'exit 1' HUP INT TERM
your-identity-provider-command > "$TOKEN_TEMP"
test -s "$TOKEN_TEMP"
mv -f -- "$TOKEN_TEMP" "$TOKEN_FILE"

Führe den Aktualisierungsprozess außerhalb aller Shells und Tools aus, die Codex steuern kann.
Lass die Lesesperre während der Aktualisierung und Bereinigung aktiv. Bleibt nach einem
erzwungenen Abbruch eine temporäre Datei zurück, muss sie innerhalb des gesperrten
Verzeichnisses bleiben. Hinterlege keine Einstellungen für die Workload-Identität in `config.toml`.

## Verbindung überprüfen

Lade die heruntergeladene Umgebung und überprüfe die ausgewählte Authentifizierungsmethode:

```bash
. ./workload-identity-idpm_example.env
codex login status

In PowerShell:

```powershell
$env:OPENAI_FEDERATION_RULE_ID = "idpm_..."
$env:OPENAI_IDENTITY_TOKEN_FILE = "C:\run\openai\identity-token"
codex login status

Bei erfolgreicher Prüfung wird `Logged in using workload identity` ausgegeben. Damit wird bestätigt,
dass Codex über die konfigurierte Föderationsregel ein Token ausgetauscht hat. Der Befehl
gibt weder den ermittelten Workspace noch den Prinzipal oder die Regel aus. Überprüfe diese Angaben
im Admin Portal, bevor du den Workload startest. Meldet Codex eine andere
Authentifizierungsmethode, wurden die beiden erforderlichen WIF-Variablen nicht an den Prozess übergeben.

Wenn der Anbieter **Wiederholung von Assertions verhindern** verwendet und die Assertion den Claim `jti`
enthält, verbraucht diese Prüfung den betreffenden `jti`-Wert. Schreibe eine neu ausgestellte Assertion mit einem neuen
`jti`-Wert, bevor du einen weiteren Codex-Prozess startest.

Sende aus derselben Umgebung eine kurze Anfrage:

```bash
codex exec "Reply with only: workload identity is working"

Codex tauscht das vorgelagerte Token aus und hält das OpenAI-Zugriffstoken im Arbeitsspeicher.
Es schreibt keines der beiden Token in `auth.json`, den Systemschlüsselbund oder
`config.toml`.

## Token aktuell halten

Aktualisiere die Datei mit dem Identitätstoken, bevor das vorgelagerte Token abläuft. Codex liest die Datei erneut, sobald es ein weiteres OpenAI-Zugriffstoken benötigt. Das OpenAI-Token läuft ab, sobald entweder das vorgelagerte Token abläuft oder die durch die Föderationsregel festgelegte Gültigkeitsdauer endet, je nachdem, was zuerst eintritt. Es ist nie länger als eine Stunde gültig.

Wenn eine Person mit Administrationsrechten den Replay-Schutz aktiviert, muss jedes vorgelagerte JWT einen
eindeutigen `jti`-Wert enthalten. Schreibe vor jedem Austausch eine neu ausgestellte Assertion mit einem neuen `jti`-Wert,
auch bei Aktualisierungen in einem länger laufenden Prozess. Assertions ohne
`jti` haben keinen Replay-Schutz.

Codex verwendet innerhalb jedes Hostprozesses eine gemeinsame Austauschsitzung im Arbeitsspeicher. Gleichzeitige Anfragen in diesem Prozess nutzen ein gültiges OpenAI-Zugriffstoken gemeinsam und teilen sich nach dessen Ablauf einen einzigen Aktualisierungsvorgang. Separate Prozesse führen separate Austauschvorgänge durch und benötigen deshalb Assertions, deren Nutzung der Anbieter ihnen erlaubt.

## Rangfolge der Zugangsdaten

Die beiden erforderlichen Variablen für die Workload-Identität haben Vorrang vor jeder anderen Quelle für Zugangsdaten:

1. Wenn entweder `OPENAI_FEDERATION_RULE_ID` oder
`OPENAI_IDENTITY_TOKEN_FILE` vorhanden ist, wählt Codex die Workload-Identität aus.
2. Ist nur eine der erforderlichen Variablen vorhanden, gibt Codex einen Fehler zurück. Es greift nicht auf einen API-Schlüssel, ein Zugriffstoken oder eine gespeicherte Anmeldung zurück.
3. Mit `OPENAI_WORKLOAD_IDENTITY_CONTEXT` allein wählt Codex die Workload-Identität nicht aus.
4. Ist keine der beiden erforderlichen WIF-Variablen vorhanden, gelten für den jeweiligen Zugriffsweg die üblichen
   Regeln für Zugangsdaten. Bei Zugriffswegen, die eine Authentifizierung per API-Schlüssel
   unterstützen, hat `CODEX_API_KEY` bei `codex exec`,
`codex review`, dem TypeScript SDK und `codex exec-server --remote` Vorrang. Andere
   Zugriffswege können `CODEX_ACCESS_TOKEN` oder eine gespeicherte Anmeldung verwenden.

Die SDK-Option `apiKey` wird zu `CODEX_API_KEY`. WIF hat jedoch Vorrang,
sobald eine der beiden erforderlichen WIF-Variablen vorhanden ist. Lass diese Option bei Verwendung von WIF weg,
damit der Workload keine ungenutzten, langlebigen Zugangsdaten mitführt.

Um einen vorhandenen Workload ohne Ausfallzeit umzustellen, konfiguriere WIF, solange die bisherigen Zugangsdaten noch verfügbar sind. Starte einen neuen Prozess mit beiden erforderlichen WIF-Variablen. WIF hat Vorrang, selbst wenn die bisherigen Zugangsdaten noch vorhanden sind. Sobald der Workload mit WIF erfolgreich ausgeführt wird, entferne die bisherigen Zugangsdaten aus seiner Laufzeitumgebung und seinem Geheimnisspeicher und widerrufe sie anschließend. Vor dem Widerruf kannst du zur bisherigen Konfiguration zurückkehren, indem du beide erforderlichen WIF-Variablen entfernst und einen neuen Prozess startest.

## Unterstützte Codex-Zugriffswege

Konfiguriere die Workload-Identität auf dem Rechner, auf dem der Codex-Prozess ausgeführt wird.

| Zugriffsweg                                         | Unterstützung und Hostgrenze                                                                               |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Interaktive Nutzung von `codex`, `resume` und `fork`       | Unterstützt. Starte die CLI in der konfigurierten Umgebung.                                                 |
| `codex exec`, `exec resume` und `codex review` | Unterstützt. Bereits eine der beiden erforderlichen WIF-Variablen bewirkt, dass WIF Vorrang hat.                                      |
| TypeScript SDK                                  | Unterstützt. Der übergeordnete Prozess stellt die erforderlichen WIF-Variablen und gegebenenfalls einen Zuordnungskontext bereit. |
| `codex app-server`                              | Unterstützt. Konfiguriere WIF auf dem app-server-Host, nicht auf einem Remote-Client.                                |
| `codex exec-server --remote`                    | Unterstützt für die Authentifizierung bei der Registry für Remote-Umgebungen. Konfiguriere WIF auf dem exec-server-Host. |
| Lokale Prozessvorgänge des exec-server            | Sie verwenden keine WIF-Authentifizierung und laufen über das lokale exec-server-Protokoll.                         |
| `codex mcp-server`                              | Nicht unterstützt.                                                                                          |

Remote-Clients für app-server und exec-server übertragen das vorgelagerte Identitätstoken niemals über ihre Protokolle.

## Zugriff ändern oder entziehen

Änderungen an den Subjects, Audiences, Claims, der CEL-Bedingung, den Scopes oder der Token-Gültigkeitsdauer einer Regel gelten für neue Austauschvorgänge. Ein vor der Änderung ausgestelltes Token kann bis zum Ablauf seiner Gültigkeitsdauer gültig bleiben.

Deaktiviere einen Anbieter oder eine Regel, um den Zugriff sofort zu unterbinden. Die Deaktivierung verhindert neue Austauschvorgänge und widerruft bereits über diese Ressource ausgestellte OpenAI-Zugriffstoken. Die Archivierung hat dieselben Auswirkungen auf den Zugriff und lässt sich nicht rückgängig machen. Auch eine Änderung der Vertrauenskonfiguration des Anbieters widerruft ausgestellte Token, bevor die neue Vertrauenskonfiguration wirksam wird.

## Änderungen auditieren

Beim Erstellen, Aktualisieren und Archivieren von Anbietern und Föderationsregeln entstehen
Audit-Ereignisse. Nutze den [Leitfaden zur Compliance API
und zu Audit-Ereignissen](/de-DE/codex/enterprise/compliance-api), um die von deinem Workspace
unterstützten Ereignisse zu exportieren. Gleiche sie mit den Ausstellungsprotokollen deines Identitätsanbieters ab
und protokolliere in keinem der beiden Systeme vorgelagerte Assertions oder OpenAI-Zugriffstoken.

Wenn der Prozess `OPENAI_WORKLOAD_IDENTITY_CONTEXT` bereitstellt, enthalten Audit-Ereignisse über eine erfolgreiche
Token-Ausstellung zusätzlich die stabile Zuordnungs-ID und den oben beschriebenen
normalisierten Kontext.

## Fehlerbehebung

| Symptom                                                               | Prüfung                                                                                                              |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Codex meldet eine unvollständige Konfiguration der Workload-Identität              | Lege beide erforderlichen Variablen im selben Prozess fest und verwende einen absoluten Pfad zur Token-Datei.                               |
| Codex meldet, dass seine Anmelderichtlinie keine Workload-Identität zulässt | Erlaube die ChatGPT-Authentifizierung in der wirksamen Richtlinie und nimm den Workspace der Regel in die Liste der zulässigen Workspaces auf. |
| Codex meldet andere Zugangsdaten                                      | Lade beide erforderlichen WIF-Variablen in den Codex-Prozess, starte anschließend einen neuen Prozess und führe `codex login status` erneut aus.  |
| OpenAI lehnt den Workload-Kontext ab                                       | Überprüfe die JSON-Struktur, die Größe, die zulässigen Zeichen und die Grenzwerte der Felder. Entferne sensible Daten oder Kundeninhalte.            |
| OpenAI lehnt das Token ab                                              | Gleiche `iss`, `aud`, den Ablaufzeitpunkt, den Signaturschlüssel und die Gültigkeitsdauer der Assertion mit der Anbieterkonfiguration ab.               |
| Die Regel greift nicht                                               | Vergewissere dich, dass der Client die vorgesehene Regel-ID verwendet und alle Prüfungen für Subject, Audience, exakte Claims und CEL erfolgreich sind.  |
| OpenAI lehnt den Prinzipal ab                                          | Stelle sicher, dass das Benutzer- oder Dienstkonto aktiv ist und dem ausgewählten Workspace als aktives Mitglied angehört.                   |
| OpenAI lehnt eine wiederholt verwendete Assertion ab.                                   | Fordere ein neues JWT mit einer neuen `jti` an. Verwende dieselbe gegen Replay geschützte Assertion nicht erneut.                                  |
| Ein lang andauernder Prozess führt keine Aktualisierungen mehr durch.                               | Stelle sicher, dass der Aktualisierungsprozess auf dem Host die Token-Datei weiterhin rechtzeitig vor Ablauf ersetzt.                                  |

Informationen zur Überprüfung von Anbietern, zu Grenzwerten und zu CEL findest du in der [Referenz zu
Föderationsregeln](/api/docs/guides/workload-identity-federation/federation-rules).

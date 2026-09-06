<!-- source: https://learn.chatgpt.com/de-DE/docs/auth -->

## OpenAI-Authentifizierung

<a id="sign-in-with-chatgpt"></a>

Codex unterstützt bei der Verwendung von OpenAI-Modellen zwei Anmeldemethoden:

- Mit ChatGPT anmelden, um über ein Abonnement Zugriff zu erhalten
- Mit einem API-Schlüssel anmelden, um nutzungsbasierten Zugriff zu erhalten

Die ChatGPT-Desktop-App, Codex CLI und die IDE-Erweiterung unterstützen beide
Anmeldemethoden für die lokale Arbeit. Codex Cloud erfordert die Anmeldung mit ChatGPT.

Deine Anmeldemethode bestimmt außerdem, welche administrativen Kontrollen und Richtlinien zur Datenverarbeitung gelten.

- Wenn du dich mit ChatGPT anmeldest, gelten für die Codex-Nutzung die Berechtigungen deines ChatGPT-Workspaces,
die rollenbasierte Zugriffskontrolle (RBAC) sowie die Einstellungen von ChatGPT Enterprise
zur Datenaufbewahrung und Datenresidenz.
- Bei einem API-Schlüssel gelten stattdessen die Einstellungen deiner API-Organisation zur Datenaufbewahrung und
Datenfreigabe.

Bei verwalteten Workspaces ist die Authentifizierung nur eine Ebene der Zugriffssteuerung. Die Mitgliedschaft im Workspace und die
Provisionierung legen fest, wer sich anmelden kann. Lizenzen und
Workspace-Rollen bestimmen, welche Produktoberflächen und Funktionen diese Personen nutzen können.
Bei der lokalen Arbeit in der ChatGPT-Desktop-App, mit Codex CLI oder der IDE-Erweiterung
legen Berechtigungsprofile fest, welche Aktionen der Agent auf dem Gerät ausführen darf. Unter
[Gruppen und Provisionierung](/de-DE/codex/enterprise/groups-and-provisioning)
und [Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions)
erfährst du, wie du diese Kontrollen planst.

### Mit ChatGPT anmelden

Wenn du dich über die ChatGPT-Desktop-App, Codex CLI oder die IDE-Erweiterung mit ChatGPT anmeldest, öffnet der Anmeldevorgang ein Browserfenster. Nach der Anmeldung übermittelt der Browser deine Anmeldedaten an Codex.

### ChatGPT Web

Öffne [ChatGPT](https://chatgpt.com), melde dich an und wähle den Workspace aus, in dem du
arbeiten möchtest. ChatGPT Web hält die authentifizierte Sitzung in deinem Browser aufrecht.

#### ChatGPT-Desktop-App

Wähle auf dem Anmeldebildschirm **Weiter zur Anmeldung** aus und schließe den
Vorgang im Browser ab.

#### Codex CLI

Führe `codex login` aus und schließe den Vorgang im Browser ab. Dies ist die standardmäßige
Authentifizierungsmethode, wenn keine gültige Sitzung verfügbar ist.

#### IDE-Erweiterung

Wähle auf dem Anmeldebildschirm **Mit ChatGPT anmelden** aus und schließe den
Vorgang im Browser ab.

<a id="sign-in-with-an-api-key"></a>

### Mit einem API-Schlüssel anmelden

Du kannst dich auch mit einem API-Schlüssel bei der ChatGPT-Desktop-App, Codex CLI oder der IDE-Erweiterung anmelden. Deinen API-Schlüssel erhältst du im [OpenAI-Dashboard](https://platform.openai.com/api-keys).

#### ChatGPT-Desktop-App

Wähle auf dem Anmeldebildschirm **Anders anmelden** aus, gib deinen Schlüssel ein und
wähle anschließend **Weiter** aus.

#### Codex CLI

Leite den Schlüssel über stdin an `codex login` weiter:

```shell
printenv OPENAI_API_KEY | codex login --with-api-key

#### IDE-Erweiterung

Wähle auf dem Anmeldebildschirm **API-Schlüssel verwenden** aus, gib deinen Schlüssel ein und wähle anschließend
**OK** aus.

OpenAI rechnet die Nutzung des API-Schlüssels über dein Konto auf der OpenAI Platform zu den regulären API-Tarifen ab. Weitere Informationen findest du auf der [Seite zu den API-Preisen](https://openai.com/api/pricing/).

Die Authentifizierung per API-Schlüssel unterstützt lokale Codex-Arbeitsabläufe. Einige Funktionen, die
Zugriff auf einen ChatGPT-Workspace oder Cloud-Dienste erfordern, sind jedoch eingeschränkt oder nicht verfügbar.
Vergleiche die von den einzelnen Tarifen unterstützten Funktionen unter
[Verfügbarkeit der Funktionen](/de-DE/codex/pricing#feature-availability).

In Codex CLI und Codex in der ChatGPT-Desktop-App ermöglicht die Authentifizierung per API-Schlüssel
den Zugriff auf unterstützte, von OpenAI kuratierte Plug-ins. Einige Plug-ins sind nicht
verfügbar, weil ihre Verbindungsvorgänge OAuth-Funktionen erfordern, die nicht
unterstützt werden. Weitere Informationen findest du unter [Plug-ins verwenden](/de-DE/codex/plugins#api-key-availability).

Wenn du dich mit einem API-Schlüssel anmeldest, gelten für Codex die regulären API-Preise anstelle der
im ChatGPT-Tarif enthaltenen Credits.

Verwende die Authentifizierung per API-Schlüssel für programmatische Arbeitsabläufe mit Codex CLI, zum Beispiel für CI/CD-Jobs.
Stelle die Ausführung von Codex weder in nicht vertrauenswürdigen noch in öffentlichen Umgebungen bereit.

### Authentifizierung prüfen oder abmelden

Öffne das Profilmenü, um das aktive Konto und den Workspace zu überprüfen. Um die
Sitzung von ChatGPT Web in diesem Browser zu beenden, wähle **Abmelden** aus.

Öffne das Profilmenü, um das aktive Konto oder den Status des API-Schlüssels anzuzeigen. Wähle
**Abmelden** aus, um die aktuellen Anmeldedaten zu löschen.

Führe `codex login status` aus, um die aktive Authentifizierungsmethode anzuzeigen. Sind Authentifizierungsdaten gespeichert,
führe `codex logout` aus, um die aktuellen Anmeldedaten zu löschen. Wenn
der Prozess die Authentifizierung über eine Workload-Identität auswählt, lehnt Codex `codex login` und
`codex logout` ab, da die Prozessumgebung die Authentifizierung steuert.

Öffne das Profilmenü, um das aktive Konto oder den Status des API-Schlüssels anzuzeigen. Wähle
**Abmelden** aus, um die aktuellen Anmeldedaten zu löschen.

### Codex-Zugriffstoken für Automatisierungen im Unternehmen verwenden

In ChatGPT Enterprise-Workspaces können Administrierende die Berechtigung für Zugriffstoken
erteilen, sodass berechtigte Mitglieder Codex-Zugriffstoken für vertrauenswürdige,
nicht interaktive lokale Codex-Arbeitsabläufe erstellen können. Verwende ein Zugriffstoken,
wenn eine Automatisierung ohne Browseranmeldung Zugriff auf einen ChatGPT-Workspace,
von ChatGPT verwaltete Codex-Nutzungsrechte oder Kontrollfunktionen eines Unternehmens-Workspaces benötigt.

Zugriffstoken sind für vertrauenswürdige Skripte, Scheduler und private CI-Runner
vorgesehen. Verwende für allgemeine OpenAI-API-Aufrufe weiterhin Platform-API-Schlüssel.

Schritte zum Setup sowie Hinweise zu Berechtigungen, Rotation und Widerruf findest du unter
[Zugriffstoken](/de-DE/codex/enterprise/access-tokens).

Wenn deine Cloud-Plattform, dein CI-System oder dein Cluster bereits kurzlebige
Workload-Token ausgibt, verwende die
[Föderation von Workload-Identitäten](/de-DE/codex/enterprise/workload-identity),
anstatt OpenAI-Anmeldedaten zu speichern.

Wenn deine Umgebung bereits ein Codex-Zugriffstoken bereitstellt, leite es per Pipe an die CLI weiter:

```shell
printenv CODEX_ACCESS_TOKEN | codex login --with-access-token

## Dein Konto für Codex Cloud absichern

Codex Cloud interagiert direkt mit deiner Codebasis und benötigt daher stärkere Sicherheitsvorkehrungen als viele andere ChatGPT-Funktionen. Aktiviere die Multi-Faktor-Authentifizierung (MFA).

Wenn du dich über einen externen Anbieter (Google, Microsoft, Apple) anmeldest, musst du MFA für dein ChatGPT-Konto nicht aktivieren. Du kannst MFA aber bei diesem Anbieter einrichten.

Anleitungen zum Setup findest du hier:

- [Google](https://support.google.com/accounts/answer/185839)
- [Microsoft](https://support.microsoft.com/en-us/topic/what-is-multifactor-authentication-e5e39437-121c-be60-d123-eda06bddf661)
- [Apple](https://support.apple.com/en-us/102660)

Wenn du über Single Sign-On (SSO) auf ChatGPT zugreifst, sollte die SSO-Administration deiner Organisation MFA für alle Nutzenden verpflichtend machen.

Wenn du dich mit E-Mail-Adresse und Passwort anmeldest, musst du MFA für dein Konto einrichten, bevor du auf Codex Cloud zugreifst.

Wenn dein Konto mehrere Anmeldemethoden unterstützt und eine davon die Anmeldung mit E-Mail-Adresse und Passwort ist, musst du vor dem Zugriff auf Codex MFA einrichten. Das gilt auch, wenn du dich auf andere Weise anmeldest.

<a id="login-caching"></a>

## Zwischenspeichern von Anmeldedaten

Wenn du dich in der ChatGPT-Desktop-App, in Codex CLI oder in der IDE-Erweiterung über ChatGPT oder mit einem API-Schlüssel anmeldest, werden deine Anmeldedaten zwischengespeichert und wiederverwendet. Die CLI und die Erweiterung verwenden dieselben zwischengespeicherten Anmeldedaten. Wenn du dich bei einer von beiden abmeldest, musst du dich beim nächsten Start der CLI oder Erweiterung erneut anmelden.

Codex speichert Anmeldedaten lokal in einer Klartextdatei unter `~/.codex/auth.json` oder im Anmeldedatenspeicher deines Betriebssystems zwischen.

Bei Sitzungen nach einer Anmeldung mit ChatGPT aktualisiert Codex die Token während der Nutzung automatisch, bevor sie ablaufen. Aktive Sitzungen werden daher normalerweise ohne erneute Anmeldung im Browser fortgesetzt.

<a id="credential-storage"></a>
<a id="enforce-a-login-method-or-workspace"></a>

## Speicherung von Anmeldedaten

Mit `cli_auth_credentials_store` legst du fest, wo Codex CLI zwischengespeicherte Anmeldedaten speichert:

```toml
# file | keyring | auto
cli_auth_credentials_store = "keyring"

- `file` speichert Anmeldedaten in `auth.json` unter `CODEX_HOME` (standardmäßig `~/.codex`).
- `keyring` speichert Anmeldedaten im Anmeldedatenspeicher deines Betriebssystems.
- `auto` verwendet den Anmeldedatenspeicher des Betriebssystems, sofern er verfügbar ist, und greift andernfalls auf `auth.json` zurück.

In der [Konfigurationsreferenz](/de-DE/codex/config-file/config-reference) findest du das vollständige
`config.toml`-Schema.

  Wenn du die dateibasierte Speicherung verwendest, behandle `~/.codex/auth.json` wie ein Passwort: Die Datei
  enthält Zugriffstoken. Nimm sie nicht in einen Commit auf, füge sie nicht in Tickets ein und teile sie nicht im
  Chat.

## Anmeldemethode oder Workspace erzwingen

In verwalteten Umgebungen können Administrierende einschränken, wie sich Nutzende authentifizieren dürfen:

```toml
# Only allow ChatGPT login or only allow API key login.
forced_login_method = "chatgpt" # or "api"

# When using ChatGPT login, restrict users to a specific workspace.
forced_chatgpt_workspace_id = "00000000-0000-0000-0000-000000000000"

Wenn die aktiven Anmeldedaten nicht den konfigurierten Einschränkungen entsprechen, meldet Codex dich ab und beendet sich.

Diese Einstellungen werden üblicherweise über die verwaltete Konfiguration statt über ein individuelles Setup festgelegt. Weitere Informationen findest du unter [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration).

## Anmeldediagnose

Wenn du `codex login` direkt ausführst, legt Codex die separate Datei `codex-login.log` in
deinem konfigurierten Protokollverzeichnis an. Nutze sie, um Fehler bei der Browseranmeldung oder
der Gerätecodeanmeldung zu untersuchen oder wenn der Support spezielle Anmeldeprotokolle anfordert.

## Benutzerdefinierte CA-Bundles

Wenn dein Netzwerk einen TLS-Proxy deines Unternehmens oder eine private Root-CA verwendet, setze vor der Anmeldung
`CODEX_CA_CERTIFICATE` auf ein PEM-Bundle. Wenn
`CODEX_CA_CERTIFICATE` nicht gesetzt ist, greift Codex auf `SSL_CERT_FILE` zurück. Dieselben
benutzerdefinierten CA-Einstellungen gelten für die Anmeldung, normale HTTPS-Anfragen
und sichere WebSocket-Verbindungen.

```shell

codex login

## Anmeldung auf Headless-Geräten

Wenn du dich mit Codex CLI bei ChatGPT anmeldest, funktioniert die browserbasierte Anmeldeoberfläche in manchen Situationen möglicherweise nicht:

- Du führst die CLI in einer Remote- oder Headless-Umgebung aus.
- Deine lokale Netzwerkkonfiguration blockiert den localhost-Callback, über den Codex das OAuth-Token nach der Anmeldung an die CLI zurückgibt.

Verwende in diesen Situationen bevorzugt die Gerätecode-Authentifizierung (Beta). Wähle in der interaktiven Anmeldeoberfläche **Mit Gerätecode anmelden** aus oder führe `codex login --device-auth` direkt aus. Wenn die Gerätecode-Authentifizierung in deiner Umgebung nicht funktioniert, verwende eine der alternativen Methoden.

### Empfohlen: Gerätecode-Authentifizierung (Beta)

1. Aktiviere die Anmeldung per Gerätecode in deinen ChatGPT-Sicherheitseinstellungen (persönliches Konto) oder in den Workspace-Berechtigungen von ChatGPT (Workspace-Admin).
2. Wähle im Terminal, in dem du Codex ausführst, eine der folgenden Optionen:
   - Wähle in der interaktiven Anmeldeoberfläche **Mit Gerätecode anmelden** aus.
   - Führe `codex login --device-auth` aus.
3. Öffne den Link in deinem Browser, melde dich an und gib anschließend den Einmalcode ein.

Wenn die Anmeldung per Gerätecode in deiner Umgebung nicht verfügbar ist, verwende eine der
folgenden alternativen Methoden.

### Alternative: Lokal anmelden und den Anmelde-Cache kopieren

Wenn du den Anmeldevorgang auf einem Computer mit Browser abschließen kannst, kannst du die zwischengespeicherten Anmeldedaten auf das Headless-Gerät kopieren.

1. Führe auf einem Computer, auf dem du den browserbasierten Anmeldevorgang verwenden kannst, `codex login` aus.
2. Prüfe, ob der Anmelde-Cache unter `~/.codex/auth.json` vorhanden ist.
3. Kopiere `~/.codex/auth.json` an den Speicherort `~/.codex/auth.json` auf dem Headless-Gerät.

Behandle `~/.codex/auth.json` wie ein Passwort: Die Datei enthält Zugriffstoken. Nimm sie nicht in einen Commit auf, füge sie nicht in Tickets ein und teile sie nicht im Chat.

Wenn dein Betriebssystem die Anmeldedaten statt in `~/.codex/auth.json` in einem Anmeldedatenspeicher ablegt, ist diese Methode möglicherweise nicht anwendbar. Unter
[Speicherung von Anmeldedaten](/de-DE/codex/auth#credential-storage) erfährst du, wie du die dateibasierte Speicherung konfigurierst.

Per SSH auf einen Remote-Computer kopieren:

```shell
ssh user@remote 'mkdir -p ~/.codex'
scp ~/.codex/auth.json user@remote:~/.codex/auth.json

Oder verwende einen Einzeiler ohne `scp`:

```shell
ssh user@remote 'mkdir -p ~/.codex && cat > ~/.codex/auth.json' < ~/.codex/auth.json

In einen Docker-Container kopieren:

```shell
# Replace MY_CONTAINER with the name or ID of your container.
CONTAINER_HOME=$(docker exec MY_CONTAINER printenv HOME)
docker exec MY_CONTAINER mkdir -p "$CONTAINER_HOME/.codex"
docker cp ~/.codex/auth.json MY_CONTAINER:"$CONTAINER_HOME/.codex/auth.json"

Eine fortgeschrittene Variante desselben Vorgehens auf vertrauenswürdigen CI/CD-Runnern findest du unter
[Codex-Kontoauthentifizierung in CI/CD aufrechterhalten (fortgeschritten)](/codex/auth/ci-cd-auth).
Die Anleitung erklärt, wie du Codex `auth.json` bei regulären Ausführungen aktualisieren lässt und
die aktualisierte Datei anschließend für den nächsten Job aufbewahrst. API-Schlüssel bleiben die empfohlene
Standardoption für die Automatisierung.

### Alternative: localhost-Callback über SSH weiterleiten

Wenn du Ports zwischen deinem lokalen Computer und dem Remote-Host weiterleiten kannst, lässt sich der standardmäßige browserbasierte Anmeldevorgang verwenden. Richte dazu einen Tunnel zum lokalen Callback-Server von Codex ein (standardmäßig `localhost:1455`).

1. Starte auf deinem lokalen Computer die Portweiterleitung:

```shell
ssh -L 1455:localhost:1455 user@remote

2. Führe in dieser SSH-Sitzung `codex login` aus und rufe auf deinem lokalen Computer die ausgegebene Adresse auf.

## Alternative Modellanbieter

Wenn du in deiner Konfigurationsdatei einen [benutzerdefinierten Modellanbieter](/de-DE/codex/config-file/config-advanced#custom-model-providers) definierst, kannst du eine der folgenden Authentifizierungsmethoden wählen:

- **OpenAI-Authentifizierung**: Lege `requires_openai_auth = true` fest, um die OpenAI-Authentifizierung zu verwenden. Anschließend kannst du dich mit ChatGPT oder einem API-Schlüssel anmelden. Das ist hilfreich, wenn du über einen LLM-Proxyserver auf OpenAI-Modelle zugreifst. Bei `requires_openai_auth = true` ignoriert Codex `env_key`.
- **Authentifizierung über eine Umgebungsvariable**: Lege `env_key = "<ENV_VARIABLE_NAME>"` fest, um einen anbieterspezifischen API-Schlüssel aus der lokalen Umgebungsvariablen `<ENV_VARIABLE_NAME>` zu verwenden.
- **Keine Authentifizierung**: Wenn du `requires_openai_auth` nicht festlegst (oder auf `false` setzt) und `env_key` ebenfalls nicht festlegst, geht Codex davon aus, dass der Anbieter keine Authentifizierung erfordert. Das ist für lokale Modelle nützlich.

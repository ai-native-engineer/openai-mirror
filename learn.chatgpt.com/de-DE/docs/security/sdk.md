<!-- source: https://learn.chatgpt.com/de-DE/docs/security/sdk -->

Verwende das Codex Security TypeScript SDK, um aus deiner Anwendung oder deinem Entwicklungstool Sicherheitsscans für Repositorys und Codeänderungen auszuführen. Das SDK gibt typisierte Befunde, Details zur Abdeckung und Pfade zu Scan-Artefakten zurück. Für längere Scans unterstützt es Preflight-Prüfungen, Kostenlimits, Fortschritts-Callbacks und Abbrüche.

Das SDK verwendet ECMAScript-Module (ESM) und läuft serverseitig mit Node.js 22
(22.13.0 oder höher), 24 oder 26. Für Scans ist außerdem Python 3.10 oder höher erforderlich.
Python 3.10 benötigt zusätzlich das Paket `tomli`.

  Das Codex Security SDK ist [öffentlich auf
  GitHub verfügbar](https://github.com/openai/codex-security). Zum Ausführen von Scans ist
  Zugriff auf Codex Security erforderlich. Informationen zu allgemeinen Programmieragenten findest du im [Leitfaden zum
  Codex SDK](/de-DE/codex/codex-sdk). Informationen zu Terminal- und CI-Arbeitsabläufen findest du im [Schnellstart für die
  Codex Security CLI](/de-DE/codex/security/cli).

## SDK einrichten

Installiere das SDK:

```bash
npm install @openai/codex-security

Lege vor dem Start eines Scans `OPENAI_API_KEY` oder `CODEX_API_KEY` fest, verwende eine
vorhandene dateibasierte Codex-Anmeldung oder [konfiguriere einen anderen
Anbieter](#configure-the-runtime-and-credentials). Amazon Bedrock verwendet AWS-Anmeldedaten;
OpenRouter und Fireworks verwenden anbieterspezifische API-Schlüssel und
Konfigurationen.

Verwende für optimale Ergebnisse ein Konto, das für [Trusted Access for
Cyber](https://chatgpt.com/cyber) verifiziert ist. Eine Anmeldung oder die Angabe eines API-Schlüssels
gewährt keinen Trusted Access.

## Scan ausführen

Scanne nur Repositorys, denen du vertraust und für deren Überprüfung du berechtigt bist. Das SDK läuft
mit deinen lokalen Betriebssystemberechtigungen und hält niemals an, um eine Genehmigung einzuholen.
Scan-Prozesse können deine Umgebung übernehmen. Entferne daher vor dem Start
Anmeldedaten, die nichts mit dem Scan zu tun haben. Siehe [Berechtigungen für lokale
Scans](/de-DE/codex/security/cli/reference#local-scan-permissions).

Erstelle genau einen `CodexSecurity`-Client, führe einen Standardscan des Repositorys aus und schließe
den Client nach Abschluss des Vorgangs. Übergib `outputDir`, um ein privates
Ergebnisverzeichnis außerhalb des umgebenden Git-Worktrees auszuwählen.

Wenn du `outputDir` weglässt, speichert Codex Security die Ergebnisse in einem eigenen persistenten
Zustandsverzeichnis. Ergebnisse können Auszüge aus dem Quellcode und Details zu Schwachstellen
enthalten. Wähle daher geeignete Berechtigungen und Aufbewahrungsrichtlinien.

```ts

const security = new CodexSecurity();

try {
  const result = await security.run("/path/to/repository", {
    outputDir: "/path/outside/repository/results",
  });

  console.log(result.reportPath);
  console.log(result.coverage.completeness);
  console.log(result.findings.findings.length);
} finally {
  await security.close();
}

`run` startet den Scan, wartet auf seinen Abschluss, validiert die versiegelten Artefakte
und gibt ein `ScanResult` zurück. `close` gibt die isolierte Laufzeitumgebung frei und kann
wiederholt aufgerufen werden.

## Eingaben mit Preflight prüfen

Prüfe vor dem Start eines Scans mit `preflight` ein Repository, das Ziel, den Modus, Dokumente der Wissensdatenbank,
den Ausgabeort und die Codex-Konfiguration:

```ts
const plan = await security.preflight("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
  knowledgeBasePaths: ["/path/to/architecture.md"],
  outputDir: "/path/outside/repository/results",
});

console.log(plan.repository);
console.log(plan.target.kind);
console.log(plan.mode);
console.log(plan.outputDir);

Preflight verändert weder die Codex-Laufzeitumgebung noch die Anmeldedaten. Auch die Suche nach Plug-ins und Python übernimmt erst der Scan selbst. Daher eignet sich Preflight, um Benutzereingaben vor lang andauernden Vorgängen oder Vorgängen, die Anmeldedaten erfordern, zu prüfen.

Um die Archivierung eines vorhandenen Ergebnisverzeichnisses vorab anzuzeigen, lege
`archiveExisting: true` fest:

```ts
const plan = await security.preflight("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
});

console.log(plan.archiveDir);

Der zurückgegebene Wert `archiveDir` zeigt vorab, wie das Archiv benannt wird. Der endgültige Pfad kann
abweichen, weil `run` ein eigenes eindeutiges Ziel erzeugt. Erfasse den tatsächlichen
Archivpfad mit `onOutputArchived`:

```ts
await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
  onOutputArchived(archiveDir) {
    console.log("Archived results:", archiveDir);
  },
});

Der Scan archiviert die vorherigen Ergebnisse und beginnt mit einem leeren Ausgabeverzeichnis.

## Scan-Ziel auswählen

Das SDK unterstützt Ziele für Repositorys, Pfade, Commit-Diffs und Worktrees. Standardmäßig ist das vollständige Repository das Ziel.

### Ausgewählte Pfade scannen

Übergib ein Array mit Pfaden innerhalb des Repositorys:

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
});

Pfade können Dateien oder Verzeichnisse bezeichnen. Das SDK löst jeden Pfad innerhalb des Repositorys auf und entfernt Duplikate.

### Änderungen aus Commits scannen

Scanne mit `DiffTarget.refs` Änderungen aus Commits zwischen zwei lokal verfügbaren
Git-Revisionen:

```ts

const target = DiffTarget.refs({
  base: "origin/main",
  head: "HEAD",
});

const result = await security.run("/path/to/repository", { target });

Als Head wird standardmäßig `HEAD` verwendet. Bei Diff-Zielen muss das Repository-Argument
das Stammverzeichnis des Git-Worktrees sein.

### Worktree scannen

Scanne mit `DiffTarget.workingTree` zum Commit vorgemerkte und nicht vorgemerkte Änderungen gegenüber einer
Basisrevision:

```ts
const target = DiffTarget.workingTree({ base: "HEAD" });
const result = await security.run("/path/to/repository", { target });

Als Basis wird standardmäßig `HEAD` verwendet. Rufe die ausgewählten Revisionen ab, bevor du einen
Diff- oder Worktree-Scan startest.

### Tiefenmodus auswählen

Lege `mode: "deep"` für einen Repository- oder Pfad-Scan fest, der eine umfassendere Überprüfung erfordert:

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing"],
  mode: "deep",
  workers: 2,
  subagents: 0,
  stopAfterNoNew: 3,
  maxDiscoveryRuns: 10,
  maxTimeHours: 1.5,
});

Der Tiefenmodus unterstützt Repository- und Pfadziele. Verwende für Diff- und
Worktree-Scans den Standardmodus. Mit den optionalen Einstellungen steuerst du, wie viele unabhängige Worker für Standardscans parallel
laufen, wie viele Subagenten pro Worker eingesetzt werden und wie viele Worker-Scans nacheinander
ohne neue Befunde abgeschlossen werden. Du steuerst außerdem die Gesamtzahl und Dauer der Worker-Durchläufe.
Diese Einstellungen setzen `mode: "deep"` voraus.

`maxTimeHours` ist standardmäßig auf `96` gesetzt und akzeptiert positive Werte bis `96`;
auch Stundenbruchteile sind zulässig. Nach Ablauf der Zeit stoppt Codex Security noch laufende
Worker, bewahrt die Ergebnisse abgeschlossener Scans auf und fasst sie im abschließenden
Bericht zusammen. Prüfe `result.coverage.completeness`, bevor du einen zeitlich begrenzten
Scan als Nachweis vollständiger Abdeckung wertest.

### Sicherheitsbezogene Wissensdatenbank hinzufügen

Übergib Architekturdokumente, Bedrohungsmodelle oder Sicherheitsrichtlinien über
`knowledgeBasePaths`:

```ts
const result = await security.run("/path/to/repository", {
  knowledgeBasePaths: [
    "/path/to/architecture.md",
    "/path/to/security-policies",
  ],
});

Das SDK akzeptiert Dateien oder Verzeichnisse und durchsucht Verzeichnisse rekursiv.
Unterstützte Dokumentformate sind `.md`, `.markdown`, `.txt`, `.pdf` und `.docx`.
Das SDK lehnt verknüpfte Eingabepfade ab, überspringt verknüpfte Verzeichniseinträge und nimmt
extrahierte Dokumentinhalte nicht in die gespeicherten Scan-Ergebnisse auf.

### Anweisungen für Scans und Folgeaktionen hinzufügen

Mit `scanPrompt` legst du den Schwerpunkt des Scans fest; mit `postScanPrompt` forderst du eine Folgeaktion an:

```ts
const result = await security.run("/path/to/repository", {
  scanPrompt: "Focus on tenant isolation and authorization checks.",
  postScanPrompt: "Write confirmed findings to post-scan-summary.md.",
});

Wenn die Folgeaktion fehlschlägt, behält das SDK den abgeschlossenen Scan bei und meldet den
Fehler über `onWarning`. Es stellt alle Artefakte des abgeschlossenen Scans wieder her, die durch die
Folgeaktion geändert wurden.

### Budget für einen Scan festlegen

Lege `maxCostUsd` fest, damit ein Scan beendet wird, wenn seine geschätzten Modellkosten ein Limit überschreiten.
Mit `onCost` kannst du die Kosten während des Scans verfolgen:

```ts
const result = await security.run("/path/to/repository", {
  maxCostUsd: 5,
  onCost(cost) {
    console.log(cost.estimatedUsd);
  },
});

console.log(result.cost?.estimatedUsd);

Das Limit beruht auf geschätzten Ausgaben und ist keine feste Obergrenze. Bereits laufende
Anfragen können daher mit Kosten knapp über dem Limit abgeschlossen werden. Erreicht ein Tiefenscan das Limit,
nachdem Codex Security die Ergebnisse abgeschlossener Worker zusammengeführt hat, gibt `run` ein Ergebnis zurück,
bei dem `coverage.completeness` auf `"partial"` gesetzt ist, und meldet die Budgetwarnung
über `onWarning`.

Wenn der Scan kein abgeschlossenes Teilergebnis erzeugen kann, löst `run`
`ScanCostLimitExceededError` aus und bewahrt alle verfügbaren Ausgaben auf.

## Mit Scan-Ergebnissen arbeiten

`ScanResult` stellt die strukturierten Dokumente, Scan-Metadaten und Artefaktpfade
bereit:

| Eigenschaft             | Inhalt                                                                           |
| -------------------- | ---------------------------------------------------------------------------------- |
| `manifest`           | Das versiegelte Scan-Manifest mit Angaben zu Ziel, Umfang und Ersteller sowie den Artefakteinträgen. |
| `findings`           | Befunde aus dem aktuellen Scan. Lies die Befundobjekte aus `findings.findings`.     |
| `repositoryFindings` | Offene Befunde aus mehreren Repository-Scans, sofern ein Scan-Verlauf verfügbar ist.             |
| `coverage`           | Überprüfte Bereiche, Ausschlüsse, zurückgestellte Aufgaben, offene Fragen und Vollständigkeit.    |
| `scanDir`            | Das Scan-Verzeichnis.                                                                |
| `threadId`           | Die Codex-Thread-Kennung für den Scan.                                          |
| `turnResult`         | Status und Antwort des Turns sowie verfügbare Nutzungsmetadaten.                               |
| `cost`               | Geschätzte Modell- und Token-Kosten oder `null`, falls nicht verfügbar.                        |
| `reportPath`         | Der Pfad zu `report.md`.                                                           |
| `manifestPath`       | Der Pfad zu `scan-manifest.json`.                                                  |
| `findingsPath`       | Der Pfad zu `findings.json`.                                                       |
| `coveragePath`       | Der Pfad zu `coverage.json`.                                                       |
| `artifactsDir`       | Das Verzeichnis supporting-artifacts.                                                |
| `sarifPath`          | Der generierte SARIF-Pfad oder `null`, wenn SARIF nicht vorhanden ist.                          |
| `pluginVersion`      | Die vom Scan-Ersteller erfasste Version.                                         |

Um für einen späteren Scan dasselbe Plug-in vorauszusetzen, übergib
`expectedPluginVersion: result.pluginVersion`. Das SDK lehnt den Scan ab, wenn die
installierte Plug-in-Version abweicht.

Nutze die strukturierten Befunde und die Abdeckung direkt:

```ts
for (const finding of result.findings.findings) {
  const location = finding.locations[0];
  if (location === undefined) continue;

  console.log(
    finding.severity.level,
    `${location.path}:${location.startLine}`,
    finding.title
  );
}

for (const deferred of result.coverage.deferred) {
  console.log(deferred.id, deferred.reason);
}

Befunde können die optionalen Felder `codeEvidence`, `rootCause`, `validation`,
`attackPath`, `remediationTests` und `preventiveControls` enthalten.

Bei repositoryweiten Befunden unterscheidet `confirmedInLatestScan` zwischen Befunden
aus dem neuesten Scan und früheren, weiterhin offenen Befunden:

```ts
for (const finding of result.repositoryFindings ?? []) {
  console.log(finding.title, finding.confirmedInLatestScan);
}

Die Vollständigkeit der Abdeckung wird als `complete`, `partial` oder `unknown` angegeben. Prüfe zurückgestellte
Bereiche, Ausschlüsse und offene Fragen, bevor du einen Scan als Nachweis für eine
Sicherheitsentscheidung heranziehst.

`result.toJSON()` gibt das Manifest, die Befunde für das Repository und den aktuellen Scan,
die Abdeckung, die Scan- und Thread-Kennungen, `reportPath`, `artifactsDir`,
`sarifPath`, die Kosten und die Turn-Metadaten in einem JSON-kompatiblen Objekt zurück.

## Einen Scan verfolgen oder abbrechen

Übergib `ScanOptions`-Callbacks, um den Start des Scans, den Fortschritt der Worker und
erneute Verbindungsversuche zu melden:

```ts
const result = await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  onScanStarted() {
    console.log("Scan started");
  },
  onProgress(progress) {
    console.log(progress.phase, progress.filesCompleted, progress.filesTotal);
  },
  onWorkerStatus(status) {
    console.log(status.kind, status);
  },
  onSessionEvent(session) {
    console.log(session.threadId, session.worker, session.event["type"]);
  },
  onReconnect(attempt, maxAttempts) {
    console.log(`Reconnect attempt ${attempt} of ${maxAttempts}`);
  },
  onObserverError(observer, error) {
    console.error(`${observer} failed`, error);
  },
});

console.log(result.reportPath);

Übergib ein `AbortSignal`, wenn der Abbruch durch eine Anfrage, einen Job-Controller
oder ein Timeout ausgelöst wird:

```ts

const controller = new AbortController();

try {
  const scan = security.run("/path/to/repository", {
    outputDir: "/path/outside/repository/results",
    signal: controller.signal,
  });

  controller.abort();
  await scan;
} catch (error) {
  if (error instanceof ScanInterruptedError) {
    console.error(error.scanDir);
  } else {
    throw error;
  }
}

Ein unterbrochener Scan kann in `scanDir` unvollständige Ausgaben hinterlassen. Bewahre dieses
Verzeichnis auf, wenn das Ergebnis untersucht werden muss.

Anwendungen, die den Fortschritt des Scan-Setups anzeigen, können auch die Lebenszyklus-Callbacks von `ScanOptions`
verwenden:

| Callback                            | Aufrufzeitpunkt                                          |
| ----------------------------------- | ---------------------------------------------------- |
| `onAuthentication(authentication)`  | Der Scan wählt seine Authentifizierungsmethode aus.          |
| `onOutputArchived(archiveDir)`      | Vorhandene Ergebnisse werden in das Archivverzeichnis verschoben.      |
| `onOutputDirReady(scanDir)`         | Das private Scanverzeichnis ist bereit.                 |
| `onScanStarted()`                   | Das Scan-Setup ist abgeschlossen und die Ausführung beginnt.           |
| `onTrustedAccessStatus(status)`     | Der Status von Trusted Access ist verfügbar.             |
| `onReconnect(attempt, maxAttempts)` | Das SDK versucht erneut, die Verbindung zu einem unterbrochenen Scan-Stream herzustellen.          |
| `onActivity(activity)`              | Ein Befehl, ein Tool, ein Reasoning-Schritt oder eine Nachricht wird aktualisiert. |
| `onProgress(progress)`              | Die Scanphase oder die Anzahl der überprüften Dateien ändert sich.       |
| `onWorkerStatus(status)`            | Der Status der Vorabprüfung oder Zuweisung eines Workers ändert sich.         |
| `onSessionEvent(session)`           | Eine Scan- oder Worker-Sitzung gibt ein Ereignis aus.             |
| `onCost(cost)`                      | Eine aktualisierte Schätzung der Scankosten liegt vor.         |
| `onWarning(warning)`                | Der Scan meldet eine Warnung.                          |
| `onObserverError(observer, error)`  | Ein anderer Lebenszyklus-Callback des Scans löst einen Fehler aus.     |

Der Status von Trusted Access lautet `granted`, `not_granted` oder `unknown`. Fehlender oder
unbekannter Zugriff löst ebenfalls `onWarning` aus.

`onSessionEvent` empfängt ungeschwärzte Ereignisse, die Quellcode
oder Anmeldedaten enthalten können. Filtere sie, bevor du sie in gemeinsam genutzte Logs schreibst oder an andere
Dienste sendest.

## Laufzeitumgebung und Anmeldedaten konfigurieren

Übergib eine Laufzeitkonfiguration, wenn du ein bestimmtes Plug-in, einen Interpreter oder
eine bestimmte Codex-Einstellung benötigst:

```ts
const security = new CodexSecurity({
  pluginPath: "/path/to/codex-security-plugin",
  pythonPath: "/path/to/python",
  codexOverrides: {
    model: "gpt-5.6-terra",
    model_reasoning_effort: "high",
  },
});

`pluginPath` akzeptiert ein Plug-in-Verzeichnis oder eine ZIP-Datei. Mit `pythonPath` wählst du den
Plug-in-Interpreter aus. `codexOverrides` führt unterstützte Werte mit der isolierten
Codex-Konfiguration zusammen. Scans verwenden standardmäßig `gpt-5.6-sol` mit sehr hohem
Reasoning-Aufwand. Lege `model` und `model_reasoning_effort` in `codexOverrides` fest, um
ein anderes Modell oder einen anderen Reasoning-Aufwand zu verwenden. Um [Amazon
Bedrock](/de-DE/codex/security/cli/reference#use-amazon-bedrock) zu nutzen, lege
`model_provider` und `model` in `codexOverrides` fest.

`codexOverrides` kann weder den Dateisystemzugriff des Scans einschränken noch dessen
Genehmigungsrichtlinie ändern. Siehe [Berechtigungen für lokale
Scans](/de-DE/codex/security/cli/reference#local-scan-permissions).

Gib für OpenRouter oder Fireworks außerdem den passenden API-Schlüssel und eine vollständige
Anbieterkonfiguration in `codexOverrides` an. Lege beispielsweise
`OPENROUTER_API_KEY` fest und konfiguriere OpenRouter:

```ts
const security = new CodexSecurity({
  codexOverrides: {
    model: "anthropic/claude-sonnet-4.5",
    model_provider: "openrouter",
    model_providers: {
      openrouter: {
        name: "OpenRouter",
        base_url: "https://openrouter.ai/api/v1",
        env_key: "OPENROUTER_API_KEY",
        wire_api: "responses",
      },
    },
  },
});

Ändere für Fireworks beide Schlüssel mit dem Namen `openrouter` in `fireworks`, setze `name` auf
`Fireworks AI`, setze `env_key` auf `FIREWORKS_API_KEY`, verwende
`https://api.fireworks.ai/inference/v1` als `base_url` und wähle ein Fireworks-Modell
aus.

Der Client stellt außerdem unterstützte Authentifizierungsmethoden bereit:

| Methode                     | Zweck                                                     |
| -------------------------- | ----------------------------------------------------------- |
| `loginApiKey(apiKey)`      | Die isolierte Laufzeitumgebung mit einem API-Schlüssel authentifizieren.          |
| `loginChatGPT()`           | Einen Anmeldevorgang im Browser starten und ein Login-Handle zurückgeben.     |
| `loginChatGPTDeviceCode()` | Einen Anmeldevorgang mit Gerätecode starten und ein Login-Handle zurückgeben. |
| `account()`                | Den aktuellen Authentifizierungsstatus zurückgeben.                    |
| `logout()`                 | Die isolierten Authentifizierungsdaten löschen.                              |

Ein Login-Handle stellt `waitForInstructions`, `authUrl`, `verificationUrl`,
`userCode`, `wait` und `cancel` bereit, damit eine Anwendung den
ausgewählten Anmeldevorgang anzeigen und abschließen kann. Das SDK kann eine in einer Datei gespeicherte Codex-Anmeldung wiederverwenden. API-Schlüssel
eignen sich gut für CI und serverseitige Automatisierung.

Wenn sowohl ein API-Schlüssel als auch eine gespeicherte Anmeldung verfügbar sind, verwendet das SDK standardmäßig den
API-Schlüssel. Um stattdessen deine ChatGPT-Anmeldung zu verwenden, wähle sie für den Scan aus:

```ts
const result = await security.run("/path/to/repository", {
  auth: "chatgpt",
});

Lege `auth: "api-key"` fest, damit ein API-Schlüssel aus der Umgebung erforderlich ist. Auch `preflight` akzeptiert
dieselbe Option `auth`.

## Scanfehler behandeln

Fange die exportierte Fehlerklasse ab, auf die deine Anwendung sinnvoll
reagieren kann:

| Fehler                            | Bedeutung                                                            |
| -------------------------------- | ------------------------------------------------------------------ |
| `AuthenticationRequiredError`    | Für einen Scan sind unterstützte Anmeldedaten erforderlich.                               |
| `ConfigurationError`             | Die Codex-Konfiguration oder eine Überschreibung ist ungeeignet.                  |
| `InvalidTargetError`             | Das Repository, der Pfad, der Modus oder das Git-Ziel ist ungeeignet.           |
| `OutputDirectoryError`           | Der Ausgabeort oder die zugehörigen Berechtigungen sind ungeeignet.             |
| `OutputInsideProtectedRootError` | Das Ausgabeverzeichnis liegt innerhalb des gescannten Repositorys oder Worktrees. |
| `PluginPythonUnavailableError`   | Es ist kein verwendbarer Python-Interpreter verfügbar.                        |
| `PluginBootstrapError`           | Die Plug-in-Laufzeitumgebung konnte nicht gestartet werden.                                |
| `ScanCostLimitExceededError`     | Der Scan hat das Limit für die geschätzten Kosten überschritten.                        |
| `IncompleteScanError`            | Der Scan endete, bevor das erforderliche Ergebnis erzeugt wurde.               |
| `ContractValidationError`        | Ein abgeschlossener Scan gab einen Fehler im strukturierten Vertrag zurück.             |
| `ScanInterruptedError`           | Eine Unterbrechung hat den Scan gestoppt und möglicherweise unvollständige Ausgaben hinterlassen. |

Weiter geht es mit dem [CLI-Schnellstart](/de-DE/codex/security/cli), dem [Leitfaden für
CI](/de-DE/codex/security/cli/ci) oder der [Referenz für
die CLI](/de-DE/codex/security/cli/reference).

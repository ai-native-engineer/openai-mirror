<!-- source: https://learn.chatgpt.com/de-DE/docs/security/security-review -->

Codex Security Review ist als Forschungsvorschau verfügbar.
Die Funktion steht Nutzenden von ChatGPT Enterprise, ChatGPT Business, ChatGPT Edu und ChatGPT Pro zur Verfügung; für ChatGPT Plus ist sie
nicht verfügbar. Während der Einführungsphase werden für Codex Security Review
keine ChatGPT-Credits verbraucht. Es können Nutzungslimits gelten.

Codex Security Review ist eine zusätzliche Überprüfung für alle, die bei
Pull Requests besonderes Augenmerk auf Sicherheitsprobleme legen möchten.

Codex Security Review untersucht sicherheitsspezifische Risiken gründlicher als [Code
Review](/de-DE/codex/third-party/github). Dazu analysiert die Funktion den
Diff des Pull Requests, ergänzenden Repository-Kontext sowie konfigurierte Bedrohungsmodelle
oder Sicherheitshinweise. Auch Code Review kann im Rahmen der allgemeinen Überprüfung sicherheitsrelevante Probleme erkennen,
sodass sich Befunde gelegentlich überschneiden können.

## Bevor du beginnst

Um Codex Security Review für die automatische Ausführung zu konfigurieren, benötigst du:

- Zugriff auf die Forschungsvorschau von Codex Security Review für deinen Workspace
- [Codex Cloud](/de-DE/codex/cloud), eingerichtet mit einem verbundenen GitHub-Repository
- Push- oder Admin-Berechtigung für die Repository-Einstellungen in GitHub

Ein bestehender Scan mit Codex Security ist optional.

<a id="configure-security-review"></a>

## Codex Security Review konfigurieren

1. Öffne die [Codex-Einstellungen](https://chatgpt.com/codex/settings/code-review).
2. Wähle unter **Repository-Einstellungen** aus, welche Pull Requests eine Codex
   Security Review erhalten sollen:
   - Mit **Persönlichen Einstellungen folgen** können alle Mitwirkenden Codex Security Review in ihren persönlichen
     Einstellungen aktivieren.
   - Die Option **Alle PRs überprüfen** gilt für jeden Pull Request im Repository.
   - Die Option **Team-PRs überprüfen** gilt, sofern verfügbar, für Pull Requests, die von
     Mitgliedern deines ChatGPT-Workspaces geöffnet wurden, jedoch nicht für Pull Requests von Mitgliedern eines GitHub-Teams.
3. Wähle aus, wann Codex Security Review ausgeführt wird:
   - Mit der Option **Beim Öffnen eines PR** wird eine eigenständige Überprüfung ausgeführt, sobald ein Pull Request geöffnet wird.
   - Mit der Option **Bei jedem Push** wird eine eigenständige Überprüfung ausgeführt, nachdem neue Commits gepusht wurden.
   - Für die Option **Immer wenn Code Review ausgeführt wird** ist Code Review erforderlich; Codex Security
     Review wird parallel dazu ausgeführt.

## Kontext zum Bedrohungsmodell hinzufügen

Du kannst ein Bedrohungsmodell konfigurieren, um Codex Kontext zu den Assets deiner Anwendung,
ihren Vertrauensgrenzen, Sicherheitsannahmen und Repository-spezifischen Risiken zu geben.
Wenn das Repository bereits über eine Scan-Konfiguration für Codex Security verfügt, kannst du
das zugehörige Bedrohungsmodell verwenden. Andernfalls gib den Pfad zu einer Datei mit dem Bedrohungsmodell an, die im Repository
eingecheckt ist. Wenn du keine Quelle angibst, erstellt Codex das
Bedrohungsmodell für jede Überprüfung neu.

## Meldeschwellenwerte festlegen

Automatische Codex Security Reviews melden standardmäßig als **Hoch** und **Kritisch**
eingestufte Befunde, manuell angeforderte Überprüfungen dagegen als **Mittel**, **Hoch** und
**Kritisch** eingestufte Befunde. Du kannst den Mindestschweregrad für
automatische und manuelle Überprüfungen unabhängig voneinander ändern und pfadbasierte Überschreibungen hinzufügen.

Befunde, die in einem Pull Request veröffentlicht werden, haben auf GitHub
dieselbe Sichtbarkeit wie der Pull Request. Alle, die den Pull Request sehen können, sehen auch diese Befunde,
auch bei öffentlichen Repositorys oder Pull Requests von Mitwirkenden außerhalb
deines Workspaces. Wähle die Meldeschwellenwerte bei Repositorys, in denen
Pull-Request-Kommentare für viele sichtbar sein können, mit Bedacht. Der Meldeschwellenwert legt fest,
was Codex auf GitHub veröffentlicht. Der vollständige Bericht von Codex Security Review bleibt in
Codex.

<a id="request-a-security-review"></a>

## Codex Security Review anfordern

Füge einem Pull Request diesen Kommentar hinzu, um Codex Security Review manuell anzufordern:

`@codex security review`

Codex reagiert, während die Überprüfung läuft, und veröffentlicht anschließend Befunde, die deinen
manuellen Meldeschwellenwert erreichen, direkt im Pull Request. Öffne die zugehörige
Codex-Aufgabe und wähle den Tab **Sicherheitsbericht** aus, um den vollständigen Bericht anzuzeigen,
einschließlich des Schweregrads, des Angriffspfads, der Belege, der Validierung und
der Empfehlungen zur Behebung. Wenn keine Probleme den Meldeschwellenwert erreichen, veröffentlicht Codex keine
Befunde im Pull Request.

## Weitere Dokumentation

- [Pull Requests in GitHub mit Codex überprüfen](/de-DE/codex/third-party/github) erläutert Code Review und die GitHub-Integration.
- [Codex Security](/de-DE/codex/security) bietet eine Übersicht über das Produkt.
- [Setup für Codex Security Cloud](/de-DE/codex/security/setup) erläutert Repository-Scans und die Überprüfung von Befunden.
- [Bedrohungsmodell verbessern](/de-DE/codex/security/threat-model) erläutert, wie du den Repository-Kontext gezielt anpasst.

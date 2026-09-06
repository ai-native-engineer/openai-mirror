<!-- source: https://learn.chatgpt.com/de-DE/docs/security -->

Codex Security ist ein Agent für Anwendungssicherheit, der Sicherheits- und
Entwicklungsteams dabei unterstützt, Schwachstellen zu finden, zu bestätigen und zu
beheben. Verwende ihn in Codex, über dein Terminal, mit dem TypeScript SDK oder mit
verbundenen GitHub-Repositories.

Für eine konkrete Anleitung zu deinem ersten lokalen Scan beginne mit dem [Schnellstart für das
Codex-Security-Plugin](/de-DE/codex/security/plugin).

## Codex Security in der Desktop-App verwenden

Öffne in der ChatGPT-Desktop-App das ChatGPT-Dropdown-Menü und wähle **Codex** aus.
Installiere und aktiviere das Codex-Security-Plugin, um **Sicherheit** in der
Seitenleiste zu öffnen. In der Sicherheits-Workbench findest du deine Scans, Befunde und
Repositories an einem Ort, während Codex jeden Scan als Aufgabe ausführt.

- Unter **Scans** kannst du Scans starten, ihren Fortschritt verfolgen und gespeicherte Ergebnisse überprüfen.
- Unter **Befunde** kannst du Probleme und Belege aus abgeschlossenen Scans untersuchen.
- Unter **Repositories** kannst du den Verlauf von Repositories und offene Befunde überprüfen.

Unter [Sicherheits-Workbench verwenden](/de-DE/codex/security/plugin/workbench) findest du den
vollständigen Ablauf in der Desktop-App.

### Anwendungsfälle des Plug-ins entdecken

- [Sicherheitsscan durchführen](/de-DE/codex/security/plugin/scans) für ein Repository oder einen einzelnen ausgewählten Ordner.
- [Tiefgehenden Sicherheitsscan durchführen](/de-DE/codex/security/plugin/deep-scans), wenn du eine umfassendere Prüfung benötigst und länger auf den Abschluss warten kannst.
- [Codeänderungen überprüfen](/de-DE/codex/security/plugin/code-changes), bevor du einen Pull Request oder Branch zusammenführst.
- [Backlog prüfen und priorisieren](/de-DE/codex/security/plugin/triage-backlog), wenn bereits Sicherheitsbefunde zur Überprüfung vorliegen.
- [Befunde beheben und überprüfen](/de-DE/codex/security/plugin/fix-findings) mit klar abgegrenzten Patches für genehmigte Befunde.
- [Befunde exportieren oder nachverfolgen](/de-DE/codex/security/plugin/export-findings), als übertragbare Artefakte oder über genehmigungspflichtige Zielsysteme zur Nachverfolgung.
- [Schwachstellenberichte erstellen](/de-DE/codex/security/plugin/vulnerability-reports) aus bereitgestellten Befunden, Hinweisen zur Offenlegung, Quellcode und PoCs.
- [Maßnahmen zur Sicherheitshärtung vorschlagen](/de-DE/codex/security/plugin/security-hardening) auf Grundlage von Scanergebnissen oder anderen sicherheitsrelevanten Belegen.
- Sieh dir die [Neuigkeiten](/de-DE/codex/security/plugin/changelog) zum Codex-Security-Plugin an.

  Die Sicherheits-Workbench in der Desktop-App und die Codex CLI verwenden das Codex-Security-Plugin.
  Codex Security Cloud scannt verbundene GitHub-Repositories über Codex Cloud.
  Informationen zu Sandboxing, Genehmigungen, Netzwerkkontrollen und Admin-Einstellungen von Codex findest du unter
[Agentenfreigaben und Sicherheit](/de-DE/codex/agent-approvals-security).

## Codex Security CLI und SDK

Die CLI und das TypeScript SDK sind als öffentliches Paket
[`@openai/codex-security`](https://github.com/openai/codex-security) verfügbar.
Führe die CLI mit `npx` aus:

```bash
npx @openai/codex-security --help

Für Scans benötigst du Zugriff auf Codex Security. Die besten Ergebnisse erzielst du mit einem Konto,
das für [Trusted Access for Cyber](https://chatgpt.com/cyber) verifiziert ist.

Nutze denselben Scanner wie im Plug-in für verschiedene Repositories und über längere Zeit. Die CLI
findet GitHub-Repositories, setzt Massenscans fort, verfolgt Befunde über mehrere Scans
hinweg und erfasst Rückmeldungen zu falsch positiven Ergebnissen. Füge Angaben zu deiner Architektur und deine
Sicherheitsrichtlinien hinzu, lege ein geschätztes Kostenlimit fest oder führe Prüfungen in CI und vor Commits durch.
Mit dem TypeScript SDK integrierst du Scans, Fortschrittsberichte und Kostenkontrollen
in eine Anwendung oder ein Entwicklungstool.

- [Starte mit dem CLI-Schnellstart](/de-DE/codex/security/cli), um die CLI einzurichten,
  ein Repository vorab zu prüfen und einen lokalen Scan durchzuführen.
- [Sicherheitsscans in großem Umfang durchführen](/de-DE/codex/security/cli/bulk-scans), um
  GitHub-Repositories zu finden oder anhand einer CSV-Bestandsliste eine fortsetzbare Kampagne durchzuführen.
- [Scans in CI durchführen](/de-DE/codex/security/cli/ci), um Änderungen an Pull Requests zu überprüfen,
  Artefakte aufzubewahren, SARIF hochzuladen und eine Richtlinie für Schweregrade festzulegen.
- [Lies die CLI-FAQ](/de-DE/codex/security/cli/faq), um Antworten zu Scanverlauf,
  Rückmeldungen zu falsch positiven Ergebnissen, Abdeckung und der Überprüfung von Fehlerbehebungen zu finden.
- [Nutze die CLI-Referenz](/de-DE/codex/security/cli/reference), um die unterstützten
  Befehle, Flags, Ausgabeformate, Artefakte und Exitcodes nachzuschlagen.
- [Integriere das TypeScript SDK](/de-DE/codex/security/sdk), um Ziele auszuwählen,
  Ergebnisse zu prüfen, Fortschritte zu verfolgen und Scans direkt aus dem Code abzubrechen.

## Codex Security Cloud

Codex Security Cloud ist derzeit als Forschungsvorschau verfügbar. Sie scannt verbundene
GitHub-Repositories auf mögliche Sicherheitsprobleme.

Damit können Teams:

1. **Mögliche Schwachstellen finden** , indem sie ein auf das jeweilige Repository zugeschnittenes Bedrohungsmodell und den tatsächlichen Codekontext nutzen.
2. **Irrelevante Meldungen reduzieren** , indem Befunde validiert werden, bevor du sie überprüfst.
3. **Die Behebung von Befunden voranbringen** mithilfe priorisierter Ergebnisse, Belege und vorgeschlagener Patch-Optionen.

## So funktioniert Codex Security Cloud

Codex Security scannt verbundene Repositories Commit für Commit.
Dazu stellt es aus deinem Repository den Scankontext zusammen, überprüft mögliche Schwachstellen anhand dieses Kontexts und validiert besonders aussagekräftige Befunde in einer isolierten Umgebung, bevor es sie anzeigt.

Der Ablauf konzentriert sich auf:

- Kontext aus dem jeweiligen Repository statt allgemeiner Signaturen
- Nachweise aus der Validierung, die helfen, falsch positive Ergebnisse zu reduzieren
- Lösungsvorschläge, die du auf GitHub überprüfen kannst

## Zugriff auf Codex Security Cloud und Voraussetzungen

Codex Security Cloud arbeitet mit GitHub-Repositories, die über Codex Cloud verbunden
sind. Falls ein Repository nicht angezeigt wird, prüfe, ob es in deinem
Codex Cloud-Workspace verfügbar ist, oder wende dich an dein OpenAI-Account-Team.

## Weiterführende Dokumentation

- [Schnellstart für das Codex-Security-Plugin](/de-DE/codex/security/plugin) führt dich durch die Installation und deinen ersten lokalen Scan.
- [Sicherheits-Workbench](/de-DE/codex/security/plugin/workbench) erläutert gespeicherte Scans, Befunde, Repositories und Scanaktivitäten in der Desktop-App.
- [Schnellstart für die Codex Security CLI](/de-DE/codex/security/cli) führt dich durch das Setup, die Vorabprüfung und den ersten Scan im Terminal.
- [Sicherheitsscans in großem Umfang durchführen](/de-DE/codex/security/cli/bulk-scans) erläutert die Erkennung von GitHub-Repositories, CSV-Bestandslisten, Kampagnenergebnisse und das Fortsetzen von Kampagnen.
- [FAQ zur Codex Security CLI](/de-DE/codex/security/cli/faq) beantwortet häufige Fragen zu Scans, Befunden, Abdeckung und Kosten.
- [Codex Security TypeScript SDK](/de-DE/codex/security/sdk) erläutert, wie du Scans aus einer Anwendung oder einem Entwicklungstool ausführst.
- [Setup für Codex Security Cloud](/de-DE/codex/security/setup) beschreibt das Setup, Scans und die Überprüfung von Befunden.
- [Sicherheits-Review](/de-DE/codex/security/security-review) erläutert, wie du eingehende Sicherheitsprüfungen für Pull Requests auf GitHub durchführst.
- [Bedrohungsmodell verbessern](/de-DE/codex/security/threat-model) erläutert, wie du Umfang, Einstiegspunkte und Annahmen zur Kritikalität anpasst.
- [FAQ zu Codex Security Cloud](/de-DE/codex/security/faq) beantwortet häufige Fragen zum Cloud-Produkt.

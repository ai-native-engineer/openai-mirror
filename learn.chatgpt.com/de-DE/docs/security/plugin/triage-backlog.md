<!-- source: https://learn.chatgpt.com/de-DE/docs/security/plugin/triage-backlog -->

Verwende `$codex-security:triage-finding`, um vorhandene Sicherheitsbefunde
anhand des aktuellen Repositorys zu prüfen. Dieser Workflow führt eine statische Analyse ohne
Schreibzugriff durch: Codex behandelt jeden Befund als unbewiesene Behauptung und prüft Belege
im Repository, ohne den Code auszuführen.

Führe diesen Workflow in einem Codex-Projekt für das Repository aus, das du
prüfen möchtest. Codex muss den Quellcode des Repositorys lesen können. Konnektoren für Jira und Linear
können Daten zu Befunden bereitstellen, während für GitHub-Befunde authentifizierter
Zugriff auf GitHub REST erforderlich ist. Keiner dieser Zugriffswege ersetzt den Zugriff auf den Quellcode.

Intern beginnt Codex mit den angegebenen Code- oder Versionsinformationen. Codex
verfolgt die mutmaßlich von Angreifenden kontrollierte Quelle, relevante Schutzmaßnahmen,
die gefährliche Senke und den erreichbaren Pfad. Außerdem prüft Codex den Produktbereich und die
Vertrauensgrenze, sucht nach widersprechenden Belegen und erfasst Nachweislücken. Anschließend gibt Codex
für jeden Befund eine Einstufung aus und priorisiert die Befunde, die Maßnahmen oder eine weitere
Prüfung erfordern.

Dieser Workflow unterscheidet sich von `$codex-security:validation`, da Codex damit Code kompilieren oder ausführen,
einen gezielten Test oder Proof of Concept erstellen oder eine echte Schnittstelle testen kann, um
einen Befund zu reproduzieren oder zu widerlegen. Verwende die Triage, um einen
vorhandenen Backlog zu klassifizieren und zu priorisieren. Verwende die Validierung, wenn Laufzeitbelege einen Befund klären können,
der anhand statischer Belege nicht eindeutig ist.

  Die Backlog-Triage geht von vorhandenen Befunden aus. Um das Repository nach neuen
  Schwachstellen zu durchsuchen, [führe einen Sicherheitsscan aus](/de-DE/codex/security/plugin/scans). Die Triage
  ändert das Repository nicht und setzt keine Korrekturen um.

## Befunde für die Triage auswählen

Du kannst einen einzelnen Befund oder eine Sammlung aus folgenden Quellen bereitstellen:

| Quelle                   | Erforderliche Angaben                                                                                                                                                                                                                                                                                                                                                                                                                                        | Voraussetzungen                                                                                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Eingefügte oder lokale Befunde | SARIF-Ergebnisse, eine CVE oder GHSA, ein Sicherheitshinweis, ein Scanner-Ticket, ein Bug-Bounty-Bericht, ein Befundartefakt aus Codex Security oder eine in natürlicher Sprache formulierte Behauptung zu einer Schwachstelle.                                                                                                                                                                                                                                                                                          | Kein Konnektor erforderlich.                                                                                                                                                                           |
| Jira oder Linear           | Genaue URLs oder Kennungen von Sicherheits- oder Schwachstellen-Issues, Jira JQL oder ein Team, Projekt bzw. Suchbegriff in Linear. Codex ruft vor der Triage die Inhalte der ausgewählten Issues ab.                                                                                                                                                                                                                                                                            | [Jira über Atlassian Rovo](codex://plugins/plugin_connector_692de805e3ec8191834719067174a384) oder [Linear](codex://plugins/plugin_asdk_app_69a089a326dc8191b32a3f2553f5be2c) mit Lesezugriff. |
| GitHub                   | Ein Repository und eine Befundquelle: Code-Scanning, von `Dependabot` gemeldete Schwachstellen und Malware, Sicherheitshinweise und private Schwachstellenmeldungen oder alle Quellen. Wenn du kein Repository angibst, verwendet Codex, sofern verfügbar, das GitHub-Repository, das mit dem aktuellen Codex-Projekt verknüpft ist. GitHub-Issues gehören nicht zu den standardmäßigen GitHub-Quellen. Gib ein bestimmtes Issue an oder fordere GitHub-Issues ausdrücklich an, wenn du sie in die Triage aufnehmen möchtest. | Authentifizierter Zugriff auf GitHub REST, etwa über `gh auth token`, `GH_TOKEN` oder `GITHUB_TOKEN`, mit Leseberechtigung für das ausgewählte Repository und den ausgewählten Befundtyp.                                      |

Codex behält für jeden angegebenen Befund genau ein Ergebnis in der Eingabereihenfolge bei, sodass jeder
ursprüngliche Befund nachverfolgbar bleibt. Befunde, die wie Duplikate wirken, werden weder zusammengeführt noch
verworfen.

## Triage ohne Schreibzugriff ausführen

Sende für eingefügte Befunde oder lokale Artefakte beispielsweise folgenden Prompt:

```text
Use $codex-security:triage-finding to triage these existing security findings against this repository:

[Paste the findings or provide the artifact path.]

Gib bei Issues aus Jira oder Linear die Issue-Auswahl an und greife auf das Quellsystem
ohne Schreibzugriff zu:

```text
Use $codex-security:triage-finding to import and triage the security findings from [Jira or Linear issue URLs, identifiers, or query] against this repository.
Do not change the source issues.

Gib bei GitHub-Befunden das Repository und die Quelle an:

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from [owner/repository] against this repository.

Um das mit dem aktuellen Codex-Projekt verknüpfte GitHub-Repository zu verwenden, gib
nur die Befundquelle an:

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from GitHub against this repository. Use the GitHub repository attached to the current Codex project.

Der Workflow läuft in dieser Reihenfolge ab:

1. Befunde erfassen und organisieren

   Codex ruft alle angeforderten Inhalte aus Issues oder GitHub ab, behält
Quellkennungen und Verweise bei und erstellt pro Eingabe ein Triage-Element. Codex stellt
die vollständige Elementliste zusammen, bevor die Einstufungen zugewiesen werden.

2. Repository-Kontext bestätigen

   Codex ermittelt, sofern verfügbar, das aktuelle Repository und die aktuelle Revision. Codex liest
`SECURITY.md`, sofern vorhanden, damit unterstützte Versionen, vertrauenswürdige Eingaben, Produktgrenzen
   und Bereiche außerhalb des Geltungsbereichs in die Bewertung einfließen.

3. Statische Belege prüfen

   Für jeden Befund verfolgt Codex die mutmaßlich von Angreifenden kontrollierte Quelle,
die relevante Schutzmaßnahme, die anfällige Senke, den erreichbaren Pfad und die unterstützte
Sicherheitsgrenze. Codex erfasst stützende Belege, gegen die Behauptung sprechende Belege und
Nachweislücken.

4. Einstufungen und Ränge zuweisen

   Codex weist jedem Befund eine Einstufung und ein Konfidenzniveau zu. Codex ordnet
Befunde mit dem Status `confirmed` oder `needs_review` in getrennten Warteschlangen nach Ausnutzbarkeit.

## Ergebnisse prüfen

| Einstufung          | Bedeutung                                                                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `confirmed`      | Die Belege im Repository zeigen, dass der Pfad zur Schwachstelle unter den genannten Vorbedingungen erreichbar ist und eine unterstützte Sicherheitsgrenze überschreitet.                     |
| `not_actionable` | Die Belege im Repository widerlegen die Behauptung, etwa indem sie eine nicht betroffene Version, einen nicht erreichbaren Pfad, eine wirksame Schutzmaßnahme oder einen Produktbereich aufzeigen, der nicht ausgeliefert wird.                 |
| `needs_review`   | Die Belege im Repository reichen für eine Entscheidung nicht aus, weil erforderliche Informationen fehlen, uneindeutig sind oder von der Laufzeit, der Umgebung oder von Richtlinien abhängen. |

  Ränge nach Ausnutzbarkeit werden mit positiven Ganzzahlen ab `1` vergeben, jeweils unabhängig
  innerhalb der Warteschlange für die jeweilige Einstufung. So bleiben die Prioritäten für Behebungsmaßnahmen von
  noch offenen Prüfarbeiten getrennt. Rang `1` bezeichnet in dieser Ergebnismenge den am leichtesten ausnutzbaren Befund mit dem Status `confirmed`
  oder den Befund mit dem Status `needs_review`, dessen Prüfung höchste Priorität hat. Der Rang
  ist kein vom Scanner vergebener Schweregradwert. Befunde mit dem Status `not_actionable` erhalten keinen Rang.

Prüfe für jeden Befund:

- die Begründung für die Einstufung und den Rang
- stützende Belege sowie Belege, die gegen die Behauptung sprechen
- offene Fragen und verbleibende Nachweislücken
- die betroffene Stelle und Komponente
- den Produktbereich und die Vertrauensstufe der Quelle
- den empfohlenen nächsten Schritt
- die Übergabe an [`$codex-security:fix-finding`](/de-DE/codex/security/plugin/fix-findings)
  für einen Befund mit dem Status `confirmed`

Die Triage ist abgeschlossen, wenn für jeden angegebenen Befund genau ein Ergebnis vorliegt, Codex
die jeweilige Quellkennung beibehält und jede Unsicherheit ausdrücklich benannt ist. Einträge in Jira, Linear und anderen
Backlogs bleiben unverändert, sofern du Codex nicht nach der Prüfung der Triage-Ergebnisse
anweist, Änderungen zurückzuschreiben.

## Nächste Schritte

- `confirmed`: Nachdem eine Person den Befund zur Behebung freigegeben hat, verwende
[`$codex-security:fix-finding`](/de-DE/codex/security/plugin/fix-findings), um ihn zu beheben und
  zu verifizieren. Die Triage bereitet eine direkt als Prompt nutzbare Übergabe vor, ruft den Skill aber nicht
  automatisch auf.
- `needs_review`: Wenn sich die Nachweislücke durch Ausführen des Codes schließen lässt, verwende
`$codex-security:validation` für eine klar abgegrenzte dynamische Validierung. Übergib
  die im Befund erhobene Behauptung, betroffene Stellen, Vorbedingungen, statische Belege und
  Nachweislücken aus dem Triage-Ergebnis:

  ```text
  Use $codex-security:validation to dynamically validate finding [triage item ID or source ID] from the backlog triage result. Use the strongest realistic, bounded method, record exactly what was tested, and preserve any remaining proof gaps.

  Im Gegensatz zur Triage kann Codex bei der Validierung Code kompilieren oder ausführen, einen gezielten Test oder
  Proof of Concept erstellen oder eine echte Schnittstelle testen. Prüfe die vorgeschlagenen Befehle,
  bevor du sie genehmigst, und behalte die [Genehmigungs- und Sicherheitsrichtlinien
  von Codex](/de-DE/codex/agent-approvals-security) bei.

- `needs_review`: Wenn der Befund von Produktrichtlinien oder vom Bereitstellungskontext
  abhängt, beantworte die aufgeführten offenen Fragen, bevor du Code änderst.
- `not_actionable`: Bewahre die Belege zusammen mit dem Triage-Eintrag auf. Codex schließt das Ausgangsticket nicht automatisch und
  aktualisiert es auch nicht.
- Um über den angegebenen Backlog hinaus nach Schwachstellen zu suchen, [führe einen
  Sicherheitsscan aus](/de-DE/codex/security/plugin/scans).

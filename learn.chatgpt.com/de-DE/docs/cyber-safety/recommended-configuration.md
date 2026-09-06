<!-- source: https://learn.chatgpt.com/de-DE/docs/cyber-safety/recommended-configuration -->

Welche Sicherheitsmaßnahmen für einen Arbeitsablauf im Bereich Cybersicherheit angemessen sind, hängt vom Modell, den Aktionen, die es ausführen kann, den Systemen, auf die es zugreifen kann, und der Sensibilität der betroffenen Daten ab.

Für die meisten Daybreak Blue-Arbeitsabläufe reichen die etablierten Sicherheitsmaßnahmen deiner Organisation möglicherweise aus, etwa Zugriffskontrollen, der Schutz von Anmeldedaten und die Überprüfung sensibler Aktionen.

Bei Daybreak Red-Arbeitsabläufen, autonomen Sicherheitstests und Aktivitäten, die Produktionssysteme, sensible Daten oder externe Tools einbeziehen, sind möglicherweise stärkere Schutzmaßnahmen erforderlich. Die folgenden Empfehlungen richten sich in erster Linie an diese Szenarien mit höherem Risiko.

  Du bist dafür verantwortlich, die Risiken deines konkreten Arbeitsablaufs zu bewerten und
geeignete Sicherheitsmaßnahmen umzusetzen. Schutzmechanismen des Modells und Trusted
Access ersetzen nicht die Sicherheits-, Überwachungs- und
Aufsichtsverfahren deiner Organisation.

Trusted Access regelt den genehmigten Zugriff auf Modelle, konfiguriert aber nicht deine Umgebung und setzt auch keine Beschränkungen für genehmigte Systeme und Aktionen durch. Dein Team muss geeignete Kontrollen für Isolation, Berechtigungen, Überprüfung, Überwachung und menschliche Aufsicht einrichten. Gehe davon aus, dass das Modell, seine Tools und jedes verbundene System kompromittiert sein könnten. Konfiguriere die Umgebung dann so, dass sie selbst in diesem Fall weder auf nicht autorisierte Systeme zugreifen noch Anmeldedaten offenlegen, Schutzmechanismen deaktivieren oder über das Ende der Arbeit hinaus aktiv bleiben können.

## Umgebung isolieren

Führe offensive Sicherheitsaufgaben in einem dedizierten Labor oder einer Sandbox aus. Beginne ohne uneingeschränkten Internetzugang sowie ohne Zugriff auf sensible Produktionssysteme, Unternehmensnetzwerke, nicht zugehörige Workloads oder Schnittstellen zur Host-Verwaltung. Halte Geheimnisse, Anmeldedaten, Möglichkeiten für dauerhaften Zugriff und dauerhafte Systemänderungen außer Reichweite, sofern dies für die genehmigte Arbeit nicht ausdrücklich erforderlich und autorisiert ist.

Nutze für jeden Versuch mit höherem Risiko oder reduzierten Schutzmechanismen eine neue, stark isolierte Umgebung. Trenne Rechenressourcen, Speicher, Netzwerk und Identitäten voneinander und lösche die Umgebung anschließend, anstatt sie zurückzusetzen oder wiederzuverwenden.

Teste vor Beginn von Arbeiten mit höherem Risiko die Grenzen des Dateisystems und Netzwerks. Beziehe alle erreichbaren Hosts, verbundenen Tools, delegierten Agenten und nachgelagerten Dienste ein. Halte die Host-Umgebung auch dann isoliert, wenn das Modell oder die Prüfinstanz eine einzelne Aktion genehmigt.

## Genehmigte Rahmenbedingungen definieren und durchsetzen

Dokumentiere vor dem Start des Modells, welche Systeme, Tools, Aktionen und Zeitlimits für deine Arbeit genehmigt sind. Halte Folgendes fest:

- Genehmigte Zielsysteme, Hosts und Umgebungen.
- Ausgeschlossene Systeme, darunter Produktionssysteme und nicht zugehörige Infrastruktur.
- Genehmigte Tools und verbundene Dienste.
- Genehmigte und verbotene Aktionen.
- Genehmigte Start- und Endzeiten sowie Vorgaben zum Umgang mit Daten.
- Offenlegung von Sicherheitslücken, Genehmigung von Patches und Abstimmung mit dem zuständigen Wartungsteam.
- Abbruchbedingungen und Aktionen, die ausdrücklich von einer Person genehmigt werden müssen.

Stelle dem Agenten diese genehmigten Rahmenbedingungen als Aufgabenkontext bereit. Ihre Dokumentation allein setzt sie nicht durch: Nutze unabhängige Kontrollen für Dateisystem, Netzwerk, Identitäten und Tools, um nicht autorisierte Aktionen technisch unmöglich zu machen, wann immer dies praktikabel ist.

Verwende die [Berechtigungsprofile](/de-DE/codex/permissions) von Codex, um eine Grenze nach dem Prinzip der geringsten Rechte zu schaffen. Wähle `:read-only`, wenn für die Aufgabe keine Änderungen erforderlich sind, oder erweitere `:workspace`, wenn Änderungen im Workspace nötig sind. Beispiel:

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = "cyber-lab"

[features]
network_proxy = true

[permissions.cyber-lab]
description = "Limit security testing to the approved lab and workspace."
extends = ":workspace"

[permissions.cyber-lab.filesystem]
glob_scan_max_depth = 3

[permissions.cyber-lab.filesystem.":workspace_roots"]
"**/.env*" = "deny"
"**/*.pem" = "deny"

[permissions.cyber-lab.network]
enabled = true
# Uncomment only for an approved host that resolves to a private address.
# allow_local_binding = true

[permissions.cyber-lab.network.domains]
"lab.example.com" = "allow"

Die Funktion `network_proxy` erzwingt die Beschränkung auf die genehmigte Domain. Ohne sie
ermöglicht `network.enabled = true` direkten Netzwerkzugriff, und die Zulassungsliste des Labors
beschränkt die Ziele nicht. Websuche, Apps, Konnektoren, MCP-Server,
Browseraktivitäten und Codex Cloud verwenden jeweils eigene Kontrollen. Schränke alle Funktionen ein
oder deaktiviere sie, wenn sie für den genehmigten Arbeitsablauf nicht erforderlich sind.

Ersetze `lab.example.com` durch ein genehmigtes Ziel. Die begrenzte Dateisystemsuche soll verhindern, dass unter Linux, WSL und Windows der gesamte Workspace durchsucht wird. Erhöhe die Tiefe oder verwende genaue Pfade für Ausschlüsse, wenn sensible Dateien in tieferen Ebenen liegen. Kombiniere Berechtigungsprofile nicht mit veralteten Einstellungen für `sandbox_mode`, sondern folge den [Konfigurationshinweisen für Berechtigungsprofile](/de-DE/codex/permissions#define-and-select-a-profile).

Wenn die Namensauflösung für den genehmigten Lab-Host eine private Adresse ergibt, blockiert Codex ihn standardmäßig, selbst wenn der Host auf der Zulassungsliste steht. Lege `allow_local_binding = true` nur für ausdrücklich genehmigte Arbeiten in privaten Netzwerken fest, beschränke die Zulassungsliste für Ziele auf das Nötigste und beachte die [Hinweise zu lokalen und privaten Netzwerken](/de-DE/codex/permissions#local-and-private-networks). Du kannst auch genau die genehmigte private IP-Adresse in die Zulassungsliste aufnehmen.

Blockiere standardmäßig den Zugriff auf das offene Internet und auf Produktionsnetzwerke. Wenn externer Zugriff erforderlich ist, leite ihn über ein separat kontrolliertes Gateway oder einen separat kontrollierten Proxy und nutze eng gefasste Zulassungslisten, die Prüfung von Anfragen und Protokollierung. Wende dieselben Einschränkungen auf indirekte Verbindungen über Paketmanager, Webhooks, Dienste zum Abrufen von URLs, Weiterleitungen, Cloud-APIs und verbundene Tools an. Lade Abhängigkeiten vor der Ausführung oder verwende von der Administration genehmigte Abhängigkeiten.

## Anmeldedaten und sensible Daten schützen

Lege wiederverwendbare API-Schlüssel, Cloud-Anmeldedaten, Passwörter und Dienstkonto-Token nicht in Prompts, Repositories, Umgebungsvariablen, gemeinsam genutzten Dateisystemen oder Protokollen ab, auf die das Modell zugreifen kann. Wenn eine Authentifizierung erforderlich ist, stelle über einen separaten Broker oder ein Gateway kurzlebige Anmeldedaten bereit, die genau auf das Ziel und die zulässige Aktion beschränkt sind, ohne sie dem Modell offenzulegen.

Stelle nur die Daten bereit, die für die genehmigte Aufgabe erforderlich sind. Entferne unnötige sensible Informationen, sperre den Zugriff auf Cloud-Metadaten und Endpunkte für Anmeldedaten und behandle vom Modell erzeugte Dateien als nicht vertrauenswürdig.

Vermeide `:danger-full-access` und `--yolo` in Arbeitsabläufen für Cybersicherheit. Vollzugriff hebt die durchsetzbare Sandbox-Grenze auf, die für die automatische Überprüfung erforderlich ist. Verwaltete Organisationen können `:danger-full-access` und `--yolo` ausschließen, die zulässigen Genehmigungsrichtlinien begrenzen und über eine [unternehmensweit verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration#configure-automatic-review-policy) die automatische Überprüfung vorschreiben.

Bevor du **Vollzugriff** für ein genehmigtes Sicherheitsmodell aktivierst, zeigt die ChatGPT-Desktop-App eine modellspezifische Warnung vor gefährlichen Aktionen an. Die Warnung empfiehlt stattdessen die Option **Für mich genehmigen** und verweist auf die [Konfiguration der Prüfrichtlinie](/de-DE/codex/sandboxing/auto-review#configuration). Sie stellt die Sandbox-Grenze nicht wieder her und setzt die Organisationsrichtlinie nicht außer Kraft.

Schutzmechanismen ergänzen einen kontrollierten Arbeitsablauf für Cybersicherheit um eine richtlinienbasierte Überprüfung. Sie ersetzen weder die Isolation der Umgebung noch Berechtigungen nach dem Prinzip der geringsten Rechte, klar definierte Grenzen, Überwachung oder menschliche Aufsicht.

## Sensible Codex-Aktionen überprüfen

Die [Automatische Überprüfung](/de-DE/codex/sandboxing/auto-review) leitet dafür vorgesehene Genehmigungsanfragen an der Sandbox-Grenze vor Ausführung der vorgeschlagenen Aktion an eine separate Prüfinstanz weiter. Die Prüfinstanz berücksichtigt die vorgeschlagene Aktion, den klar abgegrenzten Aufgabenkontext und die geltende Richtlinie und genehmigt die Anfrage oder lehnt sie ab. Organisationen können diese Richtlinie an ihre genehmigten Ziele, verbotenen Aktionen und Bedingungen anpassen, unter denen eine menschliche Überprüfung erforderlich ist.

Verlange eine ausdrückliche Genehmigung durch eine Person für Aktionen, die Produktivsysteme, externe Systeme, sensible Daten, Rechteausweitungen, dauerhaften Zugriff oder unumkehrbare Änderungen betreffen. Behandle Anweisungen, die in Websites, Repositories, Dokumente und Tool-Ausgaben eingebettet sind, als nicht vertrauenswürdig. Sie können den autorisierten Geltungsbereich weder erweitern noch Zugriffskontrollen außer Kraft setzen.

Wenn du in der ChatGPT-Desktop-App ein genehmigtes Daybreak-Modell auswählst, wird die Berechtigungsauswahl automatisch auf **Für mich genehmigen** gestellt, sofern dieser Modus für dein Konto verfügbar ist und die Organisationsrichtlinie ihn zulässt. Das gilt auch, wenn du in der Desktop-App den Befehl `/model` verwendest. Ist der Modus nicht verfügbar, bleibt der aktuelle Berechtigungsmodus unverändert. Die Modellauswahl setzt zentral verwaltete Vorgaben deiner Organisation niemals außer Kraft.

Damit die automatische Überprüfung ausgeführt werden kann, müssen alle drei Vorkehrungen bestehen bleiben:

1. Verwende eine interaktive Genehmigungsrichtlinie wie `approval_policy = "on-request"`.
2. Lege `approvals_reviewer = "auto_review"` fest.
3. Behalte eine durchsetzbare Begrenzung durch eine Sandbox oder ein Berechtigungsprofil bei.

Anfragen an ein Ziel auf der Netzwerk-Zulassungsliste bleiben innerhalb der Netzwerkgrenze und lösen nicht automatisch eine automatische Überprüfung aus. Damit ein sensibler Befehl auch dann überprüft wird, wenn sein Ziel auf der Zulassungsliste steht, erstelle unter `~/.codex/rules/` eine explizite [Befehlsregel](/de-DE/codex/agent-configuration/rules):

```python
prefix_rule(
    pattern = ["curl"],
    decision = "prompt",
    justification = "Review requests to the approved cybersecurity target.",
)

Starte Codex neu, nachdem du die Regel hinzugefügt hast. Mit `approvals_reviewer = "auto_review"` werden übereinstimmende Befehle vor ihrer Ausführung an die Prüfinstanz weitergeleitet. Füge für jeden sensiblen Befehl entsprechende Prompt-Regeln hinzu oder verwende `approval_mode = "prompt"` für einzelne [MCP-Tools](/de-DE/codex/extend/mcp). Aktionen, bei denen eine Person entscheiden muss, müssen weiterhin ausdrücklich durch eine Person genehmigt werden.

Die automatische Überprüfung erfasst keine Routineaktionen, die innerhalb der Sandbox bereits zulässig sind. Bei `approval_policy = "never"` oder Vollzugriff erzeugt eine sensible Aktion möglicherweise keine überprüfbare Genehmigungsanfrage. Die automatische Überprüfung kann Fehler machen und ersetzt weder Isolation, klar definierte Grenzen und Überwachung noch eine ausdrückliche menschliche Aufsicht.

Informationen zu einer Richtlinie mit klar begrenztem Geltungsbereich und ihrer organisationsweiten Durchsetzung findest du unter [Einen autorisierten Arbeitsablauf für Cybersicherheit konfigurieren](/de-DE/codex/sandboxing/auto-review#configure-an-authorized-cybersecurity-engagement).

## Unabhängig überwachen und bei Ausfällen sicher abbrechen

Protokolliere Modellanfragen, Tool-Aufrufe, Netzwerkaktivitäten, die Nutzung von Anmeldedaten und sicherheitsrelevante Änderungen. Bewahre Protokolle und Überwachungssysteme außerhalb der vom Modell kontrollierten Umgebung auf. Löse Warnmeldungen bei nicht autorisierten Zielen, unerwarteten Netzwerkanfragen, offengelegten Anmeldedaten, Richtlinienänderungen, fehlenden Protokollen und Versuchen zur Umgehung von Schutzmechanismen aus.

Halte die Durchsetzung von Richtlinien, Broker für Anmeldedaten, Prüfsysteme und Notabschaltmechanismen unabhängig vom Agenten. Stoppe den Arbeitsablauf, wenn eine wesentliche Kontrolle oder ein Überwachungssystem ausfällt.

## Benutzerdefinierte Agenten-Arbeitsabläufe um Schutzmechanismen ergänzen

Wenn du mit der Responses API, dem Agents SDK oder einem anderen Harness entwickelst, füge unmittelbar vor der Tool-Ausführung eine Überprüfung hinzu. Gleiche vorgeschlagene sensible Aktionen vor der Ausführung mit den genehmigten Systemen, Aktionen und Zeitlimits ab, lege mehrdeutige oder risikoreiche Aktionen einer Person zur Entscheidung vor, setze unabhängige Dateisystem- und Netzwerkbeschränkungen durch, führe Auditprotokolle und verweigere die Ausführung, wenn die Prüfinstanz oder Richtlinie nicht verfügbar ist.

Die automatische Überprüfung von Codex schützt benutzerdefinierte Tools oder externe Harnesses nicht automatisch. Verwende für das Agents SDK-Muster [Schutzmechanismen und menschliche Überprüfung](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution) und nutze die [quelloffene Prüfrichtlinie](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md) als Referenz.

Das produktseitige Sandboxing und die produktseitige Überprüfung von Codex sind von den [API-Prüfungen für Cybersicherheit](/api/docs/guides/safety-checks/cybersecurity) getrennt. API-Schutzmechanismen können Fehler des Typs `cyber_policy` zurückgeben, und nutzerbezogene Werte für `safety_identifier` können dazu beitragen, die Auswirkungen einer Schutzmaßnahme zu begrenzen.

## Bereinigen und Ergebnisse validieren

Widerrufe nach Abschluss der Arbeit temporäre Anmeldedaten, beende Hintergrundprozesse, entferne dauerhafte Zugriffsmöglichkeiten und lösche Umgebungen mit höherem Risiko vollständig. Stelle sicher, dass Callbacks, offengelegte Artefakte, gemeinsam genutzte Zustände und laufübergreifende Zugriffe vollständig entfernt sind, und halte verschiedene Benutzerkonten, Sitzungen und Evaluierungen voneinander isoliert.

Validiere Befunde, bevor du auf ihrer Grundlage handelst, halte dich an Verfahren zur koordinierten Offenlegung und stelle sicher, dass Menschen für Behebungsmaßnahmen und Änderungen verantwortlich bleiben.

## Bevor du beginnst

Bestätige die genehmigten Systeme und Aktionen, das geeignete Modell, die isolierte Umgebung, Berechtigungen nach dem Prinzip der geringsten Rechte, den beschränkten Netzwerkzugriff, geschützte Anmeldedaten, die Überprüfung von Aktionen, unabhängige Überwachung, die Notabschaltung und den Bereinigungsplan. Schutzmechanismen des Modells, Isolation, klar begrenzte Berechtigungen, die Überprüfung von Aktionen, Überwachung und menschliche Aufsicht ergänzen einander. Keine davon sollte als einzige Kontrollmaßnahme dienen.

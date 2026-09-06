<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/skills -->

Skills sind wiederverwendbare Arbeitsabläufe, die aus Anweisungen und zugehörigen Ressourcen bestehen.
Für Skills im ChatGPT-Workspace, Dateisystem-Skills, die von den betreffenden lokalen Funktionen
in der ChatGPT-Desktop-App, der Codex CLI oder der IDE-Erweiterung verwendet werden, sowie für Plug-ins, die
Skills bündeln, gibt es jeweils eigene Funktionen zur Lebenszyklus- und Zugriffsverwaltung.

Das vollständige Administrationsmodell findest du unter
[Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions).

<a id="distinguish-the-distribution-models"></a>

## Verteilung und Administration von Skills

| Verteilungsmodell      | Verwendungszweck                                                                                           | Zuständige Verwaltungsebene                                                                       |
| ----------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Skill im ChatGPT-Workspace | Freigeben oder Installieren eines genehmigten Arbeitsablaufs mithilfe unterstützter Funktionen im ChatGPT-Workspace              | Berechtigungen und Funktionen zur Lebenszyklusverwaltung für Skills im ChatGPT-Workspace                                    |
| Lokaler Dateisystem-Skill  | Laden eines installierten Arbeitsablaufs aus einem Repository, einem persönlichen Verzeichnis, einem von der Administration verwalteten Verzeichnis oder einem mitgelieferten Systemverzeichnis     | Verteilung über das Dateisystem, Konfiguration des lokalen Clients und Laufzeitberechtigungen                  |
| Plug-in                  | Bündeln eines oder mehrerer Skills mit optionalen Konnektoren, MCP-Servern, Hooks und Metadaten für die Darstellung | Verfügbarkeit und Installation des Plug-ins sowie separate Verwaltungsoptionen für jede enthaltene Funktion |

Die Verteilung von Skills im ChatGPT-Workspace, die Installation lokaler Dateisystem-Skills und
 die Installation von Plug-ins für die jeweilige Oberfläche sind voneinander getrennte Verfahren. Beim Verschieben eines Skills werden
 die Eigentümerschaft, Freigaben und Rollenzuweisungen im ChatGPT-Workspace, der
 Installationsstatus von Plug-ins oder die Autorisierung von Konnektoren nicht mitübertragen.

Plug-ins lassen sich in Chat und Work in ChatGPT im Web, auf dem Desktop und auf Mobilgeräten verwenden,
in Codex in der ChatGPT-Desktop-App sowie über den Plug-in-Browser der Codex CLI.
In der IDE-Erweiterung sind sie nicht verfügbar.
Diese unterstützten Oberflächen beziehen öffentliche Plug-ins aus einem einzigen universellen Verzeichnis,
das ChatGPT und Codex gemeinsam nutzen.

## Zuständige Verwaltungsebenen

Unter [Skills erstellen](/de-DE/codex/build-skills) findest du Informationen zu Speicherorten im Dateisystem und zum Erstellen von Skills,
unter [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
zu aktuellen Abläufen im Workspace und unter [Plug-ins erstellen](https://developers.openai.com/plugins/build/plugins) zur
Paketierung von Plug-ins.

Über die Verwaltungsfunktionen im ChatGPT-Workspace werden weder lokale Dateisystem-Skills noch Plug-ins installiert.
Bei der Verteilung über das Dateisystem werden weder Eigentümerschaft noch Rollen im ChatGPT-Workspace zugewiesen.
Durch die Installation eines Plug-ins erhältst du keinen Zugriff auf einen Konnektor, einen MCP-Server oder
einen verbundenen Dienst. Konfiguriere jede Funktion über die Verwaltungsoberfläche, die
dafür zuständig ist.

## Weitere Dokumentation

- [Skills und Plug-ins](/de-DE/codex/skills-and-plugins)
- [Plug-ins](/de-DE/codex/plugins)
- [Skills erstellen](/de-DE/codex/build-skills)
- [Plug-ins erstellen](https://developers.openai.com/plugins/build/plugins)
- [Rollout-Leitfaden für die Administration](/de-DE/codex/enterprise/admin-setup)
- [Verwaltung von Plug-ins](/de-DE/codex/enterprise/apps-and-connectors)

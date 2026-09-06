<!-- source: https://learn.chatgpt.com/de-DE/use-cases/update-documentation -->

## Einführung

Dokumentation lässt sich am einfachsten aktuell halten, wenn sie zusammen mit Änderungen am Quellcode aktualisiert wird und nicht erst Wochen später. Codex kann geänderten Code, Tests, Versionshinweise, verknüpfte Issues und den Kontext von Pull Requests prüfen und anschließend eine gezielte Aktualisierung der Dokumentation entwerfen, die zur bestehenden Struktur passt.

Nutze diesen Arbeitsablauf für Entwicklerdokumentation, README-Aktualisierungen, Entwürfe für Änderungsprotokolle, Migrationshinweise, Runbooks und alles andere, was häufige Verhaltensänderungen berücksichtigen muss.

## So gehst du vor

1. Beginne mit der Änderung, die du dokumentieren musst.

   Stelle den Branch, den Pull Request, den Commit, das Issue oder die Dateien bereit. Wenn die Dokumentation öffentlich ist, sage ausdrücklich, dass unveröffentlichte Roadmap-Inhalte, vertrauliche Kundeninformationen und rein interner Kontext nicht aufgenommen werden dürfen.

2. Bitte Codex, die betroffenen Dokumentationsseiten zu ermitteln.

   Lass Codex die bestehende Dokumentation vor dem Entwurf nach Funktionsnamen, Konfigurationsschlüsseln, Befehlen, Beispielen und verwandten Begriffen durchsuchen.

3. Beschränke die Aktualisierung auf den kleinsten sinnvollen Teil der Dokumentation.

   Codex sollte die aktuelle Seitenstruktur, Terminologie, Querverweise und Frontmatter beibehalten. Wenn die gezielte Aktualisierung eines Hinweises, Beispiels oder Abschnitts ausreicht, sollte Codex keine umfassenden Überarbeitungen vornehmen.

4. Prüfe die Änderungen.

   Bitte Codex, die zum Repository passenden Formatierungs- und Dokumentationsprüfungen auszuführen. Lass Codex anschließend zusammenfassen, welche Belege jede für Nutzende relevante Aussage stützen.

## Was du Codex bereitstellen solltest

| Quelle                               | Warum das hilft                                                               |
| ------------------------------------ | -------------------------------------------------------------------------- |
| Änderungen an Code und Tests               | Damit kann Codex das tatsächliche Verhalten analysieren und gezielte Aktualisierungen der Dokumentation entwerfen. |
| Öffentliche Versionshinweise oder Produktdokumentation | Hilft Codex, sich bei Terminologie, Verfügbarkeit und Funktionsstatus an den öffentlichen Angaben zu orientieren.    |
| Kontext eines Pull Requests oder Issues        | Erklärt, warum die Änderung vorgenommen wurde und welches für Nutzende sichtbare Verhalten relevant ist.   |
| Lokale Dokumentationsprüfungen                    | Gibt Codex konkrete Kriterien, die vor der Veröffentlichung der Dokumentation erfüllt sein müssen.   |

Mit zusätzlichem Kontext wie öffentlichen Versionshinweisen kann Codex vermeiden, vertrauliche Informationen oder noch nicht veröffentlichte Aktualisierungen aufzunehmen.

## Arbeitsablauf wiederholbar machen

Um eine Konvention für das gesamte Repository festzulegen, trage die Vorgaben zur Dokumentation in [AGENTS.md](/de-DE/codex/agent-configuration/agents-md) ein. Beispiel:

```md
## Documentation

- When user-facing behavior changes, check whether docs, examples, or changelogs need updates.
- Public docs must only include public information or behavior visible in this repo.
- Preserve existing terminology and frontmatter.
- Run the docs formatting and build checks before final handoff.

Wenn der Prozess weitere Schritte umfasst, erstelle daraus einen [Skill](/de-DE/codex/build-skills). So können künftige Codex-Aufgaben demselben Ablauf aus Quellenprüfung, Entwurf und Verifizierung folgen. Weitere Informationen zu diesem Muster findest du unter [Arbeitsabläufe als Skills speichern](/de-DE/codex/use-cases/reusable-codex-skills).

Du kannst auch [direkt aus dem aktuellen Chat eine Aufgabe für diesen Arbeitsablauf planen](/de-DE/codex/automations#schedule-a-task-inside-a-chat). Bitte Codex beispielsweise, jede Woche die neuesten Pull Requests auf GitHub abzurufen und die Dokumentation aktuell zu halten:

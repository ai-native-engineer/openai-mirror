<!-- source: https://learn.chatgpt.com/de-DE/docs/open-source -->

OpenAI entwickelt zentrale Teile von Codex als Open Source. Die Entwicklung findet auf GitHub statt. Dort kannst du Fortschritte verfolgen, Probleme melden und Verbesserungen beisteuern.

Wenn du ein weitverbreitetes Open-Source-Projekt pflegst oder Personen vorschlagen möchtest, die wichtige Projekte betreuen, kannst du dich außerdem [für das Programm Codex for OSS bewerben](/community/codex-for-oss) und API-Credits, ChatGPT Pro mit Codex sowie in ausgewählten Fällen Zugriff auf Codex Security erhalten.

## Open-Source-Komponenten

| Komponente                     | Speicherort                                                                                             | Hinweise                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Codex CLI                     | [openai/codex](https://github.com/openai/codex)                                                           | Zentrale Anlaufstelle für die Open-Source-Entwicklung von Codex      |
| Codex SDK                     | [openai/codex/codex-sdk](https://github.com/openai/codex/tree/main/sdk)                                   | Der SDK-Quellcode befindet sich im Codex-Repository                      |
| Codex Security CLI            | [openai/codex-security](https://github.com/openai/codex-security)                                         | CLI zum Ermitteln und Validieren von Sicherheitslücken |
| Codex Security TypeScript SDK | [openai/codex-security/sdk/typescript](https://github.com/openai/codex-security/tree/main/sdk/typescript) | TypeScript SDK zum Ausführen von Scans mit Codex Security         |
| Codex App Server              | [openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)         | Der Quellcode für den App Server befindet sich im Codex-Repository               |
| Skills                        | [openai/skills](https://github.com/openai/skills)                                                         | Wiederverwendbare Skills, die ChatGPT und Codex erweitern           |
| Plug-ins                       | [openai/plugins](https://github.com/openai/plugins)                                                       | Wiederverwendbare Plug-ins für ChatGPT und Codex                  |
| IDE-Erweiterung                 | -                                                                                                         | Nicht als Open Source verfügbar                                         |
| Codex Cloud                   | -                                                                                                         | Nicht als Open Source verfügbar                                         |
| Universelle Cloud-Umgebung   | [openai/codex-universal](https://github.com/openai/codex-universal)                                       | Codex Cloud verwendet diese Basisumgebung                    |

## Wo du Probleme melden und Funktionswünsche einreichen kannst

Verwende für Fehlerberichte und Funktionswünsche das passende GitHub-Repository:

- Fehlerberichte und Funktionswünsche für Codex: [openai/codex/issues](https://github.com/openai/codex/issues)
- Fehlerberichte und Funktionswünsche für die Codex Security CLI und das TypeScript SDK: [openai/codex-security/issues](https://github.com/openai/codex-security/issues)
- Diskussionsforum: [openai/codex/discussions](https://github.com/openai/codex/discussions)

Wenn du ein Issue erstellst, gib die verwendete Komponente (CLI, SDK, IDE-Erweiterung, Codex Cloud oder Codex Security) und nach Möglichkeit deren Version an.

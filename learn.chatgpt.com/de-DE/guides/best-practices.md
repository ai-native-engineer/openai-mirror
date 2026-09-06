<!-- source: https://learn.chatgpt.com/de-DE/guides/best-practices -->

Wenn du Codex oder Coding-Agenten im Allgemeinen noch nicht kennst, hilft dir dieser Leitfaden, schneller bessere Ergebnisse zu erzielen. Er beschreibt die wichtigsten Gewohnheiten, mit denen du Codex in der [CLI](/de-DE/codex/cli), der [IDE-Erweiterung](/de-DE/codex/ide) und der [ChatGPT-Desktop-App](/de-DE/codex/app) effektiver nutzt: vom Prompting und Planen über die Validierung bis hin zu MCP, Skills und geplanten Aufgaben.

Codex funktioniert am besten, wenn du es weniger als Assistenten für einzelne Aufgaben und mehr als Teammitglied betrachtest, das du im Laufe der Zeit konfigurierst und verbesserst.

Ein hilfreicher Ansatz: Stelle zuerst den richtigen Kontext für die Aufgabe bereit, nutze `AGENTS.md` für dauerhafte Anweisungen, stimme Codex auf deinen Arbeitsablauf ab, binde externe Systeme über MCP an, überführe wiederkehrende Aufgaben in Skills und automatisiere stabile Arbeitsabläufe.

## Erfolgreich starten: Kontext und Prompts

Codex ist bereits so leistungsfähig, dass es auch dann nützlich ist, wenn dein Prompt nicht perfekt ist. Oft kannst du Codex mit minimalem Setup ein schwieriges Problem übergeben und trotzdem ein gutes Ergebnis erhalten. Klares [Prompting](/de-DE/codex/prompting) ist keine Voraussetzung für brauchbare Ergebnisse, macht sie aber verlässlicher, insbesondere bei größeren Codebasen oder besonders wichtigen Aufgaben.

Wenn du in einem großen oder komplexen Repository arbeitest, erreichst du am meisten, indem du Codex den passenden Kontext für die Aufgabe gibst und klar strukturierst, was es erledigen soll.

Im Normalfall sollte dein Prompt vier Angaben enthalten:

- **Ziel:** Was möchtest du ändern oder entwickeln?
- **Kontext:** Welche Dateien, Ordner, Dokumentationen, Beispiele oder Fehler sind für diese Aufgabe relevant? Du kannst bestimmte Dateien mit @ erwähnen und so als Kontext einbinden.
- **Vorgaben:** Welche Standards, Architekturvorgaben, Sicherheitsanforderungen oder Konventionen soll Codex einhalten?
- **Abgeschlossen, wenn:** Welche Bedingungen müssen erfüllt sein, bevor die Aufgabe als abgeschlossen gilt, etwa erfolgreiche Tests, ein geändertes Verhalten oder ein Fehler, der sich nicht mehr reproduzieren lässt?

So bleibt Codex auf die Aufgabe fokussiert, trifft weniger Annahmen und liefert Ergebnisse, die sich leichter überprüfen lassen.

Wähle den Reasoning-Aufwand passend zum Schwierigkeitsgrad der Aufgabe und teste, was für deinen Arbeitsablauf am besten funktioniert. Welche Einstellung am besten funktioniert, hängt von der Person und der Aufgabe ab.

- Niedrig für schnellere, klar abgegrenzte Aufgaben
- Mittel oder Hoch für komplexere Änderungen oder Debugging
- Sehr hoch für länger dauernde agentische Aufgaben mit hohem Reasoning-Aufwand

  Um Kontext schneller bereitzustellen, kannst du in der ChatGPT-
Desktop-App die Diktierfunktion verwenden und einsprechen, was Codex tun soll, statt es einzutippen.

## Bei schwierigen Aufgaben zuerst planen

Wenn die Aufgabe komplex, mehrdeutig oder schwer zu beschreiben ist, bitte Codex, einen Plan zu erstellen, bevor es mit dem Programmieren beginnt.

Diese Ansätze funktionieren gut:

**Planmodus verwenden:** Für die meisten ist das die einfachste und effektivste Option. Im Planmodus kann Codex Kontext zusammentragen, Rückfragen stellen und vor der Umsetzung einen fundierteren Plan erstellen. Schalte ihn mit `/plan` oder <kbd>Shift</kbd>+<kbd>Tab</kbd> um.

**Lass dich von Codex befragen:** Wenn du eine grobe Vorstellung davon hast, was du möchtest, aber nicht weißt, wie du es gut beschreiben sollst, bitte Codex, dir zuerst Fragen zu stellen. Weise es an, deine Annahmen zu hinterfragen und die vage Idee zu konkretisieren, bevor es Code schreibt.

**Eine PLANS.md-Vorlage verwenden:** Für fortgeschrittene Arbeitsabläufe kannst du Codex so konfigurieren, dass es für länger laufende oder mehrstufige Aufgaben entweder `PLANS.md` oder eine Vorlage für Ausführungspläne verwendet. Weitere Einzelheiten findest du im [Leitfaden für Ausführungspläne](/cookbook/articles/codex_exec_plans).

## Anweisungen mit `AGENTS.md` wiederverwendbar machen

Sobald ein Prompting-Muster funktioniert, solltest du es nicht mehr von Hand wiederholen. Genau hier hilft [AGENTS.md](/de-DE/codex/agent-configuration/agents-md) weiter.

Du kannst dir `AGENTS.md` wie eine frei formatierbare README-Datei für Agenten vorstellen. Die Datei wird automatisch in den Kontext geladen und eignet sich am besten, um festzulegen, wie du und dein Team Codex in einem Repository einsetzen möchtet.

Eine gute `AGENTS.md` enthält:

- Repository-Struktur und wichtige Verzeichnisse
- Anleitung zum Ausführen des Projekts
- Build-, Test- und Lint-Befehle
- Entwicklungskonventionen und Anforderungen an PRs
- Einschränkungen und Verbote
- Wann die Arbeit abgeschlossen ist und wie du sie überprüfst

Der Slash-Befehl `/init` in der CLI ist der Schnellstartbefehl, mit dem du im aktuellen Verzeichnis ein Grundgerüst für `AGENTS.md` erstellst. Das ist ein guter Ausgangspunkt. Passe das Ergebnis jedoch daran an, wie dein Team Code tatsächlich erstellt, testet, überprüft und ausliefert.

Du kannst `AGENTS.md` auf unterschiedlichen Ebenen anlegen: als globale `AGENTS.md` mit persönlichen Standardeinstellungen in `~/.codex`, als Datei auf Repository-Ebene für gemeinsame Standards und als spezifischere Dateien in Unterverzeichnissen für lokale Regeln. Befindet sich näher an deinem aktuellen Verzeichnis eine spezifischere Datei, haben deren Anweisungen Vorrang.

Bleib praxisnah. Eine kurze, präzise `AGENTS.md` ist nützlicher als eine lange Datei voller vager Regeln. Beginne mit den Grundlagen und ergänze neue Regeln erst, wenn du feststellst, dass sich Fehler wiederholen.

Wenn `AGENTS.md` zu umfangreich wird, halte die Hauptdatei knapp und verweise für Themen wie Planung, Codeüberprüfung oder Architektur auf aufgabenspezifische Markdown-Dateien.

  Wenn Codex denselben Fehler zweimal macht, bitte es um eine Retrospektive und aktualisiere
`AGENTS.md`. So bleiben die Anweisungen praxisnah und beruhen auf tatsächlichen Problemen.

## Codex für konsistentes Verhalten konfigurieren

Mit der Konfiguration sorgst du vor allem dafür, dass sich Codex über Sitzungen und Oberflächen hinweg konsistenter verhält. Du kannst beispielsweise Standardwerte für Modellauswahl, Reasoning-Aufwand, Sandbox-Modus, Genehmigungsrichtlinie, Profile und MCP-Setup festlegen.

Ein guter Ausgangspunkt ist:

- Speichere persönliche Standardeinstellungen in `~/.codex/config.toml` (**Einstellungen \> Konfiguration \> config.toml öffnen** in der ChatGPT-Desktop-App)
- Lege Repository-spezifisches Verhalten in `.codex/config.toml` fest
- Nutze Überschreibungen über die Kommandozeile nur in Einzelfällen (wenn du die CLI verwendest)

In [`config.toml`](/de-DE/codex/config-file/config-basic) legst du dauerhafte Einstellungen wie MCP-Server, das Multi-Agenten-Setup und Feature-Flags fest. Profilspezifische Überschreibungen werden in separaten Dateien nach dem Muster `$CODEX_HOME/profile-name.config.toml` gespeichert.

Codex verfügt über Sandboxing auf Betriebssystemebene und bietet zwei zentrale Einstellungen, die du steuern kannst. Der Genehmigungsmodus legt fest, wann Codex dich um Erlaubnis bittet, einen Befehl auszuführen. Der Sandbox-Modus bestimmt, ob Codex im Verzeichnis lesen oder schreiben darf und auf welche Dateien der Agent zugreifen kann.

Wenn du Coding-Agenten noch nicht kennst, beginne mit den Standardberechtigungen. Wähle für Genehmigungen und Sandboxing standardmäßig restriktive Einstellungen. Lockere die Berechtigungen erst für vertrauenswürdige Repositorys oder bestimmte Arbeitsabläufe, wenn der Bedarf klar ist.

Beachte, dass CLI, IDE-Erweiterung und ChatGPT-Desktop-App dieselben Konfigurationsebenen verwenden. Weitere Informationen findest du auf der Seite [Beispielkonfiguration](/de-DE/codex/config-file/config-sample).

  Konfiguriere Codex frühzeitig für deine tatsächliche Umgebung. Viele Qualitätsprobleme sind
in Wirklichkeit Setup-Probleme, etwa ein falsches Arbeitsverzeichnis, fehlender Schreibzugriff,
falsche Modellvorgaben oder fehlende Tools und Konnektoren.

## Zuverlässigkeit durch Tests und Überprüfung verbessern

Belasse es nicht dabei, Codex um eine Änderung zu bitten. Bitte Codex auch, bei Bedarf Tests zu erstellen, die relevanten Prüfungen auszuführen, das Ergebnis zu bestätigen und die Arbeit zu überprüfen, bevor du sie akzeptierst.

Codex kann diesen Ablauf für dich übernehmen, aber nur, wenn es weiß, wie ein „gutes“ Ergebnis aussieht. Die entsprechenden Vorgaben können aus dem Prompt oder aus `AGENTS.md` stammen.

Dazu kann Folgendes gehören:

- Tests für die Änderung schreiben oder aktualisieren
- Die passenden Test-Suites ausführen
- Lint-, Formatierungs- oder Typprüfungen ausführen
- Bestätigen, dass das endgültige Verhalten der Anforderung entspricht
- Den Diff auf Fehler, Regressionen oder riskante Muster prüfen

  Blende in der ChatGPT-Desktop-App den Diff-Bereich ein oder aus und [überprüfe
  Änderungen](/de-DE/codex/code-review?surface=app) direkt auf deinem Computer. Klicke auf eine bestimmte Zeile, um
  Feedback zu geben, das Codex bei der nächsten Interaktion als Kontext erhält.

Eine nützliche Option ist hier der Slash-Befehl `/review`, mit dem du Code auf verschiedene Arten überprüfen kannst:

- Code für eine Überprüfung im PR-Stil mit einem Basis-Branch vergleichen
- Nicht committete Änderungen überprüfen
- Einen Commit überprüfen
- Eigene Anweisungen für die Überprüfung verwenden

Wenn du mit deinem Team die Datei `code_review.md` verwendest und in `AGENTS.md` darauf verweist, kann Codex diese Vorgaben auch bei der Überprüfung befolgen. Dieses Muster eignet sich gut für Teams, in denen Überprüfungen für alle Repositorys und Mitwirkenden einheitlich ablaufen sollen.

Codex sollte nicht nur Code generieren. Mit den richtigen Anweisungen kann es auch dabei helfen, **ihn zu testen, zu validieren und zu überprüfen**.

Wenn du GitHub Cloud verwendest, kannst du Codex so einrichten, dass es [Code Reviews für deine PRs ausführt](/de-DE/codex/third-party/github). Bei OpenAI überprüft Codex 100 % der PRs. Du kannst automatische Überprüfungen aktivieren oder bei Bedarf eine Überprüfung auslösen, indem du @Codex erwähnst.

## MCPs für externen Kontext verwenden

Verwende MCPs, wenn sich der von Codex benötigte Kontext außerhalb des Repositorys befindet. Über MCPs kann Codex eine Verbindung zu den Tools und Systemen herstellen, die du bereits nutzt. So musst du aktuelle Informationen nicht immer wieder kopieren und in Prompts einfügen.

[Model Context Protocol](/de-DE/codex/extend/mcp), kurz MCP, ist ein offener Standard, um Codex mit externen Tools und Systemen zu verbinden.

Verwende MCP in folgenden Fällen:

- Der benötigte Kontext befindet sich außerhalb des Repositorys
- Die Daten ändern sich häufig
- Codex soll ein Tool verwenden, statt sich auf hineinkopierte Anweisungen zu verlassen
- Du benötigst eine wiederverwendbare Integration für verschiedene Personen oder Projekte

Codex unterstützt Server mit OAuth sowohl über STDIO als auch über Streamable HTTP.

Gehe in der ChatGPT-Desktop-App zu **Einstellungen \> MCP-Server**, um benutzerdefinierte und empfohlene Server anzuzeigen. Codex kann dir häufig bei der Installation der benötigten Server helfen. Du brauchst Codex nur darum zu bitten. Außerdem kannst du in der CLI den Befehl `codex mcp add` verwenden, um deine benutzerdefinierten Server mit einem Namen, einer URL und weiteren Angaben hinzuzufügen.

  Füge Tools nur hinzu, wenn sie einen echten Arbeitsablauf ermöglichen. Binde nicht gleich
jedes verwendete Tool ein. Beginne mit ein oder zwei Tools, die einen manuellen
Ablauf ersetzen, den du ohnehin häufig wiederholst, und erweitere die Auswahl dann schrittweise.

## Wiederholbare Arbeitsabläufe in Skills überführen

Sobald du einen Arbeitsablauf zuverlässig wiederholen kannst, solltest du nicht mehr auf lange Prompts oder wiederholtes Hin und Her setzen. Verwende einen [Skill](/de-DE/codex/build-skills), um die Anweisungen, den Kontext und die ergänzende Logik, die Codex konsistent anwenden soll, in der Datei `SKILL.md` zu bündeln. Skills funktionieren in der CLI, der IDE-Erweiterung und der ChatGPT-Desktop-App.

Beschränke jeden Skill auf eine Aufgabe. Beginne mit zwei bis drei konkreten Anwendungsfällen, definiere klare Eingaben und Ausgaben und beschreibe, was der Skill tut und wann er verwendet werden sollte. Nimm außerdem Formulierungen auf, mit denen Nutzende den Skill tatsächlich aufrufen würden.

Versuche nicht, von Anfang an jeden Ausnahmefall abzudecken. Beginne mit einer typischen Aufgabe und sorge dafür, dass sie zuverlässig funktioniert. Überführe den Arbeitsablauf dann in einen Skill und verbessere ihn schrittweise. Füge Skripte oder zusätzliche Ressourcen nur hinzu, wenn sie die Zuverlässigkeit erhöhen.

Eine gute Faustregel: Wenn du immer wieder denselben Prompt verwendest oder denselben Arbeitsablauf korrigierst, sollte daraus wahrscheinlich ein Skill werden.

Skills eignen sich besonders für wiederkehrende Aufgaben wie:

- Log-Triage
- Versionshinweise entwerfen
- PRs anhand einer Checkliste überprüfen
- Migrationen planen
- Telemetriedaten oder Vorfälle zusammenfassen
- Standardisierte Debugging-Abläufe

Der Skill `$skill-creator` ist der beste Ausgangspunkt, um das Grundgerüst für die erste Version eines Skills zu erstellen. Behalte die erste Version lokal, während du sie weiterentwickelst. Sobald du sie allgemein bereitstellen möchtest, verpacke sie als [Plug-in](https://developers.openai.com/plugins/build/plugins). Die Beschreibung gehört zu den wichtigsten Bestandteilen eines Skills. Sie sollte erklären, was der Skill tut und wann er verwendet werden sollte.

  Persönliche Skills werden in `$HOME/.agents/skills` gespeichert. Gemeinsam genutzte Team-Skills
  können in einem Repository unter `.agents/skills` eingecheckt werden. Das ist besonders
  hilfreich, um neue Teammitglieder einzuarbeiten.

## Geplante Aufgaben für wiederkehrende Arbeiten nutzen

Sobald ein Arbeitsablauf stabil läuft, kannst du festlegen, dass Codex ihn für dich im Hintergrund ausführt. In der ChatGPT-Desktop-App kannst du für wiederkehrende Arbeiten über [geplante Aufgaben](/de-DE/codex/automations) das Projekt, den Prompt, das Ausführungsintervall und die Ausführungsumgebung auswählen.

Erstelle auf der Seite **Geplant** eine geplante Aufgabe. Wähle das Projekt, den Prompt,
das Ausführungsintervall und ob die Aufgabe in einem eigenen Git-Worktree oder in deiner lokalen
Umgebung ausgeführt wird. Der Prompt kann Skills aufrufen. Erfahre mehr über
[Git-Worktrees](/de-DE/codex/environments/git-worktrees).

Dafür eignen sich beispielsweise:

- Aktuelle Commits zusammenfassen
- Nach potenziellen Bugs suchen
- Versionshinweise entwerfen
- CI-Fehler prüfen
- Stand-up-Zusammenfassungen erstellen
- Wiederholbare Analyseabläufe nach Zeitplan ausführen

Eine hilfreiche Regel: Skills legen die Methode fest, geplante Aufgaben den Zeitplan. Wenn ein Arbeitsablauf noch viel manuelle Steuerung erfordert, überführe ihn zunächst in einen Skill. Sobald er vorhersehbar abläuft, kannst du durch seine geplante Ausführung Zeit sparen.

  Nutze geplante Aufgaben nicht nur zur Ausführung, sondern auch zur Auswertung und Pflege. Überprüfe
aktuelle Chats, fasse wiederkehrende Schwierigkeiten zusammen und verbessere mit der Zeit Prompts, Anweisungen
oder die Konfiguration des Arbeitsablaufs.

<a id="organize-long-running-tasks"></a>

## Länger laufende Chats organisieren

In Chats sammeln sich mit der Zeit Kontext, Entscheidungen und Aktionen an. Wie du sie organisierst, wirkt sich daher stark auf die Qualität aus.

Mit der ChatGPT-Desktop-App kannst du Chats anheften und Worktrees erstellen. Wenn du die
CLI verwendest, sind diese [Slash-Befehle](/codex/developer-commands?surface=cli) besonders nützlich:

- Mit `/experimental` kannst du experimentelle Funktionen umschalten und in deine Konfigurationsdatei `config.toml` aufnehmen
- Mit `/resume` kannst du einen gespeicherten Chat fortsetzen
- Mit `/fork` kannst du einen neuen Chat erstellen und dabei das ursprüngliche Transkript beibehalten
- Verwende `/compact`, wenn der Chat lang wird und du eine Zusammenfassung des bisherigen Kontexts möchtest. Codex verdichtet Chats außerdem automatisch
- Verwende `/agent`, wenn du mehrere Agenten parallel ausführst und zwischen den aktiven Agenten-Threads wechseln möchtest
- Mit `/theme` kannst du ein Farbschema für die Syntaxhervorhebung auswählen
- Mit `/apps` kannst du ChatGPT-Apps direkt in Codex verwenden
- Mit `/status` kannst du den aktuellen Sitzungsstatus prüfen

Verwende für jede zusammenhängende Arbeitseinheit einen eigenen Chat. Wenn die Arbeit weiterhin dasselbe
Problem betrifft, ist es oft besser, im selben Chat zu bleiben, weil dadurch der
bisherige Lösungsweg erhalten bleibt. Forke nur, wenn sich die Arbeit tatsächlich verzweigt.

  Nutze die Arbeitsabläufe mit [Subagenten](/de-DE/codex/agent-configuration/subagents) in Codex, um
  klar abgegrenzte Aufgaben aus dem Haupt-Thread auszulagern. Der Hauptagent sollte sich auf das
  Kernproblem konzentrieren. Setze Subagenten für Aufgaben wie Erkundung, Tests oder Triage ein.

## Häufige Fehler

Einige häufige Fehler, die du bei deinen ersten Schritten mit Codex vermeiden solltest:

- Den Prompt mit dauerhaften Vorgaben überladen, anstatt sie in `AGENTS.md` oder einen Skill auszulagern
- Dem Agenten nicht ermöglichen, seine Arbeit zu überprüfen, weil Angaben dazu fehlen, wie Build- und Testbefehle am besten ausgeführt werden
- Bei mehrstufigen und komplexen Aufgaben auf die Planung verzichten
- Codex Vollzugriff auf deinen Computer geben, bevor du den Arbeitsablauf verstanden hast
- Laufende Aufgaben an denselben Dateien ausführen, ohne Git-Worktrees zu verwenden
- Eine wiederkehrende Aufgabe planen, bevor sie bei manueller Ausführung zuverlässig funktioniert
- Codex so verwenden, als müsstest du jeden Schritt überwachen, statt es parallel zu deiner eigenen Arbeit einzusetzen
- Einen einzigen Chat für ein ganzes Projekt verwenden, statt für jedes zusammenhängende Ergebnis einen eigenen Chat zu nutzen. Dadurch wächst der Kontext unnötig an und die Ergebnisse werden mit der Zeit schlechter

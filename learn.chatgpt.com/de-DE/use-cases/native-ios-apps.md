<!-- source: https://learn.chatgpt.com/de-DE/use-cases/native-ios-apps -->

## Grundgerüst für App und Build-Schleife erstellen

Beginne bei neuen Projekten mit einfachem Prompting. Bitte Codex, das Grundgerüst für eine iOS-SwiftUI-App zu erstellen und ein kleines Build-und-Start-Skript zu schreiben, das du in einer [lokalen Umgebung](/de-DE/codex/environments/local-environment) mit der Aktion `Build` verknüpfen kannst.

Halte die Schleife CLI-zentriert. Apples `xcodebuild` kann Schemes auflisten und die Aktionen build, test, archive, `build-for-testing` und `test-without-building` vom Terminal aus ausführen. Dadurch kann Codex im agentischen Arbeitsablauf bleiben, statt immer wieder zur Xcode-Benutzeroberfläche wechseln zu müssen.

Wenn du einen aufgeräumteren Projektgenerator möchtest und Tools von Drittanbietern für dich in Ordnung sind, ist [Tuist](https://tuist.dev/) ein guter nächster Schritt. Damit lassen sich Xcode-Projekte ohne Benutzeroberfläche generieren und kompilieren, während Codex die App weiterhin vom Terminal aus kompilieren und starten kann.

Nutze [XcodeBuildMCP](https://www.xcodebuildmcp.com/), sobald du in einem vollständigen Xcode-Projekt arbeitest und weitergehende Automatisierung benötigst. Ab diesem Punkt sind Schemes, Targets, Simulatorsteuerung, Screenshots, Protokolle und UI-Interaktionen so wichtig, dass einfache Shell-Befehle allein nicht mehr ausreichen.

## Skills gezielt einsetzen

Für den ersten Durchlauf brauchst du oft weder einen Skill noch einen MCP-Server. Füge Skills hinzu, sobald die Arbeit spezieller wird oder du im Ablauf strengere SwiftUI-Konventionen verankern möchtest.

- [SwiftUI expert](https://github.com/AvdLee/SwiftUI-Agent-Skill) ist ein leistungsfähiger, vielseitig einsetzbarer SwiftUI-Skill, der bereits viele bewährte Methoden enthält.
- [SwiftUI Pro](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/main/swiftui-pro/SKILL.md) ist ein umfassender Skill zur Überprüfung von SwiftUI-Code auf moderne APIs, Wartbarkeit, Barrierefreiheit und Leistung.

- [Liquid Glass expert](https://github.com/Dimillian/Skills/blob/main/swiftui-liquid-glass/SKILL.md) unterstützt Codex dabei, die neuen APIs für Liquid Glass in iOS 26 einzusetzen und benutzerdefinierte Komponenten so abzustimmen, dass sie zum aktuellen Systemdesign passen.
- [SwiftUI performance](https://github.com/Dimillian/Skills/blob/main/swiftui-performance-audit/SKILL.md) hilft, wenn eine Funktion langsam reagiert oder der Aktualisierungspfad einer SwiftUI-Ansicht verdächtig wirkt. Der Skill sucht nach häufigen SwiftUI-Fehlern und erstellt einen priorisierten Bericht dazu, was behoben werden sollte und wo die größten Verbesserungen möglich sind.
- [Swift concurrency expert](https://github.com/Dimillian/Skills/blob/main/swift-concurrency-expert/SKILL.md) hilft, wenn kryptische Fehler und Compilerwarnungen die gewünschte Änderung erschweren. Bei GPT-5.6 Terra brauchst du den Skill möglicherweise seltener. Er bleibt jedoch nützlich, wenn sich die Diagnosemeldungen zur Nebenläufigkeit in Swift häufen.
- [SwiftUI view refactor](https://github.com/Dimillian/Skills/blob/main/swiftui-view-refactor/SKILL.md) hilft dabei, Dateien kleiner zu halten und SwiftUI-Code im gesamten Repository einheitlicher zu gestalten.
- [SwiftUI patterns](https://github.com/Dimillian/Skills/blob/main/swiftui-ui-patterns/SKILL.md) hilft dir, mit wachsender App auf verlässliche Architekturmuster mit `@Observable` und `@Environment` zu setzen.

Weitere Informationen zur Installation und Verwendung von Skills findest du in unserer [Dokumentation zu Skills](/de-DE/codex/build-skills).

## Iterieren

Sobald eine erste Version funktioniert oder wenn du mit einem bestehenden Projekt beginnst, kannst du die Benutzeroberfläche oder das Verhalten schrittweise weiterentwickeln.

Gib für diesen Teil genau an, was und wie du es ändern möchtest.

Formuliere diese Vorgaben im Prompt ausdrücklich: Teile Codex mit, ob es in einem neuen Repository oder einem bestehenden Xcode-Projekt arbeitet, welche iOS-Geräte oder Deployment-Ziele weiterhin unterstützt werden müssen und welche Validierungsschleife du erwartest.

### Beispiel-Prompt

Wenn du beispielsweise einer bestehenden App eine Funktion hinzufügen möchtest, kannst du Codex um eine Änderung wie diese bitten:

## Praxistipps

### Mit den Grundlagen beginnen

Beginne bei neuen Projekten mit einfachem Prompting. Bitte Codex, das Grundgerüst für eine SwiftUI-App zu erstellen und ein kleines Build-und-Start-Skript zu schreiben, das du in einer [lokalen Umgebung](/de-DE/codex/environments/local-environment) mit der Aktion `Build` verknüpfen kannst. Für diesen ersten Durchlauf brauchst du oft weder einen Skill noch einen MCP-Server.

### Eine kleine, verlässliche Validierungsschleife nutzen

Weise Codex nach jeder Änderung an, den möglichst gezielten Befehl auszuführen, der tatsächlich nachweist, dass die betroffene Anforderung erfüllt ist. Weite die Prüfung erst später auf umfangreichere Builds aus. So bleibt Codex schnell, ohne so zu tun, als sei für jede Änderung ein vollständiger App-Build erforderlich.

### Setze im Entwicklungszyklus primär auf die CLI

Setze im Entwicklungszyklus primär auf die CLI. Apples Tool `xcodebuild` kann Schemes auflisten und die Aktionen build, test, archive, `build-for-testing` und `test-without-building` über das Terminal ausführen. So kann Codex eigenständig weiterarbeiten, statt immer wieder zur grafischen Benutzeroberfläche von Xcode wechseln zu müssen.

### Nutze XcodeBuildMCP

Nutze XcodeBuildMCP, sobald du in einem vollständigen Xcode-Projekt arbeitest und weitergehende Automatisierung benötigst. Ab dann spielen Schemes, Targets, die Steuerung des Simulators, Screenshots, Logs und UI-Interaktionen eine so große Rolle, dass einfache Shell-Befehle allein nicht mehr ausreichen.

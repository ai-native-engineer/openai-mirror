<!-- source: https://learn.chatgpt.com/de-DE/guides/build-ai-native-engineering-team -->

## Einführung

KI-Modelle können immer mehr Aufgaben übernehmen, was erhebliche Auswirkungen auf das Engineering hat. Modernste Systeme können mittlerweile über mehrere Stunden hinweg schlussfolgern. Im August 2025 stellte METR fest, dass führende Modelle **2 Stunden und 17 Minuten** lang kontinuierlich arbeiten konnten und dabei mit **etwa 50 % Wahrscheinlichkeit** ein korrektes Ergebnis erzielten.

Diese Fähigkeit entwickelt sich rasant weiter: Die Dauer der bewältigbaren Aufgaben verdoppelt sich etwa alle sieben Monate. Noch vor wenigen Jahren konnten Modelle etwa 30 Sekunden lang schlussfolgern, gerade genug für kleine Codevorschläge. Heute können Modelle längere Gedankengänge aufrechterhalten, sodass KI potenziell den gesamten Softwareentwicklungszyklus unterstützen kann. Coding-Agenten können damit effektiv zu Planung, Design, Entwicklung, Tests, Code Reviews und Bereitstellung beitragen.

![][image1]In diesem Leitfaden zeigen wir anhand konkreter Beispiele, wie KI-Agenten zum Softwareentwicklungszyklus beitragen. Außerdem geben wir Verantwortlichen im Engineering praktische Hinweise, wie sie schon heute KI-native Teams und Prozesse aufbauen können.

## Programmieren mit KI: Von Autovervollständigung zu Agenten

KI-Tools für die Softwareentwicklung können inzwischen weit mehr als ihre ursprüngliche Aufgabe als Autovervollständigungsassistenten. Frühe Tools erledigten kurze Aufgaben, etwa die nächste Codezeile vorzuschlagen oder Funktionsvorlagen auszufüllen. Mit den wachsenden Reasoning-Fähigkeiten der Modelle begannen Entwicklungsteams, über Chat-Oberflächen in IDEs mit Agenten zu interagieren, beispielsweise für Paarprogrammierung und die Erkundung von Code.

Heutige Coding-Agenten können vollständige Dateien generieren, Grundgerüste für neue Projekte erstellen und Designs in Code umsetzen. Sie können mehrstufige Probleme wie Debugging oder Refactoring lösen. Zugleich verlagert sich die Ausführung der Agenten von lokalen Rechnern in cloudbasierte Umgebungen mit mehreren Agenten. Dadurch erstellen Entwicklungsteams weniger Code gemeinsam mit dem Agenten in der IDE und delegieren stattdessen häufiger ganze Arbeitsabläufe.

| Fähigkeit                         | Was sie ermöglicht                                                                                                                                                        |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Einheitlicher Kontext über Systemgrenzen hinweg** | Ein einziges Modell kann Code, Konfiguration und Telemetriedaten lesen und so über mehrere Ebenen hinweg konsistent schlussfolgern. Zuvor waren dafür separate Tools erforderlich.                    |
| **Strukturierte Ausführung von Tools**      | Modelle können Compiler, Test-Runner und Scanner jetzt direkt aufrufen und dadurch überprüfbare Ergebnisse statt statischer Vorschläge liefern.                                       |
| **Dauerhaftes Projektgedächtnis**      | Große Kontextfenster und Techniken wie Compaction (Kontextverdichtung) ermöglichen es Modellen, ein Feature vom ersten Vorschlag bis zur Bereitstellung zu begleiten und sich dabei an frühere Designentscheidungen und Einschränkungen zu erinnern. |
| **Evaluationsschleifen**               | Modellausgaben lassen sich automatisch anhand von Benchmarks wie Unit-Tests, Latenzzielen oder Styleguides prüfen. So basieren Verbesserungen auf messbarer Qualität.          |

Bei OpenAI erleben wir das aus erster Hand. Die Entwicklungszyklen haben sich verkürzt: Arbeiten, die früher Wochen dauerten, werden heute innerhalb weniger Tage abgeschlossen. Teams wechseln leichter zwischen Fachgebieten, finden sich schneller in unbekannten Projekten zurecht und arbeiten im gesamten Unternehmen agiler und eigenständiger. Viele Routineaufgaben und zeitaufwendige Tätigkeiten werden inzwischen vollständig an Codex delegiert, darunter das Dokumentieren von neuem Code, das Ermitteln relevanter Tests, die Pflege von Abhängigkeiten und das Bereinigen von Feature-Flags.

Einige Aspekte des Engineerings bleiben jedoch unverändert. Die letztliche Verantwortung für Code liegt weiterhin bei den Engineering-Teams, insbesondere bei neuen oder unklaren Problemstellungen. Bestimmte Herausforderungen übersteigen zudem die Fähigkeiten heutiger Modelle. Mit Coding-Agenten wie Codex können sich Engineering-Teams jedoch intensiver komplexen und neuartigen Aufgaben widmen. Statt Debugging oder schematischer Implementierung stehen Design, Architektur und systemübergreifende Überlegungen im Mittelpunkt.

In den folgenden Abschnitten zeigen wir, wie Coding-Agenten die einzelnen Phasen des SDLC verändern, und nennen konkrete Schritte, mit denen dein Team als KI-native Engineering-Organisation arbeiten kann.

## 1. Planung

Teams im gesamten Unternehmen sind häufig auf Engineering-Fachwissen angewiesen, um festzustellen, ob ein Feature umsetzbar ist, wie lange die Entwicklung dauert und welche Systeme oder Teams beteiligt sind. Zwar kann grundsätzlich jede Person eine Spezifikation entwerfen, doch eine belastbare Planung erfordert meist detaillierte Kenntnisse der Codebasis und mehrere Abstimmungsrunden mit dem Engineering-Team. Nur so lassen sich Anforderungen ermitteln, Ausnahmefälle klären und realistische technische Ziele vereinbaren.

### So helfen Coding-Agenten

KI-Coding-Agenten liefern Teams bei der Planung und Abgrenzung des Umfangs sofort verwertbare Erkenntnisse mit direktem Codebezug. Teams können beispielsweise Arbeitsabläufe einrichten, die Coding-Agenten an ihre Issue-Tracking-Systeme anbinden. Die Agenten lesen dann eine Feature-Spezifikation, gleichen sie mit der Codebasis ab, markieren Unklarheiten, unterteilen die Arbeit in Teilkomponenten oder schätzen den Schwierigkeitsgrad ein.

Coding-Agenten können außerdem Codepfade sofort nachverfolgen und zeigen, welche Services an einem Feature beteiligt sind. Diese Arbeit erforderte früher stunden- oder tagelange manuelle Recherchen in einer großen Codebasis.

### Worauf sich Engineering-Teams stattdessen konzentrieren

Teams haben mehr Zeit für die eigentliche Feature-Arbeit, weil Agenten den Kontext bereitstellen, für den zuvor Meetings zur Produktabstimmung und Umfangsplanung nötig waren. Wichtige Implementierungsdetails, Abhängigkeiten und Ausnahmefälle werden von Anfang an erkannt. So lassen sich Entscheidungen schneller und mit weniger Meetings treffen.

| Delegieren                                                                                                                                                                                                              | Review                                                                                                                                                                                                                                       | Verantworten                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| KI-Agenten können eine erste Machbarkeits- und Architekturanalyse übernehmen. Sie lesen eine Spezifikation, gleichen sie mit der Codebasis ab, ermitteln Abhängigkeiten und weisen auf Unklarheiten oder Ausnahmefälle hin, die geklärt werden müssen. | Teams prüfen die Ergebnisse des Agenten auf Richtigkeit und Vollständigkeit und stellen sicher, dass die Schätzungen den tatsächlichen technischen Einschränkungen entsprechen. Für die Vergabe von Story Points, die Aufwandsschätzung und das Erkennen nicht offensichtlicher Risiken ist weiterhin menschliches Urteilsvermögen nötig. | Strategische Entscheidungen, etwa zu Priorisierung, langfristiger Ausrichtung, Reihenfolge und Zielkonflikten, werden weiterhin von Menschen getroffen. Teams können den Agenten nach Optionen oder nächsten Schritten fragen, doch die Organisation trägt letztlich die Verantwortung für Planung und Produktausrichtung. |

### Checkliste für den Einstieg

- Ermittle gängige Prozesse, bei denen Features und Quellcode aufeinander abgestimmt werden müssen. Häufige Bereiche sind die Eingrenzung des Feature-Umfangs und die Ticketerstellung.
- Implementiere zunächst grundlegende Arbeitsabläufe, etwa zum Taggen und Deduplizieren von Issues oder Feature-Anfragen.
- Ziehe anspruchsvollere Arbeitsabläufe in Betracht, etwa das Hinzufügen von Unteraufgaben zu einem Ticket auf Grundlage einer ersten Feature-Beschreibung. Oder starte einen Agentenlauf, sobald ein Ticket eine bestimmte Phase erreicht, damit der Agent die Beschreibung um weitere Details ergänzt.

<br />

## 2. Design

Die Designphase wird häufig durch grundlegende Setup-Arbeiten ausgebremst. Teams verbringen viel Zeit damit, Boilerplate-Code einzurichten, Designsysteme zu integrieren und UI-Komponenten oder Abläufe auszuarbeiten. Wenn Mockups und Implementierung nicht übereinstimmen, entstehen Nacharbeiten und lange Feedbackzyklen. Begrenzte Kapazitäten, um Alternativen auszuloten oder auf veränderte Anforderungen zu reagieren, verzögern zudem die Validierung des Designs.

### So helfen Coding-Agenten

KI-Tools für die Softwareentwicklung beschleunigen das Prototyping erheblich: Sie erstellen Boilerplate-Code, bauen Projektstrukturen auf und implementieren Design-Tokens oder Styleguides sofort. Engineering-Teams können gewünschte Features oder UI-Layouts in natürlicher Sprache beschreiben und erhalten Prototypcode oder Komponenten-Stubs, die den Konventionen des Teams entsprechen.

Sie können Designs direkt in Code umsetzen, Verbesserungen für die Barrierefreiheit vorschlagen und sogar die Codebasis auf Nutzungsabläufe oder Ausnahmefälle untersuchen. Dadurch können Teams mehrere Prototypen innerhalb von Stunden statt Tagen iterativ verbessern und bereits früh detailgetreu arbeiten. Das schafft eine klarere Entscheidungsgrundlage und ermöglicht Kundentests deutlich früher im Prozess.

### Worauf sich Engineering-Teams stattdessen konzentrieren

Wenn Agenten routinemäßige Setup- und Übertragungsaufgaben übernehmen, können sich Teams wirkungsvolleren Aufgaben widmen. Engineering-Teams konzentrieren sich auf die Kernlogik, etablieren skalierbare Architekturmuster und stellen sicher, dass Komponenten die Qualitäts- und Zuverlässigkeitsstandards erfüllen. Designteams können mehr Zeit in die Bewertung von Nutzungsabläufen und die Erkundung alternativer Konzepte investieren. In der Zusammenarbeit geht es damit weniger um Implementierungsaufwand und stärker um ein besseres Produkterlebnis.

| Delegieren                                                                                                                                                                             | Review                                                                                                                                                                       | Verantworten                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Agenten übernehmen die erste Implementierung: Sie erstellen Projektgrundgerüste und Boilerplate-Code, überführen Mockups in Komponenten und wenden Design-Tokens oder Styleguides an. | Das Team prüft die Ausgabe des Agenten und stellt sicher, dass die Komponenten den Designkonventionen folgen, die Standards für Qualität und Barrierefreiheit erfüllen und korrekt in bestehende Systeme integriert sind. | Das Team verantwortet das übergreifende Designsystem, die UX-Muster, Architekturentscheidungen und die endgültige Ausrichtung des Nutzungserlebnisses. |

### Checkliste für den Einstieg

- Nutze einen multimodalen Coding-Agenten, der sowohl Text- als auch Bildeingaben akzeptiert
- Binde Design-Tools über MCP an Coding-Agenten an
- Mache Komponentenbibliotheken über MCP programmatisch zugänglich und integriere sie in dein Coding-Modell
- Erstelle Arbeitsabläufe, die Designs → Komponenten → Komponentenimplementierung abbilden
- Nutze typisierte Programmiersprachen (z. B. Typescript), um gültige Props und Unterkomponenten für den Agenten zu definieren
  <br />

## 3. Implementierung

In der Implementierungsphase erleben Teams die größten Reibungsverluste, und hier haben Coding-Agenten den deutlichsten Effekt. Engineering-Teams investieren viel Zeit darin, Spezifikationen in Codestrukturen zu übertragen, Services miteinander zu verbinden, Muster in der gesamten Codebasis zu duplizieren und Boilerplate-Code zu ergänzen. Selbst kleine Features erfordern dadurch stundenlange Routinearbeit.

Mit wachsenden Systemen verstärken sich diese Reibungsverluste. In großen Monorepos sammeln sich Muster, Konventionen und historisch bedingte Eigenheiten an, die Mitwirkende ausbremsen. Engineering-Teams können genauso viel Zeit damit verbringen, den „richtigen Weg“ für eine Aufgabe erneut herauszufinden, wie mit der eigentlichen Implementierung des Features. Der ständige Wechsel zwischen Spezifikationen, Codesuche, Build-Fehlern, fehlgeschlagenen Tests und Abhängigkeitsverwaltung erhöht die kognitive Belastung. Unterbrechungen während lang laufender Aufgaben stören zusätzlich den Arbeitsfluss und verzögern die Auslieferung.

### So helfen Coding-Agenten

Coding-Agenten in IDE und CLI beschleunigen die Implementierungsphase, indem sie größere, mehrstufige Implementierungsaufgaben übernehmen. Statt lediglich die nächste Funktion oder Datei zu erstellen, können sie in einem einzigen koordinierten Lauf vollständige Features von Anfang bis Ende umsetzen: Datenmodelle, APIs, UI-Komponenten, Tests und Dokumentation. Da sie über längere Zeit hinweg die gesamte Codebasis in ihre Schlussfolgerungen einbeziehen, können sie Entscheidungen treffen, für die Engineering-Teams früher Codepfade manuell nachverfolgen mussten.

Bei lang laufenden Aufgaben können Agenten:

- Vollständige Feature-Implementierungen anhand einer schriftlichen Spezifikation entwerfen.
- Code in Dutzenden von Dateien durchsuchen und ändern und dabei die Konsistenz wahren.
- Boilerplate-Code nach bestehenden Konventionen erzeugen: für Fehlerbehandlung, Telemetrie, Sicherheits-Wrapper oder Stilmuster.
- Build-Fehler direkt beheben, wenn sie auftreten, statt auf menschliches Eingreifen zu warten.
- Tests parallel zur Implementierung in einem einzigen Arbeitsablauf schreiben.
- Änderungssätze erstellen, die direkt als Diff geprüft werden können, internen Richtlinien entsprechen und PR-Beschreibungen enthalten.

In der Praxis verlagert sich dadurch ein Großteil der mechanischen Implementierungsarbeit vom Entwicklungsteam auf die Agenten. Der Agent erstellt den ersten Implementierungsentwurf; das Team prüft und überarbeitet ihn und gibt die Richtung vor.

### Was Entwicklungsteams stattdessen tun

Wenn Agenten mehrstufige Implementierungsaufgaben zuverlässig ausführen können, konzentrieren sich Entwicklungsteams auf anspruchsvollere Aufgaben:

- Produktverhalten, Ausnahmefälle und Spezifikationen vor der Implementierung klären.
- Die architektonischen Auswirkungen von KI-generiertem Code prüfen, statt Komponenten routinemäßig miteinander zu verbinden.
- Geschäftslogik und performancekritische Pfade verfeinern, die fundierte Kenntnisse der Domäne erfordern.
- Muster, Leitplanken und Konventionen entwerfen, die von Agenten generierten Code steuern.
- Mit PMs und dem Designteam zusammenarbeiten, um die Zielsetzung eines Features iterativ zu verfeinern, statt sich mit Boilerplate-Code zu befassen.

Statt eine Feature-Spezifikation in Code zu „übersetzen“, konzentrieren sich Entwicklungsteams auf Korrektheit, Konsistenz, Wartbarkeit und langfristige Qualität. In diesen Bereichen bleibt menschliches Kontextwissen besonders wichtig.

| Delegieren                                                                                                                                                                                                                                           | Review                                                                                                                                                                                                                              | Verantworten                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agenten erstellen einen ersten Implementierungsentwurf für klar spezifizierte Features: Scaffolding, CRUD-Logik, die Verknüpfung von Komponenten, Refactorings und Tests. Da Modelle immer länger zuverlässig arbeiten können, umfasst dies zunehmend vollständige End-to-End-Implementierungen statt einzelner Codeausschnitte. | Entwicklungsteams prüfen Designentscheidungen, Performance, Sicherheit, Migrationsrisiken und die fachliche Passung. Dabei korrigieren sie subtile Probleme, die dem Agenten möglicherweise entgehen. Sie gestalten und verfeinern KI-generierten Code, statt die mechanische Arbeit selbst auszuführen. | Entwicklungsteams bleiben für Arbeiten verantwortlich, die ein fundiertes Systemverständnis erfordern: neue Abstraktionen, übergreifende Architekturänderungen, mehrdeutige Produktanforderungen und langfristige Abwägungen zur Wartbarkeit. Je längere Aufgaben Agenten übernehmen, desto stärker verlagert sich die Entwicklungsarbeit von der zeilenweisen Implementierung hin zur iterativen Begleitung und Kontrolle. |

Beispiel:

Die Teams für Entwicklung, Produktmanagement, Design und Betrieb bei Cloudwalk nutzen Codex täglich, um Spezifikationen in funktionierenden Code umzusetzen, egal, ob sie ein Skript, eine neue Regel zur Betrugserkennung oder einen vollständigen Microservice benötigen, der in wenigen Minuten bereitsteht. Codex nimmt ihnen die Routinearbeit in der Implementierungsphase ab und ermöglicht allen Beschäftigten, Ideen bemerkenswert schnell umzusetzen.

### Checkliste für die ersten Schritte

- Beginne mit klar spezifizierten Aufgaben
- Lass den Agenten ein Planungstool über MCP verwenden oder eine PLAN.md-Datei schreiben, die in die Codebasis committet wird
- Prüfe, ob die Befehle, die der Agent auszuführen versucht, erfolgreich abgeschlossen werden
- Optimiere eine AGENTS.md-Datei iterativ, damit der Agent Feedbackschleifen durchlaufen kann, etwa indem er Tests und Linter ausführt und deren Feedback nutzt
  <br />

## 4. Testen

Entwicklungsteams fällt es oft schwer, eine ausreichende Testabdeckung sicherzustellen, weil das Schreiben und Pflegen umfassender Tests Zeit kostet, Kontextwechsel erfordert und ein tiefes Verständnis von Ausnahmefällen voraussetzt. Teams müssen häufig zwischen hoher Entwicklungsgeschwindigkeit und gründlichen Tests abwägen. Bei knappen Fristen leidet die Testabdeckung oft als Erstes.

Selbst vorhandene Tests mit der Weiterentwicklung des Codes aktuell zu halten, verursacht kontinuierlichen Aufwand. Tests können fragil werden, aus unklaren Gründen fehlschlagen und umfangreiche eigene Refactorings erfordern, wenn sich das zugrunde liegende Produkt ändert. Hochwertige Tests ermöglichen Teams, schneller und mit größerer Sicherheit auszuliefern.

### Wie Coding-Agenten helfen

KI-Tools für die Softwareentwicklung können auf verschiedene Weise dabei helfen, bessere Tests zu schreiben. Zunächst können sie anhand eines Anforderungsdokuments und der Logik im Feature-Code Testfälle vorschlagen. Modelle können überraschend gut Ausnahmefälle und Fehlerszenarien aufzeigen, die bei der Entwicklung leicht übersehen werden. Das gilt besonders, wenn sich jemand intensiv auf das Feature konzentriert hat und eine zweite Einschätzung braucht.

Darüber hinaus können Modelle Tests bei Änderungen am Code auf dem neuesten Stand halten. Das erleichtert Refactorings und verhindert veraltete Tests, die unzuverlässig werden. Indem Coding-Agenten grundlegende Implementierungsdetails beim Schreiben von Tests übernehmen und auf Ausnahmefälle hinweisen, beschleunigen sie die Testentwicklung.

### Was Entwicklungsteams stattdessen tun

Tests mit KI-Tools zu schreiben, entbindet Entwicklungsteams nicht davon, sich mit der Teststrategie auseinanderzusetzen. Im Gegenteil: Da Agenten Hürden bei der Codegenerierung abbauen, werden Tests als maßgebliche Referenz für die Anwendungsfunktionalität immer wichtiger. Da Agenten die Testsuite ausführen und ihre Arbeit anhand der Ergebnisse iterativ verbessern können, ist die Definition hochwertiger Tests oft der erste Schritt, damit ein Agent ein Feature implementieren kann.

Stattdessen achten Entwicklungsteams stärker auf übergeordnete Muster in der Testabdeckung und ergänzen und hinterfragen die vom Modell ermittelten Testfälle. Wenn sich Tests schneller schreiben lassen, können sie Features zügiger ausliefern und zugleich ambitioniertere Features angehen.

| Delegieren                                                                                                                                                                                                                                                                          | Review                                                                                                                                                                                                                                                                                                                                           | Verantworten                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Entwicklungsteams delegieren den ersten Entwurf von Testfällen auf Grundlage der Feature-Spezifikationen. Auch für eine erste Implementierung der Tests nutzen sie das Modell. Dabei kann es hilfreich sein, das Modell die Tests in einer separaten Sitzung und unabhängig von der Feature-Implementierung generieren zu lassen. | Entwicklungsteams müssen vom Modell generierte Tests weiterhin gründlich prüfen, um sicherzustellen, dass das Modell keine Abkürzungen genommen oder bloße Stub-Tests implementiert hat. Sie stellen außerdem sicher, dass ihre Agenten die Tests ausführen können, die erforderlichen Berechtigungen haben und über den nötigen Kontext zu den verfügbaren Testsuites verfügen. | Entwicklungsteams sind dafür verantwortlich, die Testabdeckung an den Feature-Spezifikationen und den Erwartungen an die User Experience auszurichten. Adversariales Denken, Kreativität beim Erfassen von Ausnahmefällen und ein klarer Fokus auf die Zielsetzung der Tests bleiben entscheidende Kompetenzen. |

### Checkliste für die ersten Schritte

- Lass das Modell Tests in einem separaten Schritt implementieren und prüfe, ob neue Tests fehlschlagen, bevor du mit der Feature-Implementierung beginnst.
- Lege in deiner AGENTS.md-Datei Richtlinien für die Testabdeckung fest
- Gib dem Agenten konkrete Beispiele für Tools zur Codeabdeckung, die er aufrufen kann, um die Testabdeckung zu ermitteln
  <br />

## 5. Review

Im Durchschnitt verbringen Entwicklungsteams 2–5 Stunden pro Woche mit Codeüberprüfungen. Oft müssen sie sich entscheiden, ob sie viel Zeit in eine gründliche Prüfung investieren oder scheinbar kleine Änderungen nur kurz nach dem Prinzip „gut genug“ prüfen. Werden dabei die falschen Prioritäten gesetzt, gelangen Fehler in die Produktion. Das verursacht Probleme für die Nutzenden und erheblichen Nacharbeitsaufwand.

### Wie Coding-Agenten helfen

Coding-Agenten ermöglichen es, Codeüberprüfungen zu skalieren, sodass jeder PR ein einheitliches Mindestmaß an Aufmerksamkeit erhält. Im Gegensatz zu herkömmlichen Tools für die statische Analyse, die auf Musterabgleich und regelbasierten Prüfungen beruhen, können KI-Reviewer Teile des Codes tatsächlich ausführen, das Laufzeitverhalten interpretieren und die Logik über Dateien und Services hinweg nachvollziehen. Damit dies effektiv funktioniert, müssen Modelle jedoch gezielt zum Erkennen von Fehlern der Stufen P0 und P1 trainiert und darauf abgestimmt werden, knappes, aussagekräftiges Feedback zu liefern. Zu ausführliche Antworten werden genauso leicht ignoriert wie wenig aussagekräftige Lint-Warnungen.

### Was Entwicklungsteams stattdessen tun

Unsere Erfahrung bei OpenAI zeigt, dass KI-gestützte Codeüberprüfungen Entwicklungsteams mehr Sicherheit geben, keine schwerwiegenden Fehler in die Produktion auszuliefern. Häufig werden dabei Probleme entdeckt, die noch vor der Einbindung eines weiteren Teammitglieds behoben werden können. Eine Codeüberprüfung beschleunigt den Prozess für Pull Requests nicht unbedingt, insbesondere wenn sie relevante Fehler aufdeckt. Sie verhindert jedoch Defekte und Ausfälle.

### Delegieren, überprüfen oder selbst verantworten

Auch mit KI-gestützter Codeüberprüfung bleiben Entwicklungsteams dafür verantwortlich, dass der Code zur Auslieferung bereit ist. Konkret bedeutet das, die Änderungen zu lesen und ihre Auswirkungen zu verstehen. Die erste Codeüberprüfung delegieren sie an einen Agenten, die Verantwortung für die abschließende Prüfung und den Merge-Prozess bleibt jedoch bei ihnen.

| Delegieren                                                                                                                                                    | Review                                                                                                                                                                                                                       | Verantworten                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Entwicklungsteams delegieren die erste Codeüberprüfung an Agenten. Das kann mehrmals geschehen, bevor der Pull Request als bereit für die Überprüfung durch ein Teammitglied gekennzeichnet wird. | Entwicklungsteams überprüfen Pull Requests weiterhin selbst. Der Schwerpunkt liegt dabei jedoch stärker auf der architektonischen Ausrichtung: Werden modular kombinierbare Muster implementiert? Werden die richtigen Konventionen verwendet? Entspricht die Funktionalität den Anforderungen? | Entwicklungsteams tragen letztlich die Verantwortung für den Code, der in der Produktion bereitgestellt wird. Sie müssen sicherstellen, dass er zuverlässig funktioniert und die vorgesehenen Anforderungen erfüllt. |

Beispiel:

Sansan nutzt Codex Review für Race Conditions und Datenbankbeziehungen, zwei Problemarten, die Menschen häufig übersehen. Codex konnte außerdem unsachgemäßes Hardcoding erkennen und sogar künftige Skalierbarkeitsprobleme vorhersehen.

### Checkliste für die ersten Schritte

- Stelle Beispiele für vorbildliche PRs zusammen, die Mitglieder des Entwicklungsteams bearbeitet haben, und berücksichtige dabei sowohl die Codeänderungen als auch die hinterlassenen Kommentare. Speichere sie als Evaluationsdatensatz, um verschiedene Tools zu vergleichen.
- Wähle ein Produkt mit einem Modell, das speziell für die Codeüberprüfung trainiert wurde. Wir haben festgestellt, dass generalistische Modelle häufig Kleinigkeiten beanstanden und ein niedriges Signal-Rausch-Verhältnis liefern.
- Lege fest, wie dein Team die Qualität von Reviews misst. Wir empfehlen, Reaktionen auf PR-Kommentare zu erfassen, um gute und schlechte Reviews mit wenig Aufwand zu kennzeichnen.
- Starte im kleinen Rahmen, weite den Einsatz aber zügig aus, sobald du den Ergebnissen der Reviews vertraust.
  <br />

## 6. Dokumentieren

Die meisten Entwicklungsteams wissen, dass ihre Dokumentation nicht auf dem aktuellen Stand ist, doch das Nacharbeiten ist aufwendig. Wichtiges Wissen liegt oft nur bei einzelnen Personen, statt in durchsuchbaren Wissensdatenbanken erfasst zu sein. Bestehende Dokumentation veraltet schnell, weil ihre Aktualisierung Zeit von der Produktentwicklung abzieht. Selbst Dokumentations-Sprints bleiben meist einmalige Aktionen, deren Ergebnisse veralten, sobald sich das System weiterentwickelt.

### So helfen Coding-Agenten

Coding-Agenten können die Funktionsweise von Codebasen nach deren Analyse sehr gut zusammenfassen. Sie können nicht nur beschreiben, wie Teile der Codebasis funktionieren, sondern auch Systemdiagramme in Formaten wie mermaid erstellen. Wenn Entwicklungsteams mithilfe von Agenten Funktionen umsetzen, müssen sie das Modell nur per Prompt anweisen, auch die Dokumentation zu aktualisieren. Über AGENTS.md lassen sich Anweisungen, die Dokumentation bei Bedarf zu aktualisieren, automatisch jedem Prompt hinzufügen. Das sorgt für konsistentere Ergebnisse.

Da sich Coding-Agenten über SDKs programmatisch ausführen lassen, können sie auch in Release-Arbeitsabläufe eingebunden werden. Beispielsweise können wir einen Coding-Agenten anweisen, die in einem Release enthaltenen Commits zu prüfen und die wichtigsten Änderungen zusammenzufassen. Damit wird Dokumentation zu einem festen Bestandteil der Auslieferungspipeline: Sie lässt sich schneller erstellen und leichter aktuell halten und hängt nicht mehr davon ab, dass jemand „Zeit dafür findet“.

### Was Entwicklungsteams stattdessen tun

Entwicklungsteams verfassen nicht mehr jedes Dokument von Hand, sondern gestalten und überwachen das Dokumentationssystem. Sie legen fest, wie die Dokumentation organisiert wird, dokumentieren die wichtigen Gründe für Entscheidungen, definieren klare Standards und Vorlagen für Agenten und prüfen kritische oder an die Kundschaft gerichtete Inhalte. Ihre Aufgabe besteht darin, für eine strukturierte und korrekte Dokumentation zu sorgen, die in den Auslieferungsprozess eingebunden ist, statt jeden Text selbst zu verfassen.

| Delegieren                                                                                                                                                                                                   | Review                                                                                                                                                                              | Verantworten                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Übergib risikoarme, wiederkehrende Aufgaben vollständig an Codex. Dazu zählen erste Entwürfe von Zusammenfassungen zu Dateien und Modulen, grundlegende Beschreibungen von Ein- und Ausgaben, Abhängigkeitslisten und kurze Zusammenfassungen von Änderungen in Pull Requests. | Entwicklungsteams prüfen und bearbeiten wichtige Dokumente, die Codex entworfen hat, etwa Übersichten zu zentralen Diensten, öffentliche API- und SDK-Dokumentation, Runbooks und Architekturseiten, bevor diese veröffentlicht werden. | Entwicklungsteams bleiben verantwortlich für die gesamte Dokumentationsstrategie und -struktur, für die Standards und Vorlagen, denen der Agent folgt, sowie für sämtliche externe oder sicherheitskritische Dokumentation, die rechtliche, regulatorische oder Markenrisiken birgt. |

### Checkliste für die ersten Schritte

- Erprobe die Dokumentationsgenerierung, indem du dem Coding-Agenten passende Prompts gibst
- Nimm Dokumentationsrichtlinien in AGENTS.md auf
- Ermittle Arbeitsabläufe (z. B. Release-Zyklen), in denen sich Dokumentation automatisch generieren lässt
- Prüfe generierte Inhalte auf Qualität und Korrektheit sowie darauf, ob sie klar fokussiert sind
  <br />

## 7. Bereitstellen und warten

Das Anwendungs-Logging zu verstehen, ist für die Zuverlässigkeit von Software entscheidend. Bei einem Vorfall ziehen Entwicklungsteams Logging-Tools, Code-Bereitstellungen und Infrastrukturänderungen heran, um die Ursache zu ermitteln. Dieser Prozess ist oft überraschend manuell: Entwicklungsteams müssen ständig zwischen verschiedenen Systemen wechseln und verlieren dadurch gerade in Situationen mit hohem Zeitdruck wertvolle Minuten.

### So helfen Coding-Agenten

Mit KI-Coding-Tools kannst du dem Modell neben dem Kontext deiner Codebasis über MCP-Server auch Zugriff auf deine Logging-Tools geben. Das ermöglicht einen einheitlichen Arbeitsablauf: Du kannst das Modell anweisen, Fehler an einem bestimmten Endpunkt zu untersuchen. Mit diesem Kontext kann es anschließend die Codebasis durchsuchen und relevante Bugs oder Leistungsprobleme finden. Coding-Agenten können außerdem Kommandozeilentools einsetzen und so im Git-Verlauf konkrete Änderungen ermitteln, die zu den in Log-Traces erfassten Problemen geführt haben könnten.

### Was Entwicklungsteams stattdessen tun

Indem KI die mühsamen Teile der Log-Analyse und Vorfalltriage automatisiert, können sich Entwicklungsteams auf anspruchsvollere Fehlerbehebung und Systemverbesserungen konzentrieren. Statt Logs, Commits und Infrastrukturänderungen manuell abzugleichen, validieren sie von der KI ermittelte Fehlerursachen, entwerfen robuste Korrekturen und entwickeln Präventivmaßnahmen. Dadurch verbringen Teams weniger Zeit mit reaktiver Störungsbehebung und können mehr in proaktive Zuverlässigkeitsarbeit und Architekturverbesserungen investieren.

| Delegieren                                                                                                                                                      | Review                                                                                                                                                                      | Verantworten                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Viele operative Aufgaben lassen sich an Agenten delegieren: Logs parsen, auffällige Metriken aufzeigen, verdächtige Codeänderungen ermitteln und sogar Hotfixes vorschlagen. | Entwicklungsteams prüfen und verfeinern KI-generierte Diagnosen, bestätigen ihre Korrektheit und geben Schritte zur Behebung frei. Sie stellen sicher, dass Korrekturen den Anforderungen an Zuverlässigkeit, Sicherheit und Compliance entsprechen. | Kritische Entscheidungen bleiben beim Entwicklungsteam, insbesondere bei bislang unbekannten Vorfällen, sensiblen Änderungen an Produktionssystemen oder wenn die Konfidenz des Modells gering ist. Menschen tragen weiterhin die Verantwortung für die Beurteilung und endgültige Freigabe. |

Beispiel:

Virgin Atlantic nutzt Codex, um die Abläufe für Bereitstellung und Wartung der Systeme zu verbessern. Mit der Codex-Erweiterung für VS Code können Entwicklungsteams an einem zentralen Ort Logs untersuchen, Probleme über Code und Daten hinweg nachverfolgen und Änderungen mithilfe von Azure DevOps MCP und Databricks Managed MCPs überprüfen. Durch diese Bündelung des operativen Kontexts in der IDE beschleunigt Codex die Ursachenanalyse, reduziert die manuelle Triage und hilft Teams, Korrekturen zu validieren und die Systemzuverlässigkeit zu verbessern.

### Checkliste für die ersten Schritte

- Verbinde KI-Tools mit Logging- und Bereitstellungssystemen: Binde Codex CLI oder vergleichbare Tools an deine MCP-Server und Log-Aggregatoren an.
- Definiere Zugriffsbereiche und Berechtigungen: Stelle sicher, dass Agenten auf relevante Logs, Code-Repositories und Bereitstellungsverläufe zugreifen können, ohne bewährte Sicherheitspraktiken zu vernachlässigen.
- Konfiguriere Prompt-Vorlagen: Erstelle wiederverwendbare Prompts für häufige operative Anfragen, etwa „Untersuche Fehler am Endpunkt X“ oder „Analysiere sprunghafte Anstiege des Log-Aufkommens nach der Bereitstellung.“
- Teste den Arbeitsablauf: Spiele simulierte Vorfallszenarien durch und stelle sicher, dass die KI den richtigen Kontext ermittelt, Codepfade korrekt nachverfolgt und Diagnosen liefert, aus denen sich konkrete Maßnahmen ableiten lassen.
- Verbessere den Arbeitsablauf schrittweise: Sammle Feedback aus realen Vorfällen, optimiere deine Prompt-Strategien und erweitere die Einsatzmöglichkeiten der Agenten, während sich deine Systeme und Prozesse weiterentwickeln.
  <br />

## Fazit

Coding-Agenten verändern den Softwareentwicklungszyklus, indem sie routinemäßige, mehrstufige Aufgaben übernehmen, die Entwicklungsteams bisher ausgebremst haben. Mit lang anhaltender Analysefähigkeit, einheitlichem Kontext zur Codebasis und der Fähigkeit, echte Tools auszuführen, übernehmen diese Agenten inzwischen Aufgaben von der Definition des Umfangs und dem Prototyping über Implementierung, Tests und Review bis hin zur operativen Triage. Entwicklungsteams behalten die klare Kontrolle über Architektur, Produktziele und Qualität. Coding-Agenten erstellen jedoch zunehmend die Erstimplementierung und arbeiten in jeder Phase des SDLC kontinuierlich mit.

Dieser Wandel erfordert keinen radikalen Umbau. Der Nutzen kleiner, gezielter Arbeitsabläufe wächst schnell, während Coding-Agenten leistungsfähiger und zuverlässiger werden. Teams, die mit klar abgegrenzten Aufgaben beginnen, geeignete Leitplanken etablieren und den Verantwortungsbereich der Agenten schrittweise erweitern, erzielen spürbare Fortschritte: Sie arbeiten schneller und konsistenter und können sich besser auf zentrale Entwicklungsaufgaben konzentrieren.

Wenn du untersuchst, wie Coding-Agenten die Arbeit in deiner Organisation beschleunigen können, oder deine erste Bereitstellung vorbereitest, wende dich an OpenAI. Wir helfen dir, mit Coding-Agenten spürbare Vorteile zu erzielen: Wir gestalten durchgängige Arbeitsabläufe für Planung, Design, Implementierung, Tests, Review und Betrieb und unterstützen dein Team dabei, produktionsreife Muster einzuführen, mit denen sich KI-native Softwareentwicklung in der Praxis umsetzen lässt.

[image1]: /images/codex/guides/build-ai-native-engineering-team.png

<!-- source: https://learn.chatgpt.com/de-DE/use-cases/refactor-your-codebase -->

## Einführung

Wenn sich in deiner Codebasis ungenutzter Code, doppelte Logik, veraltete Abstraktionen, große Dateien oder Legacy-Muster angesammelt haben und dadurch jede Änderung aufwendiger als nötig geworden ist, solltest du erwägen, die technischen Schulden durch eine Refaktorierung abzubauen. Bei einer Refaktorierung verbesserst du die Struktur des bestehenden Systems, ohne daraus eine Migration des Technologie-Stacks zu machen.

Codex kann sich hier zunächst einen Überblick über den unübersichtlichen Bereich verschaffen und die Bereinigung dann in kleinen, gut überprüfbaren Schritten umsetzen: ungenutzte Codepfade löschen, große Module entflechten, doppelte Codepfade zusammenführen, alte Framework-Muster modernisieren und jeden Schritt mit gezielten Prüfungen absichern.

Ziel ist es, die bestehende Codebasis zu verbessern, ohne sie zu migrieren:

1. Entferne ungenutzten Code, veraltete Hilfsfunktionen, alte Flags und nicht mehr benötigte Kompatibilitäts-Shims.
2. Verschlanke überladene Module, indem du Hilfsfunktionen extrahierst, Komponenten aufteilst oder Seiteneffekte an klar definierten Grenzen bündelst.
3. Ersetze Legacy-Muster durch die aktuellen Konventionen des Repositorys: neuere Framework-Bausteine, klarere Typen, einfachere Zustandsflüsse oder Hilfsfunktionen der Standardbibliothek.
4. Sorge dafür, dass das nach außen sichtbare Verhalten stabil bleibt und die nächste Änderung weniger Aufwand verursacht.

## So gehst du vor

1. Bitte Codex, sich vor der Bearbeitung einen Überblick über den Bereich zu verschaffen: überladene Module, doppelte Logik, ungenutzter Code, Tests, öffentliche Schnittstellenverträge und alle alten Muster, die im Repository inzwischen überholt sind.
2. Wähle jeweils nur ein Thema für die Bereinigung: ungenutzten Code entfernen, den Kontrollfluss vereinfachen, ein veraltetes Muster modernisieren oder eine große Datei in kleinere Teile mit klarer Zuständigkeit aufteilen.
3. Bevor Codex Dateien ändert, lass dir das aktuelle Verhalten, die geplante strukturelle Verbesserung und die kleinste Prüfung nennen, die belegen soll, dass das Verhalten stabil geblieben ist.
4. Überprüfe nach jedem Schritt die Änderungen und führe die kleinste sinnvolle Prüfung aus, statt die gesamte Bereinigung in einem einzigen Diff zu bündeln.
5. Behandle Änderungen am Technologie-Stack, Abhängigkeitsmigrationen und Architekturumstellungen als separate Aufgaben, es sei denn, sie sind für den Abschluss der Bereinigung erforderlich.

  Du kannst im Planmodus einen Plan für die Refaktorierung erstellen, bevor du mit der
Arbeit beginnst.

## ExecPlans nutzen

Das [Kochbuch zur Codemodernisierung](/cookbook/examples/codex/code_modernization) stellt ExecPlans vor: Dokumente, mit denen Codex den Überblick über die Bereinigung behalten, den angestrebten Endzustand festhalten und die Validierung nach jedem Schritt protokollieren kann.
Sie eignen sich, wenn die Refaktorierung mehrere Module umfasst oder mehr als eine Sitzung dauert. Dokumentiere darin Löschungen, Änderungen an Mustern und Verträge, die stabil bleiben mussten, sowie weiterhin zurückgestellte Arbeiten.

## Skills für wiederkehrende Muster nutzen

[Skills](/de-DE/codex/build-skills) sind hilfreich, wenn dieselben Bereinigungsregeln in verschiedenen Repositorys, Diensten oder Teams immer wieder gelten. Nutze frameworkspezifische Skills, sofern sie verfügbar sind, ergänze bei riskanten Bereinigungen Sicherheits- und CI-Skills und erstelle einen Team-Skill, wenn du eine bewährte Checkliste für das Entfernen ungenutzten Codes, das Extrahieren von Modulen oder das Modernisieren von Legacy-Mustern hast.
Wenn du denselben Modernisierungsschritt in mehreren Codebasen durchführst, kann Codex dir helfen, aus dem ersten erfolgreichen Durchlauf einen wiederverwendbaren Skill zu machen.

<!-- source: https://learn.chatgpt.com/de-DE/use-cases/code-migrations -->

## Einführung

Beim Wechsel von einem Stack zu einem anderen kannst du mit Codex die einzelnen Komponenten dem Ziel-Stack zuordnen und die Migration kontrolliert durchführen: Routing, Datenmodelle, Konfiguration, Authentifizierung, Hintergrundjobs, Build-Tools, Deployment, Tests oder sogar die Konventionen der Programmiersprache und des Frameworks selbst.

Codex ist hier hilfreich, weil Codex den Bestand des Legacy-Systems erfassen, die Konzepte des alten Systems den neuen Konzepten zuordnen und die Änderung in Etappen umsetzen kann, statt alles in einem einzigen umfassenden Rewrite neu zu schreiben. Das ist wichtig, wenn du ein Legacy-Framework ablöst, auf eine neue Laufzeitumgebung portierst oder einen Stack schrittweise durch einen anderen ersetzt, während das Produkt durchgehend funktionieren muss.

## So gehst du vor

1. Erfasse zunächst den Migrationsumfang: Legacy-Pakete, Framework-Konventionen, Routing, Datenzugriff, Authentifizierung, Konfiguration, Build-Tools, Tests, Annahmen zum Deployment und alle externen Schnittstellenverträge, die bei der Migration erhalten bleiben müssen.
2. Bitte Codex, die Konzepte des Legacy-Systems auf den Ziel-Stack abzubilden und deutlich zu benennen, wofür es keine direkte Entsprechung gibt.
3. Wähle eine schrittweise Strategie: eine Kompatibilitätsschicht, eine modulweise Portierung, Branch by Abstraction oder eine Ablösung nach dem Strangler-Pattern, die jeweils an einer Systemgrenze ansetzt.
4. Behalte das bestehende Verhalten bei, bis die Migration selbst eine sichtbare Änderung erzwingt, und benenne diese Ausnahmen ausdrücklich.
5. Führe nach jeder Etappe nur die Prüfungen aus, die zum Nachweis der Funktionsparität erforderlich sind: Linting, Typprüfung, gezielte Tests, Contract-Tests, Smoke-Tests oder ein direkter Vergleich mit dem Legacy-Pfad.
6. Überprüfe nach jedem Prüfpunkt den Diff und das verbleibende Risiko der Umstellung, statt bis zum vollständigen Rewrite zu warten.

## ExecPlans nutzen

In unserem [Cookbook zur Codemodernisierung](/cookbook/examples/codex/code_modernization) stellen wir ExecPlans vor: Dokumente, mit denen Codex alle Bereinigungsarbeiten im Blick behält, den angestrebten Endzustand genau beschreibt und die Validierung nach jedem Durchlauf protokolliert.
Wenn du Codex mit einer komplexen Migration beauftragst, lass Codex für jeden Teil des Systems einen ExecPlan erstellen, damit sämtliche Entscheidungen einschließlich der Wahl des Technologie-Stacks dokumentiert und später überprüft werden können.

## Mit einem Ziel kombinieren

Nutze für länger dauernde Teilmigrationen ein [Ziel](/de-DE/codex/use-cases/follow-goals), um Codex durch die Arbeit zu führen. Definiere für das Ziel einen klaren Endzustand, Prüfungen auf Funktionsparität, Vorgaben für Rollbacks und ein Abbruchkriterium.

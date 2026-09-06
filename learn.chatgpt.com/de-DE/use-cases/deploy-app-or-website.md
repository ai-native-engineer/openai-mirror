<!-- source: https://learn.chatgpt.com/de-DE/use-cases/deploy-app-or-website -->

## Beginne mit der Website und dem Deployment-Ziel

Codex kann eine Website oder App entwickeln oder aktualisieren, die Projektprüfungen ausführen, sie mit Vercel bereitstellen und die URL zurückgeben.

Am besten übergibst du Codex etwas Konkretes: ein Repository, einen Screenshot, eine Karte, ein Design-Briefing, eine Produktnotiz, eine API-Dokumentation oder eine Datenquelle. Codex sollte das Projekt prüfen, bevor es Änderungen daran vornimmt, und anschließend das Vercel-Plug-in verwenden, um standardmäßig eine Vorschau bereitzustellen.

Verwende `@build-web-apps`, wenn Codex die App entwickeln oder optimieren soll. Verwende `@vercel`, wenn Codex die App bereitstellen, das Deployment prüfen oder Vercel-Build-Protokolle lesen soll.

## Prüfe das Ergebnis, bevor du es teilst

Codex sollte dir mitteilen, was es geändert hat, mit welchem Befehl es den Build des Projekts ausgeführt hat und ob das Vercel-Deployment bereit ist. Wenn für das Deployment noch eine Umgebungsvariable gesetzt, ein Team ausgewählt, eine Domain-Einstellung vorgenommen oder eine Anmeldung durchgeführt werden muss, sollte Codex darauf hinweisen, anstatt den Eindruck zu erwecken, die Website sei fertig.

Gib ausdrücklich an, wenn die Produktionsumgebung geändert werden soll. Standardmäßig wird eine Vorschau bereitgestellt; fordere ein Produktions-Deployment nur an, wenn das wirklich dein Ziel ist.

## Arbeite mit der Live-URL weiter

Sobald die Vorschau verfügbar ist, arbeite im selben Chat weiter. Bitte Codex, die URL zu öffnen, Layoutprobleme zu beheben, Texte zu aktualisieren, fehlende Daten anzubinden oder die Vercel-Protokolle zu lesen, falls das Deployment fehlschlägt. Der Chat enthält bereits den Kontext zum Repository, zum Deployment und zum Build.

Gute Folgeanfragen sind konkret formuliert:

- „Das Layout auf Mobilgeräten ist zu eng. Korrigiere es und stelle die Vorschau erneut bereit.“
- „Verwende dasselbe Projekt und füge die neuesten Daten aus \[source\] hinzu.“
- „Lies die Protokolle des fehlgeschlagenen Builds und behebe den Fehler beim Deployment.“

<!-- source: https://learn.chatgpt.com/de-DE/docs/security/plugin/fix-findings -->

Verwende Codex Security, um einen akzeptierten Sicherheitsbefund mit einem gezielten,
verifizierten Patch zu beheben. Du kannst im Security-Arbeitsbereich arbeiten oder den Workflow zur Behebung
über einen Prompt, die Befehlszeile oder CI/CD ausführen. Codex validiert den Befund
und fügt, sofern Tests gefahrlos und praktikabel sind, einen gezielten Regressionstest hinzu, der
vor der Behebung fehlschlägt und danach erfolgreich durchläuft. Außerdem prüft Codex, ob zulässiges
Verhalten weiterhin funktioniert. Ist ein Regressionstest nicht gefahrlos oder nicht durchführbar, dokumentiert Codex
die Nachweislücke und stellt stattdessen das aussagekräftigste wiederholbare Validierungsartefakt
bereit.

Beginne mit einem akzeptierten Befund und prüfe den vorgeschlagenen Patch sowie die
Verifizierungsnachweise. Wenn der Workflow deinen Standards entspricht, bearbeite weitere akzeptierte
Befunde nacheinander in separaten Codex-Aufgaben oder CI/CD-Jobs. Wenn jede Aufgabe klar abgegrenzt
bleibt, lassen sich die zugehörigen Codeänderungen und Nachweise leichter prüfen.

## Einen Befund in der UI beheben

Öffne unter **Befunde** einen akzeptierten Befund oder unter **Scans** einen abgeschlossenen Scan.
Prüfe die zugehörigen Nachweise und verwende dann **Patch**, um eine einzelne gezielte Fehlerbehebung zu generieren, zu prüfen und anzuwenden
sowie zu verifizieren.

1. Generiere einen gezielten Patch

   Öffne den Befund, wähle den Tab **Patch** und dann **Patch generieren** aus.
   Codex validiert oder reproduziert das Problem, sofern möglich, und erstellt den Patch
   als Artefakt, ohne den ausgewählten Checkout zu ändern.

2. Prüfe den vorgeschlagenen Diff

   Prüfe jede geänderte Quelldatei, jeden Regressionstest und jedes Validierungsartefakt. Lehne
umfangreiche Refactorings, Bereinigungen ohne Bezug zum Befund oder Änderungen ab, die einen anderen
Sicherheitsmechanismus schwächen.

3. Wende den Patch lokal an

   Wähle **Patch anwenden** erst aus, wenn der Diff akzeptabel ist. Codex wendet den
   generierten Patch unverändert auf das Arbeitsverzeichnis an und protokolliert diesen Zustand. Prüfe den
   Diff des Arbeitsverzeichnisses, bevor du fortfährst.

4. Verifiziere die Fehlerbehebung

   Wähle **Fehlerbehebung verifizieren** aus. Codex führt das ursprüngliche Reproduktionsverfahren oder die aussagekräftigste
   verfügbare Exploit-Prüfung erneut aus. Wenn ein Regressionstest gefahrlos und praktikabel ist, prüft Codex,
   ob er vor der Fehlerbehebung fehlschlägt und danach erfolgreich durchläuft. Wenn der Test
   nicht gefahrlos oder nicht durchführbar ist, dokumentiert Codex die Nachweislücke und stellt stattdessen das
   aussagekräftigste wiederholbare Validierungsartefakt bereit. Außerdem prüft Codex
   zulässiges Verhalten, naheliegende Umgehungswege und relevante Repository-Tests.

5. Schließe den Befund bewusst

   Durch die Verifizierung wird ein Befund nicht automatisch geschlossen. Prüfe die Befehle,
Ergebnisse und die verbleibende Nachweislücke. Schließe den Befund anschließend mit einer zutreffenden
Begründung oder lasse ihn für weitere Arbeiten offen.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Prüfe die generierte Sicherheitskorrektur, bevor du sie auf deinen Checkout anwendest.
  </figcaption>
</figure>

## Einen Befund über die CLI beheben

Verwende die Codex CLI für einen akzeptierten Befund aus einem Scan, einem Ticket, einem Sicherheitshinweis,
einer Offenlegung, einer Sicherheitsbewertung oder einer internen Überprüfung.

Installiere Codex Security in dem `CODEX_HOME`, das `codex exec` verwendet, bevor du
diese Befehle ausführst. Ein neuer CI-Runner enthält Marketplace-Plug-ins
standardmäßig nicht.

```text
Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.

Gib die bekannte Quelle, Senke, von Angreifenden kontrollierte Eingabe, Auswirkung, erwartete Invariante,
das Reproduktionsverfahren, die betroffenen Dateien und den Validierungsbefehl an. Codex kann im
Repository nach fehlenden technischen Details suchen. Codex sollte nachfragen, bevor es von einer
Produktvorgabe oder vorgesehenen Sicherheitsinvariante ausgeht.

Checke für eine automatisierte Ausführung den Code aus, stelle den Befundbericht bereit
und installiere das Plug-in im `CODEX_HOME` des Runners. Aktiviere anschließend Schreibzugriff auf den Workspace
und übergib den Prompt an `codex exec`:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

## Befunde in CI/CD scannen und beheben

Installiere Codex Security im `CODEX_HOME` des Runners, bevor du einen der beiden
Skills aufrufst. Die folgenden Befehle verwenden das installierte Plug-in; sie installieren es nicht.

Trenne in CI/CD den Änderungsscan von der Behebung und verlange, dass der Scan den
Checkout unverändert lässt. Bewahre das Verzeichnis des abgeschlossenen Scans als Job-Artefakt
auf, prüfe die Befunde und starte für jeden zur Behebung akzeptierten Befund eine separate
Codex-Aufgabe oder einen separaten Job.

Standardmäßig verwendet `codex exec` eine Sandbox ohne Schreibzugriff. Führe sowohl den Änderungsscan als auch
die Behebung mit `--sandbox workspace-write` aus. Der Scan benötigt diese Berechtigung,
um temporäre Artefakte zu speichern. Sein Prompt muss aber weiterhin die Anweisung `Do not modify
the checkout` enthalten. Die Behebung benötigt dieselbe Berechtigung, um den gezielten
Patch und die Verifizierungsnachweise in den Workspace zu schreiben. Weitere Informationen findest du unter [Berechtigungen und
Sicherheit](/de-DE/codex/non-interactive-mode#permissions-and-safety).

Für jeden Scan und jeden akzeptierten Befund:

1. Ermittle die Basis- und Head-Revision für die Änderung.
2. Führe `$codex-security:security-diff-scan` für diesen Diff aus, ohne den
   Checkout zu ändern.
3. Bewahre das vollständige Scanverzeichnis auf und wähle die zu behebenden Befunde aus.
4. Rufe `$codex-security:fix-finding` einmal für jeden akzeptierten Befund auf und übergib
   dabei die jeweilige Befund-ID und das Verzeichnis des abgeschlossenen Scans.
5. Generiere einen gezielten Patch und füge einen Regressionstest hinzu, der vor der
Fehlerbehebung fehlschlägt und danach erfolgreich durchläuft. Wenn dieser Test nicht gefahrlos oder nicht durchführbar ist, dokumentiere die
Nachweislücke und verwende stattdessen das aussagekräftigste wiederholbare Validierungsartefakt.
6. Verifiziere das ursprüngliche Problem und das zulässige Verhalten. Gib jeden Patch, jeden Test
bzw. jedes alternative Validierungsartefakt, jeden Verifizierungsbefehl und jede etwaige Nachweislücke
separat zurück.

Scanne zuerst die Änderung, ohne den Checkout zu ändern:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:security-diff-scan to review changes from <base-revision> to <head-revision> for security regressions. Do not modify the checkout.'

Behebe dann einen akzeptierten Befund aus dem abgeschlossenen Scan:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <completed-scan-directory>. Validate the finding, generate one minimal patch, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

Wiederhole den zweiten Befehl für jeden verbleibenden
akzeptierten Befund in einer separaten Aufgabe oder einem separaten Job. Integriere jeden Patch nach der Verifizierung im Rahmen deines üblichen
Prozesses für Code-Reviews und Releases. Wenn du Befunde vor der
Behebung an ein anderes Team übergeben möchtest, siehe [Befunde exportieren oder
nachverfolgen](/de-DE/codex/security/plugin/export-findings).

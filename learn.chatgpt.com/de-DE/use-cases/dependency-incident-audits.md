<!-- source: https://learn.chatgpt.com/de-DE/use-cases/dependency-incident-audits -->

## Mit einem sicheren Auditplan beginnen

Wenn sich ein Vorfall im Zusammenhang mit Abhängigkeiten oder der Softwarelieferkette schnell entwickelt, hilft dir ein übereilter Patch zunächst nicht. Du brauchst einen klaren Auditplan: Was hat sich geändert, welche Pakete oder Arbeitsabläufe könnten betroffen sein und welche Belege würden nachweisen, dass dein Repository betroffen ist?

Nutze Codex, um aus dem Sicherheitshinweis eine Checkliste für ein bewusst vorsichtiges Vorgehen ohne Schreibzugriff zu erstellen, bevor du mit Installationen, Builds oder Tests beginnst oder etwas ausführst.

## Erste Prüfung ohne Schreibzugriff durchführen

1. Stelle Codex den öffentlichen Sicherheitshinweis, den Vorfallbericht oder die Liste der betroffenen Pakete bereit.
2. Bitte Codex, maßgebliche Quellen von allgemeinen Kommentaren und Einschätzungen zu trennen.
3. Lass Codex festlegen, welche Belege eine Betroffenheit nachweisen oder ausschließen würden.
4. Lass Codex Manifeste, Lockfiles, CI-Arbeitsabläufe, Skripte und relevante Dateien im Repository prüfen.
5. Bitte Codex, die Ergebnisse nach dem Status der Belege, dem Schweregrad und dem empfohlenen nächsten Schritt zu gruppieren.

Führe bei Vorfällen mit Paketen keine Installations-, Build-, Test-, Import- oder Lifecycle-Befehle aus, bis du weißt, welche Komponenten laut dem Sicherheitshinweis betroffen sind. Codex kann Lockfiles und Arbeitsabläufe durchsuchen, ohne nicht vertrauenswürdigen Code auszuführen.

## Status der Belege getrennt vom Schweregrad angeben

Ein hilfreiches Auditergebnis sollte sowohl zeigen, wie schwerwiegend ein Befund wäre, als auch, wie belastbar die Belege sind:

  <p>
    <strong>Betroffenheit bestätigt:</strong> Das Lockfile enthält eine betroffene
    Paketversion in einem produktiv genutzten Abhängigkeitspfad.
  </p>
  <p>
    <strong>Überprüfung erforderlich:</strong> Ein CI-Job hat Berechtigungen zum Veröffentlichen, aber
    der Arbeitsablauf scheint das betroffene Paket nicht direkt zu installieren.
  </p>
  <p>
    <strong>Ausgeschlossen:</strong> Der Paketname kommt nur in der Dokumentation vor und ist nicht
    in Manifesten oder Lockfiles enthalten.
  </p>
  <p>
    <strong>Nächster Schritt:</strong> Prüfe die vorgeschlagene Aktualisierung der Abhängigkeiten und den Plan, Tokens
    zu rotieren, bevor du eine destruktive Maßnahme ergreifst.
  </p>

Sobald die Prüfung ohne Schreibzugriff abgeschlossen ist, kannst du Codex bitten, einen Pull Request zur Behebung vorzubereiten, die CI-Berechtigungen zu aktualisieren oder eine Notiz zur Nachbereitung des Vorfalls zu verfassen. Führe diese Schritte getrennt vom anfänglichen Audit aus.

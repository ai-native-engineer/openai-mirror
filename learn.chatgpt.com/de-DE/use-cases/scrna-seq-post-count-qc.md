<!-- source: https://learn.chatgpt.com/de-DE/use-cases/scrna-seq-post-count-qc -->

## Skills nutzen

Das NGS Analysis-Plug-in umfasst:

- `ngs-analysis-router`
- `scrna-seq-qc`
- `ngs-scrna-seq`

Wenn du das Plug-in verwendest, kann ChatGPT alle darin gebündelten Skills nutzen.

## Schritt-für-Schritt-Anleitung

1. Verweise ChatGPT auf die passende Matrix, die Barcodes, Gene oder Features, das Manifest und die Datensatzmetadaten oder gib genaue Dateireferenzen an.
2. Führe den Starter-Prompt aus, damit ChatGPT anhand der beobachteten Verteilungen QC-Schwellenwerte festlegen und die Begründung in den Artefakten des Durchlaufs dokumentieren kann.
3. Öffne den Visualisierungsindex und das Review-Notebook oder die Review-App. Prüfe dort, wie viele Zellen die QC bestanden bzw. nicht bestanden haben, und sieh dir die UMAPs sowie die Konfidenz der Annotationen an.
4. Arbeite im selben Chat weiter, um die Schwellenwerte zu verfeinern, einen passenden Referenzatlas bereitzustellen oder den Lauf erneut auszuführen, sobald die Doubletten-Erkennung nicht mehr blockiert ist.

## Ergebnisse

Der Durchlauf erzeugt eine Review-Oberfläche für die Filterentscheidungen und nicht nur
eine gefilterte Matrix. Beginne mit den Diagrammen zur Begründung der Schwellenwerte und einer Zusammenfassung der QC.
Daran erkennst du, wie viele Zellen jeder Filter entfernt oder markiert hat und
ob die gewählten Grenzwerte zu den beobachteten Verteilungen passen.

![Prüfe bei einem Einzelzell-Durchlauf die Diagramme zur Begründung der Schwellenwerte und wie viele Zellen die QC bestanden bzw. nicht bestanden haben.](/codex/use-cases/scrna-seq-post-count-qc-screenshot-1.webp)

Prüfe anschließend die erstellten UMAPs, aufgeschlüsselt nach groben Labels und Leiden-Clustern. Diese
Ansichten erleichtern es, Lücken in den Annotationen, verdächtige Cluster oder
gewählte Schwellenwerte zu erkennen, die noch einmal geprüft werden sollten.

![Prüfe UMAP-Diagramme, aufgeschlüsselt nach groben Labels und Leiden-Clustern.](/codex/use-cases/scrna-seq-post-count-qc-screenshot-2.webp)

Prüfe abschließend die Metriken auf Zellebene und die Filterergebnisse. ChatGPT speichert
diese Tabelle zusammen mit der gefilterten Datei im Format `.h5ad` und den Visualisierungsartefakten, sodass du
die Schwellenwerte im selben Chat überarbeiten kannst, ohne die Begründung des
ersten Durchlaufs zu verlieren.

![Öffne die QC-Metriken auf Zellebene und die Filterergebnisse zur Überprüfung.](/codex/use-cases/scrna-seq-post-count-qc-screenshot-3.webp)

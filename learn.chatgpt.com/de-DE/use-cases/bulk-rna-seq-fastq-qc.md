<!-- source: https://learn.chatgpt.com/de-DE/use-cases/bulk-rna-seq-fastq-qc -->

## Skills nutzen

Das NGS Analysis-Plug-in enthält:

- `ngs-analysis-router`
- `ngs-bulk-rnaseq-counts-qc`
- `ngs-runtime-env`

Wenn du das Plug-in verwendest, kann ChatGPT alle darin gebündelten Skills nutzen.

## Schritt-für-Schritt-Anleitung

1. Gib ChatGPT entweder ein Verzeichnis mit dem Probenblatt, den FASTQs, der Transkriptom-FASTA, der Genom-FASTA und der GTF-Datei oder genaue Verweise auf die einzelnen Dateien an.
2. Führe den Starter-Prompt aus, damit ChatGPT vor der Ausführung die Strangspezifität und die Konsistenz der Referenzdaten validieren und prüfen kann, ob die Tools einsatzbereit sind.
3. Öffne die erstellten MultiQC- und Matrixartefakte in ChatGPT, um die Mapping-Rate, Duplikation und Übereinstimmung beim Bibliothekstyp zu bewerten und zu prüfen, ob die Ressourcen einsatzbereit sind.
4. Arbeite im selben Chat weiter, um blockierende Probleme zu beheben, den Lauf mit aktualisierten Metadaten erneut auszuführen oder die entstandenen Matrizen auf Genebene für die anschließende Analyse der differentiellen Genexpression weiterzugeben.

## Ergebnisse

Der Lauf liefert statt einer reinen Quantifizierung
ein Paket mit QC-geprüften Zählwerten. Prüfe zuerst den MultiQC-Bericht auf Warnungen mit möglichen Auswirkungen
auf die spätere Interpretation der Ergebnisse. In diesem Beispiel zeigt ChatGPT Warnungen von FastQC
zum Sequenzinhalt zusammen mit der Laufzusammenfassung an, damit das Team entscheiden kann,
ob das beobachtete Muster für die Bibliothekspräparation zu erwarten ist.

![Prüfe die FastQC-Warnungen zum Sequenzinhalt zusammen mit der Laufzusammenfassung für bulk RNA-seq.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-1.webp)

Prüfe als Nächstes die Salmon-Statistiken im selben Bericht. Mapping-Raten,
Zuordnungen der Bibliothekstypen und Duplikationssignale zeigen auf einen Blick die Eignung der Daten
für die Analyse der differentiellen Genexpression.

![Prüfe im erstellten MultiQC-Bericht die Salmon-Statistiken zu Alignment und Bibliothekstyp.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-2.webp)

Die resultierende Zählwertmatrix auf Genebene wird als wiederverwendbares Artefakt gespeichert. Öffne sie
in ChatGPT, um zu prüfen, ob die erwarteten Proben und Merkmale vorhanden sind. Bewahre sie anschließend
zusammen mit den Provenienzdaten des Laufs für die anschließende Analyse auf.

![Öffne die erstellte Zählwertmatrix auf Genebene für die anschließende Prüfung.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-3.webp)

<!-- source: https://learn.chatgpt.com/de-DE/use-cases/discover-protein-folding-architectures -->

## Eine Architekturhypothese zur Proteinfaltung untersuchen

Verwende Codex im Zielmodus, wenn deine Hypothese zur Proteinfaltung mehr
als einen Implementierungsdurchlauf erfordert. Gib Codex eine klar abgegrenzte Forschungsrichtung, eine
funktionsfähige Ausgangsbasis und einen automatisch auswertbaren Benchmark. Codex kann
die Architekturvariante implementieren, Experimente nachverfolgen, Fehler diagnostizieren und weiter
iterieren, während du die Evidenz prüfst.

Dieses Beispiel ging von einer konkreten Frage aus: Könnte ein AlphaFold2-artiges Modell
eine nützliche Proteingeometrie effizienter erlernen, wenn sein Trunk nicht
nur Residuen und Residuenpaare, sondern auch explizite topologische Objekte
höherer Ordnung darstellen würde?

## Ein klar begrenztes Experiment definieren

AlphaFold2 nutzt im Evoformer bereits leistungsfähige paarweise und dreiecksbasierte
Verarbeitung. Die Dreiecksoperationen verbessern die Kantenrepräsentationen, schreiben ihre Ergebnisse aber weiterhin
in einen Paartensor zurück. Der wissenschaftliche Vorschlag war, zu prüfen, ob persistente
erlernte Repräsentationen für dreieckige Flächen und tetraedrische Zellen
bei begrenzter Datenmenge einen nützlichen induktiven Bias liefern könnten.

Das daraus entstandene öffentliche Repository, [SimplexFold](https://github.com/ChrisHayduk/SimplexFold),
führt dünn besetzte Flächenzustände `F_ijk` und tetraedrische Zustände `U_ijkl` neben der
herkömmlichen paarweisen Repräsentation `Z_ij` ein.

```text
MSA representation M
        <-> pair / edge tensor Z_ij
        <-> sparse face tensor F_ijk
        <-> sparse tetra tensor U_ijkl
        -> structure module
        -> recycled geometry
        loops back into the next pass

Beginne mit dem Starter-Prompt auf dieser Seite, einer minimalen AlphaFold2-artigen Ausgangsbasis
und dem öffentlichen NanoFold-Benchmark. Der Benchmark bietet eine kleine, kuratierte
Datengrundlage mit festem Datenbestand, die automatisch auswertbar ist und sich für strukturbiologische
Experimente eignet. Halte die erste Implementierung so klein, dass du sie
mit gezielten Unit-Tests und Mikrobenchmarks prüfen kannst, bevor du aufwendige Trainingsläufe
startest.

## Die Suche mit dem Zielmodus durchführen

1. Gib eine falsifizierbare, übergeordnete wissenschaftliche Hypothese vor, statt das Modell aufzufordern, von Grund auf eine vollständige Forschungsagenda zu entwerfen.
2. Nutze GPT-5.5 Pro in ChatGPT, um aus diesem Ansatz einen Implementierungsplan mit klaren Einschränkungen und Ablationsstudien zu entwickeln.
3. Bitte Codex, [SimplexFold](https://github.com/ChrisHayduk/SimplexFold) als kleinstmögliche ausführbare Ausgangsbasis zu implementieren und anschließend mit gezielten Unit-Tests und Mikrobenchmarks zu überprüfen.
4. Übergib das entstandene Repository an Codex im Zielmodus und weise Codex an, den Validierungswert `lDDT-Cα` beim NanoFold-Benchmark schrittweise zu steigern und dabei Experimentprotokolle, Pläne und Verweise auf Artefakte aufzubewahren.
5. Lass den Zielmodus kontinuierlich laufen, während er die Architektur, das Trainingsverfahren und das experimentelle Harness anhand des Benchmark-Feedbacks iterativ weiterentwickelt. In diesem Beispiel lief die Schleife mehr als 150 Stunden lang.

Verwende `PLAN.md` für die aktuelle Strategie und die nächsten Schritte, `EXPERIMENTS.md` für ein
strukturiertes Ergebnisprotokoll und `EXPERIMENT_NOTES.md` als fortlaufendes Arbeitsnotizbuch.
Diese Artefakte machen eine lang laufende Suche nachvollziehbar und bieten dir einen festen
Ort, an dem du die nächste Iteration steuern kannst.

Der Zielmodus eignet sich hier, weil die Suche wiederholte Implementierungen,
Tests, Experimentnachverfolgung, Fehlerdiagnosen und benchmarkgestützte
Iterationen erfordert. Ungesteuerte automatisierte Forschung lief häufig auf bekannte lokale Änderungen
an Verlustfunktionen, Optimierern und Hyperparametern hinaus. Eine kompakte, von Forschenden vorgegebene
Architekturhypothese gab Codex einen zielführenderen Suchraum vor und ließ zugleich
genug Spielraum, um die Implementierung zu testen, Fehler zu diagnostizieren und sie zu verfeinern.

Dieser Workflow eignet sich auch für Teams, die untersuchen, wie sich die Einbindung von Forschenden
in die Steuerung auf die Qualität agentengestützter wissenschaftlicher Suche auswirkt.

## Beispielergebnis

Das Ergebnis dieses Workflows war [SimplexFold](https://github.com/ChrisHayduk/SimplexFold),
eine experimentelle Architektur mit expliziten Simplex-Zuständen höherer Ordnung. Prüfe
die Topologie zusammen mit den Benchmark-Protokollen, um sicherzustellen, dass jede Iteration weiterhin
die ursprüngliche wissenschaftliche Idee testet.

![Ein Vergleich von Proteingeometrien mit 1-, 2- und 3-Simplizes.](/codex/use-cases/discover-protein-folding-architectures-simplex.webp)

Die entscheidende Erkenntnis ist nicht, dass Codex die Proteinfaltung autonom gelöst hätte. Der
Workflow zeigt vielmehr, wie der Zielmodus als kontinuierliche wissenschaftlich-technische Iterationsschleife
dienen kann: Forschende geben den konzeptionellen Impuls, und Codex verkürzt den
Zyklus aus Implementierung, Experimenten, Debugging und weiterführender Suche.

Betrachte vielversprechende Diagnoseergebnisse als Beleg dafür, dass der Implementierungsweg funktioniert,
nicht als Nachweis der Generalisierbarkeit. Überprüfe regelmäßig den Verlauf des Agenten,
lenke ihn zurück zu wissenschaftlich relevanten Architekturfragen, wenn er
in lokale Hyperparameteroptimierung abgleitet, und mache weitergehende Aussagen erst nach
Vergleichen mit öffentlichen Validierungsdaten unter gleichen Bedingungen und mit angemessenen Replikaten.

## Ressourcen

- [SimplexFold-Repository](https://github.com/ChrisHayduk/SimplexFold)
- [Benchmarkplan für SimplexFold](https://github.com/ChrisHayduk/SimplexFold/blob/main/BENCHMARK_PLAN.md)
- [NanoFold-Wettbewerb](https://github.com/ChrisHayduk/nanoFold-Competition)
- [Regeln des NanoFold-Wettbewerbs](https://github.com/ChrisHayduk/nanoFold-Competition/blob/main/docs/COMPETITION.md)
- [Zielmodus mit mehr als 150 Stunden Laufzeit](https://x.com/ChrisHayduk/status/2055757345506877759?s=20)
- [Artikel zum Zielmodus](https://x.com/ChrisHayduk/status/2053807198870880743?s=20)

<!-- source: https://learn.chatgpt.com/de-DE/use-cases/iterate-on-difficult-problems -->

## Einführung

Einige Aufgaben lassen sich in einem einzigen Durchgang leicht überprüfen: Der Build ist erfolgreich, die Tests sind grün und die Aufgabe ist erledigt. Manche Optimierungsprobleme sind jedoch schwer zu lösen und erfordern viele Iterationen mit einer engmaschigen Evaluierungsschleife. Um zu erkennen, welche Richtung sinnvoll ist, muss Codex die aktuelle Ausgabe prüfen, bewerten, die nächste Änderung festlegen und diesen Ablauf wiederholen, bis das Ergebnis tatsächlich gut ist.

Diese Art von Anwendungsfall lässt sich gut mit einer individuellen Benutzeroberfläche kombinieren, in der du den Fortschritt visuell nachvollziehen kannst, während Codex die Ausgaben und erzeugten Artefakte jeder Iteration protokolliert.
In der App kannst du beobachten, wie Codex weiterarbeitet und sich das Zielartefakt, die Modellausgabe oder das erzeugte Asset dabei stetig verbessert.
Entscheidend ist, Codex die nötigen Skripte bereitzustellen, mit denen die Evaluierungsmetriken und die zu prüfenden Artefakte erzeugt werden.

## Mit Evals beginnen

Lege vor Beginn der Aufgabe fest, wie der Erfolg gemessen wird. Das beste Setup kombiniert in der Regel:

- **Deterministische Prüfungen:** Aspekte, die Skripte direkt bewerten können, beispielsweise Verstöße gegen Vorgaben oder deterministische, per Code berechnete Metriken
- **Prüfungen mit einem LLM als Bewertungsinstanz:** kriterienbasierte Bewertungen für Eigenschaften, die sich nur schwer exakt formalisieren lassen, etwa Ähnlichkeit, Lesbarkeit, Nützlichkeit oder Gesamtqualität. Dabei können Text- oder Bildausgaben herangezogen werden

Wenn subjektive Aspekte wichtig sind, gib Codex ein Skript, das beispielsweise über die [Responses API](/api/reference/resources/responses/methods/create) ein Modell aufrufen und strukturierte Bewertungen zurückgeben kann. Deterministische Prüfungen sollen dadurch nicht ersetzt, sondern um eine konsistente Bewertungsinstanz für die Aspekte ergänzt werden, die Menschen sonst nach Augenschein beurteilen müssten.

Die Schleife funktioniert am besten, wenn die Eval-Ausgabe maschinenlesbar ist, nach jedem Durchlauf gespeichert wird und sich im Zeitverlauf leicht vergleichen lässt.

  **Tipp**: Bitte Codex, das Evaluierungsskript für dich zu erstellen, und beschreibe dabei die
  Prüfungen, die du ausführen möchtest.

## Lege für Codex eine Abbruchbedingung fest

Bei schwierigen Aufgaben verliert die Bearbeitung leicht die klare Richtung, wenn im Prompt nur „weiter verbessern“ steht, aber nicht, wann Schluss ist. Formuliere die Abbruchbedingung ausdrücklich.

Ein praxistaugliches Muster sieht so aus:

1. Lege einen Zielwert für die Gesamtpunktzahl fest.
2. Lege einen separaten Zielwert für die durchschnittliche Bewertung durch das LLM fest.
3. Weise Codex an, fortzufahren, bis beide Werte über dem Schwellenwert liegen, nicht nur einer.

Wenn das Ziel beispielsweise ein hochwertiges Artefakt ist, bitte Codex, weiterzumachen, bis sowohl die Gesamtpunktzahl als auch der Durchschnitt der LLM-Bewertungen über 90 % liegen. Damit ist die Aufgabe klar messbar: Codex erkennt, ob das Ergebnis noch unter dem Zielwert liegt, wo noch Verbesserungspotenzial besteht und ob die letzte Änderung geholfen hat.

## Die Schleife fortlaufend protokollieren

Lang laufende Aufgaben lassen sich wesentlich zuverlässiger bearbeiten, wenn Codex Notizen zur Schleife führt, statt sich nur auf den Chat-Kontext zu verlassen.

Dieses fortlaufende Protokoll sollte Folgendes enthalten:

- die aktuell besten Punktzahlen
- was sich in der letzten Iteration geändert hat
- was sich laut Eval verbessert oder verschlechtert hat
- was Codex als Nächstes ausprobieren will

Das ist besonders wichtig, wenn eine Aufgabe lange läuft. Das Protokoll dient dann als Ausgangspunkt für die Wiederaufnahme und als Dokumentation der Selbstevaluierung des aktuellen Durchlaufs.

## Nicht nur die Protokolle, sondern auch das Artefakt prüfen

Bei manchen schwierigen Aufgaben reichen der Code-Diff und die ausgegebenen Metriken nicht aus. Codex sollte das erzeugte Artefakt selbst prüfen.

Wenn die Ausgabe visuell ist, etwa ein erzeugtes Bild, ein Layout oder ein gerenderter Zustand, lass Codex dieses Artefakt direkt prüfen. Das gilt beispielsweise, wenn die Ausgabe im Dateisystem als Bilddatei gespeichert ist. Codex sollte das aktuelle Ergebnis mit dem bisher besten Ergebnis oder mit den festgelegten Bewertungskriterien vergleichen.

So wird die Schleife robuster:

- das Eval-Skript gibt die Punktzahl aus
- das Artefakt zeigt, was in der Bewertung nicht erfasst wurde
- die nächste Änderung stützt sich auf beides

Diese Kombination ist wesentlich effektiver, als den Code zwischen den Durchläufen ohne klare Grundlage zu ändern.

## Jede Iteration klar strukturieren

Bitte Codex, bei jedem Durchlauf dieselbe Schleife einzuhalten:

1. Führe die Evals für den aktuellen Ausgangsstand aus.
2. Ermittle anhand der Punktzahlen und Artefakte die größte Schwachstelle.
3. Nimm eine gezielte Änderung vor, die diesen Engpass behebt.
4. Führe die Evals erneut aus.
5. Protokolliere die neuen Punktzahlen und ob die Änderung geholfen hat.
6. Fahre fort, bis die Schwellenwerte erreicht sind.

Dieses konsequente Vorgehen ist wichtig. Wenn Codex in einer Iteration zu viele Dinge auf einmal ändert, lässt sich nicht erkennen, welcher Ansatz die Punktzahl verbessert hat. Wenn Codex nichts protokolliert, ist die Verlässlichkeit der Arbeit schwer einzuschätzen und die Aufgabe lässt sich nur schwer fortsetzen.

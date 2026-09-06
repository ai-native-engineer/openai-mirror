<!-- source: https://learn.chatgpt.com/de-DE/use-cases/ios-swiftui-view-refactor -->

## Einen Screen refaktorieren, ohne sein Verhalten zu ändern

Dieser Anwendungsfall ist für Situationen gedacht, in denen eine SwiftUI-Datei zu einem einzigen riesigen Screen angewachsen ist und jede kleine Änderung riskant erscheint. Ziel ist weder, die Funktion neu zu gestalten, noch eine neue Architektur zu erfinden. Bitte Codex, Verhalten und Layout beizubehalten und den Screen anschließend in kleine Unteransichten mit explizitem Datenfluss aufzuteilen. So lässt sich die nächste Änderung leichter überprüfen.

Nutze das [Build iOS Apps-Plug-in](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) für diese Art der Bereinigung. Sein Skill zur Refaktorierung von SwiftUI-Views verfolgt einen klaren, nützlichen Ansatz: Setze standardmäßig auf MV statt auf MVVM, belasse die Geschäftslogik in Services oder Modellen, nutze zuerst lokalen View-Zustand und Umgebungsabhängigkeiten und behalte ein View Model nur bei, wenn die Funktion eindeutig eines benötigt.

## Was Codex tun soll

Nenne zuerst eine konkrete Screen-Datei und bitte Codex, das Verhalten beizubehalten und zugleich die Struktur zu verbessern. Diese Regeln für die Refaktorierung solltest du direkt in deinen Prompt aufnehmen:

- Ordne die Datei so, dass Umgebungsabhängigkeiten, gespeicherte Eigenschaften, berechnete Zustandswerte, die keine Views erzeugen, `init`, `body`, View-Hilfsfunktionen und Hilfsmethoden von oben nach unten leicht zu erfassen sind.
- Extrahiere aussagekräftige Abschnitte in eigene Typen, die `View` implementieren und mit wenigen expliziten Eingaben, `@Binding`s und Callbacks auskommen.
- Verwende berechnete Hilfsfunktionen, die `some View` zurückgeben, nur selten und halte sie klein. Baue einen riesigen Screen nicht als lange Liste privater berechneter View-Fragmente neu auf.
- Verschiebe nicht triviale Button-Aktionen und Nebeneffekte aus `body` in kleine Methoden und echte Geschäftslogik in Services oder Modelle.
- Halte den View-Baum auf oberster Ebene stabil. Bevorzuge lokale Bedingungen in Abschnitten oder Modifiern gegenüber Verzweigungen mit `if/else` auf oberster Ebene, die ganze Screens austauschen.
- Sorge dabei auch in Observation für korrekte Besitzverhältnisse. Bei Modellen mit `@Observable` auf oberster Ebene sollte die verantwortliche View sie unter iOS 17+ mithilfe von `@State` speichern; ältere Observable-Wrapper solltest du nur verwenden, wenn dein Deployment-Target dies erfordert.

## Bitte Codex um einen kurzen Validierungszyklus

Verhaltenserhaltende Refaktorierungen sollten belegt werden. Bitte Codex, nach jeder sinnvollen Extraktion die kleinste sinnvolle Prüfung per Build, Vorschau, Test oder Simulator auszuführen, die den Screen abdeckt. Lass Codex anschließend zusammenfassen, was sich strukturell geändert hat und was bewusst unverändert geblieben ist.

## Praktische Tipps

### Erst aufteilen, dann die Architektur diskutieren

Wenn ein Screen zu groß ist, bitte Codex zunächst, Abschnittsansichten zu extrahieren, bevor du eine neue Abstraktionsebene einführst. Ein kürzerer, expliziterer View-Baum macht ein View Model oft vollständig überflüssig.

### Halte die Schnittstelle jeder Unteransicht so klein wie möglich

Bevorzuge mit `let` deklarierte Werte, `@Binding`s und Callbacks für genau einen Zweck, statt jeder untergeordneten View das gesamte übergeordnete Modell zu übergeben. So kannst du jeden extrahierten Abschnitt leichter in der Vorschau darstellen und koppelst ihn nicht so leicht versehentlich wieder an den gesamten Screen.

### Lass Codex ausdrücklich nennen, was unverändert bleibt

Für eine risikoarme Refaktorierung ist es hilfreich, wenn Codex ausdrücklich aufführt, was nicht geändert wurde: Geschäftsregeln, Navigationsverhalten, Persistenz, Analytics-Semantik und das für Nutzende sichtbare Layout. Das beschleunigt die Review deutlich.

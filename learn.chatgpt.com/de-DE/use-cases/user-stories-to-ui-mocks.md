<!-- source: https://learn.chatgpt.com/de-DE/use-cases/user-stories-to-ui-mocks -->

## Einführung

Produktteams sammeln Feedback häufig aus unterschiedlichen Quellen, etwa aus Slack-Threads, Linear-Issues, Dokumenten oder Tabellen in Google Drive und Notizen aus Kundengesprächen. Manchmal liegen klare User Stories vor, die ein Problem beschreiben, das sie lösen möchten. In anderen Fällen steckt der Kontext in diesen Quellen.

ChatGPT kann diesen Kontext zusammentragen und daraus ein UI-Mockup für ein Feature erstellen, das das Problem lösen würde. Sobald du das Konzept validiert hast, kann Codex es im Produkt umsetzen.

## Eine verlässliche visuelle Referenz erstellen

Wenn du bereits eine klare User Story hast, kannst du damit beginnen. Andernfalls kannst du dich zunächst mit ChatGPT austauschen, dabei Kontext aus verschiedenen Quellen zusammentragen und daraus eine User Story entwickeln.

Anschließend kannst du ChatGPT bitten, mithilfe der Bildgenerierung mehrere Mockup-Varianten zu erstellen. Die Mockups sollten die Informationsarchitektur des Produkts beibehalten und die Vorgaben des Designsystems einhalten.

Bei Bedarf kannst du Screenshots der aktuellen UI oder eine Figma-Datei als Referenz bereitstellen.

Wiederhole diesen Vorgang, bis du mit dem Mockup zufrieden bist. Je genauer du die Änderungen eingrenzt, desto wahrscheinlicher erstellt Codex ein Mockup, das sich direkt umsetzen lässt.

## Vom Mockup zum Prototyp

Verwende das fertige Mockup-Bild, das Codex umsetzen soll. Wähle Codex aus, starte einen neuen Chat und hänge das Bild erneut an, statt den Chat direkt in ChatGPT fortzusetzen. Bitte Codex anschließend, das Mockup in einen funktionsfähigen Prototyp umzusetzen. Wenn du eine Web-App entwickelst, kannst du dafür optional das [Plug-in „Build Web Apps“](https://github.com/openai/plugins/tree/main/plugins/build-web-apps) verwenden:

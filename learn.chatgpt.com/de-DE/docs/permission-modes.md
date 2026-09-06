<!-- source: https://learn.chatgpt.com/de-DE/docs/permission-modes -->

{/* vale Microsoft.FirstPerson = NO */}

## Berechtigungsmodi

Berechtigungen steuern, wie ChatGPT (in der Desktop-App) und Codex (in der CLI oder IDE) lokal agieren, etwa beim Bearbeiten von Dateien, beim Ausführen von Befehlen und beim Zugriff auf das Internet. Der ausgewählte Modus legt die Grenze dafür fest,
was ChatGPT selbstständig tun kann und was überprüft werden muss.

Für die meisten Aufgaben solltest du mit **Genehmigung anfordern** beginnen. Dabei kann ChatGPT im
aktuellen Workspace arbeiten und pausiert, bevor es diese Grenze überschreitet.

Wähle unten verschiedene Modi aus, um zu sehen, wie sie jeweils funktionieren.

## Modi aktivieren

Wenn du die ChatGPT-Desktop-App zum ersten Mal verwendest, musst du die Modi in den Einstellungen der App aktivieren.

**Genehmigung anfordern** ist immer verfügbar. Um **Für mich genehmigen** (in den Einstellungen als
**Automatische Überprüfung** bezeichnet) oder **Vollzugriff** dem Berechtigungsmenü hinzuzufügen, öffne in der ChatGPT-Desktop-App
**Einstellungen \> Allgemein** und aktiviere den Modus dann unter
**Berechtigungen**. Wenn du einen Modus aktivierst, ist er im Menü verfügbar; dadurch wird weder
der Modus ausgewählt noch ein vorhandener Chat geändert.

  

  Welche Modi verfügbar sind, kann von deiner lokalen Konfiguration und den
Vorgaben deiner Organisation abhängen. Ein nicht zugelassener Modus wird deaktiviert angezeigt.

## So funktionieren Berechtigungen

Zwei Mechanismen greifen ineinander:

- Die **Sandbox** legt fest, auf welche Dateien und Netzwerkressourcen ChatGPT zugreifen kann.
- **Genehmigungen** legen fest, wann ChatGPT vor einer Aktion pausiert oder die
  Anfrage zur automatischen Überprüfung weiterleitet.

Auch wenn du änderst, wer eine Anfrage überprüft, wird die Sandbox dadurch nicht erweitert. Beispielsweise behält der Modus
**Für mich genehmigen** dieselbe Workspace-Grenze bei wie **Genehmigung anfordern**;
er leitet Anfragen zum Überschreiten dieser Grenze zur automatischen Überprüfung weiter.

Verwende in der ChatGPT-Desktop-App oder
in der IDE-Erweiterung die Berechtigungsauswahl unter dem Editor.

Gib in der CLI `/permissions` ein. Technische Details findest du unter
[Sandbox](/de-DE/codex/sandboxing), [automatische Überprüfung](/de-DE/codex/sandboxing/auto-review) oder
[Berechtigungsprofile](/de-DE/codex/permissions).

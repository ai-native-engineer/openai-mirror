<!-- source: https://learn.chatgpt.com/de-DE/docs/pets -->

Begleiter sind optionale animierte Figuren, mit denen du laufende Aufgaben verfolgen kannst. Wo der Begleiter erscheint
und was er anzeigt, hängt von der jeweiligen Oberfläche ab. Durch die Auswahl eines Begleiters ändert sich nur sein
Aussehen, nicht die Art, wie ChatGPT Aufgaben erledigt.

<div class="flow-root">
  <div class="w-full md:float-right md:ml-6 md:w-64 xl:w-72">
    
  </div>

## Einen schwebenden Begleiter verwenden

In der ChatGPT-Desktop-App kann ein Begleiter über den Fenstern anderer Apps schweben und dir
helfen, Aktivitäten in deinen Chats zu verfolgen.

### Begleiter auswählen und wecken

1. Öffne unten in der App das Profilmenü und wähle **Begleiter** aus. Du kannst
   auch [**Einstellungen**](codex://settings) öffnen und zu **Begleiter** wechseln.
2. Wähle einen integrierten oder eigenen Begleiter aus.
3. Gib `/pet` ein oder öffne das Befehlsmenü und wähle **Begleiter wecken** aus.

Wähle **Begleiter ausblenden** unter **Einstellungen \> Begleiter** oder im Befehlsmenü aus oder gib
`/pet` erneut ein, um den Begleiter auszublenden. Deine Auswahl und die Position des Begleiters bleiben erhalten,
wenn du die App erneut öffnest.

Wenn du einen eigenen Begleiter auswählst, erscheint er auch in der Ansicht **Profil**.

### Status des Begleiters verstehen

| Status          | Bedeutung                                                  |
| --------------- | -------------------------------------------------------- |
| **Wird ausgeführt**     | In einem Chat wird gerade eine Aufgabe bearbeitet.                              |
| **Eingabe erforderlich** | In einem Chat musst du etwas genehmigen, antworten oder eine andere Entscheidung treffen. |
| **Bereit**       | Eine Aufgabe in einem Chat ist abgeschlossen und es gibt ungelesene Aktivitäten.            |
| **Blockiert**     | Ein Chat ist fehlgeschlagen oder es ist ein Systemfehler aufgetreten.             |

Wenn es in mehreren Chats Aktivitäten gibt, priorisiert der Begleiter Chats, für die eine
Eingabe erforderlich ist. Danach folgen in dieser Reihenfolge Chats mit dem Status „Blockiert“, „Bereit“ und „Wird ausgeführt“. Öffne die Aktivitätsübersicht, um
einen Chat auszuwählen.

Wähle den Begleiter aus, um zu ChatGPT zurückzukehren, oder wähle eine Aktivität aus, um den zugehörigen Chat zu öffnen.
Die Aktivitätsübersicht ist von [Benachrichtigungen des
Systems](/de-DE/codex/notifications?surface=app) getrennt.

### Computernutzung verfolgen

Unter macOS lässt sich das Bild-in-Bild-Fenster der [Computernutzung](/de-DE/codex/computer-use) an einen aktiven Begleiter
andocken. Bewegst du den Begleiter, folgt das Fenster.

### Eigenen Begleiter erstellen

1. Öffne **Einstellungen \> Begleiter** und wähle **Eigenen Begleiter erstellen** aus.
2. Die App installiert den mitgelieferten Skill `hatch-pet`, lädt die Skills neu und öffnet einen
   neuen Chat.
3. Beschreibe den gewünschten Begleiter und sende den Prompt.
4. Kehre nach Abschluss der Aufgabe zu **Einstellungen \> Begleiter** zurück, wähle **Aktualisieren** aus
   und wähle deinen neuen Begleiter aus.

Eigene Begleiter, die du in der Desktop-App erstellst, werden lokal auf deinem Computer gespeichert.
Sie werden nicht automatisch mit ChatGPT im Web synchronisiert.

### Animationen reduzieren

Begleiter berücksichtigen die Betriebssystemeinstellung „Bewegung reduzieren“. Ist diese
Option aktiviert, zeigt der Begleiter statt einer Sprite-Animation ein Standbild.

## Begleiter im Web auswählen

Wenn Begleiter für dein Konto und deinen Workspace verfügbar sind, öffne **Einstellungen \>
Personalisierung \> Begleiter \> Begleiter auswählen**. Wähle einen integrierten Begleiter oder
**Standard** aus, um ChatGPT ohne Begleiter zu verwenden.

In unterstützten Chats von ChatGPT Work wird ein Web-Begleiter angezeigt. Er bietet weder das schwebende Overlay
der Desktop-App noch deren Aktivitätsübersicht oder den Befehl `/pet`.

### Eigenen Begleiter hochladen

Wähle **Begleiter hochladen**, um ein eigenes Sprite-Sheet hinzuzufügen. Die Datei muss eine
transparente PNG- oder WebP-Datei sein und genau 1.536 × 1.872 Pixel messen; sie darf höchstens 20 MiB groß sein.
In derselben Einstellung kannst du hochgeladene Begleiter bearbeiten, herunterladen, aktualisieren oder löschen.

## Terminal-Begleiter auswählen

In einer interaktiven Sitzung der Codex CLI:

- Gib `/pets` oder `/pet` ein, um die Begleiterauswahl zu öffnen.
- Gib `/pets <name>` ein, um direkt einen Begleiter auszuwählen.
- Gib `/pets off` ein, um Terminal-Begleiter zu deaktivieren.

Die Auswahl umfasst integrierte Begleiter und kompatible eigene Begleiter, die auf deinem
Computer installiert sind. Ein Terminal-Begleiter zeigt Aktivitäten der aktuellen CLI-Sitzung an. Dabei verwendet er
die Status **Wird ausgeführt**, **Eingabe erforderlich**, **Bereit** und **Blockiert**, bietet aber nicht
die Aktivitätsübersicht der Desktop-App für mehrere Chats.

Terminal-Begleiter setzen iTerm2 ab Version 3.6 oder ein Terminal mit Unterstützung für Kitty-Grafiken oder
Sixel voraus. In tmux und Zellij sind sie nicht verfügbar.

## Begleiter in der IDE-Erweiterung

Die Codex IDE-Erweiterung bietet weder eine Begleiterauswahl noch ein schwebendes Begleiter-Overlay.
Verwende die ChatGPT-Desktop-App oder die Codex CLI, wenn du einen eigenen Begleiter verwenden möchtest.

</div>

## Weiterführende Dokumentation

- [Benachrichtigungen](/de-DE/codex/notifications)
- [Lang laufende Aufgaben](/de-DE/codex/long-running-work)
- [Einstellungen der ChatGPT-Desktop-App](/codex/reference/settings#pets)

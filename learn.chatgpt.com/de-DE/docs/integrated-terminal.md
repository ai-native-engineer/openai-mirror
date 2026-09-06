<!-- source: https://learn.chatgpt.com/de-DE/docs/integrated-terminal -->

Jeder Chat in der ChatGPT-Desktop-App verfügt über ein Terminal für das aktuelle Projekt oder
den aktuellen Worktree. Öffne es über das Terminalsymbol oben rechts in der App oder
drücke <kbd>Ctrl</kbd>+<kbd>\`</kbd>.

  
    
  

## Projekt ausführen und überprüfen

Nutze das Terminal, um Änderungen zu überprüfen, Skripte auszuführen und Git-Vorgänge durchzuführen,
ohne zwischen Apps zu wechseln. ChatGPT kann die aktuelle Terminalausgabe lesen und so
einen laufenden Entwicklungsserver überprüfen oder auf einen fehlgeschlagenen Build eingehen,
während es mit dir zusammenarbeitet.

Gängige Befehle sind:

- `git status`
- `git pull --rebase`
- `pnpm test` oder `npm test`
- `pnpm run lint` oder eine andere projektspezifische Prüfung

## Wiederverwendbare Aktionen erstellen

Wenn du einen Befehl regelmäßig ausführst, lege in deiner [lokalen Umgebung](/de-DE/codex/environments/local-environment#actions) eine Aktion fest.
Aktionen werden in der ChatGPT-Desktop-App als Schnellzugriffe angezeigt und im integrierten
Terminal ausgeführt.

<kbd>Cmd</kbd>+<kbd>K</kbd> öffnet die Befehlspalette der App, leert aber nicht das
Terminal. Um das Terminal zu leeren, drücke <kbd>Ctrl</kbd>+<kbd>L</kbd>.

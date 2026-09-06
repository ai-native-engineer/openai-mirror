<!-- source: https://learn.chatgpt.com/de-DE/docs/features/codex-micro -->

<div class="grid gap-6 lg:grid-cols-2 lg:items-start lg:gap-10">
  <div class="min-w-0 [&_p]:!mt-0">

Codex Micro ist ein limitiertes Gemeinschaftsprojekt von Codex und Work Louder. Es
funktioniert mit der ChatGPT-Desktop-App. Damit kannst du Chats schnell prüfen,
zwischen ihnen wechseln, die Spracheingabe nutzen und gängige Aktionen oder Skills auslösen,
ohne die Hände von der Tastatur nehmen zu müssen.

  </div>
  <div class="min-w-0">
    
      
    
  </div>
</div>

## Codex Micro einrichten

1. Öffne die ChatGPT-Desktop-App.
2. Drücke einmal die Taste auf der Rückseite, um Codex Micro einzuschalten.
3. Verbinde es über ein USB-C-Kabel oder [kopple es per Bluetooth](#pair-with-bluetooth),
   und führe anschließend das Setup aus, das angezeigt wird, sobald ChatGPT es erkennt.
4. Erlaube unter macOS bei Aufforderung die **Eingabeüberwachung**, damit ChatGPT auf
   Tastendrücke reagieren kann.
5. Öffne **Einstellungen \> Codex Micro**, um festzulegen, welchen Chats die Agententasten folgen oder
   welche Aktionen sie auslösen. Passe außerdem die Befehlstasten, den Analogstick und den Drehregler an und konfiguriere
   die Beleuchtung und Sprachsteuerung.

Halte den Drehregler standardmäßig kurz gedrückt, um diese Einstellungen zu öffnen. Du
kannst auch unten in ChatGPT neben deinem Kontonamen das Micro-Symbol auswählen.
Eine benutzerdefinierte Belegung des Drehreglers kann die Funktion zum Öffnen durch Gedrückthalten ersetzen.

Die Geräteeinstellungen bleiben verfügbar, sobald ChatGPT erstmals ein unterstütztes Micro
erkannt hat. Work Louder Input ist für die ChatGPT-Integration nicht erforderlich.
Damit kannst du Bedienelemente für andere Apps anpassen oder weitere Ebenen konfigurieren.

## Mit Bluetooth koppeln

Codex Micro verfügt über drei Bluetooth-Kanäle.

1. Drücke einmal die Taste auf der Rückseite, um das Micro einzuschalten.
2. Halte das Touch-Bedienfeld am linken unteren Rand drei Sekunden lang gedrückt.
Die Beleuchtung unter dem Micro leuchtet blau, wenn der Bluetooth-Modus aktiv ist.
3. Tippe auf das Touch-Bedienfeld, um Bluetooth-Kanal 1, 2 oder 3 auszuwählen. Wenn die
Kanalanzeige schnell blinkt, ist das Micro zum Koppeln bereit.
4. Öffne die Bluetooth-Einstellungen deines Computers und stelle eine Verbindung zum Micro her, sobald es
angezeigt wird.
5. Warte, bis die Kanalanzeige dauerhaft leuchtet. Damit ist die Kopplung abgeschlossen.

Die Verbindungsauswahl schließt sich nach fünf Sekunden ohne Eingabe. Um zu
einem anderen gekoppelten Kanal zu wechseln, öffne die Auswahl erneut, wähle den Kanal aus und warte,
bis sie sich schließt. Um diesen Kanal erneut zu koppeln, halte das Touch-Bedienfeld
drei Sekunden lang gedrückt, bis die Kanalanzeige zu blinken beginnt.

Wenn du stattdessen USB-C verwenden möchtest, öffne die Verbindungsauswahl und tippe auf das Touch-Bedienfeld,
bis die Beleuchtung unter dem Micro weiß leuchtet. Wenn du ein USB-C-Kabel anschließt, während
sich das Micro noch im Bluetooth-Modus befindet, wird es aufgeladen, wechselt aber nicht zur
Kabelverbindung.

Hardwarediagramme findest du im [Leitfaden von Work Louder zur Einrichtung von
Codex Micro](https://worklouder.cc/openai-micro-setup).

<a id="read-and-switch-tasks-with-agent-keys"></a>

## Chats mit Agententasten verfolgen und wechseln

Jede der sechs mattierten Agententasten kann einem Chat folgen und dessen
aktuellen Status durch Aufleuchten anzeigen. Drücke eine Agententaste einmal, um zu diesem Chat zu wechseln, ohne
ChatGPT in den Vordergrund zu holen. Drücke sie innerhalb von 350 Millisekunden zweimal, um den Chat zu wechseln und
das ChatGPT-Fenster in den Vordergrund zu holen. Wenn ChatGPT schon beim ersten Drücken fokussiert werden soll, aktiviere
**ChatGPT mit einmaligem Tippen fokussieren** in den Geräteeinstellungen.

| Licht | Status           | Bedeutung                                   |
| ----- | ---------------- | ----------------------------------------- |
| Weiß | Inaktiv             | Der Chat ist inaktiv.                         |
| Blau  | Denkt nach         | ChatGPT arbeitet.                       |
| Grün | Abgeschlossen         | Der Chat wurde abgeschlossen und enthält eine ungelesene Aktualisierung. |
| Bernsteinfarben | Eingabe erforderlich   | ChatGPT benötigt deine Genehmigung oder Antwort.  |
| Rot   | Fehler            | Etwas ist schiefgelaufen.                     |
| Aus   | Kein Chat zugewiesen | Die Taste folgt keinem Chat.            |

Das Statuslicht der Taste für den ausgewählten Chat pulsiert.

Standardmäßig folgen die Tasten deinen sechs zuletzt aktualisierten Chats, unabhängig davon,
ob diese angeheftet sind. Wähle in den Geräteeinstellungen unter **Agententasten** eine
andere Anordnung aus:

- **Zuletzt aktualisierte Chats**: Die Tasten folgen den sechs zuletzt aktualisierten Chats, unabhängig davon, ob sie
  angeheftet sind.
- **Angeheftete Chats**: Die Tasten folgen den ersten sechs Chats unter **Angeheftet**.
- **Priorisierte Chats**: Chats mit ausstehender Eingabe, ungelesene Chats und aktive
  Chats werden zuerst berücksichtigt.
- **Benutzerdefinierte Belegungen**: Weise jeder Agententaste einen Chat, ein Tastenkürzel, die Aktion einer physischen Taste oder einen aktivierten
  Skill zu. Drücke eine nicht belegte Agententaste, um einen neuen Chat zu öffnen.
  Wenn du den Chat startest, weist ChatGPT ihn dieser Taste zu.

Die Statusfarben bleiben bei Tasten, die Chats folgen, unverändert. Wenn du **Benutzerdefinierte
Belegungen** verwendest, kann eine Agententaste stattdessen eine Aktion auslösen.

## Befehlstasten verwenden und anpassen

Die Standardbelegung von Codex Micro umfasst sechs Aktionen:

<div class="grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-start">
  <div class="min-w-0 [&_table]:!mt-0 [&_td:first-child]:!px-2 [&_th:first-child]:!px-2 md:order-2">

|                            Taste                            | Standardaktion                           |
| :-------------------------------------------------------: | ---------------------------------------- |
|     | Schalte den Schnellmodus ein oder aus.                |
|  | Genehmige die aktuelle Anfrage.             |
|   | Lehne die aktuelle Anfrage ab.             |
|    | Den aktuellen Chat in einem neuen Chat fortsetzen. |
|       | Push-to-Talk starten.                      |
|   | Die Nachricht im Editor senden.        |

  </div>
  <div class="min-w-0 md:order-1">

Die Mikrofontaste nutzt das Mikrofon deines Computers. Codex Micro hat kein
eigenes Mikrofon. Standardmäßig ist **Push-to-Talk** aktiviert: Halte die Taste gedrückt, während
du sprichst, und lass sie los, um die Aufnahme zu beenden. Drücke sie für eine freihändige Aufnahme innerhalb
von 350 Millisekunden zweimal, damit die Aufnahme weiterläuft. Drücke die Taste erneut, um die Aufnahme zu beenden.

Ein seegrünes Licht wandert während der Aufnahme um die Tastatur.
Während ChatGPT deine Sprache verarbeitet, wird es zu einem wandernden weißen Licht und leuchtet dauerhaft weiß,
sobald der Prompt bereit ist. Drücke die Codex-Taste, um ihn zu senden.

Wenn **Sprachchat** unter **Mikrofontaste** verfügbar ist, wähle die Option aus. Mit der
Mikrofontaste kannst du dann einen Sprachchat starten oder dein Mikrofon ein- und ausschalten. Halte sie gedrückt, um
den Chat zu beenden. Aktiviere **Separate Mikrofontasten verwenden**, um die beiden Schalter
unter der breiten Mikrofontaste unabhängig voneinander zu belegen.

In den Geräteeinstellungen wählst du in der Vorschau unter **Layout** eine Befehlstaste aus und
legst anschließend Tastenkappe und Aktion fest. Du kannst den Browser oder das Terminal öffnen,
Chats verwalten, Änderungen überprüfen, Aktionen für Git und Pull Requests ausführen, Dateien oder Fotos anhängen,
Plug-ins oder geplante Aufgaben öffnen, den Reasoning-Aufwand ändern, einen aktivierten Skill ausführen
oder ein anderes Tastenkürzel zuweisen. Wenn du eine Tastenkappe auswählst, die bereits
anderweitig verwendet wird, vertauscht ChatGPT die beiden Tastenkappen, statt eine davon doppelt zu verwenden.

Nachdem du eine Taste neu belegt hast, tausche die physische Tastenkappe passend zur neuen Aktion aus.
Wähle **Layout zurücksetzen** aus, um die Standardbelegungen der Befehlstasten und des Analogsticks
wiederherzustellen, ohne den Modus der Agententasten oder benutzerdefinierte Chat-Zuweisungen zu ändern.

  </div>
</div>

## Analogstick und Drehregler verwenden

<div class="grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-start">
  <div class="min-w-0">

Der Analogstick lässt sich frei in jede Richtung bewegen. Bewegst du ihn weit genug
von der Mitte weg, wandelt ChatGPT die Bewegung in eine von vier Richtungsaktionen
um. Codex Micro verwendet zunächst die hier gezeigten Belegungen.

Wähle für jede Richtung in den Geräteeinstellungen einen verfügbaren Befehl der ChatGPT-Desktop-App oder einen aktivierten
Skill aus.

  </div>
  <div class="min-w-0 [&_table]:!mt-0">

| Richtung | Standardaktion             |
| --------- | -------------------------- |
| Nach oben        | Planmodus ein- oder ausschalten.  |
| Nach rechts     | Im App-Verlauf vorwärtsgehen. |
| Nach unten      | Seitenleiste ein- oder ausblenden.  |
| Nach links      | Im App-Verlauf zurückgehen.    |

  </div>
</div>

Der Drehregler verwendet standardmäßig **Editor-Navigation**. Drehe ihn, um durch
die Bedienelemente und Optionen des Editors zu navigieren. Drücke ihn anschließend, um das fokussierte
Bedienelement zu öffnen oder auszuwählen. Wenn ein Bedienelement oder Menü im Editor geöffnet ist, leuchtet die Agententaste direkt
rechts neben dem Drehregler rot. Drücke diese Taste, um abzubrechen.

Wähle in den Geräteeinstellungen einen von vier Modi für den Drehregler aus:

| Modus                       | Verhalten                                                                       |
| -------------------------- | ------------------------------------------------------------------------------ |
| **Editor-Navigation**    | Navigiere durch die Bedienelemente des Editors und wähle das fokussierte Bedienelement aus.                 |
| **Nur Reasoning-Aufwand**         | Passe den Reasoning-Aufwand an und öffne den zugehörigen Schieberegler oder die erweiterten Optionen.               |
| **Im Chat scrollen** | Scrolle im aktiven Chat; drücke den Drehregler, um zur neuesten Nachricht zu springen.          |
| **Benutzerdefinierte Zuweisungen**     | Weise dem Drehen nach links und rechts sowie dem Drücken und langen Drücken jeweils eine Aktion oder einen Skill zu. |

Wenn du den Drehregler gedrückt hältst, öffnest du in jedem Modus die Geräteeinstellungen. Das gilt nicht für den Modus
**Benutzerdefinierte Zuweisungen**: Dort wird die Aktion ausgeführt, die dem langen Drücken zugewiesen ist.

## Beleuchtung anpassen

{/* vale Microsoft.Auto = NO */}

Passe in den Geräteeinstellungen die **Helligkeit** an und wähle für **Automatisch dimmen**
ein Intervall von 30 Sekunden bis zu einer Stunde aus oder deaktiviere das automatische Dimmen. Die Beleuchtung
schaltet sich wieder ein, wenn du das Micro verwendest oder sich der Status einer Agententaste ändert. Standardmäßig
schaltet sie sich nach drei Minuten aus.

{/* vale Microsoft.Auto = YES */}

Wenn das Micro seinen Akkustand meldet, siehst du ihn in den Geräteeinstellungen
und neben dem Micro-Symbol in der Seitenleiste.

## Weitere Ebenen hinzufügen

ChatGPT verwendet Ebene 1. Mit [Work Louder
Input](https://worklouder.cc/micro-setup) kannst du bis zu fünf weitere Ebenen
mit Tastenkürzeln und Aktionen für andere Apps konfigurieren.

## Probleme mit Codex Micro beheben

### Probleme mit der Eingabeüberwachung unter macOS beheben

Wenn die Geräteeinstellungen anzeigen, dass die Eingabeüberwachung nicht eingerichtet ist, wähle **Systemeinstellungen
 öffnen** aus und gehe dann wie folgt vor:

1. Öffne **Systemeinstellungen \> Datenschutz & Sicherheit \> Eingabeüberwachung**.
2. Aktiviere den Zugriff für ChatGPT, wenn es bereits aufgeführt ist. Fehlt der Eintrag, ziehe
**ChatGPT** aus dem Ordner „Programme“ in die Liste oder wähle **Hinzufügen (+)** und anschließend
**ChatGPT** aus.
3. Beende ChatGPT und öffne es erneut. Vergewissere dich dann, dass das Micro auf Ebene 1 erkannt wird.

Weitere Informationen zu dieser macOS-Berechtigung findest du in [Apples Leitfaden zur
Eingabeüberwachung](https://support.apple.com/guide/mac-help/mchl4cedafb6/mac).

### Verbindungsstörungen beheben

ChatGPT versucht es automatisch erneut, wenn es ein Micro erkennt, aber keine Verbindung herstellen kann oder die
Kommunikation abbricht. Wenn das Problem weiterhin besteht, verbinde das Micro erneut und prüfe, ob
ein Tastaturdienstprogramm oder Sicherheitstool den Zugriff darauf blockiert.

{/* vale Vale.Spelling = NO */}

Work Louder weist darauf hin, dass Karabiner und Logitech Options+ unter macOS die Kommunikation
mit dem Micro stören können, wenn diese Apps die Berechtigung zur Eingabeüberwachung haben. Um
eine Störung zu testen, beende das Tastaturdienstprogramm oder deaktiviere vorübergehend dessen
Zugriff auf die Eingabeüberwachung. Verbinde danach das Micro erneut. Wenn deine Organisation
deinen Computer verwaltet, bitte deine IT-Abteilung, die Geräteregeln zu prüfen.

{/* vale Vale.Spelling = YES */}

### Weitere Hilfe von Work Louder

Hilfe zu Bluetooth, Kabeln, Stromversorgung oder zum Zurücksetzen der Tastatur findest du im [Setup-Leitfaden von Work
Louder für Codex Micro](https://worklouder.cc/openai-micro-setup). Direkten
Support erhältst du per E-Mail an
[hello@worklouder.cc](mailto:hello@worklouder.cc).

## Ein kompatibles Micro beziehen

Prüfe die Verfügbarkeit von Codex Micro über [OpenAI Supply
Co](https://openai.com/supply/co-lab/work-louder/). Die ChatGPT-Desktop-App
unterstützt außerdem [Creator Micro 2](https://worklouder.cc/creator-micro-2), das
direkt bei Work Louder erhältlich ist.

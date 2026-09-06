<!-- source: https://learn.chatgpt.com/de-DE/docs/customization/computer-history -->

Der Verlauf der Computernutzung ist für Nutzende von ChatGPT Pro, Business und Enterprise in der ChatGPT-Desktop-App unter macOS **standardmäßig deaktiviert** .
  Mit Pro kannst du selbst entscheiden, ob du ihn aktivierst. In Business- und
  Enterprise-Workspaces muss die Administration den Zugriff ausdrücklich freigeben,
  bevor jedes Mitglied selbst entscheiden kann, ob es den Verlauf aktiviert.
  Außerdem setzt der Verlauf der Computernutzung [Erinnerungen](/de-DE/codex/customization/memories) voraus und ist weder
  mit einem API-Schlüssel noch mit Amazon Bedrock verfügbar. Er ist in unterstützten
  Regionen verfügbar, darunter im Europäischen Wirtschaftsraum (EWR), in der Schweiz
  und im Vereinigten Königreich.

Der Verlauf der Computernutzung wandelt deine Aktivitäten in Apps und auf Websites in Erinnerungen und eine Zeitachse um, auf die ChatGPT und Codex zurückgreifen können. Du kannst Fragen zu deiner letzten Arbeit in natürlicher Sprache stellen, dort weitermachen, wo du aufgehört hast, Muster in deiner Arbeitsweise erkennen und wiederkehrende Arbeitsabläufe in Skills oder Automatisierungen umwandeln.

Dein Verlauf beginnt erst, wenn du ihn aktivierst. Du bestimmst, welche Apps und Websites einbezogen werden, kannst die Erfassung über die macOS-Menüleiste einsehen und pausieren und deinen Verlauf jederzeit überprüfen oder löschen.

Der Verlauf der Computernutzung ersetzt die frühere Forschungsvorschau Chronicle, ist jedoch ein neu entwickeltes System und nicht bloß eine Umbenennung. Er nutzt Interaktionsereignisse sowie Texte und weitere Kontextinformationen, die über die macOS-Bedienungshilfen verfügbar sind, um Zusammenfassungen zu erstellen, die du überprüfen und löschen kannst. Der Verlauf enthält keine Screenshots, es wird kein Audio aufgezeichnet und Aktivitäten beim Surfen im privaten Modus werden niemals einbezogen.

  

## So hilft dir der Verlauf der Computernutzung

Der Verlauf der Computernutzung stellt deine letzten Aktivitäten als Kontext bereit. Wenn sich eine Datei, eine Slack-Unterhaltung, ein Google Doc oder eine andere Quelle besser für die Aufgabe eignet, können ChatGPT und Codex diese Quelle anhand des Verlaufs identifizieren und anschließend direkt lesen.

<section class="feature-grid mt-4">

<div>

### Dort weitermachen, wo du aufgehört hast

Frage, woran du vor einer Pause gearbeitet hast, ohne jede geöffnete App, jedes Dokument und jeden nächsten Schritt rekonstruieren zu müssen.

</div>

</section>

<section class="feature-grid inverse">

<div>

### Zuletzt Bearbeitetes finden

Beschreibe ein Dokument, eine Unterhaltung oder eine Aufgabe so, wie du dich daran erinnerst. Der Verlauf der Computernutzung kann anhand der Zeitachse deiner Aktivitäten erkennen, welche Quelle du meinst.

</div>

</section>

<section class="feature-grid">

<div>

### Arbeitsabläufe wiederverwenden

Wenn der Verlauf der Computernutzung wiederkehrende Tätigkeiten erkennt, kann ein Eintrag auf der Zeitachse einen Skill oder eine Automatisierung vorschlagen. Prüfe den Vorschlag und bitte Codex anschließend, anhand des aufgezeichneten Ablaufs den Skill oder die Automatisierung zu erstellen.

</div>

</section>

## So funktioniert der Verlauf der Computernutzung

Der Verlauf der Computernutzung erfasst Interaktionsereignisse aus zugelassenen Apps und Websites in einem Ereignisstrom. Dazu gehören Klicks, Tastatureingaben, Tastenkürzel, App-Wechsel und Kontextinformationen, die macOS über seine Bedienungshilfen bereitstellt. Aus diesen Ereignissen erstellt der Verlauf der Computernutzung regelmäßig Textzusammenfassungen und lokale Erinnerungsdateien.

Der Verlauf der Computernutzung nimmt keine Screenshots in deinen Verlauf auf und zeichnet weder Mikrofoneingaben noch Systemaudio auf. Aktivitäten im privaten Browsermodus werden niemals einbezogen.

Unter **Einstellungen \> Verlauf der Computernutzung \> Verlauf** ordnet die Zeitleiste Zusammenfassungen nach
Tag und Uhrzeit. Jeder Eintrag kann Folgendes anzeigen:

- Einen Titel und eine textliche Zusammenfassung der Aktivität.
- Die Apps, deren Aktivitäten in die Zusammenfassung eingeflossen sind.
- Einen vorgeschlagenen Skill oder eine Automatisierung, wenn ChatGPT wiederholbare Aufgaben erkennt.
- Aktionen, um die Erinnerungsdatei im Finder anzuzeigen oder den Eintrag zu löschen.

Wähle **Fragen zum Verlauf stellen** aus, um einen Chat zum Verlauf der Computernutzung zu starten, oder verwende
Prompts wie:

- „Woran habe ich vor meiner letzten Pause gearbeitet?“
- „Wo finde ich das Dokument mit dem Vorschlag, nach dem ich heute schon gesucht habe?“
- „Liste alle Aufgaben auf, an denen ich heute gearbeitet habe, und gib ihren Status an.“
- „Erstelle für das Stand-up eine Zusammenfassung meiner gestrigen Arbeit.“

## Berechtigungen und Zugriff

Der Verlauf der Computernutzung hat separate Einstellungen für den Workspace-Zugriff, die persönliche Aktivierung, Erinnerungen sowie die Apps und Websites, die im Verlauf berücksichtigt werden:

- **Workspace-Zugriff:** In Business- und
  Enterprise-Workspaces ist der Verlauf der Computernutzung standardmäßig deaktiviert und erst verfügbar,
  wenn die Administration den Zugriff ausdrücklich freigibt. Administrierende in Enterprise-Workspaces können über **Verlauf der Computernutzung
  aktivieren** unter [**Workspace-Einstellungen \> Berechtigungen und Rollen**](https://chatgpt.com/admin/settings)
  den entsprechenden Workspace-Rollen Zugriff gewähren.
- **Persönliche Aktivierung:** Die Freigabe des Workspace-Zugriffs ermöglicht es einem Mitglied lediglich,
  den Verlauf der Computernutzung selbst zu aktivieren. Die Funktion wird dadurch für niemanden aktiviert. Jede
  Person muss sie selbst aktivieren, auch Personen mit ChatGPT Pro.
- **Erinnerungen:** Der Verlauf der Computernutzung setzt außerdem [Erinnerungen](/de-DE/codex/customization/memories) voraus.
  Mit `/memories` legst du fest, ob ein einzelner Chat lokale Erinnerungen verwenden
  oder zu künftigen Erinnerungen beitragen darf.
- **Apps und Websites:** Deine Berechtigungen für Apps und Websites legen fest, aus welchen
  Quellen Interaktionsereignisse erfasst werden dürfen. Du kannst nur bestimmte
  Quellen zulassen oder Apps und Website-URLs ausschließen, die du nicht berücksichtigen möchtest.

Wenn deine Workspace-Rolle keinen Zugriff hat, lässt sich der Verlauf der Computernutzung nicht durch Änderungen an lokalen Einstellungen aktivieren.

## Verlauf der Computernutzung aktivieren

Der Verlauf der Computernutzung ist standardmäßig deaktiviert. Wenn du einen Business- oder Enterprise-Workspace verwendest, bitte die zuständige Administration, dir vor der Aktivierung Zugriff zu gewähren. Die Genehmigung durch die Administration aktiviert die Funktion nicht automatisch für dich.

1. Öffne die ChatGPT-Desktop-App unter macOS.
2. Wähle in den Einstellungen unter **Integrationen** die Option **Verlauf der Computernutzung** aus.
3. Wähle **Aktivieren** aus und prüfe die Informationen zu Datenschutz, Berechtigungen und
   lokaler Speicherung.
4. Aktiviere **Erinnerungen**, wenn du dazu aufgefordert wirst. Der Verlauf der Computernutzung benötigt Erinnerungen,
   damit er den Kontext deiner Aktivitäten über Chats und Aufgaben hinweg verwenden kann.
5. Wähle aus, welche Apps und Websites in deinen Verlauf einfließen dürfen, und folge gegebenenfalls den macOS-Aufforderungen zur Berechtigungsvergabe.

Der Verlauf der Computernutzung erfordert keine Berechtigung zur Bildschirmaufnahme. Falls die Einstellung nicht angezeigt wird, prüfe, ob dein Tarif den Verlauf der Computernutzung unterstützt und ob ihn deine Workspace-Administration gegebenenfalls aktiviert hat.

## Festlegen, was in den Verlauf aufgenommen wird

Du entscheidest, welche Apps und Websites künftig in den Verlauf einfließen und ob der Verlauf der Computernutzung gerade Interaktionsereignisse erfasst.

### Apps und Websites auswählen

Lege unter **Einstellungen \> Verlauf der Computernutzung \> Berechtigungen** fest, welche Apps und
Websites in den Verlauf der Computernutzung aufgenommen werden dürfen:

- **Diese Apps ausschließen** und **Diese Websites ausschließen** blockieren die von dir angegebenen Apps oder URLs,
  während andere unterstützte Quellen zugelassen bleiben.
- **Nur diese Apps einbeziehen** und **Nur diese Websites einbeziehen** lassen ausschließlich die
  Quellen zu, die du ausdrücklich auswählst.

Du kannst auch das Symbol einer App in einem Eintrag der Zeitleiste auswählen, um diese App künftig vom Verlauf auszuschließen. Später kannst du sie wieder einbeziehen.

Aktivitäten im privaten Browsermodus werden niemals einbezogen. Änderungen der Berechtigungen für Apps oder Websites wirken sich auf künftige Verlaufseinträge aus. Vorhandene Einträge entfernst du, indem du sie oder den Verlauf löschst.

### Erfassung pausieren, fortsetzen oder beenden

Über die Einstellungen für den Verlauf der Computernutzung oder die macOS-Menüleiste kannst du festlegen, wann die Funktion Aktivitäten erfasst:

- Wähle das ChatGPT-Symbol in der macOS-Menüleiste aus und klappe das Menü für den Verlauf der Computernutzung auf, um zu sehen, welche Aktivitäten erfasst werden, und auf die Steuerelemente zuzugreifen.
- Wähle **Pausieren** aus, um die Erfassung neuer Interaktionsereignisse zu stoppen, oder wähle
**Fortsetzen** aus, wenn du sie wieder aufnehmen möchtest.
- Deaktiviere den Verlauf der Computernutzung, um künftig keine Aktivitäten mehr zu erfassen.

Der Verlauf der Computernutzung kann Interaktionsereignisse aus Apps und Websites zur Kommunikation enthalten. Deaktiviere ihn bei der Kommunikation mit anderen Personen, sofern sie nicht vorher ausdrücklich zugestimmt haben. Erwäge, die Erfassung zu pausieren oder Apps auszuschließen, die sensible Gesundheitsdaten, Finanzdaten oder persönliche Informationen enthalten.

## Verlauf überprüfen und löschen

Öffne **Einstellungen \> Verlauf der Computernutzung \> Verlauf** , um nachzusehen, was der Verlauf der Computernutzung
zusammengefasst hat. Du kannst die lokale Erinnerungsdatei einer Zusammenfassung im Finder anzeigen,
einzelne Einträge in der Zeitleiste löschen oder den Verlauf der letzten 10 Minuten, der letzten Stunde,
des letzten Tages oder den gesamten Verlauf löschen. Über die macOS-Menüleiste kannst du außerdem die letzte Sitzung
einer kürzlich verwendeten App löschen.

Wenn du den Verlauf löschst, werden die zugehörigen Interaktionsereignisse und alle daraus entstandenen Erinnerungen gelöscht. Dieser Vorgang kann nicht rückgängig gemacht werden.

## Datenschutz und lokale Speicherung

Der Verlauf der Computernutzung speichert Interaktionsereignisse als Ereignisstrom vorübergehend auf deinem Mac, damit ChatGPT und Codex Erinnerungen und Vorschläge für Arbeitsabläufe erstellen können. Dieser Ereignisstrom kann Aktivitäten wie Klicks und Tastatureingaben sowie Text und weitere Kontextinformationen enthalten, die über die macOS-Bedienungshilfen verfügbar sind. Der Verlauf der Computernutzung nimmt keine Screenshots in deinen Verlauf auf und zeichnet weder Mikrofoneingaben noch Systemaudio auf. Aktivitäten im privaten Browsermodus werden niemals einbezogen.

Temporäre Ereignisdateien werden bis zu 48 Stunden aufbewahrt. Erstellte Erinnerungsdateien verbleiben in deinem Dateisystem, bis du sie oder den Verlauf löschst. Über die Zeitleiste des Verlaufs kannst du diese Dateien anzeigen.

### Wo speichert der Verlauf der Computernutzung meine Daten?

Der Verlauf der Computernutzung speichert Interaktionsereignisse vorübergehend auf deinem Mac.
Die Ereignisdateien sind innerhalb der
[App Group](https://developer.apple.com/documentation/xcode/protecting-local-app-data-using-containers) von ChatGPT isoliert,
sodass andere Apps ohne ausdrückliche Berechtigung nicht darauf zugreifen können.
ChatGPT und Codex löschen diese Ereignisdateien nach 48 Stunden.

Der Verlauf der Computernutzung erstellt dieselbe Art lokaler Erinnerungen wie Codex: Markdown-Dateien
im Klartext, die du lesen und ändern kannst. Die Dateien werden
unter `$CODEX_HOME/memories/extensions/skysight/` gespeichert. Dieser Pfad wird normalerweise zu
`~/.codex/memories/extensions/skysight/` aufgelöst.

<div className="not-prose my-4">
  
</div>

### Welche Daten werden an OpenAI weitergegeben?

Der Verlauf der Computernutzung erfasst Interaktionsereignisse lokal und startet anschließend in regelmäßigen Abständen eine temporäre Codex-Sitzung mit Zugriff auf den Ereignisstrom, um deine Aktivitäten in Erinnerungen zusammenzufassen.

OpenAI verarbeitet temporäre Ereignisdateien auf seinen Servern, um Erinnerungen zu erstellen, die anschließend lokal auf deinem Mac gespeichert werden. Nach der Verarbeitung bewahrt OpenAI diese Ereignisdateien nur auf, wenn dies gesetzlich vorgeschrieben ist, und verwendet sie nicht für das Training.

Wenn ChatGPT oder Codex in einem späteren Chat eine Erinnerung verwendet, können relevante Erinnerungsinhalte
und Interaktionsereignisse als Kontext einbezogen werden. Diese Chat-Inhalte können zur Verbesserung von
OpenAI-Modellen verwendet werden, sofern deine
[Dateneinstellungen in ChatGPT](https://help.openai.com/en/articles/7730893-data-controls-faq) dies zulassen.
Für Erinnerungen gelten außerdem dieselben
[Einstellungen auf Chat-Ebene wie für andere Codex-Erinnerungen](/de-DE/codex/customization/memories#control-memories-per-chat).

### Risiko durch Prompt Injection

Der Verlauf der Computernutzung erhöht das Risiko von Prompt Injection durch Inhalte in Apps und auf Websites. Wenn du beispielsweise eine Website mit schädlichen Anweisungen besuchst, könnten ChatGPT oder Codex diesen Anweisungen folgen.

## Tokenverbrauch

Der Verlauf der Computernutzung verbraucht Token, wenn er Aktivitäten zusammenfasst und Erinnerungen erstellt.

## Fehlerbehebung

Wenn der Verlauf der Computernutzung verfügbar ist, aber nicht startet:

1. Prüfe, ob **Erinnerungen** aktiviert sind.
2. Öffne **Einstellungen \> Verlauf der Computernutzung** und wähle je nach angezeigtem Status **Setup abschließen**, **Fortsetzen**
   oder **Erneut versuchen** aus.
3. Beende die ChatGPT-Desktop-App und öffne sie erneut, wenn die Einstellung weiterhin nicht verfügbar ist.

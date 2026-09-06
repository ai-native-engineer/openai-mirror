<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/manage-app-updates -->

Die ChatGPT-Desktop-App sucht normalerweise selbst nach Updates und installiert sie. Wenn
deine Organisation neue Versionen prüfen muss, bevor Nutzende sie erhalten, kannst du
den integrierten Updater der App deaktivieren und freigegebene Versionen über
deine Geräteverwaltungsplattform bereitstellen.

Der Updater der App ist standardmäßig aktiviert. Seine Deaktivierung verhindert nicht, dass
der Microsoft Store, Microsoft Intune, die Mobilgeräteverwaltung (MDM), Paketmanager
oder andere externe Bereitstellungstools Updates installieren.

## Bevor du beginnst

Stelle sicher, dass Folgendes vorhanden ist:

- Codex-Administratorzugriff auf
[Verwaltete Konfiguration](https://chatgpt.com/codex/settings/managed-configs)
  für deinen Workspace.
- Eine Version der ChatGPT-Desktop-App für macOS oder Windows, die
von der Organisation verwaltete Updates unterstützt.
- Eine MDM- oder Softwarebereitstellungsplattform, die freigegebene App-Pakete
auf den verwalteten Geräten deiner Organisation installieren kann.
- Ein Verfahren, um neue Versionen zu testen, Sicherheitsupdates bereitzustellen und
installierte App-Versionen nachzuverfolgen.

Wenn du die App noch nicht unter Windows bereitgestellt hast, beginne mit
[Windows-App bereitstellen](/de-DE/codex/enterprise/windows-deployment).

## In-App-Updates deaktivieren

  Wenn du In-App-Updates deaktivierst, ist deine Organisation dafür verantwortlich,
neue App-Versionen und Sicherheitskorrekturen zeitnah bereitzustellen. Verzögerte Updates können
die App und ihre mitgelieferten Komponenten bekannten Sicherheitslücken
aussetzen. Ältere App-Versionen erhalten weder separate Sicherheitspatches noch
erweiterten Support.

Erstelle eine verwaltete Richtlinie, die den eigenen Updater der Desktop-App deaktiviert:

1. Öffne
[Verwaltete Konfiguration](https://chatgpt.com/codex/settings/managed-configs).
2. Wähle **Richtlinie hinzufügen** aus oder öffne eine vorhandene Richtlinie für die Nutzenden, Gruppen oder
   Plattformen, die du verwalten möchtest.
3. Wähle unter **Ziele** die Option **Ziel hinzufügen** aus und lege konkrete Ziele für die Richtlinie fest:
**Gruppen**, **Nutzende** oder **Plattformen**. Beginne nach Möglichkeit mit
   einer kleinen Pilotgruppe.
4. Öffne **TOML-Rohdaten** und suche den Editor für **requirements.toml**.
5. Füge die folgende Richtlinie hinzu:

   ```toml
   [features]
   in_app_updates = false

   Wenn deine Richtlinie bereits eine Tabelle `[features]` enthält, füge
`in_app_updates = false` dieser Tabelle hinzu. Füge keine zweite Tabelle `[features]` hinzu
   und trage die Einstellung nicht in **config.toml** ein.

6. Wähle **Änderungen speichern** aus.
7. Bitte betroffene Nutzende, die ChatGPT-Desktop-App vollständig zu beenden und erneut zu öffnen. Das Schließen
des App-Fensters reicht nicht immer aus, um die Anwendung neu zu starten.

In einigen Workspaces wird anstelle des Tabs **TOML-Rohdaten** ein Editor mit einer Richtlinienliste angezeigt. Füge in
dieser Oberfläche denselben TOML-Block direkt zur entsprechenden Richtlinie hinzu. Verwende
**Gruppen** für die Zuweisung der Richtlinie, sofern die Option verfügbar ist, und wähle **Speichern** aus.

Weitere Informationen zur Bereitstellung verwalteter Richtlinien und ihrer Prioritätsreihenfolge findest du unter
[Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration).

## Verwaltete Einstellung überprüfen

Überprüfe die Richtlinie nach dem Neustart der App auf dem Gerät einer betroffenen Person:

1. Melde dich in der ChatGPT-Desktop-App mit einem Konto an, für das die Richtlinie gilt.
2. Öffne **Einstellungen** \> **Allgemein**.
3. Suche **In-App-Updates** und vergewissere dich, dass dort der Status **Verwaltet** und die Meldung
   „Deine Organisation hat In-App-Updates deaktiviert.“ angezeigt werden.
4. Vergewissere dich, dass deine Geräteverwaltungsplattform weiterhin eine freigegebene
App-Version bereitstellen kann.

Die Menüoption **Nach Updates suchen** kann sichtbar bleiben, auch wenn die Richtlinie
In-App-Updates blockiert. Nutze die Anzeige **Verwaltet**, um die Richtlinie zu prüfen,
statt dich daran zu orientieren, ob diese Menüoption sichtbar ist.

Wenn die Anzeige nach dem ersten Neustart nicht erscheint, verwendet die App möglicherweise noch
eine zwischengespeicherte Richtlinie. Warte, bis die Richtlinie aktualisiert wurde, beende die
App dann vollständig und öffne sie erneut. Verlasse dich erst dann auf die Update-Beschränkung, wenn **Verwaltet** angezeigt wird.

## Freigegebene App-Versionen bereitstellen

Nachdem du In-App-Updates deaktiviert hast, nutze deinen bestehenden Geräteverwaltungsprozess
zur Bereitstellung neuer Versionen:

1. Wähle die App-Version aus, die deine Organisation bereitstellen möchte.
2. Lade das unterstützte Installationspaket für jedes Betriebssystem und jede
Gerätearchitektur in deiner Geräteflotte herunter.
3. Teste die Version mit einer kleinen, repräsentativen Gruppe von Nutzenden.
4. Stelle das freigegebene Paket über Microsoft Intune, deine MDM-Plattform oder
ein anderes Tool zur Softwarebereitstellung bereit.
5. Prüfe im Geräteinventar, ob deine Plattform die vorgesehene
Version installiert hat. Weite die Bereitstellung anschließend auf andere Gruppen aus.

Deine Verwaltungsplattform bestimmt, wie du die Bereitstellung neuer Versionen staffelst, Versionen auswählst
und mit unvollständigen Bereitstellungen umgehst. Wenn deine Plattform Rollbacks zulässt,
wird durch die Rückkehr zu einer älteren Version weder der Support verlängert noch
die Kompatibilität mit dem Dienst garantiert.

Lade für macOS das
[Installationsprogramm der ChatGPT-Desktop-App](https://persistent.oaistatic.com/codex-app-prod/ChatGPT.dmg) herunter.
Informationen zu Installationsmethoden unter Windows und architekturspezifischen Paketen findest du unter
[Windows-App bereitstellen](/de-DE/codex/enterprise/windows-deployment).

## In-App-Updates wieder aktivieren

So stellst du das normale Update-Verhalten der App wieder her:

1. Ermittle alle verwalteten Richtlinien, systemweiten Dateien `requirements.toml` und MDM-Profile,
   durch die Updates für die betroffenen Personen deaktiviert werden.
2. Entferne `in_app_updates = false` aus jeder relevanten Tabelle `[features]`.
3. Speichere die Richtlinienänderungen und stelle alle aktualisierten Vorgaben über die Geräteverwaltung erneut bereit.
4. Bitte betroffene Nutzende, die ChatGPT-Desktop-App vollständig zu beenden und erneut zu öffnen.
5. Prüfe unter **Einstellungen** \> **Allgemein**, ob die als verwaltet gekennzeichnete Zeile **In-App-Updates**
   nicht mehr angezeigt wird.

Wenn keine geltende Richtlinie `in_app_updates = false` festlegt, verhält sich der integrierte
Updater der App wie gewohnt. Falls die Anzeige **Verwaltet** weiterhin
erscheint, prüfe andere Workspace-Richtlinien, MDM-Profile sowie systemweite
Dateien `requirements.toml`. Im Abschnitt
[Speicherorte und Prioritätsreihenfolge](/de-DE/codex/enterprise/managed-configuration#locations-and-precedence)
erfährst du, in welcher Reihenfolge verwaltete Quellen angewendet werden.

## Verantwortlichkeiten für Sicherheit und Support verstehen

Sobald die App die Richtlinie für verwaltete Updates empfangen und angewendet hat, gilt Folgendes:

- Die Desktop-App kann über ihren eigenen Updater weder nach Updates suchen noch Updates
herunterladen oder installieren.
- Die Richtlinie bietet keine von OpenAI verwaltete Versionsfixierung, keinen separaten Versionskanal
und keine Garantie für die Kompatibilität älterer Versionen mit dem Dienst.
- Die Richtlinie gilt für unterstützte Builds der ChatGPT-Desktop-App unter macOS und Windows. Sie
verwaltet keine Updates für mobile Apps, die Codex CLI oder die IDE-Erweiterung.

## Häufige Probleme beheben

Wenn ein Authentifizierungsproblem, ein Verbindungsproblem oder eine Zeitüberschreitung die App daran hindert,
die verwaltete Richtlinie abzurufen oder anzuwenden, kann ihr integrierter Updater
aktiviert bleiben. Gehe nur dann davon aus, dass die App Updates blockiert, wenn **Verwaltet** angezeigt wird.

Wenn die Anzeige **Verwaltet** nicht erscheint, überprüfe Folgendes:

- Die betroffene Person hat den vorgesehenen Workspace ausgewählt.
- Die Richtlinie gilt für diese Person, Gruppe oder Plattform.
- Auf dem Gerät wird eine unterstützte App-Version ausgeführt.
- Die App kann eine Verbindung zu dem Dienst herstellen, über den verwaltete Richtlinien bereitgestellt werden.
- Die Einstellung befindet sich in **requirements.toml** und nicht in **config.toml**.
- Die betroffene Person hat die App vollständig beendet und erneut geöffnet, nachdem du die Richtlinie gespeichert hast.

Wenn du die Verwaltete Konfiguration nicht öffnen oder keine Richtlinie speichern kannst, vergewissere dich, dass du
für den Workspace über Codex-Administratorzugriff verfügst.

Wenn sich die App-Version ändert, nachdem du In-App-Updates deaktiviert hast, prüfe, ob
Microsoft Store, Intune, MDM, ein Paketmanager oder ein anderes Bereitstellungssystem
das Update installiert hat. Die Richtlinie steuert nur den integrierten Updater der App.

## Weitere Dokumentation

- [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration)
- [Windows-App bereitstellen](/de-DE/codex/enterprise/windows-deployment)
- [Konfigurationsreferenz für `requirements.toml`](/de-DE/codex/config-file/config-reference#requirementstoml)
- [Rollout-Leitfaden für die Administration](/de-DE/codex/enterprise/admin-setup)

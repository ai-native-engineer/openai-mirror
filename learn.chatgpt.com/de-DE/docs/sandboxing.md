<!-- source: https://learn.chatgpt.com/de-DE/docs/sandboxing -->

Die Sandbox bildet die Grenze, innerhalb derer der Agent autonom handeln kann, ohne
uneingeschränkten Zugriff auf deinen Computer zu erhalten. Wenn ein lokaler Chat Befehle in der
**ChatGPT-Desktop-App**, in **Codex CLI** oder in der **IDE-Erweiterung** ausführt, werden diese standardmäßig in einer
eingeschränkten Umgebung statt mit Vollzugriff ausgeführt.

Diese Umgebung legt fest, was der Agent selbstständig tun darf, etwa welche Dateien er
ändern kann und ob Befehle das Netzwerk verwenden dürfen. Bleibt eine Aufgabe innerhalb
dieser Grenzen, kann der Agent ohne Unterbrechung und ohne Bestätigung weiterarbeiten. Muss
er darüber hinausgehen, greift das Genehmigungsverfahren.

  Sandboxing und Genehmigungen sind unterschiedliche Kontrollmechanismen, die zusammenwirken. Die
Sandbox legt technische Grenzen fest. Die Genehmigungsrichtlinie bestimmt, wann der
Agent anhalten und eine Genehmigung anfordern muss, bevor er sie überschreitet.

## Funktionsweise der Sandbox

Die Sandbox gilt für gestartete Befehle und nicht nur für integrierte
Dateioperationen. Wenn der Agent Tools wie `git`, Paketmanager oder Test-Runner ausführt,
unterliegen diese Befehle denselben Sandbox-Grenzen.

Codex setzt die Beschränkungen auf jedem Betriebssystem mit plattformeigenen Mechanismen durch. Die Implementierung ist
unter macOS, Linux, WSL2 und nativem Windows unterschiedlich, doch das Prinzip ist auf allen
Oberflächen gleich: Der Agent erhält einen abgegrenzten Arbeitsbereich, damit er Routineaufgaben
innerhalb klarer Grenzen autonom ausführen kann.

## Warum das wichtig ist

Die Sandbox reduziert die Belastung durch häufige Genehmigungsanfragen. Statt jeden
Befehl mit geringem Risiko von dir bestätigen zu lassen, kann der Agent Dateien lesen, Änderungen vornehmen und routinemäßige
Projektbefehle innerhalb des bereits von dir genehmigten Rahmens ausführen.

Außerdem erhältst du ein klareres Vertrauensmodell für agentisches Arbeiten. Du vertraust nicht nur
auf die Absichten des Agenten, sondern kannst dich darauf verlassen, dass er
technisch durchgesetzte Grenzen einhält. So kannst du den Agenten leichter selbstständig arbeiten lassen
und weißt trotzdem, wann er anhält und um Hilfe bittet.

## Erste Schritte

Im standardmäßigen Berechtigungsmodus wird Sandboxing automatisch angewendet.

### Voraussetzungen

Unter **macOS** funktioniert Sandboxing ohne zusätzliche Konfiguration mit dem integrierten
Seatbelt-Framework.

Unter **Windows** verwendet Codex die native [Sandbox für
Windows](/de-DE/codex/windows/windows-sandbox#windows-sandbox), wenn du PowerShell nutzt, und die
Linux-Sandbox-Implementierung, wenn du WSL2 nutzt.

Installiere unter **Linux und WSL2** zuerst `bubblewrap` mit deinem Paketmanager:

  <div slot="ubuntu-debian">

```bash
sudo apt install bubblewrap

  </div>

  <div slot="fedora">

```bash
sudo dnf install bubblewrap

  </div>

Codex verwendet die erste ausführbare Datei für `bwrap`, die es in `PATH` findet. Ist `bwrap` nicht als ausführbare Datei
verfügbar, greift Codex auf ein mitgeliefertes Hilfsprogramm zurück. Dieses
setzt jedoch voraus, dass nicht privilegierte Benutzer-Namespaces erstellt werden können. Die Installation des
Distributionspakets, das `bwrap` bereitstellt, sorgt für ein zuverlässiges Setup.

Codex zeigt beim Start eine Warnung an, wenn `bwrap` fehlt oder das Hilfsprogramm
den benötigten Benutzer-Namespace nicht erstellen kann. Bei Distributionen mit dieser
AppArmor-Einschränkung solltest du das AppArmor-Profil für `bwrap` laden, damit `bwrap`
weiter funktioniert, ohne die Einschränkung global zu deaktivieren.

  **Hinweis zu AppArmor unter Ubuntu:** Unter Ubuntu 25.04 sollte die Installation von `bubblewrap` aus
  dem Paket-Repository von Ubuntu ohne zusätzliches AppArmor-Setup funktionieren. Das Profil
`bwrap-userns-restrict` wird im Paket `apparmor` unter
`/etc/apparmor.d/bwrap-userns-restrict` bereitgestellt.

Unter Ubuntu 24.04 warnt Codex möglicherweise weiterhin, dass der benötigte Benutzer-Namespace nicht erstellt werden kann,
auch wenn `bubblewrap` installiert ist. Kopiere und lade das zusätzliche Profil:

```bash
sudo apt update
sudo apt install apparmor-profiles apparmor-utils
sudo install -m 0644 \
  /usr/share/apparmor/extra-profiles/bwrap-userns-restrict \
  /etc/apparmor.d/bwrap-userns-restrict
sudo apparmor_parser -r /etc/apparmor.d/bwrap-userns-restrict

`apparmor_parser -r` lädt das Profil ohne Neustart in den Kernel. Du
kannst auch alle AppArmor-Profile neu laden:

```bash
sudo systemctl reload apparmor.service

Wenn dieses Profil nicht verfügbar ist oder das Problem nicht behebt, kannst du die
AppArmor-Einschränkung für nicht privilegierte Benutzer-Namespaces mit folgendem Befehl deaktivieren:

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0

## So funktionieren Berechtigungen

Verwende die Berechtigungssteuerung der jeweiligen Oberfläche, um festzulegen, wie Codex mit lokalen
Aktionen umgeht.

Genehmigungen legen fest, wann Codex vor einer Aktion pausiert. Die Sandbox
bestimmt dagegen, auf welche Dateien und Netzwerkressourcen Befehle zugreifen können. Wenn eine
Genehmigung verschiedene Geltungsbereiche anbietet, etwa einmalig oder für die Sitzung,
wähle den engsten Bereich, in dem die Aufgabe fortgesetzt werden kann. Behalte die Projektgrenze
als Standard bei. Verwende separate Projekte oder Worktrees, statt den Zugriff
auf nicht zusammengehörige Repositorys auszuweiten.

ChatGPT Work führt Code und Shell-Befehle in einer verwalteten, isolierten Umgebung aus.
Die Workspace-Richtlinie und toolspezifische Steuerelemente legen fest, welche Funktionen
verfügbar sind. Wenn die Einstellung verfügbar ist, kannst du unter **Einstellungen \> Datenkontrollen \>
Work-Netzwerkzugriff** den Netzwerkzugriff für Code und Shell-Befehle verwalten. Aktiviere
**Öffentlichen Internetzugriff zulassen** , damit diese Befehle auf das öffentliche
Internet zugreifen können. Ist die Option deaktiviert, können Befehle nur die erforderlichen Hostnamen aus einer
verwalteten Zulassungsliste erreichen.

Für die Websuche, Plug-ins und den Remote-Browser gibt es separate Steuerelemente.
Änderungen werden wirksam, nachdem die aktuelle Code- oder Shell-Ausführung beendet ist und Work
seine Ausführungsumgebung aktualisiert hat. In ChatGPT Web sind die lokale
Codex-Sandbox und die Auswahl des Genehmigungsmodus nicht verfügbar.

Verwende in der ChatGPT-Desktop-App die Berechtigungssteuerung unter dem Editor.
Je nach Konfiguration kann das Menü **Genehmigung anfordern**,
**Für mich genehmigen** für geeignete Genehmigungsanfragen, **Vollzugriff** sowie benannte oder
benutzerdefinierte Berechtigungsprofile enthalten.

Gib in der CLI
[`/permissions`](/codex/developer-commands?surface=cli#cli-update-permissions-with-permissions)
ein, um die Berechtigungsauswahl zu öffnen und das aktive Berechtigungsprofil zu ändern.

Verwende in der IDE-Erweiterung die Berechtigungssteuerung unter dem Editor.
Je nach Konfiguration kann das Menü **Genehmigung anfordern**,
**Für mich genehmigen** für geeignete Genehmigungsanfragen, **Vollzugriff** sowie benannte oder
benutzerdefinierte Berechtigungsprofile enthalten.

<div class="not-prose my-8 max-w-[18rem] mr-auto">
  
    
      
    
  
</div>

<a id="configure-defaults"></a>

## Standardeinstellungen konfigurieren

Lege in `config.toml` Standardwerte fest, damit Codex sich bei jedem Start gleich verhält.
[Grundlagen der Konfiguration](/de-DE/codex/config-file/config-basic) erklärt die Funktionsweise. Die
[Konfigurationsreferenz](/de-DE/codex/config-file/config-reference) dokumentiert die genauen Schlüssel
`sandbox_mode`, `approval_policy`, `approvals_reviewer` und
`sandbox_workspace_write.writable_roots`. Mit diesen Einstellungen legst du fest, wie viel
Autonomie der Agent standardmäßig erhält, in welche Verzeichnisse er schreiben darf, wann er
für eine Genehmigung pausieren soll und wer geeignete Genehmigungsanfragen prüft.

Die gängigen Sandbox-Modi im Überblick:

- `read-only`: Der Agent kann Dateien einsehen, aber ohne Genehmigung weder Dateien bearbeiten noch
  Befehle ausführen.
- `workspace-write`: Der Agent kann Dateien lesen, im Workspace bearbeiten und
  innerhalb dieses Bereichs routinemäßige lokale Befehle ausführen. Dieser Standardmodus ermöglicht unkompliziertes
  lokales Arbeiten.
- `danger-full-access`: Der Agent arbeitet ohne Sandbox-Einschränkungen. Dadurch entfallen
  die Grenzen für Dateisystem und Netzwerk. Verwende diesen Modus nur, wenn
  der Agent mit Vollzugriff arbeiten soll.

Die gängigen Genehmigungsrichtlinien sind:

- `untrusted`: Der Agent fordert vor der Ausführung von Befehlen, die nicht als
  vertrauenswürdig eingestuft sind, eine Genehmigung an.
- `on-request`: Der Agent arbeitet standardmäßig innerhalb der Sandbox und fordert eine Genehmigung an, wenn er
  diese Grenze überschreiten muss.
- `never`: Der Agent hält für Genehmigungsanfragen nicht an.

Bei interaktiven Genehmigungen kannst du mit
`approvals_reviewer` außerdem festlegen, wer sie prüft:

- `user`: Genehmigungsanfragen werden dir angezeigt. Dies ist die Standardeinstellung.
- `auto_review`: Geeignete Genehmigungsanfragen werden an einen Prüfagenten weitergeleitet (siehe
[Automatische Überprüfung](/de-DE/codex/sandboxing/auto-review)).

Vollzugriff bedeutet, `sandbox_mode = "danger-full-access"` zusammen mit
`approval_policy = "never"` zu verwenden. Die risikoärmere Voreinstellung für lokale Automatisierung
kombiniert dagegen `sandbox_mode = "workspace-write"` mit
`approval_policy = "on-request"`. Alternativ kannst du die entsprechenden CLI-Flags
`--sandbox workspace-write --ask-for-approval on-request` verwenden. Für manuelle Genehmigungen kannst du
`approvals_reviewer = "user"` beibehalten oder für die automatische Überprüfung von Genehmigungsanfragen
`approvals_reviewer = "auto_review"` festlegen.

Wenn der Agent in mehreren Verzeichnissen arbeiten soll, kannst du mit beschreibbaren Stammverzeichnissen
den Bereich erweitern, in dem er Änderungen vornehmen darf, ohne die Sandbox vollständig aufzuheben.
Benötigst du eine weiter oder enger gefasste Vertrauensgrenze, passe den standardmäßigen Sandbox-Modus
und die Genehmigungsrichtlinie an, statt dich auf einmalige Ausnahmen zu verlassen.

Wenn ein Ablauf eine bestimmte Ausnahme erfordert, verwende [Regeln](/de-DE/codex/agent-configuration/rules). Damit
kannst du Befehlspräfixe außerhalb der Sandbox zulassen, nur nach Rückfrage erlauben oder verbieten. Das ist
oft sinnvoller, als den Zugriff pauschal auszuweiten. Wo du IDE-spezifische Einstellungen
findest, erfährst du unter [Einstellungen der Codex IDE-Erweiterung](/codex/developer-settings?surface=ide).

Wenn die automatische Überprüfung verfügbar ist, ändert sie die Sandbox-Grenze nicht. Sie ist
eine der möglichen Optionen für `approvals_reviewer` bei Genehmigungsanfragen an dieser Grenze, etwa
bei Sandbox-Eskalationen, blockiertem Netzwerkzugriff oder Tool-Aufrufen mit Nebenwirkungen,
die weiterhin genehmigt werden müssen. Aktionen, die innerhalb der Sandbox bereits zulässig sind, werden
ohne zusätzliche Überprüfung ausgeführt. Details zum Lebenszyklus des Prüfagenten, zu Auslösertypen und
zur Semantik von Ablehnungen sowie zur Konfiguration findest du unter
[Automatische Überprüfung](/de-DE/codex/sandboxing/auto-review).

Details zu den einzelnen Plattformen findest du in der jeweiligen Dokumentation. Informationen zu Setup,
Verhalten und Fehlerbehebung unter nativem Windows findest du unter [Windows](/de-DE/codex/windows/windows-sandbox). Anforderungen an die Administration
und organisationsweite Einschränkungen für Sandboxing und Genehmigungen findest du unter
[Agentenfreigaben und Sicherheit](/de-DE/codex/agent-approvals-security).

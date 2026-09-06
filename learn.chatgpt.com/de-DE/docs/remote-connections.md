<!-- source: https://learn.chatgpt.com/de-DE/docs/remote-connections -->

Desktop,
  Storage,
  Terminal,
} from "@components/react/oai/platform/ui/Icon.react";

Mit Remote-Verbindungen greifst du auf Aufgaben zu, die auf einem anderen Gerät oder Computer ausgeführt werden.
Öffne in der mobilen ChatGPT-App **Remote** , um mit ChatGPT- oder Codex-Chats auf
einem verbundenen Mac- oder Windows-Gerät zu arbeiten. Du kannst deine Arbeit auch auf einem anderen
unterstützten Gerät mit der ChatGPT-Desktop-App fortsetzen oder die App mit Projekten
auf einem SSH-Host verbinden.

Beim Fernzugriff werden die Projekte, Chats, Dateien, Anmeldedaten,
Berechtigungen, Plug-ins, die Computernutzung, das Browser-Setup und die lokalen Tools des verbundenen Hosts verwendet.

## Was du per Fernzugriff tun kannst

- Starte neue Chats in Projekten auf dem Host oder setze bestehende Chats fort.
- Sende weitere Anweisungen, beantworte Fragen und steuere laufende Aufgaben.
- Genehmige Befehle und andere Aktionen.
- Prüfe Ausgaben, Diffs, Testergebnisse, Terminalausgaben und Screenshots.
- Lass dich benachrichtigen, wenn ChatGPT eine Aufgabe abschließt oder deine Aufmerksamkeit benötigt.
- Wechsle zwischen verbundenen Hosts und Chats.

In den nächsten Abschnitten erfährst du, wie du in der mobilen ChatGPT-App **Remote** öffnest, um auf einen
Desktop-Host zuzugreifen. Wie du Codex mit einem Projekt auf einem SSH-Host verbindest, erfährst du unter
[Mit einem SSH-Host verbinden](#connect-to-an-ssh-host).

<div class="not-prose my-6 max-w-4xl rounded-xl bg-[url('/images/codex/codex-wallpaper-1.webp')] bg-cover bg-center p-4 md:p-8">
  
    
      
    
  
</div>

<a id="before-you-set-up-mobile-access"></a>

## Bevor du Remote einrichtest

  Remote unterstützt Hosts, auf denen die ChatGPT-Desktop-App unter macOS oder Windows ausgeführt wird.
  Du kannst einen Host über ChatGPT unter iOS oder Android oder über einen anderen Mac oder ein anderes
  Windows-Gerät steuern, wenn **Andere Geräte steuern** verfügbar ist. Die Verfügbarkeit kann
  je nach Rollout variieren.

Du benötigst:

- Codex-Zugriff für das ChatGPT-Konto und den Workspace, die du verwenden möchtest.
- Die neueste mobile ChatGPT-App auf einem iOS- oder Android-Gerät. Wenn **Remote**
  nicht in der App angezeigt wird, aktualisiere zuerst ChatGPT.
- Die neueste ChatGPT-Desktop-App für macOS oder Windows auf einem Host, der aktiv,
online und bei demselben Konto und Workspace angemeldet ist. Das mobile Setup startest du
in der App. Über die Codex CLI oder IDE-Erweiterung kannst du es nicht einrichten.
- Alle erforderlichen Einstellungen für die Multi-Faktor-Authentifizierung, SSO oder Passkeys
in diesem Konto oder Workspace.

Wenn du Codex über einen ChatGPT-Workspace nutzt, muss die Administration deines Workspaces möglicherweise den Zugriff
per Remote-Steuerung aktivieren, bevor du dich über dein Smartphone verbinden kannst.

<a id="set-up-mobile-access"></a>

## Remote einrichten

Beginne in der ChatGPT-Desktop-App auf dem Host, den du verbinden möchtest. Der Setup-Ablauf
aktiviert den Fernzugriff für diesen Host und zeigt dann einen QR-Code an, den du mit deinem
Smartphone scannen kannst.
Der QR-Code koppelt das Smartphone mit dem Host. Kopple jedes Smartphone und jedes unterstützte
Gerät mit Desktop-App mit jedem Host, den es steuern soll.

  Bestehende Verbindungen, die seit dem 8. Juni 2026 verwendet wurden, bleiben gekoppelt. Wenn du eine bestehende
Verbindung seit dem 8. Juni 2026 nicht verwendet hast, aktualisiere beide Apps und kopple die
Geräte erneut.

1. Starte das Remote-Setup.

   Öffne die ChatGPT-Desktop-App auf dem Host. Rufe **Einstellungen** \>
**Verbindungen** \> **Diesen Mac oder PC steuern** auf und wähle dann **Einrichten** oder
**Hinzufügen** aus. Genehmige den Fernzugriff und schließe alle angeforderten Verifizierungsschritte ab.

2. Scanne den QR-Code.

   Scanne mit deinem Smartphone den in der App angezeigten QR-Code. Der Code öffnet ChatGPT,
damit du die Verbindung zwischen der mobilen App und dem Host abschließen kannst.

3. Schließe das Setup in ChatGPT ab.

   ChatGPT öffnet den Remote-Setup-Ablauf. Bestätige, dass du dasselbe ChatGPT-Konto
und denselben Workspace verwendest, und schließe alle erforderlichen Schritte für die Multi-Faktor-Authentifizierung, SSO
oder Passkeys ab. Nach erfolgreichem Setup wird der Host auf deinem Smartphone unter Remote
angezeigt.

4. Prüfe die Host-Einstellungen.

   Verwalte in der App auf dem Host unter **Einstellungen** \> **Verbindungen** die verbundenen
   Geräte. Du kannst den Computer außerdem aktiv halten, die
   Computernutzung aktivieren oder die Chrome-Erweiterung installieren.

  

## Wähle aus, was du verbinden möchtest

Beginne mit dem Laptop oder Desktop-Computer, auf dem du ChatGPT bereits verwendest. Füge einen dauerhaft eingeschalteten
Computer oder SSH-Host hinzu, wenn du dauerhaften Zugriff oder eine andere Umgebung benötigst.

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>Dein Laptop oder Desktop-Computer</span></span>

Verbinde den Mac oder Windows-PC, auf dem die Desktop-App bereits installiert ist. So kannst du
aus der Ferne auf dieselben Projekte, Chats, Anmeldedaten, Plug-ins und dasselbe lokale
Setup zugreifen, das du bereits nutzt.

Wenn dieser Computer in den Ruhezustand wechselt, die Netzwerkverbindung verliert oder die App geschlossen wird,
ist kein Fernzugriff möglich, bis der Host wieder verfügbar ist. Verwendest du diesen Computer als Host,
lasse ihn an die Stromversorgung angeschlossen und nutze, sofern verfügbar, die Verbindungseinstellungen des Hosts,
um ihn aktiv zu halten.

Auf einem Mac-Laptop kann der Fernzugriff verfügbar bleiben, wenn der Deckel geöffnet und das Gerät an die Stromversorgung
angeschlossen ist. Bei geschlossenem Deckel musst du zusätzlich ein externes Display anschließen. Wenn du
**Ruhezustand** auswählst, wird der Fernzugriff dennoch beendet.

Halte auf einem Windows-Host die Sitzung entsperrt und für Aufgaben verfügbar, die
[Computernutzung](/de-DE/codex/computer-use) verwenden. Die Computernutzung unter Windows wird im
Vordergrund ausgeführt. Die Remote-Steuerung eignet sich daher am besten, um Aufgaben zu starten oder zu überprüfen, während du
den Host-Desktop für die Aufgabe reservierst.

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>Ein dedizierter, dauerhaft eingeschalteter Computer</span></span>

Verwende einen dedizierten, dauerhaft eingeschalteten Mac oder Windows-PC, wenn ChatGPT für länger laufende Aufgaben
erreichbar bleiben soll.

Richte auf diesem Computer die Projekte, Anmeldedaten, MCP-Server, Skills und Tools ein, die ChatGPT oder
Codex verwenden soll.

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>Eine Remote-Entwicklungsumgebung</span></span>

Verwende einen SSH-Host oder eine verwaltete Remote-Entwicklungsumgebung, wenn das Projekt
bereits in einer Remote-Umgebung liegt. Verbinde den Host der Desktop-App zuerst mit dieser
Umgebung. Dein Smartphone verbindet sich weiterhin mit demselben Host, und ChatGPT arbeitet
in der Remote-Umgebung mit deren Abhängigkeiten, Sicherheitsrichtlinien und
Rechenressourcen.

Weitere Informationen zum SSH-Setup findest du unter [Mit einem SSH-Host verbinden](#connect-to-an-ssh-host).

  Aktiviere für Browser- oder Desktop-Aufgaben auf einem dauerhaft eingeschalteten Computer oder Remote-Host die
Computernutzung und installiere die Chrome-Erweiterung auf diesem Host.

## Was der verbundene Host bereitstellt

Dein Smartphone sendet Prompts, Genehmigungen und weitere Nachrichten an ChatGPT. Der
verbundene Host stellt die Umgebung bereit, die ChatGPT verwendet.

Das bedeutet:

- Die Dateien im Repository und lokale Dokumente stammen vom verbundenen Host.
- Shell-Befehle werden auf diesem Host oder in der Remote-Umgebung ausgeführt.
- MCP-Server, Skills, Browserzugriff und Computernutzung stammen aus der
Konfiguration dieses Hosts.
- Websites mit aktiver Anmeldung und Desktop-Apps sind nur verfügbar, wenn der Host darauf
zugreifen kann.
- Die Sandboxing-Einstellungen, Sicherheitskontrollen und Genehmigungen für Aktionen gelten weiterhin
für die verbundene Sitzung.

Eine sichere Relay-Ebene sorgt dafür, dass vertrauenswürdige Computer von deinen autorisierten
ChatGPT-Geräten aus erreichbar sind, ohne sie direkt im öffentlichen Internet zugänglich zu machen.

## Arbeit auf einem anderen Gerät fortsetzen

Du kannst deine Arbeit auf einem anderen angemeldeten Gerät fortsetzen, auf dem die
ChatGPT-Desktop-App läuft und das Remote-Steuerung unterstützt. Wenn dein Laptop beispielsweise nicht verfügbar ist,
kannst du über dein Smartphone einen Chat auf einem dauerhaft eingeschalteten Host starten und später die App
auf deinem Laptop öffnen, um denselben Chat dort fortzusetzen.

Auf einem Mac- oder Windows-Gerät, auf dem die Funktion verfügbar ist, kannst du unter **Einstellungen \>
Verbindungen \> Andere Geräte steuern** den anderen Host hinzufügen. Ein Gerät kann gleichzeitig
Fernzugriff zulassen und ein anderes Gerät steuern.

  

## Mit einem SSH-Host verbinden

Füge in der ChatGPT-Desktop-App Remote-Projekte von einem SSH-Host hinzu und führe Chats
mit Zugriff auf dessen Dateisystem und Shell. Chats in Remote-Projekten führen Befehle aus,
lesen Dateien und schreiben Änderungen auf dem Remote-Host.

Konfiguriere den Remote-Host nach denselben Sicherheitsanforderungen wie beim
normalen SSH-Zugriff: vertrauenswürdige Schlüssel, Konten mit minimalen Berechtigungen und keine
öffentlich erreichbaren Listener ohne Authentifizierung.

1. Füge den Host deiner SSH-Konfiguration hinzu, damit Codex ihn automatisch erkennen kann.

   ```text
   Host devbox
     HostName devbox.example.com
     User you
     IdentityFile ~/.ssh/id_ed25519

   Codex liest konkrete Host-Aliasse aus `~/.ssh/config`, löst sie mit
   OpenSSH auf und ignoriert Hosts, die ausschließlich über Muster definiert sind.

2. Stelle sicher, dass du von dem Computer, auf dem die App ausgeführt wird, per SSH auf den Host zugreifen kannst.

   ```bash
   ssh devbox

3. Installiere Codex auf dem Remote-Host und führe dort die Authentifizierung durch.

   Die App startet den Codex App Server über SSH und verwendet dabei die Login-Shell
   des Remote-Benutzerkontos. Stelle sicher, dass der Befehl `codex` in dieser Shell im
   `PATH` des Remote-Hosts verfügbar ist.

4. Öffne in der App **Einstellungen \> Verbindungen**, füge den SSH-Host hinzu oder aktiviere ihn und
   wähle dann einen Remote-Projektordner aus.

  

<a id="hand-off-a-thread-between-hosts"></a>
<a id="hand-off-a-chat-between-hosts"></a>
<a id="hand-off-a-task-between-hosts"></a>

## Chat zwischen Hosts übergeben

Mit der Übergabe verschiebst du einen bestehenden Chat samt Git-Status zwischen deinem lokalen Computer
und einem verbundenen Remote-Host. So kannst du die Arbeit lokal beginnen, in einem
Worktree auf einem Remote-Computer fortsetzen und den Chat später zurückholen.

Verbinde vor der Übergabe eines Chats den Ziel-Host und speichere dort ein Projekt
für dasselbe Git-Repository. Ist das Projekt ein Unterverzeichnis
des Repositorys, speichere auf beiden Hosts dasselbe Unterverzeichnis. Codex zeigt nur
Ziele an, für die ein passendes Projekt gespeichert ist.

So übergibst du einen Chat:

1. Öffne den Chat in der Desktop-App.
2. Wähle in der Fußzeile des Chats zuerst den aktuellen Ausführungsort und dann den
   Ziel-Host aus. Wähle **Dieser Computer** aus, wenn du einen Remote-Chat zurück
   auf deinen lokalen Computer übergibst.
3. Prüfe das Ziel sowie den Branch und wähle dann **Übergeben** aus.

Codex erstellt auf dem Ziel-Host einen Worktree oder verwendet dort einen vorhandenen, überträgt den
Chat und den Git-Status und stellt den Chat auf diesen Host um. Wenn der Chat gerade
läuft, unterbricht die Übergabe die aktuelle Antwort, bevor der Chat übertragen wird.

Du kannst Codex auch in einem anderen Chat bitten, einen benannten Chat an einen
verbundenen Host zu übergeben. Codex kann den Chat, aus dem die Anfrage stammt, nicht übergeben, und die Übergabe
an eine Codex-Cloud-Umgebung wird nicht unterstützt.

## Authentifizierung und Erreichbarkeit im Netzwerk

Remote-Verbindungen verwenden SSH, um den Codex App Server auf dem Remote-Host zu starten und zu verwalten.
Mache die Transportschnittstellen des App Servers nicht direkt in einem gemeinsam genutzten oder öffentlichen Netzwerk zugänglich.

Wenn du außerhalb deines aktuellen Netzwerks auf einen Remote-Computer zugreifen musst, verwende ein VPN
oder ein Tool für Mesh-Netzwerke, statt den App Server direkt im
Internet zugänglich zu machen.

## Fehlerbehebung

### Der Host wird auf deinem Smartphone nicht angezeigt

Vergewissere dich, dass die Desktop-App auf dem Host ausgeführt wird, **Verbindungen von
anderen Geräten zulassen** aktiviert ist und beide Geräte dasselbe ChatGPT-Konto und
denselben Workspace verwenden. Wenn du die Verbindung seit dem 8. Juni 2026 nicht verwendet hast, aktualisiere beide
Apps und kopple die Geräte erneut.

### Die Remote-Steuerung ist nach der erneuten Anmeldung deaktiviert

Wenn du dich bei ChatGPT abmeldest, wird die **Remote-Steuerung** deaktiviert, aber deine
bestehenden Gerätekopplungen bleiben erhalten. Aktiviere nach der erneuten Anmeldung die **Remote-Steuerung** , um
den vorherigen Verbindungsstatus wiederherzustellen.

Wenn ein Fehler angezeigt wird, nachdem du die **Remote-Steuerung** aktiviert und **Hinzufügen** ausgewählt hast,
starte die ChatGPT-Desktop-App auf dem Host neu und versuche es erneut.

### Die Genehmigungsanfrage wird nicht angezeigt

Öffne in der mobilen ChatGPT-App **Remote**. Vergewissere dich, dass Smartphone und Host
dasselbe ChatGPT-Konto und denselben Workspace verwenden. Scanne dann den QR-Code erneut oder starte
das Setup vom Host aus neu. Wenn du einen ChatGPT-Workspace verwendest, wende dich an die Workspace-Administration und lass dir bestätigen,
dass der Zugriff auf die Remote-Steuerung aktiviert ist.

### Die Remote-Sitzung wird getrennt

Prüfe, ob der Host in den Ruhezustand gewechselt ist, die Netzwerkverbindung unterbrochen wurde oder die App geschlossen wurde.
Sorge dafür, dass der Host aktiv und mit dem Netzwerk verbunden bleibt, während ChatGPT arbeitet.

### Die Authentifizierung blockiert das Setup

Schließe den beim Setup angezeigten Authentifizierungsschritt für dein Konto oder deinen Workspace ab. Wenn
deine Organisation SSO, Multi-Faktor-Authentifizierung oder einen Passkey verlangt,
schließe diesen Vorgang ab, bevor du es erneut versuchst. Falls das Setup weiterhin fehlschlägt, bitte die Administration deines Workspaces
zu bestätigen, dass sie den Zugriff auf die Remote-Steuerung aktiviert hat.

## Siehe auch

- [ChatGPT-Desktop-App](/de-DE/codex/app)
- [Funktionen](/de-DE/codex/features)
- [Einstellungen der ChatGPT-Desktop-App](/codex/reference/settings)
- [Computernutzung](/de-DE/codex/computer-use)
- [Chrome-Erweiterung](/de-DE/codex/chrome-extension)
- [Befehlszeilenoptionen](/codex/developer-commands?surface=cli)
- [Authentifizierung](/de-DE/codex/auth)

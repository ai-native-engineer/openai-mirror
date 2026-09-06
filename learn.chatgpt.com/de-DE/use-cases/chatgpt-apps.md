<!-- source: https://learn.chatgpt.com/de-DE/use-cases/chatgpt-apps -->

## Was du entwickelst

Jedes MCP-gestützte Plug-in besteht aus drei Teilen:

- Ein MCP-Server, der Tools definiert, Daten zurückgibt, die Authentifizierung durchsetzt und ChatGPT auf etwaige UI-Ressourcen verweist.
- Eine optionale Webkomponente, die in einem Iframe in ChatGPT dargestellt wird. Du kannst sie mit React oder nur mit HTML, CSS und JavaScript entwickeln.
- Ein Modell, das anhand der von dir bereitgestellten Metadaten entscheidet, wann es die Tools des Plug-ins aufruft.

Codex ist besonders hilfreich, wenn es die wiederkehrenden Entwicklungsaufgaben rund um diese Komponenten übernimmt:

- Tool-Schnittstelle und Metadaten planen.
- Grundgerüst für Server und Widget erstellen.
- Lokale Startskripte einbinden.
- Änderungen für Authentifizierung und Deployment schrittweise und gezielt umsetzen.
- Einen Prüfablauf implementieren, der nachweist, dass das Plug-in in ChatGPT funktioniert.

## Warum Codex gut dafür geeignet ist

- MCP-gestützte Plug-ins lassen sich klar in einen Server, eine optionale UI und modellgesteuerte
Tool-Aufrufe gliedern.
- Prompting mit Codex funktioniert am besten, wenn die Aufgabe eindeutig und klar abgegrenzt ist und
sich einfach überprüfen lässt. Das passt gut zur Entwicklung von Plug-ins.
- Skills und `AGENTS.md` geben Codex die nötigen wiederverwendbaren Anweisungen und Projektregeln, damit es sich am Projektkontext orientiert.

Weitere Informationen zur Installation und Verwendung von Skills findest du in unserer [Dokumentation zu Skills](/de-DE/codex/build-skills).

## So gehst du vor

## Voraussetzungen

- Konzentriere dich zunächst auf ein zentrales Nutzungsziel, statt zu versuchen, ein vollständiges Produkt in den Chat zu übertragen.
- Lege den Stack vorab fest: TypeScript oder Python für den Server sowie React oder nur HTML, CSS und JavaScript für das Widget.
- Lege fest, wie du während der Entwicklung HTTPS bereitstellst, zum Beispiel über `ngrok` oder Cloudflare Tunnel.
- In manchen Einstellungen werden für die Verbindung mit einem MCP-Server noch ältere Begriffe verwendet. Gehe bei
lokalen Tests davon aus, dass sich diese Bezeichnungen auf den registrierten Server beziehen.

1. Beginne mit einem klar umrissenen Ziel für das Plug-in und bitte Codex, drei bis fünf Tools mit eindeutigen Namen und Beschreibungen sowie klar definierten Ein- und Ausgaben vorzuschlagen.
2. Entscheide, ob v1 zunächst nur Daten bereitstellen kann oder ein Widget benötigt. Erstelle dann anhand vorhandener Muster im Repository ein Grundgerüst für den MCP-Server und das optionale Widget, bevor du Abhängigkeiten hinzufügst.
3. Führe den MCP-Server lokal über HTTPS aus, verbinde ihn im Entwicklermodus mit ChatGPT und teste ihn mit einem kleinen Set aus direkten, indirekten und negativen Prompts.
4. Optimiere schrittweise die Metadaten, die Zustandsverwaltung sowie die Payloads für `structuredContent` und `_meta`, bis der zentrale Leseablauf in ChatGPT zuverlässig funktioniert.
5. Füge OAuth 2.1 nur hinzu, wenn kontospezifische Daten oder Schreibaktionen dies erfordern, ohne dadurch anonyme Abläufe oder Abläufe ohne Schreibzugriff zu verkomplizieren.
6. Bereite eine gehostete Vorschau mit einem stabilen Endpunkt unter `/mcp` vor, überprüfe Streaming und Hosting der UI-Assets und gehe die Checkliste für die Veröffentlichung durch, bevor du das Plug-in freigibst oder einreichst.

## Vorgeschlagene Prompts

Gute Prompts für diesen Workflow haben folgende Bestandteile gemeinsam:

- Ein klares Ziel: Beschreibe, wobei das Plug-in in ChatGPT helfen soll.
- Ein konkreter Stack: Gib an, ob du TypeScript oder Python für den Server verwenden möchtest und ob das Widget React nutzen oder schlank bleiben soll.
- Klare Tool-Grenzen: Bitte Codex, eine kleine Auswahl an Tools vorzuschlagen oder zu entwickeln, wobei jedes Tool genau eine Aufgabe übernimmt.
- Anforderungen an die Authentifizierung: Gib an, ob die erste Version anonym funktionieren kann oder ob sie verknüpfte Konten und Schreibaktionen benötigt.
- Lokale Entwicklung: Nenne den vorgesehenen Tunnel oder Hosting-Weg für HTTPS-Tests in ChatGPT.
- Prüfschritte: Gib Codex vor, welche Befehle es ausführen, welche Prompts es testen und welche Nachweise es anschließend liefern soll.

Vermeide einen überladenen Prompt, der Planung, Implementierung, Authentifizierung, Deployment, Einreichung und Feinschliff in einem Durchgang abdecken soll. Unterteile die Arbeit stattdessen in kleinere Meilensteine.

**Plane das Plug-in, bevor du sein Grundgerüst erstellst**

**Erstelle das Grundgerüst für die erste funktionsfähige Version**

**Füge die Authentifizierung erst hinzu, wenn der zentrale Ablauf funktioniert**

**Bereite das Plug-in auf die Bereitstellung und das Review vor**

## Veröffentlichungsreife

- Das Plug-in ist auf ein einziges, für Nutzende klar verständliches Ziel ausgerichtet.
- Die Zahl der Tools bleibt gering, und Metadaten, Eingaben sowie Ausgaben sind eindeutig definiert.
- Der MCP-Server funktioniert durchgängig, gibt in `structuredContent` kompakte Daten zurück und legt ausschließlich für das Widget bestimmte Daten in `_meta` ab.
- Wenn ein Widget erforderlich ist, wird es in ChatGPT korrekt gerendert.
- Ein lokaler HTTPS-Testzyklus lässt sich im Entwicklermodus von ChatGPT erfolgreich ausführen.
- Die Tests mit einem kleinen Satz direkter, indirekter und negativer Prompts verlaufen erfolgreich; Gesprächsablauf und Tool-Payloads entsprechen den Erwartungen.
- Authentifizierung wird nur dort hinzugefügt, wo sie für Daten einzelner Nutzender oder für Schreibaktionen erforderlich ist.
- Ein Bereitstellungsplan und ein Review der Veröffentlichungsreife decken Metadaten, Tool-Hinweise, Datenschutz und Test-Prompts ab, bevor das Plug-in geteilt oder eingereicht wird.

## Häufige Fallstricke

- Codex damit beauftragen, das gesamte Produkt in ChatGPT zu übertragen. Besser: Bitte Codex, sich auf ein einziges zentrales Ziel für Nutzende, drei bis fünf Tools und ein klar begrenztes Widget zu beschränken.
- Mit einem überfrachteten Implementierungs-Prompt beginnen. Besser: Teile die Arbeit in einzelne Durchläufe für Planung, Grundgerüst, Authentifizierung, Bereitstellung und Review auf.
- Die Benutzeroberfläche entwickeln, bevor die Tool-Schnittstelle klar definiert ist. Besser: Plane zuerst die Tool-Schnittstelle und das Antwortschema und entwickle dann das Widget.
- Die offizielle Dokumentation nicht als Grundlage verwenden. Besser: Verwende `$chatgpt-apps` zusammen mit `$openai-docs`, damit das Grundgerüst den aktuellen Empfehlungen für Plug-ins folgt.
- Metadaten als Nebensache behandeln. Besser: Verfasse frühzeitig Tool-Beschreibungen und eine Parameterdokumentation und prüfe sie anschließend erneut mit einem Satz von Prompts.
- Authentifizierung hinzufügen, bevor der anonyme Ablauf oder der Ablauf ohne Schreibzugriff verifiziert ist. Besser: Sorge zuerst dafür, dass der zentrale Tool-Ablauf funktioniert, und füge OAuth dann nur bei den Tools hinzu, für die es tatsächlich erforderlich ist.
- Das Plug-in für fertig erklären, ohne es zuvor in ChatGPT zu testen. Besser: Verbinde
den MCP-Server im Entwicklermodus, prüfe die Tool-Payloads und verifiziere den tatsächlichen
Gesprächsablauf.

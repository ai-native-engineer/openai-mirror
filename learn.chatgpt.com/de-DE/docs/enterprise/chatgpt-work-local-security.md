<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/chatgpt-work-local-security -->

ChatGPT Work kann genehmigte Dateien, Anwendungen und Browsersitzungen auf den Computern der Nutzenden verwenden, um lokale Aufgaben zu erledigen. Der Zugriff hängt von den Workspace-Berechtigungen, dem bestehenden Kontozugriff der jeweiligen Person, den Betriebssystemberechtigungen, den Genehmigungen für Anwendungen und den unterstützten Geräterichtlinien ab.

Die lokalen Funktionen hängen von der unterstützten Desktop-App, dem Betriebssystem, den Nutzungsberechtigungen des Workspace, den Rollenberechtigungen, der Geräterichtlinie und dem Produkt-Rollout ab.

## Sicherheit auf einen Blick

- Lokale Aufgaben werden über die ChatGPT-Desktop-App ausgeführt. Eine gehostete Cloud-Aufgabe wird nicht zur lokalen Aufgabe, wenn du sie in derselben App öffnest.

- Welche Kontrollen für lokales und gehostetes Work verfügbar sind, hängt von der Workspace-Konfiguration und dem Rollout ab.

- Für Dateizugriff, Computernutzung, Browser und verbundene Apps gelten unterschiedliche Berechtigungen und Genehmigungen.

- Wenn in einem Browser oder einer Anwendung bereits eine Anmeldung bei einem Unternehmenssystem besteht, können darüber die Berechtigungen dieses Kontos zugänglich werden.

- Unterstützte Richtlinien für verwaltete Geräte können lokale Funktionen einschränken, ohne die Zugriffskontrollen des Workspace zu ersetzen.

- Daten aus Business-, Enterprise- und Edu-Workspaces, die von den abgedeckten OpenAI-Diensten verarbeitet werden, werden bei der Übertragung und im Ruhezustand verschlüsselt und standardmäßig nicht zum Training von OpenAI-Modellen verwendet.

- Für lokale Dateien, Aufgabenkontext, Browserdaten, Datensätze in verbundenen Systemen und Audit-Ereignisse können unterschiedliche Regeln zur Speicherung und Aufbewahrung gelten.

## Wo lokale Aufgaben ausgeführt werden

Work Lokal greift über die Desktop-App auf dem Computer der nutzenden Person auf genehmigte Ressourcen zu. Work Cloud läuft auf einer von OpenAI verwalteten Infrastruktur, auch wenn es über dieselbe Desktop-App geöffnet wird.

Lokale Dateien können auf dem Gerät bleiben. Relevante Dateiauszüge, Prompts, Screenshots, Browserinhalte oder Tool-Ergebnisse können jedoch an OpenAI-Dienste gesendet werden, um eine Aufgabe zu erledigen. Lokale Ausführung bedeutet nicht, dass die Modellinferenz offline oder ausschließlich auf dem Gerät stattfindet.

## Dateien und Gerätezugriff

Eine lokale Aufgabe kann mit Informationen arbeiten, die Nutzende bereitstellen oder zugänglich machen. Dazu gehören unterstützte Dateien, Anwendungsinhalte, Browsersitzungen und autorisierte verbundene Systeme. Der Zugriff hängt von den bestehenden Rechten der jeweiligen Person und den Kontrollen für die betreffende Funktion ab.

Die Gewährung von lokalem Work-Zugriff genehmigt nicht automatisch jede Anwendung, erteilt keine Administratorrechte und umgeht nicht die Berechtigungen des Kontos, über das auf ein anderes System zugegriffen wird. Eine genehmigte gemeinsame Verbindung kann andere Rechte haben als das persönliche Konto der nutzenden Person.

## Computernutzung und Genehmigungen für Anwendungen

Die [Computernutzung](/de-DE/codex/computer-use) kann nur dann mit unterstützten Desktop-Anwendungen interagieren, wenn die Funktion verfügbar ist, die erforderlichen Betriebssystemberechtigungen erteilt wurden und die nutzende Person die Anwendung autorisiert. Je nach verfügbaren Optionen kann die Genehmigung für die aktuelle Sitzung oder für künftige Aufgaben gelten.

Unter macOS kann die Computernutzung mit der Berechtigung „Bildschirmaufnahme“ Anwendungsinhalte sehen und mit der Berechtigung „Bedienungshilfen“ klicken, tippen und navigieren. Unterstützte macOS-Aufgaben können im Hintergrund ausgeführt werden. Unter Windows arbeitet die Computernutzung auf dem aktiven, sichtbaren Desktop und kann nicht im Hintergrund laufen, während die nutzende Person in derselben Sitzung weiterarbeitet.

Nutzende können eine Aufgabe jederzeit stoppen. Die Computernutzung kann keine Sicherheitsabfragen des Betriebssystems bestätigen, keine Authentifizierung mit Administratorrechten durchführen und weder Terminalanwendungen noch ChatGPT selbst automatisieren.

### Gesperrte Geräte

In unterstützten macOS-Konfigurationen lässt sich optional erlauben, dass eine genehmigte Aufgabe mit Computernutzung weiterläuft, während der Mac gesperrt ist. Die Verfügbarkeit hängt von der App-Version, dem Funktions-Rollout, den geltenden Anforderungen und davon ab, ob die Voraussetzungen für die Fernsteuerung erfüllt sind.

Die Administration kann den Betrieb bei gesperrtem Gerät über eine unterstützte verwaltete Konfiguration deaktivieren. Die Computernutzung unter Windows erfordert einen aktiven, entsperrten Desktop. Aus der Nutzung bei gesperrtem Mac lässt sich keine entsprechende Unterstützung unter Windows ableiten.

## Browsersitzungen und bestehende Anmeldungen

Work Lokal erhält nicht automatisch Zugriff auf jeden Browser oder jedes Unternehmenskonto. Der Zugriff hängt vom verwendeten Browser, dem angemeldeten Konto und den Genehmigungen ab, die für die jeweilige Art des Browserzugriffs erforderlich sind.

| Art des Browserzugriffs                                | Sitzung und Sicherheitsgrenze                                                                                                                                                                                                 |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [In-App-Browser der Desktop-App](/de-DE/codex/browser)    | Verwendet ein Browserprofil, das vom regulären Browser der nutzenden Person getrennt ist. Nutzende können sich in diesem Profil anmelden. Der Zugriff auf unterstützte Websites kann eine Genehmigung erfordern. Der integrierte Browser kann Datei-Uploads nicht automatisieren.              |
| [Chrome-Erweiterung](/de-DE/codex/chrome-extension) | Kann mit bestehenden Browsertabs und Konten interagieren, wenn die Erweiterung und der Websitezugriff genehmigt sind. Nutzende können eine Website einmalig genehmigen oder auch den künftigen Zugriff erlauben. Der Zugriff auf den Browserverlauf und lokale Dateien muss gesondert geprüft werden. |
| Browserbedienung per Computernutzung            | Verwendet einen als Desktop-Anwendung genehmigten Browser, einschließlich der darin bereits angemeldeten Konten. Die Betriebssystemberechtigungen, die Genehmigung für die Anwendung und die Berechtigungen des bestehenden Kontos gelten weiterhin.               |

Die Optionen zur Genehmigung von Websites und die Bestätigungen für sensible Aktionen unterscheiden sich je nach Art des Browserzugriffs. Wer alle Websites erlaubt, erhält künftig weniger Genehmigungsabfragen. Nutzende sollten diese Entscheidung daher prüfen, bevor sie die Option aktivieren.

Ein gehosteter Cloud-Browser ist von den lokalen Browsern der nutzenden Person getrennt und übernimmt deren bestehende Anmeldungen nicht automatisch. Unterstützte Cloud-Arbeitsabläufe können eine separate, von der nutzenden Person autorisierte Anmeldung anfordern.

## Apps, Plug-ins und verbundene Konten

Eine verbundene App kann Zugriff auf Informationen oder Aktionen in einem anderen System ermöglichen. Ein Plug-in kann eine App als zugrunde liegendes Tool verwenden. Die Bereitstellung eines Plug-ins aktiviert nicht automatisch die erforderliche App, autorisiert kein Konto und erlaubt nicht jede Aktion.

Die Verfügbarkeit von Plug-ins und Apps hängt vom Tarif und der Konfiguration des Workspace ab. Laut der [Übersicht zu ChatGPT Work](/de-DE/codex/enterprise/chatgpt-work-overview) sind Plug-ins und die zugrunde liegenden Apps in Enterprise- und Edu-Workspaces standardmäßig deaktiviert und in Business-Workspaces standardmäßig aktiviert. Prüfe die tatsächlichen Einstellungen für den betreffenden Workspace und die jeweilige Produktumgebung.

Bevor eine Aufgabe ein verbundenes System verwendet, stelle sicher, dass der Workspace die App und alle erforderlichen Plug-ins erlaubt, die Verbindung autorisiert ist und das verbundene Konto auf die angeforderten Informationen zugreifen oder die gewünschte Aktion ausführen kann. Einstellungen ohne Schreibzugriff, zulässige Aktionen und erforderliche Bestätigungen unterscheiden sich je nach Integration.

Für Plug-ins, die nur auf dem Desktop verfügbar sind, lokale Tools und andere lokal bereitgestellte Funktionen können unterschiedliche Installations- oder Genehmigungsverfahren gelten. Gehe nicht davon aus, dass jedes lokale Tool denselben Genehmigungsprozess durch die Administration durchläuft.

### Persönliche und gemeinsame Verbindungen

Eine persönliche Verbindung nutzt die Berechtigungen der verbundenen Person im Quellsystem. Eine gemeinsame oder einem Agenten gehörende Verbindung nutzt die Berechtigungen des verbundenen Kontos. Diese können über die eigenen Zugriffsrechte der nutzenden Person hinausgehen.

Beschränke gemeinsam genutzte Konten auf die notwendigen Daten und Aktionen sowie auf die Personen, die sie verwenden dürfen. Nutze die unterstützten Möglichkeiten, Aktionen einzuschränken oder Bestätigungen zu verlangen. Datensätze im verbundenen System unterliegen weiterhin dessen Berechtigungen und Aufbewahrungsrichtlinien.

## Administratorzugriff und Richtlinien für verwaltete Geräte

Prüfe die verfügbaren Work-Kontrollen unter **Workspace-Einstellungen** \> **Berechtigungen & Rollen**. Ob lokales und gehostetes Work als getrennte Berechtigungen angezeigt werden, hängt von der Workspace-Konfiguration und dem Rollout ab. Weitere Hinweise findest du in den [FAQ zur Administration von Work](/de-DE/codex/enterprise/work-admin-faq).

Aktiviere nur die Ausführungsumgebungen, die für die jeweilige Person oder Gruppe genehmigt sind, und überprüfe nach Änderungen die tatsächlich wirksamen Zugriffsrechte.

Workspace-Berechtigungen bestimmen, wer Work verwenden kann. Die Administration kann unterstützte Desktop-Funktionen zusätzlich durch verbindliche Vorgaben einschränken, die in `requirements.toml` festgelegt sind. Je nach Bereitstellung können diese Vorgaben über eine vom Workspace verwaltete Konfiguration, eine Konfigurationsdatei auf Systemebene oder unterstützte Tools zur Mobilgeräteverwaltung für macOS bereitgestellt werden.

Verbindliche Vorgaben können von einzelnen Nutzenden nicht außer Kraft gesetzt werden. Verwaltete Standardwerte legen dagegen anfängliche Einstellungen fest, die Nutzende unter Umständen ändern können. Weder verbindliche Vorgaben noch verwaltete Standardwerte ersetzen Workspace-Rollen oder Betriebssystemberechtigungen.

| Verwaltete Einstellung                                       | Sicherheitszweck                                                             |
| ----------------------------------------------------- | ---------------------------------------------------------------------------- |
| `features.computer_use = false`                       | Unterstützte Funktionen der Computernutzung deaktivieren.                                 |
| `allow_appshots = false`                              | Unterstützte Appshot-Aufnahmen verhindern.                                           |
| `features.in_app_browser = false`                     | Den integrierten Browser der Desktop-App deaktivieren.                                  |
| `features.browser_use = false`                        | Unterstützte Browserautomatisierung deaktivieren; andere Arten des Browserzugriffs separat prüfen. |
| `features.apps = false` oder `features.plugins = false` | Unterstützte verbundene Anwendungen oder Plug-ins einschränken.                        |
| `computer_use.allow_locked_computer_use = false`      | Die unterstützte Computernutzung bei gesperrtem Mac verhindern.                        |

Die verfügbaren Einstellungen und Bereitstellungswege hängen vom Client, dem Betriebssystem, dem Workspace und der Bereitstellungskonfiguration ab. Überprüfe die Einschränkungen auf einem repräsentativen verwalteten Gerät. Unterstützte Richtlinieneinstellungen, Konfigurationsbeispiele und Anleitungen zum MDM-Setup findest du unter [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration).

## Lokale Netzwerkverbindungen und private Ressourcen

Eine Aufgabe kann über verschiedene Wege auf Unternehmensinformationen zugreifen, etwa über einen Browser auf dem Gerät, eine genehmigte Desktop-Anwendung oder eine verbundene App. Bestehende Kontrollen für Geräte, Proxys, VPNs, Quellsysteme und Endpunkte können je nach Zugriffsweg unterschiedlich greifen.

Der Zugang zu einem Unternehmens-VPN berechtigt nicht automatisch jedes Tool, jede interne Ressource zu nutzen. Ebenso schränkt ein Work-Browser in der Cloud oder eine Kontrolle für Cloud-Netzwerke nicht pauschal die lokalen Netzwerkverbindungen eines Geräts ein. Prüfe, welche Verbindung, welche Identität, welches Ziel und welche Aktion für den Arbeitsablauf tatsächlich erforderlich sind.

## Datenverarbeitung und Aufbewahrung

Setze auf dem jeweiligen Gerät und im jeweiligen Ablauf die Schutzmaßnahmen deiner Organisation für Endgeräte, Dateizugriffe, Proxys und die Verhinderung von Datenabfluss um. Prüfe, ob diese Maßnahmen verhindern können, dass sensible Informationen vor der Verarbeitung in die Aufgabe gelangen. Audit-Protokolle und Compliance-Exporte unterstützen die Überwachung und Untersuchung, blockieren aber für sich genommen keine Verarbeitung.

Speicherung und Aufbewahrung hängen von der Informationskategorie und dem Speicherort ab.

| Informationskategorie                            | Was du prüfen solltest                                                                                                                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Lokale Aufzeichnungen von Unterhaltungen                      | Wie die Desktop-App lokale Aufzeichnungen speichert, löscht, sichert oder teilt. Gehe nicht davon aus, dass die Aufbewahrungseinstellungen für gehostete Unterhaltungen für jedes lokale Artefakt gelten. |
| Lokale Dateien und generierte Ausgaben               | Speicherung auf dem Gerät, Richtlinien für Endgeräte, von Nutzenden autorisierte Uploads, externe Freigaben und separat gespeicherte Kopien.                                                       |
| Prompts, Dateiauszüge und Anwendungskontext | Inhalte, die einem Modell oder Dienst übermittelt werden, die für den Workspace geltenden Bedingungen und der tatsächliche Datenfluss im Ablauf.                                                           |
| Stimme und Appshots                              | Mikrofoneingaben, Screenshots des Fensters im Vordergrund, zugänglicher Text aus Anwendungen, lokale Speicherung von Sitzungsdaten und alle als Aufgabenkontext gesendeten Inhalte.                          |
| Browserdaten                                    | Das verwendete Browserprofil, bestehende Anmeldungen, der Browserverlauf, Downloads, Genehmigungen für Websites und separat gespeicherte Aufgabeninhalte.                           |
| Datensätze in verbundenen Systemen                        | Berechtigungen und Aufbewahrung im Quellsystem, die Identität des verbundenen Kontos und Informationen, die separat in der Unterhaltung oder an einem anderen Speicherort gespeichert werden.              |
| Compliance- und Aktivitätsprotokolle                 | Die für den Workspace verfügbaren Ereignisse von Work Lokal, die unterstützte Integration und die Aufbewahrungsrichtlinie des empfangenden Systems.                                   |

In unterstützten Business-, Enterprise- und Edu-Workspaces werden Geschäftsdaten, die von den erfassten OpenAI-Diensten verarbeitet werden, bei der Übertragung und im gespeicherten Zustand verschlüsselt. Standardmäßig werden sie nicht zum Trainieren oder Verbessern von OpenAI-Modellen verwendet. Diese Schutzmaßnahmen bedeuten nicht, dass OpenAI jede Datei auf dem Gerät, jede Drittanbieteranwendung, jedes Browserprofil oder jeden Datensatz im Quellsystem kontrolliert.

Wende eine Aufbewahrungsfrist für gehostete Unterhaltungen, temporäre Uploads oder Compliance-Protokolle nur dann auf lokale Aufzeichnungen an, wenn du bestätigt hast, dass sie für die jeweilige Datenkategorie gilt.

## Einblick in Audit- und Compliance-Daten

Welche Berichte verfügbar sind, hängt vom Workspace-Tarif, der verwendeten Produktoberfläche, dem Ereignis, der verbundenen Anwendung und der eingesetzten Konfiguration ab. Prüfe, welche Vorgänge von Work Lokal erfasst werden, bevor du dich bei der Reaktion auf Sicherheitsvorfälle oder bei regulatorischen Prüfungen auf einen Workspace-Export verlässt.

Prüfe, ob die relevanten Systeme die Identität der Aufgabe, unterstützte Prompts und Antworten, Aufrufe verbundener Apps, Browser-Genehmigungen, Aktionen in Anwendungen, lokale Dateiaktivitäten oder Ereignisse auf Endgeräten aufzeichnen. Aufzeichnungen aus Quellsystemen und von Geräten können andere Einblicke bieten als Aufzeichnungen aus dem ChatGPT-Workspace.

OpenAI speichert kein separates, vollständiges Protokoll der Chrome-Aktionen, die über die Erweiterung ausgeführt werden. Gehe nicht davon aus, dass jeder lokale Dateivorgang, jeder Screenshot, jede Browseraktion, jede Genehmigung oder jede externe Aktualisierung in der Compliance API erscheint.

## Beginne mit einer einzelnen genehmigten Aufgabe

Beginne mit einer kleinen Gruppe, die verwaltete Geräte nutzt, und wähle eine einzelne genehmigte Aufgabe aus, etwa den Vergleich ausgewählter Arbeitsmappen mit Finanzdaten. Prüfe den Work-Zugriff jeder Person und stelle nur die Dateien, Anwendungen, Browsersitzungen oder verbundenen Konten bereit, die für die Aufgabe erforderlich sind.

Prüfe, ob genehmigte Aktionen funktionieren, eingeschränkte Aktionen blockiert werden und die verfügbaren Aufzeichnungen deinen Überwachungsanforderungen entsprechen. Lass die Ergebnisse und alle externen Änderungen von einer Person aus der Gruppe prüfen, bevor du den Zugriff ausweitest.

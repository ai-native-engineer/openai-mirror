<!-- source: https://learn.chatgpt.com/de-DE/docs/cyber-safety -->

OpenAI Daybreak unterstützt zugelassene Personen bei autorisierten defensiven Aufgaben in der Cybersicherheit. Daybreak Blue bietet Zugriff auf Flagship-Modelle, die Anfragen in autorisierten defensiven Arbeitsabläufen seltener ablehnen. Daybreak Red bietet separat genehmigten Zugriff auf spezialisierte Cybermodelle für anspruchsvollere Sicherheitsforschung.

Kombiniere dein genehmigtes Modell mit einer kontrollierten Umgebung, klaren Grenzen für genehmigte Systeme und Aktionen, Berechtigungen nach dem Prinzip der geringsten Rechte sowie einer automatischen Überprüfung vor der Ausführung sensibler Aktionen. Verwende das Modell nur mit der genehmigten Identität, im genehmigten Workspace bzw. in der genehmigten API-Organisation und im genehmigten Projekt sowie über die genehmigte Produktoberfläche.

## Wähle das richtige Modell

Nutze für die meisten autorisierten defensiven Aufgaben zunächst **GPT-Daybreak-Blue** . Dieses Modell bietet Zugriff auf erweiterte Funktionen und lehnt Anfragen in defensiven Sicherheitsabläufen seltener ab, unter anderem bei folgenden Aufgaben:

- Erkennung und Triage von Schwachstellen.
- Sicherheitsprüfung von Code und Bedrohungsmodellierung.
- Entwicklung von Erkennungsmechanismen und Reaktion auf Sicherheitsvorfälle.
- Malware-Analyse in einer kontrollierten Umgebung.
- Behebung von Sicherheitsproblemen und Validierung von Patches.

**GPT-Daybreak-Red** ist ein spezialisiertes Cybermodell für separat genehmigte und ausdrücklich autorisierte Arbeitsabläufe, etwa die kontrollierte Reproduktion von Schwachstellen, die Validierung von Proofs of Concept oder Exploits, Penetrationstests, Red Teaming und die Analyse komplexer Systeme. Für routinemäßige Sicherheitsaufgaben ist es nicht die Standardoption. Der Zugriff wird nicht automatisch gewährt und ist nicht auf jeder Produktoberfläche verfügbar.

Ohne eine klare Autorisierung können diese fortgeschrittenen Arbeitsabläufe wie böswillige Aktivitäten wirken. Nutze das genehmigte Modell nur über die genehmigte Produktoberfläche und nur für Systeme, die dir gehören oder zu deren Prüfung du ausdrücklich berechtigt bist. Sorge außerdem für eine angemessene menschliche Aufsicht.

Zum Beispiel:

- **GPT-Daybreak-Blue:** Prüfe das genehmigte Labor-Repository auf Schwachstellen in der Authentifizierung, priorisiere die Befunde anhand der Beleglage und ihrer Auswirkungen und schlage Patches vor, ohne auf externe Systeme zuzugreifen.
- **GPT-Daybreak-Red:** Reproduziere im genehmigten Labor und innerhalb des genehmigten Testzeitfensters die dokumentierte Authentifizierungsschwachstelle, validiere einen minimalen Proof of Concept und beende den Vorgang, bevor du auf Zugangsdaten zugreifst, Persistenz einrichtest oder Änderungen an Produktionssystemen vornimmst.

## Trusted Access for Cyber

Beantrage **Zugriff auf Daybreak** über [Trusted Access for Cyber](https://help.openai.com/en/articles/20001258-trusted-access-for-cyber). Der Zugriff setzt eine entsprechende Genehmigung und Bereitstellung für deine konkrete Identität oder deinen Dienst, deinen ChatGPT-Workspace oder deine API-Organisation und dein Projekt, das autorisierte Angebot und Modell sowie die zulässige Produktoberfläche voraus.

- Einzelpersonen können über den [Antrag auf Trusted Access für Einzelpersonen](https://chatgpt.com/cyber) Zugriff beantragen.
- Organisationen können das [Formular zur Beantragung von Trusted Access für Unternehmen](https://openai.com/form/enterprise-trusted-access-for-cyber/) einreichen und sich mit ihrer OpenAI-Ansprechperson abstimmen.

Auch wenn du einen Antrag einreichst oder die Identitätsprüfung abschließt, ist eine Genehmigung nicht garantiert.

  Wenn du einen Antrag stellst, deine Identität verifizierst oder eine Genehmigung für Daybreak Blue erhältst, bekommst du dadurch keinen Zugriff auf Daybreak Red oder GPT-Daybreak-Red. Das spezialisierte Angebot erfordert eine separate Genehmigung und Bereitstellung.

Verwende für den Unternehmenszugriff den genehmigten Workspace, die genehmigte API-Organisation oder das genehmigte Projekt ausschließlich für autorisierte interne Tätigkeiten deiner Organisation. Weite den Zugriff nicht auf externe Nutzende, Kundschaft außerhalb deiner Organisation, extern angebotene Dienste, darauf aufbauende Produktfunktionen oder Systeme außerhalb des genehmigten Arbeitsumfangs aus. Wenn bei Identität, Workspace, API-Organisation, Projekt, Modell oder Produktoberfläche unklar ist, was genehmigt wurde, unterbrich die Arbeit und kläre dies mit deiner OpenAI-Ansprechperson.

Trusted Access bedeutet nicht automatisch, dass [keine Datenaufbewahrung](/api/docs/guides/your-data#data-retention-controls-for-abuse-monitoring) gilt. Kläre vor Beginn, welche separat genehmigten Einstellungen zur Datenaufbewahrung für die konkrete API-Organisation und den betreffenden Endpunkt gelten.

## Fehlalarme

Auch legitime Cybersicherheitsaktivitäten oder Aktivitäten ohne Bezug zur Cybersicherheit können eine Schutzmaßnahme auslösen. Wenn eine Schutzmaßnahme eine Anfrage blockiert, umleitet oder einschränkt, prüfe den verfügbaren Hinweis im Client und die Anfrageprotokolle. Unter [Häufige Probleme und Fehlerbehebung](https://help.openai.com/en/articles/20001259) erfährst du, welche Angaben du zusammentragen solltest und wie du danach vorgehst. Melde vermutete Codex-Fehlalarme über `/feedback`, sofern diese Option verfügbar ist. Befolge bei Einschränkungen des API-Zugriffs und Einsprüchen die [Hinweise zu API-Cybersicherheitsprüfungen](/api/docs/guides/safety-checks/cybersecurity#appeals).

Für alle Nutzenden gelten weiterhin die [Nutzungsrichtlinien](https://openai.com/policies/usage-policies/) und die [Nutzungsbedingungen](https://openai.com/policies/row-terms-of-use/).

## Konfiguriere den Ablauf deiner Sicherheitsaufgaben

Trusted Access regelt den genehmigten Zugriff auf Modelle. Es konfiguriert jedoch nicht deine Umgebung, setzt keine Grenzen für genehmigte Systeme und Aktionen durch und überprüft keine vorgeschlagenen Aktionen.

- [Verwende die empfohlene Konfiguration](/de-DE/codex/cyber-safety/recommended-configuration) für Isolation, Berechtigungen nach dem Prinzip der geringsten Rechte, klar definierte Grenzen und Schutzvorkehrungen für sensible Aktionen.

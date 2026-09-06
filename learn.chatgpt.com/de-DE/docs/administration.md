<!-- source: https://learn.chatgpt.com/de-DE/docs/administration -->

# Verwaltung

Lege Zugriffsregeln und Richtlinien für ChatGPT, Codex-Entwicklungstools, APIs, Plug-ins und verbundene Systeme fest

Lege Zugriffsregeln und Richtlinien für ChatGPT, Codex-Entwicklungstools, APIs, Plug-ins und verbundene Systeme fest.

Die Verwaltung umfasst sechs zusammenhängende Kontrollbereiche: den Zugriff auf den ChatGPT-Workspace; die lokale Laufzeitrichtlinie für die davon erfassten Funktionen in der ChatGPT-Desktop-App, in Codex CLI und in der IDE-Erweiterung; die Zugangsberechtigung für Codex Cloud; den Zugriff auf die Platform API; die Verfügbarkeit von Plug-ins und Berechtigungen für Konnektoren; die Berechtigungen in verbundenen Systemen. Beginne mit der Identitäts- und Zugriffsverwaltung im Workspace und wende anschließend für jede Bereitstellung die erforderlichen Kontrollen für Laufzeit und Quellsysteme an.

Mehr zur Authentifizierung

Mitglieder, Gruppen, Zugriffstoken und Rolleneinstellungen im ChatGPT-Workspace

Erste Schritte

Beginne mit dem Rollout-Leitfaden und nutze anschließend die Referenzseiten für die einzelnen Kontrollbereiche.

Leitfaden für den administrativen Rollout

Plane den Zugriff, benenne Verantwortliche, konfiguriere die Kontrollen und überprüfe den Rollout.

ChatGPT Work

Lies die Übersicht zu ChatGPT Work und die Referenz zur Verwaltung.

Übersicht zu ChatGPT Work

Informiere dich über die gehostete Ausführung, Netzwerkkontrollen, Grenzen für den Umgang mit Daten und die für Audits einsehbaren Informationen.

Cloud-Sicherheit in ChatGPT Work

Informiere dich über die gehostete Ausführung, verbundene Konten, Zugriffskontrollen, Datenaufbewahrung und die für Audits einsehbaren Informationen.

Lokale Sicherheit in ChatGPT Work

Informiere dich über die lokale Ausführung, den Zugriff auf Geräte und Browser, verwaltete Richtlinien, den Umgang mit Daten und Einschränkungen bei Audits.

FAQ zur Administration von ChatGPT Work

Informiere dich über die Kontrollen für Zugriff, Daten, Governance, Nutzung und den Umgang mit Vorfällen in ChatGPT Work.

ChatGPT Work: Nutzung und Kosten

Informiere dich über gemeinsam genutzte Credits, die Auswirkungen auf die Abrechnung, Ausgabenkontrollen und die Planung der Einführung.

Identität und Authentifizierung

Lege fest, wie sich Personen anmelden, und vergib Zugangsdaten für programmatische Arbeitsabläufe.

Übersicht zur Authentifizierung

Vergleiche Anmeldemethoden, die Speicherung von Zugangsdaten und Kontrollen zur Durchsetzung von Vorgaben.

Workload-Identität

Ermögliche vertrauenswürdigen Workloads, Codex ohne langfristig gültige Zugangsdaten zu nutzen.

Persönliche Zugriffstoken

Erstelle und verwalte Token für den programmatischen Zugriff.

Dienstkonten

Erstelle und verwalte Workspace-Identitäten für automatisierte Arbeitsabläufe.

Workspace-Zugriff, Richtlinien und Modelle

Vergib Zugriff auf den ChatGPT-Workspace und verwalte ihn getrennt von der lokalen Laufzeitrichtlinie, dem Zugriff auf Codex Cloud und dem Zugriff auf die Platform API.

Gruppen und Provisionierung

Verwalte manuell eingerichtete Gruppen und SCIM-Gruppen sowie die Provisionierung und Rollout-Kohorten.

Verwaltung des Lebenszyklus von Nutzerkonten

Richte Zugänge für Mitarbeitende ein, aktualisiere den Gruppenzugriff und widerrufe die Zugangsdaten ausscheidender Personen.

Rollen und Berechtigungen im Workspace

Nutze die maßgebliche Übersicht über die Kontrollen für Workspace, Laufzeit, API, Plug-ins und Quellsysteme.

GPTs und Freigaben

Verwalte in deinem gesamten Workspace die Freigabe und Inhaberschaft von GPTs, verbundene Apps und Aktionen von Drittanbietern.

Verwaltete Konfiguration

Verteile verwaltete Einstellungen, sofern dies unterstützt wird, und setze Laufzeitanforderungen für die erfassten Funktionen in der ChatGPT-Desktop-App, in Codex CLI und in der IDE-Erweiterung durch.

Prisma AIRS

Wende im gesamten Workspace geltende Sicherheitsrichtlinien auf Codex-Prompts an.

HIPAA-Konfiguration

Konfiguriere Schutzmaßnahmen für die lokale Ausführung von Arbeitsabläufen, die möglicherweise geschützte Gesundheitsinformationen verarbeiten.

Verfügbarkeit von Modellen im Workspace

Verwalte den Zugriff auf Modelle für ChatGPT, Codex in der ChatGPT-Desktop-App, Codex CLI, die IDE-Erweiterung, Codex Cloud und die Platform API jeweils getrennt.

Kontrollen für Plug-ins und Konnektoren

Steuere die Installation von Plug-ins, mitgelieferte Skills, über Konnektoren bereitgestellte Funktionen und den Zugriff auf verbundene Dienste.

Kontrollen für Plug-ins

Verwalte die Verfügbarkeit von Plug-ins, den Zugriff auf Konnektoren, deren Aktionen sowie die Berechtigungen in Quellsystemen.

Plug-in-Verwaltung

Importiere Workspace-Plug-ins aus GitHub und synchronisiere sie mit GitHub.

Kontrollen für Skills

Vergleiche die Kontrollen für Skills im ChatGPT-Workspace, im lokalen Dateisystem und in Plug-ins.

Nutzung, Governance und Compliance

Ermittle den Nutzungsgrad und leite Berichts- oder Auditdaten an das jeweils dafür zuständige System weiter.

Governance

Wähle für jede Fragestellung den passenden Bereich für Analysen, Ausgaben und Audits.

Admin-Plug-in

Nutze das Admin-Plug-in für Berechtigungen, Genehmigungen und unterstützte administrative Arbeitsabläufe.

Workspace-Analysen

Verschaffe dir einen Überblick über die Verbreitung von ChatGPT und die Nutzung von Codex in deinem Workspace.

Analyse-API

Automatisiere mit der Codex Analyse-API die Berichterstattung über Entwicklungsaktivitäten und Code Reviews.

Compliance API und Audit-Ereignisse

Exportiere Aktivitätsprotokolle für Audit- und Untersuchungsprozesse.

Bereitstellung und Modellanbieter

Stelle Desktop-Apps bereit und aktualisiere sie, verbinde verwaltete Hosts oder konfiguriere einen unterstützten externen Modellanbieter.

App-Updates verwalten

Steuere Updates für Desktop-Apps und stelle freigegebene Versionen über deine Plattform zur Geräteverwaltung bereit.

Bereitstellung der Windows-App

Wähle ein Installations- und Updateverfahren für verwaltete Windows-Geräte.

Remote-Verbindungen

Starte und steuere die Arbeit auf verbundenen Computern.

Amazon Bedrock

Konfiguriere unterstützte lokale Clients so, dass sie die über Bedrock verfügbaren Modelle nutzen.

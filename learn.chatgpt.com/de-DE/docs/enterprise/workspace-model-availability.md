<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/workspace-model-availability -->

Welche Modelle einer Person zur Verfügung stehen, hängt von der verwendeten Produktoberfläche und ihrer Anmeldemethode ab. Eine Modelleinstellung in deinem ChatGPT-Workspace gilt nicht automatisch für Codex in der ChatGPT-Desktop-App, Codex CLI, die IDE-Erweiterung, Codex Cloud oder die OpenAI API.

Das vollständige Administrationsmodell findest du unter
[Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions).

## Geltungsbereich des Modellzugriffs ermitteln

| Produkt- oder Authentifizierungsbereich                                                         | Maßgeblich für den Modellzugriff                                                                                  | Aktuelle Quelle                                                                                                                |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| ChatGPT-Workspace                                                                          | Der Workspace-Tarif, der Zugriff der Mitglieder, die Workspace-Einstellungen und die unterstützten Rollenberechtigungen                 | [Modelle und Limits für ChatGPT Enterprise und Edu](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits) |
| Codex in der ChatGPT-Desktop-App, Codex CLI und IDE-Erweiterung mit ChatGPT-Anmeldung        | Vom jeweiligen Client unterstützte Modelle und die für die angemeldete ChatGPT-Identität verfügbaren Zugriffsrechte    | [Codex-Modelle](/de-DE/codex/models) und aktuelle Hinweise zum Workspace                                                                  |
| Codex Cloud                                                                                | Von gehosteten Codex-Arbeitsabläufen unterstützte Modelle und die für die angemeldete ChatGPT-Identität verfügbaren Zugriffsrechte | [Codex-Modelle](/de-DE/codex/models) und [Codex Cloud](/de-DE/codex/cloud)                                                                 |
| Codex in der ChatGPT-Desktop-App, Codex CLI und IDE-Erweiterung mit Authentifizierung per API-Schlüssel | Die dem Schlüssel zugeordnete Organisation und das zugehörige Projekt der OpenAI API                                       | [Authentifizierung](/de-DE/codex/auth) und die [OpenAI API-Plattform](https://platform.openai.com/docs/overview)                        |

Prüfe die aktuelle Quelle für die tatsächlich verwendete Produktoberfläche. Kopiere keinen Modellkatalog und gehe nicht davon aus, dass sich eine Einstellung der ChatGPT-Modellauswahl auf Codex in der ChatGPT-Desktop-App, Codex CLI, die IDE-Erweiterung, Codex Cloud und die API-Plattform gleichermaßen auswirkt.

## Mitarbeitenden einen klaren Einstieg ermöglichen

Überprüfe die [Modelleinstellungen](https://help.openai.com/en/articles/8411955) für deinen
Workspace, bevor du eine Pilotgruppe einlädst. Wer einen Workspace besitzt oder administriert, kann
getrennte Startvorgaben für Chat sowie für Work und Codex festlegen. Wenn
die jeweilige Oberfläche dies unterstützt, wähle für Chat, Work und lokale Codex-Oberflächen ein Startmodell, den Reasoning-Aufwand, die Geschwindigkeit und das Verhalten bei neuen
Chats aus.

Betrachte diese Auswahlmöglichkeiten als Standardeinstellungen, nicht als Berechtigungen. Welche Modelle verfügbar sind, hängt weiterhin vom Lizenzplatz, der Rolle und der Workspace- oder API-Identität des Mitglieds, von verbindlichen Workspace-Vorgaben sowie von der verwendeten Produktoberfläche ab. Startvorgaben gewähren keinen Zugriff auf nicht verfügbare Modelle und setzen diese Anforderungen nicht außer Kraft. In Codex Cloud lässt sich das Standardmodell nicht ändern.

Die Verfügbarkeit des Schnellmodus hängt vom Workspace, der Produktoberfläche und einer gegebenenfalls
verbindlich vorgegebenen Einstellung `features.fast_mode` in
[`requirements.toml`](/de-DE/codex/config-file/config-reference#requirementstoml) ab.
Mit dieser Einstellung lässt sich der Schnellmodus für verwaltete lokale Codex-Clients verbindlich aktivieren oder deaktivieren.
Sie ist keine Startvorgabe und kann die Verfügbarkeit im Workspace oder im Produkt nicht außer Kraft setzen.

## GPT-6 Astra in Enterprise

Während des anfänglichen Rollouts muss deine Organisation Zugriff auf Daybreak haben,
bevor Admins Astra aktivieren können. In ChatGPT Enterprise ist Astra
in den ersten zwei Wochen nach der Einführung standardmäßig deaktiviert. Admins können in berechtigten
Workspaces Astra für einzelne Personen oder Gruppen
in Chat, Work und Codex aktivieren. Die bestehenden Voraussetzungen für die Produktnutzung gelten weiterhin. Prüfe die
[Modelleinstellungen deines Workspaces](https://help.openai.com/en/articles/8411955) und
bestätige die Verfügbarkeit auf jedem Client, den deine Pilotgruppe verwendet.

Den Zugriff zu aktivieren und ein Startmodell auszuwählen, sind zwei getrennte Entscheidungen. Prüfe den
jeweiligen Lizenzplatz, die Rolle und die Abrechnungsvereinbarung, bevor du Astra als Standard festlegst.
Hinweise zu Nutzungskontingenten und Abrechnung findest du unter [Preise](/de-DE/codex/pricing).
Unter [Sicherheitsüberwachung](/de-DE/codex/agent-approvals-security#safety-monitoring-and-paused-tasks) findest du Informationen zu Aufgaben,
die zur Überprüfung pausiert werden.

Bei der Anmeldung mit einem API-Schlüssel richtet sich der Zugriff auf Astra nach der API-Organisation und dem Projekt, die dem Schlüssel zugeordnet sind. Die Aktivierung von Astra in einem ChatGPT-Workspace gewährt keinen API-Zugriff. Für den frühzeitigen Zugriff mit einem API-Schlüssel muss außerdem der Client konfiguriert werden. Bitte dein OpenAI-Account-Team um eine Setup-Anleitung. Allein die Auswahl eines Modells oder eine Änderung der lokalen Konfiguration gewährt keinen Zugriff.

## Auf das Auslaufen von GPT-5.4 vorbereiten

Ab dem 31. August 2026 stehen GPT-5.4 und GPT-5.4 mini in Codex bei einer Anmeldung mit ChatGPT nicht mehr zur Verfügung. Aktualisiere bis dahin betroffene Workspace-Standardeinstellungen, gespeicherte Modelleinstellungen, verwaltete Konfigurationen, benutzerdefinierte Agenten und geplante Aufgaben:

- Ersetze `gpt-5.4` durch `gpt-5.6-terra` (GPT-5.6 Terra).
- Ersetze `gpt-5.4-mini` durch `gpt-5.6-luna` (GPT-5.6 Luna).

Die OpenAI API ist nicht betroffen. Das gilt auch für Codex, wenn du deinen eigenen API-Schlüssel zur Authentifizierung verwendest.
Unter [Codex-Modelle](/de-DE/codex/models#deprecated-codex-models) und
[Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration)
findest du Details zur Migration.

## Modellzugriff von Laufzeitberechtigungen trennen

Der Modellzugriff bestimmt, ob ein Modell für die authentifizierte Person auf einer unterstützten Produktoberfläche verfügbar ist. Lokale Berechtigungsprofile und verwaltete Vorgaben legen fest, was ein Agent nach dem Start einer lokalen Ausführung tun darf, etwa welche Dateien er ändern oder welche Netzwerkziele er erreichen kann.

Ein Berechtigungsprofil kann keinen Modellzugriff gewähren. Der Modellzugriff kann auch die Sandbox, die Genehmigungsrichtlinie, die Netzwerkkontrollen oder die für eine Ausführung geltenden Berechtigungen des Quellsystems nicht abschwächen.

## Probleme beim Modellzugriff beheben

Wenn eine Person ein erwartetes Modell nicht auswählen kann:

- Prüfe die Produktoberfläche und die Anmeldemethode.
- Prüfe den ChatGPT-Workspace oder die Organisation und das Projekt auf der API-Plattform.
- Überprüfe die aktuellen Zugriffskontrollen für diesen Authentifizierungsbereich.
- Prüfe, ob der ausgewählte lokale Client oder Codex Cloud das Modell unterstützt.

## Aktuelle Quellen

- [Modelle und Limits für ChatGPT Enterprise und Edu](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits)
- [Workspace-Einstellungen verwalten](https://help.openai.com/en/articles/8411955)
- [Rollenbasierte Zugriffskontrolle](https://help.openai.com/en/articles/11750701-rbac)
- [Codex-Modelle](/de-DE/codex/models)
- [Verfügbarkeit von Codex-Funktionen nach Tarif](/de-DE/codex/pricing#feature-availability)
- [Authentifizierung](/de-DE/codex/auth)

## Weiterführende Dokumentation

- [Leitfaden für den administrativen Rollout](/de-DE/codex/enterprise/admin-setup)
- [Gruppen und Provisionierung](/de-DE/codex/enterprise/groups-and-provisioning)
- [Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions)
- [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration)

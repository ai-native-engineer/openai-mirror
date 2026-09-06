<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/roles-and-workspace-permissions -->

Verschiedene Einstellungen regeln unterschiedliche Bereiche der ChatGPT-Nutzung in deiner Organisation. Der Zugriff auf einen Bereich gewährt nicht automatisch Zugriff auf einen anderen. Auf dieser Seite erfährst du, wie die sechs Kontrollbereiche zusammenwirken. Folge anschließend den verlinkten Anleitungen für die aktuellen Setup-Schritte.

In den Workspace-Einstellungen bündelt **Codex und Work Lokal** den lokalen Zugriff auf Codex und Work
unter **Mitgliedern die lokale Nutzung von Codex und Work erlauben**. Andere Workspaces
führen **Codex Lokal** und **Work Lokal** als getrennte Bereiche. Dort
gewährt **Mitgliedern die lokale Nutzung von Codex erlauben** lokalen Zugriff auf Codex und
**Work lokal nutzen** lokalen Zugriff auf Work. Wird eine der beiden Berechtigungen aktiviert,
gilt die andere dadurch nicht automatisch als erteilt. Diese Bezeichnungen stehen für Workspace-Berechtigungen, nicht für separate
Produkte oder Clients. Token-Berechtigungen und Höchstgrenzen für die Gültigkeitsdauer von Anmeldedaten findest du
je nach Workspace entweder im Bereich **Zugriffstoken** oder im Bereich für den lokalen Zugriff.
Die verwaltete Konfiguration bildet eine separate Ebene. Sie schränkt das unterstützte
Laufzeitverhalten der erfassten Funktionen in diesen Clients ein. Funktionen
und tatsächlich geltende Anforderungen können sich je nach Client und Version unterscheiden.

## Kontrollbereiche verstehen

| Bereich          | Was damit gesteuert wird                                                                                                                                                                                      | Was damit nicht gesteuert wird                                                                          | Aktuelle Quelle                                                                                                                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ChatGPT-Workspace | Mitgliedschaft, Nutzerplätze, vordefinierte Administrationsrollen und rollenbasierter Zugriff auf unterstützte Workspace-Funktionen                                                                                               | Berechtigungen für lokale Agenten, Zugriff auf Organisationen der Plattform-API oder Berechtigungen in einem verbundenen Dienst | [Zugriff auf den ChatGPT-Workspace](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise) und [RBAC](https://help.openai.com/en/articles/11750701-rbac) |
| Lokale Clients     | Laufzeitverhalten der erfassten Funktionen in der ChatGPT-Desktop-App, in Codex CLI und in der IDE-Erweiterung, darunter Genehmigungen, Dateisystem- und Netzwerkzugriff, Berechtigungsprofile und zulässige Integrationen | Ein ChatGPT-Nutzerplatz, die Berechtigung zur Nutzung einer Funktion oder eines Modells oder der Zugriff auf externe Daten                         | [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration) und [Berechtigungen](/de-DE/codex/permissions)                                                                                                   |
| Codex Cloud       | Berechtigung zur Nutzung gehosteter Codex-Arbeitsabläufe und der für die jeweilige Person bereitgestellten Cloud-Umgebungen                                                                                                       | Richtlinie für die lokale Laufzeit oder Repository-Berechtigungen, die ein Quellsystem erteilt                    | [Cloud-Umgebungen](/de-DE/codex/environments/cloud-environment)                                                                                                                                              |
| Plattform-API      | Mitgliedschaft in Organisationen und Projekten, API-Schlüssel, Modellzugriff, Nutzung und Abrechnung für per API authentifizierte Vorgänge                                                                                            | Mitgliedschaft im ChatGPT-Workspace, Zugriff auf lokale Clients oder auf Codex Cloud                         | [OpenAI API-Plattform](https://platform.openai.com/docs/overview)                                                                                                                                         |
| Plug-ins           | Verfügbarkeit und Installation von Plug-ins, enthaltene Skills, Zugriff auf Konnektoren und unterstützte Konnektoraktionen                                                                                               | Autorisierung im verbundenen Dienst oder weitergehende Laufzeitberechtigungen für lokale Umgebungen und die Cloud            | [Kontrollen für Plug-ins](/de-DE/codex/enterprise/apps-and-connectors)                                                                                                                                                 |
| Verbundene Systeme | Auf welche Repositorys, Dateien und Nachrichten das authentifizierte Konto im Quellsystem zugreifen und welche Aktionen es ausführen kann                                                                                            | Berechtigung für den ChatGPT-Workspace, Plug-ins, Codex Cloud oder die Plattform-API                              | Verwaltung und Zugriffskontrollen des verbundenen Dienstes                                                                                                                                               |

Eine Anfrage muss die Kontrollen aller für sie geltenden Bereiche bestehen. Beispielsweise kann der Zugriff auf einen Workspace ein Plug-in verfügbar machen. Der verbundene Dienst entscheidet jedoch weiterhin, welche Daten das angemeldete Konto lesen darf. Ein lokales Berechtigungsprofil kann eine Ausführung in einem unterstützten lokalen Client einschränken, aber weder eine Workspace-Funktion noch ein Modell freischalten.

## Workspace-Zugriff zuweisen

Die Verwaltung des ChatGPT-Workspaces trennt den Produktzugriff von administrativen Befugnissen.

### Unterschied zwischen Nutzerplatz, Admin-Rolle und benutzerdefinierter Rolle verstehen

Ein Nutzerplatz bestimmt, auf welche Produktbereiche ein Mitglied zugreifen kann. Je nach Workspace-Tarif können ChatGPT- und Codex-Nutzerplätze verfügbar sein.

Vordefinierte Workspace-Rollen legen die administrativen Befugnisse fest. Die Rolle **Inhaber** 
verwaltet Einstellungen für den gesamten Workspace. Die Rolle **Admin** verwaltet unterstützte Vorgänge
und Gruppen. Die Rolle **Mitglied** hat keine administrativen Rechte und die Rolle
**Analysebetrachter** kann auf Workspace-Analysen zugreifen.

Benutzerdefinierte Rollen legen fest, welche unterstützten Funktionen ein Mitglied nutzen kann. Sie ersetzen nicht die Voraussetzungen für Nutzerplatz oder Tarif, erteilen keine Berechtigungen in einem verbundenen System und ändern keine Anforderungen an die lokale Laufzeit.

<div class="not-prose my-4 aspect-video overflow-hidden rounded-md bg-gray-900">
  <iframe
    src="https://player.vimeo.com/video/1215495812"
    title="Anleitung zur rollenbasierten Zugriffskontrolle"
    loading="lazy"
    allow="autoplay; fullscreen; picture-in-picture"
    allowFullScreen
    referrerPolicy="strict-origin-when-cross-origin"
    class="h-full w-full border-0"
  ></iframe>
</div>

### Workspace-Standard festlegen und anschließend gezielt benutzerdefinierte Rollen erstellen

Nur Personen mit der Rolle „Inhaber“ im Workspace können die rollenbasierte Zugriffskontrolle (RBAC) konfigurieren und benutzerdefinierte Rollen erstellen. Die Workspace-Einstellungen legen die Ausgangswerte für die unterstützten Berechtigungen fest. Personen mit dieser Rolle können benutzerdefinierte Rollen über Gruppen oder, soweit unterstützt, direkt einzelnen Mitgliedern zuweisen. Gruppen lassen sich manuell verwalten oder per SCIM synchronisieren. Ein Mitglied kann mehrere benutzerdefinierte Rollen erhalten.

Bei den entsprechenden Berechtigungen übernimmt **Standard** die Workspace-Einstellung, **Ein**
gewährt Zugriff und **Aus** verweigert ihn ausdrücklich. Ist in einer der geltenden Rollen ausdrücklich **Aus** festgelegt,
wird der Zugriff auch dann blockiert, wenn eine andere Rolle ihn gewährt. Welche
Berechtigungszustände verfügbar sind, kann je nach Funktion unterschiedlich sein.

### Berechtigungen für Work Lokal und Work Cloud prüfen

Wenn dein Workspace **Work Lokal** und **Work Cloud** anbietet, prüfe sowohl den
Workspace-Standard als auch jede geltende benutzerdefinierte Rolle. Work ist nur für
berechtigte Workspaces verfügbar. Welche Einstellungen verfügbar sind, kann sich je nach Tarif,
Workspace-Konfiguration und Rollout unterscheiden. Eine Rolle kann den Zugriff, den der Nutzerplatz
eines Mitglieds erlaubt, nicht erweitern.

**Work Cloud** regelt unterstützte Aufgaben mit ChatGPT Work in der Cloud. Wenn die
Einstellungen unabhängig voneinander sind, ermöglicht **Work Lokal** ohne **Work Cloud** die lokale
Arbeit in der ChatGPT-Desktop-App, erlaubt Mitgliedern jedoch nicht, Cloud-Aufgaben zu starten.
Der lokale Zugriff auf Codex wird über **Mitgliedern die lokale Nutzung von Codex erlauben** im Bereich **Codex
Lokal** gesteuert. Änderungen an **Work lokal nutzen** ändern weder den lokalen Zugriff auf Codex noch
ersetzen sie die Anforderungen an die lokale Laufzeit.

Manche Workspaces zeigen stattdessen den gemeinsamen Bereich **Codex und Work Lokal** . In
dieser Ansicht steuert **Mitgliedern die lokale Nutzung von Codex und Work erlauben** den Zugriff auf beide
Produkte.

Aktuelle Informationen zu den Nutzungsvoraussetzungen und Einstellungen findest du unter
[ChatGPT Work und Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

Da sich verfügbare Nutzerplätze, Rollen und Berechtigungen durch Produkt- und Tarifupdates ändern, findest du im Hilfecenter die aktuelle Liste der Berechtigungen und die Anleitung zum Einrichten:

- [Mitglieder, Nutzerplatztypen, Rollen und Zugriff verwalten](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [Rollenbasierte Zugriffskontrolle konfigurieren](https://help.openai.com/en/articles/11750701-rbac)
- [Gruppen verwalten](https://help.openai.com/en/articles/9083985-group-permissions-in-gpts)

### Zugriff auf den Verlauf der Computernutzung steuern

Der [Verlauf der Computernutzung](/de-DE/codex/customization/computer-history) ist in
Business- und Enterprise-Workspaces standardmäßig deaktiviert. Mitglieder können ihn erst aktivieren, wenn eine Person mit der Rolle „Inhaber“ im Workspace
ihnen den Zugriff ausdrücklich gewährt. Personen mit dieser Rolle in Enterprise-Workspaces können den Zugriff
rollenbasiert erteilen:

1. Öffne [**Workspace-Einstellungen \> Berechtigungen & Rollen**](https://chatgpt.com/admin/settings).
2. Suche nach **Verlauf der Computernutzung** und wähle die Workspace-Rolle aus, die
   Zugriff erhalten soll.
3. Schalte für diese Rolle **Verlauf der Computernutzung aktivieren** ein.

Diese Berechtigung erlaubt den Mitgliedern, denen sie zugewiesen ist, lediglich, den Verlauf der Computernutzung zu aktivieren. Sie aktiviert die Funktion nicht für sie. Jedes Mitglied muss die Funktion in der ChatGPT-Desktop-App unter macOS selbst aktivieren und kann auswählen, welche Apps und Websites berücksichtigt werden. Mitglieder ohne die erforderliche Workspace-Berechtigung können die Funktion nicht über lokale Einstellungen aktivieren.

## Richtlinie für die lokale Laufzeit anwenden

Die Richtlinie für die lokale Laufzeit beschränkt die erfassten Funktionen in der ChatGPT-Desktop-App, in Codex CLI und in der IDE-Erweiterung. In der Cloud verwaltete Anforderungen setzen zusätzlich eine unterstützte ChatGPT-Anmeldung und eine entsprechende Tarifberechtigung voraus. Berechtigungsprofile und verwaltete Anforderungen können Befehle, Dateisystemzugriff, Netzwerkzugriff, Genehmigungen und anderes lokales Laufzeitverhalten einschränken. Sie ändern weder den Nutzerplatz noch die Workspace-Rolle einer Person und auch nicht deren Berechtigung zur Modellnutzung oder ihre Berechtigungen in einem externen System.

Nutzende können ein vordefiniertes oder benutzerdefiniertes Berechtigungsprofil auswählen, wenn die lokale Richtlinie
dies zulässt. Personen mit Administratorrechten können Standardwerte und Anforderungen über die
unterstützten Kanäle für die verwaltete Konfiguration verteilen. Unter [Berechtigungen](/de-DE/codex/permissions)
erfährst du mehr über das Verhalten der Profile. [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration)
beschreibt Anforderungen, Bereitstellung und Rangfolge.

## Weiterführende Dokumentation

- [Leitfaden für den administrativen Rollout](/de-DE/codex/enterprise/admin-setup)
- [Gruppen und Provisionierung](/de-DE/codex/enterprise/groups-and-provisioning)
- [Verwaltung des Lebenszyklus von Nutzerkonten](/de-DE/codex/enterprise/user-lifecycle)
- [Verfügbarkeit von Modellen im Workspace](/de-DE/codex/enterprise/workspace-model-availability)
- [Zugriffstoken](/de-DE/codex/enterprise/access-tokens)
- [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration)
- [Authentifizierung](/de-DE/codex/auth)

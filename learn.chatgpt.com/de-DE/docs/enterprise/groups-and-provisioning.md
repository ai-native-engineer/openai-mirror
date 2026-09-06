<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/groups-and-provisioning -->

Gruppen fassen Personen in einem ChatGPT-Workspace zusammen und können benutzerdefinierte Rollen erhalten.
Eine Gruppenzugehörigkeit ersetzt nicht die Zuweisung von Lizenzplätzen, gewährt allein keine Berechtigungen
für Workspace-Funktionen, setzt keine lokalen Laufzeitrichtlinien außer Kraft und ermöglicht keinen Zugriff
auf die Platform API oder verbundene Systeme.

Das vollständige Modell zur Zugriffssteuerung findest du unter
[Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions).

## Quellen der Gruppenzugehörigkeit vergleichen

Nutze Gruppen für Personen mit denselben Zugriffsanforderungen, beispielsweise für eine Pilotgruppe,
Personen, die den Workspace betreiben, oder Mitglieder, die dieselbe unterstützte Funktion benötigen.

### Eine Gruppe für gemeinsame Zugriffsanforderungen erstellen

Personen mit Inhaber- oder Administrationsrechten im Workspace können Gruppen erstellen und verwalten. Erstelle eine manuell
verwaltete Gruppe für einen kleinen oder vorübergehenden Personenkreis. Soll sich die Gruppenzugehörigkeit nach deinem Verzeichnis richten,
synchronisiere eine bestehende Gruppe deines Identitätsanbieters.

Jede Gruppe hat genau eine maßgebliche Quelle der Gruppenzugehörigkeit:

| Gruppentyp                | Quelle der Gruppenzugehörigkeit                   | Wann der Gruppentyp geeignet ist                                                                  |
| ------------------------- | ----------------------------------- | -------------------------------------------------------------------------------- |
| Manuell verwaltet          | Verwaltung des ChatGPT-Workspace    | Die Gruppe ist klein, besteht nur vorübergehend oder wird nicht über die Verzeichnissynchronisierung verwaltet             |
| Vom Identitätsanbieter verwaltet | Dein Identitätsanbieter über SCIM | Die Gruppenzugehörigkeit soll sich nach dem Verzeichnis der Organisation und ihrem Verfahren zum Entfernen von Mitgliedern richten |

Manuell verwaltete und vom Identitätsanbieter verwaltete Gruppen können nebeneinander bestehen. Bei synchronisierten
Gruppen ist der Identitätsanbieter die Quelle der Gruppenzugehörigkeit. Spätere Aktualisierungen durch die Provisionierung
können Änderungen im Workspace überschreiben. Das Hilfecenter ist die maßgebliche Quelle für das aktuelle Verhalten von SCIM,
unterstützte Attribute und Setup-Schritte.

## Grenzen des Zugriffs verstehen

Die Gruppenzugehörigkeit allein gewährt keine Berechtigung für eine Workspace-Funktion.

### Eine Gruppe mit den passenden Berechtigungen verknüpfen

Personen mit Inhaberrechten für einen Workspace können benutzerdefinierte Rollen Gruppen oder, sofern verfügbar,
direkt einzelnen Mitgliedern zuweisen. Prüfe alle geltenden Rollen: Ist eine Berechtigung in einer beliebigen Rolle ausdrücklich auf **Aus** gesetzt,
wird sie verweigert, selbst wenn eine andere Rolle sie gewährt. Der Lizenztyp
und die Produktberechtigung des Mitglieds bleiben maßgeblich.

SCIM provisioniert Workspace-Mitgliedschaften und Gruppenzuweisungen. Es gewährt keine
Berechtigungen in GitHub, Google Drive, Slack oder anderen verbundenen Systemen. Es ersetzt außerdem
weder lokale Laufzeitanforderungen noch den Zugriff auf Organisationen in der Platform API.

Workspace-RBAC und lokale Laufzeitanforderungen sind getrennte Steuerungssysteme.
Eine Gruppe kann für beide relevant sein. Leite aus der Reihenfolge der Workspace-Gruppen jedoch keine Regeln für die Zuordnung
oder den Vorrang verwalteter Anforderungen ab. Unter
[Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration) findest du die
dokumentierten Regeln zur Bereitstellung und zum lokalen Vorrang.

## Aktuelle Setup-Anleitungen verwenden

Details zur Verwaltung des Workspace können sich ändern. Nutze diese Quellen für aktuelle Schritte in der
Benutzeroberfläche sowie Informationen zur Verfügbarkeit und zu Beschränkungen:

- [Mitglieder, Lizenztypen, Rollen und Zugriff verwalten](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [Gruppen verwalten](https://help.openai.com/en/articles/9083985-group-permissions-in-gpts)
- [Häufige Fragen zur SCIM-Integration](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
- [Workspace-Einstellungen verwalten](https://help.openai.com/en/articles/8411955)

### Eintritte, Wechsel und Austritte überprüfen

- **Eintritte:** Stelle sicher, dass das Mitglied eine gegebenenfalls noch offene Einladung zum Workspace annimmt und
  den vorgesehenen Lizenzplatz, die vorgesehenen Gruppenzugehörigkeiten und Berechtigungen sowie die unterstützten
  Funktionen erhält.
- **Wechsel:** Aktualisiere die maßgebliche Quelle der Gruppenzugehörigkeit und prüfe die
  effektiven Berechtigungen des Mitglieds unter Berücksichtigung aller geltenden Rollen.
- **Austritte:** Entziehe einem über SCIM verwalteten Mitglied über den Identitätsanbieter
  den Zugriff und stelle sicher, dass es nicht mehr auf den Workspace zugreifen kann. Entfernst du
  das Mitglied nur aus dem Workspace, kann eine spätere Synchronisierung den Zugriff
  wiederherstellen.

## Weiterführende Dokumentation

- [Verwaltung des Lebenszyklus von Nutzerkonten](/de-DE/codex/enterprise/user-lifecycle)
- [Authentifizierung](/de-DE/codex/auth)
- [Rollen und Berechtigungen im Workspace](/de-DE/codex/enterprise/roles-and-workspace-permissions)
- [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration)
- [Leitfaden für den administrativen Rollout](/de-DE/codex/enterprise/admin-setup)

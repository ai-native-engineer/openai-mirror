<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/plugin-management -->

## Bevor du beginnst

Mit Adminrechten im Workspace kannst du einen Plug-in-Marketplace aus GitHub importieren und seine Plug-ins über das Repository aktuell halten. Ein Marketplace ist ein JSON-Katalog, der die zu importierenden Plug-ins auflistet.

Verwende ein GitHub-Konto mit Lesezugriff auf das Marketplace-Repository und alle weiteren Repositories, auf die es verweist. Öffentliche und private GitHub-Repositories werden unterstützt. Hole vor dem Import alle Genehmigungen deiner GitHub-Organisation ein, die für den Zugriff auf das Repository erforderlich sind.

Prüfe vor dem Import den Inhalt des Repositorys. Bei neuen Plug-ins ist die Installationsrichtlinie zunächst auf **Verfügbar** gesetzt. Die Authentifizierung erfolgt bei der Installation. Für neue Marketplaces ist die automatische tägliche Synchronisierung aktiviert. Beim Import werden alle gültigen Einträge verarbeitet. Künftige Synchronisierungen fügen alle neuen Plug-ins aus dem Repository automatisch hinzu.

## Synchronisierung eines Marketplaces konfigurieren

1. Öffne **Admin** \> **Plug-ins** und wähle **Hinzufügen** \> **Marketplace importieren** aus.
2. Gib unter **Quelle** die Repository-URL ein, etwa `https://github.com/example/team-plugins`. Verwende nur die URL des Repositorys, keine Branch- oder Ordner-URL.
3. Befindet sich der Marketplace in einem Unterverzeichnis, gib dieses unter **Pfad** an. Verwende zum Beispiel `team-tools` für `team-tools/.agents/plugins/marketplace.json`. Lass **Pfad** leer, um das Stammverzeichnis des Repositorys zu verwenden. Gib nicht den Dateinamen des Manifests ein.
4. Optional kannst du unter **Branch, Tag oder Commit** einen Wert eingeben. Lass das Feld leer, um den Standard-Branch des Repositorys zu verwenden. Verwende einen Branch, um künftige Commits zu erhalten. Bei einem festgelegten Commit bleibt der Stand unverändert.
5. Wähle **Marketplace importieren** aus und autorisiere den Zugriff auf GitHub, wenn du dazu aufgefordert wirst. Der erste Import kann bei sehr großen Marketplaces bis zu einer Stunde dauern. Die anschließenden täglichen Synchronisierungen dauern in der Regel wenige Minuten.
6. Prüfe die **Importergebnisse** und öffne anschließend jedes importierte Plug-in, um seine Installationsrichtlinie und gegebenenfalls erforderliche Apps zu konfigurieren.

Um ein Update anzufordern, ohne auf die tägliche Synchronisierung zu warten, öffne den Marketplace unter **Admin** \> **Plug-ins** \> **Marketplaces** und wähle **Jetzt synchronisieren** aus.

## Unterstützte Formate

Das ausgewählte Verzeichnis muss eine dieser Dateien enthalten:

| Datei                               | Format                                                               |
| ---------------------------------- | -------------------------------------------------------------------- |
| `.agents/plugins/marketplace.json` | Ein Codex-Marketplace mit einem `plugins`-Array.                          |
| `.claude-plugin/marketplace.json`  | Ein Claude-kompatibler Marketplace mit einem `plugins`-Array.              |
| `.claude-plugin/plugin.json`       | Ein eigenständiges Claude-Plug-in, wenn kein Marketplace-Manifest vorhanden ist. |

Einträge in einem Marketplace können auf native Plug-ins mit `.codex-plugin/plugin.json`, Claude-kompatible Plug-ins, Pakete im Format Agent Plugins 1.0 oder unterstützte Skill-Pakete verweisen.

Verwende in einem Codex-Marketplace lokale Pfade für Plug-ins im selben Repository:

```json
{
  "name": "team-plugins",
  "interface": {
    "displayName": "Team plugins"
  },
  "plugins": [
    {
      "name": "team-tools",
      "source": {
        "source": "local",
        "path": "./plugins/team-tools"
      }
    }
  ]
}

Der Pfad ist relativ zum ausgewählten Stammverzeichnis des Marketplaces, nicht zu `.agents/plugins/`.

Ein Claude-kompatibler Marketplace kann für jedes lokale Plug-in einen Pfad als Zeichenfolge verwenden:

```json
{
  "name": "team-plugins",
  "plugins": [
    {
      "name": "team-tools",
      "source": "./plugins/team-tools"
    }
  ]
}

Codex-Marketplace-Einträge unterstützen außerdem `source: "url"` für ein Plug-in im Stammverzeichnis eines GitHub-Repositorys und `source: "git-subdir"` für ein Plug-in in einem GitHub-Unterverzeichnis. Zum Beispiel:

```json
{
  "name": "team-tools",
  "source": {
    "source": "git-subdir",
    "url": "https://github.com/example/team-tools.git",
    "path": "./plugins/team-tools",
    "ref": "main"
  }
}

Bei Git-Quellen lässt sich eine Referenz mit `ref` oder ein vollständiger, 40 Zeichen langer Commit-Hash mit `sha` angeben. Das GitHub-Konto, über das der Zugriff autorisiert wird, muss Lesezugriff auf jedes referenzierte Repository haben. Der Import in den Workspace unterstützt derzeit nur GitHub-Repositories.

## Zugriff im Workspace konfigurieren

Beim Import und bei der Synchronisierung aus GitHub werden keine Installations- oder Authentifizierungsrichtlinien aus dem Repository übernommen, einschließlich `AVAILABLE`, `INSTALLED_BY_DEFAULT`, `NOT_AVAILABLE`, `ON_INSTALL` und `ON_USE`. Personen mit Adminrechten im Workspace konfigurieren diese Einstellungen für jedes Plug-in. Die Workspace-Richtlinien bleiben erhalten, wenn ein Update synchronisiert oder die Verwaltung eines vorhandenen Plug-ins auf GitHub umgestellt wird.

Wähle unter **Installationsrichtlinie** für jede berechtigte Rolle **Verfügbar** oder **Installiert** aus. Erforderliche Apps müssen ebenfalls aktiviert sein, und Mitglieder müssen Zugriff auf den verbundenen Dienst haben. Der Import eines Plug-ins gewährt keinen Zugriff auf Apps und verbindet keine Konten von Mitgliedern. Informationen zu Kontrollen für Rollen, Apps und Aktionen findest du unter [Kontrollen für Plug-ins](/de-DE/codex/enterprise/apps-and-connectors).

## Verwaltung eines vorhandenen Plug-ins auf GitHub umstellen

Füge `pluginId` zum Marketplace-Eintrag des vorhandenen Plug-ins hinzu:

```json
{
  "name": "team-tools",
  "pluginId": "plugin_0123456789abcdef0123456789abcdef",
  "source": {
    "source": "local",
    "path": "./plugins/team-tools"
  }
}

Öffne das Plug-in unter **Admin** \> **Plug-ins** und kopiere aus seiner URL die ID nach `/admin/plugins/`. Füge `pluginId` im Marketplace-Eintrag auf derselben Ebene wie `name` und `source` ein. Das vorhandene Plug-in muss sich im selben Workspace befinden.

Damit stellst du die Verwaltung eines hochgeladenen oder anderweitig nicht verwalteten Workspace-Plug-ins auf GitHub um. Das Plug-in behält seine ID, Freigaben und Workspace-Richtlinien. Künftige Updates kommen aus GitHub. Das verwaltete Plug-in lässt sich nicht mehr durch hochgeladene Archive ersetzen. Ein Plug-in, das bereits über eine andere GitHub-Quelle verwaltet wird, lässt sich auf diese Weise nicht übernehmen.

## Plug-ins nur für den Desktop

Jedes importierte Plug-in, das MCP-Server in `mcp.json` oder `.mcp.json` deklariert, wird als **Nur Desktop** gekennzeichnet und funktioniert nur in der ChatGPT-Desktop-App. Das gilt auch für Server, die eine Remote-HTTPS-URL verwenden. Dieselbe Einschränkung gilt für andere unterstützte Formen der MCP-Konfiguration, etwa inline deklarierte Server.

## Mit `.app.json` auf eine vorhandene App verweisen

Füge `.app.json` im Stammverzeichnis des Plug-ins hinzu. Der Dateiname beginnt mit einem Punkt. `app.json` ohne diesen Punkt wird nicht unterstützt.

```json
{
  "apps": {
    "team-tools": {
      "id": "asdk_app_example",
      "required": true
    }
  }
}

Ersetze `asdk_app_example` durch die ID der vorhandenen App. Unterstützte App-IDs beginnen mit `asdk_app_`, `connector_` oder `templated_apps_`. Verwende die App-ID, keine `plugin_...`-ID. Eine Plug-in-URL mit `plugin_asdk_app_example` steht zum Beispiel für die App `asdk_app_example`.

Der Schlüssel `team-tools` benennt den Verweis innerhalb dieser Datei. Setze `required` auf `true`, wenn das Plug-in von der App abhängt. Du kannst weitere Einträge hinzufügen, um auf andere vorhandene Apps zu verweisen.

Setze bei einem nativen Plug-in in `.codex-plugin/plugin.json` den Wert von `apps` auf `./.app.json`. Hier ist ein vollständiges Manifest für dieses Beispiel:

```json
{
  "name": "team-tools",
  "version": "1.0.0",
  "description": "Use the team's approved tools.",
  "author": {
    "name": "Example team"
  },
  "apps": "./.app.json",
  "interface": {
    "displayName": "Team tools",
    "shortDescription": "Use approved team tools",
    "longDescription": "Connect to the team's existing app.",
    "developerName": "Example team",
    "category": "Productivity",
    "capabilities": ["Read"]
  }
}

Verwende für die Dateien diese Verzeichnisstruktur:

```text
team-plugins/
├── .agents/plugins/marketplace.json
└── plugins/team-tools/
    ├── .codex-plugin/plugin.json
    └── .app.json

Der Verweis erstellt keine App und erteilt keine Berechtigungen. Personen mit Adminrechten müssen die App für die vorgesehenen Rollen verfügbar machen, und Mitglieder müssen eine gegebenenfalls erforderliche Authentifizierung abschließen. Bestehende App-Berechtigungen, Aktionskontrollen und Regelungen für den Dienstzugriff gelten weiterhin.

## Plug-ins aktuell halten

Neue Marketplaces prüfen täglich, ob Updates verfügbar sind. Öffne **Admin** \> **Plug-ins** \> **Marketplaces**, wähle den Marketplace und dann **Jetzt synchronisieren** aus, um ein Update anzufordern, ohne auf die automatische Synchronisierung zu warten.

Die Synchronisierung kann neue Marketplace-Einträge hinzufügen und vorhandene Plug-ins aktualisieren. Prüfe Änderungen am Repository vor dem Merge, denn die automatische Synchronisierung importiert alle neuen Plug-ins.

Prüfe nach einer Synchronisierung den Status und den gespeicherten Bericht. **Abgeschlossen: N Fehler** bedeutet, dass der Durchlauf beendet ist, einige Plug-ins aber nicht verarbeitet werden konnten. Ist ein Update für ein vorhandenes Plug-in ungültig, bleibt die letzte funktionierende Version erhalten. Behebe das gemeldete Problem in GitHub und wähle anschließend **Jetzt synchronisieren** aus, um es erneut zu versuchen.

Wenn du einen Eintrag aus dem Repository entfernst, wird die importierte Kopie im Workspace nicht gelöscht. Sie erhält die Kennzeichnung **Nicht mehr in der Quelle**. Wenn du den Marketplace in ChatGPT löschst, werden alle daraus importierten Plug-ins gelöscht.

## GitHub-Zugriff wiederherstellen oder ändern

Um **den GitHub-Zugriff wiederherzustellen**, prüfe zunächst, ob das für den Import verwendete GitHub-Konto noch Zugriff auf das Repository und alle referenzierten Repositories hat. Anschließend sollte die Person mit Adminrechten, die den Marketplace ursprünglich importiert hat, das GitHub-Plug-in in ChatGPT öffnen und ihr Konto erneut verbinden. Die Marketplace-Synchronisierung verwendet die GitHub-Verbindung dieser Person.

Um **die Zuständigkeit an eine andere Person zu übertragen**, sollte die künftig zuständige Person mit Adminrechten im Workspace **Admin** \> **Plug-ins** \> **Hinzufügen** \> **Marketplace importieren** öffnen und denselben Marketplace mit denselben Werten für **Quelle**, **Pfad** und **Branch, Tag oder Commit** importieren. Künftige Synchronisierungen verwenden die GitHub-Verbindung dieser Person.

Lösche den Marketplace nicht, nur um die Verbindung wiederherzustellen oder die Zuständigkeit zu ändern: Dabei werden auch die daraus importierten Plug-ins entfernt.

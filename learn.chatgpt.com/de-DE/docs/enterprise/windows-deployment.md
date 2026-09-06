<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/windows-deployment -->

Nutzende können die ChatGPT-Desktop-App selbst installieren. Alternativ kann dein IT-Team
sie mit einem Verwaltungstool für Unternehmen bereitstellen. Die App ist vom Store signiert, aber
Nutzende müssen den Microsoft Store weder zur Installation noch zur Aktualisierung öffnen.

## Nutzenden die Installation und Aktualisierung der App ermöglichen

Wenn Nutzende ihre Anwendungen selbst verwalten können, verweise sie auf das
[Web-Installationsprogramm](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi).
Das Installationsprogramm bietet die Standardinstallation sowie automatische
Updates. Bei der Installation oder
bei Updates können Komponenten des Microsoft Store angezeigt werden, aber Nutzende müssen den Store nicht selbst öffnen.

Du kannst die App auch über die Befehlszeile installieren:

```powershell
winget install --id 9PLM9XGG6VKS -s msstore

## App mit einem Verwaltungstool für Unternehmen bereitstellen

Wenn deine Organisation Software zentral verwaltet, verwende Microsoft Intune oder
eine andere kompatible Plattform für die Mobilgeräteverwaltung (MDM) oder für die
Softwarebereitstellung. Wenn deine Plattform die Bereitstellung von Apps aus dem Microsoft Store unterstützt, suche im Ablauf für Store-Apps nach
ChatGPT von OpenAI oder verwende diese Store-Produkt-ID:

```text
9PLM9XGG6VKS

Details zum Setup findest du in der folgenden Microsoft-Dokumentation:

- [Leitfaden zur Bereitstellung in Unternehmen](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDVdo5pE5P3QKg5r0eieSvfAeE7cW0yy58ncBFW7OYajwU?e=dGH94F)
- [Leitfaden zur Bereitstellung mit Intune](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDh_5o31T6XT7bUn5RPldEJAZX58gEuRr8YnJD7d2IMpec?e=nByKw6)
- [Leitfaden zur Bereitstellung mit MECM](https://1drv.ms/b/c/123ec1ed6c72a14a/IQB829f_TSbkR7-H9qA4Q9ntAa9D2He3qMjXksWi2ozdeg8?e=GTKgAl)
- [Microsoft Store-Apps zu Microsoft Intune hinzufügen](https://learn.microsoft.com/en-us/intune/app-management/deployment/add-microsoft-store)

<a id="manage-in-app-updates"></a>

### App-Updates verwalten

Anleitungen zum Setup und Hinweise zum Rollout findest du unter
[App-Updates verwalten](/de-DE/codex/enterprise/manage-app-updates).

## Ohne Microsoft-Dienste zur App-Verteilung installieren

Wenn deine Umgebung Microsoft-Dienste zur App-Verteilung für die
Erstinstallation nicht verwenden kann, lade das vom Store signierte MSIX-Paket für jede
Gerätearchitektur herunter:

| Gerätearchitektur | Paket                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------- |
| x64                 | [ChatGPT-x64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-x64.msix)     |
| Arm64               | [ChatGPT-arm64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-arm64.msix) |

Diese stabilen Links verweisen für jede
Architektur auf das jeweils zuletzt veröffentlichte und vom Store signierte Paket. Lade für Arbeitsabläufe zur Offlinebereitstellung, die eine Lizenzdatei erfordern,
auch die
[Offlinelizenz (`ChatGPT-License.xml`)](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-License.xml) herunter.
Importiere das passende MSIX-Paket und, falls erforderlich, die Lizenzdatei in dein MDM
oder deine Plattform zur Softwarebereitstellung.

Nach der Erstinstallation können Geräte, die
`persistent.oaistatic.com` erreichen, Updates automatisch installieren, sofern die verwaltete
Konfiguration den integrierten Updater der App nicht deaktiviert. Wenn du App-interne
Updates deaktivierst, stelle neuere Pakete über dein MDM oder dein Tool zur Softwarebereitstellung bereit.

Diese Bereitstellungsmethode:

- Ermöglicht die Erstinstallation in eingeschränkten Umgebungen.
- Unterstützt Geräte mit x64 oder Arm64.
- Bietet weder ein eigenständiges MSI-Paket noch eine Store-unabhängige EXE-Datei.

## Weitere Ressourcen

- [App-Updates verwalten](/de-DE/codex/enterprise/manage-app-updates)
- [ChatGPT-Desktop-App für Windows](/de-DE/codex/app/windows)

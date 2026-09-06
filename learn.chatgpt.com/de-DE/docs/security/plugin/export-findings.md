<!-- source: https://learn.chatgpt.com/de-DE/docs/security/plugin/export-findings -->

Verwende einen abgeschlossenen Scan in Codex Security für eine dieser beiden Übergaben:

- Mit der Aktion **Export** erstellst du eine übertragbare JSON-, CSV- oder SARIF-Datei.
- Mit der Aktion **Befunde nachverfolgen** bereitest du ausgewählte Befunde als Linear-, GitHub- oder Jira-Issues
  oder als einen privaten Entwurf für ein GitHub Security Advisory vor. Codex prüft
  auf Duplikate und führt den Schreibvorgang erst nach deiner Genehmigung aus.

Beide Workflows lassen das versiegelte Scan-Paket unverändert.

  Welche Artefaktlinks und Exportformate verfügbar sind, hängt von deiner Codex-Oberfläche und
  der installierten Plug-in-Version ab. Prüfe das [Änderungsprotokoll
  des Plug-ins](/de-DE/codex/security/plugin/changelog), bevor du ein Format für
  Automatisierungen verwendest.

## Übertragbares Artefakt exportieren

Öffne in der Desktop-App unter **Sicherheit** \> **Scans** einen abgeschlossenen Scan. Über die
verfügbaren Artefaktlinks kannst du `report.md`, `findings.json`,
`scan-manifest.json`, `coverage.json` oder, sofern vorhanden, einen SARIF-Bericht einsehen.

Um ein weiteres unterstütztes Format zu erstellen, fordere Codex auf, Befunde aus dem
abgeschlossenen Scan zu exportieren, ohne dessen versiegeltes Scan-Paket zu verändern:

```text
Export the findings from [completed scan directory] as [JSON, CSV, or SARIF]. Do not modify the sealed scan bundle or upload its contents.

Wähle das Format passend zum Ziel aus:

| Format | Verwendung                                                        |
| ------ | ----------------------------------------------------------------- |
| JSON   | Bewahre die versiegelten strukturierten Befunde für Tools und Skripte auf.    |
| CSV    | Prüfe Befunde und den aktuellen lokalen Triage-Status in einer Tabelle.  |
| SARIF  | Sende Befunde an Tools, die das SARIF-Austauschformat unterstützen. |

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Öffne in einem abgeschlossenen Scan die Abdeckung, die Befunde, das Scan-Manifest, den Markdown-Bericht
oder das SARIF-Artefakt.
  </figcaption>
</figure>

Wähle **Markdown-Bericht** aus, um `report.md` in deinem konfigurierten externen
Editor zu öffnen. Welcher Editor verwendet wird, hängt von deinen Systemeinstellungen ab. Das folgende Beispiel zeigt den
Inhalt des generierten Berichts.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Prüfe im generierten Markdown-Bericht den Scan-Umfang, das Bedrohungsmodell, die validierten Befunde und die Links
zu den Detailberichten.
  </figcaption>
</figure>

Verwende den zurückgegebenen Artefaktpfad. Wenn ein anderes Tool den vollständigen Kontext des Scans
benötigt, bewahre die ursprünglichen Dateien `scan-manifest.json`, `findings.json` und
`coverage.json` zusammen auf. Durch den Export werden keine Befunde an einen Dienst
zur Codeanalyse übermittelt.

## Ausgewählte Befunde nachverfolgen

Führe `$codex-security:track-findings` mit einem validierten Befund oder einem
explizit ausgewählten Batch mit bis zu 25 Befunden aus demselben versiegelten Scan aus. Jeder
Durchlauf verwendet einen Anbieter und ein Ziel. Ein privater Entwurf für ein GitHub Security Advisory
darf nur einen Befund enthalten.

Sende Folgendes, um ein Linear-Issue vorzubereiten:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for the Linear team [team] and project [project, if
any]. Check for duplicates and show me the exact issue title, body, metadata,
and destination. Do not create or update anything until I approve that payload.

Sende Folgendes, um ein GitHub-Issue vorzubereiten:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for GitHub repository [owner/repository]. Check open
and closed issues for duplicates and show me the exact issue title, body,
metadata, repository visibility, and authenticated transport. Do not create or
update anything until I approve that payload.

Sende Folgendes, um ein Jira-Issue vorzubereiten:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for Jira project [project key] as [issue type].
Check for duplicates and show me the exact issue summary, description,
metadata, and destination. Do not create or update anything until I approve
that payload.

Für die Nachverfolgung in Jira ist das Atlassian Rovo-Plug-in in Codex erforderlich. Zum Wiederverwenden eines Issues
benötigst du Lesezugriff; zum Erstellen oder Aktualisieren Lese- und Schreibzugriff.

Sende Folgendes, um einen privaten Entwurf für ein GitHub Security Advisory vorzubereiten:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] as a private draft GitHub Security Advisory in
[owner/repository]. Verify the sealed source revision, repository, affected
paths, package metadata, and duplicate state. Show me the exact advisory
payload, authenticated GitHub CLI identity, and disclosure warnings. Do not
create anything until I approve that payload.

  Advisory-Entwürfe erfordern einen Befund aus einem versiegelten Scan des Typs `git_revision` sowie das
  verifizierte öffentliche kanonische Quell-Repository und Administratorzugriff. Mit diesem
  Workflow lassen sich Advisories weder gebündelt verarbeiten noch aktualisieren, veröffentlichen oder schließen. Wenn die Quelle diese Anforderungen nicht erfüllt, verwende ein genehmigtes
  privates Ziel für Issues.

## Vorgeschlagenen Schreibvorgang prüfen

1. Bestätige, dass die Befund-ID und der Fingerprint aus dem vorgesehenen versiegelten Scan stammen.
2. Bestätige den Anbieter, das genaue Linear-Team, das GitHub-Repository, das Jira-Projekt oder
das Advisory-Repository sowie die aktuelle Sichtbarkeit des Ziels.
3. Prüfe das Ergebnis der Duplikatprüfung: `create`, `reuse`, `update` oder `blocked`.
4. Lies den vollständigen vorgeschlagenen Titel und Text, die Fundstellen im Quellcode und die Metadaten
des Anbieters. Entferne Details zur Ausnutzung oder interne Nachweise, die am Ziel
nicht offengelegt werden sollten.
5. Genehmige nur diese exakte Payload. Wenn sich Ziel, Sichtbarkeit, Befundauswahl
oder Text ändern, ist eine neue Vorschau erforderlich.

Vertrauliche Befunde sollten an ein privates Ziel übermittelt werden. Für das Erstellen eines Issues in einem
internen oder öffentlichen GitHub-Repository sind ein ausdrücklicher Warnhinweis zur Sichtbarkeit
und die Genehmigung des vollständigen Inhalts erforderlich. Gehe mit der Beschreibung eines Advisory-Entwurfs so um, als
würde sie später öffentlich werden, und entferne Anmeldedaten, vertrauliche Nachweise sowie unnötige
Details zur Ausnutzung vor der Genehmigung.

Prüfe und genehmige externe Aktionen im Codex-Chat. Durch die Genehmigung
wird im Sicherheitsarbeitsbereich keine separate Ansicht für Issues oder Advisories erstellt.

## Nachverfolgten Eintrag verifizieren

Nachdem du den vorgeschlagenen Schreibvorgang genehmigt hast, prüft Codex die versiegelte Quelle,
das Ziel, die Zugriffsrechte und den Duplikatstatus erneut. Bei einem Batch verarbeitet Codex die Befunde
nacheinander und stoppt beim ersten unklaren Ergebnis. Das Erstellen, Aktualisieren oder
Wiederverwenden ist erst abgeschlossen, wenn Codex genau dieses Issue zurückliest und seine
Verknüpfungskennungen sowie seinen Inhalt verifiziert.

Bewahre die zurückgegebene kanonische Issue- oder Advisory-URL zusammen mit deinem Triage-Datensatz auf.
Fahre mit dem Schritt [Befund beheben und verifizieren](/de-DE/codex/security/plugin/fix-findings)
fort, wenn die verantwortliche Person den Eintrag zur Behebung übernimmt.

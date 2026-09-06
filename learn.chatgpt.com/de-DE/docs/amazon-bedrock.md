<!-- source: https://learn.chatgpt.com/de-DE/docs/amazon-bedrock -->

Konfiguriere die lokalen Oberflächen von ChatGPT Work und Codex so, dass sie die über Amazon Bedrock verfügbaren OpenAI-Modelle verwenden. Bei diesem Setup sendet der lokale Client Modellanfragen an Bedrock und nutzt dafür von AWS verwaltete Authentifizierung und Zugriffskontrollen.

## Funktionsweise

Wenn du eine lokale Oberfläche von ChatGPT Work oder Codex mit Amazon Bedrock als Modellanbieter konfigurierst, ist die von OpenAI gehostete Responses API nicht Teil des Anfragepfads. Der lokale Client sendet Modellanfragen an Amazon Bedrock. Bedrock stellt für unterstützte OpenAI-Modelle eine OpenAI-kompatible Implementierung der Responses API bereit.

  Die Authentifizierung erfolgt nativ über AWS. Du meldest dich mit einem Bedrock-API-Schlüssel oder
  AWS-IAM-Anmeldedaten an. Für diesen Anbieter verwendest du weder die ChatGPT-Anmeldung noch `OPENAI_API_KEY`
  zur Authentifizierung.

## Voraussetzungen

Du benötigst:

- Zugriff auf unterstützte OpenAI-Modelle in Amazon Bedrock.
- Eine AWS-Region, in der das ausgewählte Modell verfügbar ist.
- Eine für das AWS-Konto konfigurierte Authentifizierung für den Amazon Bedrock Mantle-Pfad.

## Anbieter konfigurieren

Trage den Modellanbieter `amazon-bedrock` für den Amazon Bedrock Mantle-Pfad in
`~/.codex/config.toml` ein. Die ChatGPT-Desktop-App, Codex CLI, die IDE-Erweiterung und das
SDK greifen auf dieselben lokalen Konfigurationsebenen zu. Die Angabe eines Modells ist optional.
Wähle bei Bedarf explizit ein unterstütztes Modell aus.

```toml
model_provider = "amazon-bedrock"

  Dieser Leitfaden behandelt den Amazon Bedrock Mantle-Pfad in unterstützten kommerziellen AWS-Regionen. Lokale Oberflächen von ChatGPT Work und Codex unterstützen keine Bedrock-Mantle-Endpunkte in AWS GovCloud-Regionen.

## Authentifizierungsoptionen

Lokale Oberflächen von ChatGPT Work und Codex unterstützen zwei Wege zur Bedrock-Authentifizierung. Sie prüfen die Optionen in dieser Reihenfolge:

1. Bedrock-API-Schlüssel.
2. Anmeldedatenkette des AWS SDK.

### Option 1: Bedrock-API-Schlüssel

Lege den Bedrock-API-Schlüssel in der Umgebung fest, die der lokale Client einliest. Bei der Authentifizierung per API-Schlüssel musst du eine AWS-Region angeben.

```shell

### Option 2: Anmeldedaten des AWS SDK

Verwende diesen Weg, wenn deine Organisation den Zugriff auf Bedrock über die Anmeldedatenkette des AWS SDK verwaltet. Der lokale Client kann diese Standardquellen des AWS SDK für Anmeldedaten verwenden:

#### Gemeinsam genutzte AWS-Konfigurationsdateien

Konfiguriere die gemeinsam genutzten AWS-Dateien `config` und `credentials`:

```shell
aws configure

#### Umgebungsvariablen

Lege die standardmäßigen Umgebungsvariablen des AWS SDK für Anmeldedaten fest:

```shell

#### Anmeldedaten für die AWS Management Console

Melde dich mit Anmeldedaten für die AWS Management Console an:

```shell
aws login

#### AWS SSO oder ein benanntes Profil

Melde dich mit AWS SSO an und wähle das benannte Profil aus:

```shell
aws sso login --profile codex-bedrock

#### Föderierte Identität

Konfiguriere für Unternehmens-SSO oder OIDC-Föderation außerhalb des lokalen Clients eine föderierte Identität mit
`credential_process`. Überlasse dem AWS SDK die Auflösung der
Anmeldedaten. Richte die Browseranmeldung, den Tokenaustausch, das Caching und die Aktualisierung im
`credential_process`-Hilfsprogramm deines AWS-Profils ein.

## Desktop-App und IDE-Erweiterung

Desktop-Apps und IDE-Erweiterungen übernehmen Umgebungsvariablen möglicherweise nicht aus der
Shell. Trage die erforderlichen Werte in `~/.codex/.env` ein und starte die App oder
Erweiterung anschließend neu.

```shell

## Setup überprüfen

- Öffne in Codex CLI `/status` und vergewissere dich, dass Codex den
Modellanbieter `amazon-bedrock` verwendet.
- Wähle nach dem Neustart in der ChatGPT-Desktop-App Work oder Codex aus und starte eine neue Aufgabe.
- Starte nach dem Neustart der IDE-Erweiterung eine neue Sitzung.
- Vergewissere dich, dass das ausgewählte Modell in der konfigurierten AWS-Region verfügbar ist und die AWS-Identität darauf zugreifen darf.

## Unterstützte Modelle

Verwende die exakten Modell-IDs:

```text
openai.gpt-5.6-sol
openai.gpt-5.6-terra
openai.gpt-5.6-luna
openai.gpt-5.5
openai.gpt-5.4

Die Modellverfügbarkeit variiert je nach AWS-Region. Prüfe vor der Auswahl eines Modells, [welche Modelle
in der jeweiligen AWS-Region
unterstützt werden](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html).

## Verfügbarkeit von Funktionen

Diese Konfiguration unterstützt lokale Arbeitsabläufe mit ChatGPT Work und Codex. Im Web gehostetes ChatGPT Work, Codex Cloud sowie Funktionen, die von durch OpenAI gehosteten Cloud-Diensten, gehosteten Tools oder in der Cloud verwalteten Discovery-Funktionen abhängen, sind derzeit nicht verfügbar.

  Der Schnellmodus ist mit Amazon Bedrock nicht verfügbar. Er nutzt priorisierte Verarbeitung. Das anfängliche Angebot für Amazon Bedrock unterstützt jedoch ausschließlich On-Demand-Inferenz.

  

  <div
    id="codex-plan-region-limits"
    className="not-prose mt-3 text-sm text-secondary"
  >
    <sup>\*</sup> Die Funktion ist derzeit nur in bestimmten Regionen verfügbar. Weitere Informationen zu
    geografischen Einschränkungen findest du in der Dokumentation zur jeweiligen Funktion.
  </div>
  <div
    id="codex-plan-plugin-limits"
    className="not-prose mt-1 text-sm text-secondary"
  >
    <sup>†</sup> Lokale Plug-in-Pakete und von OpenAI kuratierte Plug-ins, die keine
    ChatGPT-Authentifizierung erfordern, einschließlich Codex Security, sind verfügbar.
    Plug-ins, die eine ChatGPT-Authentifizierung, Konnektoren oder in der Cloud gehostete
    Freigaben erfordern, sind nicht verfügbar.
  </div>

## Fehlerbehebung

Wenn das Setup fehlschlägt, überprüfe Folgendes:

- Die Modell-ID entspricht exakt der ID eines unterstützten Modells.
- Du gibst eine AWS-Region an, in der das Modell verfügbar ist.
- Der Bedrock-API-Schlüssel oder die AWS-Anmeldedaten sind gültig und nicht abgelaufen.
- Die AWS-Identität verfügt über die Berechtigung, auf das ausgewählte Bedrock-Modell zuzugreifen.
- `AWS_BEARER_TOKEN_BEDROCK` ist nicht auf einen abgelaufenen oder nicht vorgesehenen Schlüssel gesetzt.
- Bei Verwendung der Desktop-App oder der IDE-Erweiterung sind die erforderlichen Umgebungsvariablen
  in `~/.codex/.env` vorhanden.

## Supportumfang

Der OpenAI Support kann dir beim Setup und bei der Konfiguration der Clients von ChatGPT Work und Codex,
bei Fragen zum Verhalten der lokalen CLI, der Desktop-App und der IDE-Erweiterung sowie
bei der lokalen Produktnutzung helfen.

Bei Fragen zu AWS-Anmeldedaten, IAM-Berechtigungen, dem Zugriff auf Bedrock-Modelle, Kontingenten oder der Abrechnung,
zur regionalen Verfügbarkeit, zu fehlgeschlagenen Bedrock-Anfragen, AWS-Dienstprotokollen oder
zum Verhalten des Bedrock-Dienstes wende dich an die zuständige AWS-Administration des Kundenunternehmens oder den AWS Support.

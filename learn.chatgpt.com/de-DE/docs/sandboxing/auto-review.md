<!-- source: https://learn.chatgpt.com/de-DE/docs/sandboxing/auto-review -->

Die automatische Überprüfung ersetzt die manuelle Genehmigung an der Sandbox-Grenze durch einen separaten
Prüfagenten. Der Hauptagent von Codex wird weiterhin in derselben Sandbox ausgeführt, mit
derselben Genehmigungsrichtlinie und denselben Netzwerk- und Dateisystembeschränkungen. Der
Unterschied besteht darin, wer die dafür infrage kommenden Eskalationsanfragen prüft.

  Die automatische Überprüfung gilt nur, wenn Genehmigungen interaktiv eingeholt werden. In der Praxis
  bedeutet das `approval_policy = "on-request"` oder eine granulare Genehmigungsrichtlinie, bei der
  die betreffende Prompt-Kategorie weiterhin angezeigt wird. Bei `approval_policy = "never"`
  gibt es nichts zu überprüfen.

In der ChatGPT-Desktop-App wird bei Auswahl eines genehmigten Daybreak-Modells
die Berechtigungssteuerung automatisch auf **Für mich genehmigen** umgestellt, wenn dieser
Modus für dein Konto verfügbar und laut Organisationsrichtlinie zulässig ist. Das
gilt auch, wenn du in der Desktop-App den Befehl `/model` verwendest. Wenn dieser Modus
nicht verfügbar ist, bleibt der aktuelle Berechtigungsmodus unverändert. Die Modellauswahl
setzt verwaltete Vorgaben der Organisation niemals außer Kraft.

Bevor du **Vollzugriff** für ein genehmigtes Sicherheitsmodell aktivierst, zeigt die
ChatGPT-Desktop-App eine modellspezifische Warnung vor gefährlichen Aktionen an. Die
Warnung empfiehlt stattdessen **Für mich genehmigen** und verweist auf die
[Konfiguration der Prüfrichtlinie](#configuration). Die Warnung stellt
die Sandbox-Grenze nicht wieder her und setzt die Organisationsrichtlinie nicht außer Kraft.

## Funktionsweise der automatischen Überprüfung

Der Ablauf im Überblick:

1. Der Hauptagent arbeitet in einer Sandbox im Modus `read-only` oder `workspace-write`.
2. Muss er die Sandbox-Grenze überschreiten, fordert er eine Genehmigung an.
3. Wenn `approvals_reviewer = "auto_review"` festgelegt ist, leitet Codex diese Genehmigungsanfrage
   an einen separaten Prüfagenten weiter, statt auf die Prüfung durch eine Person zu warten.
4. Der Prüfagent entscheidet, ob die Aktion ausgeführt werden soll, und gibt eine Begründung zurück.
5. Wird die Aktion genehmigt, wird die Ausführung fortgesetzt. Wird sie abgelehnt, erhält der
Hauptagent die Anweisung, eine deutlich sicherere Vorgehensweise zu finden oder anzuhalten und
bei dir nachzufragen.

Die automatische Überprüfung wechselt lediglich die Prüfinstanz; sie gewährt keine Berechtigungen. Sie erweitert
`writable_roots` nicht, aktiviert keinen Netzwerkzugriff und schwächt keine geschützten Pfade. Sie
ändert nur, wie Codex mit Aktionen umgeht, die ohnehin genehmigt werden müssen.

## Wann sie ausgelöst wird

Die automatische Überprüfung bewertet Genehmigungsanfragen, bei denen der Ablauf sonst für eine manuelle Prüfung angehalten würde.
Dazu gehören:

- Aufrufe von Shell- oder exec-Tools, die erhöhte Sandbox-Berechtigungen anfordern.
- Netzwerkanfragen, die von der aktuellen Sandbox oder Richtlinie blockiert werden.
- Dateiänderungen außerhalb der für Schreibzugriffe freigegebenen Stammverzeichnisse.
- Aufrufe von MCP- oder App-Tools, die aufgrund ihrer Tool-Annotationen
oder des konfigurierten Genehmigungsmodus genehmigt werden müssen.
- Zugriffe auf eine neue Website oder Domain über die Computernutzung.

Die automatische Überprüfung wird nicht für Routineaktionen ausgeführt, die bereits innerhalb der
Sandbox zulässig sind. Wenn ein Befehl mit dem aktiven `sandbox_mode` ausgeführt werden kann oder ein Tool-Aufruf
von der geltenden Richtlinie zugelassen ist, setzt der Hauptagent seine Arbeit ohne Überprüfung fort.

Die Computernutzung ist ein Sonderfall. Genehmigungsanfragen auf App-Ebene für die Computernutzung werden dir weiterhin
direkt vorgelegt. Die automatische Überprüfung ersetzt diese Prompts auf App-Ebene daher nicht.

## Was die automatische Überprüfung blockiert

Im Wesentlichen soll die automatische Überprüfung folgende Aktionen blockieren:

- private Daten, Geheimnisse oder Anmeldedaten an nicht vertrauenswürdige Ziele senden
- nach Anmeldedaten, Tokens, Cookies oder Sitzungsdaten suchen
- umfassende oder dauerhafte Schwächung der Sicherheit
- destruktive Aktionen mit erheblichem Risiko irreversibler Schäden

Die genaue Richtlinie findest du im Open-Source-Repository von Codex:
[policy\_template.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy_template.md)
und
[policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md).
Diese Richtlinie lässt sich für jedes Unternehmen mit `guardian_policy_config` oder
für einzelne Nutzende mit einer lokalen [`[auto_review].policy`](/de-DE/codex/config-file/config-advanced#approval-policies-and-sandbox-modes) anpassen.

## Was der Prüfagent sieht

Der Prüfagent ist selbst ein Codex-Agent, hat aber eine enger gefasste Aufgabe als der Hauptagent:
Er entscheidet, ob eine bestimmte Aktion über die Sandbox-Grenze hinweg ausgeführt werden soll.

Der Prüfagent sieht ein kompaktes Protokoll und die genaue Genehmigungsanfrage. Dazu
gehören normalerweise deine Nachrichten, sichtbare Updates des Assistenten, relevante
Tool-Aufrufe und Tool-Ausgaben sowie die Aktion, die gerade zur Genehmigung vorgeschlagen wird. Er kann
außerdem Prüfungen ohne Schreibzugriff durchführen, um fehlenden Kontext zusammenzutragen, nutzt diese Möglichkeit aber nur selten.

Interne Überlegungen des Assistenten sind nicht enthalten. Die automatische Überprüfung sieht aufbewahrte
Chat-Elemente und Tool-Belege, aber keine private Gedankenkette.

## Ablehnungen und Verhalten bei Fehlern

Eine ausdrückliche Ablehnung wird nicht wie ein gewöhnlicher Sandbox-Fehler behandelt. Codex gibt
dem Hauptagenten die Begründung des Prüfagenten zurück und ergänzt eine nachdrücklichere Anweisung:

- Versuche nicht, dasselbe Ergebnis durch einen Workaround, indirekte Ausführung oder
Umgehung der Richtlinie zu erzielen.
- Setze die Arbeit nur mit einer deutlich sichereren Alternative fort.
- Andernfalls halte an und frage die Person, die den Auftrag erteilt hat.

Codex nutzt außerdem pro Durchlauf einen Abbruchmechanismus für Ablehnungen. In der aktuellen
Open-Source-Implementierung unterbricht die automatische Überprüfung den Durchlauf nach `3`
aufeinanderfolgenden Ablehnungen oder bei `10` Ablehnungen in einem gleitenden Fenster der letzten `50`
Überprüfungen im selben Durchlauf.

Jedes Ergebnis, das keine Ablehnung ist, setzt den Zähler für aufeinanderfolgende Ablehnungen zurück. Sobald der Mechanismus greift,
gibt Codex eine Warnung aus und bricht den aktuellen Durchlauf mit einem Interrupt ab, statt
zuzulassen, dass der Agent weitere Eskalationsversuche in einer Schleife wiederholt.

Zeitüberschreitungen werden getrennt von ausdrücklichen Ablehnungen gemeldet. Der Hauptagent wird
darüber informiert, dass eine Zeitüberschreitung allein nicht beweist, dass die Aktion unsicher ist.

Für abgelehnte Aktionen gibt es außerdem eine explizite Möglichkeit, die Ablehnung zu übergehen. In der aktuellen
Open-Source-TUI führst du `/approve` aus, um die Auswahl **Ablehnungen der automatischen Überprüfung** zu öffnen. Wähle dann
eine kürzlich abgelehnte Aktion aus und genehmige einen erneuten Versuch. Codex erfasst bis zu 10
kürzlich erfolgte Ablehnungen pro Aufgabe. Diese Genehmigung ist eng begrenzt: Sie gilt genau für die
abgelehnte Aktion, nicht für ähnliche künftige Aktionen; sie wird für einen erneuten Versuch im
selben Kontext gespeichert; und der erneute Versuch durchläuft weiterhin die automatische Überprüfung. Im Hintergrund
fügt Codex eine Genehmigungsmarkierung auf Entwicklerebene für genau diese Aktion ein. Der
Prüfagent sieht deine ausdrückliche Ausnahmegenehmigung dann als Kontextinformation, befolgt aber weiterhin
die Richtlinie und kann die Aktion erneut ablehnen, wenn die Richtlinie vorsieht, dass du diese Art von
Ablehnung nicht aufheben darfst.

## Konfiguration

Weitere Informationen zum Setup findest du unter
[Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration#configure-automatic-review-policy).

Die standardmäßige Prüfrichtlinie befindet sich im Open-Source-Repository von Codex:
[core/src/guardian/policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md).
Unternehmen können deren mandantenspezifischen Abschnitt in den verwalteten Vorgaben durch
`guardian_policy_config` ersetzen. Einzelne Nutzende können außerdem
eine lokale Einstellung unter
[`[auto_review].policy`](/de-DE/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)
in ihrer `config.toml` festlegen. Verwaltete Vorgaben haben jedoch Vorrang:

```toml
[auto_review]
policy = """
YOUR POLICY GOES HERE
"""

Um die Richtlinie anzupassen, kopiere zunächst den vollständigen Wortlaut der Standardrichtlinie. Passe ihn dann
schrittweise an dein individuelles Risikoprofil an.

## Einen autorisierten Cybersicherheitsauftrag konfigurieren

Kombiniere für autorisierte Sicherheitsarbeiten die automatische Überprüfung mit einem schriftlich festgelegten
Auftragsumfang und einem [Berechtigungsprofil](/de-DE/codex/permissions) nach dem Prinzip der geringsten Rechte.
Verwende ein genehmigtes Testziel, dokumentiere die Aktionen und den Auftragszeitraum und
schließe Produktionssysteme, nicht zugehörige Hosts, Anmeldedaten und dauerhafte Änderungen
vom Umfang aus, sofern sie nicht ausdrücklich autorisiert sind.

Sowohl `[auto_review].policy` als auch `guardian_policy_config` ersetzen deine aktuelle
Prüfrichtlinie. Sie werden nicht mit Richtlinien zusammengeführt, die mit deinem Modell ausgeliefert oder
von deiner Organisation verwaltet werden. Die integrierten Prüfanweisungen und das
Antwortformat gelten weiterhin. Bevor du eines der Beispiele verwendest, kopiere die vollständige aktuelle
Richtlinie, behalte alle vorhandenen Regeln bei und füge die Regeln für deine autorisierten Arbeiten hinzu.
Ersetze den Platzhalter in Großbuchstaben durch diese vollständige Richtlinie. Wenn du
nicht auf die aktuelle Richtlinie zugreifen kannst, überschreibe sie nicht.

Die folgende lokale Vorlage für `config.toml` aktiviert die Überprüfung und fügt nach der vorhandenen Prüfrichtlinie begrenzte
Bedingungen hinzu:

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = ":workspace"

[auto_review]
policy = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.
- Approved actions: inspect the target, reproduce authorized vulnerabilities,
  and validate fixes within the documented engagement window.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only actions against the approved target that match the documented
  engagement scope and approved actions.
- Deny out-of-scope or unknown hosts, production access, credential theft,
  persistence, data exfiltration, destructive operations, and policy bypass.
- Deny ambiguous actions and high-impact changes until a human explicitly
  approves the exact target, action, and side effects.
"""

Ersetze das Beispielziel und die zulässigen Aktionen durch den tatsächlich genehmigten Umfang.
Setze die Zielbeschränkungen mit unabhängigen Dateisystem- und Netzwerkregeln durch;
Anweisungen für den Prüfagenten ersetzen diese Grenzen nicht.

Organisationen können dieselben Bedingungen in der verwalteten Datei `requirements.toml` durchsetzen:

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]
allowed_sandbox_modes = ["read-only", "workspace-write"]
default_permissions = ":workspace"

guardian_policy_config = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only approved actions against the documented engagement target.
- Deny out-of-scope hosts, production access, credential theft, persistence,
  data exfiltration, destructive operations, and attempts to bypass policy.
- Deny ambiguous or high-impact actions until a human explicitly approves the
  exact target, action, and side effects.
"""

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

`allowed_permission_profiles` steuert die aktuellen Berechtigungsprofile.
`allowed_sandbox_modes` verhindert außerdem den Vollzugriff in Bereitstellungen, die noch den
veralteten `sandbox_mode` verwenden.

Die verwaltete Einstellung `guardian_policy_config` hat Vorrang vor deiner lokalen
Einstellung `[auto_review].policy`. Behalte `approval_policy = "on-request"` oder eine andere
geeignete interaktive Genehmigungsrichtlinie und eine wirksame Sandbox-Grenze bei.
Bei `approval_policy = "never"`, `:danger-full-access` oder `--yolo` kann
eine Aktion erfolgen, ohne die für die Überprüfung erforderliche Genehmigungsanfrage zum Überschreiten der Grenze auszulösen.

Ein Netzwerkziel auf der Zulassungsliste löst für sich allein keine Überprüfung aus. Füge
explizite [Befehlsregeln](/de-DE/codex/agent-configuration/rules) mit
`decision = "prompt"` hinzu oder konfiguriere sensible MCP-Tools so, dass sie eine Genehmigung erfordern,
wenn auch Aktionen innerhalb der Sandbox an den Prüfagenten weitergeleitet werden müssen.

Unter [Modelle und vertrauenswürdiger Zugriff](/de-DE/codex/cyber-safety) und [empfohlene
Konfiguration](/de-DE/codex/cyber-safety/recommended-configuration) findest du Informationen zu Modellzugriff,
Auftrags-Setup und benutzerdefinierten Arbeitsabläufen für Agenten. Unter [Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration#configure-automatic-review-policy)
findest du Details zum Vorrang von Unternehmensvorgaben und zu unterstützten Clientversionen. Verwende für eigene API- oder
Agents SDK-Harnesses [Schutzmechanismen und Prüfung durch Personen](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution).

## Anzahl der Überprüfungen reduzieren, ohne die Sicherheit zu schwächen

Die automatische Überprüfung funktioniert am besten, wenn die Sandbox deine üblichen sicheren
Arbeitsabläufe bereits abdeckt. Wenn zu viele Routineaktionen überprüft werden müssen, korrigiere zuerst die Sandbox-Grenze,
statt dem Prüfagenten beizubringen, unnötige Eskalationsanfragen dauerhaft zu genehmigen.

In der Praxis sind folgende Änderungen am wirksamsten:

- Füge eng begrenzte
[`writable_roots`](/de-DE/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)
  für temporäre Arbeitsverzeichnisse oder benachbarte Repositorys hinzu, die du bewusst verwendest.
- Füge eng begrenzte [Präfixregeln](/de-DE/codex/agent-configuration/rules) hinzu. Bevorzuge präzise Befehlspräfixe
  wie `["cargo", "test"]` oder `["pnpm", "run", "lint"]` gegenüber weit gefassten
  Mustern wie `["python"]` oder `["curl"]`. Weit gefasste Regeln heben oft genau die
  Grenze auf, die die automatische Überprüfung schützen soll.

Sitzungsprotokolle der automatischen Überprüfung werden standardmäßig unter `~/.codex/sessions`
gespeichert. So kannst du Codex bitten, die bisherigen Vorgänge dort zu analysieren, bevor du
Richtlinien oder Berechtigungen änderst.

## Einschränkungen

Die automatische Überprüfung bietet einen besseren Ausgangspunkt für lang laufende agentische Aufgaben,
ist jedoch keine deterministische Sicherheitsgarantie.

- Sie bewertet nur Aktionen, die eine Grenze überschreiten sollen.
- Dennoch kann sie Fehler machen, insbesondere in adversarialen oder ungewöhnlichen Kontexten.
- Sie soll ein gutes Sandbox-Design, Monitoring und
eine organisationsspezifische Richtlinie ergänzen, nicht ersetzen.

Informationen zu den wissenschaftlichen Grundlagen und den veröffentlichten Evaluationsergebnissen findest du im
[Beitrag von Alignment Research zur automatischen Überprüfung](https://alignment.openai.com/auto-review/).

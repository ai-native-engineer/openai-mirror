<!-- source: https://learn.chatgpt.com/de-DE/docs/third-party/gitlab -->

Nutze Code Review mit Codex für eine zusätzliche, aussagekräftige Überprüfung von GitLab-Merge-Requests. Codex überprüft den Diff des Merge Requests, befolgt die Vorgaben für dein Repository und veröffentlicht ein reguläres GitLab-Code-Review, das sich auf schwerwiegende Probleme konzentriert.

Die GitLab-Unterstützung befindet sich in der Betaphase und ist in allen ChatGPT-Tarifen verfügbar. Die Codex-Integration
läuft in Codex Cloud. GitHub-typische Repository-Funktionen in der
Desktop-App, etwa **Pull Request erstellen**, sind in dieser Betaversion nicht enthalten.

## Bevor du beginnst

Stelle sicher, dass du Folgendes hast:

- Ein verbundenes GitLab-Konto. Für GitLab.com ist der
[standardmäßige Verbindungsablauf](https://help.openai.com/articles/20001486) erforderlich;
  selbstverwaltete GitLab-Instanzen oder GitLab Dedicated erfordern die
[Einrichtung einer Vorlage durch Workspace-Admins](https://help.openai.com/articles/20001487).
- Eine `AGENTS.md`-Datei, wenn Codex die für das Repository geltenden Review-Vorgaben
  befolgen soll.

## Code Review mit Codex einrichten

### GitLab-Verbindung und Review-Identität für Codex einrichten

Verbinde bei GitLab.com dein GitLab-Konto mit Codex, nachdem du
[die Verbindung zu GitLab in ChatGPT hergestellt hast](https://help.openai.com/articles/20001486).
Bei selbstverwaltetem GitLab oder GitLab Dedicated sollten alle Reviewenden ihr Konto erst verbinden, nachdem die
[Vorlage für Workspace-Admins](https://help.openai.com/articles/20001487)
veröffentlicht wurde.

Öffne bei selbstverwaltetem GitLab oder GitLab Dedicated **Codex Cloud** → **Einstellungen** →
[**Konnektoren**](https://chatgpt.com/codex/cloud/settings/connectors). Workspace-Admins
können Codex ein Dienstkonto erstellen lassen oder ein vorhandenes persönliches
Zugriffstoken für ein Dienstkonto speichern.

#### Konto von Codex erstellen lassen

In **Codex Cloud** → **Einstellungen** → **Konnektoren** wählst du die App für deinen
selbstverwalteten GitLab-Host oder deinen Host bei GitLab Dedicated aus. Wähle anschließend **Dienstkonto einrichten** →
**Dienstkonto erstellen**. Wer als Workspace-Admin das Setup abschließt, benötigt
Administratorzugriff auf die GitLab-Instanz. Wähle entweder **Ausgewählte Gruppen**
oder **Nur ausgewählte Projekte**. Lege dann fest, wo Codex arbeiten soll, und erstelle
das Konto. Mit der Gruppenoption erhält das Konto für jede ausgewählte Gruppe Developer-Zugriff,
der an deren Projekte und Untergruppen vererbt wird. Die Projektoption gewährt Developer-Zugriff
ausschließlich auf die von dir ausgewählten Projekte. Codex erstellt das Instanzdienstkonto „ChatGPT
Codex Connector“ mit einem persönlichen Zugriffstoken mit dem
Scope `api`.

#### Vorhandenes Konto verwenden

Erstelle oder wähle in GitLab ein Dienstkonto und gewähre ihm Developer-Zugriff
nur auf die Gruppen oder Projekte, in denen Codex arbeiten soll. Öffne die Seite **Konten für
Dienste** und wähle das Konto → **Zugriffstoken verwalten** → **Neues Token
hinzufügen** , um
[ein persönliches Zugriffstoken zu erstellen](https://docs.gitlab.com/user/profile/service_accounts/#create-a-personal-access-token-for-a-service-account). Es muss
den Scope `api` haben und frühestens in 30 Tagen ablaufen. Wechsle anschließend zu
Codex, wähle **Vorhandenes Dienstkonto verwenden**, füge das Token ein und wähle
**Token speichern**. Das Token wird beim Speichern verschlüsselt und nie wieder angezeigt.

#### Token für das Dienstkonto verwalten

Workspace-Admins können das Dienstkonto unter **Codex Cloud** →
**Einstellungen** → **Konnektoren** verwalten. Bei einem von Codex erstellten Konto können sie
das aktuelle Token widerrufen und ein neues generieren. Bei einem vorhandenen Konto können sie
das in Codex gespeicherte Token ersetzen oder entfernen und es bei Bedarf separat in GitLab
widerrufen. Codex kann erst auf GitLab-Aktivitäten reagieren, wenn ein gültiges Token
konfiguriert ist.

### Festlegen, wie GitLab-Aktivitäten an Codex übermittelt werden

#### Projektumgebung für Programmieraufgaben oder ein projektspezifisches Setup erstellen

Wähle unter **Codex Cloud** → **Einstellungen** → **Umgebungen** das GitLab-Projekt
aus und erstelle eine Projektumgebung, wenn Codex dafür Code schreiben oder ausführen soll,
etwa um Dateien zu bearbeiten, Änderungen zu committen oder Updates in den Branch eines
Merge Requests zu pushen. Eine Projektumgebung ist auch erforderlich, wenn ein Review von projektspezifischen Secrets,
Netzwerkzugriff oder Setup-Befehlen abhängt.

Bei GitLab.com ist außerdem eine Projektumgebung erforderlich, um Reviews durch Codex zu aktivieren.

Aktiviere beim Erstellen der Umgebung **Codex-Aktivitäten aus GitLab aktivieren**,
um den Projekt-Webhook zu installieren, der Ereignisse zu Merge Requests, Kommentaren und Issues
an Codex übermittelt. Zum Erstellen des Projekt-Webhooks benötigst du Zugriff als Maintainer oder Owner,
Administratorzugriff oder eine benutzerdefinierte Rolle, die Projekt-Webhooks verwalten
kann. Signierte Projekt- und Gruppen-Webhooks erfordern GitLab 19.0 oder neuer. Prüfe bei
selbstverwaltetem GitLab 19.0, ob das Feature-Flag `webhook_signing_token`
aktiviert ist. Es ist standardmäßig aktiviert und wurde in GitLab 19.1 entfernt.

#### GitLab-Aktivitäten für Codex-Reviews gruppenweit aktivieren

Bei selbstverwaltetem GitLab oder GitLab Dedicated können Workspace-Admins **Umgebungen**
→ **GitLab-Aktivitäten** → **Gruppen verwalten** öffnen, um Codex-Reviews für eine Gruppe
und ihre Untergruppen zu aktivieren. Codex installiert einen Gruppen-Webhook, der die Projekte
in der gesamten Gruppe abdeckt. Das verbundene GitLab-Konto muss in der Gruppe die Rolle „Owner“ haben.
Gruppen-Webhooks erfordern GitLab Premium oder Ultimate sowie GitLab 19.0 oder neuer.

Gruppenaktivitäten ermöglichen Code Reviews, erstellen jedoch keine Projektumgebungen. Um durch GitLab ausgelöste Programmieraufgaben auszuführen, etwa Dateien zu bearbeiten, Befehle auszuführen, Änderungen zu committen oder Updates für einen Merge Request zu pushen, musst du eine Projektumgebung erstellen.

### Richtlinien für Code Reviews konfigurieren

Konfiguriere die Richtlinien für Code Reviews in den
[Codex-Review-Einstellungen](https://chatgpt.com/codex/cloud/settings/code-review?provider=gitlab).
Wähle die Repository-Richtlinie aus: `Review my MRs`, `Review team MRs`,
`Review all MRs` oder `Follow personal`. Lege anschließend fest, wann Reviews ausgeführt werden: **Beim Öffnen eines MR**,
**Bei jedem Push** oder **Intelligenter Auslöser (experimentell)**. Repository-Einstellungen können
persönliche Standardeinstellungen überschreiben.

## Codex-Review anfordern

1. Erwähne `@codex review` in einem Kommentar zum Merge Request.
2. Warte, bis Codex reagiert (👀) und ein Review veröffentlicht.

Codex veröffentlicht in GitLab Diskussionen und Notizen zum Merge Request, wie es auch ein Teammitglied tun würde. Manuell angeforderte Reviews können standardmäßig Befunde mit den Prioritäten P0, P1 und P2 enthalten, während sich automatische Reviews auf Befunde mit den Prioritäten P0 und P1 konzentrieren.

## Automatische Reviews aktivieren

Um geeignete Merge Requests automatisch überprüfen zu lassen, aktiviere in den Codex-Einstellungen **Automatische
Reviews** , wähle die GitLab-Repository-Richtlinie aus und lege einen
Auslöser fest: **Beim Öffnen eines MR**, **Bei jedem Push** oder **Intelligenter Auslöser (experimentell)**.
Codex wird ohne einen Kommentar mit `@codex review` ausgeführt, wenn das Ereignis zum Merge Request
der ausgewählten Richtlinie und dem Auslöser entspricht.

GitLab-Aktivitäten müssen über einen Projekt-Webhook oder den Webhook einer übergeordneten Gruppe aktiviert sein. Bei selbstverwaltetem GitLab oder GitLab Dedicated muss das konfigurierte Dienstkonto außerdem Schreibzugriff auf das Projekt haben. Falls eine konfigurierte Projektumgebung vorhanden ist, verwendet Codex sie. Wenn GitLab-Aktivitäten bereits für eine übergeordnete Gruppe aktiviert sind, gilt dies automatisch auch für ihre untergeordneten Projekte.

## Festlegen, was Codex überprüft

Codex durchsucht dein Repository nach `AGENTS.md`-Dateien und befolgt die geltenden
Regeln für Code Reviews. Ergänze die Datei, die dem betreffenden Code am nächsten liegt, um einen Abschnitt `## Code Review Rules`.
Verwende Überschriften mit `###`, um zusammengehörige Prüfungen bei
Bedarf zu gruppieren.

Ein Dienst für Experimentberichte kann beispielsweise verhindern, dass das Verhalten nach der Exposition eine Vergleichskohorte verändert:

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Lege Regeln für das gesamte Repository in der `AGENTS.md`-Datei im Stammverzeichnis ab und dienstspezifische Regeln in
einer Datei in einem Unterverzeichnis, etwa `services/experiment_reporting/AGENTS.md`. Codex wendet
auf jede geänderte Datei die allgemeinen und die jeweils für sie geltenden spezifischen Vorgaben an,
sodass Änderungen in anderen Bereichen keinen dienstspezifischen Kontext benötigen.

Beginne mit zwei oder drei prägnanten Regeln für Prüfungen, die Reviewende häufig erklären. Hilfreiche Regeln:

- **Konzentriere dich auf wichtiges, Repository-spezifisches Verhalten.** Beschreibe die
  Kompatibilitätsanforderung, Datenabgrenzung oder riskante Nebenwirkung, auf die Codex hinweisen soll,
  und erläutere, warum das wichtig ist.
- **Beschreibe die sichere Vorgehensweise oder den Ausnahmefall.** Gib Codex genügend Kontext, um
  ein tatsächliches Problem von erwartetem Verhalten zu unterscheiden.
- **Halte Regeln klar abgegrenzt und langfristig gültig.** Beschreibe gewünschte Ergebnisse statt Funktionsnamen, die sich
  ändern können, und platziere Vorgaben nahe beim Code, für den sie gelten.
- **Überlasse automatisierbare Prüfungen der CI.** Nimm Formatierung, Linting und andere
  deterministische Prüfungen nicht in die Review-Regeln auf.

Öffne einen repräsentativen Merge Request und fordere mit `@codex review` ein Review an.
Passe die Regeln anhand der Ergebnisse und des Feedbacks an und grenze Vorgaben ein oder
entferne sie, wenn sie irrelevante Hinweise erzeugen.

Regeln für Code Reviews geben Codex Orientierung. Sie ersetzen keine Tests, keine Branch-Schutzregeln und keine erforderlichen Genehmigungen.

Wenn Codex einmalig einen bestimmten Aspekt prüfen soll, ergänze deinen Kommentar zum Merge Request entsprechend:

`@codex review for issues in the database migration`

## Auf Review-Ergebnisse reagieren

Für die Behebung der im Review gefundenen Probleme ist eine **konfigurierte Projektumgebung** erforderlich;
Gruppenaktivitäten allein ermöglichen Reviews, aber keine Programmieraufgaben. Wenn das Projekt über
eine Umgebung verfügt, fordere Codex mit einem weiteren Kommentar auf, ein Problem im selben Merge Request
zu beheben:

```md
@codex fix the P1 issue

Codex startet einen [Cloud-Chat](/de-DE/codex/cloud) mit dem Merge Request als Kontext und
kann eine Korrektur zurück in den Branch pushen, sofern die entsprechende Berechtigung vorliegt.

## Codex weitere Aufgaben geben

Auch andere Programmieraufgaben erfordern eine **konfigurierte Projektumgebung**;
Gruppenaktivitäten allein ermöglichen Reviews. Wenn du `@codex` in einem Kommentar mit
einer anderen Anweisung als `review` erwähnst, startet Codex einen [Cloud-Chat](/de-DE/codex/cloud), in dem
dein Merge Request als Kontext dient.

```md
@codex fix the CI failures

## Probleme mit Code Review beheben

Wenn Codex nicht reagiert oder kein Review veröffentlicht:

- Prüfe, ob die gewünschte GitLab-App ausgewählt ist. Falls du ein projektspezifisches Setup verwendest, prüfe, ob für das Projekt die vorgesehene Umgebung in Codex Cloud eingerichtet ist.
- Prüfe, ob Aktivitäten für das Projekt oder eine übergeordnete Gruppe aktiviert sind. Öffne in GitLab
**Webhooks** →
[**Letzte Ereignisse**](https://docs.gitlab.com/user/project/integrations/webhooks/)
  und kontrolliere, ob Ereignisse zu Merge Requests und Notizen erfolgreich übermittelt werden.
- Prüfe bei selbstverwaltetem GitLab oder GitLab Dedicated, ob der Projekt- oder Gruppen-Webhook
  signiert ist, die SSL-Überprüfung aktiviert ist und die Instanz GitLab 19.0 oder
  neuer verwendet. Kontrolliere bei selbstverwaltetem GitLab 19.0, ob das Feature-Flag `webhook_signing_token`
  aktiviert ist. Repariere Hooks, die nach Fehlern automatisch deaktiviert wurden.
- Prüfe bei selbstverwaltetem GitLab oder GitLab Dedicated, ob ein vorhandenes persönliches
  Zugriffstoken für das Dienstkonto aktiv ist und über den Scope `api` verfügt. Wenn Codex das
  Dienstkonto erstellt hat, prüfe, ob es in den
[Einstellungen für Codex-Konnektoren](https://chatgpt.com/codex/cloud/settings/connectors) korrekt konfiguriert ist
  und ob das Projekt oder die Gruppe aktiviert ist.
- Prüfe bei selbstverwaltetem GitLab oder GitLab Dedicated, ob das Workspace-Dienstkonto und nicht nur das verbundene GitLab-Konto über Developer-Zugriff auf das Projekt oder eine übergeordnete Gruppe verfügt. Nur dann kann Codex Reviews und Reaktionen veröffentlichen. Mitgliedschaften werden vererbt; GitLab-Aktivitäten und der Zugriff des Dienstkontos sind voneinander unabhängig.
- Prüfe, ob **Code Review** oder **Automatische Reviews** aktiviert ist und der MR
  der Repository-Richtlinie sowie dem Auslöser entspricht.
- Verwende `@codex review`.

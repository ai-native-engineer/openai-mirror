<!-- source: https://learn.chatgpt.com/de-DE/docs/custom-prompts -->

Benutzerdefinierte Prompts sind veraltet. Verwende [Skills](/de-DE/codex/build-skills) für wiederverwendbare
  Anweisungen, die Codex explizit oder implizit aufrufen kann.

Mit benutzerdefinierten Prompts (veraltet) kannst du Markdown-Dateien in wiederverwendbare Prompts umwandeln, die du sowohl in der Codex CLI als auch in der Codex IDE-Erweiterung als Slash-Befehle aufrufen kannst.

Benutzerdefinierte Prompts müssen explizit aufgerufen werden und befinden sich in deinem lokalen Codex-Home-Verzeichnis (zum Beispiel `~/.codex`). Daher werden sie nicht über dein Repository geteilt. Wenn du einen Prompt teilen möchtest (oder Codex ihn implizit aufrufen soll), [verwende Skills](/de-DE/codex/build-skills).

1. Erstelle das Prompt-Verzeichnis:

   ```bash
   mkdir -p ~/.codex/prompts

2. Erstelle die Datei `~/.codex/prompts/draftpr.md` mit wiederverwendbaren Anweisungen:

   ```markdown
   ---
   description: Prep a branch, commit, and open a draft PR
   argument-hint: [FILES=<paths>] [PR_TITLE="<title>"]
   ---

   Create a branch named `dev/<feature_name>` for this work.
   If files are specified, stage them first: $FILES.
   Commit the staged changes with a clear message.
   Open a draft PR on the same branch. Use $PR_TITLE when supplied; otherwise write a concise summary yourself.

3. Starte Codex neu, damit der neue Prompt geladen wird (starte deine CLI-Sitzung neu und lade die IDE-Erweiterung neu, falls du sie verwendest).

Erwartetes Ergebnis: Wenn du `/prompts:draftpr` im Menü für Slash-Befehle eingibst, wird dein benutzerdefinierter Befehl mit der Beschreibung aus dem Frontmatter und dem Hinweis angezeigt, dass Dateien und ein PR-Titel optional sind.

## Metadaten und Argumente hinzufügen

Beim nächsten Start der Sitzung liest Codex die Prompt-Metadaten ein und löst die Platzhalter auf.

- **Beschreibung:** Wird im Pop-up unter dem Befehlsnamen angezeigt. Lege sie im YAML-Frontmatter mit `description:` fest.
- **Argumenthinweis:** Dokumentiere die erwarteten Parameter mit `argument-hint: KEY=<value>`.
- **Positionale Platzhalter:** `$1` bis `$9` werden durch die entsprechenden Argumente ersetzt, die du nach dem Befehl durch Leerzeichen getrennt angibst. `$ARGUMENTS` enthält alle Argumente.
- **Benannte Platzhalter:** Verwende Namen in Großbuchstaben wie `$FILE` oder `$TICKET_ID` und gib Werte im Format `KEY=value` an. Setze Werte, die Leerzeichen enthalten, in Anführungszeichen (zum Beispiel `FOCUS="loading state"`).
- **Literale Dollarzeichen:** Schreibe `$$`, um im resultierenden Prompt ein einzelnes `$` auszugeben.

Wenn du Prompt-Dateien bearbeitet hast, starte Codex neu oder öffne einen neuen Chat, damit die Änderungen geladen werden. Codex ignoriert im Prompt-Verzeichnis alle Dateien, die nicht im Markdown-Format vorliegen.

## Benutzerdefinierte Befehle aufrufen und verwalten

1. Gib in Codex (CLI oder IDE-Erweiterung) `/` ein, um das Menü für Slash-Befehle zu öffnen.
2. Gib `prompts:` oder den Namen des Prompts ein, zum Beispiel `/prompts:draftpr`.
3. Gib die erforderlichen Argumente an:

   ```text
   /prompts:draftpr FILES="src/pages/index.astro src/lib/api.ts" PR_TITLE="Add hero animation"

4. Drücke die Eingabetaste, um die resultierenden Anweisungen zu senden (lass Argumente weg, die du nicht benötigst).

Erwartetes Ergebnis: Codex verarbeitet den Inhalt von `draftpr.md`, ersetzt dabei die Platzhalter durch die von dir angegebenen Argumente und sendet das Ergebnis anschließend als Nachricht.

Verwalte Prompts, indem du Dateien unter `~/.codex/prompts/` bearbeitest oder löschst. Codex berücksichtigt in diesem Ordner nur Markdown-Dateien auf der obersten Ebene. Lege daher jeden benutzerdefinierten Prompt direkt unter `~/.codex/prompts/` und nicht in Unterverzeichnissen ab.

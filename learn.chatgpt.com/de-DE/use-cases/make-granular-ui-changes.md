<!-- source: https://learn.chatgpt.com/de-DE/use-cases/make-granular-ui-changes -->

## Einführung

Wenn du eine bestehende App hast und ihre UI schnell weiterentwickeln möchtest, kannst du mit `gpt-5.3-codex-spark` kleine, gezielte UI-Änderungen vornehmen.
Codex-Spark ist unser schnellstes Modell und für nahezu verzögerungsfreie Code-Iterationen in Echtzeit optimiert.

Am besten wiederholst du einen kurzen Ablauf: ein visueller Hinweis, eine gezielte Änderung, eine Browserprüfung und dann der nächste Hinweis.

  Für diese Aufgabe kannst du das [Modell Codex Spark](/de-DE/codex/models) verwenden. Es ist
  in Pro-Tarifen verfügbar.

## Modell auswählen

Nutze für schnelle UI-Iterationen zunächst `gpt-5.3-codex-spark`, sofern du darauf zugreifen kannst. Dieses Modell ist weniger leistungsfähig als unsere universell einsetzbaren Modelle, aber für Code-Iterationen in Echtzeit ausgelegt. Wenn du nicht darauf zugreifen kannst, verwende <code>{RECOMMENDED_MODEL_REFERENCES.latestMainlineModel.slug}</code> mit dem Reasoning-Aufwand `medium` oder `low`.

Dieser Kompromiss eignet sich gut für kleinteilige UI-Arbeiten. In der Regel brauchst du kein besonders leistungsfähiges Modell, um einen Button zu verschieben, einen Breakpoint feinzujustieren oder einen Komponentenzustand anzupassen. Du brauchst ein Modell, das schnell reagiert, den lokalen Code versteht, die richtige Datei bearbeitet und den Ablauf wiederholt, ohne dass sich die Iteration schwerfällig anfühlt.

## Entwicklungsablauf

1. Öffne die bestehende App und rufe die relevante Route oder Komponente auf.
2. Öffne den aktiven Codex-Chat in einem [schwebenden Fenster](/codex/reference/settings#keep-a-chat-near-your-work) und lass dieses während der Arbeit neben deinem Browser, deinem Editor oder deiner Designvorschau geöffnet.
3. Gib Codex jeweils nur eine konkrete UI-Änderung vor. Ergänze die Route, den Viewport, einen aktuellen Screenshot, einen Ziel-Screenshot oder die genaue Produktvorgabe, sofern vorhanden.
4. Bitte Codex, die aktuelle Implementierung zu prüfen, die kleinstmögliche vertretbare Änderung vorzunehmen und die vorhandenen Komponenten, Tokens, Layout-Grundelemente sowie den Datenfluss der App beizubehalten.
5. Prüfe das Ergebnis und sende dann im selben Chat die nächste kleine Anpassung.

## Kleine Prompts formulieren

Prompts für kleinteilige UI-Änderungen sollten direkt und klar begrenzt sein. Ein guter Prompt benennt den betroffenen UI-Bereich, die gewünschte Änderung und die erwartete Prüfung.

Wenn das Ergebnis fast, aber noch nicht ganz stimmt, formuliere auch den nächsten Prompt ebenso konkret:

## Wann du gründlicher vorgehen solltest

Halte nicht am schnellen Ablauf fest, wenn die Aufgabe nicht mehr kleinteilig ist. Wechsle zu einem leistungsfähigeren Modell und einem durchdachteren Prompt, wenn die Änderung eine umfassende Refaktorierung, ein neues Grundelement des Designsystems, komplexe Barrierefreiheitslogik oder eine Produktentscheidung erfordert, die mehr als einen Bildschirm betrifft.

Schnelle UI-Iterationen funktionieren am besten, wenn Codex einen UI-Bereich anpasst, dessen Aufbau bereits klar ist, statt die App von Grund auf neu zu gestalten.

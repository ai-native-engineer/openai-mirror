<!-- source: https://learn.chatgpt.com/de-DE/use-cases/api-integration-migrations -->

## Einführung

Wenn wir neue Modelle und API-Funktionen veröffentlichen, empfehlen wir dir, deine Integration zu aktualisieren, damit du von den neuesten Verbesserungen profitierst.
Beim Wechsel von einem Modell zu einem anderen reicht es oft nicht aus, nur den Modellnamen zu ändern.

Es kann Änderungen an der API geben. Für das Modell GPT-5.4 haben wir der Assistentennachricht beispielsweise einen neuen Parameter `phase` hinzugefügt, den du in deiner Integration berücksichtigen solltest. Vor allem aber kann sich das Modell anders verhalten, sodass Änderungen an deinen bestehenden Prompts nötig werden.

Bei der Migration auf ein neues Modell solltest du neben den notwendigen Codeänderungen auch die Auswirkungen auf deine Arbeitsabläufe bewerten.

## Den Skill für die OpenAI-Dokumentation nutzen

Die Seite [Modellempfehlungen](/api/docs/guides/latest-model) bündelt für jede Modellgeneration Hinweise zu API-Funktionen, Modellverhalten, Migration und zum Formulieren von Prompts.

Der Skill für die OpenAI-Dokumentation enthält außerdem [spezifische Hinweise](https://github.com/openai/codex/blob/6323f0104d17d211029faab149231ba787f7da37/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-5p4.md) als konkrete Referenz für die Migration. Welches Modell aktuell als Upgrade-Ziel empfohlen wird, erfährst du auf der Seite [Modellempfehlungen](/api/docs/guides/latest-model).

Codex enthält jetzt standardmäßig den Skill für die OpenAI-Dokumentation. Erwähne ihn daher in deinem Prompt, damit du beim Entwickeln mit der OpenAI API auf die gesamte aktuelle Dokumentation und alle aktuellen Empfehlungen zugreifen kannst.

## Eine robuste Evals-Pipeline aufbauen

Codex kann deine Prompts anhand der neuesten Empfehlungen zum Formulieren von Prompts automatisch aktualisieren. Du solltest jedoch automatisiert prüfen können, ob deine Integration wie erwartet funktioniert.

Richte eine Evals-Pipeline ein, die du nach jeder Änderung an deiner Integration ausführen kannst, um sicherzustellen, dass keine Regressionen im Verhalten auftreten.

Dieser [Cookbook-Leitfaden](/cookbook/examples/evaluation/building_resilient_prompts_using_an_evaluation_flywheel) erläutert ausführlich, wie du dies mit unserer [Evals API](/api/docs/guides/evals) umsetzt.

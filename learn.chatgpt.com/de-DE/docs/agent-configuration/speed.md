<!-- source: https://learn.chatgpt.com/de-DE/docs/agent-configuration/speed -->

<strong>ChatGPT Work und Codex teilen sich das Nutzungskontingent.</strong> Für beide gelten dieselben
  Preise, Credits und Nutzungslimits. Unter [Codex-Preise](/codex/pricing) findest du
  weitere Informationen.

## Schnellmodus

Mit Codex kannst du die Geschwindigkeit des Modells erhöhen. Dafür werden mehr
Credits verbraucht.

Bei GPT-5.6, GPT-5.5 und GPT-5.4 erhöht der Schnellmodus die Modellgeschwindigkeit auf das 1,5-Fache.
GPT-5.6 und GPT-5.5 verbrauchen dabei 2,5-mal so viele Credits wie im Standardmodus;
GPT-5.4 verbraucht doppelt so viele.

Der Schnellmodus für GPT-6 Astra verbraucht, sofern verfügbar,
2,5-mal so viele Credits wie im Standardmodus. Informationen zur Modellverfügbarkeit findest du unter [Modelle](/de-DE/codex/models) und
zu den Token-Preisen unter [Preise](/de-DE/codex/pricing#token-rates).

Mit `/fast on`, `/fast off` oder `/fast status` kannst du in der CLI die aktuelle Einstellung ändern oder
prüfen. Du kannst die Standardeinstellung außerdem dauerhaft festlegen, indem du `service_tier =
"fast"` zusammen mit `[features].fast_mode = true` in `config.toml` einträgst. Der Schnellmodus ist
in der ChatGPT-Desktop-App, in der Codex CLI und in der IDE-Erweiterung verfügbar, wenn du
dich mit ChatGPT anmeldest. Der Schnellmodus ist eine Funktion, die über ChatGPT-Credits abgerechnet wird. Wenn du einen API-Schlüssel verwendest,
gelten für Codex stattdessen die Preise für API-Token. Die Multiplikatoren für ChatGPT-Credits
gelten dann nicht. Für die Priority-Verarbeitung der API gilt ein eigener Tarif; bei GPT-5.6 entspricht dieser
dem Doppelten des Standardtarifs für API-Token.

## Codex-Spark

GPT-5.3-Codex-Spark ist ein eigenständiges, schnelles, aber weniger leistungsfähiges Codex-Modell, das für
nahezu verzögerungsfreie Iterationen am Code in Echtzeit optimiert ist. Anders als der Schnellmodus, der ein
unterstütztes Modell bei höherem Credit-Verbrauch beschleunigt, ist Codex-Spark als eigenes Modell auswählbar
und hat eigene Nutzungslimits.

Während der Forschungsvorschau ist Codex-Spark nur mit einem Abonnement für ChatGPT Pro verfügbar.

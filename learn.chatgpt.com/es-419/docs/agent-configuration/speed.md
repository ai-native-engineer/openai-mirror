<!-- source: https://learn.chatgpt.com/es-419/docs/agent-configuration/speed -->

<strong>ChatGPT Work y Codex comparten el uso.</strong> Para ambos se aplican los mismos
  precios, créditos y límites de uso. Consulta [Precios de Codex](/codex/pricing) para obtener
  más información.

## Modo rápido

Codex permite aumentar la velocidad del modelo a cambio de un mayor
consumo de créditos.

Para GPT-5.6, GPT-5.5 y GPT-5.4, el modo rápido multiplica la velocidad del modelo por 1,5.
GPT-5.6 y GPT-5.5 consumen créditos a una tasa equivalente a 2,5 veces la tasa estándar; GPT-5.4 consume
créditos al doble de la tasa estándar.

El modo rápido de GPT-6 Astra consume créditos a una tasa equivalente a 2,5 veces la tasa estándar donde está
disponible. Consulta [Modelos](/es-419/codex/models) para conocer la disponibilidad de los modelos y
[Precios](/es-419/codex/pricing#token-rates) para conocer las tarifas por token.

Usa `/fast on`, `/fast off` o `/fast status` en la CLI para cambiar o consultar
la configuración actual. También puedes guardar el valor predeterminado con `service_tier =
"fast"` y `[features].fast_mode = true` en `config.toml`. El modo rápido está
disponible en la aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE cuando
inicias sesión con ChatGPT. El modo rápido es una función que usa créditos de ChatGPT. Si usas una clave de API,
Codex aplica en su lugar los precios por token de la API, y los multiplicadores de créditos de ChatGPT no
se aplican. El procesamiento prioritario de la API tiene su propia tarifa; para GPT-5.6, cuesta
el doble de la tarifa estándar por token de la API.

## Codex-Spark

GPT-5.3-Codex-Spark es un modelo de Codex independiente, rápido y con menos capacidades, optimizado para
iteraciones de programación en tiempo real y prácticamente instantáneas. A diferencia del modo rápido, que acelera un
modelo compatible con una mayor tasa de consumo de créditos, Codex-Spark es una opción de modelo independiente
y tiene sus propios límites de uso.

Durante la versión preliminar de investigación, Codex-Spark solo está disponible para los suscriptores de ChatGPT Pro.

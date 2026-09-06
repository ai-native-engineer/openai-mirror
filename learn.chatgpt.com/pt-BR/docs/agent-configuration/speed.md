<!-- source: https://learn.chatgpt.com/pt-BR/docs/agent-configuration/speed -->

<strong>O uso é compartilhado entre o ChatGPT Work e o Codex.</strong> Os mesmos
  preços, créditos e limites de uso se aplicam a ambos. Consulte [Preços do Codex](/codex/pricing) para
  mais detalhes.

## modo Fast

O Codex permite aumentar a velocidade do modelo em troca de um maior
consumo de créditos.

Para GPT-5.6, GPT-5.5 e GPT-5.4, o modo Fast multiplica a velocidade do modelo por 1,5.
GPT-5.6 e GPT-5.5 consomem créditos a uma taxa equivalente a 2,5 vezes a taxa padrão; GPT-5.4 consome
créditos ao dobro da taxa padrão.

Quando disponível, o modo Fast do GPT-6 Astra consome créditos a uma taxa equivalente a
2,5 vezes a taxa padrão. Consulte [Modelos](/pt-BR/codex/models) para saber sobre a disponibilidade dos modelos e
[Preços](/pt-BR/codex/pricing#token-rates) para conferir as tarifas por token.

Use `/fast on`, `/fast off` ou `/fast status` na CLI para alterar ou consultar
a configuração atual. Você também pode salvar a configuração padrão com `service_tier =
"fast"` e `[features].fast_mode = true` em `config.toml`. O modo Fast está
disponível no aplicativo do ChatGPT para desktop, na Codex CLI e na extensão para IDE quando você
faz login com o ChatGPT. O modo Fast é um recurso que usa créditos do ChatGPT. Com uma chave de API,
o Codex usa os preços dos tokens da API, e os multiplicadores de créditos do ChatGPT não
se aplicam. O processamento prioritário da API tem uma tarifa própria; no caso do GPT-5.6, custa
o dobro da tarifa padrão por token da API.

## Codex-Spark

GPT-5.3-Codex-Spark é um modelo Codex distinto, rápido e menos capaz, otimizado para
iterações de código quase instantâneas e em tempo real. Diferentemente do modo Fast, que acelera um
modelo compatível em troca de uma taxa maior de consumo de créditos, o Codex-Spark é uma opção de modelo distinta
e tem limites de uso próprios.

Durante a prévia de pesquisa, o Codex-Spark está disponível apenas para assinantes do ChatGPT Pro.

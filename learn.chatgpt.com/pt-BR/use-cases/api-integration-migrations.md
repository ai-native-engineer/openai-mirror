<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/api-integration-migrations -->

## Introdução

À medida que lançamos novos modelos e recursos da API, recomendamos atualizar sua integração para aproveitar as melhorias mais recentes.
Mudar de um modelo para outro muitas vezes não é tão simples quanto apenas atualizar o nome do modelo.

Pode haver alterações na API. No caso do modelo GPT-5.4, por exemplo, adicionamos um novo parâmetro `phase` à mensagem do assistente, e é importante incluí-lo na sua integração. O mais importante, porém, é que o comportamento do modelo pode ser diferente e exigir alterações nos prompts existentes.

Ao migrar para um novo modelo, certifique-se não apenas de fazer as alterações de código necessárias, mas também de avaliar o impacto nos seus fluxos de trabalho.

## Use a habilidade OpenAI Docs

A página [Orientações sobre modelos](/api/docs/guides/latest-model) reúne orientações sobre recursos da API, comportamento dos modelos, migração e criação de prompts para cada geração de modelos.

A habilidade OpenAI Docs também inclui [orientações específicas](https://github.com/openai/codex/blob/6323f0104d17d211029faab149231ba787f7da37/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-5p4.md) como referência prática para a migração. Para saber qual modelo adotar na atualização atual, use a página [Orientações sobre modelos](/api/docs/guides/latest-model).

Agora, o Codex já vem com a habilidade OpenAI Docs. Portanto, não deixe de mencioná-la no prompt para acessar toda a documentação e todas as orientações mais recentes ao desenvolver com a API da OpenAI.

## Crie um pipeline robusto de avaliações

O Codex pode atualizar automaticamente seus prompts com base nas orientações mais recentes para a criação de prompts, mas você deve ter uma forma de verificar automaticamente se sua integração está funcionando como esperado.

Certifique-se de criar um pipeline de avaliações que você possa executar sempre que fizer alterações na sua integração, para verificar se não houve regressão no comportamento.

Este [guia do Cookbook](/cookbook/examples/evaluation/building_resilient_prompts_using_an_evaluation_flywheel) explica em detalhes como fazer isso usando nossa [Evals API](/api/docs/guides/evals).

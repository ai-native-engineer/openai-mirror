<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/github-code-reviews -->

## Como usar

Comece adicionando a revisão de código do Codex à sua organização ou ao seu repositório no GitHub.
Consulte [Revisão de código do Codex no GitHub](/pt-BR/codex/third-party/github) para saber mais.

Você pode configurar o Codex para revisar automaticamente cada pull request ou solicitar uma revisão usando `@codex review` em um comentário no pull request.

Se o Codex sinalizar uma regressão ou um possível problema, você pode pedir que ele faça a correção comentando no pull request com um prompt de acompanhamento, como `@codex fix it`.

Isso iniciará um novo chat na nuvem que corrigirá o problema e atualizará o pull request.

## Defina diretrizes para a revisão

Para personalizar o que o Codex revisa, adicione uma seção `## Code Review Rules` ao
`AGENTS.md` mais próximo do código ao qual as regras se aplicam. Por exemplo:

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Coloque as regras válidas para todo o repositório no `AGENTS.md` da raiz e as regras específicas de cada serviço
em um arquivo aninhado. Escreva regras concisas que descrevam o comportamento que deve ser sinalizado e qualquer
alternativa segura ou exceção. Deixe as verificações de formatação e lint a cargo da CI. Consulte
[Como personalizar o que o Codex revisa](/pt-BR/codex/third-party/github#customize-what-codex-reviews)
para obter orientações de configuração e redação de regras.

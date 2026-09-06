<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/update-documentation -->

## Introdução

É mais fácil manter a documentação em dia quando ela é atualizada junto com as alterações no código-fonte, e não semanas depois. O Codex pode analisar código alterado, testes, notas de versão, issues vinculadas e o contexto da pull request para então elaborar uma atualização da documentação com escopo delimitado e alinhada à estrutura existente.

Use este fluxo de trabalho para documentação para desenvolvedores, atualizações de README, rascunhos do registro de alterações, notas de migração, runbooks ou qualquer outro conteúdo que precise acompanhar mudanças frequentes de comportamento.

## Como usar

1. Comece pela alteração que você precisa documentar.

   Compartilhe a branch, a pull request, o commit, a issue ou os arquivos. Se a documentação for pública, diga explicitamente que planos futuros ainda não publicados, detalhes privados de clientes e contexto exclusivo para uso interno devem ficar de fora.

2. Peça ao Codex para mapear a documentação afetada.

   Antes de criar o rascunho, peça que ele pesquise na documentação existente nomes de recursos, chaves de configuração, comandos, exemplos e termos relacionados.

3. Atualize apenas a parte necessária da documentação.

   O Codex deve preservar a estrutura atual da página, sua terminologia, seus links cruzados e seu frontmatter. Deve evitar reformulações amplas quando bastar uma observação pontual, um exemplo ou uma atualização de seção.

4. Verifique as alterações.

   Peça ao Codex para executar as verificações de formatação e de documentação adequadas ao repositório e depois resumir as evidências que sustentam cada afirmação voltada aos usuários.

## O que fornecer ao Codex

| Fonte                               | Como isso ajuda                                                               |
| ------------------------------------ | -------------------------------------------------------------------------- |
| Código e testes alterados               | Permite que o Codex analise o comportamento real para elaborar atualizações pontuais na documentação. |
| Notas de versão públicas ou documentação do produto | Ajuda o Codex a refletir corretamente a terminologia pública, a disponibilidade e o status do recurso.    |
| Contexto da pull request ou da issue        | Explica por que a alteração ocorreu e qual comportamento é relevante para os usuários.   |
| Verificações locais da documentação                    | Dá ao Codex critérios concretos de conclusão antes que a documentação seja publicada.   |

Adicionar mais contexto, como notas de versão públicas, ajuda o Codex a evitar a inclusão de informações privadas ou atualizações que ainda não são públicas.

## Torne o fluxo de trabalho repetível

Para definir uma convenção para todo o repositório, adicione ao [AGENTS.md](/pt-BR/codex/agent-configuration/agents-md) as expectativas relacionadas à documentação. Por exemplo:

```md
## Documentation

- When user-facing behavior changes, check whether docs, examples, or changelogs need updates.
- Public docs must only include public information or behavior visible in this repo.
- Preserve existing terminology and frontmatter.
- Run the docs formatting and build checks before final handoff.

Se o processo tiver mais etapas, transforme-o em uma [habilidade](/pt-BR/codex/build-skills) para que as tarefas futuras do Codex possam seguir o mesmo ciclo de verificação de fontes, elaboração e validação. Consulte [Salvar fluxos de trabalho como habilidades](/pt-BR/codex/use-cases/reusable-codex-skills) para saber mais sobre esse padrão.

Você também pode [agendar uma tarefa para este fluxo de trabalho diretamente no chat atual](/pt-BR/codex/automations#schedule-a-task-inside-a-chat). Por exemplo, peça ao Codex para buscar pull requests recentes no GitHub e manter a documentação atualizada toda semana:

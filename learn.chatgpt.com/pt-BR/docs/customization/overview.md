<!-- source: https://learn.chatgpt.com/pt-BR/docs/customization/overview -->

A personalização permite adaptar o Codex à forma como sua equipe trabalha.

No Codex, a personalização é composta por algumas camadas que atuam em conjunto:

- **Orientações do projeto (`AGENTS.md`)** para instruções persistentes
- **[Memórias](/pt-BR/codex/customization/memories)** para preservar o contexto útil obtido de trabalhos anteriores
- **Habilidades** para fluxos de trabalho reutilizáveis e conhecimento especializado no domínio
- **[MCP](/pt-BR/codex/extend/mcp)** para acessar ferramentas externas e sistemas compartilhados
- **[Subagentes](/pt-BR/codex/agent-configuration/subagents)** para delegar trabalho a subagentes especializados

Essas camadas se complementam, não competem entre si. `AGENTS.md` orienta o comportamento, as memórias
preservam o contexto local para uso futuro, as habilidades encapsulam processos repetíveis, e
[MCP](/pt-BR/codex/extend/mcp) conecta o Codex a sistemas fora do workspace local.

## Orientações do AGENTS.md

`AGENTS.md` fornece ao Codex orientações duradouras sobre o projeto que acompanham seu repositório e se aplicam antes que o agente comece a trabalhar. Mantenha-o enxuto.

Use-o para definir as regras que você quer que o Codex siga sempre em um repositório, como:

- Comandos de build e teste
- Expectativas de revisão
- convenções específicas do repositório
- Instruções específicas de cada diretório

Quando o agente fizer suposições incorretas sobre sua base de código, corrija-as em `AGENTS.md` e peça ao agente que atualize `AGENTS.md` para que a correção persista. Trate isso como um ciclo de feedback.

**Como atualizar `AGENTS.md`:** Comece apenas com as instruções essenciais. Registre como regras o feedback recorrente de revisões, coloque cada orientação no diretório mais próximo ao qual ela se aplica e peça ao agente que atualize `AGENTS.md` quando você corrigir algo, para que sessões futuras incorporem a correção.

### Quando atualizar `AGENTS.md`

- **Erros repetidos**: Se o agente cometer o mesmo erro repetidamente, adicione uma regra.
- **Leitura excessiva**: Se ele encontrar os arquivos certos, mas ler documentos demais, adicione instruções de direcionamento (quais diretórios/arquivos priorizar).
- **Feedback recorrente em PRs**: Se você der o mesmo feedback mais de uma vez, registre-o como regra.
- **No GitHub**: Em um comentário de pull request, marque `@codex` e faça uma solicitação (por exemplo, `@codex add this to AGENTS.md`) para delegar a atualização a um chat na nuvem.
- **Automatize verificações de divergência**: Use [tarefas agendadas](/pt-BR/codex/automations) para executar verificações recorrentes (por exemplo, todos os dias) que identifiquem lacunas nas orientações e sugiram o que adicionar a `AGENTS.md`.

Combine `AGENTS.md` com uma infraestrutura que aplique essas regras: hooks de pre-commit, linters e verificadores de tipos detectam problemas antes que você os veja, tornando o sistema mais eficaz na prevenção de erros recorrentes.

O Codex pode carregar orientações de vários locais: um arquivo global no diretório inicial do Codex (para você, como desenvolvedor) e arquivos específicos do repositório que as equipes podem versionar. Os arquivos mais próximos do diretório de trabalho têm precedência.
Use o arquivo global para definir como o Codex se comunica com você (por exemplo, estilo de revisão, nível de detalhamento e valores padrão) e mantenha os arquivos do repositório voltados às regras da equipe e da base de código.

[Instruções personalizadas com o AGENTS.md](/pt-BR/codex/agent-configuration/agents-md)

## Habilidades

As habilidades oferecem ao Codex recursos reutilizáveis para fluxos de trabalho repetíveis.
Em geral, as habilidades são a melhor opção para fluxos de trabalho reutilizáveis, pois aceitam instruções mais detalhadas, scripts e referências e podem ser reutilizadas em diferentes tarefas.
As habilidades são carregadas e ficam visíveis para o agente (pelo menos seus metadados), portanto o Codex pode descobri-las e selecioná-las implicitamente. Isso mantém fluxos de trabalho completos disponíveis sem sobrecarregar o contexto logo de início.

Use pastas de habilidades para criar e aprimorar fluxos de trabalho localmente. Se um plug-in
já existir para o fluxo de trabalho, instale-o primeiro para reutilizar uma configuração já validada. Quando
quiser distribuir seu próprio fluxo de trabalho entre equipes ou agrupá-lo com
conectores, empacote-o como um [plug-in](/pt-BR/codex/build-plugins). As habilidades continuam sendo o
formato de criação; os plug-ins são a unidade de distribuição instalável.

Uma habilidade geralmente consiste em um arquivo `SKILL.md` e, opcionalmente, scripts, referências e recursos.

O diretório da habilidade pode incluir uma pasta `scripts/` com scripts de CLI que o Codex executa como parte do fluxo de trabalho (por exemplo, para gerar dados iniciais ou executar validações). Quando o fluxo de trabalho precisar de sistemas externos (rastreadores de issues, ferramentas de design, servidores de documentação), combine a habilidade com o [MCP](/pt-BR/codex/extend/mcp).

Exemplo de `SKILL.md`:

```md
---
name: commit
description: Stage and commit changes in semantic groups. Use when the user wants to commit, organize commits, or clean up a branch before pushing.
---

1. Do not run `git add .`. Stage files in logical groups by purpose.
2. Group into separate commits: feat → test → docs → refactor → chore.
3. Write concise commit messages that match the change scope.
4. Keep each commit focused and reviewable.

Use habilidades para:

- Fluxos de trabalho repetíveis (etapas de lançamento, rotinas de revisão, atualizações da documentação)
- Conhecimento especializado da equipe
- Procedimentos que exigem exemplos, referências ou scripts auxiliares

As habilidades podem ser globais (no seu diretório de usuário, para você como desenvolvedor) ou específicas do repositório (versionadas em `.agents/skills`, para sua equipe). Coloque as habilidades do repositório em `.agents/skills` quando o fluxo de trabalho se aplicar a esse projeto; use seu diretório de usuário para as habilidades que você quer disponibilizar em todos os repositórios.

| Camada  | Global               | repositório                                           |
| :----- | :------------------- | :--------------------------------------------- |
| AGENTS | `~/.codex/AGENTS.md` | `AGENTS.md` na raiz do repositório ou em diretórios aninhados |
| Habilidades | `~/.agents/skills`   | `.agents/skills` no repositório                       |

O Codex carrega as habilidades de forma progressiva:

- Ele começa com os metadados (`name`, `description`) para descobrir as habilidades
- Ele só carrega `SKILL.md` quando uma habilidade é selecionada
- Ele só lê referências ou executa scripts quando necessário

As habilidades podem ser invocadas explicitamente, e o Codex também pode selecioná-las implicitamente quando a tarefa corresponder à descrição da habilidade. Descrições claras tornam o acionamento das habilidades mais confiável.

[Criar habilidades](/pt-BR/codex/build-skills)

## MCP

MCP (Model Context Protocol) é a forma padrão de conectar o Codex a ferramentas externas e provedores de contexto.
Ele é especialmente útil para sistemas hospedados remotamente, como Figma, Linear, GitHub ou serviços internos de conhecimento dos quais sua equipe depende.

Use o MCP quando o Codex precisar de recursos disponíveis fora do repositório local, como rastreadores de issues, ferramentas de design, navegadores ou sistemas compartilhados de documentação.

Uma forma de entender isso:

- **Host**: Codex
- **Cliente**: a conexão MCP dentro do Codex
- **Servidor**: a ferramenta externa ou o provedor de contexto

Os servidores MCP podem disponibilizar:

- **Ferramentas** (ações)
- **Recursos** (dados legíveis)
- **Prompts** (modelos reutilizáveis de prompt)

Essa separação ajuda a analisar os limites de confiança e de capacidade. Alguns servidores fornecem principalmente contexto, enquanto outros disponibilizam ações poderosas.

Na prática, o MCP costuma ser mais útil quando usado em conjunto com habilidades:

- Uma habilidade define o fluxo de trabalho e especifica quais ferramentas MCP usar

[Model Context Protocol](/pt-BR/codex/extend/mcp)

## Subagentes

Você pode criar agentes com funções diferentes e instruí-los a usar as ferramentas de maneiras distintas. Por exemplo, um agente pode executar testes com comandos e configurações específicos, enquanto outro conta com servidores MCP que recuperam logs de produção para depuração. Cada subagente mantém o foco e usa as ferramentas adequadas à sua tarefa.

[Subagentes](/pt-BR/codex/agent-configuration/subagents)

## Habilidades + MCP em conjunto

É ao combinar Habilidades e MCP que tudo se encaixa: as habilidades definem fluxos de trabalho repetíveis, e o MCP conecta esses fluxos a ferramentas e sistemas externos.
Se uma habilidade depender do MCP, declare essa dependência em `agents/openai.yaml` para que o Codex possa instalá-la e configurá-la automaticamente (consulte [Criar habilidades](/pt-BR/codex/build-skills)).

## Próxima etapa

Implemente nesta ordem:

1. [Instruções personalizadas com AGENTS.md](/pt-BR/codex/agent-configuration/agents-md) para que o Codex siga as convenções do seu repositório. Adicione hooks de pre-commit e linters para aplicar essas regras.
2. Instale um [plug-in](/pt-BR/codex/plugins) quando já existir um fluxo de trabalho reutilizável. Caso contrário, crie uma [habilidade](/pt-BR/codex/build-skills) e empacote-a como plug-in quando quiser compartilhá-la.
3. [MCP](/pt-BR/codex/extend/mcp) quando os fluxos de trabalho precisarem de sistemas externos (Linear, GitHub, servidores de documentação, ferramentas de design).
4. [Subagentes](/pt-BR/codex/agent-configuration/subagents) quando você estiver pronto para delegar a eles tarefas que geram muito ruído ou exigem especialização.

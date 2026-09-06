<!-- source: https://learn.chatgpt.com/pt-BR/guides/best-practices -->

Se você está começando a usar o Codex ou agentes de programação em geral, este guia ajudará você a obter resultados melhores mais rapidamente. Ele aborda os principais hábitos que tornam o Codex mais eficaz na [CLI](/pt-BR/codex/cli), na [extensão para IDE](/pt-BR/codex/ide) e no [aplicativo do ChatGPT para desktop](/pt-BR/codex/app), desde a criação de prompts e o planejamento até a validação, o MCP, as habilidades e as tarefas agendadas.

O Codex funciona melhor quando você o trata menos como um assistente para tarefas pontuais e mais como um colega de equipe que você configura e aprimora ao longo do tempo.

Uma forma útil de pensar nisso: comece com o contexto certo para a tarefa, use `AGENTS.md` para orientações persistentes, configure o Codex de acordo com seu fluxo de trabalho, conecte sistemas externos com o MCP, transforme tarefas recorrentes em habilidades e automatize fluxos de trabalho estáveis.

## Para começar bem: contexto e prompts

O Codex já é bastante eficaz mesmo quando seu prompt não é perfeito. Muitas vezes, você pode apresentar a ele um problema difícil com o mínimo de configuração e ainda assim obter um ótimo resultado. A clareza na [criação de prompts](/pt-BR/codex/prompting) não é indispensável para que o Codex seja útil, mas torna os resultados mais confiáveis, especialmente em bases de código maiores ou tarefas mais críticas.

Se você trabalha em um repositório grande ou complexo, o que mais faz diferença é fornecer ao Codex o contexto certo para a tarefa e uma estrutura clara do que deseja que seja feito.

Um bom ponto de partida é incluir quatro elementos no prompt:

- **Objetivo:** O que você está tentando alterar ou criar?
- **Contexto:** Quais arquivos, pastas, documentos, exemplos ou erros são relevantes para esta tarefa? Você pode mencionar determinados arquivos com @ para usá-los como contexto.
- **Restrições:** Quais padrões, diretrizes de arquitetura, requisitos de segurança ou convenções o Codex deve seguir?
- **Critérios de conclusão:** Quais condições devem ser atendidas para que a tarefa seja considerada concluída, como os testes passarem, o comportamento mudar ou um bug deixar de ser reproduzido?

Isso ajuda o Codex a permanecer dentro do escopo, fazer menos suposições e produzir um trabalho mais fácil de revisar.

Escolha um nível de raciocínio de acordo com a dificuldade da tarefa e teste o que funciona melhor no seu fluxo de trabalho. Configurações diferentes funcionam melhor para usuários e tarefas diferentes.

- Baixo para tarefas mais rápidas e de escopo bem definido
- Médio ou Alto para alterações mais complexas ou depuração
- Extra alto para tarefas longas, agênticas e que exigem muito raciocínio

  Para fornecer contexto mais rapidamente, experimente usar o ditado por voz no aplicativo do ChatGPT
para desktop para ditar o que deseja que o Codex faça, em vez de digitar.

## Em tarefas difíceis, planeje primeiro

Se a tarefa for complexa, ambígua ou difícil de descrever com clareza, peça ao Codex que faça um plano antes de começar a programar.

Algumas abordagens funcionam bem:

**Use o Modo planejamento:** Para a maioria dos usuários, esta é a opção mais simples e eficaz. O Modo planejamento permite que o Codex reúna contexto, faça perguntas de esclarecimento e elabore um plano mais sólido antes da implementação. Para alternar o modo, use `/plan` ou <kbd>Shift</kbd>+<kbd>Tab</kbd>.

**Peça ao Codex que entreviste você:** Se você tem uma ideia geral do que deseja, mas não sabe bem como descrevê-la, peça primeiro ao Codex que faça perguntas. Diga a ele que questione suas suposições e transforme a ideia ainda vaga em algo concreto antes de escrever código.

**Use um modelo PLANS.md:** Em fluxos de trabalho mais avançados, você pode configurar o Codex para seguir um modelo `PLANS.md` ou um modelo de plano de execução em tarefas de longa duração ou com várias etapas. Para saber mais, consulte o [guia de planos de execução](/cookbook/articles/codex_exec_plans).

## Torne as orientações reutilizáveis com `AGENTS.md`

Quando você encontrar um padrão de criação de prompts que funcione, a próxima etapa é deixar de repeti-lo manualmente. É aí que entra o [AGENTS.md](/pt-BR/codex/agent-configuration/agents-md).

Pense no `AGENTS.md` como um README em formato aberto para agentes. Ele é carregado automaticamente no contexto e é o melhor lugar para registrar como você e sua equipe querem que o Codex trabalhe em um repositório.

Um bom `AGENTS.md` abrange:

- estrutura do repositório e diretórios importantes
- Como executar o projeto
- Comandos de build, teste e lint
- Convenções de engenharia e expectativas para PRs
- Restrições e regras sobre o que não fazer
- Critérios de conclusão e como verificar o trabalho

O comando de barra `/init` na CLI permite começar rapidamente criando um `AGENTS.md` inicial no diretório atual. É um ótimo ponto de partida, mas você deve editar o resultado para refletir como sua equipe realmente compila, testa, revisa e entrega código.

Você pode criar arquivos `AGENTS.md` em diferentes níveis: um `AGENTS.md` global para orientações pessoais padrão, localizado em `~/.codex`; um arquivo no nível do repositório para padrões compartilhados; e arquivos mais específicos em subdiretórios, para regras locais. Se houver um arquivo mais específico e mais próximo do diretório atual, as orientações desse arquivo prevalecem.

Seja prático. Um `AGENTS.md` curto e preciso é mais útil do que um arquivo longo repleto de regras vagas. Comece pelo básico e só adicione novas regras quando perceber erros recorrentes.

Se o `AGENTS.md` começar a ficar grande demais, mantenha o arquivo principal conciso e faça referência a arquivos Markdown específicos de cada tarefa para assuntos como planejamento, revisão de código ou arquitetura.

  Quando o Codex cometer o mesmo erro duas vezes, peça uma retrospectiva e atualize
`AGENTS.md`. Assim, as orientações continuam práticas e baseadas em dificuldades reais.

## Configure o Codex para manter a consistência

A configuração é uma das principais formas de tornar o comportamento do Codex mais consistente entre sessões e interfaces. Por exemplo, você pode definir valores padrão para a escolha do modelo, o esforço de raciocínio, o modo sandbox, a política de aprovação, os perfis e a configuração do MCP.

Um bom ponto de partida é:

- Mantenha suas preferências padrão em `~/.codex/config.toml` (**Configurações \> Configuração \> Abrir config.toml** no aplicativo do ChatGPT para desktop)
- Mantenha as configurações específicas do repositório em `.codex/config.toml`
- Use a linha de comando para substituir configurações apenas em situações pontuais (se você usa a CLI)

No [`config.toml`](/pt-BR/codex/config-file/config-basic), você define preferências persistentes, como servidores MCP, configuração de vários agentes e sinalizadores de recursos. As substituições específicas de cada perfil ficam em arquivos `$CODEX_HOME/profile-name.config.toml` separados.

O Codex já vem com ambiente isolado em nível operacional e oferece dois controles principais que você pode ajustar. O modo de aprovação determina quando o Codex pede sua permissão para executar um comando, e o modo sandbox determina se o Codex pode ler ou gravar no diretório e quais arquivos o agente pode acessar.

Se você está começando a usar agentes de programação, comece com as permissões padrão. Mantenha as configurações de aprovação e ambiente isolado restritivas por padrão e só amplie as permissões para repositórios confiáveis ou fluxos de trabalho específicos quando houver uma necessidade clara.

Vale observar que a CLI, a extensão para IDE e o aplicativo do ChatGPT para desktop compartilham as mesmas camadas de configuração. Saiba mais na página de [exemplo de configuração](/pt-BR/codex/config-file/config-sample).

  Configure o Codex desde cedo para seu ambiente real. Muitos problemas de qualidade são
na verdade problemas de configuração, como diretório de trabalho incorreto, falta de acesso de gravação,
valores padrão de modelo incorretos ou ausência de ferramentas e conectores.

## Melhore a confiabilidade com testes e revisão

Não se limite a pedir que o Codex faça uma alteração. Peça também que crie testes quando necessário, execute as verificações relevantes, confirme o resultado e revise o trabalho antes de aceitá-lo.

O Codex pode executar esse ciclo por você, mas apenas se souber o que é considerado “bom”. Essa orientação pode vir do prompt ou do `AGENTS.md`.

Isso pode incluir:

- Criar ou atualizar testes para a alteração
- Executar as suítes de testes corretas
- Executar verificações de lint, formatação ou tipos
- Confirmar que o comportamento final corresponde à solicitação
- Revisar o diff em busca de bugs, regressões ou padrões de risco

  Alterne a exibição do painel de diff no aplicativo do ChatGPT para desktop para [revisar
  alterações](/pt-BR/codex/code-review?surface=app) diretamente no ambiente local. Clique em uma linha específica para
  enviar feedback, que será usado como contexto na próxima interação do Codex.

Uma opção útil aqui é o comando de barra `/review`, que oferece algumas formas de revisar código:

- Revisar em relação a uma branch base, no estilo de PR
- Revisar alterações sem commit
- Revisar um commit
- Usar instruções de revisão personalizadas

Se você e sua equipe tiverem um arquivo `code_review.md` e fizerem referência a ele em `AGENTS.md`, o Codex também poderá seguir essas orientações durante a revisão. Esse é um padrão eficaz para equipes que desejam manter as revisões consistentes entre repositórios e colaboradores.

O Codex não deve apenas gerar código. Com as instruções certas, ele também pode ajudar a **testar, verificar e revisar esse código**.

Se você usa o GitHub Cloud, pode configurar o Codex para executar [revisões de código em seus PRs](/pt-BR/codex/third-party/github). Na OpenAI, o Codex revisa 100% dos PRs. Você pode ativar revisões automáticas ou fazer com que o Codex revise sob demanda quando você mencionar @Codex.

## Use servidores MCP para obter contexto externo

Use servidores MCP quando o contexto de que o Codex precisa estiver fora do repositório. Assim, o Codex pode se conectar às ferramentas e aos sistemas que você já usa, sem que você precise ficar copiando e colando informações atualizadas nos prompts.

[Model Context Protocol](/pt-BR/codex/extend/mcp), ou MCP, é um padrão aberto para conectar o Codex a ferramentas e sistemas externos.

Use o MCP quando:

- O contexto necessário está fora do repositório
- Os dados mudam com frequência
- Você quer que o Codex use uma ferramenta em vez de depender de instruções copiadas e coladas
- Você precisa de uma integração que possa ser reproduzida entre usuários ou projetos

O Codex oferece suporte a servidores STDIO e Streamable HTTP com OAuth.

No aplicativo para desktop do ChatGPT, acesse **Configurações \> Servidores MCP** para ver os servidores personalizados e recomendados. Muitas vezes, o Codex pode ajudar você a instalar os servidores necessários. Basta pedir. Também é possível usar o comando `codex mcp add` na CLI para adicionar seus servidores personalizados com nome, URL e outros detalhes.

  Adicione ferramentas somente quando elas viabilizarem um fluxo de trabalho real. Não comece integrando
todas as ferramentas que você usa. Comece com uma ou duas ferramentas que eliminem de fato um ciclo manual
que você já executa com frequência e, depois, amplie a partir daí.

## Transforme fluxos de trabalho repetíveis em habilidades

Quando um fluxo de trabalho se tornar repetível, pare de depender de prompts longos ou de trocas repetidas de mensagens. Use uma [habilidade](/pt-BR/codex/build-skills) para reunir em um arquivo `SKILL.md` as instruções, o contexto e a lógica auxiliar que o Codex deve aplicar de forma consistente. As habilidades funcionam na CLI, na extensão para IDE e no aplicativo para desktop do ChatGPT.

Mantenha cada habilidade restrita a uma única tarefa. Comece com 2 ou 3 casos de uso concretos, defina entradas e saídas claras e escreva uma descrição que explique o que a habilidade faz e quando deve ser usada. Inclua os tipos de frase de acionamento que um usuário realmente diria.

Não tente abranger todos os casos extremos logo de início. Comece com uma tarefa representativa, faça-a funcionar bem, depois transforme esse fluxo de trabalho em uma habilidade e continue aprimorando-a. Inclua scripts ou recursos adicionais somente quando aumentarem a confiabilidade.

Uma boa regra prática: se você continuar reutilizando o mesmo prompt ou corrigindo o mesmo fluxo de trabalho, provavelmente deverá transformá-lo em uma habilidade.

As habilidades são especialmente úteis para tarefas recorrentes como:

- Triagem de logs
- Elaboração de notas de versão
- Revisão de PR com base em uma lista de verificação
- Planejamento de migrações
- Resumos de telemetria ou de incidentes
- Fluxos padrão de depuração

A habilidade `$skill-creator` é o melhor ponto de partida para criar a estrutura da primeira versão de uma habilidade. Mantenha a primeira versão local enquanto faz ajustes. Quando ela estiver pronta para ser compartilhada de forma ampla, empacote-a como um [plug-in](https://developers.openai.com/plugins/build/plugins). Uma das partes mais importantes de uma habilidade é a descrição. Ela deve indicar o que a habilidade faz e quando deve ser usada.

  As habilidades pessoais são armazenadas em `$HOME/.agents/skills`, e as habilidades compartilhadas com a equipe
  podem ser versionadas em `.agents/skills` dentro de um repositório. Isso é especialmente
  útil para integrar novos membros à equipe.

## Use tarefas agendadas para trabalhos recorrentes

Quando um fluxo de trabalho estiver estável, você poderá agendar sua execução em segundo plano pelo Codex. No aplicativo para desktop do ChatGPT, as [tarefas agendadas](/pt-BR/codex/automations) permitem escolher o projeto, o prompt, a frequência e o ambiente de execução para trabalhos recorrentes.

Crie uma tarefa agendada na página **Agendadas**. Escolha o projeto, o prompt,
a frequência e se a tarefa será executada em uma árvore de trabalho dedicada do Git ou em seu ambiente
local. O prompt pode invocar habilidades. Saiba mais sobre
[árvores de trabalho do Git](/pt-BR/codex/environments/git-worktrees).

Boas opções incluem:

- Resumir commits recentes
- Buscar possíveis bugs
- Elaborar notas de versão
- Verificar falhas de CI
- Produzir resumos de stand-up
- Executar periodicamente fluxos de análise repetíveis

Uma regra útil é: as habilidades definem o método, enquanto as tarefas agendadas definem o cronograma. Se um fluxo de trabalho ainda precisar de muita orientação, transforme-o primeiro em uma habilidade. Quando ele se tornar previsível, agendá-lo poderá economizar tempo.

  Use tarefas agendadas para análise retrospectiva e manutenção, não apenas para execução. Revise
chats recentes, resuma dificuldades recorrentes e aprimore prompts, instruções
ou a configuração dos fluxos de trabalho ao longo do tempo.

<a id="organize-long-running-tasks"></a>

## Organize chats de longa duração

Os chats acumulam contexto, decisões e ações ao longo do tempo, por isso gerenciá-los bem tem grande impacto na qualidade.

No aplicativo para desktop do ChatGPT, você pode fixar chats e criar árvores de trabalho. Se usar a
CLI, estes [comandos de barra](/codex/developer-commands?surface=cli) serão especialmente úteis:

- `/experimental` para ativar ou desativar recursos experimentais e adicioná-los ao seu `config.toml`
- `/resume` para retomar um chat salvo
- `/fork` para criar um novo chat preservando a transcrição original
- `/compact` quando o chat começar a ficar longo e você quiser uma versão resumida do contexto anterior. O Codex também compacta os chats automaticamente
- `/agent` quando você estiver executando agentes em paralelo e quiser alternar entre as threads dos agentes ativos
- `/theme` para escolher um tema de realce de sintaxe
- `/apps` para usar Apps do ChatGPT diretamente no Codex
- `/status` para inspecionar o estado atual da sessão

Mantenha um chat para cada unidade coerente de trabalho. Se o trabalho ainda fizer parte do mesmo
problema, permanecer no mesmo chat costuma ser melhor porque preserva a
linha de raciocínio. Crie um fork somente quando o trabalho realmente se ramificar.

  Use os fluxos de trabalho de [subagentes](/pt-BR/codex/agent-configuration/subagents) do Codex para
  delegar tarefas de escopo delimitado, liberando a thread principal. Mantenha o agente principal concentrado no
  problema central e use subagentes para tarefas como exploração, testes ou triagem.

## Erros comuns

Alguns erros comuns que você deve evitar ao começar a usar o Codex:

- Sobrecarregar o prompt com regras persistentes em vez de colocá-las em `AGENTS.md` ou em uma habilidade
- Não permitir que o agente verifique o próprio trabalho por não fornecer detalhes sobre a melhor forma de executar os comandos de build e teste
- Pular o planejamento em tarefas complexas e com várias etapas
- Dar ao Codex permissão total para acessar seu computador antes de entender o fluxo de trabalho
- Executar tarefas em paralelo nos mesmos arquivos sem usar árvores de trabalho do Git
- Agendar uma tarefa recorrente antes de ela funcionar de forma confiável quando executada manualmente
- Tratar o Codex como algo que você precisa acompanhar passo a passo, em vez de usá-lo em paralelo ao seu próprio trabalho
- Usar um único chat para um projeto inteiro, em vez de um chat para cada resultado coerente. Isso acumula contexto desnecessário e piora os resultados ao longo do tempo

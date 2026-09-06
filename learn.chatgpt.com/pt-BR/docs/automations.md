<!-- source: https://learn.chatgpt.com/pt-BR/docs/automations -->

Agende tarefas recorrentes para serem executadas em segundo plano. No ChatGPT na Web e em dispositivos móveis,
os planos elegíveis também permitem executar tarefas em resposta a eventos compatíveis de aplicativos. Analise as tarefas ativas,
pausadas e concluídas e as execuções recentes em **Agendadas**. Você pode combinar
tarefas agendadas com [habilidades](/pt-BR/codex/build-skills) para atividades mais complexas.

No aplicativo do ChatGPT para desktop, as tarefas agendadas podem trabalhar com projetos locais e
ser executadas no diretório do projeto ou em uma árvore de trabalho isolada. Mantenha o computador ligado e
o aplicativo em execução quando uma tarefa agendada precisar de arquivos locais.

Quando as tarefas agendadas estiverem ativadas no seu workspace, crie-as pelo Chat ou
pelo ChatGPT Work na Web e gerencie as execuções em **Agendadas**. As tarefas na Web
podem usar o contexto enviado e ferramentas conectadas, mas não podem trabalhar diretamente em
uma pasta no seu computador.

A Codex CLI não oferece a interface de gerenciamento da seção Agendadas. Use o ChatGPT na Web
ou o aplicativo para desktop para criar e gerenciar tarefas agendadas. A CLI pode ajudar você
a preparar e testar com antecedência um prompt, uma habilidade ou um script.

A extensão para IDE não oferece a interface de gerenciamento da seção Agendadas. Use
o ChatGPT na Web ou o aplicativo para desktop para criar e gerenciar tarefas agendadas. A extensão para IDE
pode ajudar você a preparar e testar um prompt, uma habilidade ou uma alteração no workspace
com antecedência.

<a id="managing-tasks"></a>
<a id="ask-codex-to-create-or-update-automations"></a>
<a id="ask-chatgpt-to-create-or-update-scheduled-tasks"></a>
<a id="thread-automations"></a>
<a id="scheduled-tasks-in-threads"></a>
<a id="scheduled-tasks-in-chats"></a>
<a id="schedule-work-from-a-task"></a>
<a id="schedule-a-task-inside-a-chat"></a>
<a id="test-automations"></a>
<a id="test-scheduled-tasks"></a>
<a id="worktree-cleanup-for-automations"></a>
<a id="worktree-cleanup-for-scheduled-tasks"></a>
<a id="permissions-and-security-model"></a>
<a id="examples"></a>
<a id="automatically-create-new-skills"></a>
<a id="stay-up-to-date-with-your-project"></a>
<a id="combining-automations-with-skills-to-fix-your-own-bugs"></a>
<a id="combining-scheduled-tasks-with-skills-to-fix-your-own-bugs"></a>

## Gerenciar tarefas agendadas na Web

Abra **Agendadas** para analisar o status das tarefas e as execuções recentes. Use uma tarefa agendada independente
quando cada execução precisar começar pelo prompt salvo. Use uma tarefa agendada em uma
conversa quando quiser que o ChatGPT retorne à mesma conversa com o contexto
existente.

As tarefas agendadas na Web podem usar arquivos enviados, ferramentas conectadas, habilidades e
plug-ins disponíveis para essa conversa. Elas não mantêm uma pasta local ou
árvore de trabalho disponível entre as execuções. Inclua no prompt da tarefa
ou em uma habilidade anexada instruções que continuem válidas e mantenha o material de origem necessário em um
projeto, arquivo enviado ou serviço conectado que esteja acessível.

Antes de agendar uma tarefa, teste o prompt em uma conversa normal na Web.
Analise as primeiras execuções e depois ajuste o prompt, as ferramentas ou a frequência caso os
resultados sejam abrangentes demais ou precisem de mais contexto.

## Acionar tarefas por eventos de aplicativos

Nos planos elegíveis, as tarefas agendadas podem ser executadas quando ocorre um evento compatível do Gmail, do Slack ou do
GitHub. As tarefas acionadas por eventos estão disponíveis no ChatGPT na Web
e em dispositivos móveis. Elas não estão disponíveis no aplicativo do ChatGPT para desktop, na Codex CLI ou na
extensão para IDE.

Peça ao ChatGPT para criar a tarefa e descreva o evento a monitorar e o que
fazer quando ele ocorrer. O gatilho determina quando a tarefa é executada; o prompt
salvo determina o que cada execução faz. Uma tarefa pode usar vários gatilhos de eventos,
mas não pode combiná-los com uma programação baseada em horários.

Os gatilhos de eventos compatíveis incluem:

- **Gmail:** Novas mensagens recebidas, com filtros opcionais por remetente ou assunto.
- **Slack:** Novas mensagens nos canais selecionados, com filtros opcionais por autor
  e pela inclusão ou não de respostas em conversas. Não há suporte a reações, edições, exclusões ou
  mensagens diretas.
- **GitHub:** Atividade de pull requests em um repositório. Filtre por pull request,
  autor, título ou rótulo e escolha se revisões, comentários, atualizações de commits
  ou apenas mesclagens devem acionar a tarefa.

Conecte e autorize o aplicativo antes de criar a tarefa. No Slack, adicione
`@ChatGPT` a cada canal que a tarefa monitora. No GitHub, o aplicativo conectado
precisa ter acesso ao repositório.

Quando vários eventos correspondentes chegam em um curto intervalo, o ChatGPT pode agrupá-los
em uma única execução. Abra **Agendadas** para analisar os eventos pendentes ou escolha **Executar agora**
para processá-los.

A disponibilidade depende do seu plano e das configurações do workspace. Em workspaces
gerenciados, os administradores podem controlar o acesso com a permissão **Permitir tarefas agendadas
acionadas por eventos** .

Por exemplo, agende uma tarefa para avaliar erros de telemetria e enviar correções,
ou para criar relatórios sobre alterações recentes na base de código. Para trabalhos contínuos que
devem continuar usando o mesmo contexto, [agende uma tarefa em uma conversa existente](#schedule-a-task-inside-a-chat).

Para tarefas agendadas com escopo de projeto, mantenha o computador ligado e o aplicativo do ChatGPT
para desktop em execução. O projeto selecionado precisa continuar disponível no disco quando
chegar o horário agendado para executar a tarefa.

Em repositórios Git, você pode escolher se uma tarefa agendada será executada no seu
projeto local ou em uma nova [árvore de trabalho](/pt-BR/codex/environments/git-worktrees). Nos dois casos, a execução ocorre em
segundo plano. As árvores de trabalho mantêm as alterações das tarefas agendadas separadas do trabalho local
inacabado, enquanto a execução no projeto local pode modificar arquivos nos quais você ainda está
trabalhando. Em projetos sem controle de versão, as tarefas agendadas são executadas diretamente no
diretório do projeto.

Você também pode manter as configurações padrão do modelo e do esforço de raciocínio ou
escolhê-los explicitamente para ter mais controle sobre a execução da tarefa agendada.

Se uma tarefa agendada usa `gpt-5.4` ou `gpt-5.4-mini` com login do ChatGPT,
atualize-a antes que esses modelos sejam descontinuados em 31 de agosto de 2026. Substitua `gpt-5.4` por
`gpt-5.6-terra` e `gpt-5.4-mini` por `gpt-5.6-luna`.

  

As tarefas agendadas são executadas sem supervisão com suas configurações padrão do Sandbox. Comece com o
nível de acesso mais restrito que permita concluir a tarefa e conceda acesso à rede ou acesso mais amplo aos arquivos
somente quando necessário. [Entenda o ambiente isolado](/pt-BR/codex/sandboxing).

## Gerenciar tarefas agendadas

Encontre todas as tarefas agendadas e suas execuções em **Agendadas** , na barra lateral
do aplicativo do ChatGPT para desktop.

A tela **Agendadas** funciona como sua caixa de entrada. As execuções de tarefas agendadas com resultados
aparecem nela, e um indicador de item não lido sinaliza quando uma execução precisa da sua atenção.

  

As tarefas agendadas independentes iniciam uma nova conversa a cada execução agendada e apresentam
os resultados em **Agendadas**. Use-as quando cada execução precisar ser independente ou quando uma única
tarefa agendada precisar ser executada em um ou mais projetos. Se precisar de uma
frequência personalizada, use os controles de programação personalizada. Para uma programação avançada, edite sua
regra de recorrência RFC 5545 (RRULE), como
`RRULE:FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0`.

Em repositórios Git, cada tarefa agendada pode ser executada no seu projeto local ou
em uma [árvore de trabalho](/pt-BR/codex/environments/git-worktrees) exclusiva para execução em segundo plano. Use
árvores de trabalho quando quiser isolar as alterações da tarefa agendada do trabalho local
inacabado. Use o modo local quando quiser que a tarefa agendada trabalhe diretamente na sua cópia
de trabalho principal, lembrando que ela pode alterar arquivos que você está editando ativamente.
Em projetos sem controle de versão, as tarefas agendadas são executadas diretamente no
diretório do projeto. Você pode executar a mesma tarefa agendada em mais de um projeto.

As tarefas agendadas criadas com o ChatGPT Work na Web, ou com o ChatGPT Work ou
o Codex no aplicativo para desktop, podem usar plug-ins. As tarefas agendadas também podem usar habilidades.
Para facilitar a manutenção e o compartilhamento das tarefas agendadas entre equipes, use
[habilidades](/pt-BR/codex/build-skills) para definir a ação e fornecer ferramentas e contexto.
Selecione ou invoque uma habilidade específica no prompt da tarefa quando o fluxo de trabalho não deva
depender da seleção automática de ferramentas.

## Peça ao ChatGPT para criar ou atualizar tarefas agendadas

Você pode criar e atualizar tarefas agendadas em uma conversa do ChatGPT ou do Codex.
Descreva o trabalho, quando ele deve ser executado e se cada execução deve retornar à
conversa atual ou iniciar uma nova conversa. O ChatGPT pode elaborar o prompt, escolher o
destino adequado e atualizar a tarefa quando o escopo ou a frequência
mudar.

Por exemplo, peça ao ChatGPT para agendar um acompanhamento na conversa atual enquanto uma
implantação termina ou para criar uma tarefa agendada independente que verifique
um projeto em intervalos recorrentes.

As habilidades também podem criar ou atualizar tarefas agendadas. Por exemplo, uma habilidade para
acompanhar uma pull request poderia configurar uma tarefa agendada que verifique o
status da PR com o plug-in do GitHub e faça correções com base em novos comentários de revisão.

## Agendar uma tarefa em uma conversa

Agende uma tarefa em uma conversa existente quando quiser que o ChatGPT retorne a essa conversa
de acordo com a programação. A tarefa agendada usa o contexto já existente da conversa, em vez de
começar com um novo prompt a cada vez.

As tarefas agendadas em uma conversa podem usar intervalos em minutos para ciclos ativos de acompanhamento
ou programações diárias e semanais quando você precisar de uma verificação em um horário
específico.

Agende uma tarefa em uma conversa para:

- verificar uma operação de longa duração até que seja concluída
- consultar uma fonte conectada em intervalos fixos quando você precisar de um registro periódico
do estado, em vez de uma resposta a um evento compatível de aplicativo
- lembrar o ChatGPT de continuar um ciclo de revisão em intervalos fixos
- executar um fluxo de trabalho orientado por uma habilidade que usa plug-ins, como verificar o status da PR
e tratar novos comentários
- continuar uma conversa de pesquisa ou triagem em andamento sem perder o contexto

Use uma tarefa agendada independente quando cada execução precisar ser independente ou quando
os resultados precisarem aparecer como execuções separadas em **Agendadas**.

Ao agendar uma tarefa em uma conversa, formule um prompt que continue válido. Ele deve descrever
o que o ChatGPT deve fazer em cada execução agendada, como decidir se há
algo importante a relatar e quando parar ou pedir sua orientação.

## Testar tarefas agendadas

Antes de agendar uma tarefa, teste o prompt manualmente em uma conversa normal.
Isso ajuda você a confirmar:

- O prompt está claro e com o escopo definido corretamente.
- O modelo, o esforço de raciocínio e as ferramentas selecionados ou usados por padrão funcionam como esperado.
- O resultado gerado pode ser revisado.

Quando começar a agendar execuções, analise os primeiros resultados e ajuste o
prompt ou a frequência conforme necessário.

No aplicativo do ChatGPT para desktop, você pode acionar explicitamente uma habilidade no prompt de uma tarefa
agendada usando `$skill-name`.

## Limpeza de árvores de trabalho usadas por tarefas agendadas

Se você escolher árvores de trabalho para repositórios Git, programações frequentes podem criar
muitas árvores de trabalho ao longo do tempo. Arquive as execuções agendadas de que não precisa mais e evite
fixar execuções, a menos que pretenda manter as árvores de trabalho delas.

## Permissões e modelo de segurança

As tarefas agendadas são executadas sem supervisão e usam suas configurações padrão do Sandbox.

Para uma explicação em linguagem simples sobre esses limites, consulte a
[visão geral do ambiente isolado](/pt-BR/codex/sandboxing). Para conhecer as regras do sistema de arquivos e da rede,
consulte [Permissões](/pt-BR/codex/permissions).

- Se o modo do Sandbox for **somente leitura**, as chamadas de ferramentas falham se exigirem
  alterar arquivos, acessar a rede ou usar aplicativos no seu computador.
  Considere alterar as configurações do Sandbox para gravação no workspace.
- Se o modo do Sandbox for **workspace-write**, as chamadas de ferramentas falham se exigirem
  alterar arquivos fora do workspace, acessar a rede ou usar aplicativos
  no seu computador. Você pode permitir seletivamente a execução de comandos fora do
  Sandbox usando [regras](/pt-BR/codex/agent-configuration/rules).
- Se o modo do Sandbox for **acesso completo**, as tarefas agendadas em segundo plano apresentam
  risco elevado, pois o ChatGPT pode alterar arquivos, executar comandos e acessar a rede
  sem perguntar. Considere alterar as configurações do Sandbox para gravação no workspace e
  usar [regras](/pt-BR/codex/agent-configuration/rules) para definir seletivamente quais comandos o agente
  pode executar com acesso completo.

Se você estiver em um ambiente gerenciado, os administradores podem restringir esses comportamentos por meio de
requisitos impostos por administradores. Por exemplo, podem proibir `approval_policy =
"never"` ou restringir os modos do Sandbox permitidos. Consulte
[Requisitos impostos por administradores (`requirements.toml`)](/pt-BR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

As tarefas agendadas usam `approval_policy = "never"` quando a política da sua organização
permite. Se os requisitos impostos por administradores proibirem `approval_policy = "never"`,
as tarefas agendadas passam a seguir o comportamento de aprovação do modo de permissão
selecionado.

## Exemplos

### Crie novas habilidades automaticamente

```markdown
Scan all of the `~/.codex/sessions` files from the past day and if there have been any issues using particular skills, update the skills to be more helpful. Personal skills only, no repo skills.

If there’s anything we’ve been doing often and struggle with that we should save as a skill to speed up future work, let’s do it.

Definitely don't feel like you need to update any- only if there's a good reason!

Let me know if you make any.

### Mantenha-se atualizado sobre seu projeto

```markdown
Look at the latest remote origin/master or origin/main . Then produce an exec briefing for the last 24 hours of commits that touch 

Formatting + structure:

- Use rich Markdown (H1 workstream sections, italics for the subtitle, horizontal rules as needed).
- Preamble can read something like “Here’s the last 24h brief for <directory>:”
- Subtitle should read: “Narrative walkthrough with owners; grouped by workstream.”
- Group by workstream rather than listing each commit. Workstream titles should be H1.
- Write a short narrative per workstream that explains the changes in plain language.
- Use bullet points and bolding when it makes things more readable
- Feel free to make bullets per person, but bold their name

Content requirements:

- Include PR links inline (e.g., [#123](...)) without a “PRs:” label.
- Do NOT include commit hashes or a “Key commits” section.
- It’s fine if multiple PRs appear under one workstream, but avoid per‑commit bullet lists.

Scope rules:

- Only include changes within the current cwd (or main checkout equivalent)
- Only include the last 24h of commits.
- Use `gh` to fetch PR titles and descriptions if it helps.
  Also feel free to pull PR reviews and comments

### Combine tarefas agendadas com habilidades para corrigir seus próprios bugs

Crie uma nova habilidade `$recent-code-bugfix` que tente corrigir um bug introduzido pelos seus próprios commits e [salve-a nas suas habilidades pessoais](/pt-BR/codex/build-skills#where-to-save-skills).

```markdown
---
name: recent-code-bugfix
description: Find and fix a bug introduced by the current author within the last week in the current working directory. Use when a user wants a proactive bugfix from their recent changes, when the prompt is empty, or when asked to triage/fix issues caused by their recent commits. Root cause must map directly to the author’s own changes.
---

# Recent Code Bugfix

## Overview

Find a bug introduced by the current author in the last week, implement a fix, and verify it when possible. Operate in the current working directory, assume the code is local, and ensure the root cause is tied directly to the author’s own edits.

## Workflow

### 1) Establish the recent-change scope

Use Git to identify the author and changed files from the last week.

- Determine the author from `git config user.name`/`user.email`. If unavailable, use the current user’s name from the environment or ask once.
- Use `git log --since=1.week --author=<author>` to list recent commits and files. Focus on files touched by those commits.
- If the user’s prompt is empty, proceed directly with this default scope.

### 2) Find a concrete failure tied to recent changes

Prioritize defects that are directly attributable to the author’s edits.

- Look for recent failures (tests, lint, runtime errors) if logs or CI outputs are available locally.
- If no failures are provided, run the smallest relevant verification (single test, file-level lint, or targeted repro) that touches the edited files.
- Confirm the root cause is directly connected to the author’s changes, not unrelated legacy issues. If only unrelated failures are found, stop and report that no qualifying bug was detected.

### 3) Implement the fix

Make a minimal fix that aligns with project conventions.

- Update only the files needed to resolve the issue.
- Avoid adding extra defensive checks or unrelated refactors.
- Keep changes consistent with local style and tests.

### 4) Verify

Attempt verification when possible.

- Prefer the smallest validation step (targeted test, focused lint, or direct repro command).
- If verification cannot be run, state what would be run and why it wasn’t executed.

### 5) Report

Summarize the root cause, the fix, and the verification performed. Make it explicit how the root cause ties to the author’s recent changes.

Depois, crie uma nova tarefa agendada:

```markdown
Check my commits from the last 24h and submit a $recent-code-bugfix.

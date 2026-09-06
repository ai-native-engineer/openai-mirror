<!-- source: https://learn.chatgpt.com/pt-BR/docs/sandboxing/auto-review -->

A Revisão automática substitui a aprovação manual no limite do sandbox por um
agente revisor separado. O agente principal do Codex continua em execução no mesmo sandbox, com
a mesma política de aprovação e os mesmos limites de rede e sistema de arquivos. A
diferença está em quem analisa as solicitações de escalonamento elegíveis.

  A Revisão automática só se aplica quando as aprovações são interativas. Na prática, isso
  significa usar `approval_policy = "on-request"` ou uma política de aprovação granular que
  ainda exiba a categoria de prompt relevante. Com `approval_policy = "never"`,
  não há nada para revisar.

No aplicativo do ChatGPT para desktop, selecionar um modelo Daybreak aprovado
muda automaticamente o controle de permissões para **Aprovar por mim** quando esse
modo estiver disponível para sua conta e for permitido pela política da organização. Isso
também ocorre quando você usa o comando `/model` do aplicativo para desktop. Se esse modo
não estiver disponível, o modo de permissão atual permanecerá inalterado. A seleção do modelo
nunca substitui os requisitos gerenciados da organização.

Antes de ativar o **Acesso completo** para um modelo de segurança aprovado, o
aplicativo do ChatGPT para desktop exibe um aviso específico do modelo sobre ações perigosas. O
aviso recomenda usar **Aprovar por mim** em vez disso e inclui um link para a
[configuração da política do revisor](#configuration). O aviso não restaura
o limite do sandbox nem substitui a política da organização.

## Como funciona a Revisão automática

Em linhas gerais, o fluxo funciona assim:

1. O agente principal opera em `read-only` ou `workspace-write`.
2. Quando precisa ultrapassar o limite do sandbox, ele solicita aprovação.
3. Se `approvals_reviewer = "auto_review"`, o Codex encaminha essa solicitação de aprovação
   a um agente revisor separado, em vez de parar à espera de uma pessoa.
4. O revisor decide se a ação deve ser executada e retorna uma justificativa.
5. Se a ação for aprovada, a execução continua. Se for recusada, o
agente principal é instruído a encontrar uma alternativa significativamente mais segura ou a parar e perguntar ao
usuário.

A Revisão automática é uma troca de revisor, não uma concessão de permissão. Ela não amplia
`writable_roots`, não ativa o acesso à rede nem enfraquece os caminhos protegidos. Ela apenas
muda como o Codex lida com ações que já precisam de aprovação.

## Quando é acionada

A Revisão automática avalia solicitações de aprovação que, sem ela, pausariam a execução para aguardar uma pessoa.
Entre elas estão:

- Chamadas de ferramentas shell ou exec que solicitam permissões elevadas no sandbox.
- Solicitações de rede bloqueadas pelo sandbox ou pela política atual.
- Edições de arquivos fora das raízes graváveis permitidas.
- Chamadas de ferramentas MCP ou de aplicativo que exigem aprovação com base nas anotações da ferramenta
ou no modo de aprovação configurado.
- Acesso a um novo site ou domínio pelo Uso do computador.

A Revisão automática não é executada para ações rotineiras já permitidas no
sandbox. Se um comando puder ser executado de acordo com o `sandbox_mode` ativo ou se uma chamada de ferramenta
permanecer dentro do que a política permite, o agente principal continuará sem revisão.

O Uso do computador é um caso à parte. As aprovações do App para o Uso do computador ainda são exibidas
diretamente ao usuário; portanto, a Revisão automática não substitui esses prompts no nível do aplicativo.

## O que a Revisão automática bloqueia

Em linhas gerais, a Revisão automática destina-se a bloquear ações como:

- envio de dados privados, segredos ou credenciais a destinos não confiáveis
- tentativas de localizar credenciais, tokens, cookies ou dados de sessão
- enfraquecimento amplo ou persistente da segurança
- ações destrutivas com risco significativo de danos irreversíveis

A política exata está no repositório de código aberto do Codex:
[policy\_template.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy_template.md)
e
[policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md).
Essa política pode ser personalizada por empresa com `guardian_policy_config` ou
por usuário com a configuração local [`[auto_review].policy`](/pt-BR/codex/config-file/config-advanced#approval-policies-and-sandbox-modes).

## O que o revisor vê

O próprio revisor é um agente do Codex com uma função mais restrita do que a do agente principal:
decidir se uma ação específica que ultrapassa um limite deve ser executada.

O revisor vê uma transcrição compacta e a solicitação de aprovação exata. Isso
normalmente inclui mensagens do usuário, atualizações do assistente exibidas, chamadas de
ferramentas relevantes e resultados das ferramentas, além da ação que está sendo proposta para aprovação. Ele também pode
realizar verificações somente leitura para obter o contexto ausente, mas raramente faz isso.

O raciocínio oculto do assistente não é incluído. A Revisão automática vê itens retidos
do chat e evidências das ferramentas, não a cadeia de pensamento privada.

## Recusas e comportamento em caso de falha

Uma recusa explícita não é tratada como um erro comum do sandbox. O Codex devolve
a justificativa da revisão ao agente principal e acrescenta uma instrução mais enfática:

- Não busque o mesmo resultado por meio de soluções de contorno, execução indireta ou
burla da política.
- Prossiga somente com uma alternativa significativamente mais segura.
- Caso contrário, pare e pergunte ao usuário.

O Codex também aplica um mecanismo de interrupção por recusas a cada turno. Na implementação atual
de código aberto, a Revisão automática interrompe o turno após `3`
recusas consecutivas ou `10` recusas em uma janela móvel das últimas `50`
revisões do mesmo turno.

Qualquer resultado que não seja uma recusa zera o contador de recusas consecutivas. Quando o mecanismo é acionado,
o Codex emite um aviso e aborta o turno atual com uma interrupção, em vez de
permitir que o agente entre em loop com novas tentativas de escalonamento.

Os tempos limite são apresentados separadamente das recusas explícitas, e o agente principal é
informado de que um tempo limite, por si só, não prova que a ação é insegura.

Também há um caminho explícito de anulação para ações recusadas. Na TUI atual
de código aberto, execute `/approve` para abrir o seletor **Recusas da Revisão automática** e, em seguida,
selecione uma ação recusada recentemente para aprová-la para uma nova tentativa. O Codex registra até 10
recusas recentes por tarefa. Essa aprovação é restrita: aplica-se à ação exata
que foi recusada, não a ações futuras semelhantes; é registrada para uma nova tentativa no
mesmo contexto; e a nova tentativa ainda passa pela Revisão automática. Nos bastidores,
o Codex injeta um marcador de aprovação com escopo delimitado ao desenvolvedor para essa ação exata. O
revisor então vê essa anulação explícita pelo usuário como contexto, mas ainda segue
a política e pode recusar novamente se ela determinar que o usuário não pode anular essa categoria de
recusa.

## Configuração

Para saber como configurar, consulte
[Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration#configure-automatic-review-policy).

A política padrão do revisor está no repositório de código aberto do Codex:
[core/src/guardian/policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md).
As empresas podem substituir a seção específica do tenant por
`guardian_policy_config` nos requisitos gerenciados. Usuários individuais também podem definir
localmente
[`[auto_review].policy`](/pt-BR/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)
no arquivo `config.toml`, mas os requisitos gerenciados têm precedência:

```toml
[auto_review]
policy = """
YOUR POLICY GOES HERE
"""

Para personalizar a política, primeiro copie todo o texto da política padrão e, depois,
faça ajustes de acordo com seu perfil de risco específico.

## Configure uma atividade autorizada de cibersegurança

Para atividades de segurança autorizadas, combine a revisão automática com um
escopo documentado para a atividade e um [perfil de permissões](/pt-BR/codex/permissions) com privilégios mínimos.
Use um alvo de laboratório aprovado, documente as ações e o período da atividade e
mantenha sistemas de produção, hosts não relacionados, credenciais e alterações persistentes
fora do escopo, a menos que haja autorização explícita.

Tanto `[auto_review].policy` quanto `guardian_policy_config` substituem sua política atual
do revisor. Essas configurações não são mescladas às políticas fornecidas com seu modelo ou
gerenciadas pela organização. As instruções de revisão e o formato de resposta
integrados continuam válidos. Antes de usar qualquer um dos exemplos, copie toda a política
atual, mantenha todas as regras existentes e adicione as regras do trabalho aprovado.
Substitua o placeholder em maiúsculas por essa política completa. Se você não
tiver acesso à política atual, não a substitua.

O modelo local de `config.toml` a seguir ativa a revisão e adiciona condições com escopo delimitado
depois da política existente do revisor:

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = ":workspace"

[auto_review]
policy = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.
- Approved actions: inspect the target, reproduce authorized vulnerabilities,
  and validate fixes within the documented engagement window.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only actions against the approved target that match the documented
  engagement scope and approved actions.
- Deny out-of-scope or unknown hosts, production access, credential theft,
  persistence, data exfiltration, destructive operations, and policy bypass.
- Deny ambiguous actions and high-impact changes until a human explicitly
  approves the exact target, action, and side effects.
"""

Substitua o alvo e as ações permitidas do exemplo pelo escopo aprovado real.
Aplique as restrições do alvo com regras independentes para o sistema de arquivos e a rede;
as instruções do revisor não substituem esses limites.

As organizações podem aplicar as mesmas condições em um `requirements.toml` gerenciado:

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]
allowed_sandbox_modes = ["read-only", "workspace-write"]
default_permissions = ":workspace"

guardian_policy_config = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only approved actions against the documented engagement target.
- Deny out-of-scope hosts, production access, credential theft, persistence,
  data exfiltration, destructive operations, and attempts to bypass policy.
- Deny ambiguous or high-impact actions until a human explicitly approves the
  exact target, action, and side effects.
"""

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

`allowed_permission_profiles` controla os perfis de permissões atuais.
`allowed_sandbox_modes` também impede o acesso completo em implantações que ainda usam
o `sandbox_mode` legado.

A configuração gerenciada `guardian_policy_config` tem precedência sobre a configuração local
`[auto_review].policy` do usuário. Mantenha `approval_policy = "on-request"` ou outra
política de aprovação interativa compatível e preserve um limite de sandbox que possa ser aplicado.
Com `approval_policy = "never"`, `:danger-full-access` ou `--yolo`, uma ação
pode deixar de gerar a solicitação de aprovação para ultrapassar o limite, necessária para que a revisão ocorra.

Um destino de rede na lista de permissões não aciona uma revisão por si só. Adicione
[regras de comando](/pt-BR/codex/agent-configuration/rules) explícitas com
`decision = "prompt"` ou configure ferramentas MCP sensíveis para exigir aprovação
quando as ações dentro do sandbox ainda precisarem chegar ao revisor.

Consulte [Modelos e acesso confiável](/pt-BR/codex/cyber-safety) e a [configuração
recomendada](/pt-BR/codex/cyber-safety/recommended-configuration) para saber mais sobre acesso a modelos,
configuração da atividade e fluxos de trabalho personalizados para agentes. Consulte [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration#configure-automatic-review-policy)
para ver a precedência para empresas e as versões compatíveis do cliente. Para harnesses personalizados da API ou
do Agents SDK, use [Guardrails e revisão humana](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution).

## Reduza o volume de revisões sem enfraquecer a segurança

A Revisão automática funciona melhor quando o sandbox já abrange os fluxos de trabalho
seguros mais comuns. Se muitas ações corriqueiras precisarem de revisão, corrija primeiro o limite,
em vez de ensinar o revisor a aprovar indefinidamente escalonamentos desnecessários.

Na prática, as mudanças de maior impacto são:

- Adicione valores com escopo restrito a
[`writable_roots`](/pt-BR/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)
  para diretórios temporários ou repositórios próximos que você usa intencionalmente.
- Adicione [regras de prefixo](/pt-BR/codex/agent-configuration/rules) com escopo delimitado. Prefira prefixos de comando
  precisos, como `["cargo", "test"]` ou `["pnpm", "run", "lint"]`, a padrões
  amplos, como `["python"]` ou `["curl"]`. Regras amplas muitas vezes eliminam justamente o
  limite que a Revisão automática deve proteger.

As transcrições das sessões da Revisão automática são mantidas em `~/.codex/sessions` por
padrão; assim, você pode pedir ao Codex que analise o tráfego anterior nesse local antes de alterar
a política ou as permissões.

## Limites

A Revisão automática melhora o padrão de operação para trabalhos agênticos de longa duração,
mas não é uma garantia determinística de segurança.

- Ela avalia apenas ações que pedem para ultrapassar um limite.
- Ela ainda pode cometer erros, especialmente em contextos adversariais ou incomuns.
- Ela deve complementar, e não substituir, um Sandbox bem projetado, o monitoramento e
as políticas específicas da organização.

Para conhecer a fundamentação da pesquisa e os resultados de avaliação publicados, consulte a
[publicação da Alignment Research sobre Revisão automática](https://alignment.openai.com/auto-review/).

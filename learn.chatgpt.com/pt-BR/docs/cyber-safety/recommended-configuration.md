<!-- source: https://learn.chatgpt.com/pt-BR/docs/cyber-safety/recommended-configuration -->

Os controles de segurança adequados para um fluxo de trabalho de cibersegurança dependem do modelo, das ações que ele pode executar, dos sistemas que pode acessar e da sensibilidade dos dados envolvidos.

Na maioria dos fluxos de trabalho do Daybreak Blue, as práticas de segurança já adotadas pela sua organização — como controles de acesso, proteção de credenciais e revisão de ações sensíveis — podem ser suficientes.

Os fluxos de trabalho do Daybreak Red, os testes autônomos de segurança e as atividades que envolvem sistemas de produção, dados confidenciais ou ferramentas externas podem exigir proteções mais rigorosas. As recomendações abaixo destinam-se principalmente a essas situações de maior risco.

  Você é responsável por avaliar os riscos do seu fluxo de trabalho específico e
implementar controles de segurança adequados. As proteções do modelo e o
Trusted Access não substituem as práticas de segurança, monitoramento e
supervisão da sua organização.

O Trusted Access controla o acesso aprovado ao modelo, mas não configura seu ambiente nem impõe limites aos sistemas e às ações aprovados. Sua equipe deve configurar controles adequados de isolamento, permissão, revisão, monitoramento e supervisão humana. Presuma que o modelo, suas ferramentas e todos os sistemas conectados possam estar comprometidos e configure o ambiente para que, mesmo assim, eles não consigam acessar sistemas não autorizados, expor credenciais, desativar proteções nem manter persistência após o término do trabalho.

## Isole o ambiente

Execute atividades ofensivas de segurança em um laboratório ou sandbox dedicado. Comece sem acesso irrestrito à internet, a sistemas de produção sensíveis, a redes corporativas, a cargas de trabalho não relacionadas ou a interfaces de gerenciamento do host. Mantenha segredos, credenciais, acesso persistente e alterações duradouras no sistema fora de alcance, a menos que as atividades aprovadas exijam e autorizem isso explicitamente.

Para atividades de maior risco ou com proteções reduzidas, use um ambiente novo e rigorosamente isolado a cada tentativa. Separe recursos de computação, armazenamento, rede e identidades e, depois, destrua o ambiente em vez de restaurá-lo ou reutilizá-lo.

Teste os limites do sistema de arquivos e da rede antes de iniciar atividades de maior risco. Inclua todos os hosts acessíveis, as ferramentas conectadas, os agentes delegados e os serviços subsequentes. Mantenha o ambiente do host isolado mesmo que o modelo ou o revisor aprove uma ação específica.

## Defina e imponha os limites aprovados

Antes de iniciar o modelo, documente os sistemas, as ferramentas, as ações e os limites de tempo aprovados para seu trabalho. Inclua:

- Sistemas, hosts e ambientes de destino aprovados.
- Sistemas excluídos, incluindo sistemas de produção e infraestrutura não relacionada.
- Ferramentas e serviços conectados aprovados.
- Ações aprovadas e proibidas.
- Horários de início e término aprovados e requisitos de tratamento de dados.
- Divulgação de vulnerabilidades, aprovação de patches e coordenação com mantenedores.
- Condições de interrupção e ações que exigem aprovação humana explícita.

Forneça ao agente esses limites aprovados como contexto da tarefa. A documentação por si só não basta para impô-los: aplique controles independentes ao sistema de arquivos, à rede, às identidades e às ferramentas para, sempre que possível, impossibilitar ações não autorizadas.

Use os [perfis de permissão](/pt-BR/codex/permissions) do Codex para criar um limite baseado no princípio do privilégio mínimo. Escolha `:read-only` quando a tarefa não exigir alterações ou estenda `:workspace` quando o trabalho exigir edições no workspace. Por exemplo:

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = "cyber-lab"

[features]
network_proxy = true

[permissions.cyber-lab]
description = "Limit security testing to the approved lab and workspace."
extends = ":workspace"

[permissions.cyber-lab.filesystem]
glob_scan_max_depth = 3

[permissions.cyber-lab.filesystem.":workspace_roots"]
"**/.env*" = "deny"
"**/*.pem" = "deny"

[permissions.cyber-lab.network]
enabled = true
# Uncomment only for an approved host that resolves to a private address.
# allow_local_binding = true

[permissions.cyber-lab.network.domains]
"lab.example.com" = "allow"

O recurso `network_proxy` impõe o domínio aprovado. Sem ele,
`network.enabled = true` permite acesso direto à rede, e a lista de permissões do laboratório
não restringe os destinos. Pesquisa na Web, aplicativos, conectores, servidores MCP,
atividade do navegador e Codex Cloud usam controles separados; restrinja ou desative
cada recurso que seu fluxo de trabalho aprovado não exigir.

Substitua `lab.example.com` por um destino aprovado. A varredura do sistema de arquivos com escopo delimitado foi projetada para evitar a busca em todo o workspace no Linux, WSL e Windows; aumente a profundidade ou use caminhos exatos de bloqueio se houver arquivos confidenciais em níveis mais profundos. Não combine perfis de permissão com configurações legadas de `sandbox_mode`; siga as [orientações de configuração de perfis de permissão](/pt-BR/codex/permissions#define-and-select-a-profile).

Se a resolução do host de laboratório aprovado resultar em um endereço privado, o Codex o bloqueará por padrão, mesmo que o host esteja na lista de permissões. Defina `allow_local_binding = true` somente para atividades em rede privada explicitamente aprovadas, mantenha restrita a lista de destinos permitidos e consulte as [orientações sobre redes locais e privadas](/pt-BR/codex/permissions#local-and-private-networks). Você também pode adicionar à lista de permissões o endereço IP privado específico que foi aprovado.

Bloqueie por padrão o acesso à internet pública e à rede de produção. Se o acesso externo for necessário, encaminhe-o por um gateway ou proxy que aplique controles de maneira independente, com listas de permissões restritas, inspeção de solicitações e registro em log. Aplique as mesmas restrições a conexões indiretas por meio de gerenciadores de pacotes, webhooks, serviços de busca de URLs, redirecionamentos, APIs de nuvem e ferramentas conectadas. Carregue as dependências antes da execução ou use dependências aprovadas por um administrador.

## Proteja credenciais e dados confidenciais

Mantenha chaves de API reutilizáveis, credenciais de nuvem, senhas e tokens de contas de serviço fora de prompts, repositórios, variáveis de ambiente, sistemas de arquivos compartilhados e logs acessíveis ao modelo. Quando a autenticação for necessária, use um intermediário ou gateway separado para fornecer credenciais de curta duração com escopo restrito ao destino exato e à ação permitida, sem expor a credencial ao modelo.

Forneça somente os dados necessários para a tarefa aprovada. Remova informações confidenciais desnecessárias, bloqueie o acesso a metadados de nuvem e endpoints de credenciais e trate os arquivos gerados pelo modelo como não confiáveis.

Evite `:danger-full-access` e `--yolo` em fluxos de trabalho de cibersegurança. O Acesso completo remove o limite do sandbox imposto pelo sistema, do qual a revisão automática depende. Organizações gerenciadas podem excluir `:danger-full-access` e `--yolo`, limitar as políticas de aprovação permitidas e exigir revisão automática por meio da [configuração gerenciada para empresas](/pt-BR/codex/enterprise/managed-configuration#configure-automatic-review-policy).

Antes de ativar o **Acesso completo** para um modelo de segurança aprovado, o aplicativo do ChatGPT para desktop exibe um aviso específico do modelo sobre ações perigosas. O aviso recomenda usar **Aprovar por mim** em vez disso e inclui um link para a [configuração da política do revisor](/pt-BR/codex/sandboxing/auto-review#configuration). O aviso não restaura o limite do sandbox nem substitui a política da organização.

Os mecanismos de proteção acrescentam uma revisão baseada em políticas a um fluxo de trabalho controlado de cibersegurança. Eles não substituem o isolamento do ambiente, as permissões com privilégio mínimo, os limites claramente definidos, o monitoramento nem a supervisão humana.

## Revise as ações sensíveis do Codex

A [Revisão automática](/pt-BR/codex/sandboxing/auto-review) encaminha a um revisor distinto as solicitações de aprovação elegíveis relacionadas ao limite do sandbox antes da execução da ação proposta. O revisor considera a ação proposta, o contexto da tarefa com escopo delimitado e a política aplicável e, então, permite ou nega a solicitação. As organizações podem personalizar essa política para incluir seus destinos aprovados, ações proibidas e condições que exigem revisão humana.

Exija aprovação humana explícita para ações que afetem a produção, sistemas externos, dados confidenciais, elevação de privilégios, acesso persistente ou alterações irreversíveis. Trate como não confiáveis as instruções incorporadas a sites, repositórios, documentos e saídas de ferramentas; elas não podem ampliar o escopo autorizado nem prevalecer sobre os controles de acesso.

No aplicativo do ChatGPT para desktop, selecionar um modelo Daybreak aprovado muda automaticamente o controle de permissões para **Aprovar por mim** quando esse modo está disponível para sua conta e é permitido pela política da organização. Isso também se aplica quando você usa o comando `/model` do aplicativo para desktop. Se esse modo não estiver disponível, o modo de permissão atual permanecerá inalterado. A seleção do modelo nunca se sobrepõe aos requisitos definidos pela configuração gerenciada da organização.

Para executar a revisão automática, mantenha os três controles a seguir em vigor:

1. Use uma política de aprovação interativa, como `approval_policy = "on-request"`.
2. Defina `approvals_reviewer = "auto_review"`.
3. Mantenha um limite de sandbox ou de perfil de permissão que possa ser efetivamente imposto.

As solicitações para um destino presente na lista de permissões da rede permanecem dentro do limite da rede e não acionam automaticamente a Revisão automática. Para revisar um comando sensível mesmo que seu destino esteja na lista de permissões, crie uma [regra de comando](/pt-BR/codex/agent-configuration/rules) explícita em `~/.codex/rules/`:

```python
prefix_rule(
    pattern = ["curl"],
    decision = "prompt",
    justification = "Review requests to the approved cybersecurity target.",
)

Reinicie o Codex após adicionar a regra. Com `approvals_reviewer = "auto_review"`, os comandos correspondentes são enviados ao revisor antes da execução. Adicione regras de prompt correspondentes para todos os comandos sensíveis ou use `approval_mode = "prompt"` para [ferramentas MCP](/pt-BR/codex/extend/mcp) específicas. As ações que exigem a decisão de uma pessoa ainda precisam de aprovação humana explícita.

A Revisão automática não inspeciona ações rotineiras que já são permitidas dentro do sandbox. Com `approval_policy = "never"` ou com Acesso completo, uma ação sensível pode não gerar uma solicitação de aprovação sujeita a revisão. A revisão automática pode cometer erros e não substitui o isolamento, os limites claramente definidos, o monitoramento nem a supervisão humana explícita.

Para obter uma política com escopo delimitado e aplicação em toda a organização, consulte [Configurar um fluxo de trabalho de cibersegurança autorizado](/pt-BR/codex/sandboxing/auto-review#configure-an-authorized-cybersecurity-engagement).

## Monitore de forma independente e bloqueie em caso de falha

Registre em log as solicitações ao modelo, as chamadas de ferramentas, a atividade de rede, o uso de credenciais e as alterações relevantes para a segurança. Mantenha os logs e os sistemas de monitoramento fora do ambiente controlado pelo modelo. Emita alertas para destinos não autorizados, solicitações de rede inesperadas, credenciais expostas, alterações em políticas, ausência de logs e tentativas de contornar proteções.

Mantenha a aplicação das políticas, os intermediários de credenciais, os sistemas de revisão e os controles de desligamento de emergência independentes do agente. Interrompa o fluxo de trabalho se um controle essencial ou sistema de monitoramento falhar.

## Adicione mecanismos de proteção a fluxos de trabalho de agentes personalizados

Se você desenvolver com a Responses API, o Agents SDK ou outro harness, adicione uma revisão no limite de execução das ferramentas. Antes da execução, verifique as ações sensíveis propostas em relação aos sistemas, às ações e aos limites de tempo aprovados, encaminhe ações ambíguas ou de alto risco para análise por uma pessoa, aplique restrições independentes ao sistema de arquivos e à rede, mantenha logs de auditoria e bloqueie a execução se o revisor ou a política estiver indisponível.

A Revisão automática do Codex não protege automaticamente ferramentas personalizadas nem harnesses externos. Consulte [Mecanismos de proteção e revisão humana](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution) para conhecer o padrão do Agents SDK e use a [política do revisor de código aberto](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md) como referência.

O ambiente isolado e a revisão fornecidos pelo produto Codex são distintos das [verificações de cibersegurança da API](/api/docs/guides/safety-checks/cybersecurity). As proteções da API podem retornar erros `cyber_policy`, e valores de `safety_identifier` específicos de cada usuário podem ajudar a limitar o impacto de uma ação de proteção.

## Faça a limpeza e valide os resultados

Após o término do trabalho, revogue as credenciais temporárias, encerre os processos em segundo plano, remova o acesso persistente e destrua os ambientes de maior risco. Verifique se não restou nenhum callback, artefato exposto, estado compartilhado nem acesso entre execuções e mantenha usuários, sessões e avaliações distintos isolados entre si.

Valide as descobertas antes de agir com base nelas, siga práticas de divulgação coordenada e atribua a pessoas a responsabilidade pela remediação e pelas alterações.

## Antes de começar

Confirme os sistemas e as ações aprovados, o modelo adequado, o ambiente isolado, as permissões com privilégio mínimo, o acesso restrito à rede, as credenciais protegidas, a revisão das ações, o monitoramento independente, o mecanismo de interrupção de emergência e o plano de limpeza. As proteções do modelo, o isolamento, as permissões com escopo delimitado, a revisão de ações, o monitoramento e a supervisão humana são complementares; nenhum desses elementos deve ser o único controle.

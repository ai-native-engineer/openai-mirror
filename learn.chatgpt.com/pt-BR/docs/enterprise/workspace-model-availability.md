<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/workspace-model-availability -->

Os modelos disponíveis para cada pessoa dependem da interface do produto e de como ela
fez login. Uma configuração de modelo no seu workspace do ChatGPT não se aplica automaticamente
ao Codex no aplicativo do ChatGPT para desktop, à Codex CLI, à extensão para IDE,
ao Codex Cloud nem à API da OpenAI.

Para conhecer o modelo completo de administração, consulte
[Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions).

## Identifique o escopo de acesso aos modelos

| Escopo de produto ou de autenticação                                                         | O acesso aos modelos depende de                                                                                  | Fonte atual                                                                                                                |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Workspace do ChatGPT                                                                          | O plano do workspace, o acesso dos membros, as configurações do workspace e as permissões disponíveis para cada função                 | [Modelos e limites do ChatGPT Enterprise e do ChatGPT Edu](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits) |
| Codex no aplicativo do ChatGPT para desktop, Codex CLI e extensão para IDE com login pelo ChatGPT        | Modelos compatíveis com o cliente específico e acesso disponível para a identidade do ChatGPT usada no login    | [Modelos do Codex](/pt-BR/codex/models) e orientações atuais para o workspace                                                                  |
| Codex Cloud                                                                                | Modelos compatíveis com os fluxos de trabalho hospedados do Codex e acesso disponível para a identidade do ChatGPT usada no login | [Modelos do Codex](/pt-BR/codex/models) e [Codex Cloud](/pt-BR/codex/cloud)                                                                 |
| Codex no aplicativo do ChatGPT para desktop, Codex CLI e extensão para IDE com autenticação por chave de API | A organização e o projeto da API da OpenAI associados à chave                                       | [Autenticação](/pt-BR/codex/auth) e a [Plataforma de API](https://platform.openai.com/docs/overview)                        |

Consulte a fonte atual da interface que o usuário realmente utiliza. Não
copie um catálogo de modelos nem presuma que uma configuração do seletor de modelos do ChatGPT
tenha o mesmo efeito no Codex do aplicativo do ChatGPT para desktop, na Codex CLI,
na extensão para IDE, no Codex Cloud e na Plataforma de API.

## Defina uma experiência inicial clara para os funcionários

Revise as [configurações de Modelos](https://help.openai.com/en/articles/8411955) do seu
workspace antes de convidar um grupo piloto. Proprietários e administradores do workspace podem
configurar padrões iniciais separados para Chat e para Work e Codex. Onde houver
suporte, escolha um modelo inicial, o nível de raciocínio, a velocidade e o comportamento
de novos chats para Chat, Work e as interfaces locais do Codex.

Trate essas escolhas como padrões, não como permissões. Os modelos disponíveis ainda dependem
da licença atribuída ao membro, de sua função, da identidade no workspace ou na API, dos requisitos obrigatórios
do workspace e da interface específica utilizada. Os padrões iniciais não concedem acesso
a modelos indisponíveis nem se sobrepõem a esses requisitos. O Codex Cloud não permite
alterar seu modelo padrão.

A disponibilidade do modo Fast depende do workspace, da interface do produto e de qualquer
configuração obrigatória de `features.fast_mode` em
[`requirements.toml`](/pt-BR/codex/config-file/config-reference#requirementstoml).
Essa configuração pode fixar o modo Fast como ativado ou desativado nos clientes locais gerenciados do Codex; ela
não é um padrão inicial e não pode se sobrepor à disponibilidade no workspace ou no produto.

## GPT-6 Astra no Enterprise

Durante a disponibilização inicial, sua organização precisa ter acesso ao Daybreak para que
um administrador possa habilitar o Astra. O Astra fica desativado por padrão no ChatGPT Enterprise
nas duas primeiras semanas após o lançamento. Administradores de workspaces elegíveis
podem habilitar o Astra para usuários ou grupos
no Chat, no Work e no Codex. Os critérios de elegibilidade existentes do produto continuam válidos. Revise as
[configurações de modelos do workspace](https://help.openai.com/en/articles/8411955) e
confirme a disponibilidade em cada cliente usado pelo seu grupo piloto.

Habilitar o acesso e escolher um modelo inicial são decisões distintas. Verifique
a licença, a função e as condições de cobrança aplicáveis antes de definir o Astra como padrão.
Consulte [preços](/pt-BR/codex/pricing) para obter orientações sobre limites de uso e cobrança
e [monitoramento de segurança](/pt-BR/codex/agent-approvals-security#safety-monitoring-and-paused-tasks)
para saber mais sobre tarefas que são pausadas para revisão.

Para login com chave de API, o acesso ao Astra depende da organização e do projeto da API
associados à chave. Habilitar o Astra em um workspace do ChatGPT não concede
acesso pela API. O acesso antecipado com uma chave de API também exige a configuração do cliente;
peça instruções de configuração à equipe da OpenAI responsável pela sua conta. Selecionar um
modelo ou alterar a configuração local não concede acesso por si só.

## Prepare-se para a descontinuação do GPT-5.4

Em 31 de agosto de 2026, o GPT-5.4 e o GPT-5.4 mini deixarão de estar disponíveis no Codex para usuários
que fizeram login com o ChatGPT. Antes dessa data, atualize os padrões afetados do workspace, as configurações de modelo salvas,
as configurações gerenciadas, os agentes personalizados e as tarefas agendadas:

- Substitua `gpt-5.4` por `gpt-5.6-terra` (GPT-5.6 Terra).
- Substitua `gpt-5.4-mini` por `gpt-5.6-luna` (GPT-5.6 Luna).

A API da OpenAI e o Codex autenticado com sua própria chave de API não são afetados.
Consulte [Modelos do Codex](/pt-BR/codex/models#deprecated-codex-models) e
[configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration)
para conferir os detalhes da migração.

## Diferencie o acesso das permissões em tempo de execução

O acesso a modelos determina se um modelo está disponível para o usuário autenticado
em uma interface compatível. Os perfis locais de permissões e os requisitos gerenciados
determinam o que um agente pode fazer depois que uma execução local começa, como os arquivos que
pode alterar e os destinos de rede que pode acessar.

Um perfil de permissões não pode conceder acesso a modelos. O acesso a modelos também não pode enfraquecer
o sandbox, a política de aprovação, os controles de rede nem as permissões do sistema de origem
aplicáveis a uma execução.

## Solucione problemas de acesso a modelos

Se um usuário não conseguir selecionar um modelo esperado:

- Confirme a interface do produto e o método de login.
- Confirme o workspace do ChatGPT ou a organização e o projeto da Plataforma de API.
- Revise os controles de acesso atuais aplicáveis a esse escopo de autenticação.
- Verifique se o cliente local selecionado ou o Codex Cloud oferece suporte ao modelo.

## Fontes atuais

- [Modelos e limites do ChatGPT Enterprise e do ChatGPT Edu](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits)
- [Gerenciar configurações do workspace](https://help.openai.com/en/articles/8411955)
- [Controle de acesso baseado em funções](https://help.openai.com/en/articles/11750701-rbac)
- [Modelos do Codex](/pt-BR/codex/models)
- [Disponibilidade dos recursos do Codex por plano](/pt-BR/codex/pricing#feature-availability)
- [Autenticação](/pt-BR/codex/auth)

## Documentação relacionada

- [Guia de implementação para administradores](/pt-BR/codex/enterprise/admin-setup)
- [Grupos e provisionamento](/pt-BR/codex/enterprise/groups-and-provisioning)
- [Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions)
- [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration)

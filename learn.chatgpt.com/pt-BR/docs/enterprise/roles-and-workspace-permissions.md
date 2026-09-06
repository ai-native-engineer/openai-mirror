<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/roles-and-workspace-permissions -->

Configurações diferentes abrangem aspectos distintos da experiência da sua organização com o
ChatGPT. Conceder acesso a alguém em uma área não concede automaticamente acesso
em outra. Use esta página para entender como os seis limites de controle funcionam
em conjunto e siga as orientações nos links para conferir as etapas atuais de configuração.

Nas configurações do workspace, **Codex e Work Local** reúne o acesso local ao Codex e ao Work
na opção **Permitir que os membros usem o Codex e o Work localmente**. Outros workspaces
separam **Codex Local** e **Work Local** em seções independentes. Nessa
organização, **Permitir que os membros usem o Codex localmente** concede acesso local ao Codex, e
**Usar o Work localmente** concede acesso local ao Work. Ativar uma opção não concede
acesso à outra. Esses rótulos identificam permissões do workspace, não produtos
ou clientes separados. As permissões de tokens e os limites de validade das credenciais aparecem
na seção **Tokens de acesso** ou na seção de acesso local, dependendo
do workspace. A configuração gerenciada é uma camada separada que restringe
o comportamento compatível em tempo de execução das capacidades abrangidas nesses clientes. Os recursos
e os requisitos em vigor podem variar conforme o cliente e a versão.

## Entenda os limites de controle

| Limite          | O que controla                                                                                                                                                                                      | O que não controla                                                                          | Fonte atual                                                                                                                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workspace do ChatGPT | Participação no workspace, licenças, funções administrativas integradas e acesso baseado em funções aos recursos compatíveis do workspace                                                                                               | Permissões do agente local, acesso à organização na Plataforma de API ou permissões em um serviço conectado | [Acesso ao workspace do ChatGPT](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise) e [RBAC](https://help.openai.com/en/articles/11750701-rbac) |
| Clientes locais     | Comportamento em tempo de execução das capacidades abrangidas no aplicativo do ChatGPT para desktop, no Codex CLI e na extensão para IDE, incluindo aprovações, acesso ao sistema de arquivos e à rede, perfis de permissão e integrações permitidas | Uma licença do ChatGPT, o direito de usar um recurso ou um modelo, ou o acesso a dados externos                         | [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration) e [Permissões](/pt-BR/codex/permissions)                                                                                                   |
| Codex Cloud       | Elegibilidade para usar os fluxos de trabalho hospedados do Codex e os ambientes de nuvem disponibilizados ao usuário                                                                                                       | A política de execução local ou as permissões do repositório concedidas por um sistema de origem                    | [Ambientes de nuvem](/pt-BR/codex/environments/cloud-environment)                                                                                                                                              |
| Plataforma de API      | Participação em organizações e projetos, chaves de API, acesso a modelos, uso e faturamento de atividades autenticadas por API                                                                                            | Participação no workspace do ChatGPT, acesso a clientes locais ou acesso ao Codex Cloud                         | [Plataforma de API](https://platform.openai.com/docs/overview)                                                                                                                                         |
| Plug-ins           | Disponibilidade e instalação de plug-ins, habilidades incluídas, acesso a conectores e ações compatíveis dos conectores                                                                                               | Autorização no serviço conectado ou permissões mais amplas de execução local e na nuvem            | [Controles de plug-ins](/pt-BR/codex/enterprise/apps-and-connectors)                                                                                                                                                 |
| Sistemas conectados | Quais repositórios, arquivos, mensagens e ações a conta autenticada pode acessar no sistema de origem                                                                                            | Direito de usar o workspace do ChatGPT, plug-ins, o Codex Cloud ou a Plataforma de API                              | Os controles administrativos e de acesso do serviço conectado                                                                                                                                               |

Uma solicitação precisa passar por todos os limites aplicáveis. Por exemplo, o acesso ao workspace
pode disponibilizar um plug-in, mas o serviço conectado ainda decide quais
dados a conta autenticada pode ler. Um perfil de permissão local pode restringir uma
execução em um cliente local compatível, mas não pode conceder acesso a um recurso ou
modelo do workspace.

## Atribua acesso ao workspace

A administração do workspace do ChatGPT separa o acesso ao produto da autoridade
administrativa.

### Entenda a diferença entre uma licença, uma função de administrador e uma função personalizada

Uma licença determina quais áreas do produto um membro pode acessar. Dependendo do
plano do workspace, os tipos de licença disponíveis podem incluir licenças do ChatGPT e do Codex.

As funções integradas do workspace determinam a autoridade administrativa. A função de **Proprietário** 
gerencia as configurações de todo o workspace; a função de **Administrador** gerencia as operações compatíveis
e os grupos; a função de **Membro** não tem direitos administrativos; e a função de
**Visualizador de análises** pode acessar as análises do workspace.

As funções personalizadas definem quais recursos compatíveis um membro pode usar. Elas não
substituem a elegibilidade da licença ou do plano, não concedem permissões em um sistema conectado nem
alteram os requisitos de execução local.

<div class="not-prose my-4 aspect-video overflow-hidden rounded-md bg-gray-900">
  <iframe
    src="https://player.vimeo.com/video/1215495812"
    title="Passo a passo do controle de acesso baseado em funções"
    loading="lazy"
    allow="autoplay; fullscreen; picture-in-picture"
    allowFullScreen
    referrerPolicy="strict-origin-when-cross-origin"
    class="h-full w-full border-0"
  ></iframe>
</div>

### Defina a configuração padrão do workspace e depois crie funções personalizadas específicas

Somente os proprietários do workspace podem configurar o controle de acesso baseado em funções (RBAC) e criar
funções personalizadas. As configurações do workspace estabelecem a base para as permissões
elegíveis. Os proprietários do workspace podem atribuir funções personalizadas por meio de grupos ou
diretamente a membros individuais, quando houver suporte. Os grupos podem ser gerenciados manualmente
ou sincronizados via SCIM, e um membro pode receber mais de uma função personalizada.

Para as permissões elegíveis, **Padrão** herda a configuração do workspace, **Ativado**
concede acesso e **Desativado** nega explicitamente o acesso. A seleção explícita de **Desativado** em qualquer
função aplicável bloqueia o acesso mesmo quando outra função o concede. Os estados de
permissão disponíveis podem variar conforme o recurso.

### Revise as permissões Work Local e Work na nuvem

Quando seu workspace oferecer **Work Local** e **Work na nuvem**, verifique tanto a configuração padrão do
workspace quanto cada função personalizada aplicável. O Work está disponível apenas para
workspaces elegíveis, e os controles disponíveis podem variar conforme o plano, a configuração
do workspace e a implementação. Uma função não pode ampliar o acesso permitido pela
licença de um membro.

**Work na nuvem** controla as tarefas compatíveis do ChatGPT Work na nuvem. Quando os
controles são independentes, **Work Local** sem **Work na nuvem** permite trabalhar
localmente no aplicativo do ChatGPT para desktop, mas não permite que os membros iniciem tarefas na nuvem.
O acesso local ao Codex usa **Permitir que os membros usem o Codex localmente** em **Codex
Local**. Alterar **Usar o Work localmente** não altera o acesso local ao Codex nem
substitui os requisitos de execução local.

Alguns workspaces exibem, em vez disso, a seção combinada **Codex e Work Local** . Nessa
organização, **Permitir que os membros usem o Codex e o Work localmente** controla os dois
produtos.

Para consultar a elegibilidade e as configurações atuais, veja
[ChatGPT Work e Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

Como as licenças, funções e permissões disponíveis mudam com as atualizações dos produtos e dos
planos, consulte a Central de Ajuda para conferir a lista atual de permissões e o procedimento de
configuração:

- [Gerenciar membros, tipos de licença, funções e acesso](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [Configurar o controle de acesso baseado em funções](https://help.openai.com/en/articles/11750701-rbac)
- [Gerenciar grupos](https://help.openai.com/en/articles/9083985-group-permissions-in-gpts)

### Controle o acesso ao Histórico do computador

O [Histórico do computador](/pt-BR/codex/customization/computer-history) está desativado por padrão nos workspaces dos planos
Business e Enterprise. Os membros não podem ativá-lo até que um proprietário do workspace
conceda acesso explicitamente. Os proprietários de workspaces Enterprise podem conceder acesso
por função:

1. Abra [**Configurações do workspace \> Permissões e funções**](https://chatgpt.com/admin/settings).
2. Encontre **Histórico do computador** e escolha a função do workspace que deverá ter
   acesso.
3. Ative a opção **Ativar Histórico do computador** para essa função.

Essa permissão apenas autoriza os membros designados a ativar o Histórico do computador; ela
não ativa o recurso para eles. Cada membro deve optar por ativá-lo no aplicativo do ChatGPT
para desktop no macOS e pode escolher quais aplicativos e sites contribuirão. Membros
sem a permissão necessária no workspace não podem ativar o recurso pelas
configurações locais.

## Aplique a política de execução local

A política de execução local restringe as capacidades abrangidas no aplicativo do ChatGPT para
desktop, no Codex CLI e na extensão para IDE. Os requisitos gerenciados na nuvem também
dependem de um login compatível no ChatGPT e da elegibilidade do plano. Os perfis de permissão
e os requisitos gerenciados podem restringir comandos, o acesso ao sistema de arquivos e à
rede, as aprovações e outros comportamentos de execução local. Eles não alteram a
licença do usuário, sua função no workspace, seu direito de usar modelos ou suas permissões em um sistema
externo.

Os usuários podem selecionar um perfil de permissão integrado ou personalizado quando a política local
permitir. Os administradores podem distribuir valores padrão e requisitos pelos
canais compatíveis de configuração gerenciada. Consulte [Permissões](/pt-BR/codex/permissions)
para saber como os perfis funcionam e [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration)
para ver os requisitos, a distribuição e a precedência.

## Documentação relacionada

- [Guia de implementação para administradores](/pt-BR/codex/enterprise/admin-setup)
- [Grupos e provisionamento](/pt-BR/codex/enterprise/groups-and-provisioning)
- [Gerenciamento do ciclo de vida de usuários](/pt-BR/codex/enterprise/user-lifecycle)
- [Disponibilidade de modelos no workspace](/pt-BR/codex/enterprise/workspace-model-availability)
- [Tokens de acesso](/pt-BR/codex/enterprise/access-tokens)
- [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration)
- [Autenticação](/pt-BR/codex/auth)

<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/admin-setup -->

Use este guia para planejar uma implementação do ChatGPT Enterprise que abranja estes
âmbitos de administração:

- Acesso ao workspace.
- Política de execução local para as capacidades abrangidas no aplicativo do ChatGPT para desktop,
no Codex CLI e na extensão para IDE.
- Codex Cloud.
- Acesso à API da plataforma.
- Acesso a plug-ins e conectores.
- Permissões em sistemas conectados.

Para uma nova implementação, conclua as etapas em ordem ou use as páginas vinculadas para alterar
um dos âmbitos.

Nas configurações do workspace, **Codex e Work Local** reúne o acesso local ao Codex e ao Work
em **Permitir que os membros usem o Codex e o Work localmente**. Alguns workspaces
oferecem, em vez disso, seções independentes de **Codex Local** e **Work Local** . Nessa
organização, **Permitir que os membros usem o Codex localmente** controla o Codex, e **Usar o
Work localmente** controla o Work. Ativar um deles não ativa o outro.
Esses rótulos identificam permissões do workspace, não produtos ou clientes separados.
As permissões de tokens e os limites de validade das credenciais aparecem na seção **Tokens de
acesso** ou na seção de acesso local, dependendo do workspace.
A configuração gerenciada é uma camada de política separada que pode restringir os comportamentos de execução com suporte
para as capacidades abrangidas nesses clientes. Este guia identifica
cada interface quando o comportamento ou a disponibilidade são diferentes.

Comece pelo mapa de referência em
[Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions).
Consulte as orientações da Central de Ajuda para ver os procedimentos atuais do workspace do ChatGPT e a
documentação para desenvolvedores vinculada para entender o comportamento da execução local e hospedada.

<a id="enterprise-grade-security-and-privacy"></a>

Para conhecer as proteções de segurança, privacidade e execução para empresas, consulte
[Aprovações e segurança de agentes](/pt-BR/codex/agent-approvals-security) e o
[white paper de segurança do Codex](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click).

<a id="pre-requisites-determine-owners-and-rollout-strategy"></a>

## Etapa 1: designe responsáveis e escolha uma abordagem de implementação

Designe um responsável por cada parte da implementação:

- **Acesso ao workspace:** membros, licenças, funções e recursos do
  workspace com suporte.
- **Política de execução local:** aprovações, perfis de permissão, acesso ao sistema de arquivos e à
  rede, além de outros requisitos para clientes locais com suporte.
- **Codex Cloud:** ambientes hospedados, conexões com repositórios e política de
  execução na nuvem.
- **Sistemas conectados:** instalação de aplicativos, contas e
  permissões no provedor.
- **Relatórios e conformidade:** acesso a análises, exportações de auditoria e
  tratamento de dados nos sistemas de destino.

Determine se cada público precisa das capacidades locais abrangidas no aplicativo do ChatGPT
para desktop, no Codex CLI, na extensão para IDE, no Codex Cloud ou em uma combinação deles. Trate
o acesso à API da plataforma como um âmbito separado de organização e projeto quando um
fluxo de trabalho usar autenticação por chave de API.

## Etapa 2: configure o acesso ao workspace e a identidade

Use os controles de membros, licenças e grupos do workspace do ChatGPT, além das permissões de RBAC com suporte,
para conceder aos públicos-alvo acesso aos recursos do workspace com suporte. Verifique o acesso aos
clientes locais e ao Codex Cloud conforme as orientações atuais do workspace, em vez
de presumir que a mesma função controla todas as interfaces. Restrinja as funções
administrativas integradas às pessoas que administram o workspace.

Os controles e rótulos do workspace mudam ao longo do tempo. Consulte estas fontes para ver os
procedimentos atuais:

- [Gerenciar membros, tipos de licença, funções e acesso](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [Configurar o controle de acesso baseado em funções](https://help.openai.com/en/articles/11750701-rbac)
- [Gerenciar as configurações do workspace](https://help.openai.com/en/articles/8411955)
- [Grupos e provisionamento](/pt-BR/codex/enterprise/groups-and-provisioning)
- [Gerenciamento do ciclo de vida de usuários](/pt-BR/codex/enterprise/user-lifecycle)
- [Autenticação](/pt-BR/codex/auth)

Teste o login e o acesso aos recursos com um membro representativo antes de ampliar
a implementação. O acesso ao workspace não concede acesso a repositórios, arquivos nem ações
em um serviço conectado.

## Etapa 3: configure os requisitos de execução local

Os requisitos locais restringem o comportamento de execução quando um usuário inicia uma execução
local com suporte no aplicativo do ChatGPT para desktop, no Codex CLI ou na extensão para IDE. Distribua o arquivo
`requirements.toml` por um canal de nuvem, de dispositivo ou de sistema com suporte. Mantenha
essa política separada das funções e dos grupos do workspace do ChatGPT.

Use perfis de permissão para os clientes locais com suporte, em vez de criar novas
implantações com base nas restrições legadas do modo Sandbox. Por exemplo:

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true

Para desativar o Uso do computador em todas as interfaces com suporte no navegador e no
desktop, restrinja cada chave pública de recurso que faça parte da experiência:

```toml
[features]
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
computer_use = false

Para ver a lista oficial de chaves, o comportamento de distribuição, a ordem de precedência e mais
exemplos, consulte
[Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration) e a
[referência de `requirements.toml`](/pt-BR/codex/config-file/config-reference#requirementstoml).

<a id="team-config"></a>
<a id="step-4-standardize-local-configuration-with-team-config"></a>

## Etapa 4: padronize a configuração do repositório

Use uma configuração com escopo de repositório para compartilhar configurações padrão do projeto, regras e
habilidades sem duplicar a configuração para cada usuário. Versione a configuração em
`.codex` ou `.agents`, conforme o local documentado para o recurso:

| Tipo          | Fonte                                           | Use para                                                  |
| ------------- | ------------------------------------------------ | ---------------------------------------------------------- |
| Configuração | [Configuração básica](/pt-BR/codex/config-file/config-basic) | Definir as configurações padrão do repositório para clientes locais com suporte        |
| Regras         | [Regras](/pt-BR/codex/agent-configuration/rules)        | Controlar comandos que exigem aprovação fora do Sandbox |
| Habilidades        | [Criar habilidades](/pt-BR/codex/build-skills)              | Disponibilizar fluxos de trabalho do repositório aos clientes com suporte   |

A configuração do repositório pode fornecer configurações padrão e fluxos de trabalho reutilizáveis. Ela não pode
conceder acesso ao workspace, a modelos, à API da plataforma nem a sistemas conectados.

## Etapa 5: configure o Codex Cloud

O Codex Cloud usa ambientes hospedados e repositórios de código-fonte conectados. Planeje
cada âmbito:

1. Conceda ao público-alvo acesso ao Codex Cloud usando os controles do workspace
com suporte.
2. Instale e configure a integração com suporte para o sistema de origem.
3. Limite o acesso a repositórios no sistema de origem àqueles de que cada
público precisa.
4. Configure ambientes de nuvem, segredos e acesso à internet para esses
repositórios.
5. Configure fluxos de trabalho hospedados opcionais, como revisão de código.
6. Faça o teste com um usuário representativo que tenha as permissões previstas no workspace e no
repositório.

O Codex Cloud respeita as permissões e proteções do repositório disponibilizadas pelo
sistema de origem conectado. O acesso ao workspace não contorna esses controles. Consulte
[Ambientes de nuvem](/pt-BR/codex/environments/cloud-environment),
[Integração com o GitHub](/pt-BR/codex/third-party/github) e
[Aprovações e segurança de agentes](/pt-BR/codex/agent-approvals-security) para ver orientações sobre a
configuração e a execução do Codex Cloud.

## Etapa 6: configure plug-ins e capacidades conectadas

Avalie como decisões separadas a instalação de plug-ins, as habilidades incluídas, as capacidades baseadas em conectores,
as ações de conectores e a autorização no sistema de origem.
Desativar uma capacidade baseada em conector não desinstala necessariamente o
plug-in nem as habilidades incluídas nele.

Antes de incluir um plug-in ou uma habilidade na implementação:

1. Confirme a origem, o responsável designado, o público-alvo e a data de revisão.
2. Revise as habilidades incluídas, os conectores, os servidores MCP, os ganchos e os dados e
as ações que cada recurso exige.
3. Teste com dados não sensíveis e com o mínimo de acesso necessário.
4. Registre quem é responsável pelas novas revisões e pela desativação.

Os plug-ins funcionam no Chat e no Work no ChatGPT na Web, no desktop e em dispositivos móveis,
no Codex no aplicativo do ChatGPT para desktop e por meio do navegador de plug-ins da Codex CLI.
Eles não estão disponíveis na extensão para IDE.
O ChatGPT e o Codex compartilham um único diretório público e universal de plug-ins; os controles do workspace
determinam a quais desses plug-ins os membros podem ter acesso.

Consulte [Controles de plug-ins](/pt-BR/codex/enterprise/apps-and-connectors) e
[Controles de habilidades](/pt-BR/codex/enterprise/skills) para ver o modelo completo.

## Etapa 7: Configure a governança e a observabilidade

Escolha a opção de relatórios adequada à pergunta:

<a id="analytics-api-setup-steps"></a>
<a id="compliance-api-setup-steps"></a>

- Use [Análises do workspace](/pt-BR/codex/enterprise/workspace-analytics) para acessar
  análises interativas do workspace do ChatGPT e análises do Codex.
- Use a [API de análise](/pt-BR/codex/enterprise/analytics-api) para gerar, de forma programática,
  relatórios agregados por meio da API de análise do Codex.
- Use a [API de Compliance](/pt-BR/codex/enterprise/compliance-api) para acessar registros de auditoria e
  investigação.
- Use [Limites de uso e controles de gastos do ChatGPT](/pt-BR/codex/enterprise/usage-limits)
  quando, dependendo do plano, a atividade do Codex consumir
  créditos elegíveis do workspace do ChatGPT.

Consulte a documentação de referência das APIs disponível mediante autenticação para verificar os requisitos atuais de acesso, os esquemas,
os campos, a retenção e o comportamento das solicitações. Não desenvolva uma integração com base em um
contrato copiado deste guia.

Proteja o perímetro da integração:

- Armazene as chaves de API e outras credenciais de integração no sistema de gerenciamento de segredos
da organização.
- Limite o acesso aos sistemas de destino e aos dados retidos ao público
autorizado.
- Proteja os registros exportados da API de Compliance conforme sua sensibilidade e
a política de retenção da organização, e teste os fluxos de trabalho de coleta e exclusão
com base no contrato vigente.

## Etapa 8: Verifique e mantenha a implantação

Verifique cada área de controle aplicável usando identidades representativas:

- Associação ao workspace do ChatGPT, licença e permissões de função compatíveis.
- Recursos locais contemplados no aplicativo do ChatGPT para desktop, na Codex CLI e na extensão
para IDE, incluindo login e requisitos efetivamente aplicados durante a execução.
- Acesso ao Codex Cloud, configuração do ambiente e permissões do repositório.
- Acesso à organização e ao projeto na Plataforma de API para fluxos de trabalho com chaves de API.
- Instalação de plug-ins, habilidades incluídas, acesso a conectores e ações compatíveis.
- Autorização e acesso a dados em sistemas conectados.
- Acesso dos administradores responsáveis a recursos de análise e conformidade.

Registre o responsável e a fonte atual dos procedimentos de cada controle. Esse registro
permite que os administradores atualizem os procedimentos quando houver mudanças na interface ou na política, sem
alterar o modelo de administração.

Após a implantação inicial, revise o acesso, os recursos conectados, o uso de créditos,
o feedback do suporte e os fluxos de trabalho que as equipes realmente usam. Ajuste o escopo da implantação
e as orientações para administradores quando houver mudanças nesses indicadores.

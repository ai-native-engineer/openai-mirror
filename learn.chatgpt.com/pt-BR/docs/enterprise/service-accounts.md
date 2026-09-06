<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/service-accounts -->

As contas de serviço permitem executar e escalar fluxos de trabalho do Codex sem interface em toda a organização, sem depender da conta de um funcionário. Cada executor de integração contínua (CI), tarefa agendada ou integração compartilhada recebe sua própria identidade no workspace do ChatGPT, com os mesmos grupos, funções, controles de acesso e recursos de auditoria esperados para usuários humanos.

Somente proprietários e administradores do workspace podem criar contas de serviço. Eles podem permitir que outras pessoas ou grupos gerenciem uma conta, configurem plug-ins ou criem tokens de acesso.

As contas de serviço estão disponíveis apenas em planos com pagamento conforme o uso.

Uma conta de serviço representa uma identidade não humana no workspace. Um [token de acesso pessoal](/pt-BR/codex/enterprise/access-tokens) representa o membro do workspace que o cria. As contas de serviço de projetos da Plataforma de API e as chaves de API usam acesso ao projeto e faturamento separados.

## Criar e configurar uma conta de serviço

Este passo a passo interativo usa o GitHub como exemplo: crie uma conta, configure um plug-in, crie um token e atribua grupos e funções.

1. Abra [Contas de serviço](https://chatgpt.com/admin/service-accounts) nas configurações do workspace.
2. Selecione o botão com o sinal de mais (**+**) e insira um nome descritivo, como `release-automation`.
3. Selecione **Criar**.

## Conectar um plug-in

Configure os plug-ins da própria conta de serviço. Ela não herda os plug-ins nem os aplicativos conectados da pessoa que a criou.

1. Abra a seção **Plug-ins** da conta e selecione **Adicionar plug-in**.
2. Escolha um plug-in e confirme que ele aparece como configurado ou ativado.

As funções **Configurar** e **Gerente** permitem configurar plug-ins. A função **Usuário** não permite.

## Criar um token de acesso

Crie um token na página de detalhes da conta de serviço. O token representa a conta de serviço, e não a pessoa que o cria.

1. Abra a conta e selecione **Criar token** em **Tokens de acesso**.
2. Dê um nome ao token, confirme o escopo **Codex** e escolha um prazo de expiração.
3. Selecione **Criar** e salve o token no seu gerenciador de segredos.

O token completo aparece apenas uma vez. As políticas do workspace determinam os prazos de expiração disponíveis.

## Atribuir funções e grupos

Uma conta de serviço pode receber funções no workspace e participar de grupos como um membro humano do workspace. Atribua o acesso diretamente à conta; ela não herda as permissões da pessoa que a criou.

Para permitir que pessoas ou grupos gerenciem a conta, selecione **Compartilhar**, depois **Adicionar pessoas ou grupos** e atribua uma função:

| Função na conta compartilhada | Configurar a conta e seus plug-ins | Criar tokens de acesso da conta de serviço |
| ------------------- | ------------------------------------- | ------------------------------------ |
| **Usuário**            | Não                                    | Sim                                  |
| **Configurar**       | Sim                                   | Não                                   |
| **Gerente**         | Sim                                   | Sim                                  |

Essas funções se aplicam às pessoas que gerenciam a conta. Elas são distintas das funções e dos grupos do workspace atribuídos à conta de serviço.

As funções **Configurar** e **Gerente** permitem ativar ou desativar a conta. Somente proprietários e administradores do workspace podem criar, excluir ou compartilhar contas. Os operadores gerenciam as contas compartilhadas enquanto estão conectados às próprias contas do ChatGPT.

Para saber mais sobre as permissões do workspace, consulte [Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions).

## Executar o Codex sem fazer login

Os tokens de acesso de contas de serviço exigem o Codex CLI na versão `0.142.0` ou posterior. Defina `CODEX_ACCESS_TOKEN` e execute o Codex sem abrir um navegador:

```bash

codex exec --json "Inspect this repository and summarize its current state."

Em CI, forneça o token por meio de um gerenciador de segredos ou de um segredo do runner.

Para salvar um login em uma máquina confiável, passe o token pela entrada padrão:

```bash
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "Summarize the changes in the current branch."

Isso salva a credencial localmente. Em runners compartilhados ou temporários, use `CODEX_ACCESS_TOKEN` sem salvar um login.

## Provisionar contas de serviço com SCIM

Se o workspace oferecer suporte ao provisionamento de contas de serviço pelo protocolo System for Cross-domain Identity Management (SCIM), defina `userType` como `ServiceAccount` no provedor de identidade:

```json
{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "userName": "svc-codex-release@company.example",
  "displayName": "Codex release automation",
  "active": true,
  "userType": "ServiceAccount"
}

Atribua a identidade ao workspace e aos grupos necessários e, em seguida, sincronize-a. O provedor de identidade gerencia o nome da conta, sua participação em grupos e seu ciclo de vida. Contas gerenciadas pelo SCIM não podem ser renomeadas nem excluídas no ChatGPT. Consulte [Grupos e provisionamento](/pt-BR/codex/enterprise/groups-and-provisioning).

## Gerenciar contas de serviço com a API Admin

Se o seu workspace tiver acesso, use uma chave da API Admin do ChatGPT para gerenciar contas, tokens e compartilhamento. Operações de leitura exigem `chatgpt.enterprise.service_account.read`; alterações exigem `chatgpt.enterprise.service_account.write`. Um token de conta de serviço não pode autenticar requisições à API Admin.

Consulte a [referência da API Admin](https://chatgpt.com/public/admin/api-reference) para verificar as operações disponíveis e os caminhos atuais das requisições.

### Contas

| Operação                    | Método   | O que faz                               |
| ---------------------------- | -------- | ------------------------------------------ |
| Listar contas                | `GET`    | Retorna as contas de serviço do workspace         |
| Criar uma conta            | `POST`   | Cria uma conta de serviço com o nome fornecido            |
| Obter uma conta               | `GET`    | Retorna uma conta de serviço                |
| Ativar ou desativar uma conta | `PATCH`  | Atualiza o valor de `enabled` da conta      |
| Excluir uma conta            | `DELETE` | Remove a conta e revoga seus tokens |

Crie contas com `POST /v1/manage/workspaces/{workspace_id}/service-accounts`. As atualizações da conta alteram apenas `enabled`.

### Tokens

| Operação      | Método   | O que faz                         |
| -------------- | -------- | ------------------------------------ |
| Listar tokens    | `GET`    | Retorna os metadados dos tokens da conta |
| Criar um token | `POST`   | Cria um token de acesso com escopo delimitado        |
| Revogar um token | `DELETE` | Revoga um token permanentemente        |

Por exemplo, crie um token do Codex que expira após 30 dias:

```json
{
  "name": "production-release-runner",
  "ttl": 2592000,
  "scopes": ["chatgpt.workspace.feature.allow-codex-local-access.access"]
}

`ttl` é o tempo de validade do token em segundos. Um prazo de validade limitado deve ser inferior a um ano e seguir a política de expiração do seu workspace. O `access_token` completo é retornado apenas quando o token é criado.

A API Admin também pode listar, adicionar, atualizar e remover acessos a contas compartilhadas. Os valores das funções são `manager`, `configurer` e `user`; `configurer` aparece como **Configurar** no ChatGPT.

## Proteger e gerenciar contas de serviço

- Conceda apenas as funções, os grupos, os plug-ins e as conexões necessários para o fluxo de trabalho.
- Armazene os tokens em um gerenciador de segredos e use executores confiáveis.
- Mantenha as credenciais fora de logs, mensagens de chat e do controle de versão.
- Defina prazos de validade limitados e revise regularmente o acesso e a atividade das contas.
- Para fazer a rotação de um token, crie um token substituto, atualize o fluxo de trabalho, verifique o acesso e revogue o token antigo no workspace ou na API Admin.
- Revogue imediatamente os tokens expostos e investigue a atividade recente da conta.
- Desative ou exclua contas não utilizadas no workspace ou na API Admin. As duas ações revogam todos os tokens ativos. Contas desativadas podem ser reativadas com novos tokens; a exclusão não pode ser desfeita.

As execuções são atribuídas à conta de serviço. As análises do workspace e os registros de auditoria disponíveis também podem identificar quem criou tokens ou alterou as configurações da conta. Confirme a cobertura de eventos na [referência da API Admin](https://chatgpt.com/public/admin/api-reference).

## Documentação relacionada

- [Autenticação](/pt-BR/codex/auth)
- [Tokens de acesso pessoal](/pt-BR/codex/enterprise/access-tokens)
- [Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions)
- [Grupos e provisionamento](/pt-BR/codex/enterprise/groups-and-provisioning)
- [Governança](/pt-BR/codex/enterprise/governance)
- [API de Compliance e eventos de auditoria](/pt-BR/codex/enterprise/compliance-api)
- [Modo não interativo](/pt-BR/codex/non-interactive-mode)

<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/access-tokens -->

Os tokens de acesso do Codex são credenciais do workspace do ChatGPT com escopo limitado às permissões do Codex. Eles autenticam fluxos de trabalho locais, confiáveis e não interativos, incluindo a Codex CLI e automações baseadas no App Server, com uma identidade do workspace do ChatGPT. Use-os quando um script, uma tarefa agendada ou um executor de CI precisar de acesso local repetível.

  Atualmente, os tokens de acesso do Codex são compatíveis com workspaces do ChatGPT Business e do
ChatGPT Enterprise.

Crie tokens de acesso pessoal no console de administração do ChatGPT, em [Tokens de acesso](https://chatgpt.com/admin/access-tokens). Cada token pertence a quem o criou e ao workspace do ChatGPT desse usuário. Os tokens funcionam como identidades de agente para fluxos de trabalho locais programáticos. Para saber mais sobre tokens criados na página de detalhes de uma identidade não humana dedicada do workspace, consulte [Contas de serviço](/pt-BR/codex/enterprise/service-accounts).

  Se uma chave de API da Plataforma funcionar para sua automação, continue usando a autenticação com chave de API. Use
os tokens de acesso do Codex quando um fluxo de trabalho local confiável precisar especificamente de acesso ao workspace do ChatGPT,
de direitos de acesso gerenciados pelo workspace ou de controles empresariais.

  Precisa acionar um agente publicado do workspace do ChatGPT a partir do seu próprio sistema? Esse
  fluxo de trabalho exige acesso a **Agentes do workspace** . Um token exclusivo do Codex não pode
  autenticar chamadas de acionamento de agentes do workspace. Se a caixa de diálogo do token oferecer
**Escopos**, selecione **Agentes do workspace** para acionar um agente e **Codex** para
  automações do Codex. Conceda vários escopos somente quando o fluxo de trabalho exigir cada
  um deles. Consulte [Autenticar com tokens de acesso
  de agentes do workspace](/workspace-agents/authentication).

## Como funcionam os tokens de acesso

Use um token de acesso quando for necessário executar a Codex CLI ou um cliente do App Server sem que um usuário conclua o login pelo navegador. O token representa o usuário do workspace do ChatGPT que o criou, de modo que as execuções podem usar o acesso desse usuário e aparecer nos dados de governança do workspace.

O cliente verifica o token quando uma execução começa e vincula a execução a essa identidade do workspace. Trate o token como qualquer outro segredo de automação: armazene-o em um gerenciador de segredos, mantenha-o fora dos logs e faça sua rotação conforme a política da sua organização.

Use tokens de acesso para:

- Tarefas `codex exec` executadas por automações confiáveis.
- Scripts locais que precisam de execuções repetíveis e não interativas da Codex CLI.
- Automações confiáveis baseadas no App Server.
- Fluxos de trabalho empresariais que associam o uso a um usuário do workspace do ChatGPT em vez de uma chave de organização da API.

Principais riscos a evitar:

- **Segredos vazados:** qualquer pessoa que tenha o token pode iniciar execuções locais pela Codex CLI ou por um cliente do App Server em nome de quem criou o token. Armazene os tokens em um gerenciador de segredos, mantenha-os fora dos logs e faça sua rotação conforme a política da sua organização.
- **Confiabilidade dos executores:** sistemas públicos de CI, pull requests originados de forks ou máquinas compartilhadas podem expor tokens a pessoas de fora do seu workspace. Use tokens de acesso somente em executores confiáveis.
- **Identidades compartilhadas:** reutilizar o token de uma pessoa em equipes sem relação entre si torna menos claras a identificação do responsável e as trilhas de auditoria. Crie tokens para um responsável específico pelo fluxo de trabalho.
- **Credenciais desatualizadas:** tokens de longa duração podem continuar ativos após mudanças no fluxo de trabalho. Prefira tokens com prazo limitado e revogue os que não estiverem mais em uso.
- **Escopo ou tipo de credencial incorreto:** automações do Codex exigem acesso ao Codex,
  o acionamento de agentes do workspace exige acesso a Agentes do workspace, e chamadas gerais à API da OpenAI
  exigem chaves de API da Plataforma. Se **Escopos** aparecer, conceda apenas as
  permissões exigidas pelo fluxo de trabalho.

## Habilitar a criação de tokens de acesso

Use a permissão para tokens de acesso nas configurações do workspace para habilitar a criação de tokens de acesso para os membros autorizados.

A permissão para tokens de acesso controla a criação de tokens. Ela não concede acesso ao
aplicativo do ChatGPT para desktop, à Codex CLI ou à extensão para IDE e não altera o
tipo de licença, a função predefinida no workspace nem o perfil de permissões do ambiente de execução local
do membro. Os fluxos de trabalho da Codex CLI e do App Server autenticados por token também exigem
a permissão de uso local do Codex para o usuário.

Para entender a relação entre esses controles, consulte
[Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions).

  
    
  

1. Peça a um proprietário do workspace que abra
[Configurações do workspace \> Permissões e funções](https://chatgpt.com/admin/permissions).
2. Se a seção **Tokens de acesso** aparecer, ative **Permitir que os usuários criem
   tokens de acesso pessoal**. Se essa seção não estiver disponível, ative **Permitir que
   os membros usem tokens de acesso do Codex** em **Codex e Work Local** ou
**Codex Local**.
3. Ative a permissão correspondente de uso local do Codex para o responsável pelo fluxo de trabalho:
**Permitir que os membros usem o Codex e o Work localmente** em **Codex e Work Local**,
   ou **Permitir que os membros usem o Codex localmente** em **Codex Local**. Quando **Work
   Local** tem sua própria seção, **Usar o Work localmente** controla o Work e não é
   necessário para tokens do Codex.

Permita a criação de tokens de acesso apenas a pessoas ou responsáveis por serviços que conheçam o local de armazenamento do token, a automação à qual ele se destina e o cronograma de rotação.

Desativar a permissão de uso local do Codex suspende os tokens ativos do Codex pertencentes aos membros
afetados; não os revoga. Restaurar o acesso local ao Codex reativa esses
tokens. Revogue os tokens quando o acesso deles precisar ser encerrado permanentemente.

## Definir um limite de expiração para tokens de acesso

Um proprietário do workspace pode definir o prazo máximo de validade que os membros podem escolher
para novos tokens de acesso. Abra
[Configurações do workspace \> Permissões e funções](https://chatgpt.com/admin/permissions).
Se a seção **Tokens de acesso** aparecer, configure o **Limite de expiração do token de acesso**
nessa seção. Caso contrário, procure essa configuração em **Codex e Work Local** ou
**Codex Local**.

  
    
  

O limite se aplica aos novos tokens de acesso. Os tokens existentes mantêm o prazo de validade atual.

## Criar um token de acesso

Use a página Tokens de acesso para dar um nome ao token, revisar os escopos de produto
disponíveis e escolher um prazo de validade adequado.

1. Acesse [Tokens de acesso](https://chatgpt.com/admin/access-tokens).
2. Selecione **Criar**.

  
    
  

3. Insira um nome descritivo, como `release-ci` ou `nightly-docs-check`.

  
    
  

4. Se a caixa de diálogo mostrar **Escopos**, selecione **Codex**. Selecione **Agentes do
   workspace** somente se o mesmo fluxo de trabalho também precisar acionar um agente do workspace.
   Se a caixa de diálogo não tiver um seletor de escopo, ela criará um token exclusivo do Codex.
5. Escolha um prazo de validade finito, como 7, 30, 60 ou 90 dias. Os tokens de acesso pessoal
   com escopos definidos devem expirar. Uma versão anterior da caixa de diálogo, exclusiva do Codex,
   pode oferecer a opção **Sem expiração**; evite essa opção, a menos que sua organização
   a aprove e faça a rotação do token de acordo com um cronograma definido.
6. Selecione **Criar**.
7. Copie imediatamente o token de acesso gerado. Você não poderá vê-lo novamente depois
que fechar a caixa de diálogo.
8. Armazene o token no seu gerenciador de segredos ou no armazenamento de segredos de CI.

O menor prazo de validade personalizado é de um dia. Você não pode usar tokens revogados ou expirados para iniciar novas execuções autenticadas.

## Usar um token de acesso com a Codex CLI

Se a caixa de diálogo de criação do token indicar uma versão necessária da Codex CLI, atualize a CLI
para essa versão ou uma posterior antes de usar o token.

Para automações efêmeras, armazene o token em `CODEX_ACCESS_TOKEN` e execute a Codex CLI normalmente:

```bash

codex exec --json "review this repository and summarize the top risks"

Para um login local persistente, encaminhe o token para a entrada padrão de `codex login --with-access-token`:

```bash
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "summarize the last release diff"

`codex login --with-access-token` armazena uma credencial de identidade de agente no armazenamento de autenticação da Codex CLI. Se preferir não persistir credenciais na máquina, use a variável do ambiente `CODEX_ACCESS_TOKEN`.

`codex app-server` pode usar a mesma credencial por meio de `CODEX_ACCESS_TOKEN` ou
de um login criado com `codex login --with-access-token` para autenticar suas
solicitações à OpenAI. Essa credencial é separada da autenticação de transporte
entre o cliente e o App Server. Para uma conexão WebSocket remota, configure um
token de portador ou de capacidade separado, conforme descrito em
[App Server](/pt-BR/codex/app-server); não reutilize o token de acesso do Codex como
token de transporte. Consulte
[Variáveis do ambiente para autenticação e rede](/pt-BR/codex/config-file/environment-variables#authentication-and-network).

## Fazer a rotação ou revogar um token

Faça a rotação dos tokens de acesso da mesma forma que faz com outros segredos de automação:

1. Crie um token substituto.
2. Atualize o segredo no executor, no agendador ou no gerenciador de segredos.
3. Execute um teste de fumaça com o novo token.
4. Revogue o token antigo na página [Tokens de acesso](https://chatgpt.com/admin/access-tokens).

Na página Tokens de acesso, proprietários e administradores do workspace podem revogar qualquer token do workspace. Membros com permissão para tokens de acesso podem revogar somente os tokens que criaram.

## Modelo de permissões

A permissão para tokens de acesso do workspace controla a criação de tokens. Dependendo de
como o workspace está organizado, a opção **Permitir que membros usem o Codex e o Work localmente** em
**Codex e Work Local**, ou **Permitir que membros usem o Codex localmente** em **Codex
Local**, controla o acesso local ao Codex. Se **Work Local** tiver uma seção própria,
**Usar o Work localmente** controla o Work e não concede acesso ao Codex. Um membro
precisa tanto de acesso local ao Codex quanto da permissão para tokens de acesso para executar fluxos de trabalho do
Codex autenticados por token. Um membro pode ter acesso local ao Codex sem permissão para
criar tokens de acesso.

| Capacidade                                                    | Proprietários e administradores do workspace                      | Membro com permissão para tokens de acesso           | Membro sem permissão para tokens de acesso |
| ------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------- | -------------------------------------- |
| Abrir [Tokens de acesso](https://chatgpt.com/admin/access-tokens) | Sim                                              | Sim                                           | Não                                     |
| Criar tokens de acesso                                          | Sim, para a própria identidade no workspace do ChatGPT    | Sim, para a própria identidade no workspace do ChatGPT | Não                                     |
| Listar tokens de acesso                                            | Lista de tokens do workspace, incluindo quem criou cada token | Somente os tokens que criou                      | Não                                     |
| Revogar tokens de acesso na página Tokens de acesso              | Qualquer token do workspace                       | Somente os tokens que criou                      | Sem acesso à página                         |
| Conceder ou remover a permissão para tokens de acesso                       | Somente o proprietário do workspace                             | Não                                            | Não                                     |
| Gerenciar outras configurações de clientes locais ou do Codex Cloud             | Sim, conforme as permissões administrativas do workspace        | Não, a menos que um proprietário conceda acesso             | Não                                     |

Em resumo: proprietários e administradores do workspace gerenciam o acesso no nível do workspace.
Os membros precisam da permissão para tokens de acesso para criar e gerenciar os próprios tokens,
mas essa permissão não concede direitos administrativos nem acesso aos tokens de outros
membros.

## Solução de problemas

### A página Tokens de acesso retorna um erro 404 ou de acesso proibido

Peça a um proprietário do workspace que confirme se sua função inclui **Permitir que usuários
criem tokens de acesso pessoal** ou **Permitir que membros usem tokens de acesso
do Codex**, dependendo da interface disponível. Para um fluxo de trabalho do Codex autenticado por token,
confirme também se a opção **Permitir que membros usem o Codex e o Work
localmente** ou **Permitir que membros usem o Codex localmente** está ativa.

### `codex login --with-access-token` falha

Confirme se você copiou o token de acesso gerado, e não um token de sessão do navegador
ou uma chave de API da Plataforma. Confirme também se o token está ativo, não expirou
e pertence a um usuário com a permissão necessária para usar o Codex localmente.

## Documentação relacionada

- [Autenticação](/pt-BR/codex/auth)
- [Contas de serviço](/pt-BR/codex/enterprise/service-accounts)
- [Modo não interativo](/pt-BR/codex/non-interactive-mode)
- [Guia de implementação para administradores](/pt-BR/codex/enterprise/admin-setup)
- [Grupos e provisionamento](/pt-BR/codex/enterprise/groups-and-provisioning)
- [Gerenciamento do ciclo de vida de usuários](/pt-BR/codex/enterprise/user-lifecycle)
- [Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions)
- [Governança](/pt-BR/codex/enterprise/governance)

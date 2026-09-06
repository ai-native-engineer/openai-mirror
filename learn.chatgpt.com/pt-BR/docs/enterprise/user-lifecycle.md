<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/user-lifecycle -->

Use este guia para conceder aos funcionários o acesso adequado ao workspace do ChatGPT quando
entrarem na organização, atualizar esse acesso quando suas responsabilidades mudarem e removê-lo
quando saírem. O processo também abrange licenças do workspace, funções baseadas em grupos,
tokens de acesso do Codex e sistemas conectados com controles de acesso próprios.

O login único (SSO) verifica a identidade de um funcionário. O provisionamento adiciona o
funcionário a um workspace. Nenhuma dessas ações, isoladamente, determina a licença do funcionário,
as permissões de recursos, a política de execução local ou o acesso a um sistema externo.

Gerencie o acesso dos funcionários em três etapas do ciclo de vida:

- **Entrada:** Provisione o acesso ao workspace, os grupos, as funções e a licença correta.
- **Mudança:** Atualize os grupos do funcionário e remova apenas as funções diretas obsoletas.
- **Saída:** Remova o acesso ao workspace, revogue os tokens e revise os sistemas conectados.

## Verifique os pré-requisitos e defina os responsáveis

Antes de integrar os funcionários, identifique quem controla cada parte do ciclo de vida:

| Responsável                     | Responsabilidade                                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| Proprietário do workspace           | Habilitar a sincronização de diretórios, atribuir funções no workspace, aprovar tipos de licença e revisar o acesso para auditoria |
| Administrador de identidade    | Configurar o provedor de identidade, as atribuições de aplicativos, os grupos de provisionamento e o status da sincronização        |
| Administrador do workspace   | Revisar os membros do workspace, a participação em grupos e as configurações de administração disponíveis                     |
| Responsável pela segurança ou pelo serviço | Revisar os tokens do Codex, os sistemas conectados, as automações compartilhadas e as evidências de auditoria exigidas                |

Confirme o workspace de destino, verifique o domínio de e-mail da organização quando
necessário e identifique um proprietário do workspace que possa habilitar a sincronização
de diretórios. Em seguida, confira quais controles estão disponíveis no plano do workspace:

| Recurso                                 | Planos de workspace compatíveis                                                                                    |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| Sincronização de diretórios via SCIM     | ChatGPT Enterprise, Edu e Healthcare                                                                      |
| Funções personalizadas e controle de acesso baseado em funções | ChatGPT Enterprise, Edu, Healthcare e Teachers                                                            |
| Tokens de acesso do Codex                        | ChatGPT Business e Enterprise                                                                              |
| Licenças exclusivas do Codex                           | Workspaces Enterprise elegíveis e workspaces Business existentes que atendam aos critérios; indisponível para Edu, Teachers ou Healthcare |

SCIM é a sigla de System for Cross-domain Identity Management. Um workspace Business
pode oferecer suporte a tokens de acesso do Codex sem SCIM, enquanto um workspace Edu
pode oferecer suporte a SCIM sem tokens de acesso do Codex nem licenças exclusivas do Codex. Aplique apenas
os controles disponíveis no seu workspace.

Um workspace Business só pode manter e adicionar licenças exclusivas do Codex se já tinha uma licença
do Codex antes de 24 de junho de 2026 ou um convite pendente elegível para uma licença do Codex
nessa data. Novos workspaces Business e workspaces sem uma licença ou um convite elegível
não podem adicionar sua primeira licença exclusiva do Codex. Consulte
[Gerenciar o ciclo de vida e a migração de workspaces no ChatGPT Business](https://help.openai.com/en/articles/8801890-managing-workspace-lifecycle-and-migration-in-chatgpt-business).

Quando o workspace oferecer suporte a mais de um tipo de licença, revise o padrão em
**Configurações do workspace \> Identidade e acesso** antes de habilitar o provisionamento
automatizado. Os usuários provisionados via SCIM herdam esse padrão, e a licença determina
quais interfaces do produto ficam disponíveis. Uma função personalizada não pode conceder acesso
que a licença não inclua.

Use **Permissões e funções** para inspecionar os controles de acesso local, tokens de acesso,
validade de credenciais e dispositivos remotos. Alguns workspaces combinam o acesso
local em **Codex e Work Local**, com o controle **Permitir que os membros usem Codex e
Work localmente** . Outros separam **Codex Local**, com **Permitir que os membros
usem Codex localmente**, de **Work Local**, com **Usar Work localmente**.
Quando Codex e Work têm controles separados, conceder acesso a um não concede acesso ao outro. Os controles
de tokens aparecem na seção de acesso local ou em uma seção separada de **Tokens
de acesso** . Essas configurações são independentes da participação em grupos e
dos tipos de licença atribuídos.

O exemplo a seguir mostra os controles combinados de **Codex e Work Local** e uma
seção separada de **Tokens de acesso** :

  

Para consultar os pré-requisitos atuais e os padrões de identidade compatíveis, veja
[Identidade e provisionamento](https://help.openai.com/en/articles/9672121)
e [Gerenciar membros, tipos de licença, funções e acesso](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise).

## Escolha como os funcionários entram no workspace

Escolha um método principal de provisionamento para cada público:

| Método                     | Como o acesso é concedido                                                       | Onde remover o acesso                                  |
| -------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------- |
| Convite manual          | Um proprietário ou administrador do workspace convida um funcionário                          | Administração de membros do workspace                         |
| Criação automática de contas | Um funcionário com um domínio de e-mail elegível faz login                      | Administração do workspace e fluxo de identidade correspondente |
| Sincronização de diretórios com SCIM   | Um administrador de identidade atribui o funcionário no provedor de identidade | O aplicativo ou grupo de provisionamento no provedor de identidade |

Use convites manuais para um pequeno projeto-piloto ou um grupo que não seja gerenciado por
sincronização de diretórios. Use SCIM quando a participação no workspace precisar acompanhar
as alterações no provedor de identidade conforme os funcionários entrarem, mudarem de equipe ou saírem.

Não habilite a Criação automática de contas e o SCIM ao mesmo tempo. Os usuários adicionados pela
Criação automática de contas podem não ser gerenciados pelo SCIM. Por isso, removê-los de
um grupo do provedor de identidade pode não remover seu acesso ao workspace. Consulte as
[Perguntas frequentes sobre a integração SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
para ver as orientações atuais.

O SCIM pode conectar um único workspace do ChatGPT ou o locatário de uma organização,
dependendo da configuração de identidade aprovada. Mantenha explícita cada atribuição de workspace
e produto. Uma conexão de diretório compartilhada não concede nem remove automaticamente
o acesso em todos os workspaces ou organizações da Plataforma de API.

## Conecte um grupo de provisionamento ao workspace correto

Configure a conexão antes de adicionar o primeiro funcionário do projeto-piloto. O proprietário
do workspace e o administrador de identidade têm responsabilidades distintas:

1. Peça ao proprietário do workspace que selecione o workspace pretendido do ChatGPT e inspecione
**Configurações do workspace \> Grupos**. Registre os nomes dos grupos existentes, seus membros,
   as atribuições de funções personalizadas e os compartilhamentos relevantes de projetos ou GPTs.
2. Peça ao administrador de identidade que identifique o grupo exato do provedor de identidade
que será sincronizado. Compare seu nome e seus membros com os de todos os
grupos existentes no workspace.
3. Se um grupo sincronizado tiver o mesmo nome de um grupo existente no workspace,
resolva o conflito ou renomeie o grupo antes de habilitar a sincronização.
Peça ao proprietário do workspace que aprove os membros, as funções herdadas e os
compartilhamentos resultantes. Um grupo existente com o mesmo nome passa a ser gerenciado pelo SCIM,
e o controle de seus membros é transferido para o provedor de identidade.
4. Selecione um grupo-piloto com escopo restrito e registre o workspace aprovado,
os funcionários esperados e as atribuições de funções aos grupos.
5. Peça ao proprietário do workspace que abra **Configurações do workspace \> Identidade e acesso**
   e selecione **Habilitar sincronização de diretórios**. Se solicitado, escolha **Usar SCIM apenas
   neste workspace** para provisionamento no nível do workspace ou **Manter a opção
   de expandir para outros produtos** para provisionamento aprovado no nível do locatário. Se
   o SCIM no nível do locatário já estiver ativo, gerencie essa conexão existente
   em vez de criar uma segunda conexão de workspace.
6. Peça ao administrador de identidade que conclua a conexão com o provedor de identidade,
selecione o aplicativo ChatGPT e atribua o grupo aprovado para provisionar
membros no workspace pretendido.
7. Em **Configurações do workspace \> Grupos**, confirme que o grupo selecionado exibe
   o selo SCIM. Verifique o nome do grupo, os membros sincronizados e o workspace
   de destino antes de usar o grupo para conceder acesso.
8. Peça ao proprietário do workspace que abra **Permissões e funções \> Funções personalizadas**,
   crie ou selecione a função aprovada e a atribua ao grupo sincronizado.
   A configuração de funções está disponível na Web e exige acesso de
   proprietário do workspace.
9. Revise as permissões efetivas do grupo e o tipo de licença padrão do workspace
antes de adicionar um funcionário com perfil representativo para o piloto.

O administrador do provedor de identidade controla a atribuição a aplicativos e a participação em grupos;
o proprietário do workspace controla a sincronização de diretórios e a atribuição de funções
no workspace. Consulte as [Perguntas frequentes sobre a integração SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
e [Configurar o controle de acesso baseado em funções](https://help.openai.com/en/articles/11750701-rbac)
para conferir os procedimentos atuais e a disponibilidade para cada provedor.

## Provisione o acesso de um novo funcionário

Para um funcionário gerenciado por SCIM:

1. Confirme o workspace pretendido, o endereço de e-mail verificado, o tipo de licença padrão
e o grupo no provedor de identidade.
2. Atribua o funcionário ao aplicativo ChatGPT ou ao grupo que concede acesso
no provedor de identidade.
3. Aguarde a conclusão da sincronização de diretórios. Verifique o status atual
no provedor de identidade se o funcionário não aparecer.
4. Em **Configurações do workspace \> Membros**, verifique o e-mail do funcionário,
   sua participação no workspace ou convite pendente, o tipo de licença e o selo SCIM.
5. Em **Configurações do workspace \> Grupos**, confirme que o funcionário pertence ao
   grupo sincronizado pretendido. Peça ao proprietário do workspace que verifique a função
   personalizada atribuída a esse grupo.
6. Peça a um funcionário com perfil representativo que entre no workspace correto e verifique
as interfaces do produto, os recursos e os sistemas conectados específicos de que precisa.
7. Registre o responsável pelo acesso e a verificação bem-sucedida usando
o processo aprovado pela sua organização.

Se você adicionar um funcionário manualmente, envie o convite pela administração de membros
do workspace e realize as mesmas verificações de licença, grupo, função e login.

Um grupo organiza os membros, mas não concede acesso a todos os recursos por si só.
Para conferir o procedimento atual de atribuição de funções, consulte
[Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions)
e [Configurar o controle de acesso baseado em funções](https://help.openai.com/en/articles/11750701-rbac).

## Atualize o acesso quando um funcionário mudar de equipe

Um funcionário que muda de equipe pode manter o acesso concedido por grupos ou funções
anteriores. Atualize a origem que gerencia a participação dele antes de verificar
o novo nível de acesso:

1. Identifique a nova equipe do funcionário, o workspace necessário, a licença, as permissões
aprovadas para os recursos e o grupo de destino.
2. Adicione o funcionário ao grupo de destino aprovado antes de removê-lo
do grupo anterior se ele precisar permanecer no workspace durante toda
a mudança. Atualize a participação gerenciada por SCIM no provedor de identidade;
atualize a participação gerenciada manualmente pela administração do workspace.
3. Confirme que a função aprovada já está atribuída ao grupo de destino.
Preserve as atribuições de funções existentes nos grupos compartilhados para que os outros membros
mantenham o acesso aprovado.
4. Peça a um proprietário do workspace que altere a atribuição de uma função a um grupo somente após
aprovar uma mudança de política separada para todo o grupo e revisar seu efeito
sobre cada membro.
5. Peça a um proprietário do workspace que abra o perfil do funcionário, revise **Funções diretas**
   e remova as funções obsoletas atribuídas diretamente a essa pessoa. As funções personalizadas usam **Padrão**,
**Ativado** e **Desativado**. Um **Desativado** explícito em qualquer função atribuída prevalece sobre
**Ativado** em outra função.
6. Revise as permissões efetivas do funcionário em todas as funções atribuídas diretamente
e por meio de grupos antes de aprovar a mudança de equipe.
7. Se o workspace oferecer suporte a mais de um tipo de licença, peça a um proprietário do workspace que abra
**Configurações do workspace \> Membros \> Alterar tipo de licença** e revise
   o acesso aos produtos pretendido para o funcionário.
8. Antes de converter uma licença do ChatGPT em uma licença exclusiva do Codex, confirme que o
funcionário deve perder o acesso a chats, memórias, projetos e outros
recursos do ChatGPT. Os dados subjacentes não são excluídos e ficam disponíveis
novamente se o funcionário voltar a ter uma licença do ChatGPT.
9. Após a conclusão da sincronização e das atualizações de permissões, verifique tanto as ações
recém-permitidas quanto as que não devem mais estar disponíveis.

Se o funcionário for responsável por um fluxo de trabalho de automação, avalie se o token do Codex,
a entrada no gerenciador de segredos ou a autorização do serviço conectado devem ser transferidos
para outro responsável aprovado. Remover a permissão de uso local do Codex do funcionário suspende
os tokens do Codex dele, mas não os revoga. Restaurar a permissão
reativa esses tokens, portanto revogue as credenciais que devem perder o acesso permanentemente.

## Remova um funcionário que está saindo

Comece pelo sistema que gerencia a participação do funcionário no workspace:

1. Determine se o funcionário é gerenciado por SCIM ou se um administrador o adicionou
manualmente.
2. Para um funcionário gerenciado por SCIM, remova sua atribuição ao aplicativo ChatGPT
e remova-o de todos os grupos de provisionamento que concedem acesso
no provedor de identidade. Não remova os próprios grupos compartilhados.
3. Para um funcionário que não é gerenciado por SCIM, peça a um proprietário ou
   administrador do workspace que remova o membro em **Configurações do workspace \> Membros**.
4. Confirme que o membro não está mais no workspace pretendido.
Para acessos gerenciados por SCIM, verifique se a sincronização foi concluída e se nenhuma
outra atribuição no provedor de identidade pode restaurar a participação.
5. Registre a remoção concluída e designe um responsável para revisar os tokens,
os sistemas conectados e os dados retidos.

Não confie apenas na remoção feita no workspace enquanto o provedor de identidade ainda mantiver
o funcionário atribuído a um grupo gerenciado por SCIM. Uma sincronização posterior pode adicionar
o funcionário novamente ao workspace.

### Revogue tokens de acesso do Codex e transfira a automação

Remover uma pessoa do workspace não substitui uma revisão explícita das
credenciais usadas por automações confiáveis. Aplique este procedimento somente quando o
workspace oferecer suporte a tokens de acesso do Codex e eles estiverem habilitados.

Remover a permissão de uso local do Codex suspende os tokens existentes, mas não os revoga.
Esses tokens podem voltar a funcionar se um proprietário do workspace restaurar a permissão,
portanto revogue explicitamente as credenciais que devem perder o acesso permanentemente.

A página **Tokens de acesso** identifica o criador e o status de cada token. Use
**Revogar** para remover o acesso dos tokens ativos:

  

1. Peça a um proprietário ou administrador do workspace que abra
[Tokens de acesso](https://chatgpt.com/admin/access-tokens).
2. Identifique os tokens criados pelo funcionário que está saindo e os fluxos de trabalho que usam
esses tokens.
3. Escolha a identidade substituta. Para um fluxo de trabalho duradouro com identidade não humana em um
   plano elegível de pagamento conforme o uso, use uma [conta de
   serviço](/pt-BR/codex/enterprise/service-accounts) dedicada e aprovada. Caso contrário, identifique um
   responsável ativo e aprovado pelo fluxo de trabalho. Peça a um proprietário do workspace que conceda a essa pessoa
   permissão para criar tokens de acesso, se necessário, e confirme que ela tem
   permissão de uso local do Codex.
4. Crie o token substituto. Um operador autorizado de conta de serviço pode
   criar um token na página de detalhes da conta de serviço. Para uma substituição por um token pessoal,
   peça ao novo responsável pelo fluxo de trabalho que crie um token para sua própria
   identidade no workspace do ChatGPT. Se a caixa de diálogo exibir **Escopos**, selecione
**Codex**. Selecione outros escopos somente quando o fluxo de trabalho precisar deles. Uma
   caixa de diálogo sem **Escopos** cria um token exclusivo do Codex. Um administrador não pode
   criar um token pessoal em nome de outro usuário.
5. Atualize o segredo armazenado do fluxo de trabalho e verifique se ele é executado com sucesso
usando o token substituto.
6. Peça ao proprietário ou administrador do workspace que revogue os tokens do funcionário que está saindo
e todas as credenciais substituídas.
7. Confirme que os tokens revogados não podem mais iniciar novas execuções autenticadas.

Quando um novo responsável aprovado criar um token, use um nome descritivo para o fluxo de trabalho
e escolha o menor prazo de validade da credencial permitido pela política
da sua organização. Se **Escopos** aparecer, selecione **Codex** e evite permissões de que o
fluxo de trabalho não precisa. O exemplo a seguir mostra a interface com escopos:

  

Proprietários e administradores de um workspace podem revogar qualquer token desse workspace. Um membro
com permissão para tokens de acesso pode revogar somente os tokens que criou. Para conferir as permissões
atuais dos tokens e as etapas de rotação, consulte
[Tokens de acesso](/pt-BR/codex/enterprise/access-tokens#rotate-or-revoke-a-token).

### Revise os sistemas conectados e os dados retidos

O provisionamento do workspace não gerencia todos os limites de autorização. Peça ao
responsável pelo serviço em questão que revise o acesso a:

- Repositórios de código-fonte e contas conectadas do GitHub.
- Google Drive, Slack e outros aplicativos conectados.
- Plug-ins instalados, habilidades incluídas e capacidades baseadas em conectores.
- Ambientes hospedados do Codex, automações compartilhadas e segredos armazenados.
- Dispositivos gerenciados, credenciais armazenadas localmente e sessões remotas compatíveis.
- Organizações, projetos e chaves de API separados na Plataforma de API.

Aplique os controles de cada sistema em vez de presumir que uma mudança em um grupo do workspace
ou no SCIM atualiza as permissões em todos os lugares. Consulte
[Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions)
para conferir o modelo completo dos limites de autorização e [Controles de plug-ins](/pt-BR/codex/enterprise/apps-and-connectors)
para saber mais sobre a disponibilidade de plug-ins, habilidades incluídas e permissões de aplicativos conectados.

Remover o acesso ao workspace não é o mesmo que excluir conteúdo. Quando um membro
sai, o workspace transfere automaticamente a propriedade dos projetos e GPTs
personalizados dele para um proprietário do workspace. Esses itens não são marcados para exclusão.
Se o membro retornar, a propriedade volta para ele.

Nos workspaces dos planos Enterprise e Edu, chats, arquivos e documentos do canvas seguem
a política de retenção configurada no workspace. Os workspaces Business mantêm chats,
arquivos e documentos do canvas por tempo indeterminado. Os workspaces Healthcare também oferecem
controles de retenção de dados; revise a configuração aplicável do workspace e
[as orientações do ChatGPT para o setor de saúde](https://help.openai.com/en/articles/20001046-chatgpt-for-healthcare).

Transferir a propriedade de um projeto ou GPT não transfere as conversas
ou os arquivos privados do ex-membro, e o proprietário do workspace não passa a ter acesso a esse conteúdo privado
com a mudança de propriedade. Consulte
[Remoção de membros do workspace e retenção de dados](https://help.openai.com/en/articles/8266418)
para conferir o comportamento atual específico de cada plano.

Se os requisitos de segurança ou conformidade exigirem evidências da alteração, registre o
workspace afetado, o funcionário, a atribuição no provedor de identidade, o horário de conclusão,
o responsável pela aprovação e a verificação da revogação dos tokens no sistema aprovado.
Confirme os registros disponíveis, as permissões de administrador e a retenção na
[Referência da API de administração](https://chatgpt.com/admin/api-reference), que exige autenticação.
Escopos sensíveis de conformidade podem exigir um proprietário do workspace. Para uma visão geral
do produto, consulte [API de Compliance e eventos de auditoria](/pt-BR/codex/enterprise/compliance-api).
Não deduza a cobertura de eventos, os campos ou os períodos de retenção com base neste guia.

## Solucione problemas de falta de acesso ou acesso inesperado

| Sintoma                                               | O que verificar                                                                             | Ação corretiva                                                                                                       |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Um funcionário consegue entrar, mas não encontra o workspace  | O workspace de destino, o convite, a atribuição no provedor de identidade e o endereço de e-mail         | Corrija a atribuição ou o mapeamento de e-mail e verifique se o funcionário é membro do workspace                                               |
| Um funcionário sincronizado recebe a licença errada       | O tipo de licença padrão do workspace e o registro atual do membro                     | Peça a um proprietário do workspace que revise o padrão e as opções de licença compatíveis com o funcionário                                     |
| Uma mudança de equipe não remove o acesso a um recurso                | A participação em outros grupos, as **Funções diretas** e as permissões combinadas do funcionário        | Remova o funcionário dos grupos aos quais ele não precisa mais pertencer e peça a um proprietário do workspace que revogue apenas as funções diretas desse funcionário que não são mais necessárias |
| Um grupo manual passa a ser gerenciado pelo SCIM sem aprovação  | Nomes de grupos coincidentes, membros no provedor de identidade, funções herdadas e compartilhamentos existentes    | Confira e ajuste os vínculos aprovados aos grupos no provedor de identidade e revise o acesso afetado                                 |
| Outros funcionários perdem acesso após uma mudança de equipe       | Alterações recentes nas atribuições de funções a grupos compartilhados e o acesso aprovado da equipe anterior     | Peça a um proprietário do workspace que restaure a função aprovada do grupo compartilhado e atualize apenas os vínculos do funcionário que está mudando de equipe        |
| Um token de automação para de funcionar após uma mudança de equipe | A permissão de uso local do Codex do responsável pelo fluxo de trabalho e o status atual do token                      | Peça a um proprietário do workspace que restaure o acesso local aprovado ao Codex ou substitua o token afetado e revogue o anterior                     |
| Uma alteração de acesso não aparece imediatamente           | O status de sincronização do provedor de identidade, o prazo de sincronização previsto e as atualizações recentes de funções          | Peça ao administrador de identidade que verifique a sincronização antes de entrar em contato com o Suporte da OpenAI                                        |
| Um funcionário removido volta ao workspace           | A atribuição ao aplicativo no provedor de identidade e todos os grupos de provisionamento que concedem acesso | Remova o funcionário no provedor de identidade, em vez de removê-lo apenas nas configurações do workspace                                      |
| Um funcionário em processo de desligamento ainda tem um token listado         | O criador do token, o responsável pelo fluxo de trabalho e as permissões do administrador do workspace para gerenciar tokens        | Faça a rotação de todas as credenciais necessárias à automação e revogue o token do funcionário em processo de desligamento                                   |
| Um aplicativo conectado ainda permite acesso           | A conta no sistema de origem, a disponibilidade do plug-in e a autorização concedida ao aplicativo                   | Peça ao responsável pelo serviço em questão que remova o acesso usando os controles compatíveis com esse sistema                                  |

A maioria dos provedores de identidade sincroniza a cada 30 a 40 minutos, embora alguns
apliquem atualizações imediatamente. Alterações em funções personalizadas podem levar cerca de cinco minutos para
aparecer. Não é possível forçar uma sincronização SCIM, portanto, não remova e recrie
um membro do workspace para contornar uma atualização atrasada.

Se uma remoção de acesso ou atualização de grupo ainda não tiver sido concluída após o prazo
previsto para o provedor, peça ao administrador de identidade que reúna:

- O workspace afetado e o endereço de e-mail do funcionário.
- O provedor de identidade, a atribuição ao aplicativo e o grupo de provisionamento.
- A alteração que se tentou fazer, a data e a hora da tentativa e o status de sincronização mais recente.
- As funções diretas, as funções de grupo ou os tokens que ainda precisam de revisão.

Entre em contato com o [Suporte da OpenAI](https://help.openai.com/) e forneça esses detalhes pela
Central de Ajuda. Trate a permanência do acesso de um funcionário desligado como uma exceção de
segurança e siga o processo de escalonamento de incidentes da sua organização.

Para saber como funcionam a configuração e a sincronização específicas de cada provedor, consulte as
[Perguntas frequentes sobre integração SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq) atualizadas.
Para erros de login e identidade, consulte
[Solução de problemas de autenticação](https://help.openai.com/en/articles/10489721-login-and-authentication-faq-s-and-troubleshooting-sso-scim-and-domain-verification).

## Verifique o ciclo de vida completo do funcionário

Use um funcionário de teste com perfil representativo para verificar as três transições antes de uma
implementação mais ampla:

| Etapa do ciclo de vida | Responsável principal                 | Resultado bem-sucedido                                                                                                            |
| --------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Admissão          | Administrador de identidade        | O funcionário entra no workspace correto com a licença, o grupo e o acesso aos recursos previstos                                    |
| Mudança de equipe           | Responsáveis pela identidade e proprietários do workspace | Os administradores atualizam a participação nos grupos, e os proprietários do workspace removem as funções diretas que não são mais necessárias, preservando as funções dos grupos compartilhados |
| Desligamento          | Responsáveis pela identidade e pela segurança  | Os administradores removem o acesso ao workspace, revisam os tokens compatíveis e revogam ou reatribuem o acesso externo                       |

Registre quem aprovou cada alteração, o que você verificou e quem ficará
responsável por resolver as exceções de acesso restantes. Agende revisões periódicas
de acesso de acordo com as políticas de identidade e segurança da sua organização.

## Documentação relacionada

- [Guia de implementação para administradores](/pt-BR/codex/enterprise/admin-setup)
- [Grupos e provisionamento](/pt-BR/codex/enterprise/groups-and-provisioning)
- [Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions)
- [Controles de plug-ins](/pt-BR/codex/enterprise/apps-and-connectors)
- [Tokens de acesso](/pt-BR/codex/enterprise/access-tokens)
- [Contas de serviço](/pt-BR/codex/enterprise/service-accounts)
- [Autenticação](/pt-BR/codex/auth)
- [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration)
- [API de Compliance e eventos de auditoria](/pt-BR/codex/enterprise/compliance-api)

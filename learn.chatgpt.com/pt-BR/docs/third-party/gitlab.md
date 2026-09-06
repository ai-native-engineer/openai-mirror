<!-- source: https://learn.chatgpt.com/pt-BR/docs/third-party/gitlab -->

Use a revisão de código do Codex para obter uma revisão adicional focada no que importa
nas merge requests do GitLab. O Codex analisa o diff da merge request, segue as
orientações do repositório e publica uma revisão de código padrão do GitLab, focada em problemas graves.

O suporte ao GitLab está em versão beta e disponível em todos os planos do ChatGPT. A integração do Codex
é executada no Codex Cloud. Controles de repositório semelhantes aos do GitHub no
aplicativo para desktop, como **Criar pull request**, não estão incluídos nesta versão beta.

## Antes de começar

Certifique-se de ter:

- Uma conta do GitLab conectada. O GitLab.com exige o
[fluxo de conexão padrão](https://help.openai.com/articles/20001486);
  instâncias do GitLab autogerenciado ou Dedicated exigem a
[configuração de um modelo pelo administrador do workspace](https://help.openai.com/articles/20001487).
- Um arquivo `AGENTS.md`, caso você queira que o Codex siga orientações de revisão
  específicas do repositório.

## Configure a revisão de código do Codex

### Configure a conexão com o GitLab e a identidade de revisão do Codex

No GitLab.com, conecte sua conta do GitLab ao Codex depois de
[conectar o GitLab ao ChatGPT](https://help.openai.com/articles/20001486).
No GitLab autogerenciado ou Dedicated, cada revisor deve se conectar depois que o
[modelo do administrador do workspace](https://help.openai.com/articles/20001487) tiver sido
publicado.

No GitLab autogerenciado ou Dedicated, abra **Codex Cloud** → **Configurações** →
[**Conectores**](https://chatgpt.com/codex/cloud/settings/connectors). Um
administrador do workspace pode permitir que o Codex crie uma conta de serviço ou salve um
token de acesso pessoal de uma conta de serviço existente.

#### Deixe o Codex criar a conta

Em **Codex Cloud** → **Configurações** → **Conectores**, selecione o aplicativo do seu host GitLab
autogerenciado ou Dedicated → selecione **Configurar conta de serviço** →
**Criar uma conta de serviço**. O administrador do workspace que concluir a configuração deve ter
acesso de administrador à instância do GitLab. Escolha **Grupos selecionados**
ou **Somente projetos selecionados**; depois, selecione onde o Codex deve operar e crie
a conta. A opção de grupos concede acesso Developer a cada grupo escolhido,
herdado por seus projetos e subgrupos; a opção de projetos concede acesso Developer
somente aos projetos individuais escolhidos. O Codex criará a conta de serviço de instância ChatGPT
Codex Connector com um token de acesso pessoal que tem o escopo
`api`.

#### Use uma conta existente

No GitLab, crie ou escolha uma conta de serviço e conceda a ela acesso Developer
somente nos grupos ou projetos em que o Codex deve operar. Na página **Contas
de serviço** , selecione a conta → **Gerenciar tokens de acesso** → **Adicionar novo
token** para
[criar um token de acesso pessoal](https://docs.gitlab.com/user/profile/service_accounts/#create-a-personal-access-token-for-a-service-account)
com o escopo `api` e uma data de expiração com prazo mínimo de 30 dias. De volta ao
Codex, escolha **Usar uma conta de serviço existente**, cole o token e selecione
**Salvar token**. O token é criptografado ao ser salvo e nunca mais é exibido.

#### Gerencie o token da conta de serviço

Administradores do workspace podem gerenciar a conta de serviço em **Codex Cloud** →
**Configurações** → **Conectores**. Para uma conta criada pelo Codex, os administradores podem revogar
o token atual e gerar um novo. Para uma conta existente, os administradores podem
substituir ou remover o token salvo no Codex e revogá-lo separadamente no GitLab, se
necessário. O Codex não pode responder à atividade do GitLab até que um token válido seja
configurado.

### Escolha como a atividade do GitLab chega ao Codex

#### Crie um ambiente de projeto para tarefas de programação ou configuração específica do projeto

Em **Codex Cloud** → **Configurações** → **Ambientes**, escolha o projeto do GitLab
e crie um ambiente de projeto quando quiser que o Codex escreva ou execute código
para esse projeto — por exemplo, para editar arquivos, fazer commit de alterações ou enviar atualizações para
a branch de uma merge request — ou quando uma revisão depender de segredos específicos do projeto,
acesso à rede ou comandos de configuração.

No GitLab.com, um ambiente de projeto também é necessário para habilitar revisões do Codex.

Ao criar o ambiente, ative **Ativar a atividade do Codex a partir do GitLab**
para instalar o webhook de projeto que envia eventos de merge request, comentários e issues
ao Codex. A criação do webhook de projeto exige acesso Maintainer ou Owner,
acesso de administrador ou uma função personalizada que permita administrar webhooks de
projeto. Webhooks de projeto e de grupo assinados exigem GitLab 19.0 ou versão posterior. No
GitLab 19.0 autogerenciado, confirme que a flag de recurso `webhook_signing_token` está
habilitada; ela é habilitada por padrão e foi removida no GitLab 19.1.

#### Ative a atividade para revisões do Codex em projetos de um grupo do GitLab

No GitLab autogerenciado ou Dedicated, administradores do workspace podem abrir **Ambientes**
→ **Atividade do GitLab** → **Gerenciar grupos** para habilitar revisões do Codex em um grupo
e seus subgrupos. O Codex instalará um webhook de grupo que abrange os projetos
de todo o grupo. O usuário conectado do GitLab deve ser Owner do grupo, e os
webhooks de grupo exigem GitLab Premium ou Ultimate e GitLab 19.0 ou versão posterior.

A atividade de grupo permite revisões de código, mas não cria ambientes de projeto.
Para executar tarefas de programação acionadas pelo GitLab, como editar arquivos,
executar comandos, fazer commit de alterações ou enviar atualizações a uma merge request,
crie um ambiente de projeto.

### Configure políticas de revisão de código

Configure políticas de revisão de código nas
[configurações de revisão do Codex](https://chatgpt.com/codex/cloud/settings/code-review?provider=gitlab).
Escolha a política do repositório: `Review my MRs`, `Review team MRs`,
`Review all MRs` ou `Follow personal`. Em seguida, escolha quando as revisões são executadas: **Ao abrir uma MR**,
**A cada push** ou **Gatilho inteligente (experimental)**. As configurações do repositório podem
substituir os padrões pessoais.

## Solicite uma revisão do Codex

1. Em um comentário da merge request, mencione `@codex review`.
2. Aguarde o Codex reagir (👀) e publicar uma revisão.

O Codex publica discussões e notas na merge request do GitLab, como faria um
colega de equipe. Por padrão, revisões solicitadas manualmente podem incluir apontamentos P0, P1 e
P2, enquanto as revisões automáticas se concentram em apontamentos P0 e P1.

## Ative revisões automáticas

Para revisar automaticamente as merge requests elegíveis, ative **Revisões
automáticas** nas configurações do Codex, escolha a política do repositório do GitLab e escolha um
gatilho: **Ao abrir uma MR**, **A cada push** ou **Gatilho inteligente (experimental)**.
O Codex é executado sem um comentário `@codex review` quando o evento de merge request
corresponde a essa política e a esse gatilho.

A atividade do GitLab deve ser habilitada por meio de um webhook de projeto ou de
um webhook de grupo ancestral. No GitLab autogerenciado ou Dedicated, a conta de
serviço configurada também precisa ter permissão de escrita no projeto. Quando há
um ambiente de projeto configurado, o Codex o utiliza. Se um grupo ancestral já habilita
a atividade, os projetos descendentes herdam essa cobertura.

## Personalize o que o Codex revisa

O Codex procura arquivos `AGENTS.md` no repositório e segue as regras aplicáveis
de revisão de código. Adicione uma seção `## Code Review Rules` ao arquivo mais próximo do
código regido por essas regras. Use títulos `###` para agrupar verificações relacionadas quando
for útil.

Por exemplo, um serviço de relatórios de experimentos pode impedir que o comportamento pós-exposição
altere uma coorte de comparação:

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Coloque regras aplicáveis a todo o repositório no arquivo `AGENTS.md` da raiz e regras específicas de um serviço em
um arquivo aninhado, como `services/experiment_reporting/AGENTS.md`. O Codex aplica
as orientações da raiz e as orientações mais específicas aplicáveis a cada arquivo alterado; assim, alterações
não relacionadas não precisam incluir o contexto específico do serviço.

Comece com duas ou três regras concisas que descrevam verificações que os revisores costumam
explicar. Regras úteis:

- **Concentre-se em comportamentos relevantes e específicos do repositório.** Descreva a
  restrição de compatibilidade, o limite de dados ou o efeito colateral inseguro que deve ser sinalizado
  e explique por que ele é importante.
- **Indique o caminho seguro ou a exceção.** Forneça contexto suficiente para o Codex distinguir
  um problema real de um comportamento esperado.
- **Mantenha regras duradouras e com escopo delimitado.** Priorize resultados em vez de nomes de funções que
  podem mudar e coloque as orientações perto do código ao qual se aplicam.
- **Deixe as verificações mecânicas para a CI.** Mantenha formatação, lint e outras
  verificações determinísticas fora das regras de revisão.

Abra uma merge request representativa e solicite uma revisão com `@codex review`.
Refine as regras com base nos apontamentos e no feedback recebidos e restrinja ou
remova orientações que gerem ruído.

As regras de revisão de código orientam o Codex; elas não substituem testes,
proteções de branch ou aprovações obrigatórias.

Para definir um foco pontual, inclua-o no comentário da merge request:

`@codex review for issues in the database migration`

## Trate os apontamentos da revisão

Corrigir apontamentos da revisão exige um **ambiente de projeto configurado**; a atividade
de grupo, por si só, permite revisões, mas não pode executar tarefas de programação. Se o projeto tiver
um ambiente, peça ao Codex que corrija um problema na mesma merge request adicionando
outro comentário:

```md
@codex fix the P1 issue

O Codex inicia um [chat na nuvem](/pt-BR/codex/cloud) usando a merge request como contexto e
pode enviar uma correção para a branch quando tem permissão para isso.

## Atribua outras tarefas ao Codex

Outras tarefas de programação também exigem um **ambiente de projeto configurado**; a atividade
de grupo, por si só, permite revisões. Se você mencionar `@codex` em um comentário com
qualquer conteúdo diferente de `review`, o Codex iniciará um [chat na nuvem](/pt-BR/codex/cloud) usando
sua merge request como contexto.

```md
@codex fix the CI failures

## Solucione problemas de revisão de código

Se o Codex não reagir nem publicar uma revisão:

- Confirme que o aplicativo do GitLab desejado foi selecionado; se você usa uma configuração específica
do projeto, confirme que ele tem o ambiente esperado do Codex Cloud.
- Confirme a atividade do projeto ou de um grupo ancestral. No GitLab, verifique
**Webhooks** →
[**Eventos recentes**](https://docs.gitlab.com/user/project/integrations/webhooks/)
  e confirme que as entregas de eventos de merge request e de notas foram bem-sucedidas.
- No GitLab autogerenciado ou Dedicated, confirme que o webhook do projeto ou do grupo está
  assinado, a verificação SSL está habilitada e a instância usa o GitLab 19.0 ou uma versão
  posterior. No GitLab 19.0 autogerenciado, confirme que a flag de recurso `webhook_signing_token`
  está habilitada; corrija os hooks desativados automaticamente após falhas.
- No GitLab autogerenciado ou Dedicated, confirme que o token de acesso pessoal de uma conta
  de serviço existente está ativo e tem o escopo `api`. Se o Codex tiver criado a
  conta de serviço, confirme que ela está configurada corretamente nas
[configurações de conectores do Codex](https://chatgpt.com/codex/cloud/settings/connectors)
  e que o projeto ou grupo está habilitado.
- No GitLab autogerenciado ou Dedicated, confirme que a conta de serviço do workspace
— e não apenas o usuário conectado do GitLab — tem acesso Developer ao projeto ou a um grupo
pai, para que o Codex possa publicar revisões e reações. A associação é
herdada; a atividade e o acesso da conta de serviço são independentes.
- Confirme se **Revisão de código** ou **Revisões automáticas** está habilitada e se a MR corresponde
  à política e ao gatilho do repositório.
- Use `@codex review`.

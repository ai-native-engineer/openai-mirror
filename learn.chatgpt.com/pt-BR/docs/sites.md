<!-- source: https://learn.chatgpt.com/pt-BR/docs/sites -->

Sites está em versão beta pública e está disponível nos planos ChatGPT Plus, Pro, Business,
Enterprise e Edu. Durante a versão beta, limites de uso específicos de cada plano se aplicam a todos os Sites.
O ChatGPT mostra os limites atuais e avisa quando você se aproxima de um deles.
Atingir um limite pode impedir que você crie um Site, adicione armazenamento ou mantenha público
um Site com alto volume de uso, mas você ainda pode editar e gerenciar os Sites existentes.

Sites permite que o ChatGPT crie, hospede, refine e compartilhe sites, aplicativos Web e jogos.
Use Sites quando quiser transformar um prompt ou um projeto existente compatível em uma
experiência hospedada sem configurar um fluxo de trabalho de implantação separado.

Abra **Sites** no aplicativo do ChatGPT para desktop. Você pode criar um site a partir de um prompt ou
de um projeto local compatível e depois voltar à visualização de Sites para gerenciá-lo.

Use Sites no ChatGPT na Web para criar e gerenciar sites hospedados. Selecione
**Mais** \> **Sites** ou acesse diretamente
[chatgpt.com/sites](https://chatgpt.com/sites) para encontrar os Sites que você criou.

Sites não oferece uma visualização independente de gerenciamento na Codex CLI. Use o ChatGPT na Web ou
o aplicativo para desktop para criar, salvar, implantar e gerenciar um projeto do Sites. Você
ainda pode usar a Codex CLI para editar e testar um projeto local antes de publicá-lo.

Sites não oferece uma visualização independente de gerenciamento na extensão para IDE. Use o ChatGPT na Web
ou o aplicativo para desktop para as operações do Sites e use a extensão para IDE para editar e
testar o projeto de código-fonte local.

  Toda URL de implantação do Sites corresponde a uma implantação em produção. Se quiser revisar uma
compilação antes que ela entre no ar, peça ao ChatGPT para salvar uma versão sem
implantá-la.

## Primeiros passos com Sites

No ChatGPT, inclua a palavra "website" no prompt ou mencione `@Sites` para
iniciar explicitamente o fluxo de trabalho do Sites.

1. Descreva o Site

   Descreva o público, a finalidade, o comportamento necessário e as informações que o Site
deve usar.

2. Revise o Site

   Revise o conteúdo e o comportamento gerados. Confira se o Site usa as
informações pretendidas e trata os dados conforme o esperado.

3. Refine o Site

   Descreva as alterações desejadas. Adicione arquivos relevantes ou contexto visual quando
isso ajudar o ChatGPT a fazer a alteração.

4. Gerencie e compartilhe o Site

   Volte para **Sites** para reabrir ou refinar o Site. Quando estiver pronto, escolha quem
   pode acessá-lo e compartilhe o link gerado.

Na prévia, selecione **Editar**. Em **Descreva as alterações no site**, descreva as
alterações desejadas. Use **Captura de tela** ou **Adicionar arquivos e mais opções** quando um
contexto adicional puder ajudar.

## Use prompts no Sites para tarefas comuns

Para um novo site, painel ou ferramenta interna, inclua o público, a experiência
principal e as informações necessárias:

```text
Build a project request dashboard for my operations team. Let team members
submit requests, see who owns each one, update the status, and filter the list.
Require people to sign in with their workspace account, and keep the request
data saved between visits.

Para um projeto existente, peça ao Sites para preparar e publicar o aplicativo atual:

```text
Deploy this project with Sites. Check whether it is compatible, make any
required changes, and give me the deployment URL.

Quando um site precisar de dados persistentes do aplicativo ou arquivos enviados, informe isso na
solicitação:

```text
Add player scores and avatar uploads to this game. Keep the scores and uploaded
avatars between visits.

  Explore as [demonstrações do Sites](/showcase) para conhecer aplicativos internos implantados e os
  prompts completos usados para criá-los.

## Confira as análises do Site

Sites registra o tráfego automaticamente para que você veja como as pessoas usam um Site
implantado sem adicionar um SDK de análise. A visualização de análises mostra o total de visitantes
únicos e de visualizações de página, além da evolução das duas métricas ao longo do tempo. Altere o intervalo de datas ou
a granularidade para consultar outro período.

Abra **Sites**, encontre o Site e selecione **Mais ações** \> **Análises**.

Acesse [chatgpt.com/sites](https://chatgpt.com/sites), encontre o Site e selecione
**Mais ações** \> **Análises**.

Sites não oferece uma visualização independente de análises na CLI nem na extensão para IDE. Abra
o Site no ChatGPT na Web ou no aplicativo para desktop para consultar as análises.

  

  No momento, as análises estão disponíveis para Sites que não pertencem a um workspace
do plano Empresas.

## Adicione a opção Entrar com o ChatGPT

Sites públicos podem continuar abertos a todos e oferecer a opção Entrar com o ChatGPT
para recursos que usam a identidade do visitante, como progresso salvo, visualizações personalizadas
ou registros pertencentes a uma pessoa específica. O login é opcional. Sites restritos ao workspace já
usam a identidade do ChatGPT para aplicar suas configurações de compartilhamento.

Peça ao Sites para adicionar a experiência de login:

```text
Add Sign in with ChatGPT to this public Site. Keep the Site available to signed-out visitors. Show a Sign in with ChatGPT action when someone is signed out. After they sign in, greet them with their full name when available, or their email address otherwise. Add a Sign out action, and keep authorization decisions in server-side code.

Sites gerencia os fluxos de login e logout por meio de caminhos fornecidos pela plataforma
e depois redireciona o visitante de volta ao seu Site:

```html
<a href="/signin-with-chatgpt">Sign in with ChatGPT</a>
<a href="/signout-with-chatgpt">Sign out</a>

Depois que um visitante faz login, Sites encaminha sua identidade ao servidor por meio
destes cabeçalhos de requisição:

- `oai-authenticated-user-email` contém o endereço de e-mail autenticado.
- `oai-authenticated-user-full-name` pode conter um nome de perfil não vazio. Trate
  esse valor como opcional e use o endereço de e-mail como alternativa.

Mantenha as decisões de autorização no código do lado do servidor e não dependa de
cabeçalhos que separam o nome em partes.

## Entenda projetos, versões e implantações

Um Site é um resultado hospedado e persistente que você pode reabrir, refinar, configurar
e compartilhar em **Sites** no ChatGPT.

Um projeto do Sites vincula um projeto de código-fonte local à hospedagem gerenciada pelo Sites.
Sites armazena essa associação e os nomes opcionais dos vínculos de armazenamento em
`.openai/hosting.json`. Um projeto inicial local recém-criado pode começar sem um
`project_id`; Sites adiciona um depois de provisionar o projeto hospedado.

Por exemplo, um site provisionado que usa um vínculo com um banco de dados relacional, mas não usa
armazenamento de arquivos, pode conter:

```json
{
  "project_id": "<project-id>",
  "d1": "DB",
  "r2": null
}

Um Site continua na sua lista de Sites mesmo após o encerramento do chat do ChatGPT Work que o criou.
Você não precisa de um projeto local nem de um manifesto para iniciar um Site na Web. Um Site é
separado de um Projeto do ChatGPT.

A publicação no Sites ocorre em duas etapas separadas:

1. **Salve uma versão.** O ChatGPT gera uma versão que pode ser implantada. Para um projeto de código-fonte
   local, o ChatGPT associa a versão ao commit do Git usado na
   compilação. Use esta etapa quando quiser uma versão candidata à implantação que possa ser revisada.
2. **Implante uma versão.** O ChatGPT publica uma versão salva e informa a
   URL de produção quando a implantação é bem-sucedida. Use esta etapa somente quando quiser que
   o público selecionado acesse o site.

Peça ao ChatGPT para listar ou inspecionar as versões salvas quando precisar identificar uma
versão anterior candidata à implantação.

## Escolha um formato de site compatível

Para novos projetos, o fluxo de trabalho do Sites pode começar com o modelo inicial de Site
recomendado. Para um projeto existente, peça ao ChatGPT para confirmar se o projeto consegue
gerar artefatos de implantação compatíveis antes de solicitar uma implantação.

Descreva ao ChatGPT o comportamento necessário do produto para que ele escolha o formato de
site adequado:

| Necessidade do Site                                                      | O que pedir ao Sites                                                         |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Site ou página de destino com foco em conteúdo                            | Um Site sem estado persistente do aplicativo, a menos que isso seja necessário para a experiência |
| Registros salvos, progresso do usuário ou pontuações de jogos                   | D1, um banco de dados relacional para dados estruturados persistentes                         |
| Imagens, documentos, áudio, vídeo ou outros arquivos enviados              | R2, armazenamento de objetos para arquivos                                                  |
| Arquivos enviados com metadados pesquisáveis                        | D1 para metadados e R2 para o conteúdo dos arquivos                                      |
| Site interno que precisa da identidade do usuário atual do workspace | Identidade do usuário autenticado pelo workspace                                         |
| Login público ou provedor de identidade externo                | Um Site com autenticação habilitada                                                |

Não solicite armazenamento durável para estados temporários da interface, como a escolha de um tema ou um banner fechado. Solicite-o para dados do produto que as pessoas esperam que o site hospedado preserve.

## Controle o acesso e os segredos

Um novo Site fica restrito ao proprietário e aos administradores do workspace até que você altere o acesso. Mantenha o acesso restrito enquanto revisa o conteúdo, o tratamento de dados e o público-alvo.

Dependendo das configurações da sua conta e do workspace, as opções de compartilhamento podem incluir:

- **Proprietário e administradores do workspace**
- **Usuários ativos ou grupos selecionados**, quando houver suporte
- **Visualizadores externos convidados**, quando os convites externos estiverem disponíveis
- **Qualquer pessoa no workspace**, quando houver suporte
- **Qualquer pessoa na internet**, somente quando a publicação pública estiver habilitada

O acesso de visitante permite que as pessoas abram o Site, mas não concede acesso de edição. Em workspaces do plano Empresas, a publicação pública fica desativada por padrão e deve ser habilitada por um administrador.

No compartilhamento restrito, os visitantes convidados precisam entrar com a conta que recebeu acesso. É possível acessar um Site público sem ter acesso a um workspace do ChatGPT. A configuração de público do Site e qualquer recurso de login integrado a ele são controles separados.

Por exemplo:

```text
Change this Site's access to everyone in my workspace after showing me the
current Site and confirming its URL.

### Convide pessoas de fora do seu workspace

Os convites externos permitem conceder acesso a um Site a pessoas específicas sem torná-lo público. Você pode convidar visualizadores de fora do seu workspace ou compartilhar um Site privado a partir de uma conta pessoal. O recurso está sendo disponibilizado gradualmente para usuários do Sites nos planos Plus, Pro, Business e Empresas.

1. Abra um Site do qual você seja proprietário e selecione **Compartilhar**.
2. Para manter o Site privado, defina **Quem tem acesso** como **Somente convidados**.
3. Insira o endereço de e-mail do visualizador em **Pesquisar pessoas ou grupos** ou,
no caso de um Site pessoal, em **Insira um endereço de e-mail** . Em seguida, selecione o destinatário.
4. Revise o público e o acesso de **Visualizador** do destinatário e selecione
**Convidar**.
5. Confirme que o visualizador aparece na lista de acesso salva. Compartilhe o link do Site e peça que ele entre com a conta que recebeu acesso.

Visualizadores externos podem abrir e usar o Site. Eles não se tornam membros do workspace nem editores do Site e não podem editá-lo ou publicá-lo. O convite concede acesso a esse Site; revise o conteúdo e os dados conectados a ele antes de compartilhar.

No plano Empresas, os administradores gerenciam a opção **Permitir que membros convidem visitantes externos para
sites** em **Configurações do workspace \> Permissões e funções**. Essa permissão
é separada da permissão para publicar Sites publicamente.
Workspaces do plano Business não têm um controle separado para habilitar ou desabilitar a permissão
de convites externos; o Sites precisa estar habilitado, e o recurso deve estar disponível para a conta.
Se a opção de convite não aparecer, verifique a conta selecionada, quem é o proprietário do Site,
as permissões do workspace e se o recurso já foi disponibilizado.

Para remover um visualizador, abra os controles de compartilhamento do Site e remova o acesso dele. Verifique também as demais configurações de público: remover um convite não elimina o acesso que a pessoa tem por meio do compartilhamento público, com o workspace ou com grupos.

### Colabore em um Site

A colaboração em um Site exige um workspace. Quando o recurso está disponível, o proprietário de um Site pode convidar membros ativos do mesmo workspace para serem editores.

Os editores podem ler os dados do banco de dados em produção do Site. Convide apenas pessoas em quem você confia para lidar com o código e os dados do Site.

1. Abra o Site e selecione **Compartilhar**.
2. Em **Adicionar pessoas ou grupos**, localize e selecione um membro do workspace. Essa pessoa
   é adicionada como visitante.
3. Abra **Pode visualizar** ao lado dessa pessoa e escolha **Pode editar**. O acesso é salvo
   automaticamente. O Site aparece em **Compartilhado com você** na visualização de
   Sites desse membro.
4. O editor pode abrir o Site, fazer alterações, salvar versões e publicar atualizações depois que o proprietário publicar o Site pela primeira vez.

O proprietário do Site gerencia o acesso dos editores e pode promover um visitante existente a
editor, alterar o acesso de um editor para **Pode visualizar** ou remover seu acesso. A edição colaborativa
não adiciona um controle separado para habilitar ou desabilitar essa permissão no workspace.

Os editores não podem alterar o público do Site, convidar ou remover outras pessoas, gerenciar configurações ou análises, restaurar uma versão anterior nem transferir a propriedade. Um editor também não pode fazer a primeira publicação do Site; o proprietário precisa publicá-lo antes que os editores possam publicar atualizações posteriores.

O acesso de edição é separado do acesso de visitante. As etapas acima primeiro adicionam a pessoa como visitante e depois concedem acesso de edição. Promover um visitante a editor não altera a configuração de público do Site.

### Configure os valores do ambiente de execução

Abra **Sites** e, em seguida, abra as configurações do Site para adicionar, atualizar ou remover
variáveis do ambiente e segredos da hospedagem. Não inclua valores secretos em prompts, arquivos
anexados nem no conteúdo do Site.

Acesse [chatgpt.com/sites](https://chatgpt.com/sites), localize o Site e selecione
**Mais ações** \> **Configurações**.

Não armazene esses valores em `.openai/hosting.json`. Mantenha os arquivos locais `.env` e
`.env.example` alinhados às chaves necessárias para o desenvolvimento local e
não faça commit de valores secretos.

Quando adicionar, atualizar ou remover valores do ambiente hospedado, peça ao ChatGPT para reimplantar a versão salva e aprovada, para que a próxima implantação use a configuração atualizada.

## Altere a URL de um Site

Quando a edição de URLs estiver disponível, os proprietários de Sites poderão alterar a URL hospedada pelo ChatGPT de um Site existente sem criar outra implantação.

1. Abra **Sites**, localize o Site e abra suas configurações.
2. Localize a URL do Site e selecione **Alterar URL**.
3. Insira um nome disponível. Ele deve conter pelo menos cinco caracteres, começar com uma letra minúscula e usar apenas letras minúsculas, números e hífens isolados. Não pode terminar com hífen nem conter hífens consecutivos.
4. Confirme a alteração e aguarde enquanto o Sites atualiza o endereço.

Alterar a URL não cria outra implantação. O endereço anterior redireciona para o novo, mantendo as rotas e os parâmetros de consulta.

Alterar a URL hospedada pelo ChatGPT não adiciona, remove nem altera um domínio personalizado. Os domínios personalizados são um recurso separado já existente; use as configurações de domínio personalizado quando esse recurso estiver disponível.

## Conecte um domínio personalizado

Quando domínios personalizados estiverem disponíveis, você poderá conectar um domínio raiz ou subdomínio que já seja seu. O Sites não registra domínios para você, então você precisa ter acesso para alterar os registros DNS do domínio. No lançamento, domínios personalizados não estão disponíveis em workspaces do plano Empresas.

Para conectar um domínio:

1. Abra as configurações do Site e selecione **Adicionar domínio**.
2. Insira o domínio raiz ou subdomínio que deseja usar.
3. Copie os registros DNS e os valores fornecidos pelo Sites e adicione-os por meio do provedor do seu domínio.
4. Aguarde alguns minutos, volte às configurações do Site e atualize o status do domínio.

Você também pode pedir ao ChatGPT para ajudar a apontar o domínio para seu Site. Se a navegação ou o Uso do computador estiver habilitado, o ChatGPT poderá ajudar você a navegar pelo site do provedor do seu domínio depois que você fizer login.

## Revise antes de compartilhar

Antes de compartilhar um Site:

- Revise o conteúdo, os textos e as imagens gerados, os links, os arquivos enviados, os formulários e o comportamento interativo.
- Confirme que ele não expõe informações confidenciais ou sensíveis, valores secretos nem conteúdo de terceiros que você não tem o direito de compartilhar.
- Teste o Site pela perspectiva do público-alvo, incluindo o funcionamento do acesso e do login.
- Revise os recursos que coletam informações pessoais ou outros conteúdos dos visitantes. Decida se o Site deve coletar, compartilhar ou publicar essas informações.
- Se o Site usar o recurso Entrar com o ChatGPT, explique quais informações dos visitantes ele recebe e como as utiliza.
- Se o Site coletar ou processar dados pessoais, cumpra as
[leis de privacidade e proteção de dados aplicáveis](https://help.openai.com/en/articles/20001340).
- Escolha a opção de compartilhamento mais restrita que atenda ao público pretendido.
- Abra o Site compartilhado e confirme que o público pretendido consegue acessá-lo.

Para um Site criado a partir de um projeto local, revise também as alterações no código-fonte e eventuais
migrações de banco de dados no [painel de revisão](/pt-BR/codex/code-review?surface=app) do Codex.

## Tirar um Site do ar ou excluí-lo

Para remover o acesso sem excluir um Site, abra as configurações de compartilhamento e restrinja
o acesso a você ou a pessoas selecionadas. Confirme que o público anterior não consegue mais
acessá-lo.

Para excluir um Site permanentemente:

1. Abra **Sites** e localize o Site.
2. Selecione **Excluir site** e siga as instruções apresentadas.
3. Digite o slug do Site e selecione **Excluir permanentemente**.

Excluir um Site o remove permanentemente. Não é possível restaurar um Site excluído.

## Entenda os limites e os usos não compatíveis

Sites hospeda experiências Web executadas no ambiente de execução compatível com Sites. Não há suporte a alguns
frameworks, redes privadas, bancos de dados, serviços em segundo plano e padrões
de hospedagem.

Há suporte a HTTP, HTTPS e WebSockets. Não há suporte a conexões TCP brutas
de entrada e saída.

Cada Site tem os seguintes limites de armazenamento:

| Recurso            | Limite                  |
| ------------------- | ---------------------- |
| Armazenamento do banco de dados D1 | 10 GB                  |
| Armazenamento de objetos R2   | Sem limite fixo de armazenamento |

No lançamento, Sites não oferece suporte à residência de dados nem à residência de inferência. Isso
inclui os Sites implantados, o código dos Sites, o armazenamento de dados e arquivos no D1 e no R2, os artefatos
gerados e os logs.

Não use Sites para processar informações de saúde protegidas ou dados de cartões de pagamento;
ter como público crianças menores de 13 anos ou abaixo da idade de consentimento digital aplicável; viabilizar
transações financeiras; distribuir malware; facilitar phishing; fazer-se passar por pessoas
ou organizações; ou violar de qualquer outra forma as políticas da OpenAI. Consulte
[Criar e gerenciar Sites do ChatGPT](https://help.openai.com/en/articles/20001339)
para conhecer os limites atuais e acessar os links das políticas.

## Documentação relacionada

- [Aplicativo do ChatGPT para desktop](/pt-BR/codex/app) apresenta a navegação no aplicativo, os projetos e os chats.
- [Revisar e publicar alterações](/pt-BR/codex/code-review?surface=app) explica como inspecionar as alterações no código-fonte
  antes de publicá-las.

- [Projetos e chats](/pt-BR/codex/projects) explica como o contexto das pastas e do workspace
  é mantido entre os chats.
- [Revisar e publicar alterações](/pt-BR/codex/code-review) explica o fluxo de trabalho de revisão para
  cada cliente do Codex.
- [Ambiente isolado](/pt-BR/codex/sandboxing) explica os limites da execução local.

- [Abra Sites no ChatGPT](https://chatgpt.com/sites) para voltar aos Sites que você
  criou.
- [Projetos e chats](/pt-BR/codex/projects?surface=web) explica como manter juntos
  os chats e arquivos de origem relacionados.
- [Trabalhar com arquivos](/pt-BR/codex/artifacts-viewer?surface=web) explica como revisar
  arquivos gerados no ChatGPT na Web.

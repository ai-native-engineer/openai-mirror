<!-- source: https://learn.chatgpt.com/pt-BR/docs/whats-new -->

Este resumo semanal destaca recursos do ChatGPT e do Codex que podem mudar sua forma de
trabalhar, com exemplos e links para saber mais. Para consultar todas as atualizações de versão, correções de bugs
e pequenas melhorias, veja o [registro de alterações do Codex](/codex/changelog).

## 31 de agosto a 4 de setembro de 2026

### Encare trabalhos exigentes com GPT-6 Astra

O [GPT-6 Astra](/pt-BR/codex/models#gpt-6-astra) combina raciocínio avançado, uso do computador
e maior capacidade de julgamento para trabalhos complexos com código, aplicativos e pesquisa no
Codex e no ChatGPT Work. Use-o para executar um fluxo de trabalho, verificar o resultado e
produzir um documento, uma planilha ou uma apresentação que se adapte aos seus modelos e
à sua tarefa.

Quando o Astra estiver disponível na sua conta, escolha-o no seletor de modelos.
Consulte [uso e preços](/pt-BR/codex/pricing) antes de iniciar uma tarefa grande.
O acesso no Enterprise exige tanto elegibilidade para a liberação quanto
ativação por um administrador.

## 24 a 28 de agosto de 2026

### Trabalhe com mais sites

- **Use seu navegador:** Trabalhe no [Edge, Brave, Opera ou Vivaldi](/pt-BR/codex/chrome-extension),
  além do Chrome, pelo aplicativo do ChatGPT para desktop. Adicione uma aba aberta a um
  chat do ChatGPT Work ou do Codex e trabalhe no site em que você já
  fez login. O Opera oferece suporte ao controle do navegador, mas não tem chat lateral.

- **Use as ferramentas de um site:** Com as [Ferramentas do site (WebMCP)](/pt-BR/codex/webmcp),
  o ChatGPT Work e o Codex podem usar ações oferecidas por um site no navegador integrado
  do aplicativo para desktop. Por exemplo, um editor de documentos pode fornecer ferramentas para encontrar
  uma seção ou adicionar um comentário. Atualize o aplicativo para desktop e use GPT-5.6 Sol ou
  GPT-5.6 Terra. As ferramentas do site não estão disponíveis com GPT-5.6 Luna nem em workspaces
  Enterprise ou Edu.

- **Faça login pelo navegador na nuvem:** Nos planos elegíveis, continue uma tarefa
  que exige uma conta em um site no ChatGPT Work na Web, no iOS ou no Android.
  Siga a [solicitação de login](/pt-BR/codex/browser?surface=web#web-sign-in-to-a-website)
  e insira seus dados no fluxo de login, não no chat. Isso não
  conecta o perfil do seu navegador local. O login em sites não está disponível para
  workspaces Enterprise ou Edu.

A disponibilidade depende da liberação do recurso e das configurações do workspace.

[Leia as notas de versão do navegador de
25 de agosto](/codex/changelog#codex-2026-08-25-browser).

### Execute tarefas agendadas a partir de eventos em aplicativos

As [tarefas agendadas](/pt-BR/codex/automations?surface=web#web-trigger-tasks-from-app-events) agora podem
começar quando um evento compatível ocorrer no Gmail, no Slack ou no GitHub. Use um gatilho
de evento para fazer a triagem de novos e-mails, resumir a atividade de um canal ou agir com base nos comentários de revisão de pull requests
sem precisar consultar atualizações em intervalos fixos.

As tarefas acionadas por eventos estão disponíveis no ChatGPT na Web e em dispositivos móveis nos
planos elegíveis. Primeiro, conecte o aplicativo relevante e aprove o acesso solicitado. Em workspaces
gerenciados, os administradores podem controlar o acesso.

<PromptComponent
  prompt={`Quando um dos meus pull requests em <owner>/<repository> receber novos comentários de revisão, resuma os comentários e prepare um plano de ajustes.`}
/>

[Leia as notas de versão de
25 de agosto](/codex/changelog#codex-2026-08-25-event-triggers).

## 17 a 21 de agosto de 2026

### Trabalhe com mais dos seus aplicativos e conteúdos

- **Apple Messages:** [Encontre chats, resuma mensagens, prepare respostas e envie pelo Messages no seu Mac](/pt-BR/codex/plugins?surface=app#app-use-apple-messages-from-codex). O plug-in está disponível em todos os planos no aplicativo do ChatGPT para desktop no macOS. Use-o no ChatGPT Work e no Codex, não nos chats comuns do ChatGPT. Por padrão, o ChatGPT envia mensagens somente depois que você aprova a mensagem e seus destinatários.

- **Edição colaborativa de Sites:** Quando o recurso estiver disponível, [convide membros ativos do seu workspace para atuar como editores](/pt-BR/codex/sites#collaborate-on-a-site). Os editores podem aprimorar o Site e publicar atualizações depois que o proprietário o publica pela primeira vez. Os editores convidados podem ler os dados do banco de dados em uso pelo Site; os proprietários mantêm o controle do compartilhamento e das configurações.

- **URLs editáveis de Sites:** Quando o recurso estiver disponível, [escolha um novo endereço hospedado pelo ChatGPT para um Site existente](/pt-BR/codex/sites#change-a-site-url) sem implantá-lo novamente. O endereço anterior redireciona para o novo.

- **Histórico do computador na Europa:** Use o [Histórico do computador](/pt-BR/codex/customization/computer-history) no EEE, na Suíça e no Reino Unido. Ele permanece desativado por padrão para usuários dos planos ChatGPT Pro, Business e Enterprise no macOS. Os administradores dos planos Business e Enterprise precisam habilitar o acesso primeiro.

- **Cópias estáticas compartilhadas de conversas:** [Compartilhe uma cópia estática somente leitura de uma conversa local do Codex](/pt-BR/codex/use-chatgpt#share-a-read-only-snapshot-of-a-codex-thread) pelo aplicativo do ChatGPT para desktop no macOS. Links de contas pessoais podem ser visualizados por qualquer pessoa que tenha o link; links de contas de workspace são restritos ao workspace de origem. O Codex oculta segredos que correspondem a padrões conhecidos, mas revise a cópia antes de compartilhá-la, pois ela ainda pode conter conteúdo sensível.

- **Conversas fixadas unificadas:** Mantenha seus [chats fixados](/pt-BR/codex/projects?surface=app#app-organize-projects-and-chats) sincronizados entre o desktop e o iOS.

[Leia as notas de versão de 20 de agosto](/codex/changelog#codex-2026-08-20-app).

### Trabalhe com projetos do GitLab no Codex Cloud

O [suporte ao GitLab](/pt-BR/codex/third-party/gitlab) está disponível em versão beta em todos os
planos do ChatGPT. Conecte um projeto, crie um ambiente de nuvem, inicie tarefas a partir de issues
ou merge requests usando `@codex` e solicite revisões
pontuais ou automáticas de merge requests.

A integração é executada no Codex Cloud, e um administrador do workspace gerenciado pode
desativá-la. Atividades acionadas pelo GitLab exigem permissão para configurar o
webhook correspondente. As conexões do GitLab Self-Managed e do GitLab Dedicated exigem
configuração por um administrador do workspace; atividades de webhook exigem GitLab 19.0 ou posterior.

[Leia as notas de versão do GitLab de
19 de agosto](/codex/changelog#codex-2026-08-19-gitlab).

### Exporte metadados de plug-ins públicos para revisão

Proprietários e administradores elegíveis de workspaces do ChatGPT Enterprise podem baixar um arquivo CSV dos
plug-ins públicos visíveis no workspace. Em
[Administração \> Plug-ins](https://chatgpt.com/admin/plugins), selecione **Públicos** e, em seguida,
selecione o ícone de download (**Exportar CSV**).

A exportação lista os nomes e as descrições de plug-ins, aplicativos e habilidades do Chat,
juntamente com o desenvolvedor, a versão, a data de adição em UTC e os metadados de verificação da OpenAI.
Ela usa uma cópia estática do catálogo público gerada há até 48 horas e exclui
plug-ins criados para o workspace. A exportação não está disponível em workspaces
FedRAMP.

[Leia as notas de versão da exportação administrativa de
17 de agosto](/codex/changelog#codex-2026-08-17-admin-csv).

## 10 a 14 de agosto de 2026

### Encontre trabalhos anteriores com o Histórico do computador

O [Histórico do computador](/pt-BR/codex/customization/computer-history) transforma a atividade nos seus aplicativos e sites
em uma linha do tempo pesquisável e em memórias que o ChatGPT
e o Codex podem usar. Ative-o somente se quiser compartilhar esse contexto e, em seguida,
escolha quais aplicativos e sites fornecem dados, pause a coleta e revise ou
exclua seu histórico a qualquer momento.

O Histórico do computador está disponível no aplicativo do ChatGPT para desktop no macOS para clientes dos planos ChatGPT
Pro, Business e Enterprise. Os administradores dos planos Business e Enterprise
precisam habilitar o acesso primeiro. Inicialmente, o recurso não está disponível na
União Europeia, na Suíça nem no Reino Unido.

### Use o aplicativo do ChatGPT para desktop no Linux

O [aplicativo do ChatGPT para desktop para Linux](/pt-BR/codex/linux/linux-app) já está disponível em
versão prévia. Instale um pacote `.deb` nas distribuições Ubuntu ou Debian compatíveis
ou um pacote `.rpm` no Fedora. Os pacotes estão disponíveis para processadores x64
e ARM64.

Faça login com sua conta do ChatGPT para trabalhar com projetos, arquivos locais e o
Codex. Alguns recursos, incluindo o Uso do computador, ainda não estão disponíveis na
versão prévia para Linux.

### Traga as configurações e o trabalho que você já tem em outros agentes

[Importe instruções, configurações, habilidades, plug-ins, projetos e trabalhos
recentes](/codex/import) do **Claude Code**, do <strong>Claude Cowork</strong> ou do
**Cursor** para o aplicativo do ChatGPT para desktop. Ative as atualizações automáticas em
**Configurações \> Importar** para manter os trabalhos importados sincronizados.

Na Codex CLI, use `/import` para trazer as configurações compatíveis e os chats recentes do
Claude Code ou do Cursor para sua sessão local.

[Leia as notas de versão de 11 de agosto do aplicativo para desktop e da
CLI](/codex/changelog#codex-2026-08-11-app).

### Escolha o acesso adequado para atividades de segurança defensiva

O Daybreak agora oferece dois níveis de acesso para profissionais de defesa cibernética aprovados. O **Daybreak Blue** oferece suporte a
atividades gerais de defesa, como revisão de segurança de código, resposta a incidentes e
validação de patches. O **Daybreak Red** exige uma aprovação separada e oferece
acesso a modelos treinados especificamente para avaliações de segurança autorizadas.

O acesso exige [Trusted Access for
Cyber](/pt-BR/codex/cyber-safety#trusted-access-for-cyber) e se aplica apenas à
identidade, ao workspace ou à organização, ao modelo e à interface do produto aprovados.

[Leia o anúncio do Daybreak de 10
de agosto](/codex/changelog#codex-2026-08-10-daybreak).

## 3–7 de agosto de 2026

### Converse sobre arquivos e projetos com o ChatGPT Modo Voz

O [ChatGPT Modo Voz](/pt-BR/codex/features/voice) agora oferece suporte a arquivos enviados e aos
[Projetos do ChatGPT](/pt-BR/codex/projects). Faça perguntas sobre um documento durante uma
conversa por voz ou dê continuidade a um projeto usando seus chats recentes, fontes e
instruções.

### Estude e ensine com plug-ins específicos para educação

Três novos [plug-ins](/pt-BR/codex/plugins) trazem fluxos de trabalho específicos para a sala de aula ao
ChatGPT Work e ao Codex. O **College Student** cria guias de estudo, questionários para
praticar, cartões de memorização e explicações interativas. O **College Educator** ajuda a
desenvolver planos de curso, materiais e avaliações. O **K–12 Educator** auxilia no
planejamento de aulas e na criação de recursos para a sala de aula e de materiais adaptados a diferentes
alunos.

Os plug-ins estão disponíveis pelo ChatGPT Edu e pelas implantações do ChatGPT for Teachers em distritos
escolares. As escolas controlam quais ferramentas e permissões ficam disponíveis. Leia
o [anúncio dos plug-ins para
educação](https://openai.com/index/learn-teach-chatgpt-work-codex/).

### Reutilize arquivos salvos e encontre trabalhos anteriores mais rápido

Na Web, adicione um arquivo salvo na Biblioteca a uma conversa sem enviá-lo
novamente, pesquise na Biblioteca e cole texto formatado sem perder títulos,
links ou listas. A pesquisa também encontra pastas e títulos de conversas na
Web, no iOS e no Android.

Textos colados com mais de 10.000 caracteres agora viram anexos em todos os planos do ChatGPT,
incluindo Enterprise e Edu. Selecione **Mostrar no campo de texto** se quiser
colocar o conteúdo de volta na mensagem.

Leia as [notas de versão
do ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes).

### Veja quanto você ainda pode usar o ChatGPT Work

Usuários elegíveis dos planos pessoais e do ChatGPT Business podem conferir quanto ainda podem usar o
ChatGPT Work diretamente na barra lateral da versão Web. As opções de créditos disponíveis dependem
da sua conta e das permissões do workspace. O ChatGPT Work e o Codex continuam
compartilhando os mesmos [limites de uso e créditos](/pt-BR/codex/pricing).

### Escolha como o GPT-5.6 responde no ChatGPT

Usuários do ChatGPT Plus e Pro podem usar um novo controle deslizante para ajustar quanto o GPT-5.6 Sol raciocina ao elaborar uma
resposta. O modelo atualizado também traz informações factuais mais confiáveis
e respostas mais focadas. O GPT-5.6 Luna passa a ser o modelo padrão do ChatGPT nos planos Free
e Go.

Essas mudanças se aplicam às conversas do ChatGPT. Elas não alteram o comportamento dos modelos
no ChatGPT Work nem no Codex. Leia as [notas de versão
do ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes).

### Organize o trabalho e alterne entre agentes no Codex CLI 0.147.0

O [Codex CLI 0.147.0](https://github.com/openai/codex/releases/tag/rust-v0.147.0)
adiciona seções de chat persistentes, com ordenação manual, e Plug-ins de agentes portáteis.
Pesquise nos catálogos de plug-ins locais, pessoais, do workspace e remotos, ou
[importe as configurações do Cursor e do Claude Code](/pt-BR/codex/import) sem duplicar
conversas sincronizadas.

Use `--approve-for-me` para ativar a [revisão automática de
aprovações](/pt-BR/codex/sandboxing/auto-review) para solicitações elegíveis sem ampliar as
permissões do sistema de arquivos ou da rede. As sessões do Amazon Bedrock também passam a contar com pesquisa na Web
com cache e compactação remota de conversas.

### Acompanhe e retome verificações de segurança mais aprofundadas

As versões `0.1.16` a `0.1.18` do Plugin Codex Security hospedado adicionam acompanhamento do progresso das verificações
em tempo real, medição do uso de tokens, verificações aprofundadas que podem ser retomadas e limites
de descoberta configuráveis. A versão mais recente também oferece suporte à autenticação do Amazon Bedrock
para verificações de repositórios e seus executores delegados.

Use a [área de trabalho do Codex Security](/pt-BR/codex/security/plugin/workbench) para revisar
o progresso e os achados das verificações ou [configure uma verificação
aprofundada](/pt-BR/codex/security/plugin/deep-scans) quando precisar de uma avaliação
mais completa. Consulte o [registro de alterações do plug-in](/pt-BR/codex/security/plugin/changelog) para
confirmar quais recursos a versão instalada oferece.

### Revise pull requests do GitHub em busca de riscos de segurança

A [Revisão do Codex Security](/pt-BR/codex/security/security-review) analisa as alterações de pull requests
junto com o contexto do repositório, modelos de ameaças e orientações de segurança.
Configure revisões automáticas quando um pull request for aberto ou receber novos
commits, ou solicite uma revisão diretamente com `@codex security review`.

O recurso está disponível em prévia de pesquisa para clientes elegíveis do ChatGPT Enterprise,
Business, Edu e Pro. Não está disponível no Plus, e podem ser aplicados limites
de uso.

## 27–31 de julho de 2026

### Use o GPT-5.6 Terra e o Luna com tarifas menores

O GPT-5.6 Terra agora custa 20% menos, e o GPT-5.6 Luna custa 80% menos. As tarifas de entrada,
entrada em cache e saída diminuíram nas mesmas proporções. Os
[limites de uso e tarifas](/pt-BR/codex/pricing) atualizados tornam o Terra mais adequado ao trabalho
do dia a dia e o Luna especialmente útil para tarefas pontuais de programação e tarefas de alto volume.

### Encontre contexto útil no navegador e nas abas abertas

No aplicativo do ChatGPT para desktop, o [navegador integrado](/pt-BR/codex/browser) pode encontrar
páginas no seu histórico de navegação ou pesquisar no Google diretamente pela barra
de endereços. O ChatGPT também pode pesquisar no seu histórico de navegação quando uma tarefa precisar de contexto
anterior.

A [extensão do Chrome](/pt-BR/codex/chrome-extension) permite mencionar abas abertas,
levar texto selecionado de uma página para um chat lateral, fazer perguntas sobre vídeos do YouTube
ou selecionar **Perguntar ao ChatGPT** no menu de contexto de uma página. Revise e aprove
as solicitações de uso do histórico de navegação antes que o ChatGPT inclua essas informações em uma
tarefa.

### Revise alterações em vários repositórios

Quando um [projeto local contém mais de uma
pasta](/pt-BR/codex/projects#use-local-projects-for-folders-and-codebases), o aplicativo para
desktop mostra todos os repositórios e as linhas alteradas em cada um. Selecione
**Revisão** para inspecionar os diffs em conjunto, sem alternar entre visualizações
de revisão separadas.

### Refine as imagens geradas na sua conversa

Abra uma imagem gerada no visualizador ampliado e alterne entre
**Visualização focada** e **Visualização do Canvas**. Adicione comentários às imagens, selecione as
versões que deseja manter e peça edições específicas sem sair do chat.
Saiba mais sobre [geração de imagens](/pt-BR/codex/image-generation).

### Encontre chats que precisam da sua atenção

A nova **Visualização de atividades** do aplicativo para desktop reúne chats com os quais você interagiu
recentemente e trabalhos que precisam da sua atenção. Selecione o sino na barra lateral
para abrir a visualização.

[Leia as notas de lançamento de 30 de julho do aplicativo para
desktop](/codex/changelog#codex-2026-07-30-app).

### Conecte ferramentas de parceiros com a opção Entrar com o ChatGPT

A opção **Entrar com o ChatGPT** está sendo disponibilizada em beta para plug-ins compatíveis e
sites de parceiros, começando por Airtable, GitLab, HubSpot, Notion, Supabase e
Vercel. Use-a para criar ou vincular uma conta em um serviço parceiro em menos etapas e comece
a trabalhar com esse serviço no ChatGPT ou no Codex.

Os parceiros recebem apenas seu nome, endereço de e-mail e foto de perfil, quando
disponível. O acesso solicitado por cada plug-in continua exigindo revisão
e aprovação separadas. Leia o [anúncio de 29 de julho sobre a opção
de login](/codex/changelog#codex-2026-07-29).

### Colabore em um workspace dedicado à pesquisa acadêmica

O [ChatGPT para Pesquisadores Acadêmicos](https://openai.com/index/chatgpt-for-academic-researchers/)
oferece a docentes e pesquisadores de pós-doutorado elegíveis 12 meses de acesso gratuito
a um workspace dedicado do ChatGPT. As equipes aprovadas podem incluir até cinco
pesquisadores verificados da mesma instituição e recebem proteções para dados
empresariais e limites de uso equivalentes aos do ChatGPT Pro. Os participantes podem usar o GPT-5.6
no ChatGPT, no ChatGPT Work e no Codex em fluxos de trabalho de pesquisa e programação.

O programa inclui acesso ao ChatGPT, mas não créditos da API da OpenAI. A elegibilidade exige
[verificação institucional e um artigo de pesquisa que atenda
aos critérios](https://help.openai.com/en/articles/20001406).

### Retome tarefas do Codex com mais confiabilidade no iOS

O ChatGPT para iOS 1.2026.202 se reconecta às tarefas com mais confiabilidade quando você volta ao
aplicativo ou desbloqueia o dispositivo com o Face ID. As conversas por voz usam a voz do
ChatGPT que você escolheu e exibem avisos de limite de uso, enquanto o editor agora sugere
plug-ins instalados e suas habilidades da mesma forma que o aplicativo para desktop.

A versão também aprimora os controles para pausar e retomar metas, as tabelas em linha
e os temas visuais, os diffs extensos do workspace, as referências a texto selecionado e a restauração
do modelo. Leia as [notas de lançamento de 27 de julho
para iOS](/codex/changelog#codex-2026-07-27-mobile).

### Compare varreduras de segurança e gerencie achados

As versões `0.1.14` e `0.1.15` do Plugin Codex Security hospedado adicionam comparações entre varreduras,
feedback sobre falsos positivos, políticas `SECURITY.md` com escopo definido e históricos mais claros de repositórios
e achados. Você pode selecionar achados para acompanhamento no Linear ou em issues do
GitHub, com o Codex revisando a ação proposta antes de você aprová-la.

Use o [painel do
Codex Security](/pt-BR/codex/security/plugin/workbench) existente para revisar varreduras salvas, achados,
o histórico do repositório e a remediação no aplicativo para desktop. O catálogo de plug-ins hospedados
oferece a versão `0.1.15`, enquanto o marketplace público de plug-ins da CLI
oferece a versão `0.1.11`. Consulte o [registro de alterações do
Plugin Codex Security](/pt-BR/codex/security/plugin/changelog) antes de contar com um novo recurso.

### Execute varreduras de segurança pelo terminal, pela CI ou com TypeScript

A CLI pública e o SDK para TypeScript de `@openai/codex-security` chegaram à versão
`0.1.5`, com numeração de versões independente da do Plugin Codex Security. Use o
pacote para [executar varreduras pela CLI](/pt-BR/codex/security/cli), revisar alterações em pull requests
e enviar resultados SARIF na [CI](/pt-BR/codex/security/cli/ci), ou executar
[varreduras em lote](/pt-BR/codex/security/cli/bulk-scans) que podem ser retomadas em repositórios do GitHub
ou a partir de um inventário CSV fixado.

O [SDK para TypeScript do Codex Security](/pt-BR/codex/security/sdk) também permite integrar
varreduras, relatórios de progresso, controles de custos e cancelamento às suas próprias
ferramentas. O pacote é público, mas executar varreduras ainda exige acesso ao Codex Security.
Algumas varreduras de repositórios inteiros também exigem Trusted Access for Cyber.

### Organize sessões e amplie os recursos do Codex CLI 0.146.0

O [Codex CLI 0.146.0](https://github.com/openai/codex/releases/tag/rust-v0.146.0)
permite nomear um novo chat com `/new release prep` ou `/clear bug bash`, fixar
conversas importantes e alternar entre conversas paralelas sem fechá-las.
Ele também adiciona forks temporários de conversas, pesquisa na Web independente para provedores
personalizados de modelos compatíveis, habilidades fornecidas pelo executor e suporte a manifestos de Plug-ins de Agentes,
publicação de plug-ins no workspace e outros marketplaces de plug-ins.

Para clientes personalizados, o [App Server](/pt-BR/codex/app-server) pode filtrar conversas
fixadas, criar forks em memória, inspecionar o estado dos conectores instalados e ler
metadados dos conectores. O suporte experimental a WebSocket também conecta o app-server a
hosts remotos do modo Código. Consulte os
[requisitos de segurança do app-server](/pt-BR/codex/app-server#connect-the-cli-terminal-ui)
antes de expor uma conexão remota. A versão também melhora o suporte a proxy,
a reconexão MCP, a capacidade de resposta do terminal e a confiabilidade do sandbox do Windows.

### Use o GPT-5.6 Sol em tarefas do Codex na nuvem

O [GPT-5.6 Sol](/pt-BR/codex/models#recommended-models) agora é o modelo usado na revisão de código
e na garantia de qualidade do Codex Cloud para clientes elegíveis. Sol é o modelo principal
da família GPT-5.6 para tarefas complexas de programação, pesquisa, uso do computador e segurança.
O Codex Cloud seleciona seu modelo automaticamente; Terra e Luna continuam disponíveis nas
interfaces locais e web compatíveis.

### Prepare-se para a descontinuação do modelo GPT-5.4

Em 31 de agosto, o GPT-5.4 e o GPT-5.4 mini serão descontinuados no Codex para usuários conectados
com o ChatGPT. Substitua `gpt-5.4` por `gpt-5.6-terra` e `gpt-5.4-mini`
por `gpt-5.6-luna` nas configurações padrão do workspace, nas configurações de modelo salvas, nas configurações
gerenciadas, nos agentes personalizados e nas tarefas agendadas.

A API da OpenAI e as sessões do Codex autenticadas com uma chave de API não são
afetadas. Consulte os [modelos descontinuados do Codex](/pt-BR/codex/models#deprecated-codex-models)
e a [disponibilidade de modelos
no workspace](/pt-BR/codex/enterprise/workspace-model-availability) antes da
data-limite.

## 20 a 24 de julho de 2026

### Converse sobre o trabalho com o ChatGPT Modo Voz

O [ChatGPT Modo Voz](/pt-BR/codex/features/voice), com tecnologia GPT-Live, permite conversar
sobre o trabalho e coordenar tarefas no Chat, no Work e no Codex pelo aplicativo do ChatGPT
para desktop. Inicie um novo chat ou tarefa no modo voz e peça ao ChatGPT para iniciar, verificar ou
orientar o trabalho em outras conversas.

No macOS, diga “Dê uma olhada nisso” para compartilhar uma [captura de aplicativo](/pt-BR/codex/appshots) da
janela em primeiro plano quando o **Contexto da tela** estiver ativado.

A Voz está disponível nos planos Plus, Pro, Business, Edu e Enterprise no
aplicativo para desktop e pelo [Remoto no iOS](/pt-BR/codex/remote-connections#set-up-mobile-access).

### Trabalhe com várias pastas em um único projeto local

Os projetos locais no aplicativo do ChatGPT para desktop agora podem incluir várias pastas
relacionadas. Escolha uma pasta principal para novos chats, operações do Git e descoberta
automática de `AGENTS.md`, habilidades e `config.toml`. As pastas secundárias continuam
disponíveis para pesquisa, leitura e edição de arquivos.

Abra **Editar projeto** para [adicionar pastas e escolher a pasta
principal](/pt-BR/codex/projects#use-local-projects-for-folders-and-codebases).

[Leia as notas de versão de 23 de julho](/codex/changelog#codex-2026-07-23-app).

## 13 a 17 de julho de 2026

### Mantenha as conversas do Work e os Projetos juntos no desktop

O aplicativo do ChatGPT para desktop agora reúne as conversas do Chat e do Work na
visualização do ChatGPT. As conversas do Work na nuvem são sincronizadas entre web, dispositivos móveis e desktop;
as conversas locais do Work permanecem no seu computador. Os Projetos do ChatGPT estão disponíveis
no aplicativo para desktop. O Codex mantém sua visualização dedicada e um histórico separado para
fluxos de trabalho de desenvolvimento.

[Compare o ChatGPT Work e o Codex no
desktop](/pt-BR/codex/use-chatgpt#compare-chatgpt-work-and-codex-on-desktop) para escolher a
visualização adequada à sua tarefa.

### Controle o trabalho em paralelo do Codex com o Codex Micro

Em 15 de julho, a OpenAI e a Work Louder lançaram o
[Codex Micro](/pt-BR/codex/features/codex-micro), um painel de controle físico com produção
limitada para o Codex no aplicativo do ChatGPT para desktop. Suas teclas de agente mostram o status de
até seis chats e permitem alternar entre eles. Teclas de comando personalizáveis, um controle
analógico e um controle giratório podem acionar ações comuns ou habilidades, ativar o recurso de pressionar para falar e
ajustar o esforço de raciocínio sem sair do teclado.

### Use o GPT-5.6 pelo Amazon Bedrock

GPT-5.6 Sol, Terra e Luna passaram a ter disponibilidade geral pelo
Amazon Bedrock. As interfaces locais do ChatGPT Work e do Codex podem usar o
[provedor `amazon-bedrock`](/pt-BR/codex/amazon-bedrock) integrado com uma chave de API do Bedrock ou a
cadeia de credenciais do SDK da AWS. Isso inclui o Work e o Codex no aplicativo do ChatGPT
para desktop, a Codex CLI, a extensão para IDE e o SDK do Codex.

### Inspecione as visualizações de tarefas do Codex no iOS

O ChatGPT para iOS 1.2026.188 adicionou visualizações em linha às tarefas do Codex e
melhorou a criação e o gerenciamento de tarefas a partir de conversas, incluindo links
confiáveis para tarefas recém-criadas. Leia as
[notas de versão de 13 de julho para iOS](/codex/changelog#codex-2026-07-13-mobile).

## 6 a 10 de julho de 2026

<a id="take-on-ambitious-work-with-chatgpt-work"></a>

### Encare trabalhos ambiciosos no ChatGPT

O [ChatGPT Work](/pt-BR/codex/get-started-with-work) no ChatGPT pode reunir contexto dos
seus arquivos e [plug-ins](/pt-BR/codex/plugins),
executar ações em fluxos de trabalho e criar documentos, apresentações,
planilhas, Sites e outros trabalhos finalizados que você pode revisar. Com o
[GPT-5.6](/pt-BR/codex/models), ele pode dividir uma meta em etapas e trabalhar por horas enquanto
você acompanha o progresso, responde a perguntas, muda a direção e aprova
ações importantes.

As [tarefas agendadas](/pt-BR/codex/automations) podem dar continuidade a esse trabalho quando você estiver ausente
com execuções únicas, programadas, acionadas por eventos ou enquanto monitoram
mudanças.

### Escolha o modelo GPT-5.6 adequado

A [família GPT-5.6](/pt-BR/codex/models#recommended-models) oferece três modelos recomendados
no ChatGPT Work, no aplicativo do ChatGPT para desktop, na Codex CLI e na extensão do Codex
para IDE. Sol é o modelo principal para programação complexa, uso do computador, pesquisa e
segurança. Terra equilibra capacidade e custo para o trabalho diário, enquanto Luna
é a opção mais rápida e de menor custo. A configuração padrão **Potência** usa Sol com
raciocínio médio.

### Use o Codex no aplicativo do ChatGPT para desktop

Em 9 de julho, o aplicativo Codex foi integrado ao
[aplicativo do ChatGPT para desktop](/pt-BR/codex/app) para macOS e Windows. O Codex mantém sua
experiência dedicada à programação ao lado do Chat e do Work do ChatGPT. A experiência do Codex
inclui edição em linha nas visualizações de diferenças, revisão de pull requests no painel lateral, o recurso
[Uso do computador](/pt-BR/codex/computer-use) mais rápido com o GPT-5.6 e projetos com vários
repositórios.

Quem já usa o aplicativo Codex pode atualizá-lo normalmente. Você pode definir o Codex como a visualização
padrão, usar o logotipo do Codex como ícone do aplicativo e acessar os projetos do Codex no desktop pelo
aplicativo do ChatGPT para dispositivos móveis. O aplicativo para desktop atualizado está disponível em todo o mundo, em todos os
planos do ChatGPT, incluindo o Free.

## 15 a 19 de junho de 2026

### Transforme demonstrações de fluxos de trabalho em habilidades reutilizáveis

O recurso [Gravar e reproduzir](/pt-BR/codex/extend/record-and-replay) permite mostrar ao ChatGPT ou ao
Codex um fluxo de trabalho no macOS e transformar a demonstração em uma habilidade reutilizável. Use-o
para tarefas repetitivas que são mais fáceis de mostrar do que descrever. Depois, aprimore a
habilidade gerada e execute-a novamente com novas entradas. Inicialmente, o recurso não está disponível
no EEE, no Reino Unido e na Suíça e exige o Uso do computador.

<a id="continue-a-task-on-another-host"></a>

### Continue um chat em outro host

A [transferência de chats](/pt-BR/codex/remote-connections#hand-off-a-chat-between-hosts)
move um chat e seu estado do Git entre o computador local e um host
remoto conectado. O Codex pode criar ou reutilizar uma árvore de trabalho no destino, transferir
o chat e continuar a partir do projeto correspondente.

A mesma versão para desktop adiciona ações em massa ao histórico de execuções agendadas, para que
você possa marcar todas as execuções como lidas ou arquivar as execuções elegíveis de uma só vez.

### Explore e revise workspaces pelo iOS

No aplicativo do ChatGPT para dispositivos móveis, o **Remoto** ganhou um explorador de arquivos do workspace, um
seletor de diretórios para novos chats, controles para expandir e recolher visualizações de diferenças e
opções de aprovação de MCP para um único chat ou vários chats no iOS.

O Uso do computador, a extensão do Chrome, as Memórias e o Chronicle também começaram a ser
disponibilizados no EEE, no Reino Unido e na Suíça. As Memórias continuam
desativadas por padrão nessas regiões, e o Chronicle é uma prévia de pesquisa com adesão opcional
para assinantes do ChatGPT Pro no macOS.

Leia as notas de versão de [15 de junho para iOS](/codex/changelog#codex-2026-06-15-mobile),
[16 de junho sobre disponibilidade](/codex/changelog#codex-2026-06-16-app) e
[18 de junho para o aplicativo](/codex/changelog#codex-2026-06-18-app).

## 8 a 12 de junho de 2026

### Depure aplicativos web com o modo de desenvolvedor do navegador

O [Modo de desenvolvedor](/pt-BR/codex/browser?surface=app#app-developer-mode) dá ao Codex acesso controlado
aos recursos do Chrome DevTools Protocol no Chrome e no navegador
integrado. O Codex pode inspecionar o tráfego de rede, a saída do console, erros de execução e o
estado da página enquanto analisa o desempenho ou depura seu aplicativo. Na seção **Modo de desenvolvedor** de
**Configurações** \> **Navegador**, ative **Habilitar acesso completo ao CDP**. O Codex pede
aprovação explícita antes de usar esse acesso em um site.

O uso do navegador também está até duas vezes mais rápido, pois otimizações no CDP e nas capturas do DOM
reduzem as trocas de requisições e respostas com o navegador.

  
    
  

### Traga sua configuração para o Codex

Novos fluxos de migração podem importar configurações compatíveis de outros agentes de programação durante a
configuração inicial. O aplicativo Codex também adicionou `/init` para criar instruções de projeto,
além de melhorias no gerenciamento de plug-ins, nos diagnósticos do navegador e nos resumos de chats
concluídos.

<a id="set-up-codex-tasks-from-ios"></a>

### Configure chats do Codex pelo iOS

O Remoto no iOS agora permite escolher uma branch, criar uma árvore de trabalho, executar um script de
configuração de ambiente, gerenciar metas e adicionar comentários de revisão em linha.

Leia as notas de versão de [9 de junho para o aplicativo](/codex/changelog#codex-2026-06-09-app),
[9 de junho para iOS](/codex/changelog#codex-2026-06-09-mobile) e
[11 de junho para o aplicativo](/codex/changelog#codex-2026-06-11-app).

## 1 a 5 de junho de 2026

### Crie e implante sites com Sites

O [Sites](/pt-BR/codex/sites) permite que o ChatGPT crie, salve, implante e inspecione sites,
painéis, ferramentas internas, aplicativos web e jogos hospedados pela OpenAI. O Sites tem um
ponto de acesso dedicado no ChatGPT na Web e no desktop, onde você pode retomar
projetos e gerenciar valores e segredos do ambiente hospedado sem montar uma
estrutura de implantação separada.

### Use o Codex com o Amazon Bedrock

Você pode [usar o Codex com o Amazon Bedrock](/pt-BR/codex/amazon-bedrock) em fluxos de trabalho locais
com autenticação, controles de conta e faturamento gerenciados pela AWS.
O recurso Remoto no iOS também ganhou um bloqueio opcional dentro do aplicativo, configurações de comportamento para mensagens de acompanhamento,
quebra de linha nas visualizações de diferenças e conexões SSH com máquinas Windows. O aplicativo para desktop
ganhou controles de posicionamento do terminal e informações sobre atividade na visualização de
perfil.

[Leia todas as notas de versão de junho de 2026](/codex/changelog#month-2026-06).

## 25 a 29 de maio de 2026

### Use aplicativos do Windows e controle o Codex remotamente

O [Uso do computador](/pt-BR/codex/computer-use#windows-foreground-use) passou a permitir
visualizar, clicar e digitar em aplicativos para desktop do Windows. Instale o plug-in de Uso do computador
antes de começar. No Windows, o Codex usa a área de trabalho ativa e assume o controle
em primeiro plano enquanto a tarefa é executada. As conexões remotas também oferecem suporte ao
Windows. No aplicativo do ChatGPT para dispositivos móveis, abra **Remoto** para começar a trabalhar em um dispositivo Windows
ou use um Mac com o aplicativo do ChatGPT para desktop em execução e acompanhe o progresso de
outro lugar.

O recurso Remoto no iOS também ganhou pontos de acesso pelo Spotlight e pelo Atalhos, navegação por chats
arquivados, `/side` e opções para salvar ou copiar imagens renderizadas. O aplicativo para desktop
ganhou coordenação de chats para projetos locais e árvores de trabalho, pesquisa por conteúdo e
nome de branch em chats anteriores e identificadores visuais consistentes para
subagentes em segundo plano.

Leia as notas de versão [do iOS de 25 de maio](/codex/changelog#codex-2026-05-25-mobile) e
[do aplicativo de 29 de maio](/codex/changelog#codex-2026-05-28-app).

## 18 a 22 de maio de 2026

### Forneça ao Codex contexto de qualquer aplicativo do Mac com Capturas do app

As [Capturas do app](/pt-BR/codex/appshots) enviam ao Codex a janela do aplicativo em primeiro plano com uma
captura de tela e o texto disponível quando você pressiona as duas teclas Command. O Codex recebe
contexto de trabalho de ferramentas de design, painéis, documentos e outros aplicativos
sem que você precise copiar, colar ou descrever o que está na tela.

### Acompanhe metas de longa duração

O [modo Meta](/pt-BR/codex/prompting#goal-mode) saiu da fase experimental e está
disponível no aplicativo Codex, na extensão para IDE e na CLI para objetivos que podem levar
horas ou dias. O [uso com o Mac bloqueado](/pt-BR/codex/computer-use#locked-use) permite que o Codex
continue tarefas aprovadas de uso do computador após o bloqueio do Mac, inclusive pelo
**Remoto** no aplicativo do ChatGPT para dispositivos móveis. Os workspaces do ChatGPT Business também podem
[compartilhar pacotes reutilizáveis de plug-ins com os membros do workspace](https://developers.openai.com/plugins/build/plugins#share-a-local-plugin-with-your-workspace).

[Leia as notas de lançamento de 21 de maio](/codex/changelog#codex-2026-05-21).

## 11 a 15 de maio de 2026

### Continue pelo celular o trabalho iniciado no computador

No aplicativo do ChatGPT para dispositivos móveis, **Remoto** se conecta a um Mac com o aplicativo do ChatGPT
para desktop em execução. Como o trabalho é executado no host conectado, seus projetos, arquivos,
credenciais, plug-ins, habilidades e configurações continuam disponíveis quando você
retoma o trabalho pelo celular. Consulte [Conexões remotas](/pt-BR/codex/remote-connections)
para configurar um host e retomar o trabalho em outro dispositivo.

### Automatize fluxos de trabalho confiáveis

Os ganchos passaram a ter disponibilidade geral para executar comandos personalizados em pontos-chave
do ciclo de vida do agente. Administradores do ChatGPT Enterprise também podem habilitar
[tokens de acesso do Codex](/pt-BR/codex/enterprise/access-tokens) para scripts confiáveis,
agendadores e executores privados de CI. As orientações para empresas foram ampliadas para abordar
a configuração gerenciada e os controles do Codex.

[Leia as notas de lançamento de 14 de maio](/codex/changelog#codex-2026-05-13-app).

## 4 a 8 de maio de 2026

### Trabalhe em várias abas do navegador com a extensão do Chrome

A [extensão do Chrome](/pt-BR/codex/chrome-extension) pode trabalhar em
paralelo em várias abas, em segundo plano, sem assumir o controle do navegador. Você
controla quais sites o Codex pode usar, o que facilita combinar pesquisa,
inserção de dados e verificação em vários aplicativos web em uma única tarefa.

O aplicativo Codex também ganhou ajustes automáticos no texto ditado e um dicionário personalizado para nomes,
caminhos de arquivos e símbolos de código. Proprietários de workspaces do ChatGPT Enterprise podem permitir
que os membros criem [tokens de acesso do Codex](/pt-BR/codex/enterprise/access-tokens) para
fluxos de trabalho locais confiáveis e não interativos.

Leia as notas de lançamento [do aplicativo de 5 de maio](/codex/changelog#codex-2026-05-05-app),
[dos tokens de acesso de 5 de maio](/codex/changelog#codex-2026-05-05) e
[do Codex para Chrome](/codex/changelog#codex-2026-05-07).

## 20 a 24 de abril de 2026

### Use o GPT-5.5 para trabalhos complexos

O [GPT-5.5](/pt-BR/codex/models) chegou ao Codex como o modelo recomendado para a maioria das
tarefas, com pontos fortes em implementação, depuração, testes, uso do computador,
pesquisa e produção de resultados prontos para uso em trabalhos intelectuais.

### Deixe o Codex operar o navegador e revisar aprovações

O [Uso do computador no navegador integrado](/pt-BR/codex/browser?surface=app#app-computer-use-in-the-browser)
permite que o Codex navegue com cliques por servidores locais de desenvolvimento e páginas baseadas em arquivos para
reproduzir problemas e verificar correções. Solicitações de aprovação elegíveis também podem passar
pela [revisão automática de aprovações](/pt-BR/codex/sandboxing/auto-review),
que mostra o status da revisão e o risco antes da execução da ação.

[Leia as notas de lançamento de 23 de abril](/codex/changelog#codex-2026-04-23).

## 13 a 17 de abril de 2026

### Veja prévias e realize tarefas em um só lugar

O [navegador integrado](/pt-BR/codex/browser?surface=app) ganhou prévias em tempo real e comentários nas páginas,
enquanto o [Uso do computador](/pt-BR/codex/computer-use) permitiu ao Codex ver e
operar aplicativos do macOS. Juntos, esses recursos tornaram a implementação visual e a verificação de ponta a ponta
parte da mesma tarefa de alteração de código.

  
    
  

<a id="start-with-a-task-and-keep-it-moving"></a>

### Comece com um chat e dê continuidade ao trabalho

Com os [chats independentes](/pt-BR/codex/projects#start-without-a-project), passou a ser
possível começar sem escolher uma pasta de projeto. A mesma versão adicionou
[tarefas agendadas dentro de um chat](/pt-BR/codex/automations#schedule-a-task-inside-a-chat),
contexto de pull requests, prévias de arquivos mais completas e [Memórias](/pt-BR/codex/customization/memories) para
trabalhos que se estendem por vários chats.

[Leia as notas de versão de 16 de abril do aplicativo Codex](/codex/changelog#codex-2026-04-16-app).

## 6 a 10 de abril de 2026

### Revise e envie pull requests no aplicativo

A experiência de revisão ganhou comentários recolhíveis em linha, modos de revisão em linha e em separado,
além de um contexto mais claro sobre o Git e o código-fonte. As atividades dos pull requests, os comentários
e as opções de push passaram a ficar no aplicativo junto com as abas de arquivos do workspace,
para que você pudesse inspecionar uma alteração e responder sem trocar de ferramenta.

Leia as notas de versão do aplicativo Codex de [9 de abril](/codex/changelog#codex-2026-04-09-app) e
[10 de abril](/codex/changelog#codex-2026-04-10-app), ou
saiba como [revisar alterações no aplicativo](/pt-BR/codex/code-review?surface=app).

## 23 a 27 de março de 2026

### Empacote fluxos de trabalho como plug-ins

Os [plug-ins](/pt-BR/codex/plugins) foram lançados como pacotes instaláveis de habilidades,
conectores e servidores MCP. Eles facilitaram a descoberta, a instalação e o compartilhamento de fluxos de trabalho completos,
enquanto as páginas redesenhadas de plug-ins e habilidades passaram a mostrar com mais clareza seu conteúdo
e status. A pesquisa de chats anteriores também chegou naquela semana.

Leia as notas de versão sobre a [pesquisa de tarefas](/codex/changelog#codex-2026-03-24-app),
o [lançamento de plug-ins](/codex/changelog#codex-2026-03-25) e
o [aplicativo Codex](/codex/changelog#codex-2026-03-25-app).

## 16 a 20 de março de 2026

### Crie forks a partir de mensagens anteriores e escolha ferramentas no editor

Passou a ser possível criar um fork de um chat a partir de uma mensagem anterior, facilitando testar uma nova
abordagem sem perder o caminho original. Comandos de modelo e raciocínio passaram a ficar
disponíveis enquanto você escrevia a mensagem, as habilidades ativadas apareceram no menu `@`, e o GPT-5.4 mini
trouxe uma opção mais rápida para tarefas mais leves e subagentes.

Leia as notas de versão do [GPT-5.4 mini](/codex/changelog#codex-2026-03-17),
do [controle de chats](/codex/changelog#codex-2026-03-18-app) e
do [menu de habilidades](/codex/changelog#codex-2026-03-19-app).

## 9 a 13 de março de 2026

### Agende tarefas no ambiente certo

As [tarefas agendadas](/pt-BR/codex/automations) podiam ser executadas localmente ou em uma árvore de trabalho
com um modelo e um nível de raciocínio definidos explicitamente. Modelos reutilizáveis agilizaram
a configuração de tarefas comuns, e temas personalizados facilitaram a
personalização do workspace.

  
    
  

### Deixe o Codex inspecionar a saída do terminal

O Codex também passou a ler o [terminal integrado](/pt-BR/codex/integrated-terminal#run-and-validate-your-project)
do chat atual. Ele podia inspecionar diretamente um servidor de desenvolvimento em execução ou a saída
de uma compilação, em vez de pedir que você colasse essas informações.

Leia as notas de versão do aplicativo Codex de [11 de março](/codex/changelog#codex-2026-03-11-app) e
[12 de março](/codex/changelog#codex-2026-03-12-app).

## 2 a 6 de março de 2026

### Execute o Codex nativamente no Windows

O aplicativo Codex foi lançado para [Windows](/pt-BR/codex/windows/windows-app) com suporte nativo ao PowerShell
e ao sandbox, além de árvores de trabalho, tarefas agendadas e habilidades. O WSL continuou
disponível para desenvolvedores que preferiam um ambiente Linux.

  
    
  

<a id="move-tasks-between-local-and-worktree"></a>

### Mova chats entre Local e Árvore de trabalho

A [transferência entre Local e Árvore de trabalho](/pt-BR/codex/environments/git-worktrees#working-between-local-and-worktree)
passou a permitir mover um chat ativo preservando seu contexto. O GPT-5.4
também chegou ao Codex naquela semana para programação, uso do computador e fluxos de trabalho
com contextos maiores.

Leia as notas de versão sobre o [lançamento para Windows](/codex/changelog#codex-2026-03-04-app),
a [transferência entre árvores de trabalho](/codex/changelog#codex-2026-03-03-app) e
o [GPT-5.4](/codex/changelog#codex-2026-03-05).

## 9 a 13 de fevereiro de 2026

### Itere em tempo real e crie um fork para explorar outra abordagem

O GPT-5.3-Codex-Spark foi disponibilizado em prévia de pesquisa como um modelo de resposta quase instantânea para
iterar no código em tempo real. O aplicativo também ganhou a opção de criar forks de chats e uma
janela de chat flutuante, sempre em primeiro plano, para você explorar outra abordagem ou
manter o Codex ao lado de um editor ou navegador.

Leia as notas de versão do [Spark](/codex/changelog#codex-2026-02-12) e do
[aplicativo Codex](/codex/changelog#codex-2026-02-12-app), ou consulte o
[guia de modelos](/pt-BR/codex/models) atual.

## 2 a 6 de fevereiro de 2026

### O aplicativo Codex chega ao macOS

O aplicativo Codex foi lançado como um workspace para desktop com chats de projetos em paralelo,
revisão integrada de alterações do Git, árvores de trabalho, habilidades, tarefas agendadas e ditado por voz.
Esses recursos agora estão no Codex, no [aplicativo do ChatGPT para desktop](/pt-BR/codex/app).

  
    
  

### Redirecione o trabalho em andamento e adicione arquivos

Passou a ser possível redirecionar o Codex durante um turno sem interromper uma
resposta em andamento, e os anexos passaram a aceitar outros arquivos além de imagens. Esses recursos
se tornaram a base para [orientar o Codex e enfileirar](/pt-BR/codex/prompting#steering-and-queuing)
mensagens de acompanhamento com o contexto de que o Codex precisa.

Leia as [notas de lançamento do aplicativo Codex](/codex/changelog#codex-2026-02-02) e
as [notas de versão do aplicativo de 5 de fevereiro](/codex/changelog#codex-2026-02-05-app).

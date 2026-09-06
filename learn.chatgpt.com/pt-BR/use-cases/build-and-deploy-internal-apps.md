<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/build-and-deploy-internal-apps -->

## Crie e implante em uma única tarefa

O Sites é um serviço gerenciado de hospedagem no ChatGPT. Peça ao ChatGPT para criar um aplicativo; ele pode desenvolver o projeto, executá-lo para testes, implantá-lo e retornar uma URL que você possa compartilhar.

O Sites está em beta público para planos pagos elegíveis. No lançamento, ele não está disponível nos planos Free ou Go, nem no EEE, na Suíça ou no Reino Unido. A liberação gradual ou as configurações do workspace podem afetar o acesso.

A abrangência vai de sites estáticos a aplicativos Web full-stack em JavaScript ou TypeScript. Por isso, o Sites é uma boa opção para ferramentas internas específicas, como painéis de integração, centrais de treinamento, bibliotecas de recursos com pesquisa, aplicativos leves de fluxo de trabalho e visualizações de relatórios.

Consulte a [documentação do Sites](/pt-BR/codex/sites) para ver orientações sobre configuração, armazenamento, implantação e acesso.

Comece por um fluxo de trabalho útil. Uma primeira versão bem definida é mais fácil de revisar, implantar e aprimorar do que uma solicitação ampla para recriar todo um sistema interno.

## O que esperar

Este é um exemplo fictício que usa um briefing de lançamento anexado e cinco solicitações de exemplo. Na primeira etapa, um rastreador específico de solicitações é criado e verificado; a solicitação complementar adiciona um filtro por responsável e facilita a identificação de solicitações em atraso.

<div data-use-case-export-only>

O rastreador de solicitações de lançamento exibe inicialmente **cinco solicitações de exemplo**, incluindo uma bloqueada, duas em revisão e uma em atraso. A equipe pode consultar as solicitações por lançamento e status, filtrar o trabalho bloqueado, adicionar uma solicitação e atualizar o status dela. O fluxo principal e o estado salvo foram verificados em larguras de tela para computadores e dispositivos móveis.

Após uma solicitação complementar, o rastreador passa a incluir um filtro por responsável e destaca o trabalho em atraso; **as solicitações bloqueadas permanecem no topo, e uma solicitação não pode ser marcada como pronta sem um responsável**. A prévia continua privada; nenhum Site foi publicado, e o acesso não foi alterado.

</div>

## Forneça ao ChatGPT o contexto do fluxo de trabalho

Informe ao ChatGPT para quem o aplicativo se destina, o que as pessoas devem fazer, quais materiais de referência ele deve consultar e o que deve ser mantido entre as sessões. Especifique o escopo de compartilhamento pretendido e peça ao ChatGPT para testar o fluxo principal antes de implantar o aplicativo.

Use [Plug-ins](/pt-BR/codex/plugins) para buscar ou atualizar dados de fontes internas conectadas. Inicie uma tarefa do Sites que use aplicativos conectados ou arquivos na nuvem no Work na Web, ou no Work ou Codex para desktop. Use o aplicativo para desktop para trabalhar com um arquivo local, o navegador integrado para acessar um site em que você já tenha iniciado sessão ou a Extensão do Chrome do Codex para usar uma sessão existente do Chrome.

  Se precisar buscar dados em tempo real, você poderá se conectar a uma ferramenta de terceiros usando uma
  chave de API configurada nas configurações do Site. Não inclua valores secretos em prompts
  nem em arquivos. Se quiser usar conexões de Plug-ins, você poderá [agendar o trabalho a partir
  da tarefa atual](/pt-BR/codex/automations#schedule-work-from-a-task) para buscar dados
  com Plug-ins de acordo com uma programação definida, atualizar o aplicativo e salvar uma versão para revisão.
  Implante a versão revisada somente após a aprovação.

## Escolha o armazenamento do aplicativo

Muitos aplicativos internos precisam de persistência. O Sites oferece suporte a duas primitivas de armazenamento:

- Use o D1, um banco de dados compatível com SQLite, para dados estruturados, como estado de listas de verificação, favoritos, filtros, anotações, configurações e metadados de arquivos.
- Use o armazenamento de objetos R2 para bytes de arquivos, como documentos enviados, imagens ou outros recursos que devam persistir.

Mantenha os metadados estruturados no D1 e os objetos de arquivos maiores no R2. Uma página de recursos somente leitura ou um pequeno site estático talvez não precise de nenhum dos dois.

O Sites não oferece suporte à residência de dados nem de inferência. Não o use para processar informações de saúde protegidas ou dados de cartões de pagamento, nem para viabilizar transações financeiras. Consulte as [restrições de dados e uso do Sites](https://help.openai.com/en/articles/20001339-creating-and-managing-chatgpt-sites) antes de armazenar informações sensíveis.

## Gerencie e compartilhe seus projetos

Você pode controlar quem pode acessar seus projetos implantados.

Mantenha um novo projeto privado enquanto revisa o conteúdo, o tratamento de dados e o público-alvo dele.

Dependendo das configurações da sua conta e do workspace, você pode compartilhá-lo com:

- Pessoas que você convidar.
- Todas as pessoas do seu workspace.
- Qualquer pessoa na internet.

O compartilhamento permite que as pessoas acessem o projeto, mas não que o editem. Para alterar o acesso, abra o [Sites no ChatGPT](https://chatgpt.com/sites) ou peça diretamente ao ChatGPT:

O compartilhamento público também é adequado para um guia simples de evento, uma página de recursos de um clube ou outro site voltado a pessoas de fora de um workspace. Nos workspaces de Empresas, a publicação pública vem desativada por padrão e precisa ser habilitada por um administrador. Mantenha os dados internos privados mesmo quando houver um link público disponível.

## Exemplos

A [Galeria do Sites](/showcase/sites) inclui exemplos de Sites com prompts completos.

{/* vale Vale.Spelling = NO */}
{/* vale Vale.Terms = NO */}

- **[Onboarding Hub](/showcase/onboarding-hub)** combina uma lista de verificação da primeira semana, recursos, notas e documentos enviados. Ele usa o D1 para o estado do usuário e os metadados de arquivos, e o R2 para os bytes dos arquivos enviados.
- **[Enablement Hub](/showcase/enablement-hub)** oferece uma biblioteca pesquisável de materiais de treinamento, com filtros e favoritos salvos no D1.
- **[Pulse Dashboard](/showcase/pulse-dashboard)** apresenta métricas, tendências e detalhes de linhagem, além de usar o D1 para configurações e snapshots em cache.
- **[Sparkboard](/showcase/idea-intake)** transforma a coleta de ideias dos funcionários em um fluxo de trabalho com envios autenticados, votação, comentários, painéis de status e ranking de colaboradores.
- **[Launch Cal](/showcase/launch-cal)** organiza os próximos lançamentos de produtos em um calendário mensal com filtros, indicadores de risco, listas de verificação e referências a fontes conectadas.
- **[Event Planning Hub](/showcase/event-planning-hub)** combina solicitações de eventos, aprovações, modelos, marcos, prontidão para atender às políticas e recursos de planejamento conectados.

{/* vale Vale.Terms = YES */}
{/* vale Vale.Spelling = YES */}

Use esses exemplos como pontos de partida e depois refine o prompt de acordo com o fluxo de trabalho e os materiais de referência da sua equipe.

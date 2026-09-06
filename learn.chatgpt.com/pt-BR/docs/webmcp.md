<!-- source: https://learn.chatgpt.com/pt-BR/docs/webmcp -->

As ferramentas do site são a implementação do
[padrão WebMCP proposto](https://webmachinelearning.github.io/webmcp/) no ChatGPT. Com o WebMCP,
um site pode oferecer ações úteis diretamente a um agente de IA, junto com a
interface que as pessoas já usam. Você e o agente podem trabalhar na mesma página em tempo real
e na mesma sessão autenticada.

No [navegador integrado](/pt-BR/codex/browser) do aplicativo do ChatGPT para desktop,
o ChatGPT Work e o Codex podem descobrir e usar essas ferramentas quando estiverem disponíveis.

  Use o GPT-5.6 Sol ou o GPT-5.6 Terra para usar as ferramentas do site. No GPT-5.6 Luna, o
WebMCP está desativado no momento. Atualize o aplicativo do ChatGPT para desktop para a versão mais recente. As ferramentas
do site não estão disponíveis em workspaces dos planos Empresas ou Edu. A disponibilidade também
depende da liberação gradual e das ferramentas oferecidas pela página atual.

## WebMCP vs. MCP

O [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/learn/architecture)
conecta um aplicativo de IA a um servidor local ou remoto. Suas ferramentas podem funcionar
independentemente de uma página da Web aberta, por exemplo, para pesquisar em um serviço ou gerenciar
registros por meio de uma API.

O [WebMCP](https://github.com/webmachinelearning/webmcp) permite que um site disponibilize suas
capacidades a um agente como um conjunto de ferramentas predefinidas. O agente pode
descobri-las ao visitar o site, então as pessoas não precisam instalar um servidor MCP separado
nem configurar outra conexão para usar essas capacidades.

Essa abordagem é útil quando você e o agente precisam ver a mesma coisa, como
ao editar uma tela ou explorar um painel. Um
[plug-in com um servidor MCP](/pt-BR/codex/build-plugins) pode oferecer uma integração
que funciona independentemente de uma página aberta. Um site pode oferecer suporte às duas abordagens.

## Como funciona no navegador

Abra um site no navegador integrado e peça ao ChatGPT Work ou ao Codex ajuda
com uma tarefa. Se a página oferecer ferramentas do site, o agente poderá descobrir e usar as
ações relevantes no site que você está visualizando. Por exemplo, um editor de
documentos pode permitir que o agente encontre uma seção ou deixe um comentário para você revisar.

Selecione **Ferramentas do site** na barra de endereços do navegador para ver o que o site
oferece. Escolha **Ferramentas do site disponíveis** para examinar cada ferramenta. O
navegador verifica cada solicitação antes que o site a execute, e o agente
pode examinar a página para ver o que mudou. Quando houver atividade recente disponível,
escolha **Usadas recentemente** para abrir **Fontes** e revisar essas chamadas.

Neste exemplo, expanda **Ferramentas do site disponíveis** para examinar as ferramentas oferecidas
pelo [Margin](https://margin-local-docs.openai.chatgpt.site).

  

As ferramentas pertencem à página que as oferece. Fechar uma página ou navegar para outra
pode tornar suas ferramentas indisponíveis. Se não houver uma ferramenta adequada disponível,
talvez o agente ainda consiga usar suas capacidades habituais de navegação.

## Exemplo: explore a documentação da OpenAI

O ChatGPT Learn e o OpenAI Developers oferecem ferramentas do site para encontrar e ler
documentação. Selecione **Abrir no ChatGPT** no editor para abrir o Learn no
navegador do aplicativo para desktop, ao lado de um novo chat com este prompt pronto para enviar.

O agente pode usar estas ferramentas para pesquisar, ler e abrir a página relevante:

| Ferramenta                    | O que faz                                                             |
| ----------------------- | ------------------------------------------------------------------------ |
| `search_openai_docs`    | Pesquisa na documentação da OpenAI.                                           |
| `lookup_page`           | Lê uma página da documentação pelo caminho ou pela URL.                               |
| `lookup_context`        | Lê a rota atual da documentação e o texto selecionado.                          |
| `navigate_to_page`      | Abre uma página correspondente no site de documentação atual.                 |
| `generate_custom_guide` | Inicia a criação de um guia personalizado de desenvolvimento ou aprendizado e retorna seu status e link. |

O Agente de documentação gera um guia personalizado de forma assíncrona. Receber o link do guia não
significa que a geração foi concluída.

## Segurança e controles do usuário

As definições e os resultados das ferramentas fornecidas por sites são conteúdo não confiável. O nome
de uma ferramenta ou a afirmação de que ela apenas lê dados não comprova o que ela faz. As instruções
de um site não dão ao agente permissão para compartilhar informações não relacionadas ou
realizar ações sensíveis.

No navegador integrado, cada chamada de ferramenta passa por uma revisão de segurança antes
de ser executada. As políticas normais de acesso a sites e de confirmação continuam válidas, inclusive
para ações de impacto, como enviar mensagens, fazer compras, excluir
dados ou alterar permissões. O navegador vincula cada chamada à sua
página de origem e ao registro da ferramenta. Essas verificações reduzem o risco; elas não
tornam um site ou seus resultados confiáveis.

Você pode desativar **Ativar ferramentas do site** em **Configurações \> Navegador \> Permissões**.
Analise o site, a ação solicitada e o resultado antes de compartilhar informações
sensíveis ou confiar em uma alteração.

Relate vulnerabilidades de segurança por meio do
[Programa de Bug Bounty de Segurança](https://bugcrowd.com/engagements/openai) da OpenAI. Para riscos de
segurança de IA, consulte o
[Programa de Bug Bounty de Segurança de IA](https://openai.com/index/safety-bug-bounty/). Siga
o escopo e as instruções de envio de cada programa.

## Limitações

O navegador integrado do ChatGPT oferece suporte atualmente a parte das APIs do WebMCP.
Os seguintes recursos não têm suporte:

- **API declarativa:** Ferramentas definidas por meio de atributos de formulários HTML não estão
  disponíveis como ferramentas do site.
- **Ferramentas em iframes:** O navegador não detecta ferramentas registradas dentro de
  iframes, incluindo iframes da mesma origem e de origens diferentes.

Use JavaScript para registrar ferramentas na página de nível superior, conforme mostrado na
[próxima seção](#add-webmcp-to-your-website). O ChatGPT Work e o Codex ainda podem
interagir com formulários usando as capacidades padrão do navegador, mas essas interações
não são chamadas de ferramentas WebMCP.

A especificação do WebMCP e o guia do Chrome para desenvolvedores descrevem um conjunto mais amplo de
APIs, incluindo recursos que atualmente não têm suporte no navegador integrado.

## Adicione WebMCP ao seu site

Você pode pedir ao Codex para adicionar suporte a WebMCP ao aplicativo web ou
[Site](/pt-BR/codex/sites) em que está trabalhando. Descreva o que um agente deve ser capaz
de fazer e peça ao Codex para reutilizar a lógica e as permissões existentes do aplicativo.

Comece com uma operação que seu aplicativo já permite realizar. Por exemplo:

- Um painel que permite ao agente definir um intervalo de datas e examinar os dados em que
um gráfico se baseia.
- Um editor de documentos que permite ao agente encontrar uma seção, sugerir uma edição ou
deixar um comentário para você revisar.
- Um planejador de viagens que permite ao agente comparar opções e atualizar um roteiro
enquanto você examina o mapa.

Você também pode escrever o código por conta própria. No módulo JavaScript da sua página, verifique
se o navegador oferece suporte e registre uma ferramenta. Este exemplo de somente leitura retorna
o título da página atual:

```javascript
if (typeof document.modelContext?.registerTool === "function") {
  await document.modelContext.registerTool({
    name: "get_page_title",
    description: "Read the title of the current page.",
    inputSchema: {
      type: "object",
      properties: {},
      additionalProperties: false,
    },
    annotations: { readOnlyHint: true },
    execute: async () => ({ title: document.title }),
  });
}

Um agente compatível pode descobrir `get_page_title` e receber o título
atual da página. Para uma ferramenta que aceita argumentos, descreva-os no esquema
de entrada e use-os no manipulador `execute` para chamar a lógica
existente do seu aplicativo.

Limite o escopo das entradas, descreva os efeitos colaterais e retorne informações suficientes para
verificar o resultado. Use os mecanismos de autenticação,
autorização e validação de entrada já existentes no seu aplicativo. Preserve a interface normal para as pessoas
e para os navegadores que não oferecem suporte a WebMCP.

Para detalhes e exemplos da API, consulte a
[especificação do WebMCP](https://webmachinelearning.github.io/webmcp/) e o
[guia do Chrome para desenvolvedores](https://developer.chrome.com/docs/ai/webmcp).

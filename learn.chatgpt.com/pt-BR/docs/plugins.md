<!-- source: https://learn.chatgpt.com/pt-BR/docs/plugins -->

## Visão geral

Os plug-ins reúnem recursos em fluxos de trabalho reutilizáveis no ChatGPT e no Codex. Eles
podem incluir habilidades, conectores ou ambos. Os dois produtos usam um único diretório universal de
plug-ins, por isso os mesmos plug-ins públicos podem ser encontrados nas interfaces
compatíveis.

Os plug-ins funcionam no Chat e no Work do ChatGPT na Web, no desktop e em dispositivos móveis,
e no Codex do aplicativo do ChatGPT para desktop. A Codex CLI também tem um navegador de plug-ins
para ambientes do Codex. A extensão para IDE não oferece suporte a plug-ins.

Em dispositivos móveis, você pode usar no Chat ou no Work os plug-ins disponíveis para sua conta.

Abra a aba **Plug-ins** para explorar e instalar plug-ins. Após a instalação, você
pode usar plug-ins no Chat ou no Work do ChatGPT, ou no Codex. Os plug-ins instalados podem
adicionar habilidades, conectores e ferramentas MCP a novas conversas.

Abra a aba **Plug-ins** para explorar e instalar plug-ins. Após a instalação, você
pode usar plug-ins no Chat ou no Work. Um plug-in pode solicitar a conexão de um serviço
externo antes de disponibilizar suas ferramentas.

Na Codex CLI, digite `/plugins` para abrir o navegador de plug-ins. Instale um plug-in de um
marketplace configurado e inicie uma nova sessão antes de usar as habilidades ou
ferramentas incluídas.

<a id="plugin-directory-in-the-ide-extension"></a>

### Usar plug-ins em uma interface compatível

Os plug-ins não estão disponíveis na extensão para IDE. Para explorar e instalar plug-ins
para o Codex, use o aplicativo do ChatGPT para desktop ou a Codex CLI.

Amplie o que o ChatGPT e o Codex podem fazer, por exemplo:

- Instale o Plugin Codex Security para analisar código autorizado e confirmar
indícios plausíveis de vulnerabilidades.
- Instale o plug-in do Gmail para trabalhar com o Gmail.
- Instale o plug-in do Google Drive para trabalhar com o Drive, Docs, Sheets e
Slides.
- Instale o plug-in do Slack para resumir canais ou redigir respostas.

Um plug-in pode conter uma ou mais destas partes:

- **Habilidades:** instruções reutilizáveis para tipos específicos de trabalho. O ChatGPT e
  o Codex podem carregá-las quando necessário para seguir as etapas corretas e usar as
  referências ou os scripts auxiliares adequados à tarefa.
- **Conectores:** conexões com ferramentas como GitHub, Slack ou Google Drive, para que
  o ChatGPT e o Codex possam ler informações dessas ferramentas e realizar ações
  nelas. Os conectores disponibilizam ferramentas e podem incluir uma interface personalizada.
- **Servidores MCP:** serviços que dão ao ChatGPT e ao Codex acesso a mais ferramentas ou
  informações compartilhadas, geralmente de sistemas externos ao seu projeto local. Eles
  também são os serviços por trás dos conectores. Definem ferramentas, exigem autenticação, retornam
  dados estruturados e executam ações em sistemas externos.
- **Extensões do navegador:** recursos do navegador necessários para o
  fluxo de trabalho de um plug-in.
- **Hooks:** comandos executados em pontos configurados do ciclo de vida. Revise os hooks
  do plug-in e confirme que são confiáveis antes de ativá-los.
- **Modelos de tarefas agendadas:** pontos de partida reutilizáveis para tarefas recorrentes
  nos contextos em que as tarefas agendadas estão disponíveis.

Você pode compartilhar plug-ins publicando-os por meio de uma fonte de marketplace, como um
marketplace de repositório para um projeto ou uma equipe. Consulte [Criar plugins](https://developers.openai.com/plugins/build/plugins)
para ver orientações sobre configuração de marketplaces, empacotamento e distribuição.

Se estiver criando uma integração, comece por
[Criar um servidor MCP](https://developers.openai.com/plugins/build/mcp-server).
Se o plug-in precisar de uma interface personalizada, consulte o
[guia de interface opcional](https://developers.openai.com/plugins/build/chatgpt-ui).

## Usar e instalar plug-ins

<a id="plugin-directory-in-the-codex-app"></a>

### Diretório universal de plug-ins

O ChatGPT e o Codex usam o mesmo catálogo público de plug-ins. Na Web ou no
aplicativo do ChatGPT para desktop, abra a aba **Plug-ins** para explorar e instalar plug-ins.

  
    
  

O Diretório de Plug-ins organiza os plug-ins em abas:

- **OpenAI:** plug-ins criados pela OpenAI.
- **Nome do seu workspace:** plug-ins fornecidos pelo seu workspace.
- **Pessoal:** plug-ins do marketplace pessoal, incluindo as seções **Criados por mim** e
**Compartilhados comigo** , quando esses plug-ins estiverem disponíveis.

Use a linha **Instalados** , exibida separadamente, para conferir os plug-ins que você já instalou.

Os administradores do workspace podem importar e sincronizar um marketplace do GitHub para a equipe. Consulte
[Gerenciamento de plug-ins](/pt-BR/codex/enterprise/plugin-management) para ver os requisitos de configuração e
acesso.

### Instalar e usar um plug-in

Depois de abrir o Diretório de Plug-ins:

1. Pesquise ou navegue pelo diretório para encontrar um plug-in e abra seus detalhes.
2. Selecione o botão com o sinal de mais para instalar o plug-in.
3. Se o plug-in precisar de um conector, conecte-o quando solicitado. Alguns plug-ins
pedem autenticação durante a instalação. Outros esperam até a primeira vez que você
os utiliza.
4. Após a instalação, inicie uma nova conversa e peça ao ChatGPT ou ao Codex que use o
plug-in.

### Conectar parceiros compatíveis usando o recurso Entrar com o ChatGPT

A opção **Entrar com o ChatGPT** está sendo disponibilizada gradualmente em versão beta para plug-ins e
sites de parceiros compatíveis, incluindo Airtable, GitLab, HubSpot, Notion, Supabase e
Vercel. Quando a opção estiver disponível, selecione **Entrar com o ChatGPT** ao
conectar o plug-in para criar ou vincular sua conta nesse serviço.

Ao entrar, você compartilha com o parceiro apenas seu nome, endereço de e-mail e foto de perfil, quando
disponível. Isso não concede ao plug-in acesso aos seus dados nem
aprova ações automaticamente. Em uma etapa separada, revise e aprove as permissões solicitadas
pelo plug-in antes de usar a conexão.

Depois de instalar um plug-in, você pode usá-lo diretamente na janela de prompt:

  
    
  

<div class="not-prose mt-4 grid gap-4 md:grid-cols-2">
  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
    <p class="text-sm font-semibold text-default">Descreva a tarefa diretamente</p>
    <p class="mt-2 text-sm text-secondary">
      Peça o resultado desejado, como "Resuma as conversas não lidas de hoje
no Gmail" ou "Busque no Google Drive as notas de lançamento mais recentes."
    </p>
    <p class="mt-3 text-sm text-secondary">
      Use essa opção quando quiser que o ChatGPT escolha as ferramentas instaladas adequadas para a
tarefa.
    </p>
  </div>

  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
    <p class="text-sm font-semibold text-default">Escolha um plug-in específico</p>
    <p class="mt-2 text-sm text-secondary">
      Digite <code>@</code> para invocar explicitamente o plug-in ou uma das habilidades
      incluídas nele.
    </p>
    <p class="mt-3 text-sm text-secondary">
      Use essa opção quando quiser especificar qual plug-in ou habilidade o ChatGPT
      deve usar. Consulte <a href="/codex/skills-and-plugins">Habilidades e Plug-ins</a>.
    </p>
  </div>
</div>

### Usar o Apple Messages no Codex

O plug-in Apple Messages está disponível em todos os planos no aplicativo do ChatGPT para desktop
para macOS. No Codex e no ChatGPT Work, ele pode ler e pesquisar conversas de iMessage, SMS e
RCS no seu Mac e enviar mensagens em seu nome pelo aplicativo Messages.
Ele não permite interagir remotamente com o ChatGPT pelo Messages e
não funciona nas conversas comuns do ChatGPT.

Neste lançamento, o plug-in Messages está incluído somente na versão para Apple Silicon
(arm64) do aplicativo do ChatGPT para desktop.

1. Abra **Plug-ins**, encontre o plug-in Apple Messages e instale-o.
2. Inicie uma nova conversa no Codex ou no ChatGPT Work e peça para encontrar, resumir, redigir
ou enviar uma mensagem.
3. Conceda as permissões do macOS solicitadas antes que o ChatGPT leia o conteúdo do Messages.
4. Revise a mensagem e os destinatários antes de permitir o envio.

Por padrão, o ChatGPT só envia mensagens depois que você aprova a mensagem e os
destinatários. Escolha **Permitir uma vez** para aprovar apenas esse envio. Se selecionar
**Sempre permitir o envio para esta conversa**, o ChatGPT poderá enviar mensagens futuras
para essa conversa do Messages sem solicitar uma nova aprovação de envio.

Mantenha a aprovação a cada envio em conversas que possam conter instruções não confiáveis ou
enganosas. A aprovação persistente elimina sua última oportunidade de revisar uma mensagem
antes que o ChatGPT a envie em seu nome. Use-a somente se aceitar esse risco.

Para restaurar a aprovação a cada envio, abra **Configurações** \> **Uso do computador** e selecione
**Gerenciar** ao lado de **Messages**. Em **Envio sempre permitido**, selecione o
ícone de lixeira ao lado da conversa e confirme em **Remover**. O ChatGPT voltará a pedir aprovação
antes de enviar mensagens para essa conversa.

**Problema conhecido:** Se sua tarefa estiver configurada como **Acesso completo** ou desativar
as solicitações de aprovação de outra forma, o Apple Messages poderá não conseguir exibir a confirmação necessária
para o envio. Mude para **Pedir aprovação** ou **Aprovar por mim** e tente novamente.

O Apple Messages é executado no seu Mac. Ele não está disponível diretamente no ChatGPT na
Web ou em dispositivos móveis, no Codex CLI nem na extensão para IDE.

Em workspaces gerenciados, os administradores podem desativar o Apple Messages usando o
controle existente de Uso do computador.

<a id="plugin-directory-in-codex-cli"></a>

### Navegador de plug-ins no Codex CLI

No Codex CLI, execute o comando a seguir para abrir o navegador de plug-ins:

```text
codex
/plugins

  
    
  

O navegador de plug-ins da CLI agrupa os plug-ins por marketplace. Use as abas de marketplace
para alternar entre as fontes, abra um plug-in para conferir seus detalhes, instale ou desinstale
itens do marketplace e pressione <kbd>Espaço</kbd> em um plug-in instalado para
ativá-lo ou desativá-lo.

<a id="api-key-availability"></a>

### Disponibilidade com chave de API

Se você [entrar no Codex com uma chave de API
da OpenAI](/pt-BR/codex/auth#sign-in-with-an-api-key), poderá procurar, instalar e gerenciar
os plug-ins compatíveis selecionados pela OpenAI no Codex CLI e no Codex do aplicativo
do ChatGPT para desktop. Alguns plug-ins não estão disponíveis com autenticação por chave de API porque
seus fluxos de conexão exigem recursos OAuth sem suporte. Confira o uso dos plug-ins
na [página de uso da plataforma](https://platform.openai.com/usage).

### Como funcionam as permissões e o compartilhamento de dados

No ChatGPT na Web, Chat e Work usam as permissões e ferramentas do workspace
disponíveis para essa conversa. Os conectores ainda exigem login e acesso próprios.

Quando um recurso de um plug-in é executado por um host do Codex, aplicam-se o [sandbox e a
política de aprovação](/pt-BR/codex/agent-approvals-security) do host.
As conexões com serviços externos usam a autenticação e os controles
de acesso do próprio serviço.

- As habilidades incluídas ficam disponíveis quando você inicia uma nova conversa ou sessão da CLI
após a instalação.
- Se um plug-in incluir conectores, o produto em uso poderá solicitar que você instale
esses conectores ou faça login neles durante a configuração ou na primeira vez que os usar.
- Se um plug-in incluir servidores MCP, eles poderão exigir configuração adicional
ou autenticação antes que você possa usá-los.
- Quando o ChatGPT envia dados por meio de um conector incluído, aplicam-se os termos
e a política de privacidade desse serviço.

### Remover um plug-in

Para remover um plug-in, abra-o em um navegador de plug-ins compatível e selecione
**Desinstalar plug-in** quando essa ação estiver disponível. Plug-ins instalados no workspace ou
incluídos por padrão podem não oferecer essa ação; nesses casos, são controlados
pelo administrador do seu workspace.

Desinstalar um plug-in remove seu pacote daquele ambiente do ChatGPT ou do Codex,
mas os conectores incluídos permanecem conectados até que você os gerencie no
ChatGPT.

## Criar seu próprio plug-in

Se quiser criar, testar ou distribuir seu próprio plug-in, consulte
[Criar plugins](https://developers.openai.com/plugins/build/plugins). Essa página aborda a criação da estrutura local,
a configuração manual do marketplace, o compartilhamento no workspace, os manifestos de plug-ins e orientações
de empacotamento.

Se seu plug-in incluir recursos fornecidos por um servidor, consulte
[Criar um servidor MCP](https://developers.openai.com/plugins/build/mcp-server).
As ferramentas MCP podem funcionar sem uma interface personalizada ou retornar uma interface quando uma interface visual ajudar
no fluxo de trabalho.

Quando seu plug-in estiver pronto para revisão, consulte
[Enviar plug-ins](https://developers.openai.com/plugins/deploy/submission) para conhecer o fluxo de envio à Plataforma da OpenAI,
as permissões necessárias, os materiais para revisão, as verificações de MCP e os requisitos
para casos de teste.

## Guias de plug-ins

- [Gravar e reproduzir](/pt-BR/codex/extend/record-and-replay): Mostre ao ChatGPT um fluxo de trabalho
  uma vez e transforme-o em uma habilidade reutilizável.
- [Plugin Codex Security](/pt-BR/codex/security/plugin): Faça uma varredura em código autorizado,
  confirme os achados e prepare correções revisadas.

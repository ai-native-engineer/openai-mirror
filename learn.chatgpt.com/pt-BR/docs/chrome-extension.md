<!-- source: https://learn.chatgpt.com/pt-BR/docs/chrome-extension -->

Use a extensão do ChatGPT para navegadores para trabalhar no Google Chrome, Microsoft Edge,
Brave, Opera ou Vivaldi pelo aplicativo do ChatGPT para desktop. O ChatGPT pode ler conteúdo ou realizar ações
em sites nos quais você já fez login, como LinkedIn, Salesforce, Gmail
ou ferramentas internas.

Os cinco navegadores permitem mencionar abas e controlar o navegador pelo aplicativo
para desktop. Chrome, Edge, Brave e Vivaldi também oferecem chat lateral. **O Opera não
oferece chat lateral**; inicie as tarefas dele no aplicativo para desktop.

Atualize o aplicativo do ChatGPT para desktop antes de configurar outro navegador. A disponibilidade dos navegadores
pode depender da liberação do recurso e das configurações do seu workspace.

Para que o ChatGPT controle o navegador integrado em vez do seu navegador, use `@Browser`. O
[navegador integrado](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app)
permite fazer login e mantém as tarefas de navegação dentro do ChatGPT sem usar seu
perfil habitual do navegador.

O ChatGPT também pode alternar entre ferramentas conforme a tarefa exigir, usando plug-ins quando uma
integração dedicada estiver disponível, seu navegador quando precisar do contexto de uma sessão com login ativo
e o navegador integrado para localhost.

<div className="not-prose my-4">
  
</div>

<a id="use-chatgpt-from-chrome"></a>

## Use o chat lateral no navegador

O chat lateral está disponível no Chrome, Edge, Brave e Vivaldi.

Abra o ChatGPT ao lado da página que você está visualizando para fazer perguntas sobre ela ou prosseguir
com tarefas que podem usar o contexto da página junto com arquivos locais e aplicativos conectados.
O ChatGPT pode usar o contexto das abas abertas quando uma tarefa exigir.

1. Abra a página com a qual você quer trabalhar.
2. Selecione o ChatGPT na barra de ferramentas do navegador ou no menu **Extensões** . No macOS, você
   também pode pressionar <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>.</kbd>.
3. Faça uma pergunta sobre a página ou dê uma tarefa ao ChatGPT.

O painel permanece vinculado à aba em que você o abriu. Os chats iniciados no chat lateral
ficam disponíveis no aplicativo do ChatGPT, e você pode abrir chats recentes do ChatGPT
no chat lateral para continuar o trabalho em qualquer um dos dois.

  

## Adicione abas e texto selecionado a um chat

Mencione uma aba aberta do navegador no aplicativo para desktop quando quiser que o ChatGPT use
essa página como contexto. Nos navegadores com chat lateral, você também pode mencionar abas
nesse chat ou selecionar texto em uma página e adicionar a seleção ao chat para
perguntar sobre um trecho específico sem copiar a página inteira.

Nos navegadores com chat lateral, você também pode clicar com o botão direito na página e selecionar
**Perguntar ao ChatGPT**. O chat lateral é aberto com o contexto relevante da página para que você possa
continuar a solicitação no navegador.

### Faça uma pergunta sobre um vídeo do YouTube

Abra um vídeo do YouTube e faça uma pergunta sobre ele no chat lateral de um navegador compatível.
Quando houver legendas, o ChatGPT poderá usar a transcrição do vídeo com marcações de tempo
para explicar, resumir ou responder a perguntas sobre o conteúdo.

Trate o conteúdo de páginas da Web, o texto selecionado e as transcrições de vídeos como contexto não
confiável. Revise a página e todas as permissões solicitadas antes de pedir ao ChatGPT que
use essas informações ou realize ações com base nelas.

<a id="set-up-the-chrome-extension"></a>

## Configure seu navegador

Instale o navegador no computador e abra **Configurações \> Uso do computador** no
aplicativo do ChatGPT para desktop. Expanda **Mais navegadores** se o seu navegador não aparecer
na lista principal.

1. Selecione seu navegador e siga as instruções exibidas para instalar o plug-in necessário.
2. Selecione **Instalar** ao lado do navegador para abrir a página da extensão na loja.
   Instale a extensão do ChatGPT e revise as solicitações de permissão do navegador.
3. Volte a **Uso do computador** e confirme que o navegador exibe **Gerenciar**.
4. Inicie um chat no ChatGPT Work ou no Codex e selecione seu navegador usando uma
menção com `@`. Use o perfil do navegador em que você instalou a extensão.

O botão de ativação do navegador em **Uso do computador** controla se ele aparece no
menu de menções com `@`. Para alterar as permissões de sites, selecione **Gerenciar** .

  

<a id="start-a-chrome-task-from-chatgpt"></a>

## Inicie uma tarefa no navegador pelo ChatGPT

Após a configuração, inicie um novo chat no ChatGPT Work ou no Codex. Selecione **Chrome**, **Edge**,
**Brave Browser**, **Opera** ou **Vivaldi** no menu de menções com `@` para escolher
qual navegador o ChatGPT usa. Por exemplo:

```text
@Edge open Salesforce and update the account from these call notes.

Você também pode mencionar uma aba aberta para fornecer ao ChatGPT o contexto dessa página.
O Opera oferece suporte a esses fluxos de trabalho no aplicativo para desktop, embora não tenha chat lateral.

## Controle o acesso a sites

Por padrão, o ChatGPT pede confirmação antes de interagir com cada novo site. A solicitação
se baseia no host do site, como `example.com`.

Quando o ChatGPT pedir para usar um site, você poderá escolher a opção adequada à
tarefa e à sua tolerância a riscos:

- **Permitir uma vez** para que o ChatGPT use o site uma única vez.
- **Permitir para este site** para que o ChatGPT possa usar o site novamente sem perguntar.
- **Permitir para todos os sites** para que o ChatGPT possa usar sites sem perguntar.
- **Recusar** para impedir que o ChatGPT use o site.

### Gerencie sites permitidos e bloqueados

No aplicativo do ChatGPT para desktop, acesse **Configurações** \> **Uso do computador** e selecione
**Gerenciar** ao lado do seu navegador para gerenciar uma lista de permissões e uma lista de bloqueios de
domínios. A lista de permissões contém os domínios que o ChatGPT pode usar sem perguntar novamente.
A lista de bloqueios contém os domínios que o ChatGPT não deve usar. Os navegadores compatíveis
compartilham essas permissões de sites.

Quando um domínio é removido da lista de permissões, o ChatGPT volta a pedir confirmação antes de usá-lo.
Quando um domínio é removido da lista de bloqueios, o ChatGPT pode voltar a pedir confirmação em vez de
tratá-lo como bloqueado.

#### Permitir para todos os sites 

Se você selecionar **Permitir para todos os sites**, o ChatGPT deixará de pedir confirmação
antes de usar sites. Escolha essa opção somente se confiar no ChatGPT para usar qualquer
site aberto no navegador.

#### Histórico do navegador 

O histórico do navegador pode incluir telemetria sensível, URLs internas, termos de pesquisa
e atividades de sessões do navegador em dispositivos conectados à sua conta. Se você permitir que o ChatGPT
acesse o histórico do navegador, os registros relevantes poderão passar a fazer parte do contexto que
o ChatGPT usa na tarefa. Conteúdos de página maliciosos ou enganosos podem aumentar o
risco de o ChatGPT copiar esses dados para um local indevido.

O ChatGPT pede confirmação quando quer usar o histórico do navegador. O acesso ao histórico fica limitado à
solicitação, e não há uma opção para sempre permitir esse acesso.

## Dados e segurança

<a id="chrome-extension-permissions"></a>

### Permissões da extensão do navegador

O navegador pede que você aceite permissões ao instalar a extensão.
Por exemplo, a solicitação de permissão do Chrome pode incluir:

- Acessar o depurador da página
- Ler e alterar todos os seus dados em todos os sites
- Ler e alterar seu histórico de navegação em todos os dispositivos conectados à sua conta
- Exibir notificações
- Ler e alterar seus favoritos
- Gerenciar seus downloads
- Comunicar-se com aplicativos nativos compatíveis
- Ver e gerenciar seus grupos de abas

Com essas permissões, a extensão pode executar fluxos de trabalho no
navegador. O ChatGPT ainda usa suas próprias confirmações, configurações e listas de permissões e de
bloqueios antes de usar sites ou o histórico do navegador durante uma tarefa.

### Memórias

O Uso do computador respeita sua configuração de Memórias. Se o recurso Memórias estiver ativado, o ChatGPT pode
usar memórias salvas relevantes enquanto trabalha no seu navegador. Se estiver desativado,
o controle do navegador não usa memórias.

### Quais dados de navegação a OpenAI armazena

A OpenAI não armazena um registro completo e separado das suas ações no navegador realizadas por meio da
extensão. A OpenAI armazena atividades do navegador somente quando elas passam a fazer parte do contexto do ChatGPT,
como textos que o ChatGPT lê em uma página, capturas de tela, chamadas de ferramentas,
resumos, mensagens ou outros conteúdos incluídos no chat.

Seus controles de dados do ChatGPT se aplicam ao conteúdo processado no contexto.
Evite enviar segredos ou dados altamente sensíveis por meio de tarefas no navegador, a menos que
sejam necessários e você esteja presente para revisar cada prompt.

## Solução de problemas

Se o ChatGPT não conseguir se conectar ao seu navegador, primeiro confirme se o site que ele está tentando
acessar não está na lista de bloqueios em Configurações. Se o site não estiver bloqueado, faça
estas verificações:

1. Atualize o aplicativo do ChatGPT para desktop. Se você tiver mais de um aplicativo do ChatGPT ou do Codex
para desktop instalado, atualize todos eles ou remova as cópias que não usa mais.
2. Reinicie seu navegador. No Chrome, Edge, Brave ou Vivaldi, reabra o ChatGPT pela
   barra de ferramentas ou pelo menu **Extensões** e confirme se o chat lateral é carregado. O Opera
   não tem chat lateral; verifique a conexão pelo aplicativo para desktop.
3. Em **Configurações \> Uso do computador**, confirme se seu navegador aparece e exibe
**Gerenciar**. Se ainda exibir **Instalar**, siga o fluxo de configuração novamente.
   Ative a opção do navegador se ele não aparecer no menu de menções com `@`.
4. Verifique se você está usando o perfil do navegador em que a extensão está
instalada. Se você usa mais de um perfil, instale e ative a
extensão no perfil ativo.
5. Inicie um novo chat no ChatGPT Work ou no Codex e tente executar a tarefa no navegador novamente. Isso pode
limpar o estado de conexão específico do chat.
6. Reinicie o aplicativo do ChatGPT para desktop e tente novamente. Se a extensão ainda
   não se conectar, reinstale-a em **Configurações \> Uso do computador**.
7. Se o ChatGPT ainda não conseguir usar o navegador, execute `/feedback`
   no aplicativo e inclua o ID do chat ao entrar em contato com o suporte.

### Fazer upload de arquivos

Se uma tarefa no Chrome precisar fazer upload de um arquivo do seu computador, permita que a Extensão do Chrome
acesse URLs de arquivos no Chrome:

1. No Chrome, clique no ícone de extensões na barra de ferramentas e depois em **Gerenciar
   extensões**.
2. No cartão da extensão, clique em **Detalhes**.
3. Ative **Permitir acesso a URLs de arquivos**.

Depois de alterar a configuração, inicie novamente a tarefa do Chrome.

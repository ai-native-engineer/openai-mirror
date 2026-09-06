<!-- source: https://learn.chatgpt.com/pt-BR/docs/browser -->

O Navegador não está disponível no Codex CLI nem na extensão do Codex para IDE. Abra o
aplicativo do ChatGPT para desktop para usar o navegador integrado.

O Navegador permite que o ChatGPT abra sites, obtenha informações atualizadas e realize ações
enquanto você mantém o controle. Use-o para comparar opções, concluir uma tarefa de várias etapas
em um site ou revisar uma página que você está criando.

O Navegador está disponível no ChatGPT na Web e no aplicativo do ChatGPT para desktop.

O [GPT-6 Astra](/pt-BR/codex/models#gpt-6-astra) melhora a avaliação visual em tarefas como
comparar uma página com uma captura de tela ou concluir um fluxo de trabalho em vários sites.
Escolha-o quando estiver disponível no seletor de modelos e descreva como verificar o
resultado final.

Em ambientes de desktop gerenciados, os administradores podem restringir as origens acessadas pelo navegador,
uploads, downloads e o acesso de desenvolvedor. Consulte os
[controles de navegador gerenciado](/pt-BR/codex/enterprise/managed-configuration#control-browser-and-computer-use).

Trate o conteúdo da página como contexto não confiável. Analise o site e a ação proposta
antes de compartilhar informações confidenciais ou permitir que o ChatGPT aja.

O navegador integrado ao aplicativo do ChatGPT para desktop oferece a você e ao ChatGPT uma visão
compartilhada de sites e aplicativos Web locais dentro de um chat. Use-o para visualizar uma página,
deixar feedback visual ou permitir que o ChatGPT interaja com um site em seu nome.

O navegador integrado usa um perfil separado do perfil do seu navegador
habitual. Ele não compartilha automaticamente suas abas existentes nem sua sessão de navegação.
Você pode fazer login diretamente quando uma tarefa exigir uma conta. Abra **Configurações \>
Navegador** para gerenciar os dados do navegador e os recursos de importação de perfil disponíveis no
seu dispositivo.

Por padrão, os downloads do Navegador são salvos na pasta Downloads do sistema. Em **Configurações \>
Navegador**, você pode escolher outro local de download, restaurar o local padrão do
sistema ou ativar **Perguntar onde salvar os downloads**.

Use a [extensão do navegador](/pt-BR/codex/chrome-extension) como alternativa quando o ChatGPT precisar
trabalhar em uma aba existente do Chrome, Edge, Brave, Opera ou Vivaldi ou usar o
perfil do seu navegador habitual.

Abra o navegador integrado pela barra de ferramentas, clicando em uma URL, navegando
manualmente ou pressionando <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>
(<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd> no Windows).

  
    
  

## Pesquisar pela barra de endereços

Comece a digitar na barra de endereços do navegador integrado para encontrar páginas no
histórico de navegação. Selecione uma página correspondente para reabri-la ou insira um termo
de pesquisa para pesquisar no Google quando não houver correspondências no histórico.

O navegador integrado mantém um perfil e um histórico de navegação próprios. Os resultados não
incluem automaticamente páginas do seu perfil habitual do Chrome nem de outros navegadores.

## Gerenciar o histórico de navegação

Abra **Configurações \> Navegador** para pesquisar no histórico do navegador integrado, reabrir uma
página visitada ou remover entradas do histórico quando sua organização permitir. Use
**Limpar dados de navegação** para escolher um período e os tipos de dados de navegação
que você quer remover.

Quando esse recurso estiver disponível, o ChatGPT pode pedir para pesquisar seu histórico de navegação e encontrar uma página
relevante para a tarefa atual. Analise a solicitação antes de permitir o acesso.
O histórico de navegação pode incluir URLs internas, termos de pesquisa e outras informações
confidenciais, então permita o acesso somente quando a tarefa exigir esse contexto.

<a id="browser-use"></a>

## Uso do computador no navegador

No aplicativo para desktop, o Uso do computador permite que o ChatGPT Work ou o Codex controle o
navegador integrado diretamente. A experiência selecionada pode abrir páginas, clicar, digitar,
inspecionar o estado renderizado, fazer capturas de tela e verificar o resultado do trabalho realizado
na página.

O Navegador vem incluído no aplicativo para desktop e é instalado automaticamente. Peça ao ChatGPT
ou ao Codex para usar o navegador integrado na tarefa ou faça referência direta a ele com
`@Browser`.

Por exemplo:

```text
Use the browser to open http://localhost:3000/settings, reproduce the layout
bug, and fix only the overflowing controls.

O ChatGPT pede permissão antes de usar um site, a menos que você já tenha autorizado esse
site. Gerencie os sites permitidos e bloqueados em **Configurações \> Navegador**. O ChatGPT também
pede confirmação antes de ações sensíveis, como enviar informações,
fazer uma compra, alterar permissões ou excluir dados. O ChatGPT não consegue
automatizar o upload de arquivos no navegador integrado.

  As instruções de uma página podem ser enganosas ou maliciosas. A permissão para usar um site
permite que o ChatGPT interaja com esse site; ela não torna o conteúdo dele
confiável nem aprova todas as ações.

## Visualizar uma página

1. Inicie o servidor de desenvolvimento do seu aplicativo no [terminal integrado](/pt-BR/codex/integrated-terminal) ou com uma [ação do ambiente local](/pt-BR/codex/environments/local-environment#actions).
2. Abra a rota local, a página baseada em arquivo ou a página pública clicando em uma URL ou
navegando manualmente no navegador.
3. Revise o estado renderizado junto com o diff do código.
4. Deixe comentários no navegador sobre os elementos ou áreas que precisam de alterações.
5. Peça ao ChatGPT para fazer as alterações indicadas nos comentários e manter o escopo delimitado.

Por exemplo:

```text
I left comments on the pricing page in the built-in browser. Address the mobile
layout issues and keep the card structure unchanged.

## Comentar na página

Quando um bug só estiver visível na página renderizada, use os comentários no navegador para dar
feedback preciso ao ChatGPT.

1. Ative o **Modo de anotação**.
2. Clique em um elemento ou arraste para selecionar uma área.
3. Escreva e salve seu comentário.
4. Envie uma mensagem no chat pedindo ao ChatGPT para fazer as alterações indicadas nos comentários.

Os comentários funcionam melhor quando você identifica o problema e o resultado desejado:

```text
This button overflows on mobile. Keep the label on one line if it fits,
otherwise wrap it without changing the card height.

```text
This tooltip covers the data point under the cursor. Reposition the tooltip so
it stays inside the chart bounds.

<section class="feature-grid">

<div>

### Feedback sobre estilo

Ao adicionar uma anotação a uma seção da página, selecione **Ajustar** ao lado do
campo de texto para dar ao ChatGPT um feedback mais detalhado sobre o estilo. Você pode alterar
valores como fonte, texto, espaçamento e cor, visualizar o resultado na página
e, em seguida, enviar a anotação com um objetivo mais claro.

</div>

  
    
  

</section>

## Delimite o escopo das tarefas do navegador

Mantenha cada tarefa do navegador pequena o suficiente para revisá-la de uma só vez.

- Especifique a página, a rota ou a URL.
- Especifique o estado de seu interesse, como carregamento, vazio, erro ou sucesso.
- Deixe comentários exatamente nos elementos ou áreas que precisam de alterações.
- Revise a página novamente depois que o ChatGPT concluir a tarefa.
- Peça ao ChatGPT para iniciar ou verificar o servidor de desenvolvimento antes de abrir uma página
local.

Para alterações no repositório, use o [painel de revisão](/pt-BR/codex/code-review?surface=app) para
inspecionar as alterações e deixar comentários.

<section class="feature-grid">

<div>

## Modo de desenvolvedor

O modo de desenvolvedor funciona com o Uso do computador no Chrome e no navegador integrado. Ele
oferece ao ChatGPT acesso controlado ao Chrome DevTools Protocol (CDP). Use-o para
analisar o desempenho do JavaScript, inspecionar a saída do console e o tráfego de rede, examinar o DOM
e os estilos aplicados ou diagnosticar uma issue no navegador em execução.

Para ativá-lo, abra [**Configurações \> Navegador**](codex://settings/browser-use) e,
em **Modo de desenvolvedor**, ative **Habilitar acesso completo ao CDP**. Se sua
organização tiver desativado essa configuração, não será possível ativá-la localmente. Os administradores podem
definir `browser_use_full_cdp_access = false` em `[features]` no arquivo
[`requirements.toml`](/pt-BR/codex/enterprise/managed-configuration#pin-feature-flags)
para desativar o acesso completo ao CDP e impedir que os usuários ativem a configuração
correspondente no aplicativo do ChatGPT para desktop.

O acesso completo ao CDP pode expor informações internas confidenciais do navegador. O ChatGPT solicita
aprovação explícita antes de usar o acesso completo ao CDP para inspecionar um site. Analise o
site, a tarefa e o acesso solicitado antes de aprová-lo.

Use `@Browser` para o navegador integrado. Para usar o modo de desenvolvedor no Chrome,
[configure a extensão do Chrome](/pt-BR/codex/chrome-extension) e invoque `@Chrome`.

Por exemplo:

```text
This app is slow. Use @Browser to capture a performance trace and inspect
network traffic, then identify the bottleneck.

</div>

  
    
  

</section>

## Use o ChatGPT Work para realizar tarefas na Web

O ChatGPT Work pode concluir tarefas em diferentes sites, inclusive naqueles em que você precisa fazer login.

O Work usa seu próprio navegador, executado em um computador separado na nuvem, e não o navegador do seu celular ou notebook.

Inicie uma tarefa no ChatGPT Work na Web ou em um dispositivo móvel, e o ChatGPT poderá continuar trabalhando mesmo que você se afaste e feche o computador. Usando seu próprio computador, o Work pode realizar uma grande variedade de tarefas na internet lendo, clicando e digitando em páginas da Web. Dependendo da sua solicitação, ele pode usar um plug-in, seu navegador ou ambos.

Por exemplo, o ChatGPT pode ajudar você a:

- Encontrar e agendar um atendimento no DMV.
- Fazer login na sua conta da concessionária de serviços públicos e comparar planos.
- Encontrar e salvar apartamentos que atendam aos seus critérios.
- Pesquisar concorrentes nas redes sociais.
- Fazer o fechamento contábil no seu software de contabilidade.

Você controla quais sites o ChatGPT pode acessar, e ele é treinado para pedir confirmação antes de realizar ações com consequências relevantes, como concluir uma reserva ou um pagamento. Se o ChatGPT ficar impedido de continuar por qualquer motivo, você pode assumir o controle do computador dele e usá-lo diretamente, tanto em dispositivos móveis quanto em computadores.

O recurso que permite ao ChatGPT Work navegar em sites que exigem autenticação está disponível na Web e em dispositivos móveis nos planos Plus e Pro.

A disponibilidade depende da liberação gradual. O login em sites não está disponível para workspaces dos planos Empresas ou Edu.

## Como funciona o computador do ChatGPT Work

Quando sua tarefa exige o uso de um site, o ChatGPT usa seu próprio navegador para navegar pelas páginas, reunir informações e concluir etapas online.

Por padrão, o ChatGPT pede permissão antes de acessar um novo site. Você pode aprovar as solicitações individualmente ou ajustar as configurações para permitir que o ChatGPT aprove automaticamente o acesso a sites relevantes para sua tarefa. O ChatGPT Work sempre pedirá confirmação antes de realizar ações com consequências relevantes, como enviar suas informações para agendar um atendimento ou concluir um pagamento.

## Faça login em um site

Se um site exigir login, o ChatGPT Work pedirá que você faça login. Após a autenticação, ele continuará trabalhando no site com sua sessão iniciada. Sua sessão permanecerá ativa para tarefas futuras, então você não precisará fazer login a cada vez.

### Use o formulário de login seguro

O ChatGPT não pode ver seu nome de usuário nem sua senha, e esses dados nunca são vistos pelo modelo nem usados no treinamento de modelos. O ChatGPT não armazena seu nome de usuário nem suas senhas. Você pode excluir seu histórico de navegação de todos os sites ou de um site específico a qualquer momento em **Configurações** \> **Navegador na nuvem** \> **Dados do navegador**, o que encerrará sua sessão nesse site.

Ao encontrar uma tela de login, o ChatGPT pausa a tarefa e pede que você insira suas credenciais e os códigos de autenticação de dois fatores, conforme necessário. No iOS, você pode usar um gerenciador de senhas compatível para fazer login com facilidade.

Use o formulário de login fornecido pelo ChatGPT. Não envie senhas no chat.

![ChatGPT Work no iOS pausando uma tarefa no DMV e exibindo um formulário de login seguro com o endereço do site e uma senha mascarada.](/images/codex/cloud-browser-auth/sign-in.webp)

### Faça login na página da Web

Se essa opção estiver disponível, selecione **Fazer login na página da Web em vez disso** para fazer login diretamente no navegador na nuvem. A tarefa fica pausada enquanto você faz login. Selecione **Concluí** para devolver o controle ao ChatGPT, ou pule ou cancele a solicitação.

<a id="start-a-browser-task"></a>
<a id="start-browser-work"></a>
<a id="web-start-browser-work"></a>

## Como iniciar uma tarefa no ChatGPT Work

1. Abra o ChatGPT na Web ou em um dispositivo móvel e inicie uma tarefa no Work.
2. Descreva o que você quer que o ChatGPT faça.
3. Aprove o acesso ao site, se solicitado.
4. Faça login diretamente caso o site exija.
5. Acompanhe o progresso da tarefa na conversa.
6. Revise o resultado e aprove quaisquer ações com consequências relevantes.

Você não precisa selecionar o navegador separadamente. O ChatGPT decide quando usá-lo com base na sua solicitação.

Alguns sites bloqueiam o acesso. Se isso acontecer, o ChatGPT avisará e, quando possível, tentará outra forma de concluir a tarefa.

<a id="website-permissions-and-confirmations"></a>
<a id="web-website-permissions-and-confirmations"></a>

## Segurança e controles do usuário

Nas configurações do ChatGPT, abra **Navegador na nuvem** para gerenciar as permissões de sites. As opções disponíveis incluem:

- **Sempre perguntar**: Revise manualmente cada solicitação de acesso a sites.
- **Aprovar automaticamente**: Permita que o ChatGPT aprove o acesso automaticamente depois de verificar se o site é relevante para sua tarefa.
- **Sempre permitir**: Permita o acesso a sites sem essa etapa adicional de revisão. Oferecemos essa opção para tornar o uso o mais simples possível, mas não a recomendamos.

![Configurações do navegador na nuvem mostrando as opções de permissão de sites Sempre perguntar, Aprovar automaticamente e Sempre permitir.](/images/codex/cloud-browser-auth/website-permissions.webp)

Você também pode permitir ou bloquear sites específicos para substituir suas permissões padrão nesses sites.

Antes de o ChatGPT pedir que você faça login em qualquer site, um modelo adicional de revisão verifica a solicitação de login e o local onde suas informações serão inseridas para identificar sinais de phishing ou práticas enganosas. Testamos o agente contra riscos como injeção de prompt, phishing e ações não intencionais.

Para garantir total transparência, você verá o endereço do site e uma prévia do formulário de login, e poderá inspecionar o site em tempo real antes de continuar. As credenciais inseridas pelo formulário de login seguro vão diretamente para o navegador e não ficam visíveis para o modelo.

<a id="browser-data"></a>
<a id="web-browser-data"></a>

## Privacidade e dados do navegador

O computador do ChatGPT Work funciona separadamente do navegador do seu dispositivo. Ele mantém seus próprios cookies, dados do navegador e sessões autenticadas. As informações usadas pelo ChatGPT ao realizar uma tarefa são tratadas de acordo com as configurações de controle de dados que você escolhe no ChatGPT. Você pode revisar essas configurações no ChatGPT na Web e em dispositivos móveis, em **Configurações** \> **Controles de dados**.

Ele não usa as abas abertas, o histórico de navegação, as senhas salvas, os cookies, as extensões nem as sessões autenticadas existentes do seu navegador pessoal.

Para limpar os dados do navegador, acesse **Configurações** \> **Navegador na nuvem** \> **Dados do navegador** \> **Limpar tudo**. Com isso, suas sessões nos sites são encerradas no navegador do ChatGPT Work, e você precisará fazer login novamente para tarefas futuras.

![Configurações do navegador na nuvem com a seção Dados do navegador e o controle Cookies para gerenciar os cookies salvos pelo navegador na nuvem.](/images/codex/cloud-browser-auth/browser-data.webp)

## Limitações

- O login em sites não está disponível em todos os workspaces nem em todas as etapas da liberação gradual. Se uma tarefa exigir um método de login que não tenha suporte, conclua essa etapa por conta própria ou use outra ferramenta disponível.
- Alguns sites bloqueiam navegadores automatizados ou exigem um CAPTCHA. O ChatGPT talvez não consiga concluir uma tarefa nesses sites.
- A disponibilidade da navegação na nuvem pode depender do seu plano, das configurações do workspace e da liberação gradual. A navegação na nuvem está disponível em todas as regiões nos planos pagos, exceto Free e Go. Os administradores de Empresas precisam ativar a navegação na nuvem para o workspace.

Durante a liberação gradual, o navegador pode não aparecer imediatamente, mesmo que seu plano ofereça suporte ao recurso.

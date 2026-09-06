<!-- source: https://learn.chatgpt.com/pt-BR/docs/customization/computer-history -->

O Histórico do computador fica **desativado por padrão** para usuários dos planos ChatGPT Pro, Business e
  Empresas no aplicativo do ChatGPT para desktop no macOS. Usuários do plano Pro podem optar por
  ativá-lo. Nos workspaces dos planos Business e Empresas, um administrador deve
  conceder acesso explicitamente antes que cada membro possa optar por ativar o recurso. O Histórico do
  computador também exige [Memórias](/pt-BR/codex/customization/memories) e não está
  disponível por meio de uma chave de API nem do Amazon Bedrock. Está disponível nas regiões com suporte,
  incluindo o Espaço Econômico Europeu (EEE), a Suíça e o Reino
  Unido.

O Histórico do computador transforma suas atividades em aplicativos e sites em
memórias e em uma linha do tempo que o ChatGPT e o Codex podem consultar. Você
pode fazer perguntas em linguagem natural sobre o trabalho recente, retomar de onde parou,
entender padrões na sua forma de trabalhar e transformar fluxos de trabalho recorrentes em habilidades ou automações.

Seu histórico só começa quando você decide ativá-lo. Você controla quais
aplicativos e sites contribuem, pode visualizar e pausar a coleta pela barra de
menus do macOS e pode consultar ou excluir seu histórico a qualquer momento.

O Histórico do computador substitui a prévia de pesquisa anterior do Chronicle,
mas é um sistema reconstruído, não apenas uma mudança de nome. Ele usa eventos de
interação, além de textos e outras informações contextuais disponíveis por meio dos
recursos de acessibilidade do macOS, para criar resumos que você pode revisar e excluir.
Não inclui capturas de tela no seu histórico nem grava áudio, e as atividades de
navegação em modo privado nunca são incluídas.

  

## Como o Histórico do computador ajuda

O Histórico do computador fornece atividades recentes como contexto. Quando um
arquivo, uma conversa no Slack, um documento do Google Docs ou outra fonte é mais
adequada para a tarefa, o ChatGPT e o Codex podem usar o histórico para identificar essa fonte e depois lê-la diretamente.

<section class="feature-grid mt-4">

<div>

### Retome de onde parou

Pergunte o que você estava fazendo antes de uma pausa sem precisar reconstituir
quais aplicativos e documentos estavam abertos nem quais eram os próximos passos.

</div>

</section>

<section class="feature-grid inverse">

<div>

### Encontre atividades recentes

Descreva um documento, uma conversa ou uma tarefa da maneira como você se lembra.
O Histórico do computador pode usar a linha do tempo de atividades para identificar a fonte à qual você se refere.

</div>

</section>

<section class="feature-grid">

<div>

### Reutilize fluxos de trabalho

Quando o Histórico do computador identifica atividades que podem ser repetidas,
uma entrada na linha do tempo pode sugerir uma habilidade ou automação. Revise a sugestão
e peça ao Codex para criá-la a partir do fluxo de trabalho registrado.

</div>

</section>

## Como funciona o Histórico do computador

O Histórico do computador cria um fluxo de eventos de interação de aplicativos e
sites autorizados. Os eventos podem incluir cliques, digitação, atalhos de
teclado, alternância entre aplicativos e contexto disponibilizado pelo sistema
de acessibilidade do macOS. Periodicamente, o Histórico do computador transforma
esses eventos em resumos de texto e arquivos de memória locais.

O Histórico do computador não inclui capturas de tela no seu histórico nem grava
o áudio do microfone ou do sistema. A atividade de navegação na Web em modo
privado nunca é incluída.

Em **Configurações \> Histórico do computador \> Histórico**, a linha do tempo agrupa os resumos por
dia e horário. Cada item pode mostrar:

- Um título e um resumo em texto da atividade.
- Os aplicativos que contribuíram para o resumo.
- Uma habilidade ou automação sugerida quando o ChatGPT identifica atividades recorrentes.
- Ações para exibir o arquivo de memória no Finder ou excluir o item.

Selecione **Perguntar sobre seu histórico** para iniciar um chat com o Histórico do computador ou use
prompts como:

- “Em que eu estava trabalhando antes da minha última pausa?”
- “Onde posso encontrar o documento da proposta que eu procurava hoje mais cedo?”
- “Liste as tarefas em que trabalhei hoje e o status de cada uma.”
- “Prepare um resumo do que fiz ontem para o standup.”

## Permissões e acesso

O Histórico do computador usa controles separados para acesso ao workspace,
adesão individual, memórias e aplicativos ou sites incluídos no seu histórico:

- **Acesso ao workspace:** o Histórico do computador vem desativado por padrão em workspaces Business e
  Enterprise e fica indisponível até que um administrador
  conceda acesso explicitamente. Administradores de workspaces Enterprise podem usar **Ativar Histórico
  do computador** em [**Configurações do workspace \> Permissões e funções**](https://chatgpt.com/admin/settings)
  para conceder acesso às funções apropriadas do workspace.
- **Adesão individual:** conceder acesso ao workspace apenas permite que um membro escolha
  ativar o Histórico do computador. Isso não ativa o recurso para ninguém. Cada
  pessoa deve aderir individualmente, inclusive usuários do ChatGPT Pro.
- **Memórias:** o Histórico do computador também requer [Memórias](/pt-BR/codex/customization/memories).
  Use `/memories` para controlar se um chat específico pode usar memórias locais
  ou contribuir para futuras memórias.
- **Aplicativos e sites:** suas permissões para aplicativos e sites determinam quais
  fontes podem contribuir com eventos de interação. Você pode permitir apenas fontes
  específicas ou excluir aplicativos e URLs de sites que não deseja incluir.

Se sua função no workspace não tiver acesso, nenhuma alteração nas configurações
locais poderá ativar o Histórico do computador.

## Ativar o Histórico do computador

O Histórico do computador vem desativado por padrão. Se você usa um workspace
Business ou Enterprise, peça ao administrador que conceda acesso antes de ativá-lo.
A aprovação do administrador não significa que você aderiu ao recurso.

1. Abra o aplicativo do ChatGPT para desktop no macOS.
2. Em Configurações, na seção **Integrações**, selecione **Histórico do computador**.
3. Selecione **Ativar** e analise as informações sobre privacidade, permissões e armazenamento
   local.
4. Se solicitado, ative **Memórias**. O Histórico do computador precisa de Memórias para
   usar o contexto das atividades em diferentes chats e tarefas.
5. Escolha quais aplicativos e sites podem contribuir para o seu histórico e siga
as solicitações de permissão do macOS.

O Histórico do computador não requer a permissão de Gravação de Tela. Se a
configuração não aparecer, confirme se seu plano oferece suporte ao Histórico do
computador e se o administrador do workspace o ativou, quando aplicável.

## Controle o que é incluído

Você controla quais aplicativos e sites contribuem para registros futuros e se
o Histórico do computador está coletando ativamente eventos de interação.

### Escolha aplicativos e sites

Em **Configurações \> Histórico do computador \> Permissões**, escolha quais aplicativos e
sites o Histórico do computador pode incluir:

- **Excluir estes aplicativos** e **Excluir estes sites** bloqueiam os aplicativos ou URLs
  que você especificar, permitindo outras fontes compatíveis.
- **Incluir somente estes aplicativos** e **Incluir somente estes sites** permitem apenas as
  fontes escolhidas explicitamente por você.

Você também pode selecionar o ícone de um aplicativo em um item da linha do tempo
do histórico para excluí-lo dos registros futuros. É possível voltar a incluí-lo depois.

A atividade de navegação na Web em modo privado nunca é incluída. Alterar as
permissões de aplicativos ou sites afeta os registros futuros. Para remover itens
já existentes, exclua-os ou limpe o histórico.

### Pausar, retomar ou interromper a coleta

Use as configurações do Histórico do computador ou a barra de menus do macOS para
controlar quando o recurso coleta atividades:

- Selecione o ícone do ChatGPT na barra de menus do macOS e expanda o menu Histórico
do computador para ver quais atividades são capturadas e acessar seus controles.
- Selecione **Pausar** para interromper a coleta de novos eventos de interação ou selecione
**Retomar** quando quiser reiniciá-la.
- Desative o Histórico do computador para interromper a coleta de atividades futuras.

O Histórico do computador pode incluir eventos de interação de aplicativos e
sites de comunicação. Desative-o durante comunicações com outras pessoas, a menos
que tenha o consentimento prévio e expresso delas. Considere pausar o recurso ou
excluir aplicativos que contenham informações sensíveis de saúde, financeiras ou pessoais.

## Revisar e limpar o histórico

Abra **Configurações \> Histórico do computador \> Histórico** para verificar o que o Histórico do computador
resumiu. Você pode exibir o arquivo de memória local de um resumo no Finder, excluir
um item específico da linha do tempo ou limpar os últimos 10 minutos, a última hora, o último dia
ou todo o histórico. A barra de menus do macOS também permite limpar a última sessão de um
aplicativo usado recentemente.

Limpar o histórico exclui os respectivos eventos de interação e todas as memórias
criadas a partir deles. Essa ação não pode ser desfeita.

## Privacidade e armazenamento local

O Histórico do computador armazena temporariamente o fluxo de eventos de interação
no seu Mac para que o ChatGPT e o Codex possam gerar memórias e criar sugestões de
fluxos de trabalho. Esse fluxo pode incluir atividades como cliques e digitação,
além de textos e outras informações de contexto disponíveis pelos recursos de
acessibilidade do macOS. O Histórico do computador não inclui capturas de tela no
seu histórico nem grava o áudio do microfone ou do sistema. A atividade de
navegação na Web em modo privado nunca é incluída.

Os arquivos temporários de eventos são mantidos por até 48 horas. Os arquivos de
memória gerados permanecem no seu sistema de arquivos até que você os exclua ou
limpe o histórico, e podem ser exibidos na linha do tempo do Histórico.

### Onde o Histórico do computador armazena meus dados?

O Histórico do computador salva temporariamente eventos de interação no seu Mac.
Os arquivos desses eventos ficam isolados no
[App Group](https://developer.apple.com/documentation/xcode/protecting-local-app-data-using-containers) do ChatGPT,
o que impede outros aplicativos de acessá-los sem permissão explícita.
O ChatGPT e o Codex excluem esses arquivos de eventos após 48 horas.

O Histórico do computador gera o mesmo tipo de memórias locais que o Codex: arquivos
Markdown de texto simples que você pode ler e modificar. Esses arquivos são armazenados
em `$CODEX_HOME/memories/extensions/skysight/`, caminho que normalmente corresponde a
`~/.codex/memories/extensions/skysight/`.

<div className="not-prose my-4">
  
</div>

### Quais dados são compartilhados com a OpenAI?

O Histórico do computador captura eventos de interação localmente e inicia
periodicamente uma sessão efêmera do Codex com acesso ao fluxo desses eventos
para resumir suas atividades em memórias.

A OpenAI processa arquivos temporários de eventos em seus servidores para gerar
memórias, que são armazenadas localmente no seu Mac. A OpenAI não mantém esses
arquivos após o processamento, exceto quando exigido por lei, e não os utiliza
para treinamento.

Quando o ChatGPT ou o Codex usa uma memória em um chat futuro, conteúdos relevantes da memória
e eventos de interação podem ser incluídos como contexto. Esse conteúdo do chat pode ser
usado para aprimorar os modelos da OpenAI, se isso for permitido pelos seus
[controles de dados do ChatGPT](https://help.openai.com/en/articles/7730893-data-controls-faq).
As memórias também seguem os mesmos
[controles por chat aplicáveis às demais memórias do Codex](/pt-BR/codex/customization/memories#control-memories-per-chat).

### Risco de injeção de prompt

O Histórico do computador aumenta o risco de injeção de prompt por meio de
conteúdos em aplicativos e sites. Por exemplo, se você visitar um site com
instruções maliciosas, o ChatGPT ou o Codex pode seguir essas instruções.

## Uso de tokens

O Histórico do computador usa tokens ao resumir atividades e criar memórias.

## Solução de problemas

Se o Histórico do computador estiver disponível, mas não iniciar:

1. Confirme se o recurso **Memórias** está ativado.
2. Abra **Configurações \> Histórico do computador** e selecione **Concluir configuração**, **Retomar**
   ou **Tentar novamente**, conforme o status exibido.
3. Encerre e reabra o aplicativo do ChatGPT para desktop se a configuração continuar indisponível.

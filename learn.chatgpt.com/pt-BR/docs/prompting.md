<!-- source: https://learn.chatgpt.com/pt-BR/docs/prompting -->

<a id="prompts"></a>

## Visão geral da criação de prompts

Ao criar prompts, você diz ao ChatGPT o que quer saber, criar ou alterar. Um prompt
pode ser uma pergunta, uma instrução ou uma meta. Você não precisa usar sintaxe técnica nem
seguir uma fórmula rígida. Comece com suas próprias palavras, revise a resposta e use mensagens de acompanhamento
para ajustar o resultado.

Um prompt curto costuma ser suficiente. Para tarefas maiores ou mais importantes, inclua as
partes relevantes:

- **Meta:** O que o ChatGPT deve fazer?
- **Contexto:** Quais informações ou fontes podem ajudar?
- **Resultado:** De qual formato, extensão ou nível de detalhe você precisa?
- **Limites:** O que deve permanecer inalterado? O que o ChatGPT deve evitar ou confirmar
  com você antes de agir?

Use apenas as partes que forem úteis. Não é preciso preencher todos os itens nem seguir um
formato obrigatório.

## Descreva o resultado de que você precisa

Comece pelo resultado, não por uma lista detalhada de etapas. Inclua o público ou o
formato quando esses detalhes mudarem o que o ChatGPT deve produzir.

```text
Turn these meeting notes into a short update for the project team.
Put the decisions and next steps first.

Este prompt explica o que criar e quem vai ler. Descreva um processo quando
o próprio processo for importante. Caso contrário, dê liberdade ao ChatGPT para pesquisar, comparar
informações e ajustar sua abordagem.

<a id="context"></a>

## Adicione contexto útil

Compartilhe as informações que possam alterar o resultado. Adicione apenas as fontes que
forem relevantes e explique o que o ChatGPT deve extrair de cada uma.

- Anexe documentos, planilhas, apresentações ou arquivos PDF quando quiser
  que o ChatGPT os resuma, compare ou transforme, ou que [crie arquivos para revisão](/pt-BR/codex/artifacts-viewer).
- Adicione uma captura de tela, um diagrama ou outra [entrada de imagem](/pt-BR/codex/image-inputs) quando a
  tarefa depender do contexto visual. Indique a área relevante, em vez de
  depender apenas da imagem.
- Peça ao ChatGPT para usar a [Pesquisa na Web](/pt-BR/codex/web-search) quando a resposta depender de
  informações atuais e solicite as fontes quando precisar verificar o resultado.
- Use um [projeto](/pt-BR/codex/projects) quando chats relacionados precisarem compartilhar arquivos,
  fontes ou uma pasta local.

### Use fontes conectadas

Quando o ChatGPT tiver acesso a fontes conectadas, informe onde ele deve procurar e o que
deve encontrar. Não é preciso descrever cada pesquisa que ele deve fazer.

```text
Use the latest project plan in Drive and relevant decisions and updates from
the project's Slack channel to prepare a status update.

As fontes conectadas exigem o plug-in correspondente, e a disponibilidade pode depender do
seu plano e das configurações do workspace.

### Use plug-ins

Plug-ins oferecem ao ChatGPT e ao Codex instruções reutilizáveis e conexões com ferramentas
como Google Drive, Gmail, Slack e GitHub. Ambos os produtos usam
plug-ins públicos do mesmo diretório universal. Peça o resultado de que precisa e deixe
a interface ativa escolher entre as ferramentas disponíveis. No ChatGPT, digite `@`
no campo de mensagem para escolher um plug-in específico.

  
    <span slot="icon">
      
    </span>
    Encontre, instale e use plug-ins no ChatGPT e no Codex.
  

### Personalize o ChatGPT

Use **Configurações \> Personalização**
para salvar como instruções personalizadas as preferências que devem valer em todos os chats. Mantenha no
prompt os detalhes relevantes apenas para o chat atual.

  
    <span slot="icon">
      
    </span>
    Defina uma personalidade padrão, instruções personalizadas e outras preferências do aplicativo.
  

## Estabeleça limites que evitem problemas reais

Limites são as poucas instruções de que o ChatGPT precisa para não gerar trabalho extra
nem executar uma ação que você não pretendia. Adicione um limite quando alterar o detalhe errado
puder tornar o resultado inutilizável ou quando você quiser revisar algo antes que isso
afete outras pessoas.

- Mantenha inalteradas as datas aprovadas e os valores do orçamento.
- Use somente as fontes fornecidas. Sinalize informações ausentes em vez de fazer suposições.
- Mantenha as recomendações dentro do orçamento informado.
- Prepare a mensagem como rascunho. Não a envie.

Concentre-se em um ou dois limites mais importantes. Não é preciso controlar
cada etapa realizada pelo ChatGPT.

## Deixe o resultado pronto para uso

Diga ao ChatGPT como você pretende usar o resultado. Isso o ajuda a escolher a
extensão, o nível de detalhe e a organização adequados.

- Crie um resumo de uma página que um diretor possa ler rapidamente antes da reunião. Coloque a
decisão e as próximas etapas primeiro.
- Transforme estas anotações em um e-mail de acompanhamento com as decisões, os responsáveis e os
prazos.
- Crie uma tabela clara que compare os gastos planejados aos reais e destaque qualquer
diferença superior a 10%.

Em trabalhos importantes, peça ao ChatGPT uma verificação final, por exemplo, para confirmar que cada
item de ação tenha um responsável e uma data de entrega ou sinalizar informações que não conseguiu
verificar. Depois, revise o resultado por conta própria antes de usá-lo ou compartilhá-lo.

## Aprimore o resultado com mensagens de acompanhamento

Seu primeiro prompt não precisa ser perfeito. Revise o resultado e depois peça a
alteração específica que deseja.

```text
Make the opening more direct, keep the evidence, and move the recommendation
above the background section.

Você pode adicionar uma fonte que faltou, corrigir o direcionamento, pedir outra opção ou
mudar o nível de detalhe sem começar de novo.

### Direcionar e colocar na fila

Quando o Codex já estiver trabalhando, você poderá enviar outra mensagem sem esperar a
execução atual terminar:

- **Direcionar** adiciona a mensagem à execução atual. Use essa opção para mudar o rumo, acrescentar
  um detalhe que faltou ou compartilhar novas informações.
- **Colocar na fila** salva a mensagem para a próxima execução. Use essa opção para uma mensagem de acompanhamento que deve
  esperar o trabalho atual terminar.

No aplicativo do ChatGPT para desktop, escolha a opção padrão em
[**Configurações \> Geral \> Comportamento de acompanhamento**](/pt-BR/codex/app/settings#general).
As mensagens na fila aparecem acima do campo de mensagem, onde você pode editá-las, reordená-las, enviá-las ou
excluí-las. Essa configuração também mostra o atalho para usar o outro comportamento
em uma mensagem sem alterar a opção padrão.

No Codex CLI, pressione <kbd>Enter</kbd> enquanto o Codex estiver trabalhando para direcionar o
turno atual ou pressione <kbd>Tab</kbd> para colocar a mensagem na fila para o próximo turno. Consulte os
[atalhos interativos](/codex/developer-commands?surface=cli#cli-interactive-shortcuts)
para saber mais.

## Junte todas as partes

Para uma atualização de projeto que usa fontes conectadas, um prompt completo poderia ser
assim:

```text
Prepare a one-page project status update for Monday's leadership meeting. Use
the latest project plan in Drive and relevant decisions and updates from the
project's Slack channel.

Lead with the decisions leadership needs to make and the next steps. Summarize
progress, risks, owners, and due dates. Keep approved dates and budget figures
unchanged. Flag any conflicting or missing information, and don't send or
publish anything.

Before you finish, check that every next step has an owner and due date.

Este prompt abrange **Meta**, **Contexto**, **Resultado** e **Limites** e depois
solicita uma verificação final sem detalhar cada etapa.

## Use o ditado por voz

No aplicativo do ChatGPT para desktop, pressione <kbd>Ctrl+Shift+D</kbd> enquanto o campo de mensagem estiver
visível e comece a falar. O ChatGPT transcreve sua fala no campo de mensagem
para que você possa revisar e editar o texto antes de enviar o prompt.

  
    
  

<a id="threads"></a>
<a id="chats"></a>

## Exemplos de prompts para o Chat

Use o Chat para perguntas, ideias, rascunhos e decisões cotidianas. Comece pelo
resultado desejado e só acrescente detalhes quando isso mudar a resposta.

### Entenda um assunto

```text
Explain how compound interest works for someone who has never invested.
Use one concrete example and define any financial terms you introduce.

### Elabore e refine textos

```text
Draft a friendly email declining this invitation because I will be traveling.
Keep it under 120 words and leave the door open for a future event.

### Compare opções

```text
Compare these two phone plans for one person who travels internationally twice
a year. Show the important differences in a table, then recommend one and explain
the tradeoff.

### Elaborar um plano prático

```text
Plan five weekday dinners that take less than 30 minutes. Avoid peanuts, reuse
ingredients across meals, and finish with one consolidated shopping list.

<a id="prompting-for-work"></a>
<a id="prompting-in-work-mode"></a>

## Criação de prompts para o ChatGPT Work

Use o Chat para perguntas rápidas, pequenas reescritas, geração de ideias e
rascunhos simples. Use o ChatGPT Work para tarefas que utilizam diferentes fontes ou ferramentas, envolvem uma
sequência de etapas, fazem alterações ou produzem uma entrega mais abrangente.

No ChatGPT Work, descreva o resultado de que você precisa, forneça o material de origem, identifique
o público e explique como revisará o trabalho. Peça ao ChatGPT para planejar,
reunir as informações necessárias, criar arquivos e verificá-los antes de concluir a tarefa.

<a id="use-work-efficiently"></a>
<a id="use-work-mode-efficiently"></a>

### Usar o ChatGPT Work com eficiência

O ChatGPT Work é útil para tarefas demoradas ou recorrentes, ou para criar arquivos prontos que você
possa reutilizar. Uma tarefa que usa mais créditos ainda pode valer a pena se economizar
tempo, melhorar a qualidade ou ajudar você a tomar uma decisão importante.

Comece com um único resultado que você possa revisar:

- Inclua apenas fontes relevantes e limite o intervalo de datas quando for apropriado.
- Defina o público, o formato de saída e o tamanho desejado.
- Separe o trabalho obrigatório das melhorias e dos refinamentos opcionais.
- Peça um plano quando a abordagem for importante. Exija sua aprovação antes que o ChatGPT
envie, publique ou altere informações das quais outras pessoas dependem.
- Reduza o escopo ou interrompa a tarefa se ela começar a realizar atividades de que você não precisa mais.

Revise o primeiro resultado, refine as instruções e reutilize o fluxo de trabalho quando
ele funcionar.

### Transformar o material de origem em arquivos prontos

```text
Use the attached quarterly reports to create a leadership brief and a six-slide
presentation.

The audience is the executive team. Lead with the three decisions they need to
make, distinguish reported facts from your analysis, cite each number to its
source file, and check that the brief and slides agree before you finish.

### Pesquisar para embasar uma decisão

```text
Research three customer-support platforms for a 50-person company. Compare
pricing, security, integrations, and migration effort using current sources.
Deliver a recommendation memo with links, assumptions, and the questions we
should answer before signing a contract.

### Coordenar um lançamento

```text
Create a launch plan for the attached product brief. Include the timeline,
owners, dependencies, risks, announcement draft, customer FAQ, and a checklist
for launch day. Flag any missing decisions before producing the final files.

Para trabalhos recorrentes, primeiro refine o prompt em um chat comum. Quando o resultado estiver
confiável, [agende uma tarefa nesse chat](/pt-BR/codex/automations#schedule-a-task-inside-a-chat).
Em vez disso, crie uma tarefa agendada independente quando cada execução agendada precisar iniciar
um novo chat.

<a id="use-editor-context"></a>

## Criação de prompts para o Codex

Use o Codex quando quiser que o ChatGPT trabalhe com código, uma base de código ou ferramentas de desenvolvimento.
Um prompt útil para o Codex descreve o comportamento desejado, indica o código relevante ou as
etapas de reprodução, preserva restrições importantes e informa como verificar a
alteração.

<a id="goal-mode"></a>

Para uma tarefa com várias etapas, insira `/plan` no campo de mensagem do aplicativo quando quiser que o Codex
investigue e proponha uma abordagem antes de fazer alterações. Quando o [modo Meta](/pt-BR/codex/long-running-work)
estiver disponível, use `/goal` após o plano para definir uma meta persistente. Consulte os [comandos de
barra do aplicativo](/codex/reference/slash-commands)
para ver a lista atual de comandos.

### Como ler estes exemplos

Cada fluxo de trabalho inclui:

- **Quando usar** e qual interface do Codex é mais adequada (IDE, CLI ou nuvem).
- **Etapas** com exemplos de prompts do usuário.
- **Observações sobre o contexto**: o que o Codex vê automaticamente e o que você deve anexar.
- **Verificação**: como conferir o resultado.

> **Observação:** A extensão para IDE inclui automaticamente os arquivos abertos como contexto. Na CLI, mencione os caminhos explicitamente ou anexe arquivos usando `/mention` e o preenchimento automático de caminhos com `@`.

O Codex executa comandos locais em um [Sandbox](/pt-BR/codex/sandboxing)
que limita o acesso a arquivos e à rede. Se uma tarefa precisar ultrapassar esse limite,
o Codex segue sua política de aprovação antes de continuar.

### Explicar uma base de código

Use este fluxo quando estiver conhecendo uma base de código, assumindo um serviço ou tentando entender um protocolo, um modelo de dados ou um fluxo de requisições.

#### Fluxo de trabalho da extensão para IDE (mais rápido para exploração local)

1. Abra os arquivos mais relevantes.
2. Selecione o código de interesse (opcional, mas recomendado).
3. Envie um prompt ao Codex:

   ```text
   Explain how the request flows through the selected code.

   Include:
   - a short summary of the responsibilities of each module involved
   - what data is validated and where
   - one or two "gotchas" to watch for when changing this

Verificação:

- Peça um diagrama ou uma lista de verificação que você possa validar:

```text
Summarize the request flow as a numbered list of steps. Then list the files involved.

#### Fluxo de trabalho da CLI (útil quando você quer uma transcrição + comandos do shell)

1. Inicie uma sessão interativa:

   ```bash
   codex

2. Anexe os arquivos (opcional) e envie um prompt:

   ```text
   I need to understand the protocol used by this service. Read @foo.ts @schema.ts and explain the schema and request/response flow. Focus on required vs optional fields and backward compatibility rules.

Observações sobre o contexto:

- Você pode usar `@` no campo de mensagem para inserir caminhos de arquivos do workspace ou `/mention` para anexar um arquivo específico.

### Corrigir um bug

Use este fluxo quando houver um comportamento incorreto que você consiga reproduzir localmente.

#### Fluxo de trabalho da CLI (ciclo rápido de reprodução e verificação)

1. Inicie o Codex na raiz do repositório:

   ```bash
   codex

2. Forneça ao Codex um procedimento de reprodução e indique os arquivos suspeitos:

   ```text
   Bug: Clicking "Save" on the settings screen sometimes shows "Saved" but doesn't persist the change.

   Repro:
   1) Start the app: npm run dev
   2) Go to /settings
   3) Toggle "Enable alerts"
   4) Click Save
   5) Refresh the page: the toggle resets

   Constraints:
   - Do not change the API shape.
   - Keep the fix minimal and add a regression test if feasible.

   Start by reproducing the bug locally, then propose a patch and run checks.

Observações sobre o contexto:

- O que você fornece: as etapas de reprodução e as restrições (elas são mais importantes do que uma descrição geral).
- O que o Codex fornece: a saída dos comandos, os pontos de chamada identificados e quaisquer rastreamentos de pilha que ele gerar.

Verificação:

- O Codex deve executar novamente as etapas de reprodução após a correção.
- Se você tiver um pipeline padrão de verificações, peça ao Codex para executá-lo:

```text
After the fix, run lint + the smallest relevant test suite. Report the commands and results.

#### Fluxo de trabalho da extensão para IDE

1. Abra o arquivo em que você acha que está o bug e também o código que faz a chamada mais próxima.
2. Envie um prompt ao Codex:

   ```text
   Find the bug causing "Saved" to show without persisting changes. After proposing the fix, tell me how to verify it in the UI.

### Escrever um teste

Use este fluxo quando quiser definir exatamente o escopo a ser testado.

#### Fluxo de trabalho da extensão para IDE (baseado em seleção)

1. Abra o arquivo que contém a função.
2. Selecione as linhas que definem a função. Na paleta de comandos, escolha "Add to Codex Thread" para adicionar essas linhas ao contexto.
3. Envie um prompt ao Codex:

   ```text
   Write a unit test for this function. Follow conventions used in other tests.

Observações sobre o contexto:

- O que o comando "Add to Codex Thread" fornece: as linhas selecionadas (este é o escopo de "número de linha"), além dos arquivos abertos.

#### Fluxo de trabalho da CLI (caminho + intervalo de linhas descritos no prompt)

1. Inicie o Codex:

   ```bash
   codex

2. Envie um prompt com o nome de uma função:

   ```text
   Add a test for the invert_list function in @transform.ts. Cover the happy path plus edge cases.

### Criar um protótipo a partir de uma captura de tela

Use este fluxo quando quiser transformar um mockup de design, uma captura de tela ou uma referência de interface em um protótipo funcional.

#### Fluxo de trabalho na CLI (imagem + prompt)

1. Salve a captura de tela localmente (por exemplo, `./specs/ui.png`).
2. Execute o Codex:

   ```bash
   codex

3. Arraste o arquivo de imagem para o terminal para anexá-lo ao prompt.

4. Depois, informe as restrições e a estrutura:

   ```text
   Create a new dashboard based on this image.

   Constraints:
   - Use react, vite, and tailwind. Write the code in typescript.
   - Match spacing, typography, and layout as closely as possible.

   Outputs:
   - A new route/page that renders the UI
   - Any small components needed
   - README.md with instructions to run it locally

Observações sobre o contexto:

- A imagem fornece os requisitos visuais, mas você ainda precisa especificar as restrições de implementação (framework, roteamento e estilo dos componentes).
- Descreva em texto os comportamentos que a imagem não mostra, como estados ao passar o cursor, regras de validação ou interações com o teclado.

Verificação:

- Peça ao Codex para executar o servidor de desenvolvimento (se permitido) e informar exatamente onde verificar o resultado:

```text
Start the dev server and tell me the local URL/route to view the prototype.

#### Fluxo de trabalho na extensão para IDE (imagem + arquivos existentes)

1. Anexe a imagem ao chat do Codex (arraste e solte ou cole).
2. Envie um prompt ao Codex:

   ```text
   Create a new settings page. Use the attached screenshot as the target UI.
   Follow design and visual patterns from other files in this project.

### Iterar na interface com atualizações em tempo real

Use este fluxo quando quiser um ciclo rápido de “design → ajuste → atualização → ajuste” enquanto o Codex edita o código.

#### Fluxo de trabalho na CLI (executar o Vite e depois iterar com prompts curtos)

1. Inicie o Codex:

   ```bash
   codex

2. Inicie o servidor de desenvolvimento em uma janela separada do terminal:

   ```bash
   npm run dev

3. Peça ao Codex para fazer alterações:

   ```text
   Propose 2-3 styling improvements for the landing page.

4. Escolha uma direção e itere usando prompts curtos e específicos:

   ```text
   Go with option 2.

   Change only the header:
   - make the typography more editorial
   - increase whitespace
   - ensure it still looks good on mobile

5. Repita com solicitações pontuais:

   ```text
   Next iteration: reduce visual noise.
   Keep the layout, but simplify colors and remove any redundant borders.

Verificação:

- Confira as alterações no navegador à medida que o Codex atualiza o código.
- Faça commit das alterações que quiser manter e reverta as demais.
- Se você reverter ou modificar uma edição, avise o Codex para que ele não a sobrescreva quando processar o próximo prompt.

### Delegar a refatoração para a nuvem

Use este fluxo quando quiser elaborar uma abordagem com o contexto local e depois delegar a implementação demorada a um chat na nuvem que possa ser executado em paralelo.

#### Planejamento local (IDE)

1. Garanta que seu trabalho atual esteja registrado em um commit ou, pelo menos, salvo no stash, para que você possa comparar as alterações com clareza.
2. Peça ao Codex para criar um plano de refatoração. Se a habilidade `$plan` estiver disponível, invoque-a explicitamente:

   ```text
   $plan

   We need to refactor the auth subsystem to:
   - split responsibilities (token parsing vs session loading vs permissions)
   - reduce circular imports
   - improve testability

   Constraints:
   - No user-visible behavior changes
   - Keep public APIs stable
   - Include a step-by-step migration plan

3. Revise o plano e negocie as alterações:

   ```text
   Revise the plan to:
   - specify exactly which files move in each milestone
   - include a rollback strategy

Observações sobre o contexto:

- O planejamento funciona melhor quando o Codex pode analisar o código atual localmente (pontos de entrada, limites dos módulos e indícios sobre o grafo de dependências).

#### Delegação para a nuvem (IDE → Nuvem)

1. Se ainda não tiver feito isso, configure um [ambiente de nuvem do Codex](/pt-BR/codex/environments/cloud-environment).
2. Clique no ícone de nuvem abaixo do campo de mensagem e selecione seu ambiente de nuvem.
3. Ao enviar o próximo prompt, o Codex cria um novo chat na nuvem e transfere para ele o contexto do chat atual (incluindo o plano e eventuais alterações locais no código-fonte).

   ```text
   Implement Milestone 1 from the plan.

4. Revise o diff na nuvem e itere, se necessário.

5. Crie uma PR diretamente na nuvem ou faça pull das alterações para o ambiente local a fim de testá-las e concluir o trabalho.

6. Faça novas iterações nos demais marcos do plano.

As tarefas delegadas à nuvem são executadas em ambientes isolados. O acesso à internet fica
desativado durante a fase do agente, a menos que você o habilite no ambiente. Saiba mais
sobre o [acesso à internet na nuvem](/pt-BR/codex/cloud/internet-access).

### Fazer uma revisão de código local

Use este fluxo quando quiser uma segunda opinião antes de fazer commit ou criar uma PR.

#### Fluxo de trabalho na CLI (revisão da sua árvore de trabalho)

1. Inicie o Codex:

   ```bash
   codex

2. Execute o comando de revisão:

   ```text
   /review

3. Opcional: forneça instruções personalizadas sobre o foco da revisão:

   ```text
   /review Focus on edge cases and security issues

Verificação:

- Aplique as correções com base no feedback da revisão e execute `/review` novamente para confirmar que você resolveu os problemas.

### Revisar um pull request do GitHub

Use este fluxo quando quiser receber feedback da revisão sem fazer pull da branch para o ambiente local.

Antes de usar esse recurso, ative a **Revisão de código** do Codex no seu repositório. Consulte [Revisão de código](/pt-BR/codex/third-party/github).

#### Fluxo de trabalho no GitHub (orientado por comentários)

1. Abra o pull request no GitHub.
2. Deixe um comentário que mencione o Codex e indique explicitamente as áreas de foco:

   ```text
   @codex review

3. Opcional: forneça instruções mais detalhadas.

   ```text
   @codex review for security vulnerabilities and security concerns

### Atualizar a documentação

Use este fluxo quando precisar fazer uma alteração clara e precisa na documentação.

#### Fluxo de trabalho na IDE ou na CLI (edições locais + validação local)

1. Identifique os arquivos de documentação que precisam ser alterados e abra-os (IDE) ou use `@` para mencioná-los (IDE ou CLI).
2. Envie um prompt ao Codex com o escopo e os requisitos de validação:

   ```text
   Update the "advanced features" documentation to provide authentication troubleshooting guidance. Verify that all links are valid.

3. Depois que o Codex preparar as alterações, revise a documentação e faça os ajustes necessários.

Verificação:

- Leia a página renderizada.

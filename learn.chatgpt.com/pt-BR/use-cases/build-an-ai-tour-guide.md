<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/build-an-ai-tour-guide -->

## Introdução

Alguns fluxos de trabalho são mais fáceis de aprender quando alguém mostra onde ir e o que selecionar. Use o Codex para criar um tutorial que oriente os usuários pelo seu aplicativo web enquanto eles executam as ações por conta própria.

Com ferramentas WebMCP para os controles, o estado e a documentação do seu aplicativo, o Codex pode escolher a próxima instrução com base no que o usuário vê. Quem ainda não conectou um serviço precisa de uma primeira etapa diferente de quem já concluiu a configuração.

## Como usar

1. Abra o repositório do seu aplicativo no Codex e escolha um fluxo de trabalho para orientar, como conectar um serviço ou adicionar uma pasta.
2. Forneça a documentação relevante e descreva os estados iniciais que o tutorial deve contemplar.
3. Execute o prompt inicial desta página para adicionar elementos-alvo do tutorial, ferramentas de estado da interface e acesso às instruções do aplicativo.
4. Teste o fluxo em um ambiente de navegador em que o Codex possa chamar as ferramentas WebMCP do seu aplicativo. Peça ao Codex que oriente você e depois conclua cada etapa por conta própria.

Mantenha o escopo do primeiro tutorial restrito. Verifique se ele consegue orientar um usuário desde a configuração até a conclusão antes de adicionar mais fluxos de trabalho.

## Exemplo: adicione uma pasta do Google Drive no Runme

No <a href="https://web.runme.dev" target="_blank" rel="noopener noreferrer">Runme</a>, os usuários editam notebooks e usam um explorador de arquivos para adicionar pastas do Google Drive e navegar pelos arquivos. O tutorial ajuda novos usuários a encontrar esses controles e aprender o fluxo.

Para saber mais sobre o Runme, leia <a href="https://developers.openai.com/blog/automating-repetitive-work-at-openai-with-codex" target="_blank" rel="noopener noreferrer">Automação de tarefas repetitivas na OpenAI com o Codex</a>.

Veja o Codex destacar os controles do Runme e explicar para que servem. As capturas de tela abaixo mostram um tutorial separado, voltado à tarefa de adicionar uma pasta do Google Drive.

<figure class="not-prose my-4">
  <video
    class="w-full rounded-lg border border-default"
    controls
    muted
    playsinline
    preload="metadata"
    poster="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/tour-demo-poster.webp"
    aria-label="Codex demonstrates an AI tour of Runme's controls"
  >
    <source
      src="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/runme-ai-tour-demo.webm"
      type="video/webm"
    />
    Seu navegador não oferece suporte à reprodução deste vídeo.
  </video>
</figure>

O tutorial do Google Drive começa com um pedido:

### Conecte o Google Drive

O Codex verifica se o Google Drive está conectado. Se não estiver, o Codex destaca **Conectar o Google Drive** e pede ao usuário que selecione essa opção e conclua a conexão.

![O Codex destaca a opção Conectar o Google Drive no Runme e explica como começar.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/connect-google-drive.webp)

### Abra o explorador de arquivos

Após a conclusão da conexão, o Codex orienta o usuário até o explorador de arquivos. A próxima instrução acompanha o estado atualizado do aplicativo.

![O Codex destaca o controle que abre o explorador de arquivos do Runme.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/open-file-explorer.webp)

### Adicione a pasta

Depois que o usuário expande a barra de ferramentas, o Codex destaca o controle para adicionar uma pasta do Google Drive. O usuário mantém o controle da interação e aprende onde encontrar esse controle na próxima vez.

![O Codex destaca o controle para adicionar uma pasta do Google Drive no Runme.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/add-google-drive-folder.webp)

## Dê ao Codex o contexto para orientar os usuários

A implementação do Runme fornece três tipos de contexto: elementos-alvo do tutorial, estado do aplicativo e documentação. Os nomes das ferramentas abaixo são os usados pelo Runme; adapte essas mesmas funções ao seu aplicativo.

### Permita que os controles sejam encontrados

Atribua valores estáveis e semânticos de `data-tour-id` aos elementos-alvo do tutorial, com um rótulo e uma descrição para cada um. O Runme expõe esses controles por meio de três ferramentas WebMCP:

- `listTargets` lista os elementos-alvo registrados, seus IDs, rótulos e descrições.
- `showTourStep({ target, title?, message, placement? })` destaca um elemento-alvo e exibe uma explicação.
- `dismiss` remove o destaque.

Isso permite ao Codex identificar um controle e explicar sua função sem executar a ação pelo usuário.

### Leia o estado e aguarde o usuário

O Runme mantém o estado relacionado ao tutorial fora do React e o expõe por meio de um controlador. Sua ferramenta `getUiSnapshot` fornece o estado atual da interface, incluindo o status de autenticação. `waitForUiChange(...)` permite que o Codex aguarde uma mudança, como quando o usuário seleciona o controle destacado.

Peça ao Codex que leia o estado novamente após cada interação. O avanço do tutorial deve depender do que aconteceu no aplicativo, não de o Codex já ter exibido uma instrução.

### Mantenha as instruções junto ao aplicativo

O Runme inclui documentação em Markdown no aplicativo e a disponibiliza por meio de WebMCP:

- `readInstructionsForAIAgents` explica como o Codex deve interagir com o aplicativo e suas ferramentas.
- `listDocumentation()` lista as páginas disponíveis e suas descrições.
- `getDocumentation({ name })` retorna uma página selecionada em Markdown.

As instruções e as ferramentas do tutorial podem ser distribuídas com o aplicativo, sem um plug-in separado do Codex para o tutorial.

## Revise o tutorial

Teste o mesmo pedido a partir de diferentes estados iniciais. Verifique se o tutorial pula as configurações já concluídas, aguarda o usuário e atualiza a orientação quando a interface muda.

Teste também uma etapa cancelada e um controle que ainda não esteja visível. O Codex deve explicar o que falta ou escolher uma próxima etapa válida. Ele não deve afirmar que uma ação foi concluída com sucesso só porque destacou um botão.

Mantenha a autenticação, as verificações de permissão e as ações do usuário no fluxo existente do aplicativo. O tutorial deve ajudar os usuários a entender a interface sem contornar esses controles.

## Sugestões para continuar

Quando o primeiro fluxo estiver funcionando, continue no mesmo chat:

- "Teste esta visita guiada quando o Google Drive já estiver conectado e o explorador de arquivos estiver fechado."
- "Trate o caso em que um usuário cancela uma etapa e depois pede para continuar a visita guiada."
- "Adicione uma visita guiada para \[next workflow\], reutilizando os alvos e as ferramentas de estado existentes."

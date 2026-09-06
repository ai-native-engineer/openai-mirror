<!-- source: https://learn.chatgpt.com/pt-BR/docs/appshots -->

As Capturas do app permitem enviar a janela do aplicativo em primeiro plano para um chat no ChatGPT. Use-as quando
você estiver trabalhando em outro aplicativo no computador e quiser fornecer ao
ChatGPT seu contexto atual para receber ajuda com a tarefa.

  As Capturas do app estão disponíveis no aplicativo para desktop do ChatGPT no macOS. Pressione as duas teclas Command
ou o atalho personalizado das Capturas do app para fazer uma captura.

## O que as Capturas do app registram

Uma captura do app registra apenas a janela em primeiro plano. Ela pode incluir:

- Uma imagem da janela visível.
- O texto disponível nessa janela, incluindo o texto visível e o texto que o aplicativo disponibiliza
fora da área visível de rolagem.

Depois que você adiciona uma captura do app a um chat, ela se comporta como um anexo. O ChatGPT
armazena as capturas do app localmente no arquivo da sessão, assim como os arquivos ou as imagens que você anexa
manualmente.

## Quando usar as Capturas do app

Use as Capturas do app quando o ChatGPT precisar do contexto de um aplicativo para Mac antes de agir.

Exemplos:

- Compartilhe uma página de referência de API e peça ao ChatGPT que escreva um script que use essa API.
- Compartilhe uma tela de e-mail ou de calendário e peça ao ChatGPT que prepare a próxima etapa.
- Compartilhe um editor de imagens, um design ou uma janela de pré-visualização e peça ao ChatGPT que revise os
recursos ou o código relacionados.
- Compartilhe um erro, um painel de configurações ou um estado do aplicativo que seja mais fácil mostrar do que
descrever.

## Fazer uma captura do app

1. Coloque em primeiro plano a janela do aplicativo que você quer compartilhar.
2. Pressione as duas teclas Command ou o atalho personalizado que você configurou nas
configurações do ChatGPT.
3. Conceda as permissões do macOS se o ChatGPT solicitar.
4. Peça ao ChatGPT que execute uma tarefa usando a captura do app.

  

Por padrão, o ChatGPT inicia um novo chat com a captura do app. Se você interagiu com um
chat nos últimos 60 segundos, o ChatGPT adiciona a captura do app a esse chat
recente. As capturas do app feitas em sequência são adicionadas ao mesmo chat.

Você pode alterar o atalho das Capturas do app nas configurações do aplicativo.

## Permissões e segurança

O ChatGPT pode solicitar permissões antes de fazer capturas do app:

- **Gravação de Tela e Áudio do Sistema** permite que o ChatGPT capture uma imagem da
  janela em primeiro plano.
- **Acessibilidade** permite que o ChatGPT leia o texto disponível na janela em primeiro plano.

Ao fazer uma captura do app, você compartilha com o ChatGPT a imagem capturada e o texto disponível.
Evite fazer capturas do app que contenham conteúdo sensível, a menos que a tarefa exija esse
conteúdo.

Confira as capturas do app com o mesmo cuidado que teria ao compartilhar capturas de tela e documentos
com o ChatGPT.

## Limites e solução de problemas

As Capturas do app estão disponíveis no aplicativo para desktop do ChatGPT no macOS. Se você retomar na CLI um chat
que já contém uma captura do app, o anexo fará parte do histórico do chat,
mas a CLI não poderá criar uma nova captura do app.

Em alguns aplicativos e sites, incluindo Google Docs, Gmail, Google Sheets e
Google Slides, o ChatGPT pode receber apenas uma captura de tela do conteúdo visível e talvez não receba
o documento completo nem o texto fora da área visível. No ChatGPT Work ou no Codex, o ChatGPT pode usar um
plug-in compatível instalado para acessar o conteúdo relevante do aplicativo e ajudar você com sua
solicitação.

Se as Capturas do app não funcionarem:

1. Abra **Ajustes do Sistema \> Privacidade e Segurança**.
2. Verifique se o Uso do computador do Codex
   está ativado em **Gravação de Tela e Áudio do Sistema** e **Acessibilidade**.
3. Reinicie o aplicativo e tente novamente.

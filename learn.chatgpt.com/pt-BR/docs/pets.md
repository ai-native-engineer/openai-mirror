<!-- source: https://learn.chatgpt.com/pt-BR/docs/pets -->

Os mascotes são companheiros animados opcionais para acompanhar o trabalho. O local em que um mascote aparece
e o que ele mostra dependem da interface usada. Escolher um mascote muda sua
aparência, não a forma como o ChatGPT conclui tarefas.

<div class="flow-root">
  <div class="w-full md:float-right md:ml-6 md:w-64 xl:w-72">
    
  </div>

## Usar um mascote flutuante

No aplicativo do ChatGPT para desktop, um mascote pode flutuar sobre janelas de outros aplicativos e ajudar
você a acompanhar a atividade nos seus chats.

### Escolher e acordar um mascote

1. Abra o menu do perfil na parte inferior do aplicativo e selecione **Mascotes**. Você também pode
   abrir [**Configurações**](codex://settings) e acessar **Mascotes**.
2. Escolha um mascote predefinido ou personalizado.
3. Digite `/pet` ou abra o menu de comandos e selecione **Acordar mascote**.

Selecione **Guardar mascote** em **Configurações \> Mascotes** ou no menu de comandos, ou digite
`/pet` novamente para ocultar o mascote. Sua seleção e a posição do mascote são mantidas
quando você reabre o aplicativo.

Ao selecionar um mascote personalizado, ele também aparece na visualização **Perfil**.

### Entender o status do mascote

| Status          | Significado                                                  |
| --------------- | -------------------------------------------------------- |
| **Em execução**     | Um chat está executando uma tarefa.                              |
| **Ação necessária** | Um chat precisa da sua aprovação, resposta ou de outra decisão. |
| **Pronto**       | Um chat concluiu uma tarefa e tem atividade não lida.            |
| **Bloqueado**     | Um chat falhou ou encontrou um erro do sistema.             |

Quando há atividade em mais de um chat, o mascote prioriza os chats que precisam de
uma ação, depois os bloqueados, os prontos e os que estão em execução. Abra a bandeja de atividades para
escolher um chat.

Selecione o mascote para voltar ao ChatGPT ou selecione uma atividade para abrir o chat correspondente.
A bandeja de atividades é separada das [notificações do
sistema](/pt-BR/codex/notifications?surface=app).

### Acompanhar o Uso do computador

No macOS, a janela de imagem em imagem do [Uso do computador](/pt-BR/codex/computer-use) pode ser
acoplada a um mascote acordado. Mova o mascote e a janela o acompanhará.

### Criar um mascote personalizado

1. Abra **Configurações \> Mascotes** e selecione **Criar seu próprio mascote**.
2. O aplicativo instala a habilidade `hatch-pet` incluída no pacote, recarrega as habilidades e abre um
   novo chat.
3. Descreva o mascote que você quer e envie o prompt.
4. Quando a tarefa terminar, volte para **Configurações \> Mascotes**, selecione **Atualizar**
   e escolha seu novo mascote.

Os mascotes personalizados criados no aplicativo para desktop ficam armazenados localmente no computador.
Eles não são sincronizados automaticamente com o ChatGPT na Web.

### Reduzir a animação

Os mascotes respeitam a configuração de redução de movimento do sistema operacional. Quando essa configuração
está ativada, o mascote usa um quadro estático em vez de uma animação de sprites.

## Escolher um mascote na Web

Se o recurso Mascotes estiver disponível para sua conta e seu workspace, abra **Configurações \>
Personalização \> Mascote \> Selecionar mascote**. Escolha um mascote predefinido ou selecione
**Padrão** para usar o ChatGPT sem mascote.

Um mascote da Web aparece nos chats compatíveis do ChatGPT Work. Ele não oferece a
sobreposição flutuante, a bandeja de atividades nem o comando `/pet` do aplicativo para desktop.

### Enviar um mascote personalizado

Selecione **Enviar mascote** para adicionar uma folha de sprites personalizada. O arquivo deve ser um
arquivo PNG ou WebP transparente, ter exatamente 1536 × 1872 pixels e no máximo 20 MiB.
Na mesma configuração, você pode editar, baixar, atualizar ou excluir os mascotes enviados.

## Escolher um mascote para o terminal

Em uma sessão interativa da CLI do Codex:

- Digite `/pets` ou `/pet` para abrir o seletor de mascotes.
- Digite `/pets <name>` para escolher diretamente um mascote.
- Digite `/pets off` para desativar os mascotes do terminal.

O seletor inclui mascotes predefinidos e mascotes personalizados compatíveis instalados no seu
computador. Um mascote do terminal mostra a atividade da sessão atual da CLI. Ele usa os
status **Em execução**, **Ação necessária**, **Pronto** e **Bloqueado**, mas não
oferece a bandeja de atividades de vários chats do aplicativo para desktop.

Os mascotes do terminal exigem o iTerm2 3.6 ou posterior, ou um terminal com suporte a gráficos Kitty ou
a Sixel. Eles não estão disponíveis no tmux nem no Zellij.

## Mascotes na extensão para IDE

A extensão do Codex para IDE não oferece um seletor de mascotes nem uma sobreposição flutuante do mascote.
Use o aplicativo do ChatGPT para desktop ou a CLI do Codex quando quiser usar seu próprio mascote.

</div>

## Documentação relacionada

- [Notificações](/pt-BR/codex/notifications)
- [Trabalho de longa duração](/pt-BR/codex/long-running-work)
- [Configurações do aplicativo do ChatGPT para desktop](/codex/reference/settings#pets)

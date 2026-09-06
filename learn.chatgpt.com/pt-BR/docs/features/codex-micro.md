<!-- source: https://learn.chatgpt.com/pt-BR/docs/features/codex-micro -->

<div class="grid gap-6 lg:grid-cols-2 lg:items-start lg:gap-10">
  <div class="min-w-0 [&_p]:!mt-0">

O Codex Micro é uma colaboração de edição limitada entre Codex e Work Louder. Ele
funciona com o aplicativo para desktop do ChatGPT, oferecendo uma forma rápida de conferir os chats,
alternar entre eles, usar a entrada por voz e acionar ações ou habilidades comuns sem
tirar as mãos do teclado.

  </div>
  <div class="min-w-0">
    
      
    
  </div>
</div>

## Configurar o Codex Micro

1. Abra o aplicativo para desktop do ChatGPT.
2. Pressione uma vez o botão traseiro para ligar o Codex Micro.
3. Conecte-o usando um cabo USB-C ou [emparelhe-o por Bluetooth](#pair-with-bluetooth),
   depois siga as instruções de configuração exibidas quando o ChatGPT detectá-lo.
4. No macOS, autorize o **Monitoramento de Entrada** quando solicitado para que o ChatGPT responda aos
   pressionamentos de teclas.
5. Abra **Configurações \> Codex Micro** para escolher o que as teclas de agente acompanham ou
   acionam, personalizar as teclas de comando, a alavanca analógica e o botão giratório e ajustar
   a iluminação e os controles de voz.

Por padrão, mantenha o botão giratório pressionado por alguns instantes para abrir essas configurações. Você
também pode selecionar o ícone do Micro ao lado do nome da sua conta, na parte inferior do ChatGPT.
Uma atribuição personalizada do botão giratório pode substituir o atalho de pressionar e segurar.

As configurações do dispositivo continuam disponíveis depois que o ChatGPT detecta um Micro compatível
pela primeira vez. O Work Louder Input não é necessário para a integração com o ChatGPT.
Use-o para personalizar controles de outros aplicativos ou configurar mais camadas.

## Emparelhar por Bluetooth

O Codex Micro oferece três canais Bluetooth.

1. Pressione uma vez o botão traseiro para ligar o Micro.
2. Mantenha pressionado por três segundos o controle sensível ao toque na borda inferior esquerda.
A iluminação sob o Micro fica azul quando o modo Bluetooth está ativo.
3. Toque no controle sensível ao toque para escolher o canal Bluetooth 1, 2 ou 3. Uma luz de canal piscando
rapidamente indica que o Micro está pronto para o emparelhamento.
4. Abra as configurações de Bluetooth do computador e conecte-se ao Micro quando ele
aparecer.
5. Aguarde até que a luz do canal fique acesa sem piscar, indicando que o emparelhamento foi concluído.

O seletor de conexão fecha após cinco segundos sem interação. Para mudar para
outro canal emparelhado, abra o seletor novamente, escolha o canal e aguarde
até que ele feche. Para emparelhar esse canal novamente, mantenha pressionado o controle sensível ao toque
por três segundos, até que a luz comece a piscar.

Para usar USB-C, abra o seletor de conexão e toque no controle sensível ao toque
até que a iluminação sob o Micro fique branca. Conectar um cabo USB-C enquanto
o Micro ainda está no modo Bluetooth carrega a bateria, mas não alterna o Micro para a
conexão com fio.

Para ver os diagramas de hardware, consulte o [guia de configuração
do Codex Micro da Work Louder](https://worklouder.cc/openai-micro-setup).

<a id="read-and-switch-tasks-with-agent-keys"></a>

## Ler e alternar entre chats com as teclas de agente

Cada uma das seis teclas de agente foscas pode acompanhar um chat e acender para mostrar o
status atual do chat. Pressione uma tecla de agente uma vez para mudar para esse chat sem colocar o
ChatGPT em primeiro plano. Pressione-a duas vezes em até 350 milissegundos para mudar de chat e
colocar a janela do ChatGPT em primeiro plano. Para dar foco ao ChatGPT já no primeiro pressionamento, ative
**Dar foco ao ChatGPT com um único toque** nas configurações do dispositivo.

| Luz | Status           | Significado                                   |
| ----- | ---------------- | ----------------------------------------- |
| Branca | Inativo             | O chat está inativo.                         |
| Azul  | Pensando         | O ChatGPT está trabalhando.                       |
| Verde | Concluído         | O chat foi concluído e há uma atualização não lida. |
| Âmbar | Requer interação   | O ChatGPT precisa da sua aprovação ou resposta.  |
| Vermelha   | Erro            | Algo deu errado.                     |
| Apagada   | Nenhum chat atribuído | A tecla não acompanha nenhum chat.            |

A tecla do chat selecionado pulsa com a cor correspondente ao status.

Por padrão, as teclas acompanham seus seis chats atualizados mais recentemente, estejam
eles fixados ou não. Nas configurações do dispositivo, altere **Teclas de agente** para usar uma
organização diferente:

- **Chats mais recentes**: acompanhe os seis chats atualizados mais recentemente, estejam fixados ou
  não.
- **Chats fixados**: acompanhe os seis primeiros chats de **Fixados**.
- **Chats prioritários**: coloque primeiro os chats que aguardam interação, os chats não lidos e os
  chats ativos.
- **Atribuições personalizadas**: atribua um chat, atalho, ação de tecla física ou habilidade ativada
  a cada tecla de agente. Pressione uma tecla de agente sem atribuição para abrir um novo chat.
  Quando você iniciar o chat, o ChatGPT o atribuirá a essa tecla.

As cores de status permanecem as mesmas nas teclas que acompanham chats. Com **Atribuições
personalizadas**, uma tecla de agente pode acionar uma ação em vez de acompanhar um chat.

## Usar e personalizar as teclas de comando

O layout padrão do Codex Micro inclui seis ações:

<div class="grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-start">
  <div class="min-w-0 [&_table]:!mt-0 [&_td:first-child]:!px-2 [&_th:first-child]:!px-2 md:order-2">

|                            Tecla                            | Ação padrão                           |
| :-------------------------------------------------------: | ---------------------------------------- |
|     | Ative ou desative o modo Fast.                |
|  | Aprove a solicitação atual.             |
|   | Recuse a solicitação atual.             |
|    | Continue o chat atual em um novo chat. |
|       | Inicie o modo Pressionar para falar.                      |
|   | Envie a mensagem no Editor.        |

  </div>
  <div class="min-w-0 md:order-1">

A tecla Mic usa o microfone do seu computador. O Codex Micro não tem
microfone próprio. Por padrão, usa **Pressionar para falar**: mantenha a tecla pressionada enquanto
fala e solte-a para parar. Para gravar sem usar as mãos, pressione-a duas vezes
em até 350 milissegundos para manter a gravação. Pressione-a novamente para parar.

Uma luz verde-água percorre o teclado enquanto você grava. Ela muda para uma
luz branca em movimento enquanto o ChatGPT processa sua fala e fica branca e fixa
quando o prompt está pronto. Pressione a tecla Codex para enviá-lo.

Se **Chat por voz** estiver disponível em **Tecla do microfone**, selecione essa opção para usar a
tecla Mic para iniciar um Chat por voz ou ligar ou desligar seu microfone; mantenha-a pressionada para
encerrar o chat. Ative **Usar teclas de microfone separadas** para mapear de forma independente os dois interruptores
sob a tecla Mic mais larga.

Nas configurações do dispositivo, selecione uma Tecla de comando na prévia de **Layout** e
escolha a capa e a ação da tecla. Você pode abrir o navegador ou o Terminal, gerenciar
chats, revisar alterações, executar ações do Git e de pull request, anexar arquivos ou fotos,
abrir plug-ins ou tarefas agendadas, alterar o esforço de raciocínio, executar uma habilidade habilitada
ou atribuir outro atalho. Se escolher uma capa de tecla que já esteja em uso
em outro lugar, o ChatGPT troca as duas, em vez de usar a mesma capa duas vezes.

Depois de remapear uma tecla, troque a capa física para que ela corresponda à nova ação.
Selecione **Redefinir layout** para restaurar as atribuições padrão das Teclas de comando e do controle analógico
sem alterar o modo das Teclas de agente nem as atribuições personalizadas de chats.

  </div>
</div>

## Use o controle analógico e o botão giratório

<div class="grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-start">
  <div class="min-w-0">

O controle analógico se move livremente em qualquer direção. Quando você o afasta o suficiente
do centro, o ChatGPT converte o movimento em uma das quatro ações
direcionais. O Codex Micro começa com os mapeamentos mostrados aqui.

Nas configurações do dispositivo, escolha um comando disponível no aplicativo do ChatGPT para desktop ou uma habilidade habilitada para cada
direção.

  </div>
  <div class="min-w-0 [&_table]:!mt-0">

| Direção | Ação padrão             |
| --------- | -------------------------- |
| Para cima        | Ative ou desative o Modo planejamento.  |
| Para a direita     | Avance no histórico do aplicativo. |
| Para baixo      | Mostre ou oculte a barra lateral.  |
| Para a esquerda      | Volte no histórico do aplicativo.    |

  </div>
</div>

Por padrão, o botão giratório usa **Navegação no Editor**. Gire-o para percorrer
os controles e as opções do Editor e pressione-o para abrir ou selecionar o controle
em foco. Quando um controle ou menu do Editor está aberto, a Tecla de agente que fica imediatamente à
direita do botão giratório acende em vermelho. Pressione essa tecla para cancelar.

Escolha um dos quatro modos do botão giratório nas configurações do dispositivo:

| Modo                       | Comportamento                                                                       |
| -------------------------- | ------------------------------------------------------------------------------ |
| **Navegação no Editor**    | Percorra os controles do Editor e selecione o controle em foco.                 |
| **Somente raciocínio**         | Ajuste o esforço de raciocínio e abra o controle deslizante correspondente ou as opções avançadas.               |
| **Rolagem da conversa** | Role o chat ativo; pressione o botão giratório para ir à mensagem mais recente.          |
| **Atribuições personalizadas**     | Atribua uma ação ou habilidade a cada gesto: girar para a esquerda, girar para a direita, pressionar e manter pressionado. |

Um pressionamento longo no botão giratório abre as configurações do dispositivo em todos os modos, exceto
**Atribuições personalizadas**, em que executa a ação atribuída a esse gesto.

## Ajustar a iluminação

{/* vale Microsoft.Auto = NO */}

Nas configurações do dispositivo, ajuste o **Brilho** e escolha um intervalo de **Escurecimento automático**
entre 30 segundos e uma hora ou desative o escurecimento automático. As luzes
voltam a acender quando você usa o Micro ou quando uma Tecla de agente muda de status. Por padrão,
as luzes apagam após três minutos.

{/* vale Microsoft.Auto = YES */}

Quando o Micro informa o status da bateria, você pode vê-lo nas configurações do dispositivo
e ao lado do ícone do Micro na barra lateral.

## Adicionar mais camadas

O ChatGPT usa a camada 1. Use o [Work Louder
Input](https://worklouder.cc/micro-setup) para configurar até cinco camadas adicionais
com atalhos e ações para outros aplicativos.

## Solucionar problemas do Codex Micro

### Corrigir o Monitoramento de Entrada no macOS

Se as configurações do dispositivo mostrarem que o Monitoramento de Entrada não foi configurado, selecione **Abrir
Ajustes do Sistema** e siga estas etapas:

1. Abra **Ajustes do Sistema \> Privacidade e Segurança \> Monitoramento de Entrada**.
2. Ative o acesso para o ChatGPT se ele já estiver na lista. Se não estiver, arraste
**ChatGPT** da pasta Aplicativos para a lista ou selecione **Adicionar (+)** e escolha
**ChatGPT**.
3. Encerre e reabra o ChatGPT. Em seguida, confirme se ele detecta o Micro na camada 1.

Para saber mais sobre essa permissão do macOS, consulte o [guia da Apple sobre
Monitoramento de Entrada](https://support.apple.com/guide/mac-help/mchl4cedafb6/mac).

### Corrigir interferências na conexão

O ChatGPT faz novas tentativas automaticamente quando detecta um Micro, mas não consegue se conectar ou perde
a comunicação. Se o problema continuar, reconecte o Micro e verifique se
algum utilitário de teclado ou ferramenta de segurança bloqueia o acesso a ele.

{/* vale Vale.Spelling = NO */}

No macOS, a Work Louder informa que o Karabiner e o Logitech Options+ podem interferir
na comunicação com o Micro quando esses aplicativos têm a permissão de Monitoramento de Entrada. Para
testar se há interferência, encerre o utilitário de teclado ou desative temporariamente o acesso dele ao
Monitoramento de Entrada e reconecte o Micro. Se a sua organização gerencia
o computador, peça ao administrador de TI para verificar as regras do dispositivo.

{/* vale Vale.Spelling = YES */}

### Obter mais ajuda da Work Louder

Para obter ajuda com Bluetooth, cabos, alimentação ou redefinição do teclado, consulte o [guia de configuração do Codex Micro da Work
Louder](https://worklouder.cc/openai-micro-setup). Para
receber suporte direto, envie um e-mail para
[hello@worklouder.cc](mailto:hello@worklouder.cc).

## Obter um Micro compatível

Confira a disponibilidade do Codex Micro na [OpenAI Supply
Co](https://openai.com/supply/co-lab/work-louder/). O aplicativo do ChatGPT para desktop também
é compatível com o [Creator Micro 2](https://worklouder.cc/creator-micro-2), disponível
diretamente na Work Louder.

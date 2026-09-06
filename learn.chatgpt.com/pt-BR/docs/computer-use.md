<!-- source: https://learn.chatgpt.com/pt-BR/docs/computer-use -->

Nas regiões compatíveis, o Uso do computador no aplicativo do ChatGPT para desktop está disponível no
macOS e no Windows com o ChatGPT Work e o Codex. Instale o plug-in de Uso do computador.
No macOS, conceda as permissões de Gravação da Tela e Acessibilidade quando
solicitado.

Com o Uso do computador, o ChatGPT pode ver e operar interfaces gráficas no macOS
ou no Windows. Use esse recurso em tarefas para as quais ferramentas de linha de comando ou integrações estruturadas
não sejam suficientes, como verificar um aplicativo para desktop, usar um navegador, alterar
configurações de aplicativos, trabalhar com uma fonte de dados que não esteja disponível como plug-in ou
reproduzir um bug que só ocorra em uma interface gráfica.

Como o Uso do computador pode afetar o estado dos aplicativos e do sistema fora do workspace do seu
projeto, use-o em tarefas de escopo delimitado e revise as solicitações de permissão antes de
continuar.

## Configure o Uso do computador

No aplicativo do ChatGPT para desktop, selecione ChatGPT e mude para Work no seletor ou selecione
Codex. Abra **Plug-ins \> Uso do
computador** e selecione **Instalar plug-in** se solicitado. Se o ChatGPT exibir **Ativar**,
selecione essa opção. Ative os controles do servidor e da habilidade do Uso do computador e selecione **Testar
agora** para começar.

  

Em seguida, abra **Configurações \> Uso do computador** para revisar o acesso aos aplicativos. Os controles do navegador
conectado exibem a ação **Gerenciar** . Os aplicativos que você aprovar para tarefas futuras aparecerão
na seção **Aplicativos sempre permitidos** .

  

No Windows, mantenha o aplicativo de destino visível na área de trabalho ativa enquanto a tarefa
estiver em execução. No macOS, conceda as permissões de Gravação da Tela e Acessibilidade quando
solicitado, para que o ChatGPT possa ver e interagir com o aplicativo de destino.

No macOS, conceda:

- A permissão de **Gravação da Tela** para que o ChatGPT possa ver o aplicativo de destino.
- A permissão de **Acessibilidade** para que o ChatGPT possa clicar, digitar e navegar.

## Quando usar o recurso Uso do computador

Para tarefas difíceis que dependem de capturas de tela ou avaliação visual, escolha
[GPT-6 Astra](/pt-BR/codex/models#gpt-6-astra) quando estiver disponível no seu seletor de
modelos. Aplicam-se a mesma configuração do plug-in, as mesmas permissões do sistema operacional e os mesmos controles de acesso
a aplicativos.

Escolha o recurso Uso do computador quando a tarefa depender de uma interface gráfica que seja
difícil de verificar apenas por meio de arquivos ou da saída de comandos.

Alguns casos de uso indicados são:

- Testar um aplicativo para macOS ou Windows, um fluxo no simulador de iOS ou outro aplicativo para desktop
que o ChatGPT esteja desenvolvendo.
- Executar uma tarefa que exija o uso do seu navegador da Web.
- Reproduzir um bug que só aparece em uma interface gráfica.
- Alterar configurações de aplicativos que exijam clicar na interface.
- Inspecionar informações em um aplicativo ou fonte de dados que não esteja disponível por meio de um
plug-in.
- No macOS, executar em segundo plano uma tarefa de escopo delimitado enquanto você continua trabalhando
em outra atividade.
- Executar um fluxo de trabalho que abranja mais de um aplicativo.

Para aplicativos Web que você está desenvolvendo localmente, use primeiro o
[navegador integrado](/pt-BR/codex/browser?surface=app).

### Uso em primeiro plano no Windows

No Windows, o Uso do computador é executado na área de trabalho ativa. Ele não pode operar em
segundo plano enquanto você continua usando a mesma sessão do Windows. Portanto, espere que o ChatGPT
mova o ponteiro, digite e assuma o controle das interações em primeiro plano durante a execução da tarefa.

Para tarefas no Windows que devam continuar enquanto você estiver ausente, mantenha o dispositivo Windows
desbloqueado e conectado à internet. Use o
[controle remoto](/pt-BR/codex/remote-connections) pelo celular para verificar o progresso
ou enviar instruções adicionais, ou execute o aplicativo do ChatGPT para desktop em uma máquina virtual
do Windows para que o Uso do computador assuma o controle da VM em vez da sua área de trabalho principal.

## Inicie uma tarefa de Uso do computador

Mencione `@Computer` ou `@AppName` no seu prompt ou peça ao ChatGPT para usar o recurso Uso do
computador. Descreva exatamente o aplicativo, a janela ou o fluxo em que o ChatGPT deve atuar.

```text
Open the app with Computer Use, reproduce the onboarding bug, and fix the
smallest code path that causes it. After each change, run the same UI flow
again.

```text
Open @Chrome and verify the checkout page still works after the latest changes.

Se o aplicativo de destino disponibilizar um plug-in dedicado ou um servidor MCP, prefira essa
integração estruturada para acessar dados e executar operações repetíveis. Escolha o recurso
Uso do computador quando o ChatGPT precisar inspecionar ou operar visualmente o aplicativo.

## Permissões e aprovações

Os administradores do workspace podem restringir quais aplicativos o Uso do computador pode acessar e
se as aprovações podem ser salvas. Consulte os
[controles gerenciados do navegador e do Uso do computador](/pt-BR/codex/enterprise/managed-configuration#control-browser-and-computer-use).

As permissões do sistema para o Uso do computador são separadas das aprovações de aplicativos no ChatGPT.
No macOS, as permissões de Gravação da Tela e Acessibilidade permitem que o ChatGPT veja e
opere aplicativos. As aprovações de aplicativos determinam quais deles você permite que o ChatGPT use. A leitura
e a edição de arquivos, assim como os comandos do shell, continuam sujeitas às configurações de sandbox e
aprovação da tarefa.

Com o Uso do computador, o ChatGPT só pode ver e realizar ações nos aplicativos que você permitir.
Durante uma tarefa, o ChatGPT pede sua permissão antes de usar um aplicativo no seu
computador. Você pode escolher **Sempre permitir** para que o ChatGPT use esse aplicativo no futuro
sem pedir novamente. É possível remover aplicativos da lista **Sempre permitir** na seção
**Uso do computador** das configurações do aplicativo do ChatGPT para desktop.

  
    
  

O ChatGPT também pode pedir permissão antes de realizar ações sensíveis ou que possam causar interrupções.

Se o ChatGPT não conseguir ver ou controlar um aplicativo, abra **Ajustes do Sistema \> Privacidade e
Segurança** e verifique as permissões de **Gravação da Tela** e **Acessibilidade** para o **Uso do computador do
Codex** no macOS. No Windows, verifique se o aplicativo de destino está visível na
sessão ativa da área de trabalho.

No Windows, o Uso do computador armazena decisões persistentes sobre aplicativos em
`$CODEX_HOME/config.toml`. Liste os aplicativos que o Uso do computador pode abrir sem
solicitar permissão:

```toml
[computer_use.windows]
always_allowed_app_ids = ["mspaint.exe"]

Use o identificador de aplicativo informado pelo Uso do computador no Windows, como o nome do
executável de um aplicativo para desktop ou um ID de modelo de usuário do aplicativo para um aplicativo empacotado. O ChatGPT
solicita permissão para aplicativos que não estão na lista. Para revogar uma decisão salva, remova
o aplicativo em **Configurações \> Uso do computador \> Sempre permitir**.

Esta tabela armazena decisões locais do Uso do computador. Ela é separada do arquivo
`requirements.toml` imposto pelos administradores, no qual eles podem desativar o Uso do
computador com `[features].computer_use = false`. As entradas antigas da lista de permissões em
`$CODEX_HOME/computer-use/config.toml` são migradas para a
configuração atual; a lista `denied` desse arquivo não faz parte do esquema atual da política.

## Uso com o Mac bloqueado

  O uso com o Mac bloqueado está disponível no macOS. No Windows, o Uso do computador funciona em primeiro plano.

O uso com o Mac bloqueado permite que o ChatGPT use o recurso Uso do computador após o bloqueio do Mac, mas somente depois que
você ativar essa opção. Use-a quando uma tarefa do ChatGPT precisar usar aplicativos para desktop a partir de um
dispositivo conectado após o bloqueio do Mac.

Ao ativar o uso com o Mac bloqueado, o ChatGPT instala um
[plug-in de autorização](https://developer.apple.com/documentation/security/authorization-plug-ins) da Apple
que participa do fluxo de desbloqueio do macOS.

O uso com o Mac bloqueado tem escopo intencionalmente restrito. Ele não é um método de desbloqueio remoto de
uso geral para o Mac e não permite que outros aplicativos ou processos locais desbloqueiem o
computador.

Para usar o recurso com o Mac bloqueado:

1. No aplicativo, abra **Configurações \> Uso do computador** .
2. Ative o uso com o Mac bloqueado.
3. Em um dispositivo conectado, inicie uma tarefa que use o recurso Uso do computador depois que a tela do Mac
for bloqueada.

Quando uma tarefa do ChatGPT acessa um aplicativo por meio do Uso do computador após o bloqueio do Mac, o ChatGPT
desbloqueia temporariamente o Mac, impede o uso local e preserva as proteções da tela
bloqueada. Antes de desbloquear, o ChatGPT verifica se a tentativa de desbloqueio está associada
a uma interação ativa e confiável do Uso do computador. Fora dessa janela de curta duração, o ChatGPT
recusa o desbloqueio e pede que você desbloqueie o Mac manualmente, se necessário.

O uso com o Mac bloqueado inclui as seguintes medidas de proteção:

- A janela de autorização tem curta duração e se limita à tentativa de desbloqueio
atual.
- O desbloqueio automático está disponível somente para o ChatGPT durante interações ativas do Uso do computador.
- O ChatGPT mantém todas as telas cobertas enquanto a área de trabalho está temporariamente desbloqueada.
- Se o ChatGPT detectar uma entrada local do teclado ou do ponteiro, ele bloqueia o Mac novamente e
pausa o desbloqueio automático até que você o desbloqueie manualmente.

## Orientações de segurança

Com o Uso do computador, o ChatGPT pode ver o conteúdo da tela, fazer capturas de tela e interagir
com janelas, menus, entradas do teclado e o estado da área de transferência no aplicativo de destino.
Considere o conteúdo visível do aplicativo, as páginas do navegador, as capturas de tela e os arquivos abertos no
aplicativo de destino como parte do contexto que o ChatGPT pode processar durante a execução da tarefa.

Mantenha as tarefas bem delimitadas e esteja presente durante fluxos sensíveis:

- Indique claramente ao ChatGPT um único aplicativo ou fluxo por vez.
- Você pode interromper a tarefa ou retomar o controle do computador a qualquer momento.
- Mantenha aplicativos sensíveis fechados, a menos que sejam necessários para a tarefa.
- No Windows, espere que o ChatGPT assuma o controle das entradas em primeiro plano enquanto trabalha; use um
dispositivo secundário, uma VM ou interrompa a tarefa antes de usar essa área de trabalho.
- Evite tarefas que exijam segredos, a menos que você esteja presente e possa aprovar cada
etapa.
- Analise as solicitações de permissão dos aplicativos antes de permitir que o ChatGPT use um aplicativo.
- Use **Sempre permitir** somente para aplicativos que você confia ao ChatGPT para uso automático em
  tarefas futuras.
- Esteja presente ao lidar com configurações de conta, segurança, privacidade, rede, pagamento ou
credenciais.
- Cancele a tarefa se o ChatGPT começar a interagir com a janela errada.

Se o ChatGPT usar seu navegador, ele poderá interagir com páginas nas quais você já
fez login. Analise as ações nos sites como se você mesmo as estivesse realizando: páginas da Web
podem conter conteúdo malicioso ou enganoso, e os sites podem atribuir à sua conta cliques aprovados,
envios de formulários e ações realizadas durante uma sessão autenticada. Para continuar
usando seu navegador enquanto o ChatGPT trabalha, peça que ele use outro navegador.

O recurso não pode automatizar aplicativos de terminal nem o próprio ChatGPT, pois isso
poderia contornar as políticas de segurança do ChatGPT. Ele também não pode se autenticar como
administrador nem aprovar solicitações de permissão de segurança e privacidade no seu
computador.

As alterações em arquivos e os comandos do shell continuam sujeitos às configurações de aprovação e do Sandbox
do ChatGPT, quando aplicável. Alterações feitas em aplicativos para desktop podem não aparecer no painel de revisão
até serem salvas no disco e rastreadas pelo projeto. Seus controles de dados do ChatGPT
se aplicam ao conteúdo processado pelo ChatGPT, incluindo capturas de tela feitas
pelo Uso do computador.

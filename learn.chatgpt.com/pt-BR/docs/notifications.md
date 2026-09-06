<!-- source: https://learn.chatgpt.com/pt-BR/docs/notifications -->

As notificações avisam quando uma atividade precisa da sua atenção. Os controles e
canais de entrega variam de acordo com a interface.

## Configurar notificações da área de trabalho

Abra [**Configurações**](codex://settings) para escolher quando os alertas de conclusão de turno
serão exibidos: nunca, somente enquanto o ChatGPT estiver em segundo plano ou sempre. Controles
separados permitem ativar ou desativar notificações sobre solicitações de permissão e perguntas. Seu
sistema operacional pode pedir que você permita que o aplicativo do ChatGPT
para desktop envie notificações.

### Acompanhar chats na visualização Atividade

Quando **Atividade** estiver disponível, selecione o sino na barra lateral para ver os chats
não lidos, em execução ou aguardando sua resposta. Você também pode abrir ou
fechar a visualização Atividade com <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>U</kbd> no macOS
ou <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>U</kbd> no Windows.

Use as opções da visualização para escolher quais chats serão exibidos. Dependendo da interface
em uso, as opções podem incluir **Work**, **Chat**, **Fixados** e
**Agendados**. Você também pode selecionar **Marcar tudo como lido** para limpar as marcações de itens não lidos.

<a id="follow-task-activity-with-a-pet"></a>

### Acompanhar a atividade dos chats com um mascote

No aplicativo ChatGPT para desktop, um mascote flutuante é outra forma de acompanhar a
atividade dos chats enquanto você trabalha em outros aplicativos. Ele pode exibir um destes status para o chat: **Em execução**,
**Precisa de informações**, **Pronto** ou **Bloqueado**.

Consulte [Mascotes](/pt-BR/codex/pets?surface=app) para escolher um mascote, entender seu status ou
criar seu próprio mascote.

## Configurar notificações na Web

Abra **Configurações \> Notificações** para gerenciar as categorias e os
canais de notificação disponíveis para sua conta. Dependendo da categoria e da conta,
os canais podem incluir notificações push, e-mail ou SMS. Use **Gerenciar tarefas** nas configurações de
notificação de tarefas para abrir **Agendados**.

## Configurar notificações da CLI

Para notificações no terminal e notificações externas, consulte
[Notificações](/pt-BR/codex/config-file/config-advanced#notifications) no guia de
configuração avançada. Você pode definir quando a TUI emite uma notificação
e se o Codex executa um programa externo ao concluir um turno.

<a id="follow-task-activity-in-the-ide"></a>

## Acompanhar a atividade do chat na IDE

A extensão para IDE não oferece controles de notificação separados. Mantenha o
chat aberto para acompanhar sua atividade. Para executar um programa externo quando um turno
for concluído, configure `notify` no host do Codex conectado. Consulte
[Notificações](/pt-BR/codex/config-file/config-advanced#notifications) no guia de
configuração avançada.

## Documentação relacionada

- [Trabalho de longa duração](/pt-BR/codex/long-running-work)
- [Tarefas agendadas](/pt-BR/codex/automations)
- [Mascotes](/pt-BR/codex/pets)

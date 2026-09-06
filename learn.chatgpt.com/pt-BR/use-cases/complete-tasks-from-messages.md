<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/complete-tasks-from-messages -->

## Introdução

Muitas conversas contêm tarefas implícitas: fazer uma reserva para jantar, agendar um acompanhamento, pesquisar opções, enviar um recibo ou reunir informações para uma resposta. O recurso Uso do computador pode ajudar lendo a conversa, identificando a tarefa e concluindo o trabalho nos aplicativos envolvidos.

Isso funciona bem quando a mensagem contém uma solicitação concreta e você quer que o ChatGPT dê continuidade a ela, em vez de apenas resumir a conversa.

## Como usar

1. Instale o [plug-in de Uso do computador](/pt-BR/codex/computer-use).
2. Peça ao ChatGPT para revisar uma conversa específica ou as mensagens de um remetente específico.
3. Diga qual ação deve ser realizada e se o ChatGPT deve pausar antes de concluir qualquer coisa.
4. Especifique se o ChatGPT deve redigir uma resposta na conversa original.

Por exemplo:

- `@Computer Look at my messages from [person]. Check my availability, find 2 dinner options in Hayes Valley, and draft a reply in the same thread. Check in with me before completing booking.`

## Dicas práticas

### Peça uma pausa antes de ações irreversíveis

Se a tarefa puder envolver o envio de dinheiro, a realização de um pedido, a confirmação de uma reserva ou a finalização de um agendamento, diga ao ChatGPT para parar e pedir sua confirmação antes de dar esse último passo.

### Verifique se os aplicativos necessários estão prontos

Isso funciona melhor quando o login já foi feito nos aplicativos relacionados e eles estão disponíveis. Se a tarefa depender do Mapas, Calendário, Notas, de um site de reservas ou de uma sessão no navegador, deixe tudo pronto com antecedência.

### Considere que a conversa será marcada como lida

Quando o ChatGPT abrir a conversa no Mensagens, ele vai se comportar como qualquer usuário que visualiza a conversa. Considere-a lida.

## Próximos passos

Esse padrão também pode funcionar em outras interfaces no estilo de caixa de entrada, como Slack ou e-mail, quando o trabalho começa em uma mensagem e termina em outro lugar. Se esse fluxo de trabalho passar a ser recorrente, adicione uma preferência ou instrução reutilizável em [Personalização](/pt-BR/codex/customization/overview) para que o ChatGPT trate essas solicitações sempre da mesma forma.

### Prompt sugerido

**Conclua uma tarefa a partir de uma conversa**

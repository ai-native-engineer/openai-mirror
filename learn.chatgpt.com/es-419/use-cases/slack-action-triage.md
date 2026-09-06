<!-- source: https://learn.chatgpt.com/es-419/use-cases/slack-action-triage -->

## Encuentra el trabajo oculto en Slack

Slack suele ser donde comienza una solicitud, pero no donde se encuentra todo el contexto. Puede que un compañero te pida una respuesta por mensaje directo, aclare la acción concreta en un hilo, comparta un enlace a un documento en un canal y más tarde resuelva el asunto sin volver a mencionarte.

Usa este flujo de trabajo cuando quieras que ChatGPT lea el contexto de Slack, compruebe si la solicitud sigue vigente y muestre solo los elementos que realmente requieren tu atención. El objetivo es obtener una lista de acciones ordenada por prioridad: qué necesita una respuesta o una decisión, con qué persona hay que comunicarse, qué documento debe actualizarse o qué requiere un traspaso.

## Haz una ronda de clasificación

1. Indícale a ChatGPT un período, una línea de trabajo, una persona, un canal o un tema.
2. Pídele que busque en los mensajes directos, los mensajes directos grupales, las menciones en canales y las respuestas relevantes de los hilos.
3. Pídele a ChatGPT que lea las respuestas más recientes de cada hilo antes de considerar que un elemento sigue pendiente.
4. Pide una lista de acciones ordenada por urgencia e impacto.
5. Pídele a ChatGPT que redacte la respuesta, el mensaje de traspaso o la tarea de seguimiento.

Después de probar este flujo y ajustarlo a tus necesidades, puedes [programar una tarea para este trabajo desde el chat](/es-419/codex/automations#schedule-a-task-inside-a-chat) pidiéndole a ChatGPT que haga lo mismo de manera programada.

## Pide el resultado adecuado

Un resultado útil de la clasificación debe explicar por qué cada elemento sigue pendiente. También debe omitir las solicitudes antiguas que alguien atendió posteriormente en el hilo.

Deberías obtener algo parecido a esto:

  <p>
    <strong>Principal acción pendiente:</strong> Priya pide ejemplos concretos de
    clientes, no solo más ideas.
  </p>
  <p>
    <strong>Por qué es importante:</strong> la actualización del lanzamiento requiere personas reales que
    el equipo pueda contactar esta semana.
  </p>
  <p>
    <strong>Evidencia:</strong> el mensaje original del canal pedía casos de uso,
    pero más adelante se indica en el hilo: “por favor, escríbeme por mensaje directo si tienes posibles contactos”.
  </p>
  <p>
    <strong>Siguiente paso:</strong> responde con los nombres de dos posibles contactos o di que puedes ser
    el ejemplo si eso resulta más útil.
  </p>

Un buen resultado deja explícitas las diferencias: una idea no es lo mismo que un posible contacto, una solicitud vigente no es lo mismo que un mensaje meramente informativo y una solicitud que ya atendiste no debe seguir en la lista.

Si obtienes demasiados resultados irrelevantes o muy pocos elementos que requieran acción, ajusta el prompt y, si es necesario, menciona los canales específicos de Slack a los que quieres que ChatGPT preste atención.

## Redacta el seguimiento

Cuando la lista tenga lo que necesitas, continúa con el siguiente paso en el mismo chat. Pídele a ChatGPT que redacte una respuesta o un mensaje de traspaso a partir de la evidencia que ya recopiló:

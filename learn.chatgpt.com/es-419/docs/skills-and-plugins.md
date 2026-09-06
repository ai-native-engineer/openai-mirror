<!-- source: https://learn.chatgpt.com/es-419/docs/skills-and-plugins -->

Las habilidades y los complementos ayudan a ChatGPT y Codex a realizar tareas recurrentes con las
instrucciones, los recursos y las herramientas adecuados. Reducen la necesidad de pegar el
mismo prompt, la misma plantilla, los mismos requisitos o el mismo proceso en cada chat.

- Una **habilidad** reúne instrucciones y recursos de apoyo para una
  tarea o un flujo de trabajo específicos.
- Un **complemento** es un paquete instalable que puede incluir habilidades, conectores o
  ambos. Los conectores se basan en servidores del Protocolo de Contexto de Modelo (MCP) y pueden
  incluir opcionalmente una interfaz de usuario personalizada de ChatGPT.

## Usa habilidades para tareas recurrentes

Una habilidad es un flujo de trabajo reutilizable que proporciona a ChatGPT o Codex orientación
específica para una tarea. Puede plasmar la forma en que ya realizas las tareas recurrentes para que cualquiera de los dos
productos siga el mismo proceso cada vez que surja esa tarea.

Una habilidad puede combinar:

- Un nombre y una descripción que ayudan a ChatGPT y Codex a reconocer en qué casos la habilidad
es adecuada.
- Instrucciones del flujo de trabajo que definen el proceso y el resultado esperado.
- Recursos de apoyo, como plantillas, ejemplos, lineamientos de marca, esquemas
o herramientas conectadas.

Las habilidades son más útiles cuando obtener buenos resultados depende de un enfoque repetible. Por
ejemplo, una habilidad puede preparar un resumen diario, revisar documentación, crear una
presentación, aplicar una norma de redacción del equipo o recopilar información de las
mismas herramientas conectadas cada semana.

Usa las habilidades para mejorar la coherencia, incorporar las prácticas recomendadas del equipo al
flujo de trabajo y compartir un proceso estándar, en lugar de depender de conocimientos
no documentados.

ChatGPT y Codex pueden elegir una habilidad cuando tu solicitud coincide con su propósito. También
puedes seleccionarla explícitamente. ChatGPT admite menciones de habilidades con `@`, mientras que Codex
admite menciones de habilidades con `$`.

## Crear habilidades

Puedes comenzar por convertir una tarea que ya repites en una guía práctica y específica para
ChatGPT y Codex. Para tu primera habilidad, puedes elegir una actualización semanal, un resumen de campaña,
el seguimiento de una reunión o cualquier tarea cuyos pasos y formato deban mantenerse
constantes.

Para crear una habilidad útil:

1. **Elige una tarea específica.** Anota con qué sueles comenzar, como
   archivos, enlaces o notas, y cómo debería ser el resultado final.
2. **Describe el flujo de trabajo.** En ChatGPT, comienza con `@skill-creator`; en Codex,
   usa `$skill-creator`. Explica el objetivo, los pasos que se deben seguir, el formato
   esperado y todo lo que la habilidad siempre debe incluir o evitar. Agrega una plantilla
   o un buen ejemplo si tienes uno.
3. **Revisa y prueba el borrador.** Verifica las instrucciones, prueba la habilidad con una
   solicitud realista y ajústala si el resultado omite un paso o se desvía
   del formato que deseas.
4. **Instálala y reutilízala.** Una vez habilitada la habilidad, ChatGPT o Codex puede
   usarla para solicitudes pertinentes, o puedes seleccionarla explícitamente. También puedes
   compartirla con tus compañeros de equipo cuando la configuración de tu espacio de trabajo lo permita.

Para obtener más detalles sobre cómo crear habilidades, consulta nuestra guía específica a continuación.

  
    <span slot="icon">
      
    </span>
    Crea, prueba y comparte habilidades reutilizables con ChatGPT y Codex.
  

## Usa complementos para herramientas y flujos de trabajo compartidos

Los complementos permiten instalar y compartir capacidades reutilizables con mayor facilidad. Un complemento puede
combinar habilidades con conectores para servicios como GitHub, Google Drive o
Slack, y puede incluir servidores MCP que proporcionen herramientas y contexto adicionales.

ChatGPT y Codex comparten un único directorio universal de complementos. Explóralo cuando quieras
agregar un flujo de trabajo existente en lugar de crear uno por tu cuenta. Después de instalar
un complemento, describe la tarea directamente o elige explícitamente un complemento o una
habilidad incluida mediante la sintaxis de invocación correspondiente a la interfaz que uses.

[Aprende a instalar y usar complementos](/es-419/codex/plugins).

## Elige entre una habilidad y un complemento

Usa una habilidad cuando necesites instrucciones reutilizables para una tarea específica. Usa un
complemento cuando quieras un paquete instalable que pueda combinar instrucciones con
servicios conectados u otras herramientas.

También puedes demostrar un flujo de trabajo con
[Grabar y reproducir](/es-419/codex/extend/record-and-replay), que convierte la grabación en una
habilidad reutilizable. Para empaquetar y distribuir tu propio paquete, consulta
[Crear plugins](https://developers.openai.com/plugins/build/plugins).

Si tu complemento necesita conectarse a un servicio o exponer herramientas de MCP, consulta
[Crear un servidor MCP](https://developers.openai.com/plugins/build/mcp-server). Cuando tu complemento esté listo para la revisión pública,
consulta [Enviar complementos](https://developers.openai.com/plugins/deploy/submission).

Para ver más ejemplos de flujos de trabajo reutilizables, consulta [Usar habilidades en OpenAI
Academy](https://openai.com/academy/skills/).

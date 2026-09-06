<!-- source: https://learn.chatgpt.com/es-419/docs/third-party/slack -->

Usa Codex en Slack para iniciar tareas de programación desde canales e hilos. Menciona a `@Codex` e incluye un prompt; Codex crea un chat en la nube y responde con los resultados.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>

<br />

## Configurar la app de Slack

1. Configura los [chats en la nube de Codex](/es-419/codex/cloud). Necesitas un plan Plus, Pro, Business, Enterprise o Edu (consulta los [precios de ChatGPT](https://chatgpt.com/pricing)), una cuenta de GitHub conectada y al menos un [entorno](/es-419/codex/environments/cloud-environment).
2. Ve a la [configuración de Codex](https://chatgpt.com/codex/settings/connectors) e instala la app de Slack en tu espacio de trabajo. Según las políticas de tu espacio de trabajo de Slack, es posible que un administrador deba aprobar la instalación.
3. Agrega `@Codex` a un canal. Si aún no lo agregaste, Slack te pedirá que lo hagas cuando lo menciones.

<a id="start-a-task"></a>

## Iniciar un chat

1. En un canal o hilo, menciona a `@Codex` e incluye tu prompt. Codex puede consultar mensajes anteriores del hilo, por lo que a menudo no necesitas repetir el contexto.
2. (Opcional) Especifica un entorno o repositorio en tu prompt, por ejemplo: `@Codex fix the above in openai/codex`.
3. Espera a que Codex reaccione (👀) y responda con un enlace al chat. Cuando termine, Codex publicará el resultado y, según tu configuración, una respuesta en el hilo.

### Cómo elige Codex un entorno y un repositorio

- Codex revisa los entornos a los que tienes acceso y selecciona el que mejor se ajusta a tu solicitud. Si la solicitud es ambigua, recurre al entorno que usaste más recientemente.
- El chat se ejecuta en la rama predeterminada del primer repositorio que figura en el mapa de repositorios de ese entorno. Actualiza el mapa de repositorios en Codex si necesitas cambiar el repositorio predeterminado o agregar más repositorios.
- Si no hay ningún entorno o repositorio adecuado disponible, Codex responderá en Slack con instrucciones para solucionar el problema antes de volver a intentarlo.

### Controles de datos para empresas

De forma predeterminada, Codex publica una respuesta en el hilo que puede incluir información del entorno en el que se ejecutó.
Para evitarlo, un administrador de Enterprise puede desmarcar **Permitir que la app de Codex para Slack publique respuestas cuando se complete una tarea** en la [configuración del espacio de trabajo de ChatGPT](https://chatgpt.com/admin/settings). Cuando un administrador desactiva las respuestas, Codex solo responde con un enlace al chat.

### Uso de datos, privacidad y seguridad

Cuando mencionas a `@Codex`, Codex recibe tu mensaje y el historial del hilo para comprender tu solicitud y crear un chat.
El tratamiento de los datos se rige por la [Política de privacidad](https://openai.com/privacy) y los [Términos de uso](https://openai.com/terms/) de OpenAI, así como por sus otras [políticas](https://openai.com/policies) aplicables.
Para obtener más información sobre la seguridad, consulta la [documentación de seguridad](/es-419/codex/agent-approvals-security) de Codex.

Codex usa modelos de lenguaje de gran tamaño que pueden cometer errores. Revisa siempre las respuestas y los diffs.

### Consejos y solución de problemas

- **Faltan conexiones**: si Codex no puede confirmar tu conexión con Slack o con GitHub, responde con un enlace para volver a conectarte.
- **Selección inesperada del entorno**: responde en el hilo indicando el entorno que quieres usar (por ejemplo, `Please run this in openai/openai (applied)`) y luego vuelve a mencionar a `@Codex`.
- **Hilos largos o complejos**: resume los detalles clave en tu mensaje más reciente para que Codex no pase por alto el contexto oculto entre mensajes anteriores del hilo.
- **Publicación en el espacio de trabajo**: algunos espacios de trabajo Enterprise restringen la publicación de respuestas finales. En esos casos, abre el enlace al chat para ver el progreso y los resultados.
- **Más ayuda**: consulta el [Centro de ayuda de OpenAI](https://help.openai.com/).

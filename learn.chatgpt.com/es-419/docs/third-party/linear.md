<!-- source: https://learn.chatgpt.com/es-419/docs/third-party/linear -->

Usa Codex en Linear para delegar trabajo desde las incidencias. Asigna una incidencia a Codex o menciona a `@Codex` en un comentario; Codex crea un chat en la nube y responde con avances y resultados.

Codex en Linear está disponible en los planes de pago (consulta [Precios](/es-419/codex/pricing)).

Si tienes un plan Empresas, pídele al administrador de tu espacio de trabajo de ChatGPT que active los chats en la nube de Codex en la [configuración del espacio de trabajo](https://chatgpt.com/admin/settings) y habilite **Codex para Linear** en la [configuración de conectores](https://chatgpt.com/admin/ca).

## Configurar la integración con Linear

1. Para configurar los [chats en la nube de Codex](/es-419/codex/cloud), conecta GitHub en [Codex](https://chatgpt.com/codex) y crea un [entorno](/es-419/codex/environments/cloud-environment) para el repositorio en el que quieres que trabaje Codex.
2. Ve a la [configuración de Codex](https://chatgpt.com/codex/settings/connectors) e instala **Codex para Linear** para tu espacio de trabajo.
3. Para vincular tu cuenta de Linear, menciona a `@Codex` en un hilo de comentarios de una incidencia de Linear.

## Delegar trabajo a Codex

Puedes delegar de dos maneras:

### Asignar una incidencia a Codex

Después de instalar la integración, puedes asignar incidencias a Codex del mismo modo que a tus compañeros de equipo. Codex comienza a trabajar y publica actualizaciones en la incidencia.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

### Mencionar a `@Codex` en los comentarios

También puedes mencionar a `@Codex` en los hilos de comentarios para delegar trabajo o hacer preguntas. Después de que Codex responda, continúa la conversación en el hilo para seguir en el mismo chat.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

Cuando Codex comienza a trabajar en una incidencia, [elige un entorno y un repositorio](#how-codex-chooses-an-environment-and-repo) en los que trabajar.
Para fijar un repositorio específico, inclúyelo en tu comentario; por ejemplo: `@Codex fix this in openai/codex`.

Para consultar el progreso:

- Abre **Actividad** en la incidencia para ver las actualizaciones sobre el progreso.
- Abre el enlace del chat para seguir el progreso con más detalle.

Cuando Codex termina, publica un resumen y un enlace al chat completado para que puedas crear un Pull Request.

### Cómo elige Codex un entorno y un repositorio

- Linear sugiere un repositorio según el contexto de la incidencia. Codex selecciona el entorno que mejor coincide con esa sugerencia. Si la solicitud es ambigua, recurre al entorno que usaste más recientemente.
- El chat se ejecuta en la rama predeterminada del primer repositorio incluido en el mapa de repositorios de ese entorno. Actualiza el mapa de repositorios en Codex si necesitas definir otro repositorio como predeterminado o agregar más repositorios.
- Si no hay ningún entorno o repositorio adecuado disponible, Codex responderá en Linear con instrucciones para corregir el problema antes de volver a intentarlo.

## Asignar incidencias a Codex automáticamente

Puedes asignar incidencias a Codex automáticamente mediante reglas de clasificación:

1. En Linear, ve a **Configuración**.
2. En **Tus equipos**, selecciona tu equipo.
3. En la configuración del flujo de trabajo, abre **Clasificación** y actívala.
4. En **Reglas de clasificación**, crea una regla y elige **Delegar** \> **Codex** (y cualquier otra propiedad que quieras establecer).

Linear asigna automáticamente a Codex las incidencias nuevas que entran en clasificación.
Cuando usas reglas de clasificación, Codex ejecuta los chats con la cuenta de la persona que creó la incidencia.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

## Uso de datos, privacidad y seguridad

Cuando mencionas a `@Codex` o le asignas una incidencia, Codex recibe el contenido de la incidencia para comprender tu solicitud y crear un chat.
El tratamiento de datos se rige por la [Política de privacidad](https://openai.com/privacy) y los [Términos de uso](https://openai.com/terms/) de OpenAI, así como por otras [políticas](https://openai.com/policies) aplicables.
Para obtener más información sobre seguridad, consulta la [documentación de seguridad de Codex](/es-419/codex/agent-approvals-security).

Codex utiliza modelos de lenguaje de gran tamaño que pueden cometer errores. Revisa siempre las respuestas y las diferencias.

## Consejos y solución de problemas

- **Conexiones faltantes**: si Codex no puede confirmar tu conexión con Linear, responde en la incidencia con un enlace para conectar tu cuenta.
- **Selección inesperada del entorno**: responde en el hilo e indica el entorno que quieres (por ejemplo, `@Codex please run this in openai/codex`).
- **Parte incorrecta del código**: agrega más contexto a la incidencia o proporciona instrucciones explícitas en tu comentario con `@Codex`.
- **Más ayuda**: consulta el [Centro de ayuda de OpenAI](https://help.openai.com/).

<a id="connect-linear-for-local-tasks-mcp"></a>

## Conectar Linear para trabajar localmente (MCP)

Si usas la aplicación de escritorio de ChatGPT, Codex CLI o la extensión para IDE y quieres que Codex acceda localmente a las incidencias de Linear, configura el servidor de Model Context Protocol (MCP) de Linear.

Para obtener más información, [consulta la documentación de Linear sobre MCP](https://linear.app/integrations/codex-mcp).

Los pasos para configurar el servidor MCP son los mismos tanto si usas la extensión para IDE como la CLI, ya que ambas comparten la misma configuración.

### Usar la CLI (recomendado)

Si tienes instalada la CLI, ejecuta:

```bash
codex mcp add linear --url https://mcp.linear.app/mcp

Se te pedirá que inicies sesión con tu cuenta de Linear y la conectes a Codex.

### Configurar manualmente

1. Abre `~/.codex/config.toml` en tu editor.
2. Agrega lo siguiente:

```toml
[mcp_servers.linear]
url = "https://mcp.linear.app/mcp"

3. Ejecuta `codex mcp login linear` para iniciar sesión.

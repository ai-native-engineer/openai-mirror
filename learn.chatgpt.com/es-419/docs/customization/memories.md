<!-- source: https://learn.chatgpt.com/es-419/docs/customization/memories -->

Las memorias permiten que ChatGPT y Codex incorporen contexto útil de trabajos anteriores en
trabajos futuros.
La versión web de ChatGPT usa la memoria de ChatGPT, mientras que los clientes locales de Codex usan un
almacén local de memorias independiente y controles propios.

Mantén las instrucciones obligatorias del equipo en `AGENTS.md` o en documentación incluida en el repositorio. Considera
las memorias como una capa útil para recuperar información, no como la única fuente de reglas que deban
aplicarse siempre.

En la aplicación de escritorio de ChatGPT, usa `/memories` para elegir si un chat puede usar
las memorias locales o contribuir a crear memorias futuras. Administra la función desde
**Configuración \> Personalización** cuando necesites activarla o desactivarla.

Administra la memoria de ChatGPT desde **Configuración \> Personalización**. ChatGPT Work usa
la configuración de memoria disponible para tu cuenta y espacio de trabajo; no usa un
almacén local de memorias de Codex ni controles locales de memoria.

En Codex CLI, usa `/memories` en una sesión interactiva para controlar si el
chat actual puede usar las memorias locales existentes o usarse como dato de entrada para generar
memorias futuras. Consulta [Configurar las memorias locales](#configure-local-memories) si el
comando no está disponible.

La extensión para IDE usa el almacén local de memorias del host de Codex conectado. Cuando
las memorias están activadas para ese host, usa los mismos controles por chat que Codex
CLI.

[Historial de la computadora](/es-419/codex/customization/computer-history) es una función de escritorio de macOS
que convierte la actividad en las aplicaciones y los sitios web permitidos en memorias y
en una cronología que ChatGPT y Codex pueden consultar.

<a id="how-memories-work"></a>
<a id="memory-storage"></a>
<a id="control-memories-per-thread"></a>
<a id="control-memories-per-chat"></a>
<a id="control-memories-per-task"></a>
<a id="review-memories"></a>

## Cómo funcionan las memorias locales de Codex

Después de activar las memorias, Codex puede convertir el contexto útil de chats anteriores
que cumplen los requisitos en archivos locales de memoria. Codex omite las sesiones activas o de corta duración,
elimina los secretos de los campos de memoria generados y actualiza las memorias en
segundo plano, en lugar de hacerlo de inmediato al final de cada chat.

Es posible que las memorias no se actualicen de inmediato cuando termina un
chat. Codex espera a que el chat lleve suficiente tiempo inactivo para evitar resumir un trabajo que aún está
en curso.

La generación de memorias también puede omitir una ejecución en segundo plano cuando el porcentaje restante de tu límite de solicitudes de Codex
sea inferior al umbral configurado, para que Codex no consuma
cuota cuando estés cerca de un límite.

## Almacenamiento local de memorias

Codex almacena las memorias en tu directorio de inicio de Codex. De forma predeterminada, ese directorio es
`~/.codex`. Consulta [Ubicaciones de configuración y estado](/es-419/codex/config-file/config-advanced#config-and-state-locations)
para saber cómo usa Codex `CODEX_HOME`.

Los principales archivos de memoria se encuentran en `~/.codex/memories/` e incluyen resúmenes,
entradas persistentes, datos de entrada recientes y evidencia de respaldo de chats anteriores.

Considera estos archivos como un estado generado. Puedes inspeccionarlos para solucionar problemas
o antes de compartir tu directorio de inicio de Codex, pero no dependas de la edición
manual como tu principal mecanismo de control.

<a id="control-local-memories-per-task"></a>

## Controlar las memorias locales en cada chat

En la aplicación de escritorio de ChatGPT y en Codex TUI, usa `/memories` para controlar cómo se usan las memorias en
el chat actual. Las opciones de cada chat te permiten decidir si el chat actual
puede usar las memorias existentes y si Codex puede usar el chat para
generar memorias futuras.

Las opciones de cada chat no cambian la configuración global de las memorias.

## Revisar las memorias locales

No almacenes secretos en las memorias. Codex elimina los secretos de los campos de memoria
generados, pero aun así debes revisar los archivos de memoria antes de compartir tu directorio de inicio
de Codex o los artefactos de memoria generados.

<a id="enable-memories"></a>
<a id="configuration"></a>

## Configurar las memorias locales

Las memorias locales de Codex están desactivadas de forma predeterminada. En la aplicación de escritorio de ChatGPT, abre
**Configuración \> Personalización** y activa la opción **Activar memorias**.

Para configurarlas mediante el archivo de configuración, agrega la marca de función a `config.toml`:

```toml
[features]
memories = true

Para conocer las ubicaciones de los archivos de configuración y la lista completa de opciones relacionadas con las memorias, consulta
[Configuración básica](/es-419/codex/config-file/config-basic) y la [referencia de
configuración](/es-419/codex/config-file/config-reference).

Algunas opciones comunes de configuración de las memorias son:

- `memories.generate_memories`: controla si los chats recién creados pueden
  almacenarse como datos de entrada para generar memorias.
- `memories.use_memories`: controla si Codex inyecta las memorias existentes en
  sesiones futuras.
- `memories.disable_on_external_context`: cuando se establece en `true`, impide que los chats que usaron
  contexto externo, como llamadas a herramientas de MCP, Búsqueda web o búsqueda de herramientas, se usen para
  generar memorias. La clave anterior `memories.no_memories_if_mcp_or_web_search`
  se sigue aceptando como alias.
- `memories.min_rate_limit_remaining_percent`: controla el porcentaje mínimo restante
  del límite de solicitudes de Codex necesario para que comience la generación de memorias.
- `memories.extract_model`: reemplaza el modelo utilizado para extraer memorias de cada
  chat.
- `memories.consolidation_model`: reemplaza el modelo utilizado para la consolidación global de
  memorias.

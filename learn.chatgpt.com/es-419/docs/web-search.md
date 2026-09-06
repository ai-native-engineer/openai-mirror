<!-- source: https://learn.chatgpt.com/es-419/docs/web-search -->

ChatGPT incluye una herramienta propia de búsqueda web. Trata todos los resultados web como
datos de entrada no confiables.

En la aplicación de escritorio de ChatGPT, pide información actualizada en un chat. ChatGPT registra
la actividad de búsqueda junto con las demás llamadas a herramientas en la transcripción.

En ChatGPT Web, pide información actualizada o fuentes. Los resultados de búsqueda y
las citas aparecen en el chat cuando ChatGPT usa la búsqueda web. La configuración del espacio de trabajo
puede limitar la disponibilidad de la búsqueda.

En la CLI, usa `--search` para obtener resultados en tiempo real durante una ejecución:

```bash
codex --search "Summarize the latest release notes for this dependency"

Las búsquedas aparecen como elementos `web_search` en la transcripción interactiva y en la salida de
`codex exec --json`.

En la extensión para IDE, pide a Codex que busque mientras trabajas en el editor. La
extensión usa el modo de búsqueda del Host de Codex conectado. La actividad de búsqueda aparece
en la transcripción del chat.

## Configurar la búsqueda web local

En los chats locales de Codex, Codex habilita la búsqueda en caché de forma predeterminada. El modo en caché usa
un índice mantenido por OpenAI en lugar de consultar cualquier página en tiempo real, lo que
reduce el riesgo de inyección de prompts, aunque no lo elimina.

La búsqueda web es una herramienta alojada, independiente del acceso a la red de los comandos locales ejecutados en el sandbox.
No usa el proxy de red ni la lista de dominios permitidos del perfil de permisos, y
puede seguir disponible cuando el acceso de los comandos a la red está deshabilitado. Configura
la búsqueda con `web_search`, `tools.web_search.allowed_domains` y la opción administrada
`allowed_web_search_modes`, según corresponda. Los filtros de dominios de búsqueda no restringen
el tráfico de los comandos locales, las apps, los conectores ni los servidores MCP.

Usa la búsqueda en tiempo real cuando tu tarea dependa de la información más reciente. Establece
`web_search = "live"` en `config.toml`. Establece `web_search = "disabled"` para desactivar
la herramienta. El modo `"indexed"` solo permite el acceso externo a la web cuando el
índice de búsqueda autoriza la solicitud. Cuando Codex se ejecuta con acceso completo, la búsqueda web
usa resultados en tiempo real de forma predeterminada. Consulta [Configuración básica](/es-419/codex/config-file/config-basic)
para conocer las ubicaciones de los archivos de configuración y su orden de precedencia.

### Buscar con un proveedor de modelos personalizado

Un proveedor de modelos personalizado puede optar por la búsqueda web independiente si admite
un punto de acceso de búsqueda compatible:

```toml
model_provider = "custom"
web_search = "live"

[model_providers.custom]
name = "Custom Responses provider"
base_url = "https://example.com/v1"
env_key = "CUSTOM_RESPONSES_API_KEY"
supports_standalone_web_search = true

De forma predeterminada, los proveedores personalizados usan `supports_standalone_web_search = false`.
La búsqueda web independiente sigue en desarrollo y está desactivada de forma predeterminada.
Configurar esta capacidad del proveedor no habilita la función: el proveedor,
el modelo seleccionado y el entorno de ejecución también deben admitir la búsqueda independiente. Las restricciones del espacio de trabajo y
de búsqueda administrada se siguen aplicando.

Para conocer los límites de red que se aplican a los entornos de Codex Cloud, consulta [Acceso a
Internet](/es-419/codex/cloud/internet-access).

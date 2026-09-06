<!-- source: https://learn.chatgpt.com/es-419/docs/import -->

Usa el flujo de importación para transferir instrucciones, configuración, habilidades, complementos, proyectos
y trabajo reciente desde otro agente a la aplicación de escritorio de ChatGPT o a Codex CLI.
La app de escritorio puede importar desde **Claude Code**, <strong>Claude Cowork</strong>
o **Cursor**. Codex CLI puede importar desde **Claude Code** o **Cursor**.

La app de escritorio importa directamente los elementos compatibles y te permite completar la configuración de
los complementos importados o las conexiones importadas que requieren autorización. También puedes mantener
sincronizado el trabajo importado mediante actualizaciones automáticas.

La importación no cambia ni elimina la configuración existente de tu agente.

  

## Iniciar una importación

### Importar en la app de escritorio

1. En la aplicación de escritorio de ChatGPT, abre **Configuración \> Importar**. Si **Importar** aún no
   está disponible como sección de configuración, abre **General** y busca **Importar configuración de otro
   agente**.
2. Selecciona **Importar**.
3. Elige los agentes desde los que quieres importar y luego selecciona **Continuar**.
4. En **Seleccionar elementos para importar**, elige qué quieres transferir y luego selecciona **Continuar**.
5. Cuando termine la importación, abre un proyecto o un chat que hayas importado para seguir trabajando.

### Mantener sincronizado el trabajo importado

En la aplicación de escritorio de ChatGPT, abre **Configuración \> Importar** y activa las actualizaciones
automáticas para mantener el trabajo importado sincronizado con el agente original. También puedes
consultar tu historial de importaciones desde la misma sección de configuración.

### Importar en Codex CLI

1. Inicia una sesión local de Codex CLI y escribe `/import`.
2. Elige **Claude Code** o **Cursor**.
3. Selecciona la configuración compatible, los archivos del proyecto y los chats recientes que quieras
importar.
4. Revisa la configuración importada y continúa trabajando en Codex.

Codex CLI importa hasta 50 chats de los últimos 30 días. El comando `/import`
no está disponible mientras se ejecuta una tarea, en una sesión remota ni mientras estás conectado
a un daemon local de app-server. Consulta [Comandos slash
de la CLI](/codex/developer-commands?surface=cli#cli-import-claude-code-or-cursor-setup-with-import).

  

## Cómo funciona la importación

El flujo de importación revisa tanto tu configuración a nivel de usuario como tus proyectos existentes.
La configuración a nivel de usuario proviene de archivos en tu computadora. La configuración a nivel de proyecto proviene
de archivos de los repositorios y las carpetas que selecciones.

Cuando realizas una importación, ChatGPT:

1. Detecta la configuración compatible y el trabajo reciente.
2. Importa los elementos que seleccionas.
3. Mantiene sin cambios la configuración existente de tu agente.
4. Comprueba si los complementos importados o las conexiones importadas aún requieren configuración.
5. Muestra una tarjeta de estado cuando necesitas completar la configuración.

## Qué puede importar ChatGPT

| Elemento importado                     | Destino                                             |
| --------------------------------- | ------------------------------------------------------- |
| Archivos de instrucciones                 | [`AGENTS.md`](/es-419/codex/agent-configuration/agents-md)     |
| `settings.json`                   | [`config.toml`](/es-419/codex/config-file/config-basic)        |
| Habilidades                            | [Habilidades](/es-419/codex/build-skills)                           |
| Complementos                           | Complementos                                                 |
| Carpetas de proyectos existentes          | Proyectos que usan las mismas carpetas                         |
| Memorias de proyectos de Claude Code | [Memorias](/es-419/codex/customization/memories)               |
| Chats de los últimos 30 días       | Chats de ChatGPT                                           |
| Configuración del servidor MCP          | [Configuración de MCP de Codex](/es-419/codex/extend/mcp)            |
| Hooks                             | [Hooks de Codex](/es-419/codex/hooks)                             |
| Comandos slash                    | [Habilidades](/es-419/codex/build-skills)                           |
| Subagentes                         | [Subagentes de Codex](/es-419/codex/agent-configuration/subagents) |

## Completar la configuración después de importar

Cuando termina la importación, la app muestra una tarjeta de estado en la esquina inferior izquierda.
Si un complemento importado o una conexión importada aún requiere configuración, la tarjeta lo indica.

Cuando la app indique que un elemento requiere atención, selecciona **Finalizar** y sigue las
indicaciones para completar la configuración.

## Qué revisar después de importar

Revisa la configuración importada antes de confiar en ella, en especial:

- Restricciones o permisos para usar herramientas en las habilidades y los agentes importados.
- La configuración de servidores MCP que use autenticación personalizada, encabezados, variables
de entorno o transportes. Es posible que debas volver a iniciar sesión.
- Hooks cuyo comportamiento podría ser diferente después de la importación.
- Complementos, marketplaces u otros elementos de configuración que requieran seguimiento manual.
- Plantillas de prompts o prompts con formato de comando que dependen de argumentos, de la interpolación del shell
o de marcadores de posición para rutas de archivo.

## Después de importar

Una vez que finalice la importación, abre uno de tus proyectos importados y continúa desde
allí. Consulta [Usa ChatGPT](/es-419/codex/use-chatgpt) para obtener orientación sobre cómo iniciar tu
siguiente tarea.

<!-- source: https://learn.chatgpt.com/es-419/docs/agent-configuration/agents-md -->

Codex lee los archivos `AGENTS.md` antes de comenzar cualquier tarea. Al combinar las instrucciones globales con instrucciones específicas del proyecto que tienen prioridad, puedes comenzar cada tarea con expectativas coherentes, sin importar qué repositorio abras.

## Cómo encuentra Codex las instrucciones

Codex crea una cadena de instrucciones al iniciarse (una vez por ejecución; en la TUI, esto suele significar una vez por cada sesión iniciada). La búsqueda sigue este orden de prioridad:

1. **Ámbito global:** en el directorio de inicio de Codex (la ubicación predeterminada es `~/.codex`, a menos que definas `CODEX_HOME`), Codex lee `AGENTS.override.md` si existe. De lo contrario, Codex lee `AGENTS.md`. Codex solo usa el primer archivo que no esté vacío en este nivel.
2. **Ámbito del proyecto:** desde la raíz del proyecto (por lo general, la raíz de Git), Codex recorre la ruta hasta llegar al directorio de trabajo actual. Si Codex no encuentra la raíz del proyecto, solo revisa el directorio actual. En cada directorio de la ruta, busca `AGENTS.override.md`, luego `AGENTS.md` y después cualquiera de los nombres alternativos definidos en `project_doc_fallback_filenames`. Codex incluye como máximo un archivo por directorio.
3. **Orden de combinación:** Codex concatena los archivos desde la raíz hacia los subdirectorios y los une con líneas en blanco. Los archivos más cercanos al directorio actual tienen prioridad sobre las instrucciones anteriores porque aparecen después en el prompt combinado.

Codex omite los archivos vacíos y deja de agregar archivos cuando el tamaño combinado alcanza el límite definido por `project_doc_max_bytes` (32 KiB de forma predeterminada). Para obtener más información sobre estas opciones de configuración, consulta [Detección de instrucciones del proyecto](/es-419/codex/config-file/config-advanced#project-instructions-discovery). Aumenta el límite o divide las instrucciones entre directorios anidados cuando llegues al máximo.

## Crear instrucciones globales

Crea valores predeterminados persistentes en tu directorio de inicio de Codex para que cada repositorio herede tus convenciones de trabajo.

1. Asegúrate de que el directorio exista:

   ```bash
   mkdir -p ~/.codex

2. Crea `~/.codex/AGENTS.md` con preferencias reutilizables:

   ```md
   # ~/.codex/AGENTS.md

   ## Working agreements

   - Always run `npm test` after modifying JavaScript files.
   - Prefer `pnpm` when installing dependencies.
   - Ask for confirmation before adding new production dependencies.

3. Ejecuta Codex desde cualquier directorio para confirmar que carga el archivo:

   ```bash
   codex --ask-for-approval never "Summarize the current instructions."

   Resultado esperado: Codex cita los elementos de `~/.codex/AGENTS.md` antes de proponer tareas.

Usa `~/.codex/AGENTS.override.md` cuando necesites reemplazar temporalmente las instrucciones globales sin eliminar el archivo base. Elimina el archivo de reemplazo para restablecer las instrucciones compartidas.

## Organizar las instrucciones del proyecto por niveles

Los archivos a nivel del repositorio mantienen a Codex al tanto de las convenciones del proyecto sin impedir que herede tus valores predeterminados globales.

1. En la raíz del repositorio, agrega un archivo `AGENTS.md` que incluya la configuración básica:

   ```md
   # AGENTS.md

   ## Repository expectations

   - Run `npm run lint` before opening a pull request.
   - Document public utilities in `docs/` when you change behavior.

2. Agrega archivos de reemplazo en directorios anidados cuando determinados equipos necesiten reglas diferentes. Por ejemplo, dentro de `services/payments/`, crea `AGENTS.override.md`:

   ```md
   # services/payments/AGENTS.override.md

   ## Payments service rules

   - Use `make test-payments` instead of `npm test`.
   - Never rotate API keys without notifying the security channel.

3. Inicia Codex desde el directorio de pagos:

   ```bash
   codex --cd services/payments --ask-for-approval never "List the instruction sources you loaded."

   Resultado esperado: Codex muestra primero el archivo global, después el archivo `AGENTS.md` de la raíz del repositorio y, al final, el archivo de reemplazo de pagos.

Codex deja de buscar cuando llega al directorio actual, así que coloca los archivos de reemplazo lo más cerca posible de donde se realiza el trabajo especializado.

Este es un repositorio de ejemplo después de agregar un archivo global y uno de reemplazo específico de pagos:

## Agregar reglas de revisión de código

Para la [revisión de código de Codex en GitHub](/es-419/codex/third-party/github#customize-what-codex-reviews),
agrega una sección `## Code Review Rules` al archivo `AGENTS.md` más cercano al código al que se
aplican las reglas. Coloca las verificaciones de todo el repositorio en la raíz y, para cada servicio, las
verificaciones específicas en un archivo anidado.

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Mantén las reglas concisas, explica qué comportamiento se debe señalar y cuáles son las alternativas seguras o
excepciones, y reserva las verificaciones de formato y lint para CI. Consulta [Personalizar lo que
revisa Codex](/es-419/codex/third-party/github#customize-what-codex-reviews) para obtener
orientación sobre la configuración y la redacción de reglas.

## Personalizar los nombres de archivo alternativos

Si tu repositorio ya usa otro nombre de archivo (por ejemplo, `TEAM_GUIDE.md`), agrégalo a la lista de nombres alternativos para que Codex lo trate como un archivo de instrucciones.

1. Edita la configuración de Codex:

   ```toml
   # ~/.codex/config.toml
   project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
   project_doc_max_bytes = 65536

2. Reinicia Codex o ejecuta un comando nuevo para que se cargue la configuración actualizada.

Ahora Codex busca estos archivos en cada directorio, en el siguiente orden: `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md`. Los nombres de archivo que no aparecen en esta lista se ignoran durante la búsqueda de instrucciones. El límite de bytes más alto permite combinar más instrucciones antes de que se trunquen.

Una vez configurada la lista de nombres alternativos, Codex trata los archivos alternativos como instrucciones:

Define la variable de entorno `CODEX_HOME` cuando quieras usar un perfil diferente, como un usuario de automatización específico del proyecto:

```bash
CODEX_HOME=$(pwd)/.codex codex exec "List active instruction sources"

Resultado esperado: la salida enumera los archivos con rutas relativas al directorio `.codex` personalizado.

## Verificar la configuración

- Ejecuta `codex --ask-for-approval never "Summarize the current instructions."` desde la raíz de un repositorio. Codex debería mostrar las instrucciones de los archivos globales y del proyecto según el orden de prioridad.
- Usa `codex --cd subdir --ask-for-approval never "Show which instruction files are active."` para confirmar que los archivos de reemplazo anidados sustituyen las reglas más generales.
- Para auditar qué archivos de instrucciones cargó Codex, habilita un registro de la TUI en texto sin formato con `codex -c log_dir=./.codex-log` y revisa `./.codex-log/codex-tui.log`, o inspecciona el archivo `session-*.jsonl` más reciente si habilitaste el registro de sesiones.
- Si las instrucciones parecen desactualizadas, reinicia Codex en el directorio de destino. Codex vuelve a crear la cadena de instrucciones en cada ejecución (y al inicio de cada sesión de la TUI), por lo que no hay ninguna caché que debas borrar manualmente.

## Solucionar problemas con la detección de instrucciones

- **No se carga nada:** verifica que estés en el repositorio correcto y que `codex status` muestre la raíz del espacio de trabajo que esperas. Asegúrate de que los archivos de instrucciones tengan contenido; Codex ignora los archivos vacíos.
- **Aparecen instrucciones incorrectas:** busca un archivo `AGENTS.override.md` en un nivel superior del árbol de directorios o dentro de tu directorio de inicio de Codex. Cámbiale el nombre o elimínalo para volver a usar el archivo estándar.
- **Codex ignora los nombres alternativos:** confirma que incluiste los nombres en `project_doc_fallback_filenames` sin errores tipográficos y, luego, reinicia Codex para que se aplique la configuración actualizada.
- **Instrucciones truncadas:** aumenta `project_doc_max_bytes` o divide los archivos grandes entre directorios anidados para mantener intactas las instrucciones esenciales.
- **Confusión con el perfil:** ejecuta `echo $CODEX_HOME` antes de iniciar Codex. Un valor distinto del predeterminado hace que Codex use un directorio de inicio diferente del que editaste.

## Próximos pasos

- Visita el sitio web oficial de [AGENTS.md](https://agents.md) para obtener más información.
- Consulta [Diseño de prompts para Codex](/es-419/codex/prompting) para conocer patrones de conversación que se complementan bien con las instrucciones persistentes.

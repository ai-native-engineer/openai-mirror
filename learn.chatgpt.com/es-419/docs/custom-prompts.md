<!-- source: https://learn.chatgpt.com/es-419/docs/custom-prompts -->

Los prompts personalizados están en desuso. Usa [habilidades](/es-419/codex/build-skills) para crear instrucciones reutilizables
  que Codex pueda invocar explícita o implícitamente.

Los prompts personalizados (en desuso) permiten convertir archivos Markdown en prompts reutilizables que puedes invocar como comandos slash tanto en la CLI de Codex como en la extensión para IDE de Codex.

Los prompts personalizados deben invocarse de forma explícita y se almacenan en el directorio de inicio local de Codex (por ejemplo, `~/.codex`), por lo que no se comparten mediante tu repositorio. Si quieres compartir un prompt (o que Codex lo invoque implícitamente), [usa habilidades](/es-419/codex/build-skills).

1. Crea el directorio de prompts:

   ```bash
   mkdir -p ~/.codex/prompts

2. Crea `~/.codex/prompts/draftpr.md` con instrucciones reutilizables:

   ```markdown
   ---
   description: Prep a branch, commit, and open a draft PR
   argument-hint: [FILES=<paths>] [PR_TITLE="<title>"]
   ---

   Create a branch named `dev/<feature_name>` for this work.
   If files are specified, stage them first: $FILES.
   Commit the staged changes with a clear message.
   Open a draft PR on the same branch. Use $PR_TITLE when supplied; otherwise write a concise summary yourself.

3. Reinicia Codex para que cargue el nuevo prompt (reinicia la sesión de la CLI y, si usas la extensión para IDE, vuelve a cargarla).

Resultado esperado: al escribir `/prompts:draftpr` en el menú de comandos slash, aparece tu comando personalizado, junto con la descripción del encabezado YAML e indicaciones de que los archivos y el título del PR son opcionales.

## Agregar metadatos y argumentos

Codex lee los metadatos del prompt y resuelve los marcadores de posición al iniciar la siguiente sesión.

- **Descripción:** Se muestra debajo del nombre del comando en la ventana emergente. Defínela como `description:` en el encabezado YAML.
- **Indicación de argumentos:** Documenta los parámetros esperados con `argument-hint: KEY=<value>`.
- **Marcadores de posición posicionales:** Los marcadores de `$1` a `$9` se sustituyen por los argumentos que proporcionas después del comando, separados por espacios. `$ARGUMENTS` los incluye todos.
- **Marcadores de posición con nombre:** Usa nombres en mayúsculas, como `$FILE` o `$TICKET_ID`, y proporciona los valores con el formato `KEY=value`. Pon entre comillas los valores que contengan espacios (por ejemplo, `FOCUS="loading state"`).
- **Signos de dólar literales:** Escribe `$$` para generar un único `$` en el prompt expandido.

Después de editar los archivos de prompts, reinicia Codex o abre un chat nuevo para que se carguen los cambios. Codex ignora los archivos que no sean Markdown en el directorio de prompts.

## Invocar y administrar comandos personalizados

1. En Codex (ya sea en la CLI o en la extensión para IDE), escribe `/` para abrir el menú de comandos slash.
2. Escribe `prompts:` o el nombre del prompt, por ejemplo, `/prompts:draftpr`.
3. Proporciona los argumentos obligatorios:

   ```text
   /prompts:draftpr FILES="src/pages/index.astro src/lib/api.ts" PR_TITLE="Add hero animation"

4. Presiona Enter para enviar las instrucciones expandidas (omite cualquiera de los dos argumentos si no hace falta).

Resultado esperado: Codex expande el contenido de `draftpr.md`, reemplaza los marcadores de posición por los argumentos que proporcionaste y luego envía el resultado como mensaje.

Administra los prompts editando o eliminando archivos en `~/.codex/prompts/`. Codex solo analiza los archivos Markdown del nivel superior de esa carpeta, así que coloca cada prompt personalizado directamente en `~/.codex/prompts/` y no en subdirectorios.

<!-- source: https://learn.chatgpt.com/es-419/docs/agent-configuration/rules -->

Usa reglas para controlar qué comandos puede ejecutar Codex fuera del sandbox.

Las reglas son experimentales y pueden cambiar.

## Crear un archivo de reglas

1. Crea un archivo `.rules` en una carpeta `rules/` junto a una capa de configuración activa (por ejemplo, `~/.codex/rules/default.rules`).
2. Agrega una regla. En este ejemplo, se solicita confirmación antes de permitir que `gh pr view` se ejecute fuera del sandbox.

   ```python
   # Prompt before running commands with the prefix `gh pr view` outside the sandbox.
   prefix_rule(
       # The prefix to match.
       pattern = ["gh", "pr", "view"],

       # The action to take when Codex requests to run a matching command.
       decision = "prompt",

       # Optional rationale for why this rule exists.
       justification = "Viewing PRs is allowed with approval",

       # `match` and `not_match` are optional "inline unit tests" where you can
       # provide examples of commands that should (or should not) match this rule.
       match = [
           "gh pr view 7888",
           "gh pr view --repo openai/codex",
           "gh pr view 7888 --json title,body,comments",
       ],
       not_match = [
           # Does not match because the `pattern` must be an exact prefix.
           "gh pr --repo openai/codex view 7888",
       ],
   )

3. Reinicia Codex.

Al iniciarse, Codex busca `rules/` en cada capa de configuración activa, incluidas las ubicaciones de [Configuración del equipo](/es-419/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config) y la capa del usuario en `~/.codex/rules/`. Las reglas locales del proyecto ubicadas en `<repo>/.codex/rules/` solo se cargan cuando la capa `.codex/` del proyecto es de confianza.

Cuando agregas un comando a la lista de permitidos en la TUI, Codex escribe en la capa del usuario, en `~/.codex/rules/default.rules`, para que en futuras ejecuciones pueda omitir la solicitud de confirmación.

Cuando las aprobaciones inteligentes están habilitadas (como ocurre de forma predeterminada), Codex puede proponerte una entrada
`prefix_rule` durante las solicitudes de escalamiento. Revisa el prefijo sugerido
con atención antes de aceptarlo.

Los administradores también pueden imponer entradas `prefix_rule` restrictivas desde
[`requirements.toml`](/es-419/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

## Comprender los campos de las reglas

`prefix_rule()` admite los siguientes campos:

- `pattern` **(obligatorio)**: una lista no vacía que define el prefijo con el que debe coincidir el comando. Cada elemento puede ser:
  - Una cadena literal (por ejemplo, `"pr"`).
  - Una unión de literales (por ejemplo, `["view", "list"]`) para hacer coincidir cualquiera de varias alternativas en esa posición del argumento.
- `decision` **(el valor predeterminado es `"allow"`)**: la acción que se realiza cuando hay una coincidencia con la regla. Si hay coincidencias con más de una regla, Codex aplica la decisión más restrictiva (`forbidden` \> `prompt` \> `allow`).
  - `allow`: ejecuta el comando fuera del sandbox sin solicitar confirmación.
  - `prompt`: solicita confirmación antes de cada invocación que coincida con la regla.
  - `forbidden`: bloquea la solicitud sin solicitar confirmación.
- `justification` **(opcional)**: un motivo para la regla que no esté vacío y sea legible para las personas. Codex puede mostrarlo en las solicitudes de aprobación o en los mensajes de rechazo. Cuando uses `forbidden`, incluye una alternativa recomendada en la justificación cuando corresponda (por ejemplo, `"Use \`rg\` en lugar de \`grep\`."\`).
- `match` y `not_match` **(el valor predeterminado es `[]`)**: ejemplos que Codex valida cuando carga tus reglas. Úsalos para detectar errores antes de que una regla entre en vigor.

Cuando Codex considera ejecutar un comando, compara la lista de argumentos del comando con `pattern`. Internamente, Codex trata el comando como una lista de argumentos (como la que recibe `execvp(3)`).

## Wrappers de shell y comandos compuestos

Algunas herramientas agrupan varios comandos de shell en una sola invocación, por ejemplo:

```text
["bash", "-lc", "git add . && rm -rf /"]

Como este tipo de comando puede ocultar varias acciones dentro de una sola cadena, Codex aplica un tratamiento especial a `bash -lc`, `bash -c` y sus equivalentes en `zsh` / `sh`.

### Cuando Codex puede dividir el script de forma segura

Si el script de shell es una cadena lineal de comandos que cumple estas condiciones:

- solo usa palabras simples (sin expansión de variables ni `VAR=...`, `$FOO`, `*`, etc.)
- los comandos están unidos mediante operadores seguros (`&&`, `||`, `;` o `|`)

en ese caso, Codex lo analiza (con tree-sitter) y lo divide en comandos individuales antes de aplicar tus reglas.

El script anterior se interpreta como dos comandos independientes:

- `["git", "add", "."]`
- `["rm", "-rf", "/"]`

Luego, Codex evalúa cada comando según tus reglas y prevalece el resultado más restrictivo.

Aunque permitas `pattern=["git", "add"]`, Codex no permitirá automáticamente `git add . && rm -rf /`, porque la parte `rm -rf /` se evalúa por separado e impide que se permita automáticamente toda la invocación.

Esto impide que se introduzcan comandos peligrosos de forma encubierta junto con otros seguros.

### Cuando Codex no divide el script

Si el script usa características más avanzadas del shell, como:

- redirección (`>`, `>>`, `<`)
- sustituciones (`$(...)`, `...`)
- variables de entorno (`FOO=bar`)
- patrones con comodines (`*`, `?`)
- flujo de control (`if`, `for`, `&&` con asignaciones, etc.)

entonces Codex no intenta interpretarlo ni dividirlo.

En esos casos, toda la invocación se trata como:

```text
["bash", "-lc", "<full script>"]

y tus reglas se aplican a esa **única** invocación.

Con este tratamiento, obtienes la seguridad que ofrece evaluar cada comando por separado cuando hacerlo es seguro y un comportamiento conservador cuando no lo es.

## Probar un archivo de reglas

Usa `codex execpolicy check` para probar cómo se aplican tus reglas a un comando:

```shell
codex execpolicy check --pretty \
  --rules ~/.codex/rules/default.rules \
  -- gh pr view 7888 --json title,body,comments

El comando genera una salida JSON que muestra la decisión más restrictiva y las reglas coincidentes, incluidos los valores de `justification` de esas reglas. Usa `--rules` más de una vez para combinar archivos y agrega `--pretty` para dar formato a la salida.

## Comprender el lenguaje de las reglas

El formato de archivo `.rules` usa `Starlark` (consulta la [especificación del lenguaje](https://github.com/bazelbuild/starlark/blob/master/spec.md)). Su sintaxis es similar a la de Python, pero este lenguaje está diseñado para ejecutarse de forma segura: el motor de reglas puede ejecutar archivos en este formato sin efectos secundarios (por ejemplo, modificar el sistema de archivos).

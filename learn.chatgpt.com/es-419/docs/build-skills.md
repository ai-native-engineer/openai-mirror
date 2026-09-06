<!-- source: https://learn.chatgpt.com/es-419/docs/build-skills -->

Usa habilidades de agentes para ampliar ChatGPT y Codex con capacidades específicas para cada tarea. Una
habilidad reúne instrucciones, recursos y scripts opcionales para que cualquiera de los dos productos
pueda seguir un flujo de trabajo de forma confiable. Las habilidades se basan en el
[estándar abierto de habilidades de agentes](https://agentskills.io).

Las habilidades son el formato de creación de flujos de trabajo reutilizables. Los complementos distribuyen
habilidades y conectores reutilizables mediante el directorio universal de complementos que comparten
ChatGPT y Codex. Los complementos funcionan en Chat y Work en ChatGPT en la web,
en equipos de escritorio y dispositivos móviles; en Codex, dentro de la aplicación de escritorio de ChatGPT; y mediante Codex
CLI. Usa habilidades para diseñar el flujo de trabajo y luego empaquétalo como un
[complemento](https://developers.openai.com/plugins/build/plugins) cuando quieras que
otras personas lo instalen.

Las habilidades independientes están disponibles en la aplicación de escritorio de ChatGPT, Codex CLI y la extensión
para IDE. Las habilidades incluidas en complementos también están disponibles en Chat y Work en
ChatGPT en la web, en equipos de escritorio y dispositivos móviles.

En la aplicación de escritorio de ChatGPT, abre **Habilidades** en la barra lateral para ver y explorar las habilidades
creadas en todos tus proyectos.

  
    
  

Las habilidades usan la **divulgación progresiva** para administrar el contexto de manera eficiente. ChatGPT y
Codex comienzan con el nombre y la descripción de cada habilidad; después, cargan las instrucciones completas de
`SKILL.md` cuando deciden usar esa habilidad.

En Codex, la lista inicial también incluye la ruta del archivo de cada habilidad. Para evitar
que ocupe el espacio destinado al resto del prompt, esta lista usa como máximo el 2 % de la ventana de
contexto del modelo, o 8 000 caracteres cuando se desconoce la ventana de contexto. Si hay muchas
habilidades instaladas, Codex acorta primero sus descripciones. Con conjuntos grandes de
habilidades, Codex puede omitir algunas de la lista inicial y mostrar una advertencia.

Este presupuesto se aplica únicamente a la lista inicial de habilidades. Cuando Codex selecciona una habilidad, de todas formas lee las instrucciones completas de SKILL.md correspondientes a esa habilidad.

Una habilidad es un directorio que contiene un archivo `SKILL.md`, además de scripts y referencias opcionales. El archivo `SKILL.md` debe incluir `name` y `description`.

<a id="how-codex-uses-skills"></a>

## Cómo usan ChatGPT y Codex las habilidades

ChatGPT y Codex pueden activar habilidades de dos maneras:

1. **Invocación explícita:** incluye la habilidad directamente en tu prompt. En
   ChatGPT, escribe `@` para seleccionar una habilidad. En Codex CLI o la extensión para IDE, ejecuta
`/skills` o escribe `$` para mencionar una habilidad.
2. **Invocación implícita:** ChatGPT o Codex pueden elegir una habilidad cuando tu tarea
   coincide con el campo `description` de esa habilidad.

Como la coincidencia implícita depende de `description`, redacta descripciones concisas
con un alcance y límites claros. Coloca al principio el caso de uso clave y las palabras de activación
para que un host pueda seguir identificando la habilidad aunque se acorten las descripciones.

## Crear una habilidad

Si ya conoces el flujo de trabajo y es más fácil mostrarlo que describirlo, usa
[Grabar y reproducir](/es-419/codex/extend/record-and-replay). La grabadora captura el
flujo de trabajo, inspecciona los pasos y genera el borrador de una habilidad reutilizable a partir de la
demostración.

Si prefieres describir la habilidad, usa el creador integrado. En ChatGPT
Work, invócalo como `@skill-creator`. En Codex, invócalo así:

```text
$skill-creator

El creador pregunta qué hace la habilidad, cuándo debe activarse y si debe limitarse a instrucciones o incluir scripts. La opción predeterminada es usar solo instrucciones.

También puedes crear una habilidad de forma manual mediante una carpeta que contenga un archivo `SKILL.md`:

```md
---
name: skill-name
description: Explain exactly when this skill should and should not trigger.
---

Skill instructions for ChatGPT or Codex to follow.

Codex detecta automáticamente los cambios en las habilidades. Si una actualización no aparece, reinicia Codex.

<a id="where-to-save-skills"></a>

## Dónde carga Codex las habilidades locales

Codex lee las habilidades desde ubicaciones del repositorio, del usuario, del administrador y del sistema. En los repositorios, Codex busca `.agents/skills` en cada directorio comprendido entre el directorio de trabajo actual y la raíz del repositorio. Si dos habilidades comparten el mismo `name`, Codex no las combina; ambas pueden aparecer en los selectores de habilidades.

| Alcance de la habilidad | Ubicación                                                                                                  | Uso sugerido                                                                                                                                                                                        |
| :---------- | :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `REPO`      | `$CWD/.agents/skills` <br /> Directorio de trabajo actual: donde inicias Codex.                           | Si estás en un repositorio o un entorno de código, los equipos pueden incorporar al repositorio habilidades pertinentes para una carpeta de trabajo. Por ejemplo, habilidades que solo sean pertinentes para un microservicio o módulo.                              |
| `REPO`      | `$CWD/../.agents/skills` <br /> Una carpeta situada por encima de CWD cuando inicias Codex dentro de un repositorio Git.         | Si estás en un repositorio con carpetas anidadas, las organizaciones pueden incorporar al repositorio habilidades pertinentes para un área compartida ubicada en una carpeta superior.                                                                       |
| `REPO`      | `$REPO_ROOT/.agents/skills` <br /> La carpeta raíz de nivel superior cuando inicias Codex dentro de un repositorio Git. | Si estás en un repositorio con carpetas anidadas, las organizaciones pueden incorporar al repositorio habilidades pertinentes para todas las personas que lo usan. Estas sirven como habilidades raíz disponibles para cualquier subcarpeta del repositorio. |
| `USER`      | `$HOME/.agents/skills` <br /> Cualquier habilidad almacenada en la carpeta personal del usuario.                         | Úsala para seleccionar habilidades pertinentes para un usuario y aplicables a cualquier repositorio en el que trabaje.                                                                                                           |
| `ADMIN`     | `/etc/codex/skills` <br /> Cualquier habilidad almacenada en la máquina o el contenedor, en una ubicación compartida del sistema. | Úsala para scripts del SDK y automatización, así como para guardar habilidades de administrador predeterminadas disponibles para cada usuario de la máquina.                                                                                     |
| `SYSTEM`    | OpenAI las incluye con Codex.                                                                             | Habilidades útiles para un público amplio, como las habilidades skill-creator y plan. Están disponibles para todos al iniciar Codex.                                                                   |

Codex admite carpetas de habilidades con enlaces simbólicos y sigue el destino del enlace simbólico al explorar estas ubicaciones.

Estas ubicaciones sirven para la creación y detección local. Cuando quieras
distribuir habilidades reutilizables más allá de un único repositorio o, de manera opcional, agruparlas con
conectores, usa [complementos](https://developers.openai.com/plugins/build/plugins).

## Distribuir habilidades con complementos

Trabajar directamente con carpetas de habilidades es lo más adecuado para la creación local y los flujos de trabajo limitados a un repositorio. Si
quieres distribuir una habilidad reutilizable, agrupar dos o más habilidades o
distribuir una habilidad junto con un conector, empaqueta todo como un
[complemento](https://developers.openai.com/plugins/build/plugins).

Los complementos pueden incluir una o más habilidades. También pueden agrupar de forma opcional
conexiones registradas a servidores MCP, la configuración integrada de servidores MCP y
recursos de presentación en un solo paquete.

## Instalar habilidades seleccionadas para uso local

Para agregar habilidades seleccionadas, además de las integradas, a tu configuración local de Codex, usa `$skill-installer`. Por ejemplo, para instalar la habilidad `$linear`:

```bash
$skill-installer linear

También puedes pedirle al instalador que descargue habilidades de otros repositorios.
Codex detecta automáticamente las habilidades recién instaladas; si alguna no aparece,
reinicia Codex.

Usa este método para la configuración y la experimentación locales. Para distribuir tus
propias habilidades de forma reutilizable, opta por los complementos.

## Habilitar o deshabilitar habilidades locales de Codex

Usa entradas `[[skills.config]]` en `~/.codex/config.toml` para deshabilitar una habilidad sin eliminarla:

```toml
[[skills.config]]
path = "/path/to/skill/SKILL.md"
enabled = false

Reinicia Codex después de modificar `~/.codex/config.toml`.

## Metadatos opcionales

Agrega `agents/openai.yaml` para configurar los metadatos de la interfaz de usuario en la [aplicación de escritorio de ChatGPT](/es-419/codex/app), establecer la política de invocación y declarar dependencias de herramientas para que la experiencia de uso de la habilidad sea más fluida.

```yaml
interface:
  display_name: "Optional user-facing name"
  short_description: "Optional user-facing description"
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
  brand_color: "#3B82F6"
  default_prompt: "Optional surrounding prompt to use the skill with"

policy:
  allow_implicit_invocation: false

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      description: "OpenAI Docs MCP server"
      transport: "streamable_http"
      url: "https://developers.openai.com/mcp"

`allow_implicit_invocation` (valor predeterminado: `true`): cuando se establece en `false`, Codex no invoca implícitamente la habilidad a partir del prompt del usuario; la invocación explícita con `$skill` sigue funcionando.

## Prácticas recomendadas

- Mantén cada habilidad enfocada en una sola tarea.
- Prefiere usar instrucciones en lugar de scripts, a menos que necesites un comportamiento determinista o herramientas externas.
- Redacta pasos en imperativo con entradas y salidas explícitas.
- Prueba los prompts con la descripción de la habilidad para confirmar que se active correctamente.

Para ver más ejemplos, consulta
[reparación de CI de GitHub](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci),
[PDF](https://github.com/openai/skills/tree/main/skills/.curated/pdf),
[Linear](https://github.com/openai/skills/tree/main/skills/.curated/linear),
[openai/skills](https://github.com/openai/skills) y la
[especificación de habilidades de agentes](https://agentskills.io/specification). Para
distribuir habilidades instalables, prefiere los [complementos](https://developers.openai.com/plugins/build/plugins).

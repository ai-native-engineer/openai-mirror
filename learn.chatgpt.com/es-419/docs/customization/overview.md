<!-- source: https://learn.chatgpt.com/es-419/docs/customization/overview -->

La personalización te permite adaptar Codex a la forma de trabajar de tu equipo.

En Codex, la personalización consta de varias capas que funcionan en conjunto:

- **Directrices del proyecto (`AGENTS.md`)** para instrucciones persistentes
- **[Memorias](/es-419/codex/customization/memories)** para conservar contexto útil obtenido de trabajos anteriores
- **Habilidades** para flujos de trabajo reutilizables y conocimientos especializados del dominio
- **[MCP](/es-419/codex/extend/mcp)** para acceder a herramientas externas y sistemas compartidos
- **[Subagentes](/es-419/codex/agent-configuration/subagents)** para delegar tareas a subagentes especializados

Estas capas se complementan, no compiten entre sí. `AGENTS.md` define el comportamiento, las memorias
conservan el contexto local para trabajos futuros, las habilidades encapsulan procesos repetibles y
[MCP](/es-419/codex/extend/mcp) conecta Codex con sistemas externos al espacio de trabajo local.

## Guía de AGENTS

`AGENTS.md` proporciona a Codex directrices duraderas para el proyecto que acompañan a tu repositorio y se aplican antes de que el agente empiece a trabajar. Mantén el archivo breve.

Úsalo para definir las reglas que quieres que Codex siga cada vez que trabaje en un repositorio, por ejemplo:

- Comandos de compilación y pruebas
- Criterios para las revisiones
- Convenciones específicas del repositorio
- Instrucciones específicas para cada directorio

Cuando el agente haga suposiciones incorrectas sobre tu base de código, corrígelas en `AGENTS.md` y pídele que actualice `AGENTS.md` para que la corrección perdure. Trátalo como un ciclo de retroalimentación.

**Actualizar `AGENTS.md`:** empieza solo con las instrucciones esenciales. Convierte los comentarios recurrentes de las revisiones en instrucciones, coloca las directrices en el directorio más cercano donde se apliquen y dile al agente que actualice `AGENTS.md` cada vez que corrijas algo, para que las sesiones futuras incorporen la corrección.

### Cuándo actualizar `AGENTS.md`

- **Errores repetidos**: si el agente comete el mismo error repetidamente, agrega una regla.
- **Demasiada lectura**: si encuentra los archivos correctos pero lee demasiados documentos, agrega indicaciones sobre qué debe consultar primero (qué directorios o archivos priorizar).
- **Comentarios recurrentes en PR**: si haces el mismo comentario más de una vez, formalízalo como una instrucción.
- **En GitHub**: en un comentario de un Pull Request, etiqueta a `@codex` con una solicitud (por ejemplo, `@codex add this to AGENTS.md`) para delegar la actualización a un chat en la nube.
- **Automatizar las comprobaciones de divergencias**: usa [tareas programadas](/es-419/codex/automations) para ejecutar comprobaciones periódicas (por ejemplo, a diario) que detecten vacíos en las directrices y sugieran qué agregar a `AGENTS.md`.

Complementa `AGENTS.md` con infraestructura que haga cumplir esas reglas: los hooks de pre-commit, los linters y los verificadores de tipos detectan problemas antes de que los veas, así el sistema mejora su capacidad para prevenir errores recurrentes.

Codex puede cargar directrices desde varias ubicaciones: un archivo global en tu directorio de inicio de Codex (para ti como desarrollador) y archivos específicos del repositorio que los equipos pueden incluir en el control de versiones. Los archivos más cercanos al directorio de trabajo tienen prioridad.
Usa el archivo global para definir cómo se comunica Codex contigo (por ejemplo, el estilo de revisión, el nivel de detalle y los valores predeterminados), y mantén los archivos del repositorio centrados en las reglas del equipo y de la base de código.

[Instrucciones personalizadas con AGENTS.md](/es-419/codex/agent-configuration/agents-md)

## Habilidades

Las habilidades ofrecen a Codex capacidades reutilizables para flujos de trabajo repetibles.
Las habilidades suelen ser la mejor opción para los flujos de trabajo reutilizables porque admiten instrucciones, scripts y referencias más completos, y se pueden reutilizar en distintas tareas.
Las habilidades se cargan y son visibles para el agente (al menos sus metadatos), de modo que Codex puede encontrarlas y seleccionarlas de forma implícita. Esto permite mantener disponibles flujos de trabajo elaborados sin saturar el contexto desde el principio.

Usa carpetas de habilidades para crear y perfeccionar flujos de trabajo de forma local. Si ya existe un complemento
para ese flujo de trabajo, instálalo primero para reutilizar una configuración comprobada. Cuando
quieras distribuir tu propio flujo de trabajo entre varios equipos o combinarlo con
conectores, empaquétalo como [complemento](/es-419/codex/build-plugins). Las habilidades siguen siendo el
formato de creación; los complementos son la unidad de distribución instalable.

Una habilidad suele consistir en un archivo `SKILL.md`, además de scripts, referencias y recursos opcionales.

El directorio de la habilidad puede incluir una carpeta `scripts/` con scripts de CLI que Codex invoca como parte del flujo de trabajo (por ejemplo, para cargar datos iniciales o ejecutar validaciones). Cuando el flujo de trabajo necesite sistemas externos (gestores de incidencias, herramientas de diseño o servidores de documentación), combina la habilidad con [MCP](/es-419/codex/extend/mcp).

Ejemplo de `SKILL.md`:

```md
---
name: commit
description: Stage and commit changes in semantic groups. Use when the user wants to commit, organize commits, or clean up a branch before pushing.
---

1. Do not run `git add .`. Stage files in logical groups by purpose.
2. Group into separate commits: feat → test → docs → refactor → chore.
3. Write concise commit messages that match the change scope.
4. Keep each commit focused and reviewable.

Usa las habilidades para:

- Flujos de trabajo repetibles (pasos de lanzamiento, rutinas de revisión y actualizaciones de documentación)
- Conocimientos especializados del equipo
- Procedimientos que requieren ejemplos, referencias o scripts auxiliares

Las habilidades pueden ser globales (en tu directorio de usuario, para ti como desarrollador) o específicas del repositorio (incluidas en `.agents/skills` para tu equipo). Guarda las habilidades del repositorio en `.agents/skills` cuando el flujo de trabajo se aplique a ese proyecto; usa tu directorio de usuario para las habilidades que quieras usar en todos los repositorios.

| Capa  | Global               | Repositorio                                           |
| :----- | :------------------- | :--------------------------------------------- |
| AGENTS | `~/.codex/AGENTS.md` | `AGENTS.md` en la raíz del repositorio o en directorios anidados |
| Habilidades | `~/.agents/skills`   | `.agents/skills` en el repositorio                       |

Codex usa la divulgación progresiva para las habilidades:

- Comienza con los metadatos (`name`, `description`) para identificar las habilidades
- Carga `SKILL.md` solo cuando se selecciona una habilidad
- Lee las referencias o ejecuta los scripts solo cuando es necesario

Las habilidades pueden invocarse explícitamente, y Codex también puede seleccionarlas de forma implícita cuando la tarea coincide con la descripción de la habilidad. Las descripciones claras de las habilidades mejoran la confiabilidad de su activación.

[Crear habilidades](/es-419/codex/build-skills)

## MCP

MCP (Model Context Protocol) es la forma estándar de conectar Codex con herramientas externas y proveedores de contexto.
Resulta especialmente útil para sistemas alojados de forma remota, como Figma, Linear, GitHub o los servicios internos de conocimiento de los que depende tu equipo.

Usa MCP cuando Codex necesite capacidades disponibles fuera del repositorio local, como gestores de incidencias, herramientas de diseño, navegadores o sistemas compartidos de documentación.

Una forma de entenderlo:

- **Host**: Codex
- **Cliente**: la conexión MCP dentro de Codex
- **Servidor**: la herramienta externa o el proveedor de contexto

Los servidores MCP pueden exponer:

- **Herramientas** (acciones)
- **Recursos** (datos legibles)
- **Prompts** (plantillas de prompts reutilizables)

Esta separación te ayuda a evaluar los límites de confianza y de capacidad. Algunos servidores proporcionan principalmente contexto, mientras que otros permiten realizar acciones de gran alcance.

En la práctica, MCP suele ser más útil cuando se combina con habilidades:

- Una habilidad define el flujo de trabajo y especifica las herramientas de MCP que se deben usar

[Model Context Protocol](/es-419/codex/extend/mcp)

## Subagentes

Puedes crear distintos agentes con diferentes roles e indicarles que usen las herramientas de distintas maneras. Por ejemplo, un agente podría ejecutar determinados comandos y configuraciones de prueba, mientras que otro dispone de servidores MCP que recuperan registros de producción para la depuración. Cada subagente se concentra y usa las herramientas adecuadas para su tarea.

[Subagentes](/es-419/codex/agent-configuration/subagents)

## Habilidades y MCP en conjunto

Las habilidades y MCP permiten integrar todo: las habilidades definen flujos de trabajo repetibles y MCP los conecta con herramientas y sistemas externos.
Si una habilidad depende de MCP, declara esa dependencia en `agents/openai.yaml` para que Codex pueda instalarla y configurarla automáticamente (consulta [Crear habilidades](/es-419/codex/build-skills)).

## Siguiente paso

Sigue este orden:

1. [Instrucciones personalizadas con AGENTS.md](/es-419/codex/agent-configuration/agents-md) para que Codex siga las convenciones de tu repositorio. Agrega hooks de pre-commit y linters para hacer cumplir esas reglas.
2. Instala un [complemento](/es-419/codex/plugins) cuando ya exista un flujo de trabajo reutilizable. De lo contrario, crea una [habilidad](/es-419/codex/build-skills) y empaquétala como complemento cuando quieras compartirla.
3. [MCP](/es-419/codex/extend/mcp) cuando los flujos de trabajo necesiten sistemas externos (Linear, GitHub, servidores de documentación, herramientas de diseño).
4. [Subagentes](/es-419/codex/agent-configuration/subagents) cuando estés listo para delegar a subagentes tareas que generen ruido o sean especializadas.

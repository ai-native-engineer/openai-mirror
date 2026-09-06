<!-- source: https://learn.chatgpt.com/es-419/guides/best-practices -->

Si es la primera vez que usas Codex o agentes de codificación en general, esta guía te ayudará a obtener mejores resultados más rápido. Abarca los hábitos fundamentales que hacen que Codex sea más eficaz en la [CLI](/es-419/codex/cli), la [Extensión para IDE](/es-419/codex/ide) y la [app de escritorio de ChatGPT](/es-419/codex/app), desde el diseño de prompts y la planificación hasta la validación, MCP, las habilidades y las tareas programadas.

Codex funciona mejor si lo tratas menos como un asistente para tareas puntuales y más como un compañero de equipo que configuras y mejoras con el tiempo.

Una forma útil de verlo: comienza con el contexto adecuado para la tarea, usa `AGENTS.md` para establecer instrucciones duraderas, configura Codex para que se adapte a tu flujo de trabajo, conecta sistemas externos mediante MCP, convierte el trabajo repetitivo en habilidades y automatiza los flujos de trabajo estables.

## Primer uso eficaz: contexto y prompts

Codex ya es lo suficientemente capaz como para resultar útil incluso si tu prompt no es perfecto. A menudo puedes plantearle un problema difícil con muy poca preparación y aun así obtener un resultado sólido. Un [diseño de prompts](/es-419/codex/prompting) claro no es indispensable para aprovechar Codex, pero sí hace que los resultados sean más confiables, especialmente en bases de código grandes o tareas más críticas.

Si trabajas en un repositorio grande o complejo, lo que marca la mayor diferencia es darle a Codex el contexto adecuado para la tarea y estructurar con claridad lo que quieres que haga.

Un buen punto de partida es incluir cuatro elementos en tu prompt:

- **Objetivo:** ¿qué quieres cambiar o crear?
- **Contexto:** ¿qué archivos, carpetas, documentos, ejemplos o errores son relevantes para esta tarea? Puedes mencionar ciertos archivos con @ para usarlos como contexto.
- **Restricciones:** ¿qué estándares, arquitectura, requisitos de seguridad o convenciones debe seguir Codex?
- **Se considera terminada cuando:** ¿qué condiciones deben cumplirse para dar por terminada la tarea, por ejemplo, que las pruebas pasen, que cambie el comportamiento o que ya no se reproduzca un error?

Esto ayuda a Codex a mantenerse dentro del alcance, hacer menos suposiciones y producir un trabajo más fácil de revisar.

Elige una intensidad de razonamiento según la dificultad de la tarea y prueba cuál funciona mejor para tu flujo de trabajo. La configuración más adecuada varía según el usuario y la tarea.

- Baja para tareas más rápidas y con un alcance bien definido
- Media o Alta para cambios más complejos o tareas de depuración
- Muy alta para tareas largas, con agentes y que exigen mucho razonamiento

  Para proporcionar contexto más rápido, prueba usar el dictado por voz en la app de escritorio de ChatGPT
para indicarle a Codex lo que quieres que haga, en lugar de escribirlo.

## Planificar antes de abordar tareas difíciles

Si la tarea es compleja, ambigua o difícil de describir con claridad, pídele a Codex que la planifique antes de comenzar a escribir código.

Hay varios enfoques que funcionan bien:

**Usa el Modo plan:** para la mayoría de los usuarios, esta es la opción más sencilla y eficaz. El Modo plan permite que Codex recopile contexto, haga preguntas aclaratorias y elabore un plan más sólido antes de comenzar la implementación. Actívalo o desactívalo con `/plan` o <kbd>Mayús</kbd>+<kbd>Tab</kbd>.

**Pídele a Codex que te entreviste:** si tienes una idea general de lo que quieres, pero no sabes bien cómo describirla, pídele a Codex que primero te haga preguntas. Indícale que cuestione tus suposiciones y convierta la idea imprecisa en algo concreto antes de escribir código.

**Usa una plantilla PLANS.md:** para flujos de trabajo más avanzados, puedes configurar Codex para que siga una plantilla `PLANS.md` o una plantilla de plan de ejecución en trabajos de mayor duración o de varios pasos. Para obtener más detalles, consulta la [guía de planes de ejecución](/cookbook/articles/codex_exec_plans).

## Crear instrucciones reutilizables con `AGENTS.md`

Una vez que encuentres un patrón de prompts que funcione, el siguiente paso es dejar de repetirlo manualmente. Ahí es donde entra en juego [AGENTS.md](/es-419/codex/agent-configuration/agents-md).

Piensa en `AGENTS.md` como un README de formato abierto para agentes. Se carga automáticamente en el contexto y es el mejor lugar para especificar cómo debe trabajar Codex en un repositorio para ti y tu equipo.

Un buen archivo `AGENTS.md` incluye:

- estructura del repositorio y directorios importantes
- Cómo ejecutar el proyecto
- Comandos de compilación, pruebas y lint
- Convenciones de ingeniería y expectativas para los PR
- Restricciones y reglas sobre lo que no se debe hacer
- Qué significa que el trabajo esté terminado y cómo verificarlo

El comando slash `/init` de la CLI permite crear rápidamente un archivo `AGENTS.md` inicial en el directorio actual. Es un excelente punto de partida, pero debes editar el resultado para adaptarlo a la forma en que tu equipo compila, prueba, revisa y entrega código.

Puedes crear archivos `AGENTS.md` en distintos niveles: un archivo `AGENTS.md` global con tus valores predeterminados personales, ubicado en `~/.codex`; un archivo en el nivel del repositorio para los estándares compartidos; y archivos más específicos en subdirectorios para las reglas locales. Si existe un archivo más específico en una ubicación más cercana a tu directorio actual, sus instrucciones tienen prioridad.

Mantén un enfoque práctico. Un archivo `AGENTS.md` breve y preciso resulta más útil que un archivo largo lleno de reglas vagas. Comienza con lo básico y agrega reglas nuevas solo después de detectar errores recurrentes.

Si `AGENTS.md` comienza a ser demasiado extenso, mantén el archivo principal conciso y agrega referencias a archivos markdown específicos para cada tarea, por ejemplo, sobre planificación, revisión de código o arquitectura.

  Cuando Codex cometa el mismo error dos veces, pídele que haga una retrospectiva y actualiza
`AGENTS.md`. Así, las instrucciones se mantienen prácticas y se basan en problemas reales.

## Configurar Codex para que se comporte de manera consistente

La configuración es una de las principales formas de hacer que Codex se comporte de manera más consistente entre sesiones e interfaces. Por ejemplo, puedes establecer valores predeterminados para la selección del modelo, el esfuerzo de razonamiento, el modo sandbox, la política de aprobación, los perfiles y la configuración de MCP.

Un buen punto de partida es:

- Guarda las opciones personales predeterminadas en `~/.codex/config.toml` (**Configuración \> Configuración \> Abrir config.toml** en la app de escritorio de ChatGPT)
- Guarda el comportamiento específico del repositorio en `.codex/config.toml`
- Sobrescribe la configuración desde la línea de comandos solo en situaciones puntuales (si usas la CLI)

[`config.toml`](/es-419/codex/config-file/config-basic) es donde defines preferencias duraderas, como los servidores MCP, la configuración de varios agentes y las marcas de funciones. Los valores de reemplazo específicos de cada perfil se guardan en archivos `$CODEX_HOME/profile-name.config.toml` independientes.

Codex incluye un entorno aislado a nivel del sistema operativo y tiene dos controles principales que puedes ajustar. El modo de aprobación determina cuándo Codex te pide permiso para ejecutar un comando, y el modo sandbox determina si Codex puede leer o escribir en el directorio y a qué archivos puede acceder el agente.

Si recién comienzas a usar agentes de codificación, empieza con los permisos predeterminados. Mantén estrictos los controles de aprobación y entorno aislado de forma predeterminada, y flexibiliza los permisos solo para repositorios de confianza o flujos de trabajo específicos cuando haya una necesidad clara.

Ten en cuenta que la CLI, la Extensión para IDE y la app de escritorio de ChatGPT comparten las mismas capas de configuración. Obtén más información en la página de [configuración de ejemplo](/es-419/codex/config-file/config-sample).

  Configura Codex desde el principio para tu entorno real. Muchos problemas de calidad son
en realidad problemas de configuración, como usar un directorio de trabajo incorrecto, no tener acceso de escritura,
utilizar valores predeterminados incorrectos para el modelo o no contar con las herramientas y los conectores necesarios.

## Mejorar la confiabilidad con pruebas y revisión

No te limites a pedirle a Codex que haga un cambio. Pídele que cree pruebas cuando sea necesario, ejecute las verificaciones pertinentes, confirme el resultado y revise el trabajo antes de que lo aceptes.

Codex puede realizar este ciclo por ti, pero solo si sabe qué se considera “bueno”. Esas instrucciones pueden provenir del prompt o de `AGENTS.md`.

Esto puede incluir:

- Escribir o actualizar pruebas para el cambio
- Ejecutar los conjuntos de pruebas adecuados
- Ejecutar las comprobaciones de lint, formato o tipos
- Confirmar que el comportamiento final coincida con la solicitud
- Revisar el diff para detectar errores, regresiones o patrones riesgosos

  Muestra u oculta el panel de diff en la app de escritorio de ChatGPT para [revisar
  los cambios](/es-419/codex/code-review?surface=app) directamente en tu entorno local. Haz clic en una fila específica para
  enviar comentarios que se incorporarán como contexto en el siguiente turno de Codex.

Una opción útil en este caso es el comando slash `/review`, que ofrece varias maneras de revisar código:

- Revisar respecto de una rama base, al estilo de una revisión de PR
- Revisar cambios sin commit
- Revisar un commit
- Usar instrucciones de revisión personalizadas

Si tú y tu equipo tienen un archivo `code_review.md` y hacen referencia a él desde `AGENTS.md`, Codex también puede seguir esas indicaciones durante la revisión. Este es un patrón sólido para los equipos que quieren mantener revisiones coherentes entre repositorios y colaboradores.

Codex no debería limitarse a generar código. Con las instrucciones adecuadas, también puede ayudar a **probarlo, verificarlo y revisarlo**.

Si usas GitHub Cloud, puedes configurar Codex para que ejecute [revisiones de código para tus Pull requests](/es-419/codex/third-party/github). En OpenAI, Codex revisa el 100 % de los Pull requests. Puedes habilitar las revisiones automáticas o hacer que Codex revise el código en respuesta a una mención con @Codex.

## Usar MCP para obtener contexto externo

Usa MCP cuando el contexto que Codex necesita se encuentre fuera del repositorio. Esto permite que Codex se conecte a las herramientas y los sistemas que ya usas, para que no tengas que copiar y pegar constantemente información actualizada en los prompts.

El [Model Context Protocol](/es-419/codex/extend/mcp), o MCP, es un estándar abierto para conectar Codex con herramientas y sistemas externos.

Usa MCP cuando:

- El contexto necesario está fuera del repositorio
- Los datos cambian con frecuencia
- Quieres que Codex use una herramienta en lugar de basarse en instrucciones copiadas y pegadas
- Necesitas una integración repetible entre distintos usuarios o proyectos

Codex admite servidores STDIO y Streamable HTTP con OAuth.

En la app de escritorio de ChatGPT, ve a **Configuración \> Servidores MCP** para ver los servidores personalizados y recomendados. A menudo, Codex puede ayudarte a instalar los servidores que necesitas. Solo tienes que pedírselo. También puedes usar el comando `codex mcp add` en la CLI para agregar tus servidores personalizados con un nombre, una URL y otros detalles.

  Agrega herramientas solo cuando habiliten un flujo de trabajo real. No empieces por integrar
todas las herramientas que usas. Empieza con una o dos que eliminen claramente un ciclo manual
que ya realizas con frecuencia y luego amplía la integración.

## Convertir flujos de trabajo repetibles en habilidades

Cuando un flujo de trabajo se vuelva repetible, deja de depender de prompts largos o de intercambios continuos. Usa una [habilidad](/es-419/codex/build-skills) para agrupar las instrucciones en un archivo `SKILL.md`, junto con el contexto y la lógica complementaria que Codex debe aplicar de manera coherente. Las habilidades funcionan en la CLI, la extensión para IDE y la app de escritorio de ChatGPT.

Limita cada habilidad a una sola tarea. Empieza con 2 o 3 casos de uso concretos, define entradas y salidas claras, y redacta la descripción de modo que explique qué hace la habilidad y cuándo usarla. Incluye los tipos de frases de activación que un usuario usaría realmente.

No intentes abarcar desde el principio todos los casos límite. Empieza con una tarea representativa, haz que funcione bien y luego convierte ese flujo de trabajo en una habilidad para seguir mejorándolo. Incluye scripts o recursos adicionales solo cuando mejoren la confiabilidad.

Una buena regla general: si sigues reutilizando el mismo prompt o corrigiendo el mismo flujo de trabajo, probablemente convenga convertirlo en una habilidad.

Las habilidades son especialmente útiles para tareas recurrentes como:

- Análisis inicial de registros
- Redacción de notas de la versión
- Revisión de PR según una lista de verificación
- Planificación de migraciones
- Resúmenes de telemetría o incidentes
- Flujos de depuración estándar

La habilidad `$skill-creator` es el mejor punto de partida para generar la estructura de la primera versión de una habilidad. Mantén la primera versión en tu entorno local mientras haces ajustes. Cuando esté lista para compartirla de manera general, empaquétala como un [complemento](https://developers.openai.com/plugins/build/plugins). Una de las partes más importantes de una habilidad es la descripción. Debe indicar qué hace la habilidad y cuándo usarla.

  Las habilidades personales se almacenan en `$HOME/.agents/skills`, y las habilidades compartidas por el equipo
  pueden agregarse a `.agents/skills` dentro de un repositorio. Esto es especialmente
  útil para incorporar a nuevos miembros del equipo.

## Usar tareas programadas para el trabajo recurrente

Cuando un flujo de trabajo sea estable, puedes programar Codex para que lo ejecute en segundo plano. En la app de escritorio de ChatGPT, las [tareas programadas](/es-419/codex/automations) te permiten elegir el proyecto, el prompt, la frecuencia y el entorno de ejecución para el trabajo recurrente.

Crea una tarea programada desde la página **Programadas**. Elige el proyecto, el prompt,
la frecuencia y si la tarea se ejecuta en un Git worktree dedicado o en tu entorno
local. El prompt puede invocar habilidades. Obtén más información sobre
[los Git worktrees](/es-419/codex/environments/git-worktrees).

Algunas buenas opciones son:

- Resumir commits recientes
- Buscar posibles errores
- Redactar notas de la versión
- Revisar fallas de CI
- Generar resúmenes de reuniones de seguimiento
- Ejecutar de forma programada flujos de trabajo de análisis repetibles

Una regla útil es que las habilidades definen el método y las tareas programadas definen la programación. Si un flujo de trabajo aún necesita mucha orientación, conviértelo primero en una habilidad. Cuando sea predecible, programarlo puede ahorrarte tiempo.

  Usa las tareas programadas para el análisis retrospectivo y el mantenimiento, no solo para la ejecución. Revisa
los chats recientes, resume los problemas recurrentes y mejora con el tiempo los prompts, las instrucciones,
o la configuración del flujo de trabajo.

<a id="organize-long-running-tasks"></a>

## Organizar chats de larga duración

Con el tiempo, los chats acumulan contexto, decisiones y acciones, por lo que gestionarlos bien tiene un gran impacto en la calidad.

La app de escritorio de ChatGPT te permite fijar chats y crear worktrees. Si usas la
CLI, estos [comandos slash](/codex/developer-commands?surface=cli) son especialmente útiles:

- `/experimental` para activar o desactivar funciones experimentales y añadirlas a tu `config.toml`
- `/resume` para reanudar un chat guardado
- `/fork` para crear un chat nuevo conservando la transcripción original
- `/compact` cuando el chat se alargue y quieras una versión resumida del contexto anterior. Codex también compacta los chats automáticamente
- `/agent` cuando ejecutes agentes en paralelo y quieras cambiar entre los hilos de los agentes activos
- `/theme` para elegir un tema de resaltado de sintaxis
- `/apps` para usar las Apps de ChatGPT directamente en Codex
- `/status` para consultar el estado de la sesión actual

Mantén un chat para cada unidad de trabajo coherente. Si el trabajo aún forma parte del mismo
problema, suele ser mejor seguir en el mismo chat porque así se conserva el
hilo de razonamiento. Haz un fork solo cuando el trabajo se bifurque de verdad.

  Usa los flujos de trabajo con [subagentes](/es-419/codex/agent-configuration/subagents) de Codex para
  delegar tareas bien delimitadas fuera del hilo principal. Mantén al agente principal enfocado en el
  problema central y usa subagentes para tareas como exploración, pruebas o análisis inicial.

## Errores comunes

Estos son algunos errores comunes que debes evitar cuando empieces a usar Codex:

- Sobrecargar el prompt con reglas permanentes en lugar de trasladarlas a `AGENTS.md` o a una habilidad
- No permitir que el agente compruebe su trabajo por no darle detalles sobre la mejor manera de ejecutar los comandos de compilación y pruebas
- Omitir la planificación en tareas complejas y de varios pasos
- Otorgar a Codex acceso total a tu computadora antes de entender el flujo de trabajo
- Ejecutar tareas en curso sobre los mismos archivos sin usar Git worktrees
- Programar una tarea recurrente antes de que su ejecución manual sea confiable
- Tratar a Codex como si tuvieras que supervisarlo paso a paso, en lugar de usarlo en paralelo con tu propio trabajo
- Usar un solo chat para todo un proyecto en lugar de uno por cada resultado coherente. Con el tiempo, esto sobrecarga el contexto y empeora los resultados

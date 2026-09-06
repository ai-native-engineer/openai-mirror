<!-- source: https://learn.chatgpt.com/es-419/use-cases/native-ios-apps -->

## Generar la estructura inicial de la app y configurar el ciclo de compilación

Para proyectos nuevos, comienza con prompts sencillos. Pide a Codex que genere la estructura inicial de una app básica de iOS con SwiftUI y escriba un pequeño script para compilarla e iniciarla que puedas vincular a una acción `Build` en un [entorno local](/es-419/codex/environments/local-environment).

Mantén el ciclo centrado en la CLI. Con la herramienta de Apple `xcodebuild`, puedes enumerar esquemas y ejecutar desde la terminal las acciones build, test, archive, `build-for-testing` y `test-without-building`; así Codex puede permanecer en un ciclo de trabajo con agentes en vez de tener que pasar constantemente a la interfaz gráfica de Xcode.

Si quieres un generador de proyectos más limpio y te parece bien usar herramientas de terceros, [Tuist](https://tuist.dev/) es una buena opción para el siguiente paso. Puede generar y compilar proyectos de Xcode sin necesitar la interfaz gráfica y, aun así, permite que Codex compile e inicie la app desde la terminal.

Usa [XcodeBuildMCP](https://www.xcodebuildmcp.com/) cuando ya trabajes con un proyecto completo de Xcode y necesites una automatización más avanzada. En ese momento, los esquemas, los targets, el control del simulador, las capturas de pantalla, los registros y la interacción con la interfaz de usuario adquieren tanta importancia que los comandos de shell por sí solos dejan de ser suficientes.

## Aprovechar las habilidades

En la primera pasada, a menudo no necesitas una habilidad ni un servidor MCP. Agrega habilidades cuando el trabajo se especialice o quieras que la ejecución incorpore convenciones más sólidas de SwiftUI.

- [Experto en SwiftUI](https://github.com/AvdLee/SwiftUI-Agent-Skill) es una sólida habilidad de SwiftUI de uso general que ya incorpora muchas prácticas recomendadas.
- [SwiftUI Pro](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/main/swiftui-pro/SKILL.md) es una habilidad integral de revisión de SwiftUI para API modernas, facilidad de mantenimiento, accesibilidad y rendimiento.

- [Experto en Liquid Glass](https://github.com/Dimillian/Skills/blob/main/swiftui-liquid-glass/SKILL.md) ayuda a Codex a adoptar las nuevas API de Liquid Glass de iOS 26 y a ajustar componentes personalizados para que se adapten al diseño más reciente del sistema.
- [Rendimiento de SwiftUI](https://github.com/Dimillian/Skills/blob/main/swiftui-performance-audit/SKILL.md) resulta útil cuando una funcionalidad se siente lenta o la ruta de actualización de una vista de SwiftUI parece sospechosa. Analiza errores comunes de SwiftUI y genera un informe priorizado que indica qué corregir y dónde se pueden obtener las mayores mejoras.
- [Experto en concurrencia de Swift](https://github.com/Dimillian/Skills/blob/main/swift-concurrency-expert/SKILL.md) resulta útil cuando los errores crípticos y las advertencias del compilador empiezan a obstaculizar el cambio que quieres hacer. Con GPT-5.6 Terra, quizá lo necesites con menos frecuencia, aunque sigue siendo útil cuando los diagnósticos de concurrencia de Swift generan demasiado ruido.
- [Refactorización de vistas de SwiftUI](https://github.com/Dimillian/Skills/blob/main/swiftui-view-refactor/SKILL.md) ayuda a mantener los archivos más pequeños y a hacer que el código SwiftUI sea más uniforme en todo el repositorio.
- [Patrones de SwiftUI](https://github.com/Dimillian/Skills/blob/main/swiftui-ui-patterns/SKILL.md) ayuda a adoptar patrones de arquitectura predecibles con `@Observable` y `@Environment` a medida que crece la app.

Para obtener más información sobre cómo instalar y usar habilidades, consulta nuestra [documentación sobre habilidades](/es-419/codex/build-skills).

## Iterar

Cuando ya tengas una primera versión funcional o si partes de un proyecto existente, puedes empezar a iterar en la interfaz de usuario o el comportamiento.

En esta etapa, especifica qué quieres cambiar y cómo quieres cambiarlo.

En el diseño del prompt, deja explícito lo siguiente: indica a Codex si trabaja en un repositorio nuevo o en un proyecto existente de Xcode, qué dispositivos iOS o destinos de implementación deben seguir siendo compatibles y qué ciclo de validación esperas.

### Prompt de ejemplo

Por ejemplo, si quieres agregar una funcionalidad a una app existente, puedes pedirle a Codex un cambio como este:

## Consejos prácticos

### Comenzar por lo básico

Para proyectos nuevos, comienza con prompts sencillos. Pide a Codex que genere la estructura inicial de una app básica de SwiftUI y escriba un pequeño script para compilarla e iniciarla que puedas vincular a una acción `Build` en un [entorno local](/es-419/codex/environments/local-environment). En esa primera pasada, a menudo no necesitas ninguna habilidad ni servidor MCP.

### Usar un ciclo de validación acotado y confiable

Después de cada cambio, dile a Codex que ejecute el comando más acotado que realmente compruebe el contrato que modificaste. Luego amplía la validación con compilaciones más completas. Esto permite que Codex siga trabajando con rapidez sin asumir que cada edición exige compilar toda la app.

### Mantén el ciclo centrado en la CLI

Mantén el ciclo centrado en la CLI. La herramienta `xcodebuild` de Apple puede enumerar esquemas y ejecutar desde la terminal acciones de compilación, prueba y archivado, así como `build-for-testing` y `test-without-building`, lo que permite que Codex permanezca en un ciclo de trabajo con agentes sin tener que cambiar a la interfaz gráfica de Xcode.

### Aprovecha XcodeBuildMCP

Usa XcodeBuildMCP en cuanto estés trabajando en un proyecto completo de Xcode y necesites una automatización más avanzada. Es entonces cuando los esquemas, los destinos, el control del simulador, las capturas de pantalla, los registros y la interacción con la interfaz de usuario cobran suficiente importancia como para que los comandos del shell por sí solos ya no basten.

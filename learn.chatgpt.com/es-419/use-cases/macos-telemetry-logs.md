<!-- source: https://learn.chatgpt.com/es-419/use-cases/macos-telemetry-logs -->

## Agrega un Logger cuando no haya suficiente información para depurar

Este caso de uso está pensado para flujos de apps para Mac en los que “pasó algo” no aporta suficiente información para depurarlos solo mediante la revisión del código. Pídele a Codex que agregue algunos registros unificados muy informativos en torno a un comportamiento, ejecute la app, active ese comportamiento y verifique en Console o `log stream` que se generaron los eventos esperados.

Usa el [complemento Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) para ese ciclo. Su habilidad de telemetría de macOS es deliberadamente ligera: usa `Logger` de Apple, elige un par claro de subsistema y categoría, registra los puntos clave de las acciones y las transiciones de estado, evita cargas útiles confidenciales y verifica el evento después de compilar y ejecutar localmente, en lugar de suponer que la instrumentación quedó integrada correctamente.

## Por qué la telemetría es útil para la ingeniería con agentes

Los buenos registros le proporcionan a Codex un ciclo de retroalimentación repetible después de cada parche. En lugar de pedirte que revises manualmente cada ventana, acción de menú o transición de sincronización, el agente puede ejecutar la app, recorrer el flujo, revisar los registros filtrados y decidir el siguiente cambio de código a partir de la evidencia.

Esto resulta especialmente útil en tres ciclos de trabajo con agentes:

- **Ciclo de depuración sin intervención manual:** Codex instrumenta un flujo sospechoso, inicia la app, hace clic en la barra lateral o activa un comando, lee la secuencia de registros generada, aplica un parche a la ruta de actualización de estado y vuelve a ejecutar el mismo flujo hasta que los registros y el comportamiento de la interfaz coincidan.
- **Ciclo de recopilación de sesiones de la app:** Codex agrega un evento para el inicio de la app, la apertura de una ventana, la selección en la barra lateral, el inicio de una importación, la finalización de una importación y el fallo de una importación; luego, ejecuta una sesión local y resume la cronología resultante para que las transiciones faltantes o fuera de orden sean evidentes.
- **Ciclo de captura dirigido por una persona:** Codex inicia la app con el registro habilitado, mantiene activo un flujo de registros filtrado mientras reproduces manualmente un flujo difícil, luego revisa la sesión capturada y propone el siguiente parche a partir de esa traza.

## Mantén la instrumentación acotada y fácil de filtrar

Pídele a Codex un logger por cada área funcional, no una línea de registro permanente para cada cambio de estado. Las categorías de funciones como `Windowing`, `Commands`, `MenuBar`, `Sidebar`, `Sync` o `Import` facilitan mucho el filtrado de los registros durante la siguiente ronda de depuración.

```swift

private let logger = Logger(
  subsystem: Bundle.main.bundleIdentifier ?? "SampleApp",
  category: "Sidebar"
)

@MainActor
func selectItem(_ item: SidebarItem) {
  logger.info("Selected sidebar item: \(item.id, privacy: .public)")
  selection = item.id
}

Usa `info` para eventos concisos de acciones y del ciclo de vida que deban seguir siendo útiles con el tiempo, y `debug` para detalles más ruidosos del estado local que puedan eliminarse o bajarse de nivel antes de terminar la tarea. Agrega marcadores solo cuando midas un intervalo de tiempo, no de forma predeterminada.

## Pídele a Codex que compruebe el evento en los registros

Lo útil no es solo agregar llamadas a `Logger`. Pídele a Codex que ejecute la app, active el flujo instrumentado y te proporcione el filtro exacto de Console o el predicado de `log stream` que usó, junto con una o dos líneas de registro representativas.

```bash
log stream --style compact --predicate 'subsystem == "com.example.app" && category == "Sidebar"'

Si no aparece un evento esperado, pídele a Codex que acerque el registro a la ruta de control sospechosa, vuelva a ejecutar el mismo flujo y repita el proceso hasta que los registros expliquen qué ocurrió. Si la tarea deriva en el análisis de un fallo o de una traza de pila, pasa al flujo de trabajo de depuración de compilación y ejecución del complemento y mantén la telemetría enfocada en los puntos clave de las acciones.

## Guarda una traza de sesión para que Codex la revise después

Para errores cuya investigación requiere más tiempo o que aparecen de forma intermitente, pídele a Codex que guarde un flujo de registros filtrado en un pequeño archivo local de traza, resuma la cronología y deje ese artefacto en el espacio de trabajo para que una ejecución posterior de Codex pueda revisar la misma evidencia sin tener que reconstruir de memoria toda la sesión. Esto facilita la depuración en varias iteraciones cuando quieres que una ejecución del agente recopile una traza y otra compare el comportamiento antes y después de un parche.

Esto también funciona bien cuando una persona debe controlar parte de la sesión. Pídele a Codex que inicie la app en un ciclo de depuración que facilite el registro, inicie una captura filtrada, espere mientras reproduces el problema manualmente y luego lea el archivo de traza guardado cuando termines.

## Consejos prácticos

### Instrumenta una función a la vez

Empieza por una sola barra lateral, ventana, comando o ruta de sincronización para que la secuencia de registros siga siendo fácil de revisar. Si esa ruta funciona de forma confiable, Codex puede extender el mismo patrón a los flujos cercanos.

### Incluye la privacidad en el prompt

Pídele a Codex que explique cada identificador que registre y evite escribir secretos, datos personales o contenido sin procesar en los registros unificados. Un vocabulario reducido de eventos suele ser suficiente para la depuración local.

### Incluye resultados de ejemplo en el resumen final

Las líneas de registro representativas inspiran mucha más confianza en el cambio que la frase “se agregó telemetría”. Pídele a Codex que incluya el predicado de filtrado y una breve cronología de acciones para que la siguiente ejecución del agente pueda reutilizar el mismo ciclo de verificación.

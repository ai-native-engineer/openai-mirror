<!-- source: https://learn.chatgpt.com/es-419/use-cases/ios-simulator-bug-debugging -->

## Deja todo el ciclo del simulador en manos de Codex

Este caso de uso funciona mejor cuando Codex se encarga de todo el ciclo: elegir el destino correcto de la app, iniciar la app en Simulator, inspeccionar la pantalla actual, ejecutar los pasos de reproducción, recopilar registros y capturas de pantalla, inspeccionar una traza de pila si es necesario, aplicar un parche al código y volver a recorrer la misma ruta para demostrar que el error desapareció.

Usa el [complemento Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) cuando quieras mantener ese ciclo en manos de agentes. Su flujo de trabajo de depuración de iOS se basa en XcodeBuildMCP, lo que permite que Codex interactúe con un simulador iniciado y recopile la misma evidencia que normalmente obtendría una persona de forma manual.

Cuando XcodeBuildMCP está configurado con flujos de trabajo de automatización del simulador, automatización de la UI, depuración y registro, Codex puede encargarse de todo el ciclo de reproducción, depuración y verificación. Si Codex aún no ha seleccionado un proyecto, un esquema y un simulador, pídele que primero los identifique y que reutilice esa configuración durante el resto de la sesión.

## Aprovecha todo lo que XcodeBuildMCP puede hacer

Estos son los grupos de capacidades prácticas que conviene pedirle a Codex que use:

- Identificación del proyecto y el simulador: comprobar si Codex ya sabe qué destino de la app y qué simulador usar, localizar el proyecto o espacio de trabajo de Xcode, enumerar los esquemas, buscar o iniciar un simulador y mantener estable esa configuración para los pasos posteriores de compilación y ejecución.
- Control de la compilación y el inicio: compilar el destino activo de la app, instalar e iniciar en el simulador la versión compilada, volver a iniciarla con captura de registros cuando sea necesario y determinar el ID del bundle de la app si Codex necesita inspeccionar registros de ejecución específicos de esa app.
- Inspección e interacción con la UI: leer la jerarquía de accesibilidad que aparece en pantalla, tomar capturas de pantalla, tocar controles, escribir en campos, desplazarse por listas y deslizar desde los bordes o realizar otros gestos en el simulador.
- Registros y estado del depurador: consultar en tiempo real los registros del simulador, conectar LLDB a la app en ejecución, establecer puntos de interrupción, inspeccionar marcos de pila y variables locales, y ejecutar comandos del depurador cuando sea necesario inspeccionar más a fondo un cierre inesperado o un bloqueo.

El hábito clave es pedirle a Codex que inspeccione el árbol de vistas antes de tocar un elemento. XcodeBuildMCP expone la jerarquía de accesibilidad junto con las coordenadas, por lo que Codex puede preferir etiquetas estables o IDs de elementos en vez de adivinar posiciones en la pantalla.

## Convierte un error poco claro en un script reproducible

La habilidad de depuración de iOS es más eficaz cuando tu prompt describe un error concreto y un resultado esperado, y luego permite que Codex controle la app y recopile evidencia de forma autónoma. Si se necesita un inicio de sesión, un deep link o un fixture de prueba, indícalo una sola vez y pídele a Codex que se detenga solo si la falta de ese dato impide continuar.

## Consejos prácticos

### Pide evidencia, no solo una corrección

Pídele a Codex que indique exactamente qué simulador, esquema, capturas de pantalla, fragmentos de registros y detalles de la pila usó para explicar el error. Así, revisar el parche final resulta mucho más fácil que con un simple “Creo que esto debería corregirlo”.

### Prefiere las etiquetas de accesibilidad a las coordenadas

Si Codex tiene que tocar un control mediante coordenadas porque no tiene una etiqueta estable ni un identificador de accesibilidad, pídele que lo señale explícitamente. Esto suele indicar que la corrección también debería incluir una pequeña mejora que facilite las pruebas de la UI.

### Limita cada ejecución a un solo error

Un ciclo de depuración controlado mediante el simulador es potente, pero inspira más confianza cuando cada prompt se centra en un solo tipo de fallo. Pídele a Codex que complete un ciclo de reproducción, corrección y verificación antes de ampliar el alcance a problemas relacionados.

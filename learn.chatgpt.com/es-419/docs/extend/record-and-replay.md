<!-- source: https://learn.chatgpt.com/es-419/docs/extend/record-and-replay -->

Grabar y reproducir está disponible en macOS. El Uso de la computadora también debe estar disponible y
habilitado.

Grabar y reproducir te permite mostrar cómo realizas un flujo de trabajo en tu
Mac y convertirlo en una habilidad reutilizable. Usa esta función cuando el flujo de trabajo sea repetitivo,
dependa de tus preferencias o sea más fácil de mostrar que de describir en un prompt.

Por ejemplo, podrías grabar cómo registras un gasto, reservas un espacio de estacionamiento,
creas una incidencia configurada correctamente, publicas un video o descargas un informe
periódico. ChatGPT o Codex puede convertir ese patrón en una habilidad que puedes reutilizar
con el Uso de la computadora, acciones del navegador, complementos conectados o una combinación
de estas opciones.

## Antes de comenzar

Elige un flujo de trabajo que ya sepas completar. Grabar y reproducir funciona
mejor cuando los pasos son estables y los criterios de éxito son claros.

## Iniciar una grabación

1. En la aplicación de escritorio de ChatGPT, selecciona ChatGPT y activa Work en el selector, o selecciona Codex. Luego, abre **Complementos**.
2. Abre el menú **+** .
3. Selecciona **Grabar una habilidad**.
4. Revisa el prompt sugerido, agrega cualquier contexto útil y envíalo.
5. Cuando el chat te pida permiso para grabar tus acciones, aprueba la
solicitud cuando estés listo para mostrar el flujo de trabajo.
6. Realiza el flujo de trabajo en tu Mac.
7. Cuando termines, detén la grabación desde la barra de menús o la superposición, o dile al
chat que ya terminaste.

Durante la grabación, ChatGPT o Codex observa las acciones y el contenido de las ventanas
necesarios para aprender el flujo de trabajo. La grabación continúa hasta que la detengas. Procura que la
grabación se centre en la tarea que quieres que enseñe la habilidad.

Después de detener la grabación, ChatGPT o Codex analiza el flujo de trabajo capturado y
crea el borrador de una habilidad. La habilidad explica cuándo usar el flujo de trabajo, qué datos de entrada
necesita, qué pasos seguir y cómo verificar el resultado. También puedes pedir
más ajustes.

## Reproducir el flujo de trabajo

Inicia un chat nuevo en ChatGPT o Codex y pídele que use la habilidad generada. Indícale
los valores que sean distintos esta vez, como el archivo que debe subir, la
incidencia que debe crear o el rango de fechas del informe.

El producto usa la habilidad como contexto reutilizable para la tarea. Luego puede
completar el flujo de trabajo con las herramientas disponibles en el entorno actual,
entre ellas, el Uso de la computadora, las acciones del navegador y los complementos instalados.

## Consejos para obtener mejores grabaciones

- Procura que la demostración sea breve y completa.
- Antes de comenzar a grabar, indica tu objetivo y cualquier dato de entrada específico que pueda variar entre
los distintos usos de la habilidad.
- Usa datos de entrada realistas, pero evita los secretos y los datos sensibles.
- Después de grabar, perfecciona la habilidad para dejar claras las preferencias implícitas importantes,
como las convenciones de nomenclatura, los valores predeterminados de los campos o los puntos de decisión.
- Detén la grabación cuando se complete el flujo de trabajo, en vez de continuar con
tareas de limpieza que no estén relacionadas.

## Cuándo crear otro complemento

Grabar y reproducir es una forma rápida de crear una habilidad a partir de la demostración de un flujo de trabajo.
Si quieres distribuir un paquete estable e independiente entre los miembros de un equipo, agrupar
varias habilidades, incluir conectores, agregar servidores MCP o administrar los metadatos
de instalación, empaqueta ese flujo de trabajo como un complemento independiente. Consulta
[Crear plugins](https://developers.openai.com/plugins/build/plugins).

## Solución de problemas

### No veo Grabar y reproducir

Si tu organización administra Codex con `requirements.toml`, el requisito
`[features].computer_use` también controla Grabar y reproducir. Configurar
`computer_use = false` hace que ambas funciones dejen de estar disponibles.

<!-- source: https://learn.chatgpt.com/es-419/use-cases/codebase-onboarding -->

## Introducción

Cuando llegas a un repositorio nuevo o te asignan una funcionalidad que no conoces, Codex puede ayudarte a orientarte antes de empezar a modificar el código. El objetivo no es solo obtener un resumen general, sino trazar el flujo de solicitudes, comprender de qué se encarga cada módulo e identificar qué archivos conviene leer a continuación.

## Cómo usarlo

Si recién te incorporas a un proyecto, puedes empezar simplemente por pedirle a Codex que explique toda la base de código:

Si necesitas incorporar una funcionalidad nueva a una base de código existente, puedes pedirle a Codex que explique un área específica del sistema. Cuanto mejor delimites la solicitud, más concreta será la explicación:

1. Proporciona a Codex los archivos o directorios relevantes, o indícale el área funcional que intentas comprender.
2. Pídele que trace el flujo de solicitudes y explique qué módulos se encargan de la lógica de negocio, el transporte, la persistencia o la interfaz de usuario.
3. Antes de modificar nada, pregunta dónde se realiza la validación y dónde se producen los efectos secundarios o las transiciones de estado.
4. Por último, pregunta qué archivos deberías leer a continuación y cuáles son los puntos de riesgo.

Una respuesta útil para familiarizarte con el proyecto debería darte un mapa concreto, no solo una lista de nombres de archivos. Al final, Codex debería haber explicado el flujo principal, destacado los puntos de riesgo e indicado qué archivos leer o qué verificaciones realizar antes de empezar a hacer cambios.

## Qué preguntar a continuación

Una vez que Codex te dé una primera respuesta, sigue profundizando hasta que la explicación sea lo suficientemente específica como para que tengas la confianza necesaria para hacer la primera modificación. Las buenas preguntas de seguimiento suelen obligarlo a señalar los supuestos, las dependencias ocultas y las verificaciones importantes después de un cambio.

- ¿Qué módulo se encarga de la lógica de negocio propiamente dicha y qué módulos se encargan de la capa de transporte o de la interfaz de usuario?
- ¿Dónde se realiza la validación y qué supuestos se exigen allí?
- ¿Qué archivos relacionados o tareas en segundo plano podrían pasar desapercibidos si cambio este flujo?
- ¿Qué pruebas o verificaciones debería ejecutar después de modificar esta área?

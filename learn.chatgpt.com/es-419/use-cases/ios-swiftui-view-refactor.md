<!-- source: https://learn.chatgpt.com/es-419/use-cases/ios-swiftui-view-refactor -->

## Refactoriza una pantalla sin cambiar lo que hace

Este caso de uso sirve para cuando un archivo de SwiftUI ha crecido hasta convertirse en una pantalla enorme y cada cambio, por pequeño que sea, parece riesgoso. El objetivo no es rediseñar la función ni inventar una arquitectura nueva. Pídele a Codex que conserve el comportamiento y el diseño, y que después divida la pantalla en subvistas pequeñas con un flujo de datos explícito para que el próximo cambio sea más fácil de revisar.

Usa el [complemento Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) para este tipo de reorganización. Su habilidad de refactorización de vistas de SwiftUI define criterios claros y útiles: prioriza MV sobre MVVM, mantén la lógica de negocio en servicios o modelos, usa primero el estado local de la vista y las dependencias del entorno, y conserva un modelo de vista solo cuando la función realmente lo necesite.

## Qué pedirle a Codex que haga

Empieza por indicar el nombre de un archivo de pantalla concreto y pedirle a Codex que conserve el comportamiento mientras mejora la estructura. Conviene incluir directamente en el prompt estas reglas de refactorización:

- Reordena el archivo para que las dependencias del entorno, las propiedades almacenadas, el estado calculado no relacionado con vistas, `init`, `body`, los elementos auxiliares de la vista y los métodos auxiliares sean fáciles de recorrer de arriba abajo.
- Extrae las secciones relevantes en tipos `View` específicos, con entradas pequeñas y explícitas, propiedades `@Binding` y callbacks.
- Usa con moderación los elementos auxiliares calculados de tipo `some View` y mantenlos pequeños. No reconstruyas una pantalla enorme como una larga lista de fragmentos de vista privados y calculados.
- Saca de `body` las acciones de botones no triviales y los efectos secundarios, y traslada la lógica de negocio real a servicios o modelos.
- Mantén estable el árbol de vistas raíz. Prioriza los condicionales puntuales en secciones o modificadores en lugar de ramas `if/else` de nivel superior que reemplacen una pantalla completa por otra.
- A medida que avanzas, corrige qué vista administra el estado de Observation. Para los modelos raíz con `@Observable` en iOS 17 o posterior, la vista propietaria debe almacenarlos en `@State`; usa contenedores observables heredados solo cuando lo requiera el destino de implementación.

## Pide un ciclo de validación breve

Las refactorizaciones que conservan el comportamiento deben ir acompañadas de evidencia. Después de cada extracción relevante, pídele a Codex que ejecute la comprobación más acotada que ejercite la pantalla, ya sea una compilación, una vista previa, una prueba o una ejecución en el simulador; luego, que resuma qué cambió en la estructura y qué se mantuvo igual de forma intencional.

## Consejos prácticos

### Primero divide; luego, debate la arquitectura

Si una pantalla es demasiado grande, pídele a Codex que extraiga vistas específicas para cada sección antes de introducir una nueva capa de abstracción. Un árbol de vistas más corto y explícito suele evitar que se sienta la necesidad de agregar un modelo de vista.

### Pasa a cada subvista la interfaz mínima posible

Prefiere valores `let`, propiedades `@Binding` y callbacks con un único propósito, en lugar de pasar el modelo completo de la vista principal a cada vista secundaria. Así, cada sección extraída es más fácil de previsualizar y resulta más difícil volver a acoplarla por accidente a toda la pantalla.

### Pide a Codex que indique qué decidió no cambiar

Para una refactorización segura, resulta útil que Codex enumere de forma explícita lo que no cambió: las reglas de negocio, el comportamiento de la navegación, la persistencia, la semántica de la analítica y el diseño visible para el usuario. Así, la revisión es mucho más rápida.

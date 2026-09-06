<!-- source: https://learn.chatgpt.com/es-419/use-cases/learn-a-new-concept -->

## Introducción

Aprender un concepto nuevo a partir de un artículo o curso de contenido denso requiere más que un simple resumen. El objetivo es crear un modelo mental funcional: qué problema aborda, qué hace realmente el método, qué evidencia lo respalda, de qué supuestos depende y qué aspectos aún necesitas investigar.

ChatGPT resulta útil en este caso porque puede automatizar la recopilación de contexto y convertir conceptos complejos en diagramas o ilustraciones útiles. Este caso de uso también se presta bien al uso de [subagentes](/es-419/codex/agent-configuration/subagents): un hilo puede leer el artículo para identificar su estructura, otro puede recopilar el contexto previo necesario, otro puede examinar las figuras y la notación, y el hilo principal puede conciliar los resultados para elaborar un informe que podrás revisar más adelante.

En este caso de uso, el resultado final debe ser algo que puedas revisar fácilmente: un archivo Markdown como `notes/concept-report.md` o un documento en otro formato. En lugar de limitarse a una respuesta efímera en el chat, debe incluir un resumen, un glosario, una explicación paso a paso, diagramas, una tabla de evidencias, limitaciones y preguntas abiertas.

## Definir el objetivo de aprendizaje

Empieza por indicar el concepto y el resultado que quieres obtener. Una pregunta bien delimitada hace que el informe sea más útil que un resumen general.

Por ejemplo:

> Quiero entender la idea principal de este artículo de investigación, cómo funciona el método, por qué los experimentos respaldan o no la afirmación y qué debería leer a continuación.

Ese alcance le da a ChatGPT una tarea concreta. Debe enseñarte el concepto, pero también mantener explícita la incertidumbre, indicar mediante citas de dónde provienen las afirmaciones y separar las afirmaciones del artículo de su propia interpretación.

## Ejemplo práctico: análisis de un artículo de investigación

Supongamos que quieres aprender sobre un artículo acerca de una arquitectura de modelo que no conoces. Quieres un informe que te permita entender el concepto de un vistazo, sin tener que leer todo el artículo.

Un buen resultado podría tener este aspecto:

- `notes/paper-report.md` con la explicación principal.
- `notes/figures/method-flow.mmd` o un diagrama Mermaid integrado para explicar el método.
- `notes/figures/concept-map.mmd` o un pequeño SVG que muestre cómo se relacionan las ideas previas necesarias.
- Una tabla de evidencias que vincule las afirmaciones con las secciones, páginas, figuras o tablas del artículo.
- Una lista de lecturas de seguimiento y preguntas sin resolver.

La idea es sistematizar el proceso de aprendizaje y crear un recurso duradero.

## Distribuir el trabajo entre subagentes

Los subagentes funcionan mejor cuando cada uno tiene una tarea bien delimitada y un formato de respuesta claro. Pídele a ChatGPT que los cree explícitamente; ChatGPT no necesita usar subagentes para cada tarea de lectura, pero la exploración en paralelo resulta útil cuando el artículo es largo o conceptualmente denso.

Para un artículo de investigación, una división práctica del trabajo sería:

- **Mapa del artículo:** extrae el planteamiento del problema, la contribución, el método, los experimentos, las limitaciones y los resultados que el artículo afirma haber obtenido.
- **Contexto previo necesario:** explica los términos básicos, los conceptos relacionados y cualquier trabajo anterior que el artículo dé por conocido.
- **Notación y figuras:** explica paso a paso las ecuaciones, los algoritmos, los diagramas, las figuras y las tablas.
- **Revisor escéptico:** comprueba si la evidencia respalda las afirmaciones, enumera las salvedades e identifica métodos de referencia omitidos o supuestos poco claros.

El agente principal debe esperar a que esos subagentes terminen, comparar sus respuestas y resolver las contradicciones. Después, ChatGPT sintetizará los resultados en un informe coherente.

## Recopilar contexto adicional de forma intencional

Cuando el artículo suponga que ya tienes conocimientos previos que en realidad no posees, pídele a ChatGPT que recopile contexto de fuentes aprobadas. Pueden ser notas locales, una carpeta de bibliografía, artículos enlazados, una búsqueda web si está habilitada o una base de conocimiento conectada.

Si estás aprendiendo sobre un concepto interno, puedes conectar varias fuentes mediante [complementos](/es-419/codex/plugins) para crear una base de conocimiento.

Mantén este paso bien delimitado. Dile a ChatGPT qué se considera una fuente confiable y cómo debe usar el contexto externo en el informe final:

- Define en un glosario los términos que es necesario conocer de antemano.
- Agrega una breve sección titulada “Conocimientos previos necesarios”.
- Presenta las lecturas de seguimiento, con sus enlaces, por separado de las afirmaciones del propio artículo.
- Señala las afirmaciones que provengan de fuentes externas al artículo.

## Generar diagramas para el informe

Los diagramas suelen ser la forma más rápida de comprobar si realmente entiendes un concepto. Para un informe en Markdown, pídele a ChatGPT que genere diagramas fieles al material de origen y fáciles de modificar.

Algunas opciones iniciales recomendadas son:

- Un mapa conceptual que muestre las ideas previas necesarias y cómo se conectan.
- Un diagrama de flujo del método que muestre las entradas, las transformaciones, los componentes del modelo y las salidas.
- Un mapa de experimentos que conecte los conjuntos de datos, las métricas, los métodos de referencia y las afirmaciones presentadas.
- Un diagrama de limitaciones que separe los supuestos, los modos de falla y las preguntas abiertas.

Para los informes cuyo formato principal sea Markdown, pide diagramas Mermaid cuando el destino los admita o un recurso SVG/PNG pequeño incluido en el control de versiones cuando no los admita. Pídele a ChatGPT que use la habilidad del sistema imagegen, que ChatGPT incluye de forma predeterminada, solo cuando necesites un recurso visual ilustrativo que no tenga que ser exacto o algo que no se pueda representar bien en un diagrama nativo de Markdown.

## Escribir el informe en Markdown

Pídele a ChatGPT que el informe incluya todo lo necesario para que puedas retomarlo más adelante. Una estructura útil es:

1. Resumen ejecutivo.
2. Lo que debes saber antes de leer.
3. Términos clave y notación.
4. Recorrido por el artículo.
5. Diagrama del método.
6. Tabla de evidencias.
7. Lo que el artículo no demuestra.
8. Preguntas abiertas y lecturas posteriores.

El informe debe incluir referencias a las fuentes siempre que sea posible. Si se trata de un PDF, pide referencias a páginas, secciones, figuras o tablas. Si ChatGPT no puede extraer referencias exactas a páginas, debe indicarlo y usar en su lugar referencias a secciones o encabezados.

## Usa el informe para crear un ciclo de estudio

El primer informe es solo el punto de partida. Después de leerlo, haz preguntas de seguimiento y pídele a ChatGPT que revise el documento.

Estas son algunas preguntas de seguimiento útiles:

- ¿Qué parte de este método debo entender primero?
- ¿Cuál es el ejemplo más sencillo que demuestra la idea central?
- ¿Qué figura sostiene en mayor medida el argumento del artículo?
- ¿Qué afirmación es la más débil o la menos fundamentada?
- ¿Qué debo leer después si quiero implementar esto?

Cuando el concepto requiera experimentación, pídele a ChatGPT que agregue un notebook o un script pequeño que reproduzca una versión simplificada de la idea. Incluye en el informe en Markdown un enlace a ese trabajo exploratorio para mantener juntos la explicación y el experimento.

Prompt de ejemplo:

## Habilidades que conviene considerar

Usa las habilidades solo si son adecuadas para el resultado que quieres crear:

- `$jupyter-notebook` para ejemplos sencillos, gráficos o reproducciones ligeras que se puedan ejecutar.
- `$imagegen` para recursos visuales ilustrativos que no necesitan ser diagramas técnicos exactos.
- `$slides` cuando quieras convertir el informe en una presentación una vez terminada la fase de aprendizaje.

Para la mayoría de los informes de análisis de artículos, los diagramas nativos de Markdown o los archivos SVG sencillos son mejores opciones predeterminadas que una imagen de mapa de bits generada. Son más fáciles de comparar entre versiones, revisar y actualizar a medida que cambia tu comprensión.

## Sugerencias de prompts

**Crea primero el esquema del informe**

**Crea diagramas para el concepto**

**Convierte el informe en un plan de estudio**

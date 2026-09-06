<!-- source: https://learn.chatgpt.com/es-419/guides/build-ai-native-engineering-team -->

## Introducción

Los modelos de IA están ampliando rápidamente la variedad de tareas que pueden realizar, lo que tiene importantes implicaciones para la ingeniería. Los sistemas de vanguardia ya son capaces de razonar durante varias horas: en agosto de 2025, METR determinó que los principales modelos podían completar **2 horas y 17 minutos** de trabajo continuo con cerca de **un 50 % de confianza** en que producirían una respuesta correcta.

Esta capacidad mejora rápidamente: la duración de las tareas se duplica aproximadamente cada siete meses. Hace apenas unos años, los modelos podían mantener unos 30 segundos de razonamiento, lo suficiente para ofrecer pequeñas sugerencias de código. Hoy, como los modelos pueden mantener cadenas de razonamiento más largas, la asistencia de la IA podría abarcar todo el ciclo de vida del desarrollo de software, lo que permite que los agentes de codificación contribuyan eficazmente a la planificación, el diseño, el desarrollo, las pruebas, las revisiones de código y el despliegue.

![][image1]En esta guía, compartiremos ejemplos reales que muestran cómo los agentes de IA contribuyen al ciclo de vida del desarrollo de software, junto con orientación práctica sobre lo que los líderes de ingeniería pueden hacer hoy para comenzar a crear equipos y procesos nativos de IA.

## Codificación con IA: del autocompletado a los agentes

Las herramientas de codificación con IA han avanzado mucho más allá de sus orígenes como asistentes de autocompletado. Las primeras herramientas se ocupaban de tareas rápidas, como sugerir la siguiente línea de código o completar plantillas de funciones. A medida que mejoraron las capacidades de razonamiento de los modelos, los desarrolladores comenzaron a interactuar con agentes mediante interfaces de chat en los IDE para programar en pareja y explorar el código.

Los agentes de codificación actuales pueden generar archivos completos, crear la estructura inicial de proyectos nuevos y convertir diseños en código. Pueden razonar para resolver problemas de varios pasos, como la depuración o la refactorización, y su ejecución también está pasando de la computadora de cada desarrollador a entornos multiagente basados en la nube. Esto está cambiando la forma de trabajar de los desarrolladores, ya que les permite dedicar menos tiempo a generar código con el agente dentro del IDE y más a delegar flujos de trabajo completos.

| Capacidad                         | Qué permite                                                                                                                                                        |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Contexto unificado entre sistemas** | Un solo modelo puede leer código, configuración y telemetría, lo que permite un razonamiento coherente entre capas que antes requerían herramientas independientes.                    |
| **Ejecución estructurada de herramientas**      | Ahora, los modelos pueden invocar directamente compiladores, ejecutores de pruebas y escáneres para producir resultados verificables en lugar de sugerencias estáticas.                                       |
| **Memoria persistente del proyecto**      | Las ventanas de contexto amplias y técnicas como la compactación permiten que los modelos hagan un seguimiento de una funcionalidad desde su propuesta hasta el despliegue y recuerden decisiones de diseño y restricciones anteriores. |
| **Ciclos de evaluación**               | Los resultados de los modelos se pueden probar automáticamente con criterios de referencia —pruebas unitarias, objetivos de latencia o guías de estilo—, de modo que las mejoras se basen en mediciones de calidad.          |

En OpenAI, lo hemos comprobado de primera mano. Los ciclos de desarrollo se han acelerado: ahora, el trabajo que antes tomaba semanas se entrega en días. Los equipos pueden pasar con mayor facilidad de un dominio a otro, incorporarse más rápido a proyectos que desconocen y operar con mayor agilidad y autonomía en toda la organización. Muchas tareas rutinarias que consumen mucho tiempo —como documentar código nuevo, localizar pruebas relevantes, mantener dependencias y limpiar marcas de funcionalidades— ahora se delegan por completo a Codex.

Sin embargo, algunos aspectos de la ingeniería siguen igual. La verdadera responsabilidad sobre el código —especialmente en problemas nuevos o ambiguos— sigue recayendo en los ingenieros, y ciertos desafíos superan las capacidades de los modelos actuales. Pero, con agentes de codificación como Codex, los ingenieros ahora pueden dedicar más tiempo a desafíos complejos y novedosos y centrarse en el diseño, la arquitectura y el razonamiento a nivel de sistema, en lugar de la depuración o las implementaciones rutinarias.

En las siguientes secciones, analizamos cómo cambia cada fase del SDLC con los agentes de codificación y presentamos los pasos concretos que tu equipo puede seguir para comenzar a operar como una organización de ingeniería nativa de IA.

## 1. Planificación

Los equipos de una organización suelen depender de los ingenieros para determinar si una funcionalidad es viable, cuánto tiempo llevará desarrollarla y qué sistemas o equipos participarán. Aunque cualquiera puede redactar una especificación, elaborar un plan preciso normalmente exige conocer a fondo el código base y realizar varias rondas de iteración con el equipo de ingeniería para descubrir requisitos, aclarar casos extremos y acordar qué es viable desde el punto de vista técnico.

### Cómo ayudan los agentes de codificación

Durante la planificación y la definición del alcance, los agentes de codificación con IA ofrecen a los equipos información inmediata basada en el código. Por ejemplo, los equipos pueden crear flujos de trabajo que conecten los agentes de codificación con sus sistemas de seguimiento de incidencias para leer una especificación de la funcionalidad, contrastarla con el código base y, luego, señalar ambigüedades, dividir el trabajo en subcomponentes o estimar su dificultad.

Los agentes de codificación también pueden rastrear de inmediato las rutas del código para mostrar qué servicios intervienen en una funcionalidad; antes, este trabajo requería horas o días de búsqueda manual en un código base grande.

### En qué se enfocan los ingenieros

Los equipos dedican más tiempo al desarrollo en sí de las funcionalidades porque los agentes proporcionan el contexto que antes requería reuniones para alinear criterios sobre el producto y definir el alcance. Los detalles clave de la implementación, las dependencias y los casos extremos se identifican desde el principio, lo que permite tomar decisiones más rápido y con menos reuniones.

| Delegación                                                                                                                                                                                                              | Revisión                                                                                                                                                                                                                                       | Responsabilidad                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Los agentes de IA pueden realizar un análisis inicial de viabilidad y arquitectura. Leen una especificación, la relacionan con el código base, identifican dependencias y detectan ambigüedades o casos extremos que deben aclararse. | Los equipos revisan los resultados del agente para validar su precisión, evaluar si están completos y asegurarse de que las estimaciones reflejen las restricciones técnicas reales. La asignación de puntos de historia, el cálculo del esfuerzo y la identificación de riesgos poco evidentes siguen requiriendo criterio humano. | Las decisiones estratégicas —como la priorización, la dirección a largo plazo, la secuenciación y la evaluación de ventajas y desventajas— siguen en manos de las personas. Los equipos pueden pedirle al agente opciones o próximos pasos, pero la responsabilidad final de la planificación y la dirección del producto sigue recayendo en la organización. |

### Lista de verificación de primeros pasos

- Identifica los procesos habituales que requieren alinear las funcionalidades con el código fuente. Algunas áreas comunes son la definición del alcance de las funcionalidades y la creación de tickets.
- Comienza por implementar flujos de trabajo básicos, como etiquetar incidencias o solicitudes de funcionalidades y eliminar sus duplicados.
- Considera flujos de trabajo más avanzados, como agregar subtareas a un ticket a partir de la descripción inicial de una funcionalidad. O bien, inicia la ejecución de un agente cuando un ticket llegue a una etapa específica para complementar la descripción con más detalles.

<br />

## 2. Diseño

La fase de diseño suele demorarse por las tareas iniciales de configuración. Los equipos dedican mucho tiempo a preparar código repetitivo, integrar sistemas de diseño y perfeccionar componentes o flujos de UI. La falta de alineación entre las maquetas y la implementación puede generar retrabajo y ciclos de retroalimentación prolongados, y la capacidad limitada para explorar alternativas o adaptarse a requisitos cambiantes retrasa la validación del diseño.

### Cómo ayudan los agentes de codificación

Las herramientas de codificación con IA aceleran considerablemente la creación de prototipos al generar código repetitivo, crear estructuras de proyecto e implementar de inmediato tokens de diseño o guías de estilo. Los ingenieros pueden describir las funcionalidades o los diseños de UI que desean en lenguaje natural y recibir código para el prototipo o componentes preliminares que se ajusten a las convenciones del equipo.

Pueden convertir diseños directamente en código, sugerir mejoras de accesibilidad e incluso analizar el código base para identificar flujos de usuario o casos extremos. Esto permite realizar iteraciones de varios prototipos en horas en lugar de días y crear prototipos de alta fidelidad desde las primeras etapas, lo que brinda a los equipos una base más clara para tomar decisiones y permite realizar pruebas con clientes mucho antes en el proceso.

### En qué se enfocan los ingenieros

Como los agentes se ocupan de las tareas rutinarias de configuración y conversión, los equipos pueden centrar su atención en trabajos de mayor impacto. Los ingenieros se enfocan en perfeccionar la lógica central, establecer patrones arquitectónicos escalables y garantizar que los componentes cumplan los estándares de calidad y confiabilidad. Los diseñadores pueden dedicar más tiempo a evaluar flujos de usuario y explorar conceptos alternativos. El esfuerzo colaborativo pasa de lidiar con la sobrecarga de la implementación a mejorar la experiencia del producto en sí.

| Delegación                                                                                                                                                                             | Revisión                                                                                                                                                                       | Responsabilidad                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Los agentes se encargan del trabajo inicial de implementación: crean la estructura de los proyectos, generan código repetitivo, convierten maquetas en componentes y aplican tokens de diseño o guías de estilo. | El equipo revisa los resultados del agente para asegurarse de que los componentes sigan las convenciones de diseño, cumplan los estándares de calidad y accesibilidad y se integren correctamente con los sistemas existentes. | El equipo es responsable del sistema de diseño general, los patrones de UX, las decisiones arquitectónicas y la dirección final de la experiencia del usuario. |

### Lista de verificación de primeros pasos

- Usa un agente de codificación multimodal que acepte entradas de texto e imágenes
- Integra herramientas de diseño con agentes de codificación mediante MCP
- Usa MCP para exponer las bibliotecas de componentes mediante programación e intégralas con tu modelo de codificación
- Crea flujos de trabajo que relacionen diseños → componentes → implementación de componentes
- Usa lenguajes con tipado (por ejemplo, Typescript) para definir props y subcomponentes válidos para el agente
  <br />

## 3. Desarrollo

La fase de desarrollo es donde los equipos encuentran más dificultades y donde el impacto de los agentes de codificación es más evidente. Los ingenieros dedican mucho tiempo a convertir especificaciones en estructuras de código, conectar servicios entre sí, replicar patrones en todo el código base y escribir código repetitivo; incluso las funcionalidades pequeñas requieren horas de trabajo tedioso.

A medida que los sistemas crecen, el problema se agrava. Los monorepositorios grandes acumulan patrones, convenciones y peculiaridades históricas que ralentizan a quienes contribuyen al código. Los ingenieros pueden dedicar tanto tiempo a redescubrir la “forma correcta” de hacer algo como a implementar la funcionalidad misma. El cambio constante de contexto entre las especificaciones, la búsqueda de código, los errores de compilación, las pruebas fallidas y la gestión de dependencias aumenta la carga cognitiva; además, las interrupciones durante tareas de larga duración rompen el ritmo de trabajo y retrasan aún más la entrega.

### Cómo ayudan los agentes de codificación

Los agentes de codificación que se ejecutan en el IDE y la CLI aceleran la fase de desarrollo al encargarse de tareas de implementación más grandes y de varios pasos. En lugar de producir solo la siguiente función o el siguiente archivo, pueden crear funcionalidades completas de principio a fin —modelos de datos, APIs, componentes de UI, pruebas y documentación— en una sola ejecución coordinada. Gracias a que pueden mantener el razonamiento en todo el código base, se encargan de tomar decisiones que antes exigían que los ingenieros rastrearan manualmente las rutas del código.

En tareas de larga duración, los agentes pueden:

- Crear un borrador de la implementación completa de una funcionalidad a partir de una especificación escrita.
- Buscar y modificar código en decenas de archivos sin perder la coherencia.
- Generar código repetitivo que respete las convenciones: manejo de errores, telemetría, capas de seguridad o patrones de estilo.
- Corregir los errores de compilación a medida que aparecen, sin detenerse a esperar la intervención humana.
- Escribir las pruebas al mismo tiempo que la implementación, como parte de un único flujo de trabajo.
- Producir conjuntos de cambios listos para generar un diff, que sigan los lineamientos internos e incluyan mensajes para los PR.

En la práctica, esto transfiere gran parte del “trabajo mecánico de desarrollo” de los ingenieros a los agentes. El agente realiza la primera implementación; el ingeniero pasa a ser quien revisa y edita, y quien marca el rumbo.

### Qué hacen los ingenieros en su lugar

Cuando los agentes pueden ejecutar de forma confiable tareas de desarrollo de varios pasos, los ingenieros centran su atención en tareas de mayor nivel:

- Aclarar el comportamiento del producto, los casos extremos y las especificaciones antes de la implementación.
- Revisar las implicaciones arquitectónicas del código generado por IA en lugar de encargarse de tareas rutinarias de integración.
- Perfeccionar la lógica de negocio y las rutas críticas para el rendimiento que requieren un razonamiento profundo sobre el dominio.
- Diseñar patrones, salvaguardas y convenciones que orienten el código generado por los agentes.
- Colaborar con los equipos de producto y diseño para perfeccionar la intención de la funcionalidad, no el código repetitivo.

En lugar de “traducir” una especificación de funcionalidad a código, los ingenieros se concentran en la corrección, la coherencia, la facilidad de mantenimiento y la calidad a largo plazo, aspectos en los que el contexto humano sigue siendo especialmente importante.

| Delegación                                                                                                                                                                                                                                           | Revisión                                                                                                                                                                                                                              | Responsabilidad                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Los agentes preparan una primera implementación de funcionalidades bien especificadas: estructura base, lógica CRUD, conexiones, refactorizaciones y pruebas. A medida que mejora el razonamiento en tareas prolongadas, esto abarca cada vez más implementaciones completas de extremo a extremo, en lugar de fragmentos aislados. | Los ingenieros evalúan las decisiones de diseño, el rendimiento, la seguridad, el riesgo de migración y la adecuación al dominio, a la vez que corrigen problemas sutiles que el agente podría pasar por alto. Dan forma y perfeccionan el código generado por IA en lugar de realizar el trabajo mecánico. | Los ingenieros conservan la responsabilidad sobre el trabajo que exige una intuición profunda sobre el sistema: nuevas abstracciones, cambios arquitectónicos transversales, requisitos de producto ambiguos y decisiones difíciles sobre la facilidad de mantenimiento a largo plazo. A medida que los agentes asumen tareas más largas, el trabajo de ingeniería pasa de la implementación línea por línea a la supervisión iterativa. |

Ejemplo:

Los ingenieros, responsables de producto, diseñadores y operadores de Cloudwalk usan Codex a diario para convertir especificaciones en código funcional, ya sea que necesiten un script, una nueva regla de fraude o un microservicio completo en cuestión de minutos. Codex elimina el trabajo tedioso de la fase de desarrollo y permite que todos los empleados implementen ideas a una velocidad notable.

### Lista de verificación de primeros pasos

- Comienza con tareas bien especificadas
- Haz que el agente use una herramienta de planificación mediante MCP o que escriba un archivo PLAN.md y lo incorpore al código base mediante un commit
- Comprueba que los comandos que el agente intenta ejecutar se completen correctamente
- Perfecciona de forma iterativa un archivo AGENTS.md que habilite ciclos de ejecución del agente, como ejecutar pruebas y linters para obtener retroalimentación
  <br />

## 4. Pruebas

Los desarrolladores suelen tener dificultades para garantizar una cobertura de pruebas adecuada porque escribir y mantener pruebas exhaustivas toma tiempo, obliga a cambiar de contexto y exige comprender a fondo los casos extremos. Los equipos suelen tener que elegir entre avanzar rápido y escribir pruebas exhaustivas. Cuando se acercan las fechas límite, la cobertura de pruebas suele ser lo primero que se sacrifica.

Incluso cuando ya se han escrito las pruebas, mantenerlas actualizadas a medida que evoluciona el código genera fricción constante. Las pruebas pueden volverse frágiles, fallar por motivos poco claros y requerir grandes refactorizaciones propias a medida que cambia el producto subyacente. Las pruebas de alta calidad permiten que los equipos hagan entregas más rápido y con más confianza.

### Cómo ayudan los agentes de codificación

Las herramientas de codificación con IA pueden ayudar a los desarrolladores a crear mejores pruebas de varias maneras eficaces. Para empezar, pueden sugerir casos de prueba tras leer un documento de requisitos y la lógica del código de la funcionalidad. Los modelos pueden ser sorprendentemente eficaces para proponer casos extremos y modos de falla que un desarrollador podría pasar por alto, sobre todo si lleva mucho tiempo concentrado en la funcionalidad y necesita una segunda opinión.

Además, los modelos pueden ayudar a mantener las pruebas actualizadas a medida que evoluciona el código, lo que reduce la fricción al refactorizar y evita pruebas obsoletas que empiezan a fallar de forma intermitente. Al encargarse de los detalles básicos de implementación al escribir pruebas e identificar casos extremos, los agentes de codificación aceleran el desarrollo de pruebas.

### Qué hacen los ingenieros en su lugar

Escribir pruebas con herramientas de IA no elimina la necesidad de que los desarrolladores reflexionen sobre las pruebas. De hecho, a medida que los agentes eliminan las barreras para generar código, las pruebas cumplen una función cada vez más importante como fuente de verdad sobre el funcionamiento de la aplicación. Dado que los agentes pueden ejecutar el conjunto de pruebas e iterar según los resultados, definir pruebas de alta calidad suele ser el primer paso para que un agente pueda desarrollar una funcionalidad.

En cambio, los desarrolladores se enfocan más en identificar patrones generales en la cobertura de pruebas, además de ampliar y cuestionar los casos de prueba que identifica el modelo. Agilizar la escritura de pruebas permite que los desarrolladores entreguen funcionalidades más rápido y también aborden funcionalidades más ambiciosas.

| Delegación                                                                                                                                                                                                                                                                          | Revisión                                                                                                                                                                                                                                                                                                                                           | Responsabilidad                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Los ingenieros delegarán una primera propuesta de casos de prueba basada en las especificaciones de la funcionalidad. También usarán el modelo para generar una primera versión de las pruebas. Puede ser útil pedirle al modelo que genere las pruebas en una sesión separada de la implementación de la funcionalidad. | Los ingenieros aún deben revisar minuciosamente las pruebas generadas por el modelo para asegurarse de que no haya tomado atajos ni implementado pruebas con stubs. También deben asegurarse de que sus agentes puedan ejecutar las pruebas, cuenten con los permisos adecuados para hacerlo y comprendan el contexto de los distintos conjuntos de pruebas que pueden ejecutar. | Los ingenieros son responsables de alinear la cobertura de pruebas con las especificaciones de la funcionalidad y las expectativas sobre la experiencia del usuario. Pensar de forma adversarial, identificar casos extremos con creatividad y centrarse en la intención de las pruebas siguen siendo habilidades fundamentales. |

### Lista de verificación de primeros pasos

- Indica al modelo que implemente las pruebas como un paso independiente y verifica que las pruebas nuevas fallen antes de pasar a implementar la funcionalidad.
- Define lineamientos de cobertura de pruebas en tu archivo AGENTS.md
- Dale al agente ejemplos específicos de herramientas de cobertura de código que pueda invocar para evaluar la cobertura de las pruebas
  <br />

## 5. Revisión

En promedio, los desarrolladores dedican 2–5 horas por semana a revisar código. Los equipos suelen tener que elegir entre invertir mucho tiempo en una revisión exhaustiva o hacer una revisión rápida y “suficientemente buena” de cambios que parecen pequeños. Cuando esta priorización es incorrecta, los errores se filtran a producción, lo que causa problemas a los usuarios y genera una cantidad considerable de trabajo adicional.

### Cómo ayudan los agentes de codificación

Los agentes de codificación permiten ampliar el proceso de revisión de código para que cada PR reciba un nivel básico y uniforme de atención. A diferencia de las herramientas tradicionales de análisis estático, que dependen de la detección de patrones y las comprobaciones basadas en reglas, los revisores con IA pueden ejecutar partes del código, interpretar el comportamiento en tiempo de ejecución y seguir la lógica entre archivos y servicios. Sin embargo, para que sean eficaces, los modelos deben entrenarse específicamente para detectar errores de nivel P0 y P1, y ajustarse para ofrecer comentarios concisos y relevantes; las respuestas demasiado extensas se ignoran con la misma facilidad que las advertencias poco útiles de los linters.

### Qué hacen los ingenieros en su lugar

En OpenAI, hemos observado que la revisión de código con IA da a los ingenieros más confianza en que no enviarán errores graves a producción. A menudo, la revisión de código detecta problemas que el autor del cambio puede corregir antes de involucrar a otro ingeniero. La revisión de código no necesariamente acelera el proceso de Pull Request, sobre todo si detecta errores importantes, pero sí evita defectos e interrupciones del servicio.

### Delegación, revisión y responsabilidad

Incluso con la revisión de código con IA, los ingenieros siguen siendo responsables de asegurarse de que el código esté listo para desplegarse. En la práctica, esto implica leer el cambio y comprender sus repercusiones. Los ingenieros delegan la revisión inicial del código a un agente, pero asumen la responsabilidad de la revisión final y del proceso de fusión.

| Delegación                                                                                                                                                    | Revisión                                                                                                                                                                                                                       | Responsabilidad                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Los ingenieros delegan en los agentes la revisión inicial del código. Esto puede ocurrir varias veces antes de que el Pull Request se marque como listo para que un compañero de equipo lo revise. | Los ingenieros siguen revisando los Pull Requests, pero ponen mayor énfasis en la alineación arquitectónica: si los patrones implementados son componibles, si se usan las convenciones correctas y si la funcionalidad cumple los requisitos. | En última instancia, los ingenieros son responsables del código desplegado en producción; deben asegurarse de que funcione de manera confiable y cumpla los requisitos previstos. |

Ejemplo:

Sansan usa la revisión de Codex para detectar condiciones de carrera y problemas en las relaciones de la base de datos, cuestiones que las personas suelen pasar por alto. Codex también ha podido detectar el uso inadecuado de valores fijos en el código e incluso anticipar posibles problemas de escalabilidad en el futuro.

### Lista de verificación de primeros pasos

- Selecciona ejemplos de Pull requests de referencia que hayan revisado ingenieros e incluyan tanto los cambios en el código como los comentarios que dejaron. Guarda estos ejemplos como un conjunto de evaluación para comparar distintas herramientas.
- Elige un producto que cuente con un modelo entrenado específicamente para revisar código. Hemos observado que los modelos generalistas suelen detenerse en detalles insignificantes y ofrecen una baja relación señal-ruido.
- Define cómo medirá tu equipo si las revisiones son de alta calidad. Te recomendamos hacer un seguimiento de las reacciones a los comentarios en los pull requests como una forma sencilla de marcar las revisiones como buenas o malas.
- Comienza a pequeña escala, pero extiende el uso rápidamente una vez que confíes en los resultados de las revisiones.
  <br />

## 6. Documentar

La mayoría de los equipos de ingeniería sabe que su documentación está rezagada, pero ponerse al día resulta costoso. El conocimiento fundamental suele quedar en manos de personas en lugar de registrarse en bases de conocimiento en las que se puedan hacer búsquedas, y la documentación existente se desactualiza rápidamente porque mantenerla al día les quita a los ingenieros tiempo para trabajar en el producto. Incluso cuando los equipos organizan sprints de documentación, el resultado suele ser un esfuerzo aislado que pierde vigencia en cuanto el sistema evoluciona.

### Cómo ayudan los agentes de programación

Los agentes de programación tienen una gran capacidad para resumir el funcionamiento de los repositorios de código después de leerlos. No solo pueden explicar cómo funcionan distintas partes del repositorio, sino que también pueden generar diagramas del sistema con sintaxis como mermaid. A medida que los desarrolladores crean funcionalidades con agentes, también pueden actualizar la documentación con solo pedírselo al modelo mediante un prompt. Con AGENTS.md, las instrucciones para actualizar la documentación cuando sea necesario pueden incluirse automáticamente en cada prompt para lograr mayor consistencia.

Como los agentes de programación se pueden ejecutar de manera programática mediante SDKs, también pueden incorporarse a flujos de trabajo de lanzamiento. Por ejemplo, podemos pedirle a un agente de programación que revise los commits incluidos en el lanzamiento y resuma los cambios principales. El resultado es que la documentación se integra en el proceso de entrega: se produce con mayor rapidez, es más fácil mantenerla actualizada y ya no depende de que alguien “encuentre tiempo”.

### Qué hacen los ingenieros en su lugar

Los ingenieros dejan de redactar cada documento a mano y pasan a dar forma al sistema y supervisarlo. Deciden cómo se organiza la documentación, incorporan el “por qué” esencial de las decisiones, establecen estándares y plantillas claros que los agentes deben seguir y revisan los materiales críticos o destinados a clientes. Su tarea pasa a ser garantizar que la documentación esté estructurada, sea precisa y se integre en el proceso de entrega, en lugar de escribirla toda por su cuenta.

| Delegación                                                                                                                                                                                                   | Revisión                                                                                                                                                                              | Responsabilidad                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Delega por completo en Codex tareas repetitivas y de bajo riesgo, como resúmenes iniciales de archivos y módulos, descripciones básicas de entradas y salidas, listas de dependencias y breves resúmenes de los cambios de los pull requests. | Los ingenieros revisan y editan documentos importantes redactados por Codex, como descripciones generales de servicios principales, documentación de API públicas y SDK, guías operativas y páginas de arquitectura, antes de que se publique cualquier contenido. | Los ingenieros siguen siendo responsables de la estrategia y la estructura generales de la documentación, de los estándares y las plantillas que sigue el agente, y de toda la documentación externa o crítica para la seguridad que conlleve riesgos legales, normativos o para la marca. |

### Lista de verificación de primeros pasos

- Experimenta con la generación de documentación mediante prompts para el agente de programación
- Incorpora lineamientos de documentación en tu AGENTS.md
- Identifica flujos de trabajo (p. ej., ciclos de lanzamiento) en los que se pueda generar documentación automáticamente
- Revisa el contenido generado para comprobar su calidad, exactitud y enfoque
  <br />

## 7. Desplegar y mantener

Comprender los registros de las aplicaciones es fundamental para la confiabilidad del software. Durante un incidente, los ingenieros de software consultan herramientas de registro, despliegues de código y cambios en la infraestructura para identificar la causa raíz. Este proceso suele ser sorprendentemente manual y obliga a los desarrolladores a alternar entre las pestañas de distintos sistemas, lo que consume minutos cruciales en situaciones de gran presión, como los incidentes.

### Cómo ayudan los agentes de programación

Con las herramientas de programación con IA, puedes darles acceso a tus herramientas de registro mediante servidores MCP, además de proporcionarles el contexto de tu repositorio de código. Esto permite que los desarrolladores usen un único flujo de trabajo para pedirle al modelo que examine los errores de un punto de acceso específico; después, el modelo puede usar ese contexto para explorar el repositorio de código y encontrar errores o problemas de rendimiento relacionados. Como los agentes de programación también pueden utilizar herramientas de línea de comandos, pueden consultar el historial de git para identificar cambios específicos que podrían haber causado los problemas reflejados en las trazas de los registros.

### Qué hacen los ingenieros en su lugar

Al automatizar los aspectos tediosos del análisis de registros y la clasificación inicial de incidentes, la IA permite que los ingenieros se concentren en resolver problemas de mayor nivel y mejorar el sistema. En vez de correlacionar manualmente registros, commits y cambios de infraestructura, pueden centrarse en validar las causas raíz identificadas por la IA, diseñar correcciones resilientes y desarrollar medidas preventivas. Este cambio reduce el tiempo dedicado a resolver problemas de forma reactiva y permite que los equipos dediquen más energía a la ingeniería proactiva de confiabilidad y a las mejoras arquitectónicas.

| Delegación                                                                                                                                                      | Revisión                                                                                                                                                                      | Responsabilidad                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Muchas tareas operativas pueden delegarse a agentes: analizar registros, detectar métricas anómalas, identificar cambios de código sospechosos e incluso proponer correcciones urgentes. | Los ingenieros evalúan y perfeccionan los diagnósticos generados por IA, confirman su exactitud y aprueban las medidas correctivas. Se aseguran de que las correcciones cumplan los estándares de confiabilidad, seguridad y cumplimiento normativo. | Las decisiones críticas siguen en manos de los ingenieros, en especial cuando se trata de nuevos tipos de incidentes, cambios delicados en producción o situaciones en las que el nivel de confianza del modelo es bajo. El criterio y la aprobación final siguen siendo responsabilidad de las personas. |

Ejemplo:

Virgin Atlantic utiliza Codex para fortalecer la forma en que sus equipos despliegan y mantienen sus sistemas. Con Codex VS Code Extension, los ingenieros cuentan con un único lugar para investigar registros, rastrear problemas en el código y los datos, y revisar cambios mediante Azure DevOps MCP y Databricks Managed MCPs. Al unificar este contexto operativo dentro del IDE, Codex acelera la identificación de causas raíz, reduce la clasificación manual de incidentes y ayuda a los equipos a concentrarse en validar las correcciones y mejorar la confiabilidad del sistema.

### Lista de verificación de primeros pasos

- Conecta las herramientas de IA a los sistemas de registro y despliegue: integra Codex CLI o una herramienta similar con tus servidores MCP y agregadores de registros.
- Define los ámbitos de acceso y los permisos: asegúrate de que los agentes puedan acceder a los registros pertinentes, los repositorios de código y los historiales de despliegue, sin dejar de aplicar las prácticas recomendadas de seguridad.
- Configura plantillas de prompts: crea prompts reutilizables para consultas operativas comunes, como “Investiga los errores del punto de acceso X” o “Analiza los picos de actividad en los registros después del despliegue”.
- Prueba el flujo de trabajo: ejecuta simulaciones de incidentes para asegurarte de que la IA muestre el contexto correcto, rastree el código con precisión y proponga diagnósticos que permitan tomar medidas.
- Itera y mejora: recopila comentarios de incidentes reales, ajusta las estrategias de prompts y amplía las capacidades de los agentes a medida que evolucionen tus sistemas y procesos.
  <br />

## Conclusión

Los agentes de programación están transformando el ciclo de vida del desarrollo de software al encargarse del trabajo mecánico y de varios pasos que tradicionalmente ha ralentizado a los equipos de ingeniería. Gracias al razonamiento sostenido, al contexto unificado del repositorio de código y a la capacidad de ejecutar herramientas reales, estos agentes ahora se ocupan de tareas que abarcan desde la definición del alcance y la creación de prototipos hasta la implementación, las pruebas, la revisión e incluso la clasificación inicial de incidentes operativos. Los ingenieros mantienen firmemente el control de la arquitectura, los objetivos del producto y la calidad, pero los agentes de programación realizan cada vez más la implementación inicial y colaboran de forma continua en cada fase del SDLC.

Este cambio no exige una transformación radical; los flujos de trabajo pequeños y específicos generan beneficios acumulativos con rapidez a medida que los agentes de programación se vuelven más capaces y confiables. Los equipos que comienzan con tareas de alcance bien definido, invierten en mecanismos de control y amplían de forma iterativa las responsabilidades de los agentes logran mejoras significativas en la velocidad, la consistencia y la capacidad del equipo de desarrollo para concentrarse.

Si estás evaluando cómo los agentes de programación pueden acelerar el trabajo de tu organización o te preparas para tu primer despliegue, ponte en contacto con OpenAI. Estamos aquí para ayudarte a convertir los agentes de programación en una ventaja real: diseñamos flujos de trabajo integrales para la planificación, el diseño, el desarrollo, las pruebas, la revisión y las operaciones, y ayudamos a tu equipo a adoptar patrones listos para producción que hagan realidad la ingeniería nativa de IA.

[image1]: /images/codex/guides/build-ai-native-engineering-team.png

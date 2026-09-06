<!-- source: https://learn.chatgpt.com/es-419/docs/security/faq -->

Estas preguntas frecuentes tratan sobre Codex Security en la nube. Para conocer los análisis locales y los flujos de trabajo que se ejecutan en
una tarea de Codex, consulta el [inicio rápido del Plugin de Codex Security](/es-419/codex/security/plugin).

{/* vale Microsoft.Auto = NO */}
{/* vale Vale.Spelling = NO */}

## Primeros pasos

### ¿Qué es Codex Security?

La seguridad del software sigue siendo uno de los problemas más difíciles e importantes de la ingeniería. Codex Security es un conjunto de herramientas de análisis de seguridad basado en LLM que inspecciona el código fuente y devuelve hallazgos estructurados y priorizados sobre vulnerabilidades, junto con parches propuestos. Ayuda a los desarrolladores y a los equipos de seguridad a detectar y corregir problemas de seguridad a escala.

### ¿Por qué es importante?

El software es fundamental para la industria y la sociedad modernas, y las vulnerabilidades generan riesgos sistémicos. Codex Security facilita un flujo de trabajo que prioriza a los defensores mediante la identificación continua de posibles problemas, su validación cuando es posible y la propuesta de correcciones. Así, los equipos pueden mejorar la seguridad sin ralentizar el desarrollo.

### ¿Qué problema de negocio resuelve Codex Security?

Codex Security acorta el proceso que va desde un posible problema hasta un hallazgo confirmado y reproducible, con evidencia y un parche propuesto. Esto reduce el trabajo de evaluación inicial y la cantidad de falsos positivos en comparación con el uso exclusivo de analizadores tradicionales.

### ¿Cómo funciona Codex Security?

Codex Security ejecuta el análisis en un contenedor efímero y aislado, y clona temporalmente el repositorio de destino. Realiza un análisis a nivel del código y devuelve hallazgos estructurados con una descripción, el archivo y la ubicación, la criticidad, la causa raíz y una corrección sugerida.

En los hallazgos que incluyen pasos de verificación, el sistema ejecuta los comandos o las pruebas propuestos en el mismo sandbox, registra el éxito o el fallo, los códigos de salida, stdout, stderr, los resultados de las pruebas y cualquier diff o artefacto generado, y adjunta esa salida como evidencia para su revisión.

### ¿Reemplaza a SAST?

No. Codex Security complementa a SAST. Incorpora razonamiento semántico basado en LLM y validación automática, mientras que las herramientas SAST existentes siguen ofreciendo una amplia cobertura determinista.

## Funciones

### ¿En qué consiste el proceso de análisis?

Codex Security sigue un proceso por etapas:

1. **El análisis** crea un modelo de amenazas para el repositorio.
2. **El análisis de commits** revisa los commits integrados y el historial del repositorio para detectar posibles problemas.
3. **La validación** intenta reproducir posibles vulnerabilidades en un sandbox para reducir los falsos positivos.
4. **La generación de parches** se integra con Codex para proponer parches que los revisores pueden inspeccionar antes de abrir un PR.

Trabaja junto con los ingenieros en GitHub, Codex y los flujos de revisión habituales.

### ¿Qué lenguajes se admiten?

Codex Security es independiente del lenguaje. En la práctica, el rendimiento depende de la capacidad de razonamiento del modelo para el lenguaje y el framework que usa el repositorio.

### ¿Qué resultados obtengo al finalizar el análisis?

Obtienes hallazgos priorizados con su nivel de criticidad, estado de validación y, cuando está disponible, un parche propuesto. Los hallazgos también pueden incluir la salida del fallo, evidencia de reproducción, contexto de la ruta de llamadas y anotaciones relacionadas.

### ¿Cómo se aísla el código del cliente?

Cada tarea de análisis y validación se ejecuta en un contenedor efímero de Codex con herramientas cuyo alcance se limita a esa sesión. Los artefactos se extraen para revisarlos y el contenedor se elimina al finalizar la tarea.

### ¿Codex Security aplica los parches automáticamente?

No. El parche propuesto es una corrección recomendada. Los usuarios pueden revisarlo y enviarlo a GitHub como un PR desde la interfaz de hallazgos, pero Codex Security no aplica cambios automáticamente al repositorio.

### ¿Es necesario compilar el proyecto para analizarlo?

No. Codex Security puede generar hallazgos a partir del contexto del repositorio y de los commits sin un paso de compilación. Durante la validación automática, puede intentar compilar el proyecto dentro del contenedor si eso ayuda a reproducir el problema. Para obtener información sobre la configuración del entorno, consulta [Entornos en la nube de Codex](/es-419/codex/environments/cloud-environment).

### ¿Cómo reduce Codex Security los falsos positivos y evita los parches que no funcionan?

Codex Security utiliza dos etapas. Primero, el modelo prioriza los posibles problemas. Luego, la validación automática intenta reproducir cada problema en un contenedor limpio. Los hallazgos que se reproducen correctamente se marcan como validados, lo que ayuda a reducir los falsos positivos antes de la revisión humana.

### ¿Cuánto tardan los análisis iniciales y qué ocurre después?

El tiempo del análisis inicial depende del tamaño del repositorio, el tiempo de compilación y cuántos hallazgos pasan a la validación. En algunos repositorios, los análisis pueden tardar varias horas. En repositorios más grandes, pueden tardar varios días. Los análisis posteriores suelen ser más rápidos porque se centran en commits nuevos y cambios incrementales.

### ¿Qué es un modelo de amenazas?

Un modelo de amenazas es el contexto de seguridad de un repositorio que se usa durante el análisis. Combina una descripción general concisa del proyecto con detalles de la superficie de ataque, como puntos de entrada, límites de confianza, supuestos de autenticación y componentes riesgosos. Para obtener más información, consulta [Mejorar el modelo de amenazas](/es-419/codex/security/threat-model).

### ¿Cómo se genera un modelo de amenazas?

Codex Security le pide al modelo que resuma la arquitectura del repositorio y sus puntos de entrada relevantes para la seguridad, clasifique el tipo de repositorio, ejecute extractores especializados y combine los resultados en una descripción general del proyecto o en un artefacto de modelo de amenazas que se usa durante todo el análisis.

### ¿Reemplaza la revisión manual de seguridad?

No. Codex Security agiliza la revisión y ayuda a priorizar los hallazgos, pero no reemplaza la validación a nivel del código, las comprobaciones de explotabilidad ni la evaluación humana de amenazas.

### ¿Puedo editar el modelo de amenazas?

Sí. Codex Security crea el modelo de amenazas inicial y puedes actualizarlo a medida que cambien la arquitectura, los riesgos y el contexto del negocio. Para conocer el flujo de edición, consulta [Mejorar el modelo de amenazas](/es-419/codex/security/threat-model).

### ¿Necesito configurar un análisis antes de usar el modelado de amenazas?

Sí. Las pautas para el modelo de amenazas dependen de qué analizas y cómo lo haces, por lo que primero debes configurar el repositorio. Consulta [Configuración de Codex Security](/es-419/codex/security/setup).

### ¿Qué incluye el parche propuesto?

Cuando se puede generar una corrección para el hallazgo, el parche propuesto incluye un diff mínimo y aplicable con el nombre del archivo y el contexto de las líneas.

### ¿El parche modifica directamente la rama de mi PR?

No. El flujo de trabajo genera un diff, un archivo de parche o un cambio sugerido que los responsables de mantenimiento y los revisores pueden inspeccionar antes de aplicarlo.

## Validación

### ¿Qué es la validación automática?

La validación automática es la fase que intenta reproducir un posible problema en un contenedor aislado. Registra si la reproducción tuvo éxito o falló, y recopila registros, comandos y artefactos relacionados como evidencia.

### ¿Qué ocurre si falla la validación?

El hallazgo permanece sin validar. Los registros y los informes siguen documentando lo que se intentó para que los ingenieros puedan volver a intentarlo, investigar más a fondo o ajustar los pasos de reproducción.

{/* vale Microsoft.Auto = YES */}
{/* vale Vale.Spelling = YES */}

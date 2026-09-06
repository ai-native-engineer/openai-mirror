<!-- source: https://learn.chatgpt.com/es-419/use-cases/datasets-and-reports -->

## Introducción

En esencia, el análisis de datos consiste en usar los datos para fundamentar decisiones. El objetivo no es analizar por analizar, sino producir un entregable que ayude a alguien a actuar: un gráfico para el equipo directivo, un resumen de resultados de un experimento para un equipo de producto, una evaluación de un modelo para investigadores o un panel que guíe las operaciones diarias.

Un marco útil, popularizado por _R for Data Science_, consiste en un ciclo: importar y ordenar los datos, y luego alternar entre transformarlos, visualizarlos y modelarlos para comprenderlos mejor antes de comunicar los resultados.

ChatGPT Work encaja bien en este flujo de trabajo. Te ayuda a limpiar datos, explorar hipótesis, generar análisis y crear entregables reproducibles. El objetivo no es crear un notebook de un solo uso, sino un análisis que otras personas puedan revisar, en el que puedan confiar y que puedan volver a ejecutar.

## Define tu caso de uso

Elige una pregunta concreta que quieras responder con tus datos. Cuanto más específica sea la pregunta, más fácil será identificar los datos de entrada, las verificaciones y el resultado adecuados.

### Ejemplo que usaremos: valor de las propiedades cerca de la autopista

Como ejemplo, exploraremos la siguiente pregunta:

> ¿Hasta qué punto tienen menor valor las casas cercanas a la autopista?

Supongamos que un conjunto de datos contiene el valor de las propiedades o los precios de venta, y otro contiene información sobre la ubicación, las parcelas o la proximidad a la autopista. El trabajo no consiste solo en ejecutar un modelo. También hay que asegurarse de que los datos de entrada sean confiables, documentar las uniones, poner a prueba el resultado y terminar con un entregable que otra persona pueda usar.

Puedes adjuntar archivos CSV o libros de Excel, mencionar una hoja de cálculo de Google aprobada con `@google-drive`, o usar la app de escritorio cuando tus datos estén guardados en tu computadora.

<div data-use-case-export-only>

### Resultado del ejemplo

En una muestra ficticia, ChatGPT vincula 11 ventas de propiedades con el archivo de distancias a la autopista y señala una venta sin una distancia correspondiente. Las viviendas situadas a una milla o menos de la autopista tienen un valor promedio de **$500 000**, frente a **$600 000** en el caso de las viviendas situadas a una distancia de entre dos y cinco millas.

Tras excluir la propiedad con el precio más alto del grupo más alejado, la diferencia sigue siendo de **$94 000**. El informe y el gráfico explican que la muestra es pequeña, que se excluyó la venta sin coincidencia y que la comparación no demuestra causalidad ni tiene en cuenta factores como el vecindario, el momento de la venta, el tráfico o el ruido.

</div>

## Importar los datos

Comienza por adjuntar los archivos y pedirle a ChatGPT que los inspeccione. Esto ayuda a responder preguntas básicas pero importantes:

- ¿Qué formatos de archivo hay?
- ¿Qué parece representar cada conjunto de datos?
- ¿Qué columnas podrían ser variables objetivo, identificadores, fechas, ubicaciones o mediciones?
- ¿Qué problemas de calidad son evidentes?

No pidas conclusiones todavía. Solicita primero un inventario y una explicación.

## Preparar y combinar los datos de entrada

La mayor parte del trabajo real comienza aquí. Tienes dos o más conjuntos de datos, la clave primaria no está clara y combinarlos sin cuidado podría provocar pérdida de datos o duplicados.

Pídele a ChatGPT que evalúe la combinación antes de realizarla:

- Comprueba la unicidad de las claves candidatas.
- Mide las tasas de valores nulos y las diferencias de formato.
- Normaliza los problemas evidentes de formato, como el uso de mayúsculas y minúsculas, los espacios en blanco o el formato de las direcciones.
- Realiza uniones de prueba e informa las tasas de coincidencia.
- Recomienda la estrategia de combinación más segura antes de crear el archivo combinado final.

Si necesitas determinar la mejor clave, como una dirección normalizada, un identificador de parcela creado a partir de unas pocas columnas o una unión por ubicación, pídele a ChatGPT que explique las ventajas y desventajas y los casos extremos antes de aceptar la combinación.

## Explorar con gráficos

Usa gráficos para comprender los datos antes de elegir un modelo. En el ejemplo que venimos usando, compara las viviendas cercanas a la autopista con las más alejadas, examina los valores atípicos, inspecciona los patrones de valores faltantes y comprueba si el efecto aparente refleja la composición de los vecindarios, el tamaño de las viviendas u otro factor.

Mantén cada gráfico ligado a la pregunta original. Guarda las comparaciones útiles para que otra persona pueda inspeccionar el análisis.

## Responder la pregunta con un modelo

No todos los análisis requieren un modelo complejo. Comienza con un modelo base interpretable.

Para analizar la pregunta sobre la autopista, un primer enfoque razonable es usar una regresión u otro modelo transparente que estime la relación entre la cercanía a la autopista y el valor de las propiedades, teniendo en cuenta factores relevantes como el tamaño, la antigüedad y la ubicación.

Pídele a ChatGPT que indique explícitamente:

- La variable objetivo y las definiciones de las características.
- Qué variables de control incluir y por qué.
- Los riesgos de fuga de datos y las exclusiones.
- Cómo eligió la partición de los datos, el enfoque de evaluación o el método para estimar la incertidumbre.
- Qué significa el resultado en términos sencillos.

Si el primer modelo no da buenos resultados, eso también es útil. Te indica si el problema está en el modelo, las características, la calidad de la unión o la pregunta misma.

## Comunicar el resultado

El análisis solo es útil si alguien más puede aprovecharlo. Pídele a ChatGPT que genere el entregable que necesita la audiencia:

- Un memorando en Markdown para colaboradores técnicos.
- Una hoja de cálculo o un archivo CSV para los procesos posteriores.
- Un documento con formato o un PDF para quienes toman decisiones.
- Un notebook, un panel o un informe estático para un análisis reutilizable.

Pídele que incluya las salvedades. Si la calidad de la unión es imperfecta, existe sesgo de muestreo o los supuestos del modelo son frágiles, el entregable debe indicarlo con claridad.

## Opcional: configurar un entorno de Python

Si el proyecto requiere scripts reutilizables o un notebook, pídele a ChatGPT que use el entorno de Python existente o configure uno mínimo y reproducible. Conserva los archivos de origen sin cambios y guarda por separado el análisis, los gráficos y el informe final. No necesitas configurar Python antes de analizar archivos adjuntos en ChatGPT Work.

## Prompts sugeridos

**Carga los conjuntos de datos y explícalos**

**Revisa la combinación antes de unir los datos**

**Crea un primer modelo interpretable**

**Prepara los resultados para las partes interesadas**

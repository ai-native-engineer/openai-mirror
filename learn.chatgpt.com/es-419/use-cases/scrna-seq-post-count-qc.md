<!-- source: https://learn.chatgpt.com/es-419/use-cases/scrna-seq-post-count-qc -->

## Aprovecha las habilidades

El complemento NGS Analysis incluye:

- `ngs-analysis-router`
- `scrna-seq-qc`
- `ngs-scrna-seq`

Cuando usas el complemento, ChatGPT puede utilizar todas las habilidades incluidas.

## Guía paso a paso

1. Indícale a ChatGPT la matriz, los códigos de barras, los genes o las características, el archivo de manifiesto y los metadatos del conjunto de datos que debe usar, o proporciona referencias exactas a los archivos.
2. Ejecuta el prompt inicial para que ChatGPT pueda elegir los umbrales de control de calidad a partir de las distribuciones observadas y registrar la justificación en los artefactos de la ejecución.
3. Abre el índice de visualizaciones y el notebook o la aplicación de revisión para inspeccionar los conteos de células que superaron o no superaron el control de calidad, los UMAP y la confianza de las anotaciones.
4. Continúa en el mismo chat para ajustar los umbrales, proporcionar un atlas de referencia compatible o volver a ejecutar el análisis después de desbloquear la detección de dobletes.

## Resultados

La ejecución genera una interfaz para revisar las decisiones de filtrado, no solo una
matriz filtrada. Comienza con las gráficas que justifican los umbrales y el
resumen de control de calidad para ver cuántas células eliminó o marcó cada filtro y
si los valores de corte seleccionados coinciden con las distribuciones observadas.

![Revisa las gráficas que justifican los umbrales y los conteos de células que superaron o no superaron el control de calidad en una ejecución con datos de célula única.](/codex/use-cases/scrna-seq-post-count-qc-screenshot-1.webp)

Después, inspecciona los UMAP generados según la etiqueta general y el clúster de Leiden. Estas
vistas facilitan la identificación de anotaciones faltantes, clústeres sospechosos o
umbrales elegidos que requieren otra revisión.

![Inspecciona las gráficas UMAP según la etiqueta general y el clúster de Leiden.](/codex/use-cases/scrna-seq-post-count-qc-screenshot-2.webp)

Por último, revisa las métricas por célula y los resultados del filtrado. ChatGPT conserva
esta tabla junto con el archivo `.h5ad` filtrado y los artefactos de visualización para que puedas
ajustar los umbrales en el mismo chat sin perder la justificación del
análisis inicial.

![Abre las métricas de control de calidad por célula y los resultados del filtrado para revisarlos.](/codex/use-cases/scrna-seq-post-count-qc-screenshot-3.webp)

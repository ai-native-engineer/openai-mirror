<!-- source: https://learn.chatgpt.com/es-419/use-cases/bulk-rna-seq-fastq-qc -->

## Aprovecha las habilidades

El complemento NGS Analysis incluye:

- `ngs-analysis-router`
- `ngs-bulk-rnaseq-counts-qc`
- `ngs-runtime-env`

Al usar el complemento, ChatGPT puede utilizar todas las habilidades incluidas en él.

## Guía paso a paso

1. Indica a ChatGPT el directorio que contiene la hoja de muestras, los archivos FASTQ, el archivo FASTA del transcriptoma, el archivo FASTA del genoma y el archivo GTF, o proporciona referencias exactas de los archivos.
2. Ejecuta el prompt inicial para que ChatGPT valide la especificidad de hebra de la biblioteca y la coherencia entre las referencias, y compruebe que las herramientas estén listas antes de iniciar la ejecución.
3. Abre en ChatGPT los artefactos de MultiQC y las matrices generados para revisar la tasa de mapeo, la duplicación y la concordancia del tipo de biblioteca, y comprobar si los recursos están listos.
4. Continúa en el mismo chat para resolver los bloqueos, volver a ejecutar con metadatos actualizados o pasar las matrices resultantes a nivel de genes al análisis posterior de expresión diferencial.

## Resultados

La ejecución devuelve un paquete de conteos revisado mediante control de calidad, en lugar de un resultado de cuantificación
sin revisión. Comienza por revisar el informe de MultiQC para identificar advertencias que podrían afectar
la interpretación posterior. En este ejemplo, ChatGPT muestra las advertencias de FastQC
sobre el contenido de las secuencias junto con el resumen de la ejecución para que el equipo pueda decidir
si el patrón observado es el esperado para la preparación de la biblioteca.

![Revisa las advertencias de FastQC sobre el contenido de las secuencias junto con el resumen de la ejecución de RNA-seq bulk.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-1.webp)

A continuación, revisa las estadísticas de Salmon en el mismo informe. Las tasas de mapeo,
las asignaciones del tipo de biblioteca y los indicadores de duplicación ofrecen una forma rápida y concisa de comprobar que todo esté listo
antes del análisis de expresión diferencial.

![Examina las estadísticas de Salmon sobre alineamiento y tipo de biblioteca en el informe de MultiQC generado.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-2.webp)

La matriz de conteos a nivel de genes resultante se guarda como un artefacto reutilizable. Ábrela
en ChatGPT para confirmar que contiene las muestras y características esperadas; luego, consérvala
junto con los datos de procedencia de la ejecución para el análisis posterior.

![Abre la matriz de conteos a nivel de genes generada para revisarla posteriormente.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-3.webp)

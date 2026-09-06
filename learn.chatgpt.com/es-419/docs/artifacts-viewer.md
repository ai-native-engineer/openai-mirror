<!-- source: https://learn.chatgpt.com/es-419/docs/artifacts-viewer -->

Cuando una tarea genere un archivo, proporciona a ChatGPT los datos de origen, el tipo de archivo esperado,
la estructura y los criterios de revisión pertinentes para la tarea. Las herramientas de vista previa y revisión
dependen de la interfaz que uses.

La aplicación de escritorio de ChatGPT muestra vistas previas de los documentos, las presentaciones,
las hojas de cálculo y los archivos PDF generados junto al chat. Cuando las vistas previas automáticas están
activadas, la aplicación puede abrir un archivo generado al finalizar una tarea.

Cuando hay vistas previas HTML disponibles, los archivos `.html` y `.htm` generados también pueden
abrirse como vistas previas interactivas. Alterna entre la vista previa renderizada y la vista
del código fuente para inspeccionar el resultado o el HTML subyacente.

Usa anotaciones para señalar una parte específica de una vista previa compatible y solicitar
una revisión puntual.

En ChatGPT Work en la web, adjunta archivos de origen o pídele a ChatGPT que cree un
documento, una presentación, una hoja de cálculo o un PDF. Revisa el archivo generado en el
chat, descárgalo cuando sea necesario y proporciona comentarios específicos para la siguiente versión.

Codex CLI puede crear y editar archivos en el directorio de trabajo, pero no
incluye una vista previa visual de los archivos ni una interfaz de anotaciones. Pídele a Codex que indique cada
ruta de salida y las comprobaciones que ejecutó.

La extensión para IDE puede crear y editar archivos en el espacio de trabajo. Revisa los archivos de texto y
de código en el editor, y abre documentos, presentaciones, hojas de cálculo o
archivos PDF en un visor compatible.

  
    
  

## Crear archivos para su revisión

Para las hojas de cálculo y las presentaciones, describe las hojas, las columnas, los gráficos,
las secciones de las diapositivas y las comprobaciones esperadas. Pídele a ChatGPT que explique dónde guardó el
archivo de salida y cómo comprobó el resultado.

<a id="refine-files-with-annotations"></a>
<span id="follow-artifact-work"></span>
<a id="review-and-refine-files"></a>

## Perfeccionar archivos con anotaciones

Las anotaciones te permiten señalar una parte específica de un archivo e indicarle a ChatGPT
qué debe cambiar. El mismo flujo de trabajo de anotaciones disponible para código, archivos Markdown
y sitios web también funciona con documentos, hojas de cálculo y
presentaciones.

Por ejemplo, puedes:

- Selecciona una barra de navegación de un sitio web y pídele a ChatGPT que cambie su tipografía.
- Resalta una afirmación en una tesis de inversión y solicita su fuente.
- Marca un gráfico en una diapositiva y solicita una etiqueta más clara.

ChatGPT usa el área seleccionada como contexto para tu solicitud, de modo que puedes perfeccionar
el archivo sin empezar de cero ni cambiar las partes que ya te gustan.
Las anotaciones son especialmente útiles después del primer borrador, cuando el trabajo requiere
revisión y ajustes sucesivos.

## Revisar y perfeccionar archivos en la web

Abre o descarga el archivo generado para revisarlo en el visor adecuado.
Cuando solicites una revisión, indica la página, la diapositiva, la hoja, la tabla o el fragmento que
requiere atención y describe qué debe quedar sin cambios. Pídele a ChatGPT que indique
el nuevo nombre del archivo y las comprobaciones que realizó antes de que descargues la siguiente
versión.

## Revisar y perfeccionar archivos

Usa la barra lateral del chat mientras se ejecuta una tarea. Puede mostrar el plan del agente,
las fuentes, los archivos generados y el resumen del chat para que puedas orientar el trabajo,
inspeccionar los archivos generados y solicitar otra revisión.

Pídele a ChatGPT que explique dónde guardó cada archivo y cómo verificó el
resultado. Usa la vista previa para inspeccionarlo y luego proporciona comentarios específicos sobre
la estructura, los datos, el diseño o la validación que necesiten una nueva revisión.

## Documentación relacionada

- [Generación de imágenes](/es-419/codex/image-generation)

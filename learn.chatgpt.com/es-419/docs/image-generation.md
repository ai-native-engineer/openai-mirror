<!-- source: https://learn.chatgpt.com/es-419/docs/image-generation -->

Pídele a ChatGPT que genere o edite imágenes. Usa la generación de imágenes para recursos de la interfaz de usuario,
banners, fondos, ilustraciones, hojas de sprites y marcadores de posición que quieras
crear junto con el código o en un chat de ChatGPT.

Pide una imagen desde el Editor de la App. Agrega una imagen de referencia cuando quieras
que ChatGPT transforme un recurso existente o lo use como guía visual.

### Revisar y editar imágenes generadas

Selecciona una imagen generada para abrirla en el visor ampliado. Alterna entre
**Vista enfocada** para examinar una imagen y **Vista de canvas** para ver las imágenes
generadas en el mismo chat.

En **Vista de canvas**, usa **Comentar** para agregar comentarios precisos a una o más
imágenes. Selecciona **Selección múltiple** para elegir las imágenes que quieras incluir y luego
envía tus comentarios y cualquier instrucción de edición adicional en el mismo chat.
Describe qué debe cambiar y qué debe permanecer igual.

Pide una imagen en un chat de la versión web de ChatGPT. Adjunta una imagen de referencia al
Editor cuando quieras que ChatGPT la edite o la use como guía visual.

Describe la imagen en una sesión interactiva o incluye `$imagegen` para invocar
explícitamente la habilidad de generación de imágenes. Adjunta una imagen existente con `-i` o
`--image` cuando deba servir como guía para el resultado.

Pide una imagen desde el chat de la extensión. Arrastra una imagen de referencia al
Editor mientras mantienes presionada la tecla <kbd>Shift</kbd> cuando quieras que Codex edite o use como punto de partida
un recurso existente.

## Generar o editar una imagen

Describe la imagen en lenguaje natural. Agrega una imagen de referencia cuando quieras
que ChatGPT transforme o amplíe un recurso existente.

Incluye `$imagegen` en tu prompt para invocar la habilidad de generación de imágenes
de forma explícita.

La generación de imágenes integrada usa `gpt-image-2` y se contabiliza en tus límites generales
de uso de Codex. Las generaciones de imágenes consumen los límites incluidos entre 3 y 5 veces más rápido, en
promedio, que turnos similares sin generación de imágenes, según la calidad
y el tamaño de la imagen. Para lotes más grandes, configura `OPENAI_API_KEY` en tu entorno y pide a
ChatGPT que genere imágenes mediante la API para que se apliquen los precios de la API.

La disponibilidad de imágenes y los límites de uso en la versión web de ChatGPT dependen de tu plan y de la
configuración del espacio de trabajo. Para generar imágenes mediante programación, usa la [API de
generación de imágenes](/api/docs/guides/image-generation).

## Escribir prompts eficaces para imágenes

Un prompt de imagen útil suele tener solo de una a tres oraciones claras. Describe los
detalles que determinan si el resultado será satisfactorio:

- Explica el propósito de la imagen o el público al que está dirigida.
- Indica cuál es el tema principal y qué está sucediendo.
- Describe el entorno, la composición y el estilo visual.
- Especifica el encuadre, las dimensiones, la iluminación, los colores o los materiales cuando sean importantes.
- Indica las restricciones, incluido todo aquello que la imagen no deba contener.

Prefiere un lenguaje visual concreto en lugar de apreciaciones generales. Por ejemplo, describe
de dónde viene la luz en vez de pedir una “iluminación bonita”. Repite cualquier
requisito que deba mantenerse sin cambios.

## Perfeccionar el resultado

Comienza con la idea principal y luego haz revisiones pequeñas y específicas. Ajusta un
elemento a la vez para evitar que cambien la composición y otros detalles importantes.
También puedes seleccionar un área específica de una imagen y describir el cambio que quieres aplicar en esa
área.

Cuando edites una imagen existente, indica con exactitud qué debe cambiar y qué debe
permanecer igual.

Para revisiones más amplias, da indicaciones directas y concretas: aumenta el brillo de la imagen,
reduce la saturación de los colores, simplifica el fondo o mantén la
composición mientras cambias el estilo.

## Usar varias imágenes de referencia

Usa un conjunto pequeño de imágenes de referencia cuando una defina el contenido y
otra defina el estilo, la disposición u otros lineamientos visuales. Identifica cada
imagen según su orden y explica cómo se relacionan entre sí. Usa términos espaciales como
primer plano, fondo, izquierda y derecha al combinar elementos.

## Agregar texto a una imagen

Mantén breve el texto dentro de la imagen y especifícalo con precisión. Escribe el texto exacto entre
comillas, conserva el uso de mayúsculas y minúsculas que quieras y describe el estilo tipográfico, el
tamaño, el color y la ubicación. Si se trata de un nombre poco común, deletréalo
cuando sea importante que aparezca con exactitud. Indica si se permite incluir algún otro texto.

## Crear infografías y diseños con mucho contenido

La generación de imágenes puede ayudarte a crear borradores de materiales explicativos, pósteres, diagramas con etiquetas,
líneas de tiempo y otros recursos visuales con mucha información. Describe la jerarquía de la
información y la disposición, usa etiquetas concisas y pide que el texto se vea nítido.
Cuando haya mucho texto o la tipografía sea crucial para la producción, revisa cada palabra y termina
el recurso en una herramienta de diseño si es necesario.

## Consideraciones adicionales

- **Ten cuidado al usar la imagen de otras personas.** Cuando representes a una persona real, proporciona una
  foto de referencia cuando corresponda y confirma que tienes permiso para usar
  su imagen.
- **Solicita un enfoque original.** Pide un diseño genérico u original
  en lugar de imitar una marca, un producto, un artista o una obra de arte específicos.
- **Dar crédito es opcional.** No tienes que dar crédito a OpenAI por las imágenes generadas,
  aunque puedes explicar cómo se creó un recurso cuando ese contexto sea útil.
- **Cumple las políticas aplicables.** Usa las imágenes de acuerdo con los
  lineamientos de tu organización y las [políticas de
  uso de OpenAI](https://openai.com/policies/usage-policies/).

## Documentación relacionada

- [Precios de Codex](/es-419/codex/pricing#image-generation-usage-limits)
- [Entradas de imágenes](/es-419/codex/image-inputs)
- [Guía de la API de generación de imágenes](/api/docs/guides/image-generation)
- [Trabajar con archivos](/es-419/codex/artifacts-viewer)
- [Crear imágenes con ChatGPT](https://openai.com/academy/image-generation/)

  
    <span slot="icon">
      
    </span>
    Explora más prompts y resultados de generación de imágenes.
  

- [Entradas de imágenes](/es-419/codex/image-inputs)
- [Guía de la API de generación de imágenes](/api/docs/guides/image-generation)
- [Trabajar con archivos](/es-419/codex/artifacts-viewer)
- [Crear imágenes con ChatGPT](https://openai.com/academy/image-generation/)

  
    <span slot="icon">
      
    </span>
    Explora más prompts y resultados de generación de imágenes.
  

- [Precios de Codex](/es-419/codex/pricing#image-generation-usage-limits)
- [Entradas de imágenes](/es-419/codex/image-inputs)
- [Guía de la API de generación de imágenes](/api/docs/guides/image-generation)
- [Trabajar con archivos](/es-419/codex/artifacts-viewer)

  
    <span slot="icon">
      
    </span>
    Explora más prompts y resultados de generación de imágenes.

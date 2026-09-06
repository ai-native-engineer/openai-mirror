<!-- source: https://learn.chatgpt.com/es-419/use-cases/chatgpt-apps -->

## Qué crearás

Todo complemento basado en MCP tiene tres partes:

- Un servidor MCP que define herramientas, devuelve datos, exige autenticación y le indica a ChatGPT qué recursos de interfaz de usuario debe usar.
- Un componente web opcional que se renderiza dentro de un iframe de ChatGPT. Puedes crearlo con React o con HTML, CSS y JavaScript puros.
- Un modelo que decide cuándo llamar a las herramientas del complemento según los metadatos que proporciones.

Codex resulta más útil cuando se encarga de las tareas de ingeniería repetitivas relacionadas con esas partes:

- Planificar el conjunto de herramientas y sus metadatos.
- Crear la estructura inicial del servidor y el widget.
- Configurar los scripts de ejecución local.
- Agregar cambios de autenticación y despliegue en iteraciones bien delimitadas.
- Crear el ciclo de verificación que demuestra que el complemento funciona en ChatGPT.

## Por qué Codex es una excelente opción

- Los complementos basados en MCP se dividen claramente en un servidor, una interfaz de usuario opcional y
llamadas a herramientas guiadas por el modelo.
- El diseño de prompts para Codex da mejores resultados cuando la tarea es explícita, acotada y
fácil de verificar, lo que se adapta bien al trabajo de creación de complementos.
- Las Habilidades y `AGENTS.md` le proporcionan a Codex las instrucciones reutilizables y las reglas del proyecto que necesita para apegarse al contexto.

Para obtener más información sobre cómo instalar y usar las Habilidades, consulta nuestra [documentación sobre Habilidades](/es-419/codex/build-skills).

## Cómo usarlo

## Requisitos previos

- Comienza con un resultado principal para el usuario en lugar de intentar trasladar un producto completo al chat.
- Elige el stack desde el principio: TypeScript o Python para el servidor y React o HTML, CSS y JavaScript puros para el widget.
- Decide cómo habilitarás HTTPS durante el desarrollo, por ejemplo, con `ngrok` o Cloudflare Tunnel.
- Algunas opciones de configuración todavía usan terminología antigua para referirse a la conexión con un servidor MCP. Durante
las pruebas locales, interpreta esas etiquetas como referencias al servidor registrado.

1. Comienza con un único resultado concreto para el complemento y pídele a Codex que proponga entre tres y cinco herramientas con nombres claros y con descripciones, entradas y salidas bien definidas.
2. Decide si la v1 puede limitarse a datos o necesita un widget. Luego, antes de agregar dependencias, crea la estructura inicial del servidor MCP y del widget opcional siguiendo los patrones existentes en el repositorio.
3. Ejecuta el servidor MCP de forma local mediante HTTPS, conéctalo en el modo de desarrollador de ChatGPT y pruébalo con un conjunto pequeño de prompts directos, indirectos y negativos.
4. Ajusta de forma iterativa los metadatos, el manejo del estado, `structuredContent` y las cargas útiles de `_meta` hasta que el flujo principal de lectura funcione de manera confiable dentro de ChatGPT.
5. Agrega OAuth 2.1 solo cuando los datos específicos del usuario o las acciones de escritura lo requieran, sin complicar los flujos anónimos o de solo lectura.
6. Prepara una vista previa alojada con un punto de acceso `/mcp` estable, verifica el streaming y el alojamiento de los recursos de la interfaz de usuario, y revisa la lista de verificación de lanzamiento antes de compartir o enviar el complemento.

## Prompts sugeridos

Los prompts eficaces para este flujo de trabajo tienen los mismos elementos:

- Un resultado claro: indica qué debería poder hacer el usuario con ayuda del complemento dentro de ChatGPT.
- Un stack concreto: indica si quieres usar TypeScript o Python en el servidor y si el widget debe usar React o mantenerse ligero.
- Límites explícitos para las herramientas: pídele a Codex que proponga o cree un conjunto pequeño de herramientas, cada una dedicada a una sola tarea.
- Necesidades de autenticación: indica si la primera versión puede ser anónima o si necesita cuentas vinculadas y acciones de escritura.
- Una vía de desarrollo local: menciona el túnel o la opción de alojamiento que prevés usar para las pruebas HTTPS en ChatGPT.
- Pasos de verificación: dile a Codex qué comandos ejecutar, qué prompts probar y qué evidencia debe incluir en la respuesta.

Evita usar un único prompt enorme que pida planificar, implementar, configurar la autenticación, desplegar, enviar y pulir todo de una sola vez. En su lugar, divide el trabajo en hitos más pequeños.

**Planifica el complemento antes de crear su estructura inicial**

**Crea la estructura inicial de la primera versión funcional**

**Agrega autenticación solo después de que funcione el flujo principal**

**Prepara el complemento para el despliegue y la revisión**

## Preparación para el lanzamiento

- El complemento se centra en un único resultado acotado y fácil de entender para los usuarios.
- El conjunto de herramientas sigue siendo reducido y tiene metadatos, entradas y salidas definidos de forma explícita.
- El servidor MCP funciona de extremo a extremo y devuelve datos concisos en `structuredContent`; los datos exclusivos del widget quedan reservados para `_meta`.
- El widget, si es necesario, se renderiza correctamente dentro de ChatGPT.
- El ciclo local de pruebas con HTTPS funciona en el modo de desarrollador de ChatGPT.
- Un pequeño conjunto de prompts directos, indirectos y negativos supera las pruebas con el flujo de conversación y los payloads de las herramientas esperados.
- La autenticación se agrega solo cuando los datos específicos del usuario o las acciones de escritura la requieren.
- Un plan de despliegue y una revisión de preparación para el lanzamiento abarcan los metadatos, las indicaciones sobre las herramientas, la privacidad y los prompts de prueba antes de compartir o enviar el complemento.

## Errores comunes

- Pedirle a Codex que lleve todo el producto a ChatGPT. Mejor opción: pide un único resultado principal para el usuario, entre tres y cinco herramientas y un solo widget bien delimitado.
- Empezar con un enorme prompt de implementación. Mejor opción: divide el trabajo en fases de planificación, creación de la estructura inicial, autenticación, despliegue y revisión.
- Escribir la interfaz de usuario antes de definir con claridad el contrato de las herramientas. Mejor opción: define primero el conjunto de herramientas y el esquema de respuesta; luego, crea el widget.
- No basarse en la documentación oficial. Mejor opción: usa `$chatgpt-apps` junto con `$openai-docs` para que la estructura inicial siga las pautas vigentes para complementos.
- Tratar los metadatos como algo secundario. Mejor opción: redacta desde el principio las descripciones de las herramientas y la documentación de los parámetros; luego, vuelve a ejecutar un conjunto de prompts para validar esos metadatos.
- Agregar la autenticación antes de validar el flujo anónimo o de solo lectura. Mejor opción: primero haz que funcione el flujo principal de las herramientas y luego agrega OAuth solo a las que realmente lo necesiten.
- Dar por terminado el complemento antes de probarlo dentro de ChatGPT. Mejor opción: conecta
el servidor MCP en modo de desarrollador, inspecciona los payloads de las herramientas y verifica el flujo real
de la conversación.

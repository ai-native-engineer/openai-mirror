<!-- source: https://learn.chatgpt.com/es-419/docs/appshots -->

Las capturas de la aplicación te permiten enviar la ventana de la app que está en primer plano a un chat de ChatGPT. Úsalas cuando
estés trabajando en otra app en tu computadora y quieras darle a
ChatGPT el contexto actual para que pueda ayudarte con la tarea.

  Las capturas de la aplicación están disponibles en la app de escritorio de ChatGPT para macOS. Presiona ambas teclas
Command o tu atajo de teclado personalizado para tomar una captura de la aplicación.

## Qué incluye una captura de la aplicación

Una captura de la aplicación abarca únicamente la ventana que está en primer plano. Puede incluir:

- Una imagen de la ventana visible.
- El texto disponible en esa ventana, incluido el texto visible y el que la app pone
a disposición fuera del área de desplazamiento visible.

Después de agregar una captura de la aplicación a un chat, esta se comporta como un archivo adjunto. ChatGPT
almacena las capturas de la aplicación de forma local en el archivo de sesión, al igual que los archivos o las imágenes que adjuntas
manualmente.

## Cuándo usar las capturas de la aplicación

Usa las capturas de la aplicación cuando ChatGPT necesite contexto de una app para Mac antes de poder actuar.

Ejemplos:

- Comparte una página de referencia de API y pídele a ChatGPT que escriba un script que la use.
- Comparte una vista de correo electrónico o de calendario y pídele a ChatGPT que prepare el siguiente paso.
- Comparte un editor de imágenes, un diseño o una ventana de vista previa y pídele a ChatGPT que ajuste los
recursos o el código relacionados.
- Comparte un error, un panel de configuración o un estado de la app que sea más fácil mostrar que
describir.

## Tomar una captura de la aplicación

1. Pon en primer plano la ventana de la app que quieras compartir.
2. Presiona ambas teclas Command o el atajo de teclado personalizado que configuraste para ChatGPT
en la configuración de la app.
3. Concede los permisos de macOS si ChatGPT te los solicita.
4. Pídele a ChatGPT que realice una tarea con la captura de la aplicación.

  

De forma predeterminada, ChatGPT inicia un chat nuevo para la captura de la aplicación. Si interactuaste con un
chat en los últimos 60 segundos, ChatGPT agrega la captura de la aplicación a ese chat
reciente, en lugar de iniciar uno nuevo. Las capturas consecutivas de la aplicación se agregan al mismo chat.

Puedes cambiar el atajo de teclado de las capturas de la aplicación en la configuración de la app.

## Permisos y seguridad

ChatGPT puede solicitarte permisos antes de poder tomar capturas de la aplicación:

- **Grabación de pantalla y audio del sistema** permite que ChatGPT capture una imagen de la
  ventana que está en primer plano.
- **Accesibilidad** permite que ChatGPT lea el texto disponible en la ventana que está en primer plano.

Al tomar una captura de la aplicación, se comparten con ChatGPT la imagen capturada y el texto disponible.
Evita tomar capturas de la aplicación con contenido sensible, a menos que la tarea requiera ese
contenido.

Revisa las capturas de la aplicación con los mismos criterios que aplicarías al compartir capturas de pantalla y documentos
con ChatGPT.

## Límites y solución de problemas

Las capturas de la aplicación están disponibles en la app de escritorio de ChatGPT para macOS. Si retomas un chat
en la CLI que ya contiene una captura de la aplicación, el archivo adjunto forma parte del historial
del chat, pero la CLI no puede crear una nueva captura de la aplicación.

En algunas apps y sitios web, como Google Docs, Gmail, Google Sheets y
Google Slides, es posible que ChatGPT solo reciba una captura de la parte visible de la pantalla y no reciba
el documento completo ni el texto que no está visible en pantalla. En ChatGPT Work o Codex, ChatGPT puede usar un
complemento compatible que esté instalado para acceder al contenido relevante de la app y ayudarte con tu
solicitud.

Si las capturas de la aplicación no funcionan:

1. Abre **Configuración del Sistema \> Privacidad y seguridad**.
2. Verifica los permisos de **Grabación de pantalla y audio del sistema** y **Accesibilidad** para Uso de la computadora de
   Codex.
3. Reinicia la app y vuelve a intentarlo.

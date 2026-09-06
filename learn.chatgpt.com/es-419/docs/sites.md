<!-- source: https://learn.chatgpt.com/es-419/docs/sites -->

Sites está en versión beta pública y está disponible con los planes ChatGPT Plus, Pro, Business,
Enterprise y Edu. Los límites de uso de cada plan se aplican al conjunto de los sitios
durante la versión beta. ChatGPT muestra los límites actuales y te avisa cuando te acercas
a uno. Alcanzar un límite puede impedirte crear un sitio, agregar almacenamiento o mantener
público un sitio con un uso elevado, pero aún puedes editar y administrar los sitios existentes.

Sites permite que ChatGPT cree, aloje, perfeccione y comparta sitios web, aplicaciones web y juegos.
Usa Sites cuando quieras convertir un prompt o un proyecto existente compatible en una
experiencia alojada sin configurar un flujo de trabajo de implementación independiente.

Abre **Sites** en la aplicación de escritorio de ChatGPT. Puedes crear un sitio a partir de un prompt o
de un proyecto local compatible y luego volver a la vista de Sites para administrarlo.

Usa Sites en ChatGPT en la web para crear y administrar sitios alojados. Selecciona
**Más** \> **Sites**, o ve directamente a
[chatgpt.com/sites](https://chatgpt.com/sites) para encontrar los sitios que creaste.

Sites no tiene una vista de administración independiente en Codex CLI. Usa ChatGPT en la web o
la aplicación de escritorio para crear, guardar, implementar y administrar un proyecto de Sites. Puedes
seguir usando Codex CLI para editar y probar un proyecto local antes de publicarlo.

Sites no tiene una vista de administración independiente en la extensión para IDE. Usa ChatGPT en la web
o la aplicación de escritorio para las operaciones de Sites, y usa la extensión para IDE para editar y
probar el proyecto de código fuente local.

  Cada URL de implementación de Sites corresponde a una implementación en producción. Si quieres revisar una
compilación antes de que esté disponible, pídele a ChatGPT que guarde una versión sin
implementarla.

## Primeros pasos con Sites

En ChatGPT, incluye la palabra “website” en tu prompt o menciona `@Sites` para
iniciar explícitamente el flujo de trabajo de Sites.

1. Describe el sitio

   Describe el público, el propósito, el comportamiento requerido y la información que el sitio
debe usar.

2. Revisa el sitio

   Revisa el contenido y el comportamiento generados. Verifica que el sitio use la
información prevista y gestione los datos como se espera.

3. Perfecciona el sitio

   Describe los cambios que quieres. Agrega archivos relevantes o contexto visual cuando
ayuden a ChatGPT a realizar el cambio.

4. Administra y comparte el sitio

   Vuelve a **Sites** para volver a abrir o perfeccionar el sitio. Cuando esté listo, elige quién
   puede visitarlo y comparte el enlace resultante.

En la vista previa, selecciona **Editar**. En **Describe los cambios en el sitio web**, describe los
cambios que quieres. Usa **Captura de pantalla** o **Agregar archivos y más** cuando el
contexto adicional resulte útil.

## Pedirle a Sites que realice tareas comunes

Para un nuevo sitio web, panel o herramienta interna, incluye el público, la experiencia
principal y la información necesaria:

```text
Build a project request dashboard for my operations team. Let team members
submit requests, see who owns each one, update the status, and filter the list.
Require people to sign in with their workspace account, and keep the request
data saved between visits.

Para un proyecto existente, pídele a Sites que prepare y publique la aplicación actual:

```text
Deploy this project with Sites. Check whether it is compatible, make any
required changes, and give me the deployment URL.

Cuando un sitio necesite datos persistentes de la aplicación o archivos subidos, indícalo en la
solicitud:

```text
Add player scores and avatar uploads to this game. Keep the scores and uploaded
avatars between visits.

  Explora la [galería de Sites](/showcase) para ver aplicaciones internas implementadas y los
  prompts completos que se usaron para crearlas.

## Revisar los datos de análisis del sitio

Sites registra el tráfico automáticamente para que puedas ver cómo las personas usan un sitio implementado
sin agregar un SDK de análisis. La vista de análisis muestra el total de visitantes únicos
y de vistas de página, así como la evolución de ambas métricas. Cambia el intervalo de fechas o
la granularidad para consultar otro periodo.

Abre **Sites**, busca el sitio y selecciona **Más acciones** \> **Análisis**.

Ve a [chatgpt.com/sites](https://chatgpt.com/sites), busca el sitio y selecciona
**Más acciones** \> **Análisis**.

Sites no tiene una vista de análisis independiente en la CLI ni en la extensión para IDE. Abre
el sitio en ChatGPT en la web o en la aplicación de escritorio para revisar sus datos de análisis.

  

  Actualmente, la función de análisis está disponible para los sitios que no pertenecen a un espacio de trabajo
de Empresas.

## Agregar el inicio de sesión con ChatGPT

Los sitios públicos pueden seguir abiertos para todos y, al mismo tiempo, ofrecer la opción de iniciar sesión con
ChatGPT para funciones basadas en la identidad, como el progreso guardado, las vistas personalizadas
o los registros que pertenecen a una persona específica. Los sitios restringidos al espacio de trabajo ya
usan la identidad de ChatGPT para aplicar su configuración de uso compartido.

Pídele a Sites que agregue la experiencia de inicio de sesión:

```text
Add Sign in with ChatGPT to this public Site. Keep the Site available to signed-out visitors. Show a Sign in with ChatGPT action when someone is signed out. After they sign in, greet them with their full name when available, or their email address otherwise. Add a Sign out action, and keep authorization decisions in server-side code.

Sites gestiona los flujos de inicio y cierre de sesión mediante las rutas que proporciona la plataforma
y luego redirige al visitante a tu sitio:

```html
<a href="/signin-with-chatgpt">Sign in with ChatGPT</a>
<a href="/signout-with-chatgpt">Sign out</a>

Después de que un visitante inicia sesión, Sites reenvía su identidad al servidor mediante
estos encabezados de solicitud:

- `oai-authenticated-user-email` contiene la dirección de correo electrónico autenticada.
- `oai-authenticated-user-full-name` puede contener un nombre de perfil no vacío. Considéralo
  opcional y usa la dirección de correo electrónico como alternativa.

Mantén las decisiones de autorización en el código del servidor y no dependas de
los encabezados que separan el nombre en partes.

## Comprender los proyectos, las versiones y las implementaciones

Un sitio es un resultado que permanece alojado y que puedes volver a abrir, perfeccionar, configurar
y compartir desde **Sites** en ChatGPT.

Un proyecto de Sites vincula un proyecto de código fuente local con el alojamiento administrado mediante Sites.
Sites almacena esa vinculación y los nombres de las vinculaciones opcionales de almacenamiento en
`.openai/hosting.json`. Un proyecto inicial local recién creado puede comenzar sin un
`project_id`; Sites agrega ese identificador después de aprovisionar el proyecto alojado.

Por ejemplo, un sitio aprovisionado que usa una vinculación a una base de datos relacional, pero no
almacenamiento de archivos, puede contener:

```json
{
  "project_id": "<project-id>",
  "d1": "DB",
  "r2": null
}

Un sitio aparece en tu lista de Sites incluso después de que termina el chat de ChatGPT Work que lo creó.
No necesitas un proyecto local ni un archivo de manifiesto para iniciar un sitio en la web. Un sitio es
independiente de un Proyecto de ChatGPT.

La publicación en Sites consta de dos etapas independientes:

1. **Guarda una versión.** ChatGPT genera una versión que se puede implementar. En el caso de un proyecto de código fuente
   local, ChatGPT asocia la versión con el commit de Git utilizado para la
   compilación. Usa esta etapa cuando quieras una versión candidata para implementación que puedas revisar.
2. **Implementa una versión.** ChatGPT publica una versión guardada e indica la
   URL de producción cuando la implementación se realiza correctamente. Usa esta etapa solo cuando quieras que
   el público seleccionado acceda al sitio.

Pídele a ChatGPT que enumere o inspeccione las versiones guardadas cuando necesites identificar una
versión anterior candidata para la implementación.

## Elegir un tipo de sitio compatible

Para proyectos nuevos, el flujo de trabajo de Sites puede comenzar con su plantilla inicial de sitio
recomendada. Para un proyecto existente, pídele a ChatGPT que confirme que el proyecto puede
generar artefactos de implementación compatibles antes de solicitar una implementación.

Indícale a ChatGPT qué comportamiento del producto necesitas para que pueda seleccionar el tipo
de sitio adecuado:

| Necesidad del sitio                                                      | Qué pedirle a Sites                                                         |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Sitio web centrado en el contenido o página de destino                            | Un sitio sin estado persistente de la aplicación, salvo que la experiencia lo requiera |
| Registros guardados, progreso de los usuarios o puntuaciones de juegos                   | D1, una base de datos relacional para datos estructurados persistentes                         |
| Imágenes, documentos, audio, video u otros archivos subidos              | R2, almacenamiento de objetos para archivos                                                  |
| Archivos subidos con metadatos que se pueden buscar                        | D1 para los metadatos y R2 para el contenido de los archivos                                      |
| Sitio interno que necesita la identidad del usuario actual del espacio de trabajo | Identidad del usuario autenticado en el espacio de trabajo                                         |
| Inicio de sesión público o un proveedor de identidad externo                | Un sitio con autenticación habilitada                                                |

No solicites almacenamiento persistente para estados temporales de la interfaz, como la elección de un tema o el cierre de un banner. Sí solicítalo para los datos del producto que las personas esperan que el sitio alojado recuerde.

## Controlar el acceso y los secretos

El acceso a un sitio nuevo está limitado a su propietario y a los administradores del espacio de trabajo hasta que cambies su configuración de acceso. Mantén el acceso limitado mientras revisas el contenido, el manejo de los datos y el público previsto.

Según la configuración de tu cuenta y de tu espacio de trabajo, las opciones para compartir pueden incluir:

- **Propietario y administradores del espacio de trabajo**
- **Usuarios activos o grupos seleccionados**, si esta opción está disponible
- **Lectores externos invitados**, cuando las invitaciones externas estén disponibles
- **Cualquier persona del espacio de trabajo**, si esta opción está disponible
- **Cualquier persona en internet**, solo cuando la publicación pública esté habilitada

El acceso de visitante permite que las personas abran el sitio; no les otorga acceso de edición. En los espacios de trabajo de Empresas, la publicación pública está desactivada de forma predeterminada y debe habilitarla un administrador.

Cuando compartes un sitio con acceso limitado, los visitantes invitados deben iniciar sesión con la cuenta que recibió acceso. Se puede acceder a un sitio público sin tener acceso a un espacio de trabajo de ChatGPT. La configuración del público del sitio y cualquier función de inicio de sesión integrada en él son controles independientes.

Por ejemplo:

```text
Change this Site's access to everyone in my workspace after showing me the
current Site and confirming its URL.

### Invitar a personas ajenas a tu espacio de trabajo

Las invitaciones externas te permiten dar acceso a un sitio a personas específicas sin hacerlo público. Puedes invitar a lectores ajenos a tu espacio de trabajo o compartir un sitio privado desde una cuenta personal. La función se está habilitando gradualmente para los usuarios de Sites con planes Plus, Pro, Business y Empresas.

1. Abre un sitio del que seas propietario y selecciona **Compartir**.
2. Para mantener el sitio privado, configura **Quién tiene acceso** en **Solo las personas invitadas**.
3. Ingresa la dirección de correo electrónico del lector en **Buscar personas o grupos**, o en
**Ingresar una dirección de correo electrónico** si se trata de un sitio personal, y luego selecciona al destinatario.
4. Revisa el público y el acceso de **Lector** del destinatario, y luego selecciona
**Invitar**.
5. Confirma que el lector aparezca en la lista de acceso guardada. Comparte el enlace del sitio y pídele que inicie sesión con la cuenta que recibió acceso.

Los lectores externos pueden abrir y usar el sitio. No se convierten en miembros del espacio de trabajo ni en editores del sitio, y no pueden editarlo ni publicarlo. La invitación otorga acceso a este sitio; revisa su contenido y los datos conectados antes de compartirlo.

En Empresas, los administradores gestionan **Permitir que los miembros inviten a visitantes externos a
sitios** en **Configuración del espacio de trabajo \> Permisos y roles**. Este permiso
es independiente del permiso para publicar sitios de forma pública.
Los espacios de trabajo de Business no tienen un control independiente para activar o desactivar el permiso de
invitaciones externas; Sites debe estar habilitado y la función debe estar disponible para la cuenta.
Si no aparece la opción para invitar, revisa la cuenta seleccionada, la propiedad del sitio,
los permisos del espacio de trabajo y la disponibilidad de la función durante su lanzamiento gradual.

Para quitar a un lector, abre los controles para compartir del sitio y quítale el acceso. Revisa también las demás opciones de público: eliminar una invitación no quita el acceso que esa persona tenga porque el sitio se comparte de forma pública, con el espacio de trabajo o con un grupo.

### Colaborar en un sitio

La colaboración en un sitio requiere un espacio de trabajo. Cuando la función está disponible, el propietario de un sitio puede invitar como editores a miembros activos del mismo espacio de trabajo.

Los editores pueden leer los datos de la base de datos en producción del sitio. Invita solo a personas a quienes puedas confiarles el código y los datos del sitio.

1. Abre el sitio y selecciona **Compartir**.
2. En **Agregar personas o grupos**, busca y selecciona a un miembro del espacio de trabajo.
   Se agregará como visitante.
3. Abre **Puede ver** junto a esa persona y elige **Puede editar**. La configuración de acceso se guarda
   automáticamente. El sitio aparece en **Compartido contigo** en la vista de
   Sites del miembro.
4. El editor puede abrir el sitio, realizar cambios, guardar versiones y publicar actualizaciones después de que el propietario haya publicado el sitio por primera vez.

El propietario del sitio administra el acceso de los editores y puede convertir a un visitante existente en
editor, cambiar el acceso de un editor a **Puede ver** o quitarle el acceso. La edición conjunta
no agrega un control independiente para activar o desactivar permisos en el espacio de trabajo.

Los editores no pueden cambiar el público del sitio, invitar o quitar a otras personas, administrar la configuración o las estadísticas, restaurar una versión anterior ni transferir la propiedad. Un editor tampoco puede realizar la primera publicación del sitio; el propietario debe publicarlo antes de que los editores puedan publicar actualizaciones posteriores.

El acceso de editor es independiente del acceso de visitante. Los pasos anteriores primero agregan a la persona como visitante y luego le otorgan acceso de edición. Convertir a un visitante en editor no cambia la configuración del público del sitio.

### Configurar los valores del entorno de ejecución

Abre **Sites** y luego la configuración del sitio para agregar, actualizar o eliminar
variables de entorno y secretos del entorno alojado. No incluyas valores secretos en prompts, archivos
adjuntos ni en el contenido del sitio.

Ve a [chatgpt.com/sites](https://chatgpt.com/sites), busca el sitio y selecciona
**Más acciones** \> **Configuración**.

No guardes estos valores en `.openai/hosting.json`. Mantén los archivos locales `.env` y
`.env.example` alineados con las claves necesarias para el desarrollo local y
no incluyas valores secretos en los commits.

Cuando agregues, actualices o elimines valores del entorno alojado, pídele a ChatGPT que vuelva a desplegar la versión guardada y aprobada para que el próximo despliegue use la configuración actualizada.

## Cambiar la URL de un sitio

Cuando la edición de URL esté disponible, los propietarios de sitios pueden cambiar la URL de un sitio existente alojado en ChatGPT sin crear otro despliegue.

1. Abre **Sites**, busca el sitio y abre su configuración.
2. Busca la URL del sitio y selecciona **Cambiar URL**.
3. Ingresa un nombre disponible. Debe tener al menos cinco caracteres, comenzar con una letra minúscula y contener únicamente letras minúsculas, números y guiones simples. No puede terminar con un guion ni contener guiones consecutivos.
4. Confirma el cambio y espera mientras Sites actualiza la dirección.

El cambio de URL no crea otro despliegue. La dirección anterior redirige a la nueva, incluidas las rutas y los parámetros de consulta.

Cambiar la URL alojada por ChatGPT no agrega, elimina ni modifica un dominio personalizado. Los dominios personalizados son una función independiente ya existente; usa la configuración de dominios personalizados cuando esta función esté disponible.

## Conectar un dominio personalizado

Cuando los dominios personalizados estén disponibles, puedes conectar un dominio raíz o un subdominio que ya sea de tu propiedad. Sites no registra dominios por ti, por lo que debes poder modificar los registros DNS del dominio. Al momento del lanzamiento, los dominios personalizados no están disponibles en los espacios de trabajo de Empresas.

Para conectar un dominio:

1. Abre la configuración del sitio y selecciona **Agregar dominio**.
2. Ingresa el dominio raíz o el subdominio que quieras usar.
3. Copia los registros DNS y los valores que proporciona Sites y luego agrégalos a través de tu proveedor de dominios.
4. Espera unos minutos, luego vuelve a la configuración del sitio y actualiza el estado del dominio.

También puedes pedirle a ChatGPT que te ayude a configurar el dominio para que apunte a tu sitio. Si la navegación o el uso de la computadora están habilitados, ChatGPT puede ayudarte a navegar por el sitio de tu proveedor de dominios después de que inicies sesión.

## Revisar antes de compartir

Antes de compartir un sitio:

- Revisa su contenido, el texto y las imágenes generados, los enlaces, los archivos cargados, los formularios y el comportamiento interactivo.
- Confirma que no exponga información confidencial o sensible, valores secretos ni contenido de terceros que no tengas derecho a compartir.
- Prueba el sitio tal como lo usarían los visitantes previstos, incluido el funcionamiento del acceso y del inicio de sesión.
- Revisa las funciones que recopilan información personal u otro contenido de los visitantes. Decide si el sitio debe recopilar, compartir o publicar esa información.
- Si el sitio usa la función Iniciar sesión con ChatGPT, explica qué información de los visitantes recibe y cómo la usa.
- Si el sitio recopila o procesa datos personales, cumple con
[las leyes de privacidad y protección de datos aplicables](https://help.openai.com/en/articles/20001340).
- Elige la opción para compartir más restrictiva que se ajuste al público previsto.
- Abre el sitio compartido y confirma que el público previsto pueda visitarlo.

Si el sitio se creó a partir de un proyecto local, revisa también los cambios en el código fuente y las
migraciones de bases de datos en el [panel de revisión](/es-419/codex/code-review?surface=app) de Codex.

## Retirar o eliminar un sitio

Para quitar el acceso sin eliminar un sitio, abre su configuración de uso compartido y restringe
el acceso a ti o a determinadas personas. Confirma que el público anterior ya no
pueda abrirlo.

Para eliminar un sitio de forma permanente:

1. Abre **Sites** y busca el sitio.
2. Selecciona **Eliminar sitio** y sigue las instrucciones del mensaje.
3. Ingresa el slug del sitio y luego selecciona **Eliminar permanentemente**.

Al eliminar un sitio, se borra de forma permanente. No puedes restaurar un sitio eliminado.

## Comprender los límites y los usos no admitidos

Sites aloja experiencias web que se ejecutan en el entorno de ejecución admitido por Sites. Algunos
frameworks, redes privadas, bases de datos, servicios en segundo plano y patrones de
alojamiento no son compatibles.

Se admiten HTTP, HTTPS y WebSockets. No se admiten conexiones TCP directas,
ya sean entrantes o salientes.

Cada sitio tiene estos límites de almacenamiento:

| Recurso            | Límite                  |
| ------------------- | ---------------------- |
| Almacenamiento de la base de datos D1 | 10 GB                  |
| Almacenamiento de objetos R2   | Sin límite fijo de almacenamiento |

Sites no admite la residencia de datos ni la residencia de inferencia en su lanzamiento. Esto
incluye los Sites desplegados, el código de los sitios, el almacenamiento de datos y archivos
en D1 y R2, los artefactos generados y los registros.

No uses Sites para procesar información de salud protegida ni datos de tarjetas de pago;
dirigirte a menores de 13 años o de la edad de consentimiento digital aplicable; habilitar
transacciones financieras; distribuir malware; facilitar el phishing; suplantar a personas
u organizaciones; o infringir de cualquier otro modo las políticas de OpenAI. Consulta
[Crear y administrar Sites de ChatGPT](https://help.openai.com/en/articles/20001339)
para conocer los límites actuales y los enlaces a las políticas.

## Documentación relacionada

- [Aplicación de escritorio de ChatGPT](/es-419/codex/app) presenta la navegación de la aplicación, los proyectos y los chats.
- [Revisar y publicar cambios](/es-419/codex/code-review?surface=app) explica cómo inspeccionar los cambios en el código fuente
  antes de publicarlos.

- [Proyectos y chats](/es-419/codex/projects) explica cómo el contexto de la carpeta y del espacio de trabajo
  se conserva de un chat a otro.
- [Revisar y publicar cambios](/es-419/codex/code-review) explica el flujo de trabajo de revisión para
  cada cliente de Codex.
- [Entorno aislado](/es-419/codex/sandboxing) explica los límites de la ejecución local.

- [Abre Sites en ChatGPT](https://chatgpt.com/sites) para volver a los Sites que
  creaste.
- [Proyectos y chats](/es-419/codex/projects?surface=web) explica cómo mantener juntos
  los chats y los archivos fuente relacionados.
- [Trabajar con archivos](/es-419/codex/artifacts-viewer?surface=web) explica cómo revisar
  los archivos generados en la versión web de ChatGPT.

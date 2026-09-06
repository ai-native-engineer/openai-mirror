<!-- source: https://learn.chatgpt.com/es-419/docs/environments/cloud-environment -->

Usa los entornos para controlar qué instala y ejecuta Codex durante los chats en la nube. Por ejemplo, puedes agregar dependencias, instalar herramientas como linters y formateadores, y definir variables de entorno.

Configura los entornos en la [configuración de Codex](https://chatgpt.com/codex/settings/environments).

<a id="how-codex-cloud-tasks-run"></a>

## Cómo se ejecutan los chats en la nube de Codex

Esto es lo que ocurre cuando envías un prompt:

1. Codex crea un contenedor y hace checkout de tu repositorio en la rama o el SHA del commit que seleccionaste.
2. Codex ejecuta tu script de configuración y, cuando se reanuda un contenedor almacenado en caché, también ejecuta un script de mantenimiento opcional.
3. Codex aplica tu configuración de acceso a Internet. Los scripts de configuración se ejecutan con acceso a Internet. El acceso a Internet del agente está desactivado de forma predeterminada, pero puedes habilitar el acceso limitado o sin restricciones si es necesario. Consulta [acceso a Internet del agente](/es-419/codex/cloud/internet-access).
4. El agente ejecuta comandos de terminal en un bucle. Edita código, ejecuta verificaciones e intenta validar su trabajo. Si tu repositorio incluye `AGENTS.md`, el agente lo usa para encontrar los comandos de lint y de pruebas específicos del proyecto.
5. Cuando el agente termina, muestra su respuesta y un diff de los archivos que haya cambiado. Puedes abrir un PR o hacer preguntas de seguimiento.

## Imagen universal predeterminada

El agente de Codex se ejecuta en una imagen de contenedor predeterminada llamada `universal`, en la que ya vienen instalados lenguajes, paquetes y herramientas comunes.

En la configuración del entorno, selecciona **Establecer versiones de paquetes** para fijar las versiones de Python, Node.js y otros entornos de ejecución.

  Para obtener detalles sobre lo que está instalado, consulta
[openai/codex-universal](https://github.com/openai/codex-universal), donde encontrarás un
  Dockerfile de referencia y una imagen que puedes descargar y probar localmente.

Aunque `codex-universal` incluye lenguajes preinstalados para ofrecer mayor rapidez y comodidad, también puedes instalar paquetes adicionales en el contenedor mediante [scripts de configuración](#manual-setup).

## Variables de entorno y secretos

**Las variables de entorno** permanecen definidas durante todo el chat (incluidos los scripts de configuración y la fase del agente).

**Los secretos** son similares a las variables de entorno, con estas diferencias:

- Se almacenan con una capa adicional de cifrado y solo se descifran durante la ejecución de la tarea.
- Solo están disponibles para los scripts de configuración. Por motivos de seguridad, los secretos se eliminan antes de que comience la fase del agente.

## Configuración automática

En proyectos que usan administradores de paquetes comunes (`npm`, `yarn`, `pnpm`, `pip`, `pipenv` y `poetry`), Codex puede instalar automáticamente dependencias y herramientas.

## Configuración manual

Si tu configuración de desarrollo es más compleja, también puedes proporcionar un script de configuración personalizado. Por ejemplo:

```bash
# Install type checker
pip install pyright

# Install dependencies
poetry install --with test
pnpm install

  Los scripts de configuración se ejecutan en una sesión de Bash separada de la del agente, por lo que los comandos como
`export` no persisten en la fase del agente. Para que las variables de
  entorno persistan, agrégalas a `~/.bashrc` o configúralas en la configuración del entorno.

## Almacenamiento en caché de contenedores

Codex almacena en caché el estado del contenedor durante un máximo de 12 horas para agilizar los chats nuevos y las consultas de seguimiento.

Cuando un entorno se almacena en caché:

- Codex clona el repositorio y hace checkout de la rama predeterminada.
- Codex ejecuta el script de configuración y almacena en caché el estado resultante del contenedor.

Cuando se reanuda un contenedor almacenado en caché:

- Codex hace checkout de la rama especificada para el chat.
- Codex ejecuta el script de mantenimiento (opcional). Esto resulta útil cuando el script de configuración se ejecutó en un commit anterior y es necesario actualizar las dependencias.

Codex invalida automáticamente la caché si modificas el script de configuración, el script de mantenimiento, las variables de entorno o los secretos. Si algún cambio en tu repositorio hace que el estado almacenado en caché sea incompatible, selecciona **Restablecer caché** en la página del entorno.

  Para los usuarios de Business y de Empresas, las cachés se comparten entre todos los usuarios que tienen
acceso al entorno. Invalidar la caché afectará a todos los usuarios del
entorno en tu espacio de trabajo.

## Acceso a Internet y proxy de red

Durante la ejecución del script de configuración, hay acceso a Internet para instalar dependencias. Durante la fase del agente, el acceso a Internet está desactivado de forma predeterminada, pero puedes configurar el acceso limitado o sin restricciones. Consulta [acceso a Internet del agente](/es-419/codex/cloud/internet-access).

Los entornos se ejecutan detrás de un proxy de red HTTP/HTTPS por motivos de seguridad y para prevenir abusos. Todo el tráfico saliente hacia Internet pasa por este proxy.

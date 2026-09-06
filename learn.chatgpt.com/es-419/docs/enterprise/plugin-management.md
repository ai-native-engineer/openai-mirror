<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/plugin-management -->

## Antes de comenzar

Los administradores del espacio de trabajo pueden importar un marketplace de complementos desde GitHub y mantener sus complementos actualizados desde el repositorio. Un marketplace es un catálogo JSON que enumera los complementos que se van a importar.

Usa una cuenta de GitHub que pueda leer el repositorio del marketplace y cualquier otro repositorio al que haga referencia. Se admiten repositorios públicos y privados de GitHub. Antes de importar, obtén cualquier aprobación de la organización de GitHub que se requiera para acceder al repositorio.

Revisa el contenido del repositorio antes de importar. Los nuevos complementos tienen inicialmente la política de instalación **Disponible** y autenticación al instalar. Los nuevos marketplaces tienen habilitada la sincronización automática diaria. La importación procesa todas las entradas válidas, y las sincronizaciones futuras agregan automáticamente cualquier complemento nuevo del repositorio.

## Configurar la sincronización de un marketplace

1. Abre **Administración** \> **Complementos** y selecciona **Agregar** \> **Importar marketplace**.
2. En **Origen**, ingresa la URL del repositorio, como `https://github.com/example/team-plugins`. Usa únicamente la URL del repositorio, no la de una rama o carpeta.
3. Si el marketplace está en un subdirectorio, ingresa ese directorio en **Ruta**. Por ejemplo, usa `team-tools` para `team-tools/.agents/plugins/marketplace.json`. Deja **Ruta** vacío para usar la raíz del repositorio. No ingreses el nombre del archivo de manifiesto.
4. De forma opcional, completa el campo **Rama, etiqueta o commit**. Déjalo vacío para usar la rama predeterminada del repositorio. Usa una rama para recibir futuros commits; si fijas un commit, se mantiene esa revisión.
5. Selecciona **Importar marketplace** y autoriza el acceso a GitHub cuando se te solicite. La importación inicial puede tardar hasta una hora en el caso de marketplaces muy grandes. Las sincronizaciones diarias posteriores suelen tardar unos minutos.
6. Revisa los **Resultados de la importación** y luego abre cada complemento importado para configurar su política de instalación y las apps requeridas.

Para solicitar una actualización sin esperar a la sincronización diaria, abre el marketplace en **Administración** \> **Complementos** \> **Marketplaces** y selecciona **Sincronizar ahora**.

## Formatos compatibles

El directorio seleccionado debe contener uno de estos archivos:

| Archivo                               | Formato                                                               |
| ---------------------------------- | -------------------------------------------------------------------- |
| `.agents/plugins/marketplace.json` | Un marketplace de Codex con un arreglo `plugins`.                          |
| `.claude-plugin/marketplace.json`  | Un marketplace compatible con Claude con un arreglo `plugins`.              |
| `.claude-plugin/plugin.json`       | Un complemento independiente de Claude, cuando no hay un archivo de manifiesto del marketplace. |

En un marketplace, las entradas pueden hacer referencia a complementos nativos con `.codex-plugin/plugin.json`, complementos compatibles con Claude, paquetes de Agent Plugins 1.0 o paquetes de habilidades compatibles.

En un marketplace de Codex, usa rutas locales para los complementos que estén en el mismo repositorio:

```json
{
  "name": "team-plugins",
  "interface": {
    "displayName": "Team plugins"
  },
  "plugins": [
    {
      "name": "team-tools",
      "source": {
        "source": "local",
        "path": "./plugins/team-tools"
      }
    }
  ]
}

La ruta es relativa a la raíz seleccionada del marketplace, no a `.agents/plugins/`.

Un marketplace compatible con Claude puede usar una cadena de texto con la ruta de cada complemento local:

```json
{
  "name": "team-plugins",
  "plugins": [
    {
      "name": "team-tools",
      "source": "./plugins/team-tools"
    }
  ]
}

Las entradas de un marketplace de Codex también admiten `source: "url"` para un complemento en la raíz de un repositorio de GitHub y `source: "git-subdir"` para un complemento en un subdirectorio de GitHub. Por ejemplo:

```json
{
  "name": "team-tools",
  "source": {
    "source": "git-subdir",
    "url": "https://github.com/example/team-tools.git",
    "path": "./plugins/team-tools",
    "ref": "main"
  }
}

Las fuentes de Git permiten seleccionar un `ref` o el `sha` completo de 40 caracteres de un commit. La cuenta de GitHub que autoriza el acceso debe poder leer todos los repositorios a los que se haga referencia. Actualmente, la importación al espacio de trabajo solo admite repositorios de GitHub.

## Configurar el acceso al espacio de trabajo

La importación y la sincronización desde GitHub no aplican las políticas de instalación o autenticación definidas en el repositorio, incluidas `AVAILABLE`, `INSTALLED_BY_DEFAULT`, `NOT_AVAILABLE`, `ON_INSTALL` y `ON_USE`. Los administradores del espacio de trabajo configuran estos ajustes para cada complemento. Al sincronizar una actualización o pasar a gestionar un complemento existente desde GitHub, se conservan sus políticas del espacio de trabajo.

Usa **Política de instalación** para elegir **Disponible** o **Instalado** para cada rol que cumpla los requisitos. Las apps requeridas también deben estar habilitadas, y los miembros deben tener acceso al servicio conectado. Importar un complemento no otorga acceso a las apps ni conecta las cuentas de los miembros. Consulta [Controles de complementos](/es-419/codex/enterprise/apps-and-connectors) para conocer los controles de roles, apps y acciones.

## Pasar a gestionar un complemento existente desde GitHub

Agrega `pluginId` a la entrada del complemento existente en el marketplace:

```json
{
  "name": "team-tools",
  "pluginId": "plugin_0123456789abcdef0123456789abcdef",
  "source": {
    "source": "local",
    "path": "./plugins/team-tools"
  }
}

Abre el complemento desde **Administración** \> **Complementos** y copia el ID que aparece después de `/admin/plugins/` en su URL. Coloca `pluginId` junto a `name` y `source` en la entrada del marketplace. El complemento existente debe estar en el mismo espacio de trabajo.

Así, un complemento del espacio de trabajo que se haya cargado o que no esté gestionado de otro modo pasa a gestionarse desde GitHub. El complemento conserva su ID, su configuración de uso compartido y sus políticas del espacio de trabajo. Las futuras actualizaciones provienen de GitHub; ya no se puede reemplazar el complemento gestionado mediante la carga de archivos comprimidos. No se puede asumir de esta forma la gestión de un complemento que ya esté gestionado desde otra fuente de GitHub.

## Complementos exclusivos para escritorio

Cualquier complemento importado que declare servidores MCP en `mcp.json` o `.mcp.json` se marca como **Solo para escritorio** y funciona únicamente en la aplicación de escritorio de ChatGPT. Esto incluye los servidores que usan una URL HTTPS remota. La misma restricción se aplica a otras formas de configuración de MCP compatibles, como las declaraciones de servidores dentro de la propia configuración.

## Hacer referencia a una app existente con `.app.json`

Agrega `.app.json` en la raíz del complemento. El nombre del archivo incluye un punto inicial; no se admite `app.json` sin el punto.

```json
{
  "apps": {
    "team-tools": {
      "id": "asdk_app_example",
      "required": true
    }
  }
}

Reemplaza `asdk_app_example` por el ID de la app existente. Los ID de apps compatibles comienzan con `asdk_app_`, `connector_` o `templated_apps_`. Usa el ID de la app, no un ID `plugin_...`. Por ejemplo, la URL de un complemento que contiene `plugin_asdk_app_example` representa la app `asdk_app_example`.

La clave `team-tools` da nombre a la referencia dentro de este archivo. Establece `required` en `true` cuando el complemento dependa de la app. Puedes agregar más entradas para hacer referencia a otras apps existentes.

Para un complemento nativo, establece `apps` en `./.app.json` dentro de `.codex-plugin/plugin.json`. Este es un archivo de manifiesto completo para este ejemplo:

```json
{
  "name": "team-tools",
  "version": "1.0.0",
  "description": "Use the team's approved tools.",
  "author": {
    "name": "Example team"
  },
  "apps": "./.app.json",
  "interface": {
    "displayName": "Team tools",
    "shortDescription": "Use approved team tools",
    "longDescription": "Connect to the team's existing app.",
    "developerName": "Example team",
    "category": "Productivity",
    "capabilities": ["Read"]
  }
}

Mantén los archivos organizados de esta forma:

```text
team-plugins/
├── .agents/plugins/marketplace.json
└── plugins/team-tools/
    ├── .codex-plugin/plugin.json
    └── .app.json

La referencia no crea una app ni otorga permisos. Los administradores deben poner la app a disposición de los roles previstos, y los miembros deben completar cualquier autenticación requerida. Los permisos de la app, los controles de acciones y el acceso al servicio existentes siguen vigentes.

## Mantener los complementos actualizados

Los nuevos marketplaces buscan actualizaciones a diario. Abre **Administración** \> **Complementos** \> **Marketplaces**, selecciona el marketplace y elige **Sincronizar ahora** para solicitar una actualización sin esperar a la sincronización automática.

La sincronización puede agregar nuevas entradas del marketplace y actualizar los complementos existentes. Revisa los cambios del repositorio antes de fusionarlos, porque la sincronización automática importará cualquier complemento nuevo.

Después de una sincronización, revisa el estado y el informe guardado. **Completado — N errores** significa que la ejecución terminó, pero no se pudieron procesar algunos complementos. Si una actualización de un complemento existente no es válida, se conserva su última versión funcional. Corrige el problema indicado en GitHub y luego selecciona **Sincronizar ahora** para volver a intentarlo.

Eliminar una entrada del repositorio no elimina su copia importada al espacio de trabajo. Se marca como **Ya no está en el origen**. Al eliminar el marketplace en ChatGPT, se eliminan todos los complementos importados de él.

## Restablecer o cambiar el acceso a GitHub

Para **restablecer el acceso a GitHub**, primero confirma que la cuenta de GitHub usada para la importación siga teniendo acceso al repositorio y a cualquier repositorio al que se haga referencia. Luego, el administrador que importó originalmente el marketplace debería abrir el complemento de GitHub en ChatGPT y volver a conectar su cuenta, ya que la sincronización del marketplace usa la conexión a GitHub de ese administrador.

Para **transferirlo a un nuevo propietario**, el nuevo administrador del espacio de trabajo debería abrir **Administración** \> **Complementos** \> **Agregar** \> **Importar marketplace** e importar el mismo marketplace con los mismos valores de **Origen**, **Ruta** y **Rama, etiqueta o commit** . Las futuras sincronizaciones usarán su conexión a GitHub.

No elimines el marketplace solo para volver a conectarlo o cambiar su propietario: al eliminarlo, también se eliminan los complementos que se importaron de él.

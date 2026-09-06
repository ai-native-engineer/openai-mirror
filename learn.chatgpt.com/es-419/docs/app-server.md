<!-- source: https://learn.chatgpt.com/es-419/docs/app-server -->

Codex app-server es la interfaz que Codex usa como base para clientes con funciones avanzadas (por ejemplo, la extensión de Codex para VS Code). Úsala cuando necesites una integración profunda en tu propio producto: autenticación, historial de conversaciones, aprobaciones y transmisión de eventos del agente. La implementación de app-server es de código abierto y se encuentra en el repositorio de Codex en GitHub ([openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)). Consulta la página [Código abierto](/es-419/codex/open-source) para ver la lista completa de componentes de código abierto de Codex.

  Si automatizas trabajos o ejecutas Codex en CI, usa el
<a href="/codex/codex-sdk">SDK de Codex</a> en su lugar.

## Conectar la interfaz de terminal de la CLI

El modo de interfaz de terminal remota te permite ejecutar app-server en una máquina y conectar la
interfaz de terminal de Codex CLI desde otra. Inicia un servicio de escucha WebSocket:

```bash
codex app-server --listen ws://127.0.0.1:4500

Luego, conecta la interfaz de terminal:

```bash
codex --remote ws://127.0.0.1:4500

Para una conexión no local, configura la autenticación WebSocket y protege la
conexión con TLS. Guarda el token de portador en una variable de entorno y
pasa su nombre en lugar de incluir el token en la línea de comandos:

```bash

codex --remote wss://remote-host:4500 \
  --remote-auth-token-env CODEX_REMOTE_TOKEN

La opción `--remote` acepta los puntos de acceso `ws://`, `wss://`, `unix://` y
`unix://PATH`. Usa WebSockets sin cifrar solo con localhost o una conexión con
reenvío de puertos mediante SSH.

## Conectar un host remoto de Code Mode

De forma predeterminada, app-server inicia un host local de Code Mode. Para usar un host remoto
en su lugar, pasa su URL segura de WebSocket:

```bash
codex app-server --code-mode-host wss://code-mode.example.com/host

`--code-mode-host` controla la conexión saliente de app-server con su
host de Code Mode. No modifica `--listen`, que controla cómo se conectan los clientes a
app-server. Todos los hilos de un mismo proceso de app-server comparten la conexión
seleccionada con el host de Code Mode.

Usa `wss://` para un host remoto. Usa `ws://` solo para una conexión a localhost o
con reenvío mediante SSH. El comando app-server y el transporte WebSocket son
experimentales y no cuentan con soporte para cargas de trabajo de producción.

## Protocolo

Al igual que [MCP](https://modelcontextprotocol.io/), `codex app-server` admite la comunicación bidireccional mediante mensajes JSON-RPC 2.0 (el encabezado `"jsonrpc":"2.0"` se omite durante la transmisión).

Transportes compatibles:

- `stdio` (`--listen stdio://`, predeterminado): JSON delimitado por saltos de línea (JSONL).
- `websocket` (`--listen ws://IP:PORT`, experimental y sin soporte): un
  mensaje JSON-RPC por cada trama de texto WebSocket.
- Socket Unix (`--listen unix://` o `--listen unix://PATH`): conexiones WebSocket
  a través del socket de control predeterminado de app-server de Codex o de una ruta
  personalizada de socket Unix, mediante la negociación HTTP Upgrade estándar.
- `off` (`--listen off`): no expone ningún transporte local.

Cuando ejecutas el servidor con `--listen ws://IP:PORT`, el mismo servicio de escucha también atiende comprobaciones básicas
de estado por HTTP:

- `GET /readyz` devuelve `200 OK` en cuanto el servicio de escucha acepta conexiones nuevas.
- `GET /healthz` devuelve `200 OK` cuando la solicitud no incluye
  un encabezado `Origin`.
- Las solicitudes con un encabezado `Origin` se rechazan con `403 Forbidden`.

El transporte WebSocket es experimental y no cuenta con soporte. Los servicios de escucha locales, como
`ws://127.0.0.1:PORT`, son adecuados para localhost y los flujos de trabajo con reenvío de puertos
mediante SSH. Actualmente, durante el despliegue, los servicios de escucha WebSocket que no usan loopback permiten
conexiones sin autenticación de forma predeterminada, así que configura la autenticación WebSocket antes de
exponer uno de forma remota.

Opciones de autenticación WebSocket compatibles:

- `--ws-auth capability-token --ws-token-file /absolute/path`
- `--ws-auth capability-token --ws-token-sha256 HEX`
- `--ws-auth signed-bearer-token --ws-shared-secret-file /absolute/path`

Para los tokens de portador firmados, también puedes configurar `--ws-issuer`, `--ws-audience` y
`--ws-max-clock-skew-seconds`. Los clientes presentan la credencial como
`Authorization: Bearer <token>` durante la negociación WebSocket, y app-server
exige la autenticación antes de `initialize` de JSON-RPC.

Usa preferentemente `--ws-token-file` en lugar de pasar tokens de portador sin procesar en la línea de comandos. Usa
`--ws-token-sha256` solo cuando el cliente conserve el token de alta entropía sin procesar en un
almacén local de secretos independiente; el hash solo sirve como verificador y los clientes siguen necesitando
el token original.

En modo WebSocket, app-server usa colas de capacidad limitada. Cuando se satura la entrada de solicitudes,
el servidor rechaza las solicitudes nuevas con el código de error JSON-RPC `-32001` y el mensaje
`"Server overloaded; retry later."` Los clientes deberían volver a intentarlo con un intervalo de espera que aumente exponencialmente
y tenga una variación aleatoria.

## Esquema de mensajes

Las solicitudes incluyen `method`, `params` y `id`:

```json
{ "method": "thread/start", "id": 10, "params": { "model": "gpt-5.6-terra" } }

Las respuestas repiten `id` junto con `result` o `error`:

```json
{ "id": 10, "result": { "thread": { "id": "thr_123" } } }

```json
{ "id": 10, "error": { "code": 123, "message": "Something went wrong" } }

Las notificaciones omiten `id` y solo usan `method` y `params`:

```json
{ "method": "turn/started", "params": { "turn": { "id": "turn_456" } } }

Puedes generar un esquema de TypeScript o un paquete JSON Schema desde la CLI. Cada resultado corresponde a la versión de Codex que ejecutaste, por lo que los artefactos generados coinciden exactamente con esa versión:

```bash
codex app-server generate-ts --out ./schemas
codex app-server generate-json-schema --out ./schemas

## Primeros pasos

1. Inicia el servidor con `codex app-server` (transporte stdio predeterminado),
`codex app-server --listen ws://127.0.0.1:4500` (WebSocket sobre TCP) o
`codex app-server --listen unix://` (socket Unix predeterminado).
2. Conecta un cliente mediante el transporte seleccionado y luego envía `initialize`, seguido de la notificación `initialized`.
3. Inicia un hilo y un turno; luego, sigue leyendo las notificaciones del flujo de transporte activo.

Ejemplo (Node.js / TypeScript):

```ts

const proc = spawn("codex", ["app-server"], {
  stdio: ["pipe", "pipe", "inherit"],
});
const rl = readline.createInterface({ input: proc.stdout });

const send = (message: unknown) => {
  proc.stdin.write(`${JSON.stringify(message)}\n`);
};

let threadId: string | null = null;

rl.on("line", (line) => {
  const msg = JSON.parse(line) as any;
  console.log("server:", msg);

  if (msg.id === 1 && msg.result?.thread?.id && !threadId) {
    threadId = msg.result.thread.id;
    send({
      method: "turn/start",
      id: 2,
      params: {
        threadId,
        input: [{ type: "text", text: "Summarize this repo." }],
      },
    });
  }
});

send({
  method: "initialize",
  id: 0,
  params: {
    clientInfo: {
      name: "my_product",
      title: "My Product",
      version: "0.1.0",
    },
  },
});
send({ method: "initialized", params: {} });
send({ method: "thread/start", id: 1, params: { model: "gpt-5.6-terra" } });

## Primitivas fundamentales

- **Hilo**: una conversación entre un usuario y el agente de Codex. Los hilos contienen turnos.
- **Turno**: una única solicitud del usuario y el trabajo que el agente realiza a continuación. Los turnos contienen elementos y transmiten actualizaciones incrementales.
- **Elemento**: una unidad de entrada o salida (mensaje del usuario, mensaje del agente, ejecuciones de comandos, cambio de archivo, llamada a una herramienta y más).

Usa las API de hilos para crear, enumerar o archivar conversaciones. Gestiona una conversación con las API de turnos y transmite el progreso mediante notificaciones de turnos.

## Descripción general del ciclo de vida

- **Inicializar una vez por conexión**: inmediatamente después de abrir una conexión de transporte, envía una solicitud `initialize` con los metadatos de tu cliente y luego emite `initialized`. El servidor rechaza cualquier solicitud en esa conexión antes de esta negociación.
- **Iniciar (o reanudar) un hilo**: llama a `thread/start` para iniciar una conversación nueva, a `thread/resume` para continuar una existente o a `thread/fork` para bifurcar el historial en un hilo con un nuevo identificador.
- **Iniciar un turno**: llama a `turn/start` con el `threadId` de destino y la entrada del usuario. Los campos opcionales reemplazan el modelo, la personalidad, `cwd`, la política del sandbox y otros valores.
- **Guiar un turno activo**: llama a `turn/steer` para agregar la entrada del usuario al turno en curso sin crear uno nuevo.
- **Transmitir eventos**: después de `turn/start`, sigue leyendo las notificaciones en stdout: `thread/archived`, `thread/unarchived`, `item/started`, `item/completed`, `item/agentMessage/delta`, el progreso de las herramientas y otras actualizaciones.
- **Finalizar el turno**: el servidor emite `turn/completed` con el estado final cuando el modelo termina o después de una cancelación mediante `turn/interrupt`.

## Inicialización

Los clientes deben enviar una única solicitud `initialize` por conexión de transporte antes de invocar cualquier otro método en esa conexión y luego enviar una notificación `initialized` como confirmación. Las solicitudes enviadas antes de la inicialización reciben el error `Not initialized`, y las llamadas repetidas a `initialize` en la misma conexión devuelven `Already initialized`.

El servidor devuelve la cadena de agente de usuario que presentará a los servicios upstream, además de los valores `platformFamily` y `platformOs` que describen la plataforma de ejecución. Configura `clientInfo` para identificar tu integración.

`initialize.params.capabilities` también admite estas capacidades del cliente:

- `optOutNotificationMethods` - nombres exactos de los métodos de notificación que se deben suprimir en
  esta conexión. La coincidencia es exacta (sin comodines ni prefijos); los nombres desconocidos
  se aceptan y se ignoran.
- `requestAttestation` - habilita la solicitud `attestation/generate`
  iniciada por el servidor. Los hosts de escritorio que proporcionan atestación a los servicios upstream responden con un
  valor opaco `{ "token": "..." }`.
- `mcpServerOpenaiFormElicitation` - permite que los servidores MCP downstream envíen la
  variante de `mcpServer/elicitation/request` con formulario extendido de OpenAI.

**Importante**: usa `clientInfo.name` para identificar tu cliente en la Plataforma de registros de cumplimiento. Si estás desarrollando una nueva integración de Codex destinada al uso empresarial, contacta a OpenAI para que se agregue a una lista de clientes conocidos. Para obtener más contexto, consulta la [referencia de registros de Codex](https://chatgpt.com/public/admin/api-reference#tag/Codex).

Ejemplo (de la extensión de Codex para VS Code):

```json
{
  "method": "initialize",
  "id": 0,
  "params": {
    "clientInfo": {
      "name": "codex_vscode",
      "title": "Codex VS Code Extension",
      "version": "0.1.0"
    }
  }
}

Ejemplo con notificaciones desactivadas:

```json
{
  "method": "initialize",
  "id": 1,
  "params": {
    "clientInfo": {
      "name": "my_client",
      "title": "My Client",
      "version": "0.1.0"
    },
    "capabilities": {
      "experimentalApi": true,
      "optOutNotificationMethods": ["thread/started", "item/agentMessage/delta"]
    }
  }
}

## Habilitar la API experimental

Por diseño, algunos métodos y campos de app-server requieren la capacidad `experimentalApi`.

- Omite `capabilities` (o establece `experimentalApi` en `false`) para limitarte a la API estable; el servidor rechaza los métodos y campos experimentales.
- Establece `capabilities.experimentalApi` en `true` para habilitar los métodos y campos experimentales.

```json
{
  "method": "initialize",
  "id": 1,
  "params": {
    "clientInfo": {
      "name": "my_client",
      "title": "My Client",
      "version": "0.1.0"
    },
    "capabilities": {
      "experimentalApi": true
    }
  }
}

Si un cliente envía un método o campo experimental sin habilitar la API experimental, app-server lo rechaza con:

`<descriptor> requires experimentalApi capability`

## Descripción general de la API

- `thread/start` - crea un hilo nuevo; emite `thread/started` y te suscribe automáticamente a los eventos de turnos y elementos de ese hilo.
- `thread/resume` - vuelve a abrir un hilo existente por ID para que las llamadas posteriores a `turn/start` agreguen contenido a ese hilo.
- `thread/fork` - crea un fork de un hilo con un nuevo ID copiando el historial almacenado. Pasa `lastTurnId` para copiar el historial hasta ese turno y omitir los turnos posteriores, o `ephemeral: true` para crear un fork en memoria. Emite `thread/started` para el hilo nuevo; los hilos devueltos incluyen `forkedFromId` cuando está disponible.
- `thread/read` - lee un hilo almacenado por ID sin reanudarlo; establece `includeTurns` para devolver el historial completo de turnos. Los objetos `thread` devueltos incluyen el campo `status` con el estado de ejecución.
- `thread/list` - consulta de forma paginada los registros almacenados de hilos; admite paginación basada en cursor, además de los filtros `modelProviders`, `sourceKinds`, `archived`, `isPinned`, `cwd`, `useStateDbOnly`, `searchTerm` y los filtros experimentales `parentThreadId` o `ancestorThreadId`. Los objetos `thread` devueltos incluyen el campo `status` con el estado de ejecución.
- `thread/turns/list` - experimental; consulta de forma paginada el historial de turnos de un hilo almacenado sin reanudarlo. `itemsView` determina si los elementos de los turnos se omiten, se resumen o se cargan por completo.
- `thread/items/list` - experimental; consulta de forma paginada los elementos persistidos de un hilo, con la opción de restringirlos a un solo `turnId`. El almacén de hilos activo debe admitir la paginación de elementos.
- `thread/loaded/list` - enumera los ID de los hilos cargados actualmente en memoria.
- `thread/name/set` - establece o actualiza el nombre visible para el usuario de un hilo, ya sea que esté cargado o tenga un registro de ejecución persistido; emite `thread/name/updated`.
- `thread/goal/set` - establece el objetivo de un hilo; emite `thread/goal/updated`.
- `thread/goal/get` - lee el objetivo actual de un hilo.
- `thread/goal/clear` - borra el objetivo de un hilo; emite `thread/goal/cleared`.
- `thread/metadata/update` - actualiza parcialmente los metadatos de hilos almacenados en SQLite, incluidos los valores persistidos de `gitInfo` y `isPinned`.
- `thread/archive` - mueve el archivo de registro de un hilo al directorio de archivado e intenta archivar los registros de los hilos descendientes generados que aún no estén archivados; devuelve `{}` si se completa correctamente y emite `thread/archived` por cada hilo archivado.
- `thread/delete` - elimina de forma permanente un hilo persistido, ya sea activo o archivado, y todos los hilos descendientes que haya generado; devuelve `{}` si se completa correctamente y emite `thread/deleted` por cada hilo eliminado.
- `thread/unsubscribe` - cancela la suscripción de esta conexión a los eventos de turnos y elementos del hilo. Si era el último suscriptor, el servidor retira el hilo de la memoria tras un período de gracia sin actividad ni suscriptores y emite `thread/closed`.
- `thread/unarchive` - restaura el registro de ejecución archivado de un hilo en el directorio de sesiones activas; devuelve el `thread` restaurado y emite `thread/unarchived`.
- `thread/status/changed` - notificación que se emite cuando cambia el campo `status` con el estado de ejecución de un hilo cargado.
- `thread/compact/start` - inicia la compactación del historial de conversación de un hilo; devuelve `{}` de inmediato mientras el progreso se transmite mediante las notificaciones `turn/*` y `item/*`.
- `thread/shellCommand` - ejecuta en un hilo un comando de shell iniciado por el usuario. Se ejecuta fuera del sandbox con acceso completo y no hereda la política de sandbox del hilo.
- `thread/backgroundTerminals/clean` - detiene todas las terminales en segundo plano que estén en ejecución para un hilo (experimental; requiere `capabilities.experimentalApi`).
- `thread/backgroundTerminals/list` - enumera las terminales en segundo plano en ejecución de un hilo cargado (experimental; requiere `capabilities.experimentalApi`).
- `thread/backgroundTerminals/terminate` - finaliza una terminal en segundo plano en ejecución mediante el `processId` de app-server (experimental; requiere `capabilities.experimentalApi`).
- `thread/rollback` - obsoleto; descarta los últimos N turnos del contexto en memoria y almacena de forma persistente un marcador de reversión; devuelve el `thread` actualizado.
- `turn/start` - agrega a un hilo la entrada del usuario o la salida independiente de una herramienta e inicia la generación de Codex; responde con el `turn` inicial y transmite eventos. Para `collaborationMode`, `settings.developer_instructions: null` significa “usar las instrucciones integradas para el modo seleccionado”.
- `thread/inject_items` - agrega elementos sin procesar de Responses API al historial de un hilo cargado que es visible para el modelo, sin iniciar un turno del usuario.
- `turn/steer` - agrega la entrada del usuario al turno activo en curso de un hilo; devuelve el `turnId` aceptado.
- `turn/interrupt` - solicita la cancelación de un turno en curso; devuelve `{}` si se completa correctamente y el turno termina con `status: "interrupted"`.
- `review/start` - inicia el revisor de Codex para un hilo; emite elementos `enteredReviewMode` y `exitedReviewMode`.
- `command/exec` - ejecuta un solo comando en el sandbox del servidor sin iniciar un hilo ni un turno.
- `command/exec/write` - escribe bytes en `stdin` de una sesión de `command/exec` en ejecución o cierra `stdin`.
- `command/exec/resize` - cambia el tamaño de una sesión de `command/exec` en ejecución con PTY.
- `command/exec/terminate` - detiene una sesión de `command/exec` en ejecución.
- `command/exec/outputDelta` (notificación) - se emite para fragmentos de stdout/stderr codificados en base64 provenientes de una sesión de `command/exec` con transmisión continua.
- `process/spawn` - inicia de forma explícita una sesión de proceso fuera del sandbox de Codex (experimental; requiere `capabilities.experimentalApi`).
- `process/writeStdin` - escribe bytes en stdin de una sesión de `process/spawn` en ejecución o cierra stdin (experimental).
- `process/resizePty` - cambia el tamaño de una sesión de proceso en ejecución con PTY (experimental).
- `process/kill` - finaliza una sesión de proceso en ejecución (experimental).
- `process/outputDelta` y `process/exited` (notificación) - se emiten para la transmisión continua de la salida del proceso y para su estado de salida (experimental).
- `model/list` - enumera los modelos disponibles (establece `includeHidden: true` para incluir entradas con `hidden: true`) junto con sus opciones de esfuerzo, el campo opcional `upgrade` y `inputModalities`.
- `modelProvider/capabilities/read` - lee los límites de las capacidades del proveedor para las combinaciones de modelo y proveedor.
- `experimentalFeature/list` - enumera los indicadores de funciones con metadatos de la etapa del ciclo de vida y paginación por cursor.
- `experimentalFeature/enablement/set` - actualiza parcialmente la configuración en memoria del entorno de ejecución para claves de funciones admitidas, como `apps` y `plugins`.
- `environment/info` - experimental; se conecta a un entorno de ejecución configurado y devuelve su shell junto con el directorio de trabajo predeterminado.
- `permissionProfile/list` - enumera los perfiles de permisos en beta e indica si los requisitos efectivos permiten usarlos, con paginación por cursor.
- `collaborationMode/list` - enumera las configuraciones predefinidas del modo de colaboración (experimental, sin paginación).
- `skills/list` - enumera las habilidades para uno o varios valores de `cwd` (admite `forceReload` y el campo opcional `perCwdExtraUserRoots`).
- `skills/extraRoots/set` - reemplaza las rutas raíz adicionales a nivel de proceso que se usan para detectar habilidades independientes, sin guardarlas de forma persistente.
- `skills/changed` (notificación) - se emite cuando cambian los archivos locales de habilidades supervisados.
- `hooks/list` - enumera los hooks del ciclo de vida detectados para uno o varios valores de `cwd`.
- `marketplace/add` - agrega un marketplace remoto de complementos y lo guarda en la configuración de marketplaces del usuario.
- `marketplace/remove` - quita un marketplace configurado y su directorio raíz de instalación, si existe.
- `marketplace/upgrade` - actualiza un marketplace de Git configurado, o todos los marketplaces de Git configurados si omites el nombre del marketplace.
- `plugin/list` - en desarrollo; enumera los marketplaces de complementos detectados y el estado de los complementos, incluidos los metadatos de las políticas de instalación y autenticación, los errores de carga de marketplaces, los ID de complementos destacados y los metadatos de origen de complementos locales, de Git, de registros de paquetes o remotos. Los resúmenes pueden incluir la versión remota en `version`, la versión local en `localVersion`, íconos estructurados para los temas claro y oscuro, y `installPolicySource`, que en las entradas remotas actuales puede ser `null`, `WORKSPACE_SETTING` o `IMPLICIT_CANONICAL_APP`. No invoques todavía este método desde clientes en producción.
- `plugin/read` - en desarrollo; lee un complemento por la ruta del marketplace o por el nombre del marketplace remoto y el nombre del complemento, incluidas las habilidades y apps que contiene, los nombres de servidores MCP y el campo `shareUrl` del complemento remoto cuando el catálogo remoto lo proporciona. No invoques todavía este método desde clientes en producción.
- `plugin/install` - en desarrollo; instala un complemento a partir de la ruta de un marketplace o del nombre de un marketplace remoto. No invoques todavía este método desde clientes en producción.
- `plugin/uninstall` - en desarrollo; desinstala un complemento instalado. No invoques todavía este método desde clientes en producción.
- `plugin/skill/read` - lee a pedido el Markdown de una habilidad de un complemento remoto según el marketplace remoto, el ID del complemento y el nombre de la habilidad.
- `app/installed` - lee el estado de ejecución de las apps instaladas, incluido si cada app está efectivamente habilitada y se puede invocar.
- `app/list` - enumera las apps disponibles (conectores) con paginación y metadatos que indican si son accesibles y están habilitadas.
- `app/read` - obtiene metadatos y resúmenes opcionales de herramientas destinados solo a mostrarse, correspondientes a ID específicos de apps.
- `skills/config/write` - habilita o deshabilita habilidades según su ruta.
- `mcpServer/oauth/login` - inicia un flujo de inicio de sesión OAuth para un servidor MCP configurado; devuelve una URL de autorización y emite `mcpServer/oauthLogin/completed` al completarse.
- `tool/requestUserInput` - solicita al usuario que responda de 1 a 3 preguntas breves para una llamada a una herramienta (experimental); las preguntas pueden establecer `isOther` para ofrecer una opción de respuesta libre.
- `mcpServer/elicitation/request` (solicitud del servidor) - solicita al cliente datos de un formulario estructurado o la confirmación de un flujo mediante URL solicitado por un servidor MCP.
- `item/permissions/requestApproval` (solicitud del servidor) - solicita al cliente que otorgue un subconjunto de los permisos de red o del sistema de archivos solicitados por la herramienta integrada `request_permissions`.
- `config/mcpServer/reload` - vuelve a cargar desde el disco la configuración de los servidores MCP y pone en cola una actualización para los hilos cargados.
- `mcpServerStatus/list` - lista los servidores MCP, las herramientas, los recursos y el estado de autenticación (paginación por cursor y límite). Usa `detail: "full"` para obtener todos los datos o `detail: "toolsAndAuthOnly"` para omitir los recursos.
- `mcpServer/resource/read` - lee un único recurso MCP mediante un servidor MCP inicializado.
- `mcpServer/tool/call` - llama a una herramienta en el servidor MCP configurado para un hilo.
- `mcpServer/startupStatus/updated` (notificación) - se emite cuando cambia el estado de inicio de un servidor MCP configurado para un hilo cargado.
- `windowsSandbox/setupStart` - inicia la configuración del sandbox de Windows en modo `elevated` o `unelevated`; responde rápidamente y luego emite `windowsSandbox/setupCompleted`.
- `feedback/upload` - envía un informe de comentarios (clasificación + motivo/registros opcionales + ID de conversación, además de archivos adjuntos `extraLogFiles` opcionales).
- `config/read` - obtiene la configuración efectiva en disco después de resolver las distintas capas de configuración.
- `externalAgentConfig/detect` - detecta artefactos de agentes externos que se pueden migrar con `includeHome` y, opcionalmente, `cwds`; cada elemento detectado incluye `cwd` (`null` para el directorio personal).
- `externalAgentConfig/import` - aplica los elementos seleccionados para la migración desde agentes externos al pasar explícitamente `migrationItems` con `cwd` (`null` para el directorio personal). Los tipos de elementos admitidos incluyen configuración, habilidades, `AGENTS.md`, complementos, configuración de servidores MCP, subagentes, hooks, comandos y sesiones; las importaciones no vacías emiten `externalAgentConfig/import/progress` y `externalAgentConfig/import/completed` a medida que finaliza el trabajo. Las importaciones de complementos y sesiones pueden completarse de forma asíncrona.
- `config/value/write` - escribe un solo par clave-valor de configuración en el archivo `config.toml` del usuario en disco.
- `config/batchWrite` - aplica de forma atómica las modificaciones de configuración al archivo `config.toml` del usuario en disco.
- `configRequirements/read` - obtiene los requisitos de `requirements.toml`, MDM o ambos, incluidos la configuración administrada exacta, las listas de elementos permitidos, los valores fijados de `featureRequirements` y los requisitos de red (o `null` si no has configurado ninguno).
- `fs/readFile`, `fs/writeFile`, `fs/createDirectory`, `fs/getMetadata`, `fs/readDirectory`, `fs/remove`, `fs/copy`, `fs/watch`, `fs/unwatch` y `fs/changed` (notificación) - operan sobre rutas absolutas del sistema de archivos mediante la API v2 del sistema de archivos de app-server.

Los resúmenes de complementos incluyen una unión `source`. Los complementos locales devuelven
`{ "type": "local", "path": ... }`, las entradas del Marketplace basadas en Git devuelven
`{ "type": "git", "url": ..., "path": ..., "refName": ..., "sha": ... }`,
las entradas del registro de paquetes devuelven
`{ "type": "npm", "package": ..., "version": ..., "registry": ... }` y
las entradas del catálogo remoto devuelven `{ "type": "remote" }`. Para las entradas de catálogo exclusivamente
remotas, `PluginMarketplaceEntry.path` puede ser `null`; pasa
`remoteMarketplaceName` en lugar de `marketplacePath` al leer o instalar
esos complementos.

## Modelos

### Listar modelos (`model/list`)

Llama a `model/list` para conocer los modelos disponibles y sus capacidades antes de renderizar los selectores de modelo o personalidad.

```json
{ "method": "model/list", "id": 6, "params": { "limit": 20, "includeHidden": false } }
{ "id": 6, "result": {
  "data": [{
    "id": "gpt-5.6-sol",
    "model": "gpt-5.6-sol",
    "displayName": "GPT-5.6-Sol",
    "hidden": false,
    "defaultReasoningEffort": "low",
    "supportedReasoningEfforts": [{
      "reasoningEffort": "low",
      "description": "Fast responses with lighter reasoning"
    }],
    "inputModalities": ["text", "image"],
    "supportsPersonality": true,
    "isDefault": true
  }],
  "nextCursor": null
} }

Cada entrada de modelo puede incluir:

- `supportedReasoningEfforts` - opciones de esfuerzo que admite el modelo.
- `defaultReasoningEffort` - esfuerzo predeterminado sugerido para los clientes.
- `upgrade` - ID opcional del modelo recomendado para la actualización, usado en los prompts de migración de los clientes.
- `upgradeInfo` - metadatos opcionales de actualización para los prompts de migración en los clientes.
- `hidden` - indica si el modelo está oculto en la lista predeterminada del selector.
- `inputModalities` - tipos de entrada que admite el modelo (por ejemplo, `text` y `image`).
- `supportsPersonality` - indica si el modelo admite instrucciones específicas de personalidad, como `/personality`.
- `isDefault` - indica si el modelo es la opción predeterminada recomendada.

De forma predeterminada, `model/list` solo devuelve los modelos visibles en el selector. Establece `includeHidden: true` si necesitas la lista completa y quieres filtrarla del lado del cliente mediante `hidden`.

Si falta `inputModalities` (en catálogos de modelos anteriores), usa `["text", "image"]` como valor para mantener la compatibilidad con versiones anteriores.

### Listar funciones experimentales (`experimentalFeature/list`)

Usa este punto de acceso para conocer los indicadores de funciones con sus metadatos y su etapa del ciclo de vida:

```json
{ "method": "experimentalFeature/list", "id": 7, "params": { "limit": 20 } }
{ "id": 7, "result": {
  "data": [{
    "name": "unified_exec",
    "stage": "beta",
    "displayName": "Unified exec",
    "description": "Use the unified PTY-backed execution tool.",
    "announcement": "Beta rollout for improved command execution reliability.",
    "enabled": false,
    "defaultEnabled": false
  }],
  "nextCursor": null
} }

`stage` puede ser `beta`, `underDevelopment`, `stable`, `deprecated` o `removed`. Para los indicadores que no están en fase beta, `displayName`, `description` y `announcement` pueden ser `null`.

### Inspeccionar un entorno de ejecución (experimental)

Usa `environment/info` para inspeccionar un entorno remoto configurado antes de
empezar a trabajar en él. El método requiere `capabilities.experimentalApi = true`.

```json
{ "method": "environment/info", "id": 8, "params": { "environmentId": "devbox" } }
{ "id": 8, "result": {
  "shell": { "name": "zsh", "path": "/bin/zsh" },
  "cwd": "file:///workspace/project"
} }

`cwd` puede ser `null`. Cuando está presente, es un URI `file:` canónico que usa la
sintaxis de rutas nativa del entorno. Los ID de entorno desconocidos y las fallas de conexión o
de protocolo hacen que se devuelvan errores de solicitud.

## Hilos

- `thread/read` lee un hilo almacenado sin suscribirse a él; establece `includeTurns` para incluir los turnos.
- `thread/turns/list` es experimental y permite consultar por páginas el historial de turnos de un hilo almacenado sin
  reanudarlo. Usa `itemsView` para elegir si los elementos de los turnos se omiten,
  se resumen o se cargan por completo.
- `thread/items/list` es experimental y permite consultar por páginas los elementos almacenados de un hilo, con la opción de restringirlos a un solo turno.
- `thread/list` admite paginación por cursor y filtros por `modelProviders`, `sourceKinds`, `archived`, `isPinned`, `cwd`, `useStateDbOnly` y `searchTerm`, además de filtros experimentales por `parentThreadId` o `ancestorThreadId`.
- `thread/loaded/list` devuelve los ID de los hilos que están actualmente en memoria.
- `thread/archive` mueve el registro JSONL almacenado del hilo al directorio de elementos archivados e intenta archivar los registros de los hilos descendientes generados que aún no estén archivados.
- `thread/delete` elimina de forma permanente un hilo almacenado, activo o archivado, y sus hilos descendientes generados.
- `thread/metadata/update` actualiza parcialmente los metadatos almacenados del hilo, incluidos los valores guardados de `gitInfo` y `isPinned`.
- `thread/unsubscribe` cancela la suscripción de la conexión actual a un hilo cargado y puede desencadenar `thread/closed` después de un período de gracia por inactividad.
- `thread/unarchive` restaura el registro de sesión de un hilo archivado en el directorio de sesiones activas.
- `thread/compact/start` activa la compactación y devuelve `{}` de inmediato.
- `thread/rollback` está en desuso. Quita los últimos N turnos del contexto en memoria y registra un marcador de reversión en el registro JSONL almacenado del hilo.
- `thread/inject_items` agrega elementos sin procesar de Responses API al historial visible para el modelo de un hilo cargado, sin iniciar un turno del usuario.

### Iniciar o reanudar un hilo

Inicia un hilo nuevo cuando necesites una nueva conversación con Codex.

```json
{ "method": "thread/start", "id": 10, "params": {
  "model": "gpt-5.6-terra",
  "cwd": "/Users/me/project",
  "approvalPolicy": "never",
  "sandbox": "workspaceWrite",
  "personality": "friendly",
  "serviceName": "my_app_server_client"
} }
{ "id": 10, "result": {
  "thread": {
    "id": "thr_123",
    "sessionId": "thr_123",
    "preview": "",
    "ephemeral": false,
    "modelProvider": "openai",
    "createdAt": 1730910000
  }
} }
{ "method": "thread/started", "params": { "thread": { "id": "thr_123" } } }

`serviceName` es opcional. Establécelo si quieres que app-server etiquete las métricas a nivel de hilo con el nombre del servicio de tu integración.

`thread/start`, `thread/resume` y `thread/fork` devuelven
`instructionSources`, un arreglo de rutas de archivos de instrucciones cargados. Cada ruta usa
la sintaxis nativa de rutas absolutas de su entorno de origen, incluso en entornos
remotos.

Los clientes experimentales pueden asignar a `historyMode` en `thread/start` el valor `"legacy"`
(el valor predeterminado) o `"paginated"`. La creación de hilos paginados aún no se admite
y devuelve el error JSON-RPC `-32601`. App-server puede listar y leer resúmenes de
registros paginados existentes, pero las lecturas del historial completo, la paginación de turnos y la reanudación
se rechazan hasta que se admita el historial paginado.

Los clientes beta que habiliten `capabilities.experimentalApi` pueden pasar el ID de un perfil
de permisos con nombre en `permissions` en lugar del campo heredado `sandbox`.
No envíes `permissions` y `sandbox` juntos. Usa
`permissionProfile/list` con el `cwd` del proyecto para consultar los perfiles disponibles
y si los requisitos administrados permiten cada uno.

`thread.sessionId` identifica la raíz del árbol de la sesión activa actual. Los hilos raíz
usan su propio ID de hilo como ID de sesión; los hilos creados mediante fork conservan el ID de sesión
de la raíz de la que provienen. Los clientes deben leer el ID de sesión de
`thread.sessionId` en lugar de derivarlo del ID del hilo.

Para continuar una sesión almacenada, llama a `thread/resume` con el `thread.id` que registraste antes. La estructura de la respuesta coincide con la de `thread/start`. También puedes pasar las mismas opciones para sobrescribir la configuración que admite `thread/start`, como `personality`:

```json
{ "method": "thread/resume", "id": 11, "params": {
  "threadId": "thr_123",
  "personality": "friendly"
} }
{ "id": 11, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false } } }

Reanudar un hilo no actualiza por sí solo `thread.updatedAt` (ni la fecha y hora de modificación del archivo de registro de la sesión). La marca de tiempo se actualiza cuando inicias un turno.

Si en la configuración marcas un servidor MCP habilitado como `required` y ese servidor no logra inicializarse, `thread/start` y `thread/resume` fallan en lugar de continuar sin él.

`dynamicTools` en `thread/start` es un campo experimental (requiere `capabilities.experimentalApi = true`). Codex almacena estas herramientas dinámicas en los metadatos del registro de ejecución del hilo y las restaura en `thread/resume` cuando no proporcionas herramientas dinámicas nuevas.

Si reanudas la sesión con un modelo distinto del que figura en el registro de ejecución, Codex emite una advertencia y aplica una instrucción de cambio de modelo una sola vez, en el siguiente turno.

### Administrar la meta de un hilo

Usa `thread/goal/set`, `thread/goal/get` y `thread/goal/clear` para administrar el
mismo estado almacenado de la meta que `/goal` muestra en la TUI.

```json
{ "method": "thread/goal/set", "id": 13, "params": {
  "threadId": "thr_123",
  "objective": "Finish the migration and keep tests green",
  "status": "active",
  "tokenBudget": 40000
} }
{ "id": 13, "result": { "goal": {
  "threadId": "thr_123",
  "objective": "Finish the migration and keep tests green",
  "status": "active",
  "tokenBudget": 40000,
  "tokensUsed": 0,
  "timeUsedSeconds": 0
} } }
{ "method": "thread/goal/updated", "params": {
  "threadId": "thr_123",
  "goal": {
    "threadId": "thr_123",
    "objective": "Finish the migration and keep tests green",
    "status": "active",
    "tokenBudget": 40000,
    "tokensUsed": 0,
    "timeUsedSeconds": 0
  }
} }

El objetivo de una meta no puede estar vacío ni superar los 4000 caracteres. Proporcionar un nuevo
objetivo reemplaza la meta y reinicia la contabilización del uso. Proporcionar el objetivo actual
que no haya alcanzado un estado final, u omitir `objective`, actualiza el estado o el presupuesto de tokens
sin modificar el historial de uso.

Para crear un fork a partir de una sesión almacenada, llama a `thread/fork` con `thread.id`. Esto crea un nuevo ID de hilo y emite una notificación `thread/started` para ese hilo. Pasa
`lastTurnId` para copiar el historial hasta ese turno inclusive y omitir los
turnos posteriores:

```json
{ "method": "thread/fork", "id": 12, "params": { "threadId": "thr_123", "lastTurnId": "turn_456" } }
{ "id": 12, "result": { "thread": { "id": "thr_456", "sessionId": "thr_123", "forkedFromId": "thr_123" } } }
{ "method": "thread/started", "params": { "thread": { "id": "thr_456" } } }

App-server rechaza un `lastTurnId` que corresponda a un turno en curso. Si omites el campo mientras el
hilo de origen está a mitad de un turno, el fork registra un marcador de interrupción en lugar de
conservar un turno parcial sin marcar.

Pasa `ephemeral: true` para crear un fork en memoria sin agregarlo a las listas de
hilos almacenados:

```json
{
  "method": "thread/fork",
  "id": 13,
  "params": {
    "threadId": "thr_123",
    "ephemeral": true
  }
}
{
  "id": 13,
  "result": {
    "thread": {
      "id": "thr_789",
      "sessionId": "thr_789",
      "forkedFromId": "thr_123",
      "ephemeral": true
    }
  }
}

Los forks efímeros de hilos paginados también requieren `excludeTurns: true`. Ese
campo es experimental y requiere `capabilities.experimentalApi = true`.

Cuando se ha establecido un título de hilo visible para el usuario, app-server completa `thread.name` en las respuestas de `thread/list`, `thread/read`, `thread/resume`, `thread/unarchive` y `thread/rollback`. `thread/start` y `thread/fork` pueden omitir `name` (o devolver `null`) hasta que se establezca un título más adelante.

### Leer un hilo almacenado (sin reanudarlo)

Usa `thread/read` cuando necesites los datos almacenados de un hilo, pero no quieras reanudarlo ni suscribirte a sus eventos.

- `includeTurns` - cuando es `true`, la respuesta incluye los turnos del hilo; cuando es `false` o se omite, solo obtienes el resumen del hilo.
- Los objetos `thread` devueltos incluyen el estado en tiempo de ejecución en `status` (`notLoaded`, `idle`, `systemError` o `active` con `activeFlags`).

```json
{ "method": "thread/read", "id": 19, "params": { "threadId": "thr_123", "includeTurns": true } }
{ "id": 19, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false, "status": { "type": "notLoaded" }, "turns": [] } } }

A diferencia de `thread/resume`, `thread/read` no carga el hilo en memoria ni emite `thread/started`.

### Listar los turnos de un hilo

`thread/turns/list` es experimental. Úsalo para consultar por páginas el historial de turnos de un hilo almacenado sin reanudarlo. De forma predeterminada, los resultados se ordenan del más reciente al más antiguo, para que los clientes puedan obtener turnos anteriores con `nextCursor`. La respuesta también incluye `backwardsCursor`; pásalo como `cursor` con `sortDirection: "asc"` para obtener turnos más recientes que el primer elemento de la página anterior.

`itemsView` controla cuántos datos de los elementos del turno incluye la respuesta:

- `notLoaded` omite los elementos.
- `summary` devuelve datos resumidos de los elementos y es el valor predeterminado cuando se omite el campo.
- `full` devuelve los datos completos de los elementos.

```json
{ "method": "thread/turns/list", "id": 20, "params": {
  "threadId": "thr_123",
  "limit": 50,
  "sortDirection": "desc",
  "itemsView": "summary"
} }
{ "id": 20, "result": {
  "data": [],
  "nextCursor": "older-turns-cursor-or-null",
  "backwardsCursor": "newer-turns-cursor-or-null"
} }

`thread/items/list` también es experimental. Permite consultar por páginas los elementos almacenados sin
reanudar el hilo. Pasa `turnId` para limitar los resultados a un turno u omítelo
para consultar por páginas los elementos de todo el hilo. El almacén de hilos activo debe admitir la
paginación de elementos; de lo contrario, el servidor devuelve un error de método no compatible.

### Listar hilos (con paginación y filtros)

`thread/list` te permite renderizar una interfaz de historial. De forma predeterminada, los resultados se ordenan del más reciente al más antiguo según `createdAt`. Los filtros se aplican antes de la paginación. Pasa los siguientes parámetros en cualquier combinación:

- `cursor` - cadena opaca de una respuesta anterior; omite este campo para la primera página.
- `limit` - si no se establece, el servidor usa un tamaño de página razonable de forma predeterminada.
- `sortKey` - `created_at` (predeterminado), `updated_at` o `recency_at`.
- `sortDirection` - `desc` (predeterminado) o `asc`.
- `modelProviders` - limita los resultados a proveedores específicos; si no se establece, es null o es un arreglo vacío, se incluyen todos los proveedores.
- `sourceKinds` - limita los resultados a hilos de orígenes específicos. Cuando se omite o es `[]`, el servidor usa de forma predeterminada solo orígenes interactivos: `cli` y `vscode`.
- `archived` - cuando es `true`, lista solo los hilos archivados. Cuando es `false` o se omite, lista los hilos no archivados (valor predeterminado).
- `isPinned` - cuando se proporciona, devuelve solo los hilos cuyo estado de fijación almacenado coincida. Omítelo para devolver los hilos fijados y no fijados.
- `cwd` - limita los resultados a hilos en los que el directorio de trabajo actual de la sesión coincida exactamente con esta ruta o con una de las rutas de un arreglo. Las rutas relativas se resuelven a partir del directorio de trabajo del proceso app-server.
- `useStateDbOnly` - cuando es `true`, devuelve los resultados de la base de datos de estado sin analizar los registros JSONL de los hilos para reparar los metadatos. Omítelo o pasa `false` para usar el comportamiento predeterminado de análisis y reparación.
- `searchTerm` - limita los resultados a los hilos cuyo título extraído contenga este fragmento de texto, distinguiendo entre mayúsculas y minúsculas.
- `parentThreadId` - limita los resultados a los hilos hijos directos del hilo padre indicado. Este filtro es experimental y requiere `capabilities.experimentalApi = true`.
- `ancestorThreadId` - limita los resultados a los hilos descendientes generados a partir del hilo indicado, a cualquier profundidad. Este filtro es experimental y requiere `capabilities.experimentalApi = true`; no lo combines con `parentThreadId`.

`sourceKinds` acepta los siguientes valores:

- `cli`
- `vscode`
- `exec`
- `appServer`
- `subAgent`
- `subAgentReview`
- `subAgentCompact`
- `subAgentThreadSpawn`
- `subAgentOther`
- `unknown`

Ejemplo:

```json
{ "method": "thread/list", "id": 20, "params": {
  "cursor": null,
  "limit": 25,
  "sortKey": "created_at"
} }
{ "id": 20, "result": {
  "data": [
    { "id": "thr_a", "preview": "Create a TUI", "ephemeral": false, "isPinned": true, "modelProvider": "openai", "createdAt": 1730831111, "updatedAt": 1730831111, "name": "TUI prototype", "status": { "type": "notLoaded" } },
    { "id": "thr_b", "preview": "Fix tests", "ephemeral": false, "isPinned": false, "modelProvider": "openai", "createdAt": 1730750000, "updatedAt": 1730750000, "status": { "type": "notLoaded" } }
  ],
  "nextCursor": "opaque-token-or-null"
} }

Cuando `nextCursor` es `null`, has llegado a la última página.

### Actualizar los metadatos almacenados de un hilo

Usa `thread/metadata/update` para modificar los metadatos almacenados del hilo sin
reanudarlo. Establece `isPinned` para fijar o dejar de fijar el hilo, o actualiza `gitInfo` para cambiar los
metadatos de Git almacenados. Los campos omitidos no cambian; un valor `null` explícito borra un
valor almacenado de metadatos de Git.

```json
{ "method": "thread/metadata/update", "id": 21, "params": {
  "threadId": "thr_123",
  "isPinned": true,
  "gitInfo": { "branch": "feature/sidebar-pr" }
} }
{ "id": 21, "result": {
  "thread": {
    "id": "thr_123",
    "isPinned": true,
    "gitInfo": { "sha": null, "branch": "feature/sidebar-pr", "originUrl": null }
  }
} }

### Supervisar los cambios de estado de un hilo

`thread/status/changed` se emite cada vez que cambia el estado en tiempo de ejecución de un hilo cargado. La carga útil incluye `threadId` y el nuevo `status`.

```json
{
  "method": "thread/status/changed",
  "params": {
    "threadId": "thr_123",
    "status": { "type": "active", "activeFlags": ["waitingOnApproval"] }
  }
}

### Listar los hilos cargados

`thread/loaded/list` devuelve los ID de los hilos cargados actualmente en memoria.

```json
{ "method": "thread/loaded/list", "id": 21 }
{ "id": 21, "result": { "data": ["thr_123", "thr_456"] } }

### Cancelar la suscripción a un hilo cargado

`thread/unsubscribe` cancela la suscripción de la conexión actual a un hilo. El estado de la respuesta es uno de los siguientes:

- `unsubscribed` cuando la conexión estaba suscrita y ahora se canceló esa suscripción.
- `notSubscribed` cuando la conexión no estaba suscrita a ese hilo.
- `notLoaded` cuando el hilo no está cargado.

Si este era el último suscriptor, el servidor mantiene el hilo cargado hasta que transcurran 30 minutos sin suscriptores ni actividad en el hilo. Al vencer el período de gracia, app-server retira el hilo de la memoria y emite `thread/status/changed` para indicar la transición a `notLoaded`, además de `thread/closed`.

```json
{ "method": "thread/unsubscribe", "id": 22, "params": { "threadId": "thr_123" } }
{ "id": 22, "result": { "status": "unsubscribed" } }

Si el hilo caduca más adelante:

```json
{ "method": "thread/status/changed", "params": {
    "threadId": "thr_123",
    "status": { "type": "notLoaded" }
} }
{ "method": "thread/closed", "params": { "threadId": "thr_123" } }

### Archivar un hilo

Usa `thread/archive` para mover el registro persistente del hilo (almacenado como un archivo JSONL en el disco) al directorio de sesiones archivadas. Al archivar un hilo, también se intenta archivar los hilos descendientes generados que aún no estén archivados.

```json
{ "method": "thread/archive", "id": 22, "params": { "threadId": "thr_b" } }
{ "id": 22, "result": {} }
{ "method": "thread/archived", "params": { "threadId": "thr_b" } }
{ "method": "thread/archived", "params": { "threadId": "thr_child" } }

Los hilos archivados no aparecerán en llamadas futuras a `thread/list`, a menos que pases `archived: true`. El servidor emite una notificación `thread/archived` por cada hilo que logra archivar; si no se puede archivar un hilo descendiente generado, la solicitud puede completarse correctamente de todos modos, sin una notificación de archivado para ese descendiente.

### Eliminar un hilo

Usa `thread/delete` para eliminar de forma permanente un hilo almacenado, ya sea activo o archivado,
y sus hilos descendientes generados. El servidor elimina los archivos de registro de ejecución existentes y los
metadatos asociados antes de indicar que la operación se realizó correctamente; los archivos de registro de ejecución que faltan se consideran
ya eliminados. No se pueden eliminar los hilos raíz efímeros.

```json
{ "method": "thread/delete", "id": 23, "params": { "threadId": "thr_b" } }
{ "id": 23, "result": {} }
{ "method": "thread/deleted", "params": { "threadId": "thr_b" } }
{ "method": "thread/deleted", "params": { "threadId": "thr_child" } }

### Desarchivar un hilo

Usa `thread/unarchive` para devolver el registro de ejecución de un hilo archivado al directorio de sesiones activas.

```json
{ "method": "thread/unarchive", "id": 24, "params": { "threadId": "thr_b" } }
{ "id": 24, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes" } } }
{ "method": "thread/unarchived", "params": { "threadId": "thr_b" } }

### Iniciar la compactación de un hilo

Usa `thread/compact/start` para iniciar manualmente la compactación del historial de un hilo. La solicitud devuelve inmediatamente `{}`.

App-server comunica el progreso mediante las notificaciones estándar `turn/*` y `item/*` en el mismo `threadId`, incluido el ciclo de vida de un elemento `contextCompaction` (`item/started` y luego `item/completed`).

```json
{ "method": "thread/compact/start", "id": 25, "params": { "threadId": "thr_b" } }
{ "id": 25, "result": {} }

### Ejecutar un comando de shell en un hilo

Usa `thread/shellCommand` para los comandos de shell iniciados por el usuario que pertenecen a un hilo. La solicitud devuelve de inmediato `{}`, mientras el progreso se transmite mediante las notificaciones estándar `turn/*` y `item/*`.

Esta API se ejecuta fuera del sandbox con acceso completo y no hereda la política del sandbox del hilo. Los clientes deberían exponerla solo para comandos que el usuario inicie explícitamente.

Si el hilo ya tiene un turno activo, el comando se ejecuta como una acción auxiliar de ese turno y su salida con formato se inserta en el flujo de mensajes del turno. Si el hilo está inactivo, app-server inicia un turno independiente para el comando de shell.

Configura `timeoutMs` para limitar el tiempo de ejecución en milisegundos. Si lo omites o pasas
`null`, se usa el valor predeterminado de una hora. `0` solicita que el tiempo de espera venza de inmediato; se rechazan los
valores negativos. El tiempo de espera no retrasa la confirmación inmediata de recepción de la RPC.

```json
{ "method": "thread/shellCommand", "id": 26, "params": { "threadId": "thr_b", "command": "git status --short", "timeoutMs": 10000 } }
{ "id": 26, "result": {} }

### Limpiar terminales en segundo plano

Usa `thread/backgroundTerminals/clean` para detener todas las terminales en segundo plano en ejecución asociadas a un hilo. Este método es experimental y requiere `capabilities.experimentalApi = true`.

```json
{ "method": "thread/backgroundTerminals/clean", "id": 27, "params": { "threadId": "thr_b" } }
{ "id": 27, "result": {} }

Usa `thread/backgroundTerminals/list` para consultar las terminales en segundo plano en ejecución
asociadas a un hilo cargado. La solicitud admite los parámetros estándar `cursor` y `limit`
para la paginación, y el valor `processId` devuelto es el identificador de proceso de app-server. Este
método es experimental y requiere `capabilities.experimentalApi = true`:

```json
{ "method": "thread/backgroundTerminals/list", "id": 28, "params": { "threadId": "thr_b" } }
{ "id": 28, "result": { "data": [
  {
    "itemId": "item_456",
    "processId": "42",
    "command": "python3 -m http.server",
    "cwd": "/workspace",
    "osPid": null,
    "cpuPercent": null,
    "rssKb": null
  }
], "nextCursor": null } }

Usa `thread/backgroundTerminals/terminate` con ese `processId` para detener una
terminal en segundo plano. Este método es experimental y requiere
`capabilities.experimentalApi = true`:

```json
{ "method": "thread/backgroundTerminals/terminate", "id": 29, "params": { "threadId": "thr_b", "processId": "42" } }
{ "id": 29, "result": { "terminated": true } }

### Revertir turnos recientes

`thread/rollback` está obsoleto y se eliminará. Elimina las últimas
`numTurns` entradas del contexto en memoria y guarda de forma persistente un marcador de reversión en
el registro de rollout. El objeto `thread` devuelto incluye `turns` con los datos actualizados tras la
reversión.

```json
{ "method": "thread/rollback", "id": 30, "params": { "threadId": "thr_b", "numTurns": 1 } }
{ "id": 30, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes", "ephemeral": false } } }

## Turnos

El campo `input` acepta una lista de elementos:

- `{ "type": "text", "text": "Explain this diff" }`
- `{ "type": "image", "url": "https://.../design.png" }`
- `{ "type": "localImage", "path": "/tmp/screenshot.png" }`

Puedes sobrescribir las opciones de configuración para cada turno (modelo, esfuerzo, personalidad, `cwd`, política del sandbox y resumen). Cuando se especifican, estas opciones se convierten en los valores predeterminados para turnos posteriores del mismo hilo. `outputSchema` se aplica solo al turno actual. Para `sandboxPolicy.type = "externalSandbox"`, configura `networkAccess` como `restricted` o `enabled`; para `workspaceWrite`, `networkAccess` sigue siendo un valor booleano.

En el caso de `turn/start.collaborationMode`, `settings.developer_instructions: null` significa “usar las instrucciones integradas del modo seleccionado”, en lugar de borrar las instrucciones del modo.

### Acceso de lectura en el sandbox (`ReadOnlyAccess`)

`sandboxPolicy` admite controles explícitos de acceso de lectura:

- `readOnly`: `access` opcional (`{ "type": "fullAccess" }` de forma predeterminada, o acceso restringido a determinados directorios raíz).
- `workspaceWrite`: `readOnlyAccess` opcional (`{ "type": "fullAccess" }` de forma predeterminada, o acceso restringido a determinados directorios raíz).

Estructura del acceso de lectura restringido:

```json
{
  "type": "restricted",
  "includePlatformDefaults": true,
  "readableRoots": ["/Users/me/shared-read-only"]
}

En macOS, `includePlatformDefaults: true` agrega una política de Seatbelt predeterminada para la plataforma, seleccionada cuidadosamente para las sesiones con acceso de lectura restringido. Esto mejora la compatibilidad con las herramientas sin permitir de forma general el acceso a todo `/System`.

Ejemplos:

```json
{ "type": "readOnly", "access": { "type": "fullAccess" } }

```json
{
  "type": "workspaceWrite",
  "writableRoots": ["/Users/me/project"],
  "readOnlyAccess": {
    "type": "restricted",
    "includePlatformDefaults": true,
    "readableRoots": ["/Users/me/shared-read-only"]
  },
  "networkAccess": false
}

### Iniciar un turno

```json
{ "method": "turn/start", "id": 30, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Run tests" } ],
  "cwd": "/Users/me/project",
  "approvalPolicy": "unlessTrusted",
  "sandboxPolicy": {
    "type": "workspaceWrite",
    "writableRoots": ["/Users/me/project"],
    "networkAccess": true
  },
  "model": "gpt-5.6-terra",
  "effort": "medium",
  "summary": "concise",
  "personality": "friendly",
  "outputSchema": {
    "type": "object",
    "properties": { "answer": { "type": "string" } },
    "required": ["answer"],
    "additionalProperties": false
  }
} }
{ "id": 30, "result": { "turn": { "id": "turn_456", "status": "inProgress", "items": [], "error": null } } }

Para iniciar un turno con la salida de una herramienta que ejecutó tu cliente, pasa `toolOutput`
con un `name` no vacío, un `namespace` opcional y un `output` que sea una cadena o un
arreglo de elementos de contenido. Configura `input` como un arreglo vacío; no puedes combinar
`toolOutput` con una entrada de usuario no vacía.

```json
{
  "method": "turn/start",
  "id": 31,
  "params": {
    "threadId": "thr_123",
    "input": [],
    "toolOutput": {
      "name": "run_tests",
      "namespace": null,
      "output": "All 42 tests passed."
    }
  }
}

La salida se mantiene como salida de herramienta en la conversación y aparece como un elemento
`functionCallOutput` en las notificaciones y en el historial persistente. Si ya hay un turno normal
activo, Codex pone la salida en cola para ese turno.

### Inyectar elementos en un hilo

Usa `thread/inject_items` para agregar elementos ya preparados de Responses API al historial de prompts de un hilo cargado sin iniciar un turno del usuario. Estos elementos se guardan de forma persistente en el rollout y se incluyen en solicitudes posteriores dirigidas al modelo.

```json
{ "method": "thread/inject_items", "id": 31, "params": {
  "threadId": "thr_123",
  "items": [
    {
      "type": "message",
      "role": "assistant",
      "content": [{ "type": "output_text", "text": "Previously computed context." }]
    }
  ]
} }
{ "id": 31, "result": {} }

### Guiar un turno activo

Usa `turn/steer` para agregar más entradas del usuario al turno activo en curso.

- Incluye `expectedTurnId`; debe coincidir con el identificador del turno activo.
- La solicitud falla si el hilo no tiene un turno activo.
- `turn/steer` no emite una nueva notificación `turn/started`.
- `turn/steer` no acepta modificaciones de configuración específicas del turno (`model`, `cwd`, `sandboxPolicy` o `outputSchema`).

```json
{ "method": "turn/steer", "id": 32, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Actually focus on failing tests first." } ],
  "expectedTurnId": "turn_456"
} }
{ "id": 32, "result": { "turnId": "turn_456" } }

### Iniciar un turno (invocar una habilidad)

Invoca una habilidad explícitamente incluyendo `$<skill-name>` en la entrada de texto y agregando también un elemento de entrada `skill`.

```json
{ "method": "turn/start", "id": 33, "params": {
  "threadId": "thr_123",
  "input": [
    { "type": "text", "text": "$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage." },
    { "type": "skill", "name": "skill-creator", "path": "/Users/me/.codex/skills/skill-creator/SKILL.md" }
  ]
} }
{ "id": 33, "result": { "turn": { "id": "turn_457", "status": "inProgress", "items": [], "error": null } } }

### Interrumpir un turno

```json
{ "method": "turn/interrupt", "id": 31, "params": { "threadId": "thr_123", "turnId": "turn_456" } }
{ "id": 31, "result": {} }

Si la operación se completa correctamente, el turno finaliza con `status: "interrupted"`.

## Revisión

`review/start` ejecuta el revisor de Codex para un hilo y transmite los elementos de revisión. Los objetivos de revisión incluyen:

- `uncommittedChanges`
- `baseBranch` (diferencias con respecto a una rama)
- `commit` (revisar un commit específico)
- `custom` (instrucciones de formato libre)

Usa `delivery: "inline"` (opción predeterminada) para ejecutar la revisión en el hilo existente, o `delivery: "detached"` para crear un nuevo hilo de revisión mediante un fork.

Ejemplo de solicitud y respuesta:

```json
{ "method": "review/start", "id": 40, "params": {
  "threadId": "thr_123",
  "delivery": "inline",
  "target": { "type": "commit", "sha": "1234567deadbeef", "title": "Polish tui colors" }
} }
{ "id": 40, "result": {
  "turn": {
    "id": "turn_900",
    "status": "inProgress",
    "items": [
      { "type": "userMessage", "id": "turn_900", "content": [ { "type": "text", "text": "Review commit 1234567: Polish tui colors" } ] }
    ],
    "error": null
  },
  "reviewThreadId": "thr_123"
} }

Para una revisión separada, usa `"delivery": "detached"`. La respuesta tiene la misma estructura, pero `reviewThreadId` será el identificador del nuevo hilo de revisión (distinto del `threadId` original). El servidor también emite una notificación `thread/started` para ese nuevo hilo antes de transmitir el turno de revisión.

Codex transmite la notificación `turn/started` habitual, seguida de una notificación `item/started` con un elemento `enteredReviewMode`:

```json
{
  "method": "item/started",
  "params": {
    "item": {
      "type": "enteredReviewMode",
      "id": "turn_900",
      "review": "current changes"
    }
  }
}

Cuando el revisor finaliza, el servidor emite las notificaciones `item/started` y `item/completed`, que contienen un elemento `exitedReviewMode` con el texto final de la revisión:

```json
{
  "method": "item/completed",
  "params": {
    "item": {
      "type": "exitedReviewMode",
      "id": "turn_900",
      "review": "Looks solid overall..."
    }
  }
}

Usa esta notificación para mostrar la salida del revisor en tu cliente.

## Ejecución de procesos

`process/*` es una API experimental para el control explícito de procesos. Requiere
`capabilities.experimentalApi = true` y se ejecuta fuera del sandbox de Codex. Úsala
solo cuando tu cliente exponga intencionalmente el control local de procesos sin un
sandbox.

Inicia un proceso con `process/spawn` y proporciona un `processHandle`; luego usa
ese identificador para las solicitudes de stdin, cambio de tamaño y terminación. La salida se transmite mediante las notificaciones
`process/outputDelta`, y la finalización se comunica mediante
`process/exited`.

```json
{ "method": "process/spawn", "id": 48, "params": {
  "command": ["python3", "-m", "pytest", "-q"],
  "processHandle": "pytest-1",
  "cwd": "/Users/me/project",
  "tty": true
} }
{ "id": 48, "result": {} }
{ "method": "process/outputDelta", "params": {
  "processHandle": "pytest-1",
  "stream": "stdout",
  "deltaBase64": "Li4u"
} }
{ "method": "process/exited", "params": {
  "processHandle": "pytest-1",
  "exitCode": 0
} }

Usa `process/writeStdin` con `deltaBase64`, `closeStdin` o ambos para enviar
datos de entrada. Usa `process/resizePty` para los eventos de cambio de tamaño de PTY y `process/kill` para
terminar un proceso en ejecución.

## Ejecución de comandos

`command/exec` ejecuta un solo comando (un arreglo `argv`) dentro del sandbox del servidor sin crear un hilo.

```json
{ "method": "command/exec", "id": 50, "params": {
  "command": ["ls", "-la"],
  "cwd": "/Users/me/project",
  "sandboxPolicy": { "type": "workspaceWrite" },
  "timeoutMs": 10000
} }
{ "id": 50, "result": { "exitCode": 0, "stdout": "...", "stderr": "" } }

Usa `sandboxPolicy.type = "externalSandbox"` si ya ejecutas el proceso del servidor dentro de un sandbox y quieres que Codex omita la aplicación de su propio sandbox. Para el modo de sandbox externo, configura `networkAccess` como `restricted` (opción predeterminada) o `enabled`. Para `readOnly` y `workspaceWrite`, usa la misma estructura opcional de `access` / `readOnlyAccess` que se mostró antes.

Notas:

- El servidor rechaza los arreglos `command` vacíos.
- `sandboxPolicy` acepta la misma estructura que usa `turn/start` (por ejemplo, `dangerFullAccess`, `readOnly`, `workspaceWrite` y `externalSandbox`).
- Si se omite, `timeoutMs` usa el valor predeterminado del servidor.
- Configura `tty: true` para las sesiones basadas en PTY y usa `processId` si después planeas usar `command/exec/write`, `command/exec/resize` o `command/exec/terminate`.
- Configura `streamStdoutStderr: true` para recibir notificaciones `command/exec/outputDelta` mientras se ejecuta el comando.

### Consultar los requisitos del administrador (`configRequirements/read`)

Usa `configRequirements/read` para consultar los requisitos efectivos del administrador cargados desde `requirements.toml` o MDM, o desde ambos.

```json
{ "method": "configRequirements/read", "id": 52, "params": {} }
{ "id": 52, "result": {
  "requirements": {
    "allowedApprovalPolicies": ["onRequest", "unlessTrusted"],
    "allowedSandboxModes": ["readOnly", "workspaceWrite"],
    "featureRequirements": {
      "personality": true,
      "unified_exec": false
    },
    "network": {
      "enabled": true,
      "allowedDomains": ["api.openai.com"],
      "allowUnixSockets": ["/tmp/example.sock"],
      "dangerouslyAllowAllUnixSockets": false
    }
  }
} }

`result.requirements` es `null` cuando no hay requisitos configurados. Consulta la documentación sobre [`requirements.toml`](/es-419/codex/config-file/config-reference#requirementstoml) para conocer las claves y los valores admitidos.

### Configuración del sandbox de Windows (`windowsSandbox/setupStart`)

Los clientes personalizados de Windows pueden iniciar la configuración del sandbox de forma asíncrona en lugar de bloquearse durante las comprobaciones de inicio.

```json
{ "method": "windowsSandbox/setupStart", "id": 53, "params": { "mode": "elevated" } }
{ "id": 53, "result": { "started": true } }

App-server inicia la configuración en segundo plano y luego emite una notificación de finalización:

```json
{
  "method": "windowsSandbox/setupCompleted",
  "params": { "mode": "elevated", "success": true, "error": null }
}

Modos:

- `elevated` - ejecuta el procedimiento de configuración del Sandbox de Windows con privilegios elevados.
- `unelevated` - ejecuta el procedimiento heredado de configuración/comprobación previa.

## Sistema de archivos

Las API v2 del sistema de archivos operan con rutas absolutas. Usa `fs/watch` cuando un cliente necesite invalidar el estado de la interfaz de usuario después de que cambie un archivo o directorio.

```json
{ "method": "fs/watch", "id": 54, "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
  "path": "/Users/me/project/.git/HEAD"
} }
{ "id": 54, "result": { "path": "/Users/me/project/.git/HEAD" } }
{ "method": "fs/changed", "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
  "changedPaths": ["/Users/me/project/.git/HEAD"]
} }
{ "method": "fs/unwatch", "id": 55, "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1"
} }
{ "id": 55, "result": {} }

Al supervisar un archivo, se emite `fs/changed` para su ruta, incluidas las actualizaciones generadas por operaciones de reemplazo o cambio de nombre.

## Eventos

Las notificaciones de eventos constituyen el flujo iniciado por el servidor para los ciclos de vida de los hilos, los turnos y los elementos que contienen. Después de iniciar o reanudar un hilo, sigue leyendo el flujo de transporte activo para recibir las notificaciones `thread/started`, `thread/archived`, `thread/unarchived`, `thread/closed`, `thread/status/changed`, `turn/*`, `item/*` y `serverRequest/resolved`.

### Exclusión de notificaciones

Los clientes pueden suprimir notificaciones específicas por conexión al enviar nombres exactos de métodos en `initialize.params.capabilities.optOutNotificationMethods`.

- Solo coincidencias exactas: `item/agentMessage/delta` suprime únicamente ese método.
- Se ignoran los nombres de métodos desconocidos.
- Se aplica a las notificaciones actuales `thread/*`, `turn/*`, `item/*` y a las notificaciones v2 relacionadas.
- No se aplica a solicitudes, respuestas ni errores.

### Eventos de búsqueda aproximada de archivos (experimental)

La API de sesiones de búsqueda aproximada de archivos emite notificaciones para cada consulta:

- `fuzzyFileSearch/sessionUpdated` - `{ sessionId, query, files }` con las coincidencias actuales de la consulta activa.
- `fuzzyFileSearch/sessionCompleted` - `{ sessionId }` cuando se completan la indexación y la búsqueda de coincidencias de esa consulta.

### Eventos de advertencia

- `configWarning` - `{ summary, details?, path?, range? }` para problemas recuperables de
  configuración o inicialización.
- `warning` - `{ threadId?, message }` para advertencias no fatales durante la ejecución.

### Eventos de configuración del Sandbox de Windows

- `windowsSandbox/setupCompleted` - `{ mode, success, error }`, que se emite después de que finaliza una solicitud `windowsSandbox/setupStart`.

### Eventos de turnos

- `turn/started` - `{ turn }` con el identificador del turno, el campo `items` vacío y `status: "inProgress"`.
- `turn/completed` - `{ turn }`, donde `turn.status` es `completed`, `interrupted` o `failed`; las fallas incluyen `{ error: { message, codexErrorInfo?, additionalDetails? } }`.
- `turn/diff/updated` - `{ threadId, turnId, diff }` con el diff unificado acumulado más reciente de todos los cambios en archivos realizados durante el turno.
- `turn/plan/updated` - `{ turnId, explanation?, plan }` cada vez que el agente comparte o modifica su plan; cada entrada de `plan` es `{ step, status }` y `status` puede ser `pending`, `inProgress` o `completed`.
- `hook/started` y `hook/completed` - `{ threadId, turnId?, run }` cuando comienza un hook síncrono del ciclo de vida y cuando está disponible el resumen final de su ejecución. Estas notificaciones no se emiten para hooks asíncronos.
- `model/safetyBuffering/updated` - `{ threadId, turnId, model, useCases, reasons, showBufferingUi, fasterModel }` cuando una respuesta comienza a almacenarse temporalmente en un búfer por seguridad.
- `model/rerouted` - `{ threadId, turnId, fromModel, toModel, reason }` cuando el servicio enruta una solicitud a otro modelo.
- `model/verification` - `{ threadId, turnId, verifications }` cuando el servicio requiere una verificación adicional de la cuenta.
- `thread/tokenUsage/updated` - actualizaciones de uso del hilo activo.

`turn/diff/updated` y `turn/plan/updated` actualmente incluyen arreglos `items` vacíos incluso cuando se transmiten eventos de elementos. Usa las notificaciones `item/*` como fuente de información definitiva para los elementos del turno.

### Elementos

`ThreadItem` es la unión etiquetada presente en las respuestas de los turnos y en las notificaciones `item/*`. Los tipos de elementos comunes incluyen:

- `userMessage` - `{id, content}`, donde `content` es una lista de entradas del usuario (`text`, `image` o `localImage`).
- `functionCallOutput` - `{id, name, namespace, output}` para la salida de una herramienta que se proporciona de forma independiente a través de `turn/start.toolOutput`. `namespace` puede ser `null`.
- `agentMessage` - `{id, text, phase?}`, que contiene la respuesta acumulada del agente. Cuando está presente, `phase` usa los valores del protocolo de Responses API (`commentary`, `final_answer`).
- `plan` - `{id, text}`, que contiene el texto del plan propuesto en el modo plan. Considera definitivo el elemento `plan` final de `item/completed`.
- `reasoning` - `{id, summary, content}`, donde `summary` contiene los resúmenes de razonamiento transmitidos y `content`, los bloques de razonamiento sin procesar.
- `commandExecution` - `{id, command, cwd, status, commandActions, aggregatedOutput?, exitCode?, durationMs?}`.
- `fileChange` - `{id, changes, status}`, que describe las ediciones propuestas; `changes` contiene una lista de `{path, kind, diff}`.
- `mcpToolCall` - `{id, server, tool, status, arguments, appContext?, pluginId?, result?, error?}`. Para las apps MCP de confianza, `appContext` puede incluir `connectorId`, `linkId`, `resourceUri`, `appName`, `templateId` y el `actionName` estable del conector. Los elementos persistidos más antiguos pueden omitir los metadatos más recientes. Usa `appContext.resourceUri` en lugar del campo de nivel superior obsoleto `mcpAppResourceUri`.
- `dynamicToolCall` - `{id, tool, arguments, status, contentItems?, success?, durationMs?}` para invocaciones de herramientas dinámicas ejecutadas por el cliente.
- `collabToolCall` - `{id, tool, status, senderThreadId, receiverThreadId?, newThreadId?, prompt?, agentStatus?}`.
- `webSearch` - `{id, query, action?}` para solicitudes de búsqueda web que envía el agente.
- `imageView` - `{id, path}`, que se emite cuando el agente invoca la herramienta de visualización de imágenes.
- `enteredReviewMode` - `{id, review}`, que se envía cuando se inicia el revisor.
- `exitedReviewMode` - `{id, review}`, que se emite cuando el revisor finaliza.
- `contextCompaction` - `{id}`, que se emite cuando Codex compacta el historial de la conversación.

Para `webSearch.action`, el campo `type` de la acción puede ser `search` (`query?`, `queries?`), `openPage` (`url?`) o `findInPage` (`url?`, `pattern?`).

App Server marca como obsoleta la notificación heredada `thread/compacted`; usa en su lugar el elemento `contextCompaction`.

Todos los elementos emiten dos eventos compartidos del ciclo de vida:

- `item/started` - emite el `item` completo cuando comienza una nueva unidad de trabajo; el valor de `item.id` coincide con el `itemId` que usan los deltas.
- `item/completed` - envía el `item` final cuando termina el trabajo; considéralo el estado definitivo.

### Deltas de elementos

- `item/agentMessage/delta` - agrega el texto transmitido al mensaje del agente.
- `item/plan/delta` - transmite el texto del plan propuesto. Es posible que el elemento `plan` final no coincida exactamente con los deltas concatenados.
- `item/reasoning/summaryTextDelta` - transmite resúmenes legibles del razonamiento; `summaryIndex` aumenta cuando comienza una nueva sección del resumen.
- `item/reasoning/summaryPartAdded` - marca la separación entre las secciones del resumen de razonamiento.
- `item/reasoning/textDelta` - transmite el texto de razonamiento sin procesar (cuando el modelo lo admite).
- `item/commandExecution/outputDelta` - transmite stdout/stderr de un comando; agrega los deltas en orden.
- `item/fileChange/outputDelta` - notificación de compatibilidad obsoleta para la salida de texto heredada de `apply_patch`. Las versiones actuales de app-server ya no la emiten; usa los elementos `fileChange` y `turn/diff/updated` en su lugar.

## Errores

Si un turno falla, el servidor emite un evento `error` con `{ error: { message, codexErrorInfo?, additionalDetails? } }` y luego finaliza el turno con `status: "failed"`. Cuando está disponible un código de estado HTTP del servicio de origen, aparece en `codexErrorInfo.httpStatusCode`.

Entre los valores habituales de `codexErrorInfo` se incluyen:

- `ContextWindowExceeded`
- `UsageLimitExceeded`
- `HttpConnectionFailed` (errores 4xx/5xx del servicio de origen)
- `ResponseStreamConnectionFailed`
- `ResponseStreamDisconnected`
- `ResponseTooManyFailedAttempts`
- `BadRequest`, `Unauthorized`, `SandboxError`, `InternalServerError`, `Other`

Cuando está disponible un código de estado HTTP del servicio de origen, el servidor lo reenvía en `httpStatusCode` dentro de la variante correspondiente de `codexErrorInfo`.

## Aprobaciones

Según la configuración de Codex de cada usuario, la ejecución de comandos y los cambios en archivos pueden requerir aprobación. App-server envía al cliente una solicitud JSON-RPC iniciada por el servidor, y el cliente responde con una carga útil que contiene la decisión.

- Decisiones sobre la ejecución de comandos: `accept`, `acceptForSession`, `decline`, `cancel` o `{ "acceptWithExecpolicyAmendment": { "execpolicy_amendment": ["cmd", "..."] } }`.
- Decisiones sobre cambios en archivos: `accept`, `acceptForSession`, `decline`, `cancel`.

- Las solicitudes incluyen `threadId` y `turnId`; úsalos para asociar el estado de la interfaz de usuario con la conversación activa.
- El servidor reanuda o rechaza el trabajo y finaliza el elemento con `item/completed`.

### Aprobaciones para la ejecución de comandos

Orden de los mensajes:

1. `item/started` muestra el elemento `commandExecution` pendiente con `command`, `cwd` y otros campos.
2. `item/commandExecution/requestApproval` incluye `itemId`, `threadId`, `turnId` y los campos opcionales `reason`, `command`, `cwd`, `commandActions`, `proposedExecpolicyAmendment`, `networkApprovalContext` y `availableDecisions`. Cuando `initialize.params.capabilities.experimentalApi = true`, la carga útil también puede incluir el campo experimental `additionalPermissions`, que describe el acceso al sandbox solicitado para cada comando. Todas las rutas del sistema de archivos incluidas en `additionalPermissions` se transmiten como rutas absolutas.
3. El cliente responde con una de las decisiones de aprobación para la ejecución de comandos indicadas anteriormente.
4. `serverRequest/resolved` confirma que la solicitud pendiente se respondió o eliminó.
5. `item/completed` devuelve el elemento `commandExecution` final con `status: completed | failed | declined`.

Cuando `networkApprovalContext` está presente, el prompt solicita acceso administrado a la red (no una aprobación general de comandos de shell). El esquema v2 actual expone el `host` y el `protocol` de destino; los clientes deben mostrar un prompt específico para la red y no asumir que `command` contiene una vista previa de un comando de shell comprensible para el usuario.

Codex agrupa por destino (`host`, protocolo y puerto) los prompts simultáneos de aprobación de red. Por lo tanto, app-server puede enviar un solo prompt que desbloquee varias solicitudes en cola al mismo destino, mientras que los distintos puertos de un mismo host se tratan por separado.

### Aprobaciones de cambios en archivos

Orden de los mensajes:

1. `item/started` emite un elemento `fileChange` con los cambios propuestos en `changes` y con `status: "inProgress"`.
2. `item/fileChange/requestApproval` incluye `itemId`, `threadId`, `turnId` y los campos opcionales `reason` y `grantRoot`.
3. El cliente responde con una de las decisiones de aprobación de cambios en archivos indicadas anteriormente.
4. `serverRequest/resolved` confirma que la solicitud pendiente se respondió o eliminó.
5. `item/completed` devuelve el elemento `fileChange` final con `status: completed | failed | declined`.

### `tool/requestUserInput`

Cuando el cliente responde a `item/tool/requestUserInput`, app-server emite `serverRequest/resolved` con `{ threadId, requestId }`. Si la solicitud pendiente se elimina al iniciar, finalizar o interrumpir un turno antes de que el cliente responda, el servidor emite la misma notificación para indicar esa eliminación.

Los parámetros de la solicitud incluyen `autoResolutionMs` como un tiempo de espera en milisegundos expresado como un número entero, o
`null`. Cuando se especifica ese tiempo, los clientes host pueden resolver el prompt automáticamente después de ese
intervalo si el usuario no responde.

### Solicitudes de permisos

La herramienta integrada `request_permissions` envía
`item/permissions/requestApproval` con `threadId`, `turnId`, `itemId`,
`environmentId`, `cwd`, el campo opcional `reason` y los permisos de red o del sistema de archivos
solicitados. Responde con `permissions` que contenga solo el subconjunto concedido.
Configura `scope` como `"session"` para mantener la concesión en turnos posteriores de la misma
sesión; omítelo o usa `"turn"` para una concesión limitada al turno. Los permisos que
no se solicitaron se ignoran.

### Solicitudes de exploración de servidores MCP

Un servidor MCP puede interrumpir un turno con `mcpServer/elicitation/request`. La
solicitud incluye `threadId`, el campo opcional `turnId`, `serverName` y uno de
estos formatos de solicitud:

- `mode: "form"` o `mode: "openai/form"`, con `message` y
`requestedSchema`.
- `mode: "url"`, con `message`, `url` y `elicitationId`.

Responde con `action: "accept"` y el `content` solicitado, o con
`action: "decline"` o `"cancel"` y `content: null`. Luego, app-server emite
`serverRequest/resolved`. Para recibir la variante `openai/form`, habilítala mediante
`initialize.params.capabilities.mcpServerOpenaiFormElicitation`.

### Llamadas a herramientas dinámicas (experimental)

`dynamicTools` en `thread/start` y el flujo correspondiente de solicitudes o respuestas de `item/tool/call` son API experimentales.

Los nombres de las herramientas dinámicas y de los espacios de nombres deben cumplir las restricciones de nomenclatura de la Responses API.
Evita los nombres de espacios de nombres reservados que usan las herramientas integradas de Codex.

Cuando se invoca una herramienta dinámica durante un turno, app-server emite:

1. `item/started` con `item.type = "dynamicToolCall"` y `status = "inProgress"`, además de `tool` y `arguments`.
2. `item/tool/call` como una solicitud del servidor al cliente.
3. La carga útil de la respuesta del cliente con los elementos de contenido devueltos.
4. `item/completed` con `item.type = "dynamicToolCall"`, el `status` final y cualquier valor devuelto en `contentItems` o `success`.

### Aprobaciones de llamadas a herramientas MCP (apps)

Las llamadas a herramientas de una App (conector) también pueden requerir aprobación. Cuando una llamada a una herramienta de una app tiene efectos secundarios, el servidor puede solicitar aprobación mediante `tool/requestUserInput` con opciones como **Aceptar**, **Rechazar** y **Cancelar**. Las anotaciones que indican que una herramienta es destructiva siempre activan una solicitud de aprobación, incluso cuando la herramienta también presenta indicadores de privilegios más limitados. Si el usuario rechaza o cancela la solicitud, el elemento `mcpToolCall` relacionado finaliza con un error en lugar de ejecutar la herramienta.

## Habilidades

Para invocar una habilidad, incluye `$<skill-name>` en la entrada de texto del usuario. Agrega un elemento de entrada de tipo `skill` (recomendado) para que el servidor incorpore las instrucciones completas de la habilidad en lugar de depender de que el modelo resuelva el nombre.

```json
{
  "method": "turn/start",
  "id": 101,
  "params": {
    "threadId": "thread-1",
    "input": [
      {
        "type": "text",
        "text": "$skill-creator Add a new skill for triaging flaky CI."
      },
      {
        "type": "skill",
        "name": "skill-creator",
        "path": "/Users/me/.codex/skills/skill-creator/SKILL.md"
      }
    ]
  }
}

Si omites el elemento `skill`, el modelo analizará de todos modos el marcador `$<skill-name>` e intentará localizar la habilidad, lo que puede aumentar la latencia.

Ejemplo:

$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage.

Usa `skills/list` para obtener las habilidades disponibles (opcionalmente con alcance limitado por `cwds` y con `forceReload`). También puedes incluir `perCwdExtraUserRoots` para examinar rutas absolutas adicionales con alcance `user` para valores específicos de `cwd`. App-server ignora las entradas cuyo `cwd` no está presente en `cwds`. `skills/list` puede reutilizar un resultado almacenado en caché para cada `cwd`; configura `forceReload: true` para actualizarlo desde el disco. Cuando están presentes, el servidor lee `interface` y `dependencies` de `SKILL.json`.

```json
{ "method": "skills/list", "id": 25, "params": {
  "cwds": ["/Users/me/project", "/Users/me/other-project"],
  "forceReload": true,
  "perCwdExtraUserRoots": [
    {
      "cwd": "/Users/me/project",
      "extraUserRoots": ["/Users/me/shared-skills"]
    }
  ]
} }
{ "id": 25, "result": {
  "data": [{
    "cwd": "/Users/me/project",
    "skills": [
      {
        "name": "skill-creator",
        "description": "Create or update a Codex skill",
        "enabled": true,
        "interface": {
          "displayName": "Skill Creator",
          "shortDescription": "Create or update a Codex skill"
        },
        "dependencies": {
          "tools": [
            {
              "type": "env_var",
              "value": "GITHUB_TOKEN",
              "description": "GitHub API token"
            },
            {
              "type": "mcp",
              "value": "github",
              "transport": "streamable_http",
              "url": "https://example.com/mcp"
            }
          ]
        }
      }
    ],
    "errors": []
  }]
} }

El servidor también emite notificaciones `skills/changed` cuando cambian los archivos de habilidades locales que monitorea. Trátalas como una señal de invalidación y vuelve a ejecutar `skills/list` con los parámetros actuales cuando sea necesario.

Para habilitar o deshabilitar una habilidad según su ruta:

```json
{
  "method": "skills/config/write",
  "id": 26,
  "params": {
    "path": "/Users/me/.codex/skills/skill-creator/SKILL.md",
    "enabled": false
  }
}

## Apps (conectores)

Usa `app/installed` para leer la instantánea confirmada más reciente del estado del entorno de ejecución de las apps instaladas.
Cada resultado incluye el `id` de la app, `runtimeName` (o `null`), el estado efectivo de
`enabled` y el estado de `callable`. Una app solo puede invocarse cuando la configuración efectiva
la habilita y al menos una herramienta visible para el modelo cumple las políticas de
la app y de la herramienta.

```json
{
  "method": "app/installed",
  "id": 49,
  "params": {
    "threadId": "thread-1",
    "forceRefresh": false
  }
}
{
  "id": 49,
  "result": {
    "apps": [
      {
        "id": "demo-app",
        "runtimeName": "Demo App",
        "enabled": true,
        "callable": true
      }
    ]
  }
}

Omite `threadId` para usar la configuración global en lugar de la de un hilo
cargado. Configura `forceRefresh: true` para actualizar la instantánea del entorno de ejecución
del conector antes de leerla. Cuando una política global o del espacio de trabajo bloquea el acceso a las apps,
una app detectada puede seguir apareciendo con `enabled` y `callable` configurados como `false`.

Usa `app/list` para obtener las apps disponibles. En la CLI/TUI, `/apps` es el selector para el usuario; en clientes personalizados, llama directamente a `app/list`. Cada entrada incluye `isAccessible` (disponible para el usuario) y `isEnabled` (habilitada en `config.toml`) para que los clientes puedan distinguir entre la instalación o el acceso y el estado de habilitación local. Las entradas de apps también pueden incluir los campos opcionales `branding`, `appMetadata` y `labels`.

```json
{ "method": "app/list", "id": 50, "params": {
  "cursor": null,
  "limit": 50,
  "threadId": "thread-1",
  "forceRefetch": false
} }
{ "id": 50, "result": {
  "data": [
    {
      "id": "demo-app",
      "name": "Demo App",
      "description": "Example connector for documentation.",
      "logoUrl": "https://example.com/demo-app.png",
      "logoUrlDark": null,
      "distributionChannel": null,
      "branding": null,
      "appMetadata": null,
      "labels": null,
      "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",
      "isAccessible": true,
      "isEnabled": true
    }
  ],
  "nextCursor": null
} }

Si proporcionas `threadId`, la habilitación de funciones de las apps (`features.apps`) usa la instantánea de configuración de ese hilo. Si lo omites, app-server usa la configuración global más reciente.

`app/list` responde una vez que terminan de cargarse tanto las apps accesibles como las apps del directorio. Configura `forceRefetch: true` para omitir las cachés de apps y obtener datos actualizados. Las entradas de caché solo se reemplazan cuando las actualizaciones se completan correctamente.

El servidor también emite notificaciones `app/list/updated` cada vez que termina de cargarse alguna de las dos fuentes (apps accesibles o apps del directorio). Cada notificación incluye la lista combinada más reciente de apps.

```json
{
  "method": "app/list/updated",
  "params": {
    "data": [
      {
        "id": "demo-app",
        "name": "Demo App",
        "description": "Example connector for documentation.",
        "logoUrl": "https://example.com/demo-app.png",
        "logoUrlDark": null,
        "distributionChannel": null,
        "branding": null,
        "appMetadata": null,
        "labels": null,
        "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",
        "isAccessible": true,
        "isEnabled": true
      }
    ]
  }
}

Usa `app/read` cuando ya conozcas los identificadores de las apps y necesites sus metadatos en vez
del estado del entorno de ejecución de las apps instaladas. Proporciona como máximo 100 `appIds`. El servidor conserva solo
la primera aparición de cada identificador repetido y mantiene ese orden tanto en
`apps` como en `missingAppIds`. Las apps desconocidas o inaccesibles se devuelven en
`missingAppIds` sin que falle toda la solicitud.

```json
{
  "method": "app/read",
  "id": 52,
  "params": {
    "appIds": ["demo-app", "missing-app"],
    "includeTools": true
  }
}
{
  "id": 52,
  "result": {
    "apps": [
      {
        "id": "demo-app",
        "name": "Demo App",
        "description": "Example connector for documentation.",
        "iconUrl": null,
        "iconUrlDark": null,
        "distributionChannel": null,
        "installUrl": null,
        "pluginDisplayNames": [],
        "toolSummaries": [
          {
            "name": "search",
            "title": "Search",
            "description": "Search the app.",
            "isEnabled": true,
            "disabledReason": null,
            "isReadOnly": true
          }
        ]
      }
    ],
    "missingAppIds": ["missing-app"]
  }
}

Establece `includeTools: true` para solicitar resúmenes públicos de herramientas solo para visualización. La
respuesta de metadatos no incluye el estado de ejecución de las apps instaladas ni autoriza una
llamada a herramientas; usa `app/installed` para comprobar el estado efectivo
de `enabled` y `callable`.

Invoca una app insertando `$<app-slug>` en la entrada de texto y agregando un elemento de entrada `mention` con la ruta `app://<id>` (recomendado).

```json
{
  "method": "turn/start",
  "id": 51,
  "params": {
    "threadId": "thread-1",
    "input": [
      {
        "type": "text",
        "text": "$demo-app Pull the latest updates from the team."
      },
      {
        "type": "mention",
        "name": "Demo App",
        "path": "app://demo-app"
      }
    ]
  }
}

### Ejemplos de RPC de configuración para los ajustes de las apps

Usa `config/read`, `config/value/write` y `config/batchWrite` para consultar o actualizar los controles de las apps en `config.toml`.

Consulta la estructura efectiva de la configuración de las apps (incluidos `_default` y los valores de reemplazo específicos de cada herramienta):

```json
{ "method": "config/read", "id": 60, "params": { "includeLayers": false } }
{ "id": 60, "result": {
  "config": {
    "apps": {
      "_default": {
        "enabled": true,
        "destructive_enabled": true,
        "open_world_enabled": true,
        "approvals_reviewer": "user",
        "default_tools_approval_mode": "auto"
      },
      "google_drive": {
        "enabled": true,
        "destructive_enabled": false,
        "approvals_reviewer": "auto_review",
        "default_tools_approval_mode": "prompt",
        "tools": {
          "files/delete": { "enabled": false, "approval_mode": "approve" }
        }
      }
    }
  }
} }

`apps._default.approvals_reviewer` establece el revisor para todas las apps, a menos que un
valor específico de una app lo reemplace. Si se omiten ambos, la app hereda el
valor de `approvals_reviewer` del nivel superior. `apps._default.default_tools_approval_mode`
establece el modo de aprobación de respaldo para las herramientas sin un valor de reemplazo
por app o por herramienta. Los requisitos administrados del modo de aprobación prevalecen
sobre la configuración del modo de aprobación de las herramientas.

Actualiza una sola opción de configuración de la app:

```json
{
  "method": "config/value/write",
  "id": 61,
  "params": {
    "keyPath": "apps.google_drive.default_tools_approval_mode",
    "value": "prompt",
    "mergeStrategy": "replace"
  }
}

Aplica varios cambios de configuración de las apps de forma atómica:

```json
{
  "method": "config/batchWrite",
  "id": 62,
  "params": {
    "edits": [
      {
        "keyPath": "apps._default.destructive_enabled",
        "value": false,
        "mergeStrategy": "upsert"
      },
      {
        "keyPath": "apps.google_drive.tools.files/delete.approval_mode",
        "value": "approve",
        "mergeStrategy": "upsert"
      }
    ]
  }
}

### Detectar e importar la configuración de agentes externos

Usa `externalAgentConfig/detect` para detectar artefactos de agentes externos que se puedan migrar y luego pasa las entradas seleccionadas a `externalAgentConfig/import`.

Ejemplo de detección:

```json
{ "method": "externalAgentConfig/detect", "id": 63, "params": {
  "includeHome": true,
  "cwds": ["/Users/me/project"]
} }
{ "id": 63, "result": {
  "items": [
    {
      "itemType": "AGENTS_MD",
      "description": "Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md.",
      "cwd": "/Users/me/project"
    },
    {
      "itemType": "SKILLS",
      "description": "Copy skill folders from /Users/me/.claude/skills to /Users/me/.agents/skills.",
      "cwd": null
    }
  ]
} }

Ejemplo de importación:

```json
{ "method": "externalAgentConfig/import", "id": 64, "params": {
  "migrationItems": [
    {
      "itemType": "AGENTS_MD",
      "description": "Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md.",
      "cwd": "/Users/me/project"
    }
  ],
  "source": "claude-code"
} }
{ "id": 64, "result": { "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868" } }

El parámetro de importación opcional `source` de nivel superior identifica el producto que
generó los elementos de migración seleccionados.

El servidor emite `externalAgentConfig/import/progress` a medida que se completa la importación de cada tipo de elemento,
y `externalAgentConfig/import/completed` cuando finalizan todas las importaciones síncronas
y en segundo plano. Estas notificaciones incluyen el mismo `importId` de la
respuesta y `itemTypeResults`, con `successes` y `failures` por tipo.
La notificación de finalización puede llegar inmediatamente después de la respuesta o cuando finalizan las importaciones remotas
en segundo plano.

```json
{ "method": "externalAgentConfig/import/progress", "params": {
  "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
  "itemTypeResults": [
    {
      "itemType": "AGENTS_MD",
      "successes": [
        { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
      ],
      "failures": []
    }
  ]
} }
{ "method": "externalAgentConfig/import/completed", "params": {
  "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
  "itemTypeResults": [
    {
      "itemType": "AGENTS_MD",
      "successes": [
        { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
      ],
      "failures": []
    }
  ]
} }

Consulta las importaciones completadas anteriormente:

```json
{ "method": "externalAgentConfig/import/readHistories", "id": 65 }
{ "id": 65, "result": { "data": [
  {
    "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
    "completedAtMs": 1781784000000,
    "successes": [
      { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
    ],
    "failures": []
  }
] } }

Los valores admitidos para `itemType` son `AGENTS_MD`, `CONFIG`, `SKILLS`, `PLUGINS`,
`MCP_SERVER_CONFIG`, `SUBAGENTS`, `HOOKS`, `COMMANDS` y `SESSIONS`. Para los
elementos `PLUGINS`, `details.plugins` enumera cada `marketplaceName` y los
`pluginNames` que Codex puede intentar migrar. La detección devuelve solo los elementos que aún
requieren trabajo. Por ejemplo, Codex omite la migración de AGENTS si `AGENTS.md`
ya existe y no está vacío, y las importaciones de habilidades no sobrescriben los
directorios de habilidades existentes.

Al detectar complementos en `.claude/settings.json`, Codex lee las fuentes de
Marketplace configuradas en `extraKnownMarketplaces`. Si `enabledPlugins` contiene
complementos de `claude-plugins-official`, pero falta la fuente de Marketplace,
Codex infiere que `anthropics/claude-plugins-official` es la fuente.

## Puntos de acceso de autenticación

La interfaz JSON-RPC de autenticación y cuenta expone métodos de solicitud y respuesta, además de notificaciones iniciadas por el servidor (sin `id`). Úsalos para determinar el estado de autenticación, iniciar o cancelar procesos de inicio de sesión, cerrar sesión, consultar los límites de solicitudes de ChatGPT y notificar a los propietarios de espacios de trabajo sobre créditos agotados o límites de uso.

### Modos de autenticación

Codex admite estos modos de autenticación. `account/updated.authMode` muestra el modo activo e incluye el valor actual de `planType` de ChatGPT cuando está disponible. `account/read` también informa los detalles de la cuenta y del plan.

- **Clave de API (`apikey`)** - el cliente proporciona una clave de API de OpenAI con `type: "apiKey"`, y Codex la almacena para las solicitudes a la API.
- **ChatGPT administrado (`chatgpt`)** - Codex gestiona el flujo OAuth de ChatGPT, almacena los tokens de forma persistente y los renueva automáticamente. Empieza con `type: "chatgpt"` para el flujo de navegador o con `type: "chatgptDeviceCode"` para el flujo de código de dispositivo.
- **Tokens externos de ChatGPT (`chatgptAuthTokens`)** - este modo es experimental y está destinado a apps host que ya gestionan el ciclo de vida de la autenticación del usuario en ChatGPT. La app host proporciona directamente un `accessToken`, un `chatgptAccountId` y un `chatgptPlanType` opcional, y debe renovar el token cuando se le solicite.
- **Amazon Bedrock** - `account/read` identifica las cuentas de Bedrock como `type: "amazonBedrock"` e indica si las credenciales provienen de una clave de API de Bedrock administrada por Codex (`credentialSource: "codexManaged"`) o de la cadena externa de credenciales de AWS (`credentialSource: "awsManaged"`). `account/updated.authMode` usa `bedrockApiKey` para las claves de API de Bedrock administradas por Codex.

### Descripción general de la API

- `account/read` - obtiene la información actual de la cuenta y, de forma opcional, renueva los tokens.
- `account/login/start` - inicia el proceso de inicio de sesión (`apiKey`, `chatgpt`, `chatgptDeviceCode` o el modo experimental `chatgptAuthTokens`).
- `account/login/completed` (notificación) - se emite cuando finaliza un intento de inicio de sesión (con éxito o con error).
- `account/login/cancel` - cancela un inicio de sesión pendiente de ChatGPT en modo administrado, identificado por `loginId`.
- `account/logout` - cierra la sesión; genera `account/updated`.
- `account/updated` (notificación) - se emite cada vez que cambia el modo de autenticación (`authMode`: `apikey`, `chatgpt`, `chatgptAuthTokens`, `agentIdentity`, `personalAccessToken`, `bedrockApiKey` o `null`) e incluye `planType` cuando está disponible.
- `account/chatgptAuthTokens/refresh` (solicitud del servidor) - solicita tokens renovados de ChatGPT administrados externamente tras un error de autorización.
- `account/rateLimits/read` - obtiene los límites de solicitudes de ChatGPT.
- `account/rateLimits/updated` (notificación) - se emite cada vez que cambian los límites de solicitudes de ChatGPT de un usuario.
- `account/sendAddCreditsNudgeEmail` - solicita a ChatGPT que envíe un correo electrónico a un propietario de un espacio de trabajo para informarle que se agotaron los créditos o se alcanzó un límite de uso.
- `account/rateLimitResetCredit/consume` - consume un restablecimiento obtenido del límite de solicitudes mediante un valor de `idempotencyKey` proporcionado por el cliente.
- `account/usage/read` - obtiene los resúmenes de actividad de tokens de la cuenta de ChatGPT y los datos agrupados por día.
- `account/workspaceMessages/read` - obtiene los mensajes activos del espacio de trabajo, incluidos los títulos de las notificaciones cuando están disponibles.
- `mcpServer/oauthLogin/completed` (notificación) - se emite después de que finaliza un flujo de `mcpServer/oauth/login`; la carga útil incluye `{ name, threadId, success, error? }`. `threadId` puede ser `null` en los flujos OAuth asociados a una app o a un complemento.
- `mcpServer/startupStatus/updated` (notificación) - se emite cuando cambia el estado de inicio de un servidor MCP configurado; la carga útil incluye `{ threadId, name, status, error, failureReason }`. `threadId` es `null` cuando el inicio corresponde a una app. Si el inicio falla, `failureReason: "reauthenticationRequired"` significa que las credenciales OAuth almacenadas caducaron y no se pudieron renovar, por lo que el cliente debería ofrecer la opción de volver a conectar el servidor.

### 1) Comprobar el estado de autenticación

Solicitud:

```json
{ "method": "account/read", "id": 1, "params": { "refreshToken": false } }

Ejemplos de respuesta:

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": false } }

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": true } }

```json
{
  "id": 1,
  "result": { "account": { "type": "apiKey" }, "requiresOpenaiAuth": true }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "amazonBedrock",
      "credentialSource": "codexManaged"
    },
    "requiresOpenaiAuth": false
  }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "amazonBedrock",
      "credentialSource": "awsManaged"
    },
    "requiresOpenaiAuth": false
  }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "chatgpt",
      "email": "user@example.com",
      "planType": "pro"
    },
    "requiresOpenaiAuth": true
  }
}

Notas sobre los campos:

- `refreshToken` (booleano): establece el valor en `true` para forzar la renovación de un token en el modo administrado de ChatGPT. En el modo de tokens externos (`chatgptAuthTokens`), app-server ignora este indicador.
- `email` tiene el valor `null` cuando la cuenta de ChatGPT no tiene una dirección de correo electrónico.
- `requiresOpenaiAuth` refleja el proveedor activo; cuando es `false`, Codex puede ejecutarse sin credenciales de OpenAI.
- Amazon Bedrock informa `credentialSource: "codexManaged"` cuando usa una
  clave de API de Bedrock administrada por Codex. Informa `credentialSource: "awsManaged"`
  para la vía externa de credenciales de AWS. Esto identifica la fuente de credenciales
  seleccionada; no verifica que la cadena de credenciales de AWS pueda obtener
  credenciales.

### 2) Iniciar sesión con una clave de API

1. Envía:

   ```json
   {
     "method": "account/login/start",
     "id": 2,
     "params": { "type": "apiKey", "apiKey": "sk-..." }
   }

2. Resultado esperado:

   ```json
   { "id": 2, "result": { "type": "apiKey" } }

3. Notificaciones:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "apikey", "planType": null }
   }

### 3) Iniciar sesión con ChatGPT (flujo de navegador)

1. Inicia:

   ```json
   {
     "method": "account/login/start",
     "id": 3,
     "params": {
       "type": "chatgpt",
       "useHostedLoginSuccessPage": true,
       "appBrand": "chatgpt"
     }
   }

   De forma predeterminada, una devolución de llamada exitosa del navegador redirige a una página local de confirmación.
   Establece `useHostedLoginSuccessPage: true` para usar la página de confirmación alojada cuando
   no sea necesario configurar la organización. Con la página de confirmación alojada habilitada, `appBrand`
   puede ser `"codex"` o `"chatgpt"`; si se omite o su valor es `null`, se usa
`"codex"` de forma predeterminada.

   ```json
   {
     "id": 3,
     "result": {
       "type": "chatgpt",
       "loginId": "<uuid>",
       "authUrl": "https://chatgpt.com/...&redirect_uri=http%3A%2F%2Flocalhost%3A<port>%2Fauth%2Fcallback"
     }
   }

2. Abre `authUrl` en un navegador; app-server aloja la devolución de llamada local.
3. Espera las notificaciones:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": "<uuid>", "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgpt", "planType": "plus" }
   }

### 3b) Iniciar sesión con ChatGPT (flujo de código de dispositivo)

Usa este flujo cuando tu cliente gestione el proceso de inicio de sesión o cuando una devolución de llamada del navegador sea poco confiable.

1. Inicia:

   ```json
   {
     "method": "account/login/start",
     "id": 4,
     "params": { "type": "chatgptDeviceCode" }
   }

   ```json
   {
     "id": 4,
     "result": {
       "type": "chatgptDeviceCode",
       "loginId": "<uuid>",
       "verificationUrl": "https://auth.openai.com/codex/device",
       "userCode": "ABCD-1234"
     }
   }

2. Muestra `verificationUrl` y `userCode` al usuario; el frontend controla la experiencia de usuario.
3. Espera las notificaciones:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": "<uuid>", "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgpt", "planType": "plus" }
   }

### 3c) Iniciar sesión con tokens de ChatGPT administrados externamente (`chatgptAuthTokens`)

Usa este modo experimental solo cuando una aplicación host gestione el ciclo de autenticación del usuario en ChatGPT y proporcione los tokens directamente. Los clientes deben establecer `capabilities.experimentalApi = true` durante `initialize` antes de usar este tipo de inicio de sesión.

1. Envía:

   ```json
   {
     "method": "account/login/start",
     "id": 7,
     "params": {
       "type": "chatgptAuthTokens",
       "accessToken": "<jwt>",
       "chatgptAccountId": "org-123",
       "chatgptPlanType": "business"
     }
   }

2. Respuesta esperada:

   ```json
   { "id": 7, "result": { "type": "chatgptAuthTokens" } }

3. Notificaciones:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgptAuthTokens", "planType": "business" }
   }

Cuando el servidor recibe un `401 Unauthorized`, puede solicitar tokens renovados a la aplicación host:

```json
{
  "method": "account/chatgptAuthTokens/refresh",
  "id": 8,
  "params": { "reason": "unauthorized", "previousAccountId": "org-123" }
}
{ "id": 8, "result": { "accessToken": "<jwt>", "chatgptAccountId": "org-123", "chatgptPlanType": "business" } }

El servidor vuelve a intentar la solicitud original después de recibir una respuesta de renovación exitosa. El tiempo de espera de las solicitudes se agota después de unos 10 segundos.

### 4) Cancelar un inicio de sesión en ChatGPT

```json
{ "method": "account/login/cancel", "id": 4, "params": { "loginId": "<uuid>" } }
{ "method": "account/login/completed", "params": { "loginId": "<uuid>", "success": false, "error": "..." } }

### 5) Cerrar sesión

```json
{ "method": "account/logout", "id": 5 }
{ "id": 5, "result": {} }
{ "method": "account/updated", "params": { "authMode": null, "planType": null } }

### 6) Límites de solicitudes (ChatGPT)

```json
{ "method": "account/rateLimits/read", "id": 6 }
{ "id": 6, "result": {
  "rateLimits": {
    "limitId": "codex",
    "limitName": null,
    "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
    "secondary": null,
    "rateLimitReachedType": null
  },
  "rateLimitsByLimitId": {
    "codex": {
      "limitId": "codex",
      "limitName": null,
      "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
      "secondary": null,
      "rateLimitReachedType": null
    },
    "codex_other": {
      "limitId": "codex_other",
      "limitName": "codex_other",
      "primary": { "usedPercent": 42, "windowDurationMins": 60, "resetsAt": 1730950800 },
      "secondary": null,
      "rateLimitReachedType": null
    }
  },
  "rateLimitResetCredits": {
    "availableCount": 2,
    "credits": [{
      "id": "RateLimitResetCredit_1",
      "resetType": "codexRateLimits",
      "status": "available",
      "grantedAt": 1781654400,
      "expiresAt": 1784246400,
      "title": "Rate-limit reset",
      "description": "Reset an eligible Codex rate-limit window."
    }]
  }
} }
{ "method": "account/rateLimits/updated", "params": {
  "rateLimits": {
    "limitId": "codex",
    "primary": { "usedPercent": 31, "windowDurationMins": 15, "resetsAt": 1730948100 }
  }
} }

Notas sobre los campos:

- `rateLimits` es la vista de un solo bucket compatible con versiones anteriores.
- `rateLimitsByLimitId` (cuando está presente) es la vista de varios buckets, indexada por el `limit_id` sujeto a medición (por ejemplo, `codex`).
- `limitId` es el identificador del bucket sujeto a medición.
- `limitName` es una etiqueta opcional del bucket visible para el usuario.
- `usedPercent` es el uso actual dentro del intervalo de cuota.
- `windowDurationMins` es la duración del intervalo de cuota.
- `resetsAt` es una marca de tiempo Unix (en segundos) para el próximo restablecimiento.
- `planType` se incluye cuando el servidor devuelve el plan de ChatGPT asociado a un bucket.
- `credits` se incluye cuando el servidor devuelve los detalles de los créditos restantes del espacio de trabajo.
- `rateLimitReachedType` identifica el estado del límite según la clasificación del servidor cuando se alcanza un límite.
- `rateLimitResetCredits` contiene la cantidad de restablecimientos ganados disponibles cuando el servicio la proporciona; de lo contrario, su valor es `null`.
- `rateLimitResetCredits.credits` es `null` cuando solo se conoce la cantidad. Un arreglo vacío significa que el servicio consultó los detalles y no devolvió ningún crédito disponible. El servicio puede limitar la cantidad de filas de detalles, por lo que `availableCount` es el valor de referencia.
- Cada fila de detalles incluye un `id` opaco, `resetType`, `status`, `grantedAt`, `expiresAt` (que puede ser `null`), `title` (que puede ser `null`) y `description` (que puede ser `null`).
- Consulta `account/rateLimits/read` después de consumir un restablecimiento.

### 7) Uso de tokens (ChatGPT)

Usa `account/usage/read` para obtener los campos de resumen de la actividad de tokens de ChatGPT y
los buckets diarios opcionales.

```json
{ "method": "account/usage/read", "id": 7 }
{ "id": 7, "result": {
  "summary": {
    "lifetimeTokens": 1234567,
    "peakDailyTokens": 45678,
    "longestRunningTurnSec": 540,
    "currentStreakDays": 8,
    "longestStreakDays": 14
  },
  "dailyUsageBuckets": [
    { "startDate": "2026-06-18", "tokens": 12345 }
  ]
} }

Notas sobre los campos:

- Los valores de `summary` pueden ser `null` cuando el servicio no haya devuelto esa métrica.
- `dailyUsageBuckets` puede ser `null`; cuando está presente, cada bucket incluye `startDate` y `tokens`.
- El punto de acceso requiere autenticación respaldada por los servicios de Codex. Se admite la autenticación con ChatGPT,
tokens externos de ChatGPT, identidad de agente y tokens de acceso personal;
no se admite la autenticación solo con clave de API ni con Bedrock.

### 8) Restablecimientos ganados para los límites de solicitudes (ChatGPT)

Usa `account/rateLimitResetCredit/consume` para consumir un restablecimiento ganado.

```json
{ "method": "account/rateLimitResetCredit/consume", "id": 8, "params": { "idempotencyKey": "8ae96ff3-3425-4f4c-8772-b6fd61502868", "creditId": "RateLimitResetCredit_1" } }
{ "id": 8, "result": { "outcome": "reset" } }

Notas sobre los campos:

- El valor de `idempotencyKey` no debe estar vacío. Usa un UUID para cada intento lógico de canje y reutiliza el mismo valor al reintentar esa operación.
- `creditId` es opcional. Si se proporciona, debe ser un ID opaco no vacío obtenido de `account/rateLimits/read`. Si se omite, el servicio selecciona el siguiente crédito disponible.
- `reset` indica que se consumió un crédito.
- `alreadyRedeemed` indica que el mismo canje ya se había completado. Trátalo como una operación idempotente exitosa y actualiza los límites de la cuenta.
- `nothingToReset` indica que no hay ningún intervalo del límite de solicitudes que cumpla los requisitos para restablecerse.
- `noCredit` indica que la cuenta no tiene créditos de restablecimiento ganados disponibles.
- Consulta `account/rateLimits/read` después de consumir un restablecimiento, en vez de deducir los intervalos actualizados a partir de esta respuesta.

### 9) Notificar al propietario de un espacio de trabajo sobre un límite

Usa `account/sendAddCreditsNudgeEmail` para pedirle a ChatGPT que envíe un correo electrónico al propietario de un espacio de trabajo cuando se agoten los créditos o se alcance un límite de uso.

```json
{ "method": "account/sendAddCreditsNudgeEmail", "id": 9, "params": { "creditType": "credits" } }
{ "id": 9, "result": { "status": "sent" } }

Usa `creditType: "credits"` cuando se agoten los créditos del espacio de trabajo, o `creditType: "usage_limit"` cuando se alcance el límite de uso del espacio de trabajo. Si ya se notificó al propietario recientemente, el estado de la respuesta es `cooldown_active`.

### 10) Mensajes del espacio de trabajo (ChatGPT)

Usa `account/workspaceMessages/read` para obtener los mensajes activos del espacio de trabajo
actual, incluidos los títulos de las notificaciones cuando estén disponibles.

```json
{ "method": "account/workspaceMessages/read", "id": 10 }
{ "id": 10, "result": { "featureEnabled": true, "messages": [
  { "messageId": "msg_123", "messageType": "headline", "messageBody": "Workspace maintenance starts at 5pm.", "createdAt": 1781395200, "archivedAt": null }
] } }

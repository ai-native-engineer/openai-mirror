<!-- source: https://learn.chatgpt.com/es-419/docs/security/sdk -->

Usa el SDK de TypeScript de Codex Security para ejecutar análisis de seguridad en repositorios y
cambios en el código desde tu aplicación o herramienta para desarrolladores. El SDK devuelve hallazgos
tipados, detalles de cobertura y rutas de los artefactos del análisis. Para análisis más prolongados,
admite comprobaciones previas, límites de costos, callbacks de progreso y cancelación.

El SDK usa módulos ECMAScript (ESM) y se ejecuta del lado del servidor con Node.js 22
(22.13.0 o una versión posterior), 24 o 26. Los análisis también requieren Python 3.10 o una versión posterior.
Python 3.10 también requiere el paquete `tomli`.

  El SDK de Codex Security está [disponible públicamente en
  GitHub](https://github.com/openai/codex-security). Para ejecutar análisis, se requiere
  acceso a Codex Security. Para agentes de programación de uso general, consulta la [guía del SDK de
  Codex](/es-419/codex/codex-sdk). Para flujos de trabajo de terminal y CI, consulta el [inicio rápido de la CLI de
  Codex Security](/es-419/codex/security/cli).

## Configurar el SDK

Instala el SDK:

```bash
npm install @openai/codex-security

Antes de iniciar un análisis, define `OPENAI_API_KEY` o `CODEX_API_KEY`, usa un
inicio de sesión existente de Codex almacenado en un archivo o [configura otro
proveedor](#configure-the-runtime-and-credentials). Amazon Bedrock usa credenciales de
AWS; OpenRouter y Fireworks usan claves de API y
configuración específicas de cada proveedor.

Para obtener los mejores resultados, usa una cuenta verificada para [Trusted Access for
Cyber](https://chatgpt.com/cyber). Iniciar sesión o proporcionar una clave de API no
otorga Trusted Access.

## Ejecutar un análisis

Analiza solo repositorios en los que confíes y que tengas permiso para evaluar. El SDK se ejecuta
con los permisos de tu sistema operativo local y nunca se detiene para solicitar aprobación.
Los procesos de análisis pueden heredar tu entorno, así que elimina las credenciales no relacionadas
antes de comenzar. Consulta [Permisos de análisis
locales](/es-419/codex/security/cli/reference#local-scan-permissions).

Crea un único cliente `CodexSecurity`, ejecuta un análisis estándar del repositorio y cierra
el cliente cuando termine el trabajo. Pasa `outputDir` para elegir un directorio privado
de resultados fuera del worktree de Git que contiene el repositorio.

Si omites `outputDir`, Codex Security guarda los resultados en su propio directorio
de estado persistente. Los resultados pueden incluir fragmentos del código fuente y detalles de
vulnerabilidades, así que elige permisos y políticas de retención adecuados.

```ts

const security = new CodexSecurity();

try {
  const result = await security.run("/path/to/repository", {
    outputDir: "/path/outside/repository/results",
  });

  console.log(result.reportPath);
  console.log(result.coverage.completeness);
  console.log(result.findings.findings.length);
} finally {
  await security.close();
}

`run` inicia el análisis, espera a que termine, valida los artefactos sellados
y devuelve un `ScanResult`. `close` libera el entorno de ejecución aislado y admite
llamadas repetidas.

## Comprobar las entradas con preflight

Usa `preflight` para comprobar un repositorio, un objetivo, un modo, los documentos de la base de conocimientos,
la ubicación de salida y la configuración de Codex antes de iniciar un análisis:

```ts
const plan = await security.preflight("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
  knowledgeBasePaths: ["/path/to/architecture.md"],
  outputDir: "/path/outside/repository/results",
});

console.log(plan.repository);
console.log(plan.target.kind);
console.log(plan.mode);
console.log(plan.outputDir);

Preflight no modifica el entorno de ejecución ni las credenciales de Codex. También deja
la detección del complemento y de Python para el análisis en sí. Esto hace que preflight resulte útil
para comprobar las entradas del usuario antes de una operación de larga duración o que requiera credenciales.

Para obtener una vista previa del archivado de un directorio de resultados existente, establece
`archiveExisting: true`:

```ts
const plan = await security.preflight("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
});

console.log(plan.archiveDir);

El valor `archiveDir` devuelto permite anticipar el nombre del directorio archivado. La ruta final puede
ser diferente porque `run` genera su propio destino único. Captura la ruta real
del directorio archivado con `onOutputArchived`:

```ts
await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
  onOutputArchived(archiveDir) {
    console.log("Archived results:", archiveDir);
  },
});

El análisis archiva los resultados anteriores y comienza con un directorio de salida
vacío.

## Elegir un objetivo de análisis

El SDK admite objetivos de repositorio, ruta, diff de commits y árbol de trabajo.
El objetivo predeterminado es el repositorio completo.

### Analizar rutas seleccionadas

Pasa un arreglo de rutas dentro del repositorio:

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
});

Las rutas pueden identificar archivos o directorios. El SDK resuelve cada ruta dentro del
repositorio y elimina los duplicados.

### Analizar cambios confirmados

Usa `DiffTarget.refs` para analizar los cambios confirmados entre dos revisiones de
Git disponibles localmente:

```ts

const target = DiffTarget.refs({
  base: "origin/main",
  head: "HEAD",
});

const result = await security.run("/path/to/repository", { target });

El valor predeterminado de head es `HEAD`. Los objetivos de diff requieren que el argumento del repositorio
sea la raíz del worktree de Git.

### Analizar el árbol de trabajo

Usa `DiffTarget.workingTree` para analizar los cambios preparados y sin preparar con respecto a una revisión
base:

```ts
const target = DiffTarget.workingTree({ base: "HEAD" });
const result = await security.run("/path/to/repository", { target });

El valor predeterminado de la base es `HEAD`. Recupera las revisiones seleccionadas antes de iniciar un
análisis de diff o del árbol de trabajo.

### Seleccionar el modo profundo

Establece `mode: "deep"` para un análisis de repositorio o ruta que requiera una revisión más amplia:

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing"],
  mode: "deep",
  workers: 2,
  subagents: 0,
  stopAfterNoNew: 3,
  maxDiscoveryRuns: 10,
  maxTimeHours: 1.5,
});

El modo profundo admite objetivos de repositorio y ruta. Usa el modo estándar para los análisis de diff y
del árbol de trabajo. La configuración opcional controla los workers independientes y simultáneos de análisis
estándar, los subagentes por worker, los análisis consecutivos completados por los workers
sin nuevos hallazgos y la cantidad total y la duración de sus ejecuciones. Estos parámetros
requieren `mode: "deep"`.

El valor predeterminado de `maxTimeHours` es `96` y acepta un número positivo de hasta `96`,
incluidas las fracciones de hora. Cuando se cumple el plazo, Codex Security detiene los workers
que no finalizaron, conserva los resultados de los análisis completados y los integra en el informe
final. Revisa `result.coverage.completeness` antes de considerar un análisis con límite de tiempo
como evidencia de una cobertura completa.

### Agregar una base de conocimientos de seguridad

Pasa documentos de arquitectura, modelos de amenazas o políticas de seguridad mediante
`knowledgeBasePaths`:

```ts
const result = await security.run("/path/to/repository", {
  knowledgeBasePaths: [
    "/path/to/architecture.md",
    "/path/to/security-policies",
  ],
});

El SDK acepta archivos o directorios y realiza búsquedas recursivas en los directorios.
Los formatos de documento compatibles son `.md`, `.markdown`, `.txt`, `.pdf` y `.docx`.
El SDK rechaza las rutas de entrada enlazadas, omite las entradas enlazadas de los directorios y mantiene
el contenido extraído de los documentos fuera de los resultados guardados del análisis.

### Agregar instrucciones de análisis y seguimiento

Usa `scanPrompt` para orientar el análisis y `postScanPrompt` para solicitar un seguimiento:

```ts
const result = await security.run("/path/to/repository", {
  scanPrompt: "Focus on tenant isolation and authorization checks.",
  postScanPrompt: "Write confirmed findings to post-scan-summary.md.",
});

Si el seguimiento falla, el SDK conserva el análisis completado e informa el
error mediante `onWarning`. Restaura todos los artefactos del análisis completado que el
seguimiento haya modificado.

### Establecer un presupuesto para el análisis

Establece `maxCostUsd` para detener un análisis cuando el costo estimado del modelo supere un límite.
Usa `onCost` para hacer un seguimiento del costo mientras se ejecuta el análisis:

```ts
const result = await security.run("/path/to/repository", {
  maxCostUsd: 5,
  onCost(cost) {
    console.log(cost.estimatedUsd);
  },
});

console.log(result.cost?.estimatedUsd);

El límite estima el gasto, pero no establece un tope estricto, por lo que las solicitudes ya
en curso pueden finalizar con un costo ligeramente superior. Si un análisis profundo alcanza el límite después de que
Codex Security integra los resultados completados por los workers, `run` devuelve un resultado
con `coverage.completeness` establecido en `"partial"` y notifica la advertencia de presupuesto
mediante `onWarning`.

Si el análisis no puede generar un resultado parcial finalizado, `run` lanza
`ScanCostLimitExceededError` y conserva cualquier salida disponible.

## Trabajar con los resultados del análisis

`ScanResult` expone los documentos estructurados, los metadatos del análisis y
las rutas de los artefactos:

| Propiedad             | Contenido                                                                           |
| -------------------- | ---------------------------------------------------------------------------------- |
| `manifest`           | El archivo de manifiesto sellado del análisis, que incluye el objetivo, el alcance, el productor y los registros de artefactos. |
| `findings`           | Hallazgos del análisis actual. Lee los objetos de hallazgo de `findings.findings`.     |
| `repositoryFindings` | Hallazgos abiertos en los análisis del repositorio, cuando hay un historial de análisis disponible.             |
| `coverage`           | Superficies revisadas, exclusiones, trabajo aplazado, preguntas abiertas y grado de completitud.    |
| `scanDir`            | El directorio del análisis.                                                                |
| `threadId`           | El identificador del hilo de Codex correspondiente al análisis.                                          |
| `turnResult`         | El estado y la respuesta del turno, y los metadatos de uso disponibles.                               |
| `cost`               | Costo estimado del modelo y de los tokens, o `null` si no está disponible.                        |
| `reportPath`         | La ruta de acceso a `report.md`.                                                           |
| `manifestPath`       | La ruta de acceso a `scan-manifest.json`.                                                  |
| `findingsPath`       | La ruta de acceso a `findings.json`.                                                       |
| `coveragePath`       | La ruta de acceso a `coverage.json`.                                                       |
| `artifactsDir`       | El directorio de artefactos de apoyo.                                                |
| `sarifPath`          | La ruta SARIF generada, o `null` si no hay SARIF.                          |
| `pluginVersion`      | La versión registrada por el productor del análisis.                                         |

Para exigir el mismo complemento en un análisis posterior, pasa
`expectedPluginVersion: result.pluginVersion`. El SDK rechaza el análisis si
la versión instalada del complemento es diferente.

Usa directamente los hallazgos estructurados y la cobertura:

```ts
for (const finding of result.findings.findings) {
  const location = finding.locations[0];
  if (location === undefined) continue;

  console.log(
    finding.severity.level,
    `${location.path}:${location.startLine}`,
    finding.title
  );
}

for (const deferred of result.coverage.deferred) {
  console.log(deferred.id, deferred.reason);
}

Los hallazgos pueden incluir los campos opcionales `codeEvidence`, `rootCause`, `validation`,
`attackPath`, `remediationTests` y `preventiveControls`.

Para los hallazgos de todo el repositorio, `confirmedInLatestScan` distingue los hallazgos
detectados en el análisis más reciente de los hallazgos anteriores que siguen abiertos:

```ts
for (const finding of result.repositoryFindings ?? []) {
  console.log(finding.title, finding.confirmedInLatestScan);
}

El grado de integridad de la cobertura es `complete`, `partial` o `unknown`. Revisa las superficies
pospuestas, las exclusiones y las preguntas abiertas antes de usar un análisis como evidencia para una
decisión de seguridad.

`result.toJSON()` devuelve el archivo de manifiesto, los hallazgos del repositorio y del análisis actual,
la cobertura, los identificadores del análisis y del hilo, `reportPath`, `artifactsDir`,
`sarifPath`, el costo y los metadatos del turno en un único objeto listo para JSON.

## Supervisar o cancelar un análisis

Pasa funciones de devolución de llamada de `ScanOptions` para informar sobre el inicio del análisis, el progreso de los workers y
los reintentos de conexión:

```ts
const result = await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  onScanStarted() {
    console.log("Scan started");
  },
  onProgress(progress) {
    console.log(progress.phase, progress.filesCompleted, progress.filesTotal);
  },
  onWorkerStatus(status) {
    console.log(status.kind, status);
  },
  onSessionEvent(session) {
    console.log(session.threadId, session.worker, session.event["type"]);
  },
  onReconnect(attempt, maxAttempts) {
    console.log(`Reconnect attempt ${attempt} of ${maxAttempts}`);
  },
  onObserverError(observer, error) {
    console.error(`${observer} failed`, error);
  },
});

console.log(result.reportPath);

Pasa un `AbortSignal` cuando la cancelación provenga de una solicitud, un controlador de tareas
o un tiempo de espera:

```ts

const controller = new AbortController();

try {
  const scan = security.run("/path/to/repository", {
    outputDir: "/path/outside/repository/results",
    signal: controller.signal,
  });

  controller.abort();
  await scan;
} catch (error) {
  if (error instanceof ScanInterruptedError) {
    console.error(error.scanDir);
  } else {
    throw error;
  }
}

Un análisis interrumpido puede dejar datos de salida parciales en `scanDir`. Conserva ese
directorio cuando sea necesario investigar el resultado.

Las aplicaciones que muestran el progreso de la configuración del análisis también pueden usar las funciones de devolución de llamada de `ScanOptions`
relacionadas con el ciclo de vida:

| Función de devolución de llamada                            | Se invoca cuando                                          |
| ----------------------------------- | ---------------------------------------------------- |
| `onAuthentication(authentication)`  | El análisis selecciona su método de autenticación.          |
| `onOutputArchived(archiveDir)`      | Los resultados existentes se trasladan al directorio de archivado.      |
| `onOutputDirReady(scanDir)`         | El directorio privado del análisis está listo.                 |
| `onScanStarted()`                   | Se completa la configuración del análisis y comienza la ejecución.           |
| `onTrustedAccessStatus(status)`     | El estado de Trusted Access pasa a estar disponible.             |
| `onReconnect(attempt, maxAttempts)` | El SDK reintenta la conexión de un flujo de análisis desconectado.          |
| `onActivity(activity)`              | Se actualiza un comando, una herramienta, un paso de razonamiento o un mensaje. |
| `onProgress(progress)`              | Cambia la fase del análisis o la cantidad de archivos revisados.       |
| `onWorkerStatus(status)`            | Cambia el estado de la comprobación preliminar o del envío del worker.         |
| `onSessionEvent(session)`           | Una sesión de análisis o de un worker emite un evento.             |
| `onCost(cost)`                      | Hay disponible una estimación actualizada del costo del análisis.         |
| `onWarning(warning)`                | El análisis emite una advertencia.                          |
| `onObserverError(observer, error)`  | Otra función de devolución de llamada del ciclo de vida del análisis genera un error.     |

El estado de Trusted Access es `granted`, `not_granted` o `unknown`. Si no hay acceso o
su estado es desconocido, también se activa `onWarning`.

`onSessionEvent` recibe eventos cuyo contenido no se ha ocultado y que pueden contener código
fuente o credenciales. Fíltralos antes de enviarlos a registros compartidos u otros
servicios.

## Configurar el entorno de ejecución y las credenciales

Pasa la configuración del entorno de ejecución cuando necesites un complemento, un intérprete o una
configuración específica de Codex:

```ts
const security = new CodexSecurity({
  pluginPath: "/path/to/codex-security-plugin",
  pythonPath: "/path/to/python",
  codexOverrides: {
    model: "gpt-5.6-terra",
    model_reasoning_effort: "high",
  },
});

`pluginPath` acepta el directorio de un complemento o un archivo ZIP. `pythonPath` selecciona el
intérprete del complemento. `codexOverrides` combina los valores admitidos en la configuración aislada de
Codex. Los análisis usan `gpt-5.6-sol` con un esfuerzo de razonamiento muy alto
de forma predeterminada. Establece `model` y `model_reasoning_effort` en `codexOverrides` para usar
otro modelo u otro nivel de esfuerzo de razonamiento. Para usar [Amazon
Bedrock](/es-419/codex/security/cli/reference#use-amazon-bedrock), establece
`model_provider` y `model` en `codexOverrides`.

`codexOverrides` no puede restringir el acceso del análisis al sistema de archivos ni cambiar su
política de aprobación. Consulta [Permisos de análisis
locales](/es-419/codex/security/cli/reference#local-scan-permissions).

Para OpenRouter o Fireworks, proporciona también la clave de API correspondiente y una configuración
completa del proveedor en `codexOverrides`. Por ejemplo, establece
`OPENROUTER_API_KEY` y configura OpenRouter:

```ts
const security = new CodexSecurity({
  codexOverrides: {
    model: "anthropic/claude-sonnet-4.5",
    model_provider: "openrouter",
    model_providers: {
      openrouter: {
        name: "OpenRouter",
        base_url: "https://openrouter.ai/api/v1",
        env_key: "OPENROUTER_API_KEY",
        wire_api: "responses",
      },
    },
  },
});

Para Fireworks, cambia ambas claves `openrouter` por `fireworks`, establece `name` en
`Fireworks AI`, establece `env_key` en `FIREWORKS_API_KEY`, usa
`https://api.fireworks.ai/inference/v1` como `base_url` y selecciona un modelo
de Fireworks.

El cliente también expone los métodos de autenticación admitidos:

| Método                     | Propósito                                                     |
| -------------------------- | ----------------------------------------------------------- |
| `loginApiKey(apiKey)`      | Autenticar el entorno de ejecución aislado con una clave de API.          |
| `loginChatGPT()`           | Iniciar un flujo de inicio de sesión en el navegador y devolver un objeto de inicio de sesión.     |
| `loginChatGPTDeviceCode()` | Iniciar un flujo de inicio de sesión mediante un código de dispositivo y devolver un objeto de inicio de sesión. |
| `account()`                | Devolver el estado actual de autenticación.                    |
| `logout()`                 | Borrar la autenticación del entorno aislado.                              |

Un objeto de inicio de sesión proporciona `waitForInstructions`, `authUrl`, `verificationUrl`,
`userCode`, `wait` y `cancel` para que una aplicación pueda mostrar y completar el
flujo de inicio de sesión seleccionado. El SDK puede reutilizar un inicio de sesión de Codex almacenado en un archivo. Las claves de API
son una opción útil para CI y la automatización del lado del servidor.

Cuando están disponibles tanto una clave de API como un inicio de sesión almacenado, el SDK usa la clave de
API de forma predeterminada. Para usar tu inicio de sesión de ChatGPT en su lugar, selecciónalo para el análisis:

```ts
const result = await security.run("/path/to/repository", {
  auth: "chatgpt",
});

Establece `auth: "api-key"` para requerir una clave de API del entorno. `preflight` acepta
la misma opción `auth`.

## Controlar los errores del análisis

Captura la clase de error exportada que corresponda a la acción que tu aplicación pueda
realizar:

| Error                            | Significado                                                            |
| -------------------------------- | ------------------------------------------------------------------ |
| `AuthenticationRequiredError`    | Un análisis necesita una credencial admitida.                               |
| `ConfigurationError`             | La configuración de Codex o una sobrescritura no es adecuada.                  |
| `InvalidTargetError`             | El repositorio, la ruta, el modo o el objetivo de Git no es adecuado.           |
| `OutputDirectoryError`           | La ubicación de salida o sus permisos no son adecuados.             |
| `OutputInsideProtectedRootError` | El directorio de salida está dentro del repositorio o Worktree analizado. |
| `PluginPythonUnavailableError`   | No hay un intérprete de Python disponible que se pueda usar.                        |
| `PluginBootstrapError`           | No se pudo iniciar el entorno de ejecución del complemento.                                |
| `ScanCostLimitExceededError`     | El análisis superó su límite de costo estimado.                        |
| `IncompleteScanError`            | El análisis terminó antes de generar el resultado requerido.               |
| `ContractValidationError`        | Un análisis completado devolvió un error de contrato estructurado.             |
| `ScanInterruptedError`           | Una interrupción detuvo el análisis y puede haber dejado datos de salida parciales. |

Continúa con el [inicio rápido de la CLI](/es-419/codex/security/cli), la [guía de
CI](/es-419/codex/security/cli/ci) o la [referencia de la
CLI](/es-419/codex/security/cli/reference).

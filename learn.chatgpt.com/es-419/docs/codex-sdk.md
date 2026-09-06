<!-- source: https://learn.chatgpt.com/es-419/docs/codex-sdk -->

Si usas Codex mediante Codex CLI, la extensión para IDE o Codex Cloud, también puedes controlarlo de forma programática.

Usa el SDK cuando necesites:

- Controlar Codex como parte de tu canalización de CI/CD
- Crear tu propio agente que pueda interactuar con Codex para realizar tareas complejas de ingeniería
- Incorporar Codex a tus propias herramientas internas y flujos de trabajo
- Integrar Codex en tu propia aplicación

Usa el SDK de Codex para automatizar tareas de programación, incluidos trabajos en CI. Usa el [App Server de Codex](/es-419/codex/app-server) para crear clientes personalizados que gestionen la autenticación, el historial de conversaciones, las aprobaciones y los eventos del agente transmitidos en streaming.

`codex mcp-server` está en desuso. La [guía del servidor MCP](/es-419/codex/mcp-server) sigue disponible para las integraciones existentes.

Si tienes acceso a la versión beta y necesitas análisis de repositorios o cambios con hallazgos de seguridad estructurados
y cobertura, usa el [SDK de TypeScript
de Codex Security](/es-419/codex/security/sdk).

## Biblioteca de TypeScript

La biblioteca de TypeScript permite que tu aplicación inicie, continúe y reanude hilos locales de Codex.

Usa la biblioteca del lado del servidor; requiere Node.js 18 o posterior.

### Instalación

Para comenzar, instala el SDK de Codex con `npm`:

```bash
npm install @openai/codex-sdk

### Uso

Inicia un hilo con Codex y ejecútalo con tu prompt.

```ts

const codex = new Codex();
const thread = codex.startThread();
const result = await thread.run(
  "Make a plan to diagnose and fix the CI failures"
);

console.log(result.finalResponse);

Llama de nuevo a `run()` para continuar en el mismo hilo o reanuda un hilo anterior proporcionando su ID.

```ts
// running the same thread
const result = await thread.run("Implement the plan");

console.log(result.finalResponse);

// resuming past thread

const threadId = "<thread-id>";
const thread2 = codex.resumeThread(threadId);
const result2 = await thread2.run("Pick up where you left off");

console.log(result2.finalResponse);

Para obtener más información, consulta el [repositorio de TypeScript](https://github.com/openai/codex/tree/main/sdk/typescript).

## Biblioteca de Python

El SDK de Python controla el app-server local de Codex mediante JSON-RPC. Requiere Python 3.10 o posterior. Las compilaciones publicadas del SDK incluyen como dependencia una versión fijada del entorno de ejecución de Codex CLI.

### Instalación

Para instalar el SDK, ejecuta:

```bash
pip install openai-codex

Las compilaciones publicadas del SDK usan automáticamente la versión del entorno de ejecución que tienen fijada. Pasa `CodexConfig(codex_bin=...)` solo cuando tengas la intención de usar un ejecutable local específico de Codex.

El SDK de Python está disponible en una versión estable. `pip install openai-codex`
instala la versión estable más reciente. Usa `pip install --pre openai-codex` para optar
por compilaciones preliminares más recientes.

### Uso

Inicia Codex, crea un hilo y ejecuta un prompt:

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(
        model="gpt-5.6-terra",
        sandbox=Sandbox.workspace_write,
    )
    result = thread.run("Make a plan to diagnose and fix the CI failures")
    print(result.final_response)

Usa `AsyncCodex` si tu aplicación ya es asíncrona:

```python

from openai_codex import AsyncCodex

async def main() -> None:
    async with AsyncCodex() as codex:
        thread = await codex.thread_start(model="gpt-5.6-terra")
        result = await thread.run("Implement the plan")
        print(result.final_response)

asyncio.run(main())

### Valores preestablecidos de Sandbox

Usa los mismos valores preestablecidos de `Sandbox` al crear un hilo o cambiar su acceso al sistema de archivos
para un turno posterior:

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(sandbox=Sandbox.workspace_write)
    thread.run("Make the requested change.")
    review = thread.run("Review the diff only.", sandbox=Sandbox.read_only)

Valores preestablecidos disponibles:

- `Sandbox.read_only`: lee archivos sin permitir operaciones de escritura.
- `Sandbox.workspace_write`: lee archivos y escribe dentro del espacio de trabajo y de los directorios raíz configurados con permisos de escritura.
- `Sandbox.full_access`: se ejecuta sin restricciones de acceso al sistema de archivos.

Cuando omites `sandbox=`, el app-server usa el valor predeterminado configurado. El sandbox
que pases a `run(...)` o `turn(...)` se aplica a ese turno y a los turnos posteriores
del hilo.

Para obtener más información, consulta el [repositorio de Python](https://github.com/openai/codex/tree/main/sdk/python).

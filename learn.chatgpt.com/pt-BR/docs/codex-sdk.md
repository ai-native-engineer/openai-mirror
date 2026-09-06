<!-- source: https://learn.chatgpt.com/pt-BR/docs/codex-sdk -->

Se você usa o Codex por meio do Codex CLI, da extensão para IDE ou do Codex Cloud, também pode controlá-lo por meio de código.

Use o SDK quando precisar:

- Controlar o Codex como parte do seu pipeline de CI/CD
- Criar seu próprio agente para interagir com o Codex e executar tarefas complexas de engenharia
- Incorporar o Codex às suas ferramentas internas e aos seus fluxos de trabalho
- Integrar o Codex ao seu próprio aplicativo

Use o SDK do Codex para automatizar tarefas de programação, incluindo tarefas em CI. Use o [App Server do Codex](/pt-BR/codex/app-server) para criar clientes personalizados que gerenciem autenticação, histórico de conversas, aprovações e o fluxo de eventos do agente.

`codex mcp-server` está obsoleto. O [guia do servidor MCP](/pt-BR/codex/mcp-server) continua disponível para integrações existentes.

Se você tiver acesso à versão beta e precisar de varreduras de repositórios ou alterações com achados
de segurança estruturados e cobertura, use o [SDK em TypeScript
do Codex Security](/pt-BR/codex/security/sdk).

## Biblioteca TypeScript

A biblioteca TypeScript permite que seu aplicativo inicie, continue e retome conversas locais do Codex.

Use a biblioteca no lado do servidor; ela requer Node.js 18 ou uma versão posterior.

### Instalação

Para começar, instale o SDK do Codex usando `npm`:

```bash
npm install @openai/codex-sdk

### Uso

Inicie uma conversa com o Codex e execute seu prompt nela.

```ts

const codex = new Codex();
const thread = codex.startThread();
const result = await thread.run(
  "Make a plan to diagnose and fix the CI failures"
);

console.log(result.finalResponse);

Chame `run()` novamente para continuar na mesma conversa ou retome uma conversa anterior informando o ID dela.

```ts
// running the same thread
const result = await thread.run("Implement the plan");

console.log(result.finalResponse);

// resuming past thread

const threadId = "<thread-id>";
const thread2 = codex.resumeThread(threadId);
const result2 = await thread2.run("Pick up where you left off");

console.log(result2.finalResponse);

Para saber mais, consulte o [repositório do SDK para TypeScript](https://github.com/openai/codex/tree/main/sdk/typescript).

## Biblioteca Python

O SDK para Python controla o app-server local do Codex via JSON-RPC. Ele requer Python 3.10 ou uma versão posterior. As versões publicadas do SDK incluem uma versão fixada do ambiente de execução do Codex CLI como dependência.

### Instalação

Para instalar o SDK, execute:

```bash
pip install openai-codex

As versões publicadas do SDK usam automaticamente a versão fixada do ambiente de execução. Passe `CodexConfig(codex_bin=...)` apenas quando quiser usar deliberadamente um executável local específico do Codex.

O SDK para Python está disponível em uma versão estável. `pip install openai-codex`
instala a versão estável mais recente. Use `pip install --pre openai-codex` para optar
por versões de pré-lançamento mais recentes.

### Uso

Inicie o Codex, crie uma conversa e execute um prompt:

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(
        model="gpt-5.6-terra",
        sandbox=Sandbox.workspace_write,
    )
    result = thread.run("Make a plan to diagnose and fix the CI failures")
    print(result.final_response)

Use `AsyncCodex` quando seu aplicativo já for assíncrono:

```python

from openai_codex import AsyncCodex

async def main() -> None:
    async with AsyncCodex() as codex:
        thread = await codex.thread_start(model="gpt-5.6-terra")
        result = await thread.run("Implement the plan")
        print(result.final_response)

asyncio.run(main())

### Predefinições de Sandbox

Use as mesmas predefinições de `Sandbox` ao criar uma conversa ou alterar seu acesso ao sistema de arquivos
para um turno posterior:

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(sandbox=Sandbox.workspace_write)
    thread.run("Make the requested change.")
    review = thread.run("Review the diff only.", sandbox=Sandbox.read_only)

Predefinições disponíveis:

- `Sandbox.read_only`: Ler arquivos sem permitir gravações.
- `Sandbox.workspace_write`: Ler arquivos e gravar no workspace e nos diretórios raiz configurados com permissão de gravação.
- `Sandbox.full_access`: Executar sem restrições de acesso ao sistema de arquivos.

Quando você omite `sandbox=`, o app-server usa o valor padrão configurado. Um sandbox
passado para `run(...)` ou `turn(...)` se aplica a esse turno e aos turnos posteriores
da conversa.

Para saber mais, consulte o [repositório do SDK para Python](https://github.com/openai/codex/tree/main/sdk/python).

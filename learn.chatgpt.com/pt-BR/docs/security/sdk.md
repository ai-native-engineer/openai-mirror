<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/sdk -->

Use o SDK do Codex Security para TypeScript no seu aplicativo ou ferramenta de desenvolvimento
para executar verificações de segurança em repositórios e alterações de código. O SDK retorna
achados tipados, detalhes de cobertura e caminhos para os artefatos das verificações. Para verificações
mais longas, oferece suporte a pré-verificações, limites de custo, callbacks de progresso e cancelamento.

O SDK usa módulos ECMAScript (ESM) e é executado no servidor com Node.js 22
(22.13.0 ou posterior), 24 ou 26. As verificações também exigem Python 3.10 ou posterior.
O Python 3.10 também exige o pacote `tomli`.

  O SDK do Codex Security está [disponível publicamente no
  GitHub](https://github.com/openai/codex-security). Para executar verificações, é necessário ter
  acesso ao Codex Security. Para agentes de programação em geral, consulte o [guia do SDK
  do Codex](/pt-BR/codex/codex-sdk). Para fluxos de trabalho no terminal e em CI, consulte o [início rápido da CLI
  do Codex Security](/pt-BR/codex/security/cli).

## Configurar o SDK

Instale o SDK:

```bash
npm install @openai/codex-security

Antes de iniciar uma verificação, defina `OPENAI_API_KEY` ou `CODEX_API_KEY`, use um
login existente do Codex armazenado em arquivo ou [configure outro
provedor](#configure-the-runtime-and-credentials). O Amazon Bedrock usa credenciais da
AWS; OpenRouter e Fireworks usam chaves de API e
configurações específicas do provedor.

Para obter os melhores resultados, use uma conta verificada para o [Trusted Access for
Cyber](https://chatgpt.com/cyber). Fazer login ou fornecer uma chave de API não
concede o Trusted Access.

## Executar uma verificação

Verifique apenas repositórios nos quais você confia e que tem permissão para avaliar. O SDK é executado
com as permissões locais do seu sistema operacional e nunca pausa para solicitar aprovação.
Os processos de verificação podem herdar seu ambiente; portanto, remova credenciais não relacionadas
antes de começar. Consulte [Permissões de verificação
local](/pt-BR/codex/security/cli/reference#local-scan-permissions).

Crie um único cliente `CodexSecurity`, execute uma verificação padrão do repositório e feche
o cliente quando o trabalho terminar. Passe `outputDir` para escolher um diretório privado
de resultados fora da árvore de trabalho do Git que contém o repositório.

Se você omitir `outputDir`, o Codex Security salvará os resultados no próprio diretório
de estado persistente. Os resultados podem incluir trechos do código-fonte e detalhes de
vulnerabilidades; portanto, escolha permissões e políticas de retenção adequadas.

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

`run` inicia a verificação, aguarda sua conclusão, valida os artefatos selados
e retorna um `ScanResult`. `close` libera o ambiente de execução isolado e aceita
chamadas repetidas.

## Verificar as entradas com a pré-verificação

Use `preflight` para verificar um repositório, o alvo, o modo, os documentos da base de conhecimento,
o local de saída e a configuração do Codex antes de iniciar uma verificação:

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

A pré-verificação não altera o ambiente de execução nem as credenciais do Codex. Ela também deixa
a detecção do plug-in e do Python para a própria verificação. Isso torna a pré-verificação útil
para verificar a entrada do usuário antes de uma operação de longa duração ou que exija credenciais.

Para ver uma prévia do arquivamento de um diretório de resultados existente, defina
`archiveExisting: true`:

```ts
const plan = await security.preflight("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
});

console.log(plan.archiveDir);

O `archiveDir` retornado mostra uma prévia do nome do diretório de arquivamento. O caminho final pode
ser diferente porque `run` gera seu próprio destino exclusivo. Capture o caminho real
do arquivamento com `onOutputArchived`:

```ts
await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
  onOutputArchived(archiveDir) {
    console.log("Archived results:", archiveDir);
  },
});

A verificação arquiva os resultados anteriores e começa com um diretório de saída
vazio.

## Escolher um alvo de verificação

O SDK oferece suporte a alvos de repositório, caminho, diff entre commits e árvore de trabalho.
O alvo padrão é o repositório inteiro.

### Verificar caminhos selecionados

Passe um array de caminhos dentro do repositório:

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
});

Os caminhos podem identificar arquivos ou diretórios. O SDK resolve cada caminho dentro do
repositório e remove duplicatas.

### Verificar alterações registradas em commits

Use `DiffTarget.refs` para verificar alterações registradas em commits entre duas revisões do Git disponíveis
localmente:

```ts

const target = DiffTarget.refs({
  base: "origin/main",
  head: "HEAD",
});

const result = await security.run("/path/to/repository", { target });

Por padrão, a referência head é `HEAD`. Os alvos de diff exigem que o argumento do repositório
seja a raiz da árvore de trabalho do Git.

### Verificar a árvore de trabalho

Use `DiffTarget.workingTree` para verificar alterações preparadas e não preparadas em relação a uma revisão
de base:

```ts
const target = DiffTarget.workingTree({ base: "HEAD" });
const result = await security.run("/path/to/repository", { target });

Por padrão, a base é `HEAD`. Faça o fetch das revisões selecionadas antes de iniciar uma
verificação de diff ou da árvore de trabalho.

### Selecionar o modo aprofundado

Defina `mode: "deep"` para uma verificação de repositório ou de caminho que exija uma revisão mais ampla:

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

O modo aprofundado oferece suporte a alvos de repositório e de caminho. Use o modo padrão para verificações de diff e
da árvore de trabalho. As configurações opcionais controlam os executores independentes e simultâneos
de verificações padrão, os subagentes por executor, as verificações consecutivas concluídas pelos executores
sem novos achados e o número total e a duração das execuções dos executores. Elas
exigem `mode: "deep"`.

`maxTimeHours` tem `96` como valor padrão e aceita um número positivo de até `96`,
incluindo frações de hora. Ao atingir o prazo, o Codex Security interrompe os executores ainda em
atividade, preserva os resultados das verificações concluídas e os reúne no relatório
final. Revise `result.coverage.completeness` antes de considerar uma verificação com limite de tempo
como evidência de cobertura completa.

### Adicionar uma base de conhecimento de segurança

Passe documentos de arquitetura, modelos de ameaças ou políticas de segurança por meio de
`knowledgeBasePaths`:

```ts
const result = await security.run("/path/to/repository", {
  knowledgeBasePaths: [
    "/path/to/architecture.md",
    "/path/to/security-policies",
  ],
});

O SDK aceita arquivos ou diretórios e faz buscas recursivas nos diretórios.
Os formatos de documento aceitos são `.md`, `.markdown`, `.txt`, `.pdf` e `.docx`.
O SDK rejeita caminhos de entrada que sejam links, ignora entradas de diretório que sejam links e mantém
o conteúdo extraído dos documentos fora dos resultados salvos da verificação.

### Adicionar instruções de verificação e acompanhamento

Use `scanPrompt` para direcionar a verificação e `postScanPrompt` para solicitar um acompanhamento:

```ts
const result = await security.run("/path/to/repository", {
  scanPrompt: "Focus on tenant isolation and authorization checks.",
  postScanPrompt: "Write confirmed findings to post-scan-summary.md.",
});

Se o acompanhamento falhar, o SDK mantém a verificação concluída e informa o
erro por meio de `onWarning`. Ele restaura quaisquer artefatos da verificação concluída
que tenham sido alterados pelo acompanhamento.

### Definir um orçamento para a verificação

Defina `maxCostUsd` para interromper uma verificação quando o custo estimado do modelo ultrapassar um limite.
Use `onCost` para acompanhar o custo durante a verificação:

```ts
const result = await security.run("/path/to/repository", {
  maxCostUsd: 5,
  onCost(cost) {
    console.log(cost.estimatedUsd);
  },
});

console.log(result.cost?.estimatedUsd);

O limite estima os gastos, mas não é um teto rígido; portanto, solicitações já em
andamento podem terminar com um custo um pouco acima dele. Se uma verificação aprofundada atingir o limite depois que
o Codex Security consolidar os resultados das verificações concluídas pelos executores, `run` retorna um resultado
com `coverage.completeness` definido como `"partial"` e informa o aviso de orçamento
por meio de `onWarning`.

Se a verificação não conseguir produzir um resultado parcial concluído, `run` lança
`ScanCostLimitExceededError` e preserva qualquer saída disponível.

## Trabalhar com os resultados da verificação

`ScanResult` expõe os documentos estruturados, os metadados da verificação e os
caminhos dos artefatos:

| Propriedade             | Conteúdo                                                                           |
| -------------------- | ---------------------------------------------------------------------------------- |
| `manifest`           | O manifesto selado da verificação, incluindo o alvo, o escopo, o produtor e os registros de artefatos. |
| `findings`           | Achados da verificação atual. Leia os objetos dos achados em `findings.findings`.     |
| `repositoryFindings` | Achados em aberto nas verificações do repositório, quando houver histórico de verificações.             |
| `coverage`           | Superfícies revisadas, exclusões, trabalho adiado, questões em aberto e completude.    |
| `scanDir`            | O diretório da verificação.                                                                |
| `threadId`           | O identificador da thread do Codex para a verificação.                                          |
| `turnResult`         | Status do turno, resposta e metadados de uso disponíveis.                               |
| `cost`               | Custo estimado do modelo e dos tokens, ou `null` quando indisponível.                        |
| `reportPath`         | O caminho para `report.md`.                                                           |
| `manifestPath`       | O caminho para `scan-manifest.json`.                                                  |
| `findingsPath`       | O caminho para `findings.json`.                                                       |
| `coveragePath`       | O caminho para `coverage.json`.                                                       |
| `artifactsDir`       | O diretório de artefatos complementares.                                                |
| `sarifPath`          | O caminho do SARIF gerado ou `null` quando não houver SARIF.                          |
| `pluginVersion`      | A versão registrada pelo produtor da verificação.                                         |

Para exigir o mesmo plug-in em uma verificação posterior, forneça
`expectedPluginVersion: result.pluginVersion`. O SDK rejeita a verificação se
a versão instalada do plug-in for diferente.

Use diretamente os achados estruturados e a cobertura:

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

Os achados podem incluir os campos opcionais `codeEvidence`, `rootCause`, `validation`,
`attackPath`, `remediationTests` e `preventiveControls`.

Para achados que abrangem todo o repositório, `confirmedInLatestScan` diferencia os achados
identificados na verificação mais recente dos achados anteriores que permanecem em aberto:

```ts
for (const finding of result.repositoryFindings ?? []) {
  console.log(finding.title, finding.confirmedInLatestScan);
}

A completude da cobertura é `complete`, `partial` ou `unknown`. Revise as superfícies cuja análise foi adiada,
as exclusões e as questões em aberto antes de usar uma verificação como evidência para uma
decisão de segurança.

`result.toJSON()` retorna o manifesto, os achados do repositório e da verificação atual,
a cobertura, os identificadores da verificação e da thread, `reportPath`, `artifactsDir`,
`sarifPath`, o custo e os metadados do turno em um único objeto pronto para JSON.

## Acompanhar ou cancelar uma verificação

Forneça callbacks de `ScanOptions` para informar o início da verificação, o progresso dos executores e
as novas tentativas de conexão:

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

Forneça um `AbortSignal` quando o cancelamento vier de uma solicitação, de um controlador de tarefas
ou de um tempo limite:

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

Uma verificação interrompida pode deixar uma saída parcial em `scanDir`. Preserve esse
diretório quando for necessário investigar o resultado.

Aplicativos que exibem o progresso da configuração da verificação também podem usar os callbacks de `ScanOptions`
relacionados ao ciclo de vida:

| Callback                            | Chamado quando                                          |
| ----------------------------------- | ---------------------------------------------------- |
| `onAuthentication(authentication)`  | A verificação seleciona seu método de autenticação.          |
| `onOutputArchived(archiveDir)`      | Os resultados existentes são movidos para o diretório de arquivamento.      |
| `onOutputDirReady(scanDir)`         | O diretório privado da verificação está pronto.                 |
| `onScanStarted()`                   | A configuração da verificação é concluída e a execução começa.           |
| `onTrustedAccessStatus(status)`     | O status do Trusted Access fica disponível.             |
| `onReconnect(attempt, maxAttempts)` | O SDK tenta reconectar um fluxo de verificação desconectado.          |
| `onActivity(activity)`              | Um comando, uma ferramenta, uma etapa de raciocínio ou uma mensagem recebe uma atualização. |
| `onProgress(progress)`              | A fase da verificação ou a quantidade de arquivos revisados muda.       |
| `onWorkerStatus(status)`            | O status da pré-verificação ou do despacho do executor muda.         |
| `onSessionEvent(session)`           | Uma sessão de verificação ou de um executor emite um evento.             |
| `onCost(cost)`                      | Uma estimativa atualizada do custo da verificação fica disponível.         |
| `onWarning(warning)`                | A verificação emite um aviso.                          |
| `onObserverError(observer, error)`  | Outro callback do ciclo de vida da verificação lança um erro.     |

O status do Trusted Access é `granted`, `not_granted` ou `unknown`. O acesso ausente ou
desconhecido também aciona `onWarning`.

`onSessionEvent` recebe eventos sem ocultação de informações que podem conter código-fonte
ou credenciais. Filtre-os antes de enviá-los a logs compartilhados ou a outros
serviços.

## Configurar o ambiente de execução e as credenciais

Forneça uma configuração do ambiente de execução quando precisar de um plug-in ou interpretador específico, ou
de uma configuração específica do Codex:

```ts
const security = new CodexSecurity({
  pluginPath: "/path/to/codex-security-plugin",
  pythonPath: "/path/to/python",
  codexOverrides: {
    model: "gpt-5.6-terra",
    model_reasoning_effort: "high",
  },
});

`pluginPath` aceita um diretório de plug-in ou um arquivo ZIP. `pythonPath` seleciona o
interpretador do plug-in. `codexOverrides` incorpora valores compatíveis à configuração isolada
do Codex. As verificações usam `gpt-5.6-sol` com esforço de raciocínio extra alto
por padrão. Defina `model` e `model_reasoning_effort` em `codexOverrides` para usar
outro modelo ou nível de esforço de raciocínio. Para usar o [Amazon
Bedrock](/pt-BR/codex/security/cli/reference#use-amazon-bedrock), defina
`model_provider` e `model` em `codexOverrides`.

`codexOverrides` não pode restringir o acesso da verificação ao sistema de arquivos nem alterar sua
política de aprovação. Consulte [Permissões de verificação
local](/pt-BR/codex/security/cli/reference#local-scan-permissions).

Para OpenRouter ou Fireworks, forneça também a chave de API correspondente e uma configuração completa
do provedor em `codexOverrides`. Por exemplo, defina
`OPENROUTER_API_KEY` e configure o OpenRouter:

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

Para o Fireworks, altere as duas chaves `openrouter` para `fireworks`, defina `name` como
`Fireworks AI`, defina `env_key` como `FIREWORKS_API_KEY`, use
`https://api.fireworks.ai/inference/v1` como `base_url` e selecione um modelo
do Fireworks.

O cliente também expõe os métodos de autenticação compatíveis:

| Método                     | Finalidade                                                     |
| -------------------------- | ----------------------------------------------------------- |
| `loginApiKey(apiKey)`      | Autenticar o ambiente de execução isolado com uma chave de API.          |
| `loginChatGPT()`           | Iniciar um fluxo de login no navegador e retornar um handle de login.     |
| `loginChatGPTDeviceCode()` | Iniciar um fluxo de login por código de dispositivo e retornar um handle de login. |
| `account()`                | Retornar o estado atual da autenticação.                    |
| `logout()`                 | Limpar a autenticação isolada.                              |

Um handle de login disponibiliza `waitForInstructions`, `authUrl`, `verificationUrl`,
`userCode`, `wait` e `cancel` para que um aplicativo possa apresentar e concluir o
fluxo de login selecionado. O SDK pode reutilizar um login do Codex armazenado em arquivo. As chaves de API
são uma boa opção para CI e automação no servidor.

Quando uma chave de API e um login armazenado estão disponíveis, o SDK usa a chave de API
por padrão. Para usar seu login do ChatGPT em vez disso, selecione-o para a verificação:

```ts
const result = await security.run("/path/to/repository", {
  auth: "chatgpt",
});

Defina `auth: "api-key"` para exigir uma chave de API definida no ambiente. `preflight` aceita
a mesma opção `auth`.

## Tratar erros de verificação

Capture a classe de erro exportada correspondente à ação que seu aplicativo pode
executar:

| Erro                            | Significado                                                            |
| -------------------------------- | ------------------------------------------------------------------ |
| `AuthenticationRequiredError`    | Uma verificação exige uma credencial compatível.                               |
| `ConfigurationError`             | A configuração do Codex ou uma substituição não é adequada.                  |
| `InvalidTargetError`             | O repositório, o caminho, o modo ou o alvo do Git não é adequado.           |
| `OutputDirectoryError`           | O local de saída ou suas permissões não são adequados.             |
| `OutputInsideProtectedRootError` | O diretório de saída está dentro do repositório ou da árvore de trabalho incluídos na verificação. |
| `PluginPythonUnavailableError`   | Nenhum interpretador Python utilizável está disponível.                        |
| `PluginBootstrapError`           | O ambiente de execução do plug-in não pôde ser iniciado.                                |
| `ScanCostLimitExceededError`     | A verificação excedeu seu limite de custo estimado.                        |
| `IncompleteScanError`            | A verificação terminou antes de produzir o resultado exigido.               |
| `ContractValidationError`        | Uma verificação concluída retornou um erro de contrato estruturado.             |
| `ScanInterruptedError`           | Uma interrupção encerrou a verificação e pode ter deixado uma saída parcial. |

Continue com o [início rápido da CLI](/pt-BR/codex/security/cli), o [guia de
CI](/pt-BR/codex/security/cli/ci) ou a [referência da
CLI](/pt-BR/codex/security/cli/reference).

<!-- source: https://learn.chatgpt.com/pt-BR/docs/non-interactive-mode -->

O modo não interativo permite executar o Codex em scripts (por exemplo, em jobs de integração contínua (CI)) sem abrir a TUI interativa.
Para invocá-lo, use `codex exec`.

Para ver os detalhes de cada flag, consulte [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec).

## Quando usar `codex exec`

Use `codex exec` quando quiser que o Codex:

- Seja executado como parte de um pipeline (CI, verificações antes do merge, jobs agendados).
- Produza uma saída que você possa encaminhar por pipe para outras ferramentas (por exemplo, para gerar notas de versão ou resumos).
- Integre-se naturalmente a fluxos de trabalho da CLI que encadeiam a saída de comandos como entrada para o Codex e passam a saída do Codex para outras ferramentas.
- Seja executado com configurações explícitas e predefinidas de Sandbox e Aprovação.

## Uso básico

Passe o prompt de uma tarefa como um único argumento:

```bash
codex exec "summarize the repository structure and list the top 5 risky areas"

Enquanto `codex exec` está em execução, o Codex transmite continuamente o progresso para `stderr` e imprime apenas a mensagem final do agente em `stdout`. Assim, fica fácil redirecionar ou encaminhar por pipe o resultado final:

```bash
codex exec "generate release notes for the last 10 commits" | tee release-notes.md

Use `--ephemeral` quando não quiser salvar em disco os arquivos de rollout da sessão:

```bash
codex exec --ephemeral "triage this repository and suggest next steps"

Se o stdin for enviado por pipe e você também fornecer um argumento de prompt, o Codex tratará o prompt como a instrução e o conteúdo recebido pelo pipe como contexto adicional.

Isso permite gerar a entrada com um comando e enviá-la diretamente ao Codex:

```bash
curl -s https://jsonplaceholder.typicode.com/comments \
  | codex exec "format the top 20 items into a markdown table" \
  > table.md

Para padrões mais avançados de uso de pipe com stdin, consulte [Uso avançado de pipe com stdin](#advanced-stdin-piping).

## Permissões e segurança

Por padrão, `codex exec` é executado em um Sandbox de somente leitura. Em automações, defina apenas as permissões mínimas necessárias para o fluxo de trabalho:

- Permitir edições: `codex exec --sandbox workspace-write "<task>"`
- Permitir acesso mais amplo: `codex exec --sandbox danger-full-access "<task>"`

Use `danger-full-access` apenas em um ambiente controlado (por exemplo, um runner de CI isolado ou um contêiner).

O Codex mantém `codex exec --full-auto` como uma flag de compatibilidade obsoleta e exibe um aviso. Em scripts novos, prefira a flag explícita `--sandbox workspace-write`.

Use `--ignore-user-config` quando precisar de uma execução que não carregue `$CODEX_HOME/config.toml` e `--ignore-rules` quando precisar ignorar os arquivos `.rules` de execpolicy do usuário e do projeto em um ambiente de automação controlado.

Se você configurar um servidor MCP habilitado com `required = true` e a inicialização dele falhar, `codex exec` será encerrado com um erro em vez de continuar sem esse servidor.

## Tornar a saída legível por máquina

Para consumir a saída do Codex em scripts, use a saída JSON Lines:

```bash
codex exec --json "summarize the repo structure" | jq

Ao habilitar `--json`, `stdout` passa a ser um fluxo JSON Lines (JSONL), permitindo capturar todos os eventos emitidos pelo Codex durante a execução. Os tipos de evento incluem `thread.started`, `turn.started`, `turn.completed`, `turn.failed`, `item.*` e `error`.

Os tipos de item incluem mensagens do agente, raciocínio, execuções de comandos, alterações em arquivos, chamadas de ferramentas MCP, pesquisas na Web e atualizações do plano.

Exemplo de fluxo JSON (cada linha é um objeto JSON):

```jsonl
{"type":"thread.started","thread_id":"0199a213-81c0-7800-8aa1-bbab2a035a53"}
{"type":"turn.started"}
{"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"bash -lc ls","status":"in_progress"}}
{"type":"item.completed","item":{"id":"item_3","type":"agent_message","text":"Repo contains docs, sdk, and examples directories."}}
{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122,"reasoning_output_tokens":0}}

Se você precisar apenas da mensagem final, grave-a em um arquivo com `-o <path>`/`--output-last-message <path>`. Isso grava a mensagem final no arquivo e ainda a imprime em `stdout` (consulte [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec) para ver detalhes).

## Criar saídas estruturadas com um esquema

Se precisar de dados estruturados para etapas posteriores, use `--output-schema` para solicitar uma resposta final em conformidade com um JSON Schema.
Isso é útil para fluxos de trabalho automatizados que exigem campos estáveis (por exemplo, resumos de jobs, relatórios de risco ou metadados de versão).

`schema.json`

```json
{
  "type": "object",
  "properties": {
    "project_name": { "type": "string" },
    "programming_languages": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["project_name", "programming_languages"],
  "additionalProperties": false
}

Execute o Codex com o esquema e grave a resposta JSON final em disco:

```bash
codex exec "Extract project metadata" \
  --output-schema ./schema.json \
  -o ./project-metadata.json

Exemplo de saída final (stdout):

```json
{
  "project_name": "Codex CLI",
  "programming_languages": ["Rust", "TypeScript", "Shell"]
}

## Autenticação em automações

`codex exec` reutiliza por padrão a autenticação salva da CLI. Na CI, é comum fornecer as credenciais explicitamente:

Se o ambiente de execução confiável na nuvem ou de CI já recebe tokens de carga de trabalho
de curta duração, use
[federação de identidade de carga de trabalho](/pt-BR/codex/enterprise/workload-identity)
em vez de armazenar uma credencial da OpenAI.

### Usar autenticação por chave de API

Para o GitHub Actions, use a [Codex GitHub Action](/pt-BR/codex/github-action) em vez de instalar e autenticar a CLI por conta própria. A ação foi projetada para reduzir a exposição da chave de API instalando o Codex, iniciando um proxy da Responses API e executando o Codex com uma estratégia de segurança configurável.

Não defina `OPENAI_API_KEY` nem `CODEX_API_KEY` como variáveis de ambiente no nível do job em fluxos de trabalho que façam checkout de código controlado pelo repositório ou o executem. Scripts de build, testes, hooks do ciclo de vida das dependências ou uma ação comprometida no mesmo job podem ler essas variáveis de ambiente.

Em outros ambientes de automação, defina `CODEX_API_KEY` apenas para a invocação do Codex
que precisa dessa chave e garanta que nenhum código não confiável seja executado no mesmo ambiente
do processo.

Para usar outra chave de API em uma única execução, defina `CODEX_API_KEY` diretamente no comando:

```bash
CODEX_API_KEY=<api-key> codex exec --json "triage open bug reports"

Você pode usar `CODEX_API_KEY` com `codex exec`, `codex review`, o SDK
para TypeScript e `codex exec-server --remote`.

Leia esta seção se precisar executar jobs de CI/CD com uma conta de usuário do Codex em vez de uma
chave de API, como equipes empresariais que usam o acesso ao Codex gerenciado pelo ChatGPT em runners
confiáveis ou usuários que precisam dos limites de taxa do ChatGPT/Codex em vez de usar uma chave de API.

As chaves de API são a opção padrão recomendada para automação porque são mais simples de
provisionar e rotacionar. Use essa abordagem somente se precisar especificamente executar a automação com
sua conta do Codex.

Trate `~/.codex/auth.json` como uma senha: o arquivo contém tokens de acesso. Não
faça commit desse arquivo, não o cole em tickets nem o compartilhe em chats.

Não use este fluxo de trabalho em repositórios públicos ou de código aberto. Se `codex login`
não for uma opção no runner, provisione `auth.json` por meio de armazenamento seguro, execute
o Codex no runner para que ele atualize o arquivo no próprio local e preserve o arquivo atualizado
entre as execuções.

Consulte [Manter a autenticação da conta do Codex em CI/CD (avançado)](/codex/auth/ci-cd-auth).

## Retomar uma sessão não interativa

Se precisar continuar uma execução anterior (por exemplo, em um pipeline de duas etapas), use o subcomando `resume`:

```bash
codex exec "review the change for race conditions"
codex exec resume --last "fix the race conditions you found"

Você também pode retomar uma sessão específica pelo ID com `codex exec resume <SESSION_ID>`.

## Repositório Git obrigatório

O Codex exige que os comandos sejam executados dentro de um repositório Git para evitar alterações destrutivas. Ignore essa verificação com `codex exec --skip-git-repo-check` se tiver certeza de que o ambiente é seguro.

## Padrões comuns de automação

### Exemplo: correção automática de falhas de CI no GitHub Actions

Para fluxos de trabalho do GitHub Actions, use [`openai/codex-action`](https://github.com/openai/codex-action) em vez de instalar o Codex e passar a chave de API para uma etapa de shell. A ação inicia um proxy seguro para a chave de API da OpenAI.

Você pode usar o Codex para propor correções automaticamente quando um fluxo de trabalho de CI falhar. O padrão é:

1. Acione um fluxo de trabalho subsequente quando o fluxo de trabalho principal de CI for concluído com erro.
2. Faça checkout do commit com falha usando apenas permissões de leitura no repositório.
3. Execute os comandos de configuração antes do Codex, sem expor sua chave de API da OpenAI a essas etapas.
4. Execute a Codex GitHub Action.
5. Salve as alterações locais feitas pelo Codex como um artefato de patch.
6. Em um job separado, aplique o patch e abra um pull request.

O job do Codex abaixo tem apenas `contents: read`. Após a execução do Codex, esse job apenas serializa o diff como um artefato. O job `open_pr` recebe permissões de gravação no repositório, mas não recebe `OPENAI_API_KEY`.

O exemplo pressupõe um projeto Node.js. Ajuste os comandos de configuração e teste de acordo com sua stack.

Para ver uma lista de verificação de segurança mais detalhada, consulte as [orientações de segurança da GitHub Action do Codex](https://github.com/openai/codex-action/blob/main/docs/security.md).

```yaml
name: Codex auto-fix on CI failure

on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]

jobs:
  generate_fix:
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      has_patch: ${{ steps.diff.outputs.has_patch }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0
          persist-credentials: false

      - uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install dependencies
        run: |
          if [ -f package-lock.json ]; then npm ci; fi

      - name: Run Codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt: |
            The CI workflow "${{ github.event.workflow_run.name }}" failed for commit
            ${{ github.event.workflow_run.head_sha }}.

            Run `npm test --silent` to reproduce the failure. Identify the minimal
            change needed to make the tests pass, implement only that change, and
            run `npm test --silent` again.

            Do not refactor unrelated files.

      - name: Create patch artifact
        id: diff
        run: |
          git add -N .
          git diff --binary HEAD > codex.patch
          if [ -s codex.patch ]; then
            echo "has_patch=true" >> "$GITHUB_OUTPUT"
          else
            echo "has_patch=false" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload patch artifact
        if: steps.diff.outputs.has_patch == 'true'
        uses: actions/upload-artifact@v4
        with:
          name: codex-fix-patch
          path: codex.patch
          if-no-files-found: error

  open_pr:
    runs-on: ubuntu-latest
    needs: generate_fix
    if: needs.generate_fix.outputs.has_patch == 'true'
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0

      - uses: actions/download-artifact@v4
        with:
          name: codex-fix-patch

      - name: Apply Codex patch
        run: git apply --index codex.patch

      - name: Open pull request
        env:
          GH_TOKEN: ${{ github.token }}
          FAILED_HEAD_BRANCH: ${{ github.event.workflow_run.head_branch }}
          FAILED_HEAD_SHA: ${{ github.event.workflow_run.head_sha }}
          RUN_ID: ${{ github.event.workflow_run.run_id }}
        run: |
          branch="codex/auto-fix-$RUN_ID"

          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git switch -c "$branch"
          git commit -m "Auto-fix failing CI via Codex"
          git push origin "$branch"

          {
            echo "Codex generated this patch after CI failed for \`$FAILED_HEAD_SHA\`."
            echo
            echo "Review the changes before merging."
          } > pr-body.md

          gh pr create \
            --base "$FAILED_HEAD_BRANCH" \
            --head "$branch" \
            --title "Auto-fix failing CI via Codex" \
            --body-file pr-body.md

## Uso avançado de pipes com stdin

Quando outro comando produzir uma entrada para o Codex, escolha o padrão de uso de stdin conforme a origem desejada para a instrução. Use prompt-plus-stdin quando você já tiver definido a instrução e quiser passar a saída recebida via pipe como contexto. Use `codex exec -` quando quiser que stdin contenha o prompt inteiro.

### Use prompt-plus-stdin

Prompt-plus-stdin é útil quando outro comando já produz os dados que você quer que o Codex examine. Nesse modo, você mesmo escreve a instrução e encaminha a saída via pipe para usá-la como contexto. Por isso, esse padrão se encaixa naturalmente em fluxos de trabalho da CLI baseados em saídas de comandos, logs e dados gerados.

```bash
npm test 2>&1 \
  | codex exec "summarize the failing tests and propose the smallest likely fix" \
  | tee test-summary.md

### Resumir logs

```bash
tail -n 200 app.log \
  | codex exec "identify the likely root cause, cite the most important errors, and suggest the next three debugging steps" \
  > log-triage.md

### Inspecionar problemas de TLS ou HTTP

```bash
curl -vv https://api.example.com/health 2>&1 \
  | codex exec "explain the TLS or HTTP failure and suggest the most likely fix" \
  > tls-debug.md

### Preparar uma atualização pronta para publicação no Slack

```bash
gh run view 123456 --log \
  | codex exec "write a concise Slack-ready update on the CI failure, including the likely cause and next step" \
  | pbcopy

### Redigir um comentário de pull request com base nos logs de CI

```bash
gh run view 123456 --log \
  | codex exec "summarize the failure in 5 bullets for the pull request thread" \
  | gh pr comment 789 --body-file -

### Use `codex exec -` quando o prompt vier de stdin

Se você omitir o argumento de prompt, o Codex lerá o prompt via stdin. Use `codex exec -` quando quiser forçar explicitamente esse comportamento.

O valor sentinela `-` é útil quando outro comando ou script gera o prompt inteiro dinamicamente. Essa abordagem é indicada quando você armazena prompts em arquivos, monta prompts com scripts de shell ou combina a saída de comandos em tempo real com instruções antes de enviar o prompt completo ao Codex.

```bash
cat prompt.txt | codex exec -

```bash
printf "Summarize this error log in 3 bullets:\n\n%s\n" "$(tail -n 200 app.log)" \
  | codex exec -

```bash
generate_prompt.sh | codex exec - --json > result.jsonl

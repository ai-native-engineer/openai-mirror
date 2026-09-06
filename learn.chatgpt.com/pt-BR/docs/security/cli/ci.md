<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/cli/ci -->

Execute a CLI do Codex Security na CI para revisar as alterações exatas de um pull request
ou merge request, preservar os achados e a cobertura e, opcionalmente, fazer a verificação falhar a
partir de uma severidade escolhida. Comece com resultados informativos, avalie a qualidade da análise e
o tempo de execução e depois adicione uma política de severidade adequada ao seu repositório.

  Instale o pacote público `@openai/codex-security`. A execução de análises ainda
  requer acesso ao Codex Security.

Este guia inclui exemplos para GitHub Actions e GitLab CI/CD. Os mesmos comandos de análise
e exportação funcionam em outros sistemas de CI.

## Prepare o fluxo de trabalho

Armazene uma chave de API da OpenAI no armazenamento de segredos do seu provedor de CI com o nome
`CODEX_SECURITY_API_KEY`.

Mapeie esse segredo diretamente para a variável de ambiente `OPENAI_API_KEY` da etapa
de análise. Mantenha a credencial restrita ao processo de análise e use
`--auth api-key` para selecioná-la explicitamente.

Execute o fluxo de trabalho somente para repositórios e pull requests em que você confia. As análises usam
as permissões locais do executor e não são pausadas para solicitar aprovação. Os processos de análise
podem herdar o ambiente do job, portanto mantenha tokens não relacionados e credenciais de nuvem
fora desse ambiente.

O executor precisa de:

- Node.js 22 (22.13.0 ou posterior), 24 ou 26.
- Python 3.10 ou posterior.
- O pacote publicado `@openai/codex-security`, instalado fora do
  checkout do repositório.
- O histórico das revisões head e base do pull request ou merge request, para que o Git possa calcular
a base de mesclagem.

## Adicione o fluxo de trabalho do GitHub Actions

Para repositórios privados ou internos, ative o
[GitHub Code Security](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github)
antes de enviar o SARIF.

Crie `.github/workflows/codex-security.yml`. Antes de fazer checkout do pull request,
instale `@openai/codex-security` em
`$RUNNER_TEMP/codex-security` para que o executável confiável fique disponível em
`$RUNNER_TEMP/codex-security/node_modules/.bin/codex-security`:

```yaml
name: Codex Security scan

on:
  pull_request:

jobs:
  codex-security:
    if: github.event.pull_request.head.repo.full_name == github.repository && github.actor != 'dependabot[bot]'
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write
    steps:
      - name: Set up Node.js
        uses: actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7
        with:
          node-version: "26"

      - name: Set up Python
        uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7
        with:
          python-version: "3.14"

      - name: Install Codex Security
        run: |
          set -euo pipefail
          npm install \
            --prefix "$RUNNER_TEMP/codex-security" \
            --ignore-scripts \
            --no-audit \
            --no-fund \
            @openai/codex-security

      - name: Verify Codex Security
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
        run: |
          set -euo pipefail
          test -x "$CODEX_SECURITY_BIN"
          "$CODEX_SECURITY_BIN" --version

      - name: Check out the pull request
        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Scan the pull request
        env:
          OPENAI_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          CODEX_SECURITY_STATE_DIR: ${{ runner.temp }}/codex-security-state
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_SHA: ${{ github.event.pull_request.head.sha }}
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
        run: |
          set -euo pipefail
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          "$CODEX_SECURITY_BIN" scan . \
            --diff "$BASE_REVISION" \
            --head "$HEAD_SHA" \
            --auth api-key \
            --output-dir "$SCAN_DIR" \
            --json > "$RUNNER_TEMP/codex-security.json"

      - name: Export SARIF
        id: export-sarif
        if: always()
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
          SARIF_FILE: ${{ runner.temp }}/codex-security.sarif
        run: |
          set -euo pipefail
          if test -f "$SCAN_DIR/scan-manifest.json"; then
            "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
              --export-format sarif \
              --source-root "$GITHUB_WORKSPACE" \
              --output "$SARIF_FILE"
            echo "available=true" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload SARIF
        if: always() && steps.export-sarif.outputs.available == 'true'
        uses: github/codeql-action/upload-sarif@e4fba868fa4b1b91e1fdab776edc8cfbe6e9fb81 # v4
        with:
          sarif_file: ${{ runner.temp }}/codex-security.sarif
          ref: refs/pull/${{ github.event.pull_request.number }}/head
          sha: ${{ github.event.pull_request.head.sha }}
          category: codex-security

      - name: Preserve scan results
        if: always()
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7
        with:
          name: codex-security-results
          path: |
            ${{ runner.temp }}/codex-security-results
            ${{ runner.temp }}/codex-security.json
          if-no-files-found: warn
          retention-days: 7

O fluxo de trabalho faz checkout da revisão head do pull request, calcula a base de mesclagem e
analisa as alterações registradas em commits entre essas revisões. O histórico completo garante que o
alvo seja exato. `persist-credentials: false` impede que o token do repositório seja armazenado na
configuração do Git no checkout. Instalar a CLI antes do checkout e
executá-la pelo caminho absoluto impede que executáveis controlados pelo repositório acessem
a credencial de análise. `--auth api-key` seleciona explicitamente a chave de API de escopo delimitado.
A análise salva seu histórico em um diretório de estado com permissão de gravação fora do
repositório.

`--json` grava um documento JSON completo em stdout, para que o fluxo de trabalho possa salvá-lo
diretamente. O progresso, os resumos de conclusão e os erros permanecem em stderr. Isso
é diferente de `codex exec --json`, que emite um fluxo de eventos JSON Lines.

A etapa de exportação lê uma análise concluída e selada e grava o SARIF. Ela mantém inalterados o
ambiente de execução e as credenciais do Codex. Os artefatos da análise podem conter trechos vulneráveis
do código-fonte, evidências e detalhes de correção. Escolha controles de acesso e um
período de retenção curto adequado ao seu repositório.

## Adicione o pipeline de CI/CD do GitLab

Para um fluxo de trabalho de produção com análises protegidas da branch padrão, análises aprofundadas
agendadas de ativação opcional, bloqueio separado com base na política SARIF e, opcionalmente, merge requests
verificados em rascunho, consulte [Execute o Codex Security no GitLab
CI/CD](/pt-BR/codex/security/cli/ci/gitlab).

O GitLab pode importar
[relatórios SARIF 2.1.0](https://docs.gitlab.com/ci/yaml/artifacts_reports/#artifactsreportssarif)
a partir do GitLab Ultimate 19.2. Adicione uma variável de CI/CD mascarada e oculta chamada
`CODEX_SECURITY_API_KEY` antes de executar o pipeline.

O exemplo mínimo a seguir adiciona um job `security` dedicado apenas à análise ao arquivo
`.gitlab-ci.yml` na raiz. Mantenha no arquivo todos os estágios e jobs existentes. O exemplo analisa
alterações de merge requests por padrão. Defina `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH`
como `"true"` para também analisar toda a branch padrão:

```yaml
variables:
  CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH: "false"

stages:
  - test
  - security

codex-security:
  stage: security
  image: node:26-bookworm-slim
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "diff"
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH && $CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH == "true"'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "full"
  variables:
    GIT_DEPTH: "0"
    CODEX_SECURITY_CLI_DIR: "/tmp/codex-security-cli"
  before_script:
    - |
      set -eu
      apt-get update -qq
      apt-get install -y -qq --no-install-recommends \
        ca-certificates \
        git \
        python3 \
        ripgrep
      npm install \
        --prefix "$CODEX_SECURITY_CLI_DIR" \
        --ignore-scripts \
        --no-audit \
        --no-fund \
        @openai/codex-security@0.1.20

      test -x "$CODEX_SECURITY_BIN"
      "$CODEX_SECURITY_BIN" --version
  script:
    - |
      set -eu
      if test -z "${CODEX_SECURITY_API_KEY:-}"; then
        echo "Set the CODEX_SECURITY_API_KEY CI/CD variable." >&2
        exit 2
      fi

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      case "${CODEX_SECURITY_SCAN_SCOPE:-}" in
        diff)
          BASE_SHA="$CI_MERGE_REQUEST_DIFF_BASE_SHA"
          HEAD_SHA="$CI_COMMIT_SHA"
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          set -- --diff "$BASE_REVISION" --head "$HEAD_SHA"
          echo "Scanning committed changes from $BASE_REVISION to $HEAD_SHA."
          ;;
        full)
          set -- --mode standard
          echo "Scanning the complete default branch at $CI_COMMIT_SHA."
          ;;
        *)
          echo "Unsupported Codex Security scan scope: ${CODEX_SECURITY_SCAN_SCOPE:-unset}" >&2
          exit 2
          ;;
      esac

      SCAN_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      JSON_FILE="/tmp/codex-security-$CI_JOB_ID.json"
      SARIF_FILE="/tmp/codex-security-$CI_JOB_ID.sarif"

      install -d -m 700 "$CODEX_SECURITY_STATE_DIR" "$SCAN_DIR"

      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          "$@" \
          --auth api-key \
          --output-dir "$SCAN_DIR" \
          --json > "$JSON_FILE"
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      install -d -m 700 codex-security-artifacts/results
      cp -R "$SCAN_DIR"/. codex-security-artifacts/results/
      if test -s "$JSON_FILE"; then
        cp "$JSON_FILE" codex-security-artifacts/codex-security.json
      fi
      printf '%s\n' "$scan_exit" > codex-security-artifacts/scan-exit-code.txt

      export_exit=0
      if test -f "$SCAN_DIR/scan-manifest.json"; then
        set +e
        "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
          --export-format sarif \
          --source-root "$CI_PROJECT_DIR" \
          --output "$SARIF_FILE"
        export_exit="$?"
        set -e
        if test -s "$SARIF_FILE"; then
          cp "$SARIF_FILE" codex-security-artifacts/codex-security.sarif
        fi
      fi

      if test "$scan_exit" -ne 0; then
        exit "$scan_exit"
      fi
      exit "$export_exit"
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/codex-security.sarif

Por padrão, o job é executado somente para merge requests de branches do mesmo
projeto, portanto os pipelines de forks não recebem a credencial de análise. Defina
`CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` como `"true"` no nível do grupo, projeto ou
pipeline para também executar uma análise completa padrão na branch padrão. As análises
completas levam mais tempo e custam mais do que as análises de diferenças.

`GIT_DEPTH: "0"` fornece o histórico necessário para calcular a base de mesclagem a partir de
`CI_MERGE_REQUEST_DIFF_BASE_SHA` e `CI_COMMIT_SHA` nas análises de merge requests.

O job instala a CLI em `/tmp`, usa o caminho absoluto para executá-la e expõe a
chave de API somente ao processo de análise. `artifacts: when: always` preserva o relatório
SARIF quando a análise falha, enquanto `artifacts:access: maintainer` limita o acesso
aos resultados detalhados da análise.

Alterações em `.gitlab-ci.yml` podem expor variáveis de CI/CD; por isso, revise as alterações do pipeline
antes de executar o job. Se você
[proteger a variável `CODEX_SECURITY_API_KEY`](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners),
o GitLab a disponibiliza somente para merge requests do mesmo projeto entre
branches protegidas e apenas quando o usuário pode acessar a branch de destino.

O guia específico do GitLab amplia este job mínimo para criar o fluxo de trabalho de produção
disponível no link no início desta seção.

## Escolha uma política de severidade

Os dois exemplos apenas geram relatórios porque omitem `--fail-on-severity`. Quando você
estiver pronto para que os achados afetem o resultado da verificação, adicione um limite ao comando
de análise:

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --fail-on-severity high

Os limites aceitos são `critical`, `high`, `medium` e `low`. Um
limite inclui os achados da análise atual nessa severidade ou em uma superior.
Achados anteriores em aberto exibidos no resumo do repositório não afetam a política.

A etapa de análise usa estes códigos de saída:

| Código de saída  | Significado                                                                                 |
| ----- | --------------------------------------------------------------------------------------- |
| `0`   | A análise foi concluída com cobertura completa, e a política configurada, se houver, foi atendida.            |
| `1`   | A análise concluída contém um achado com severidade igual ou superior ao limite.                        |
| `2`   | A CLI encontrou um erro de entrada ou de execução, ou a análise concluída tem cobertura incompleta. |
| `130` | Ctrl-C interrompeu a análise.                                                            |
| `143` | SIGTERM encerrou a análise.                                                            |

Uma análise com cobertura `partial` ou `unknown` retorna `2`, mesmo sem uma
política de severidade. A CLI ainda grava os achados e os dados de cobertura disponíveis. Revise as
áreas cuja análise foi adiada em `coverage.json` antes de considerar o resultado da verificação conclusivo.

## Tente novamente com um diretório de resultados existente

Use um diretório novo no executor para cada job de CI. Em um executor persistente ou auto-hospedado,
preserve um resultado anterior com `--archive-existing`:

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --archive-existing

O comando arquiva os resultados anteriores e começa com um diretório de análise vazio.

## Solucione problemas de uma análise de CI

- **Referência do Git desconhecida ou diff inesperado:** Busque o histórico das revisões base e head,
  calcule a base de mesclagem e informe explicitamente as duas revisões.
- **Diretório de saída protegido ou não vazio:** Escolha um diretório privado
  fora da árvore de trabalho do Git que contém o diretório de saída. Use `--archive-existing` quando o
  diretório já contiver resultados.
- **Credenciais ausentes:** Confirme se a variável `CODEX_SECURITY_API_KEY` está disponível para
  o fluxo de trabalho ou pipeline confiável e se ela está mapeada diretamente para a variável de ambiente
`OPENAI_API_KEY` do processo de análise.
- **Erro no histórico da análise:** Defina `CODEX_SECURITY_STATE_DIR` com o caminho de um diretório com permissão de gravação
  fora do repositório.
- **Erro na configuração do Python:** Confirme se o executor usa o Python 3.10 ou posterior.
- **Cobertura incompleta:** Revise `coverage.json`, incluindo as superfícies cuja análise foi adiada
  e as questões em aberto, e repita a execução com um alvo ou ambiente adequado.
- **Erro ao exportar o SARIF:** Confirme se a análise foi concluída e se todo o diretório da análise
  está disponível. A exportação valida os artefatos selados antes de gravar o
  SARIF.
- **Erro ao enviar o SARIF:** No GitHub Actions, confirme se sua organização
  ativou o GitHub Code Security para o repositório e se o fluxo de trabalho concede as permissões
`actions: read`, `contents: read` e `security-events: write`. No GitLab
  CI/CD, confirme se o projeto usa o GitLab Ultimate 19.2 ou posterior e se
  o job envia um arquivo SARIF 2.1.0 por meio de `artifacts:reports:sarif`.

Para consultar todos os comandos, sinalizadores, artefatos e campos de saída, veja a [referência da
CLI](/pt-BR/codex/security/cli/reference). Para uma revisão interativa de CI baseada em plug-in,
veja [Revisar alterações no código em busca de problemas de segurança](/pt-BR/codex/security/plugin/code-changes#automate-reviews-in-cicd).

<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/plugin/code-changes -->

Execute uma revisão de segurança das alterações para encontrar regressões em um único conjunto de alterações versionado pelo Git.
O Codex revisa cada arquivo alterado com características de código-fonte e o código que lhe dá suporte direto.
A revisão não se estende a uma auditoria completa do repositório.

Para verificar um repositório inteiro em vez de uma alteração específica, consulte [Executar uma verificação de
segurança](/pt-BR/codex/security/plugin/scans).

## Executar uma revisão manual

No aplicativo para desktop, abra **Segurança**, selecione **Verificações** e, depois, **+ Verificação**.
Escolha o repositório e selecione **Alterações**. Revise alterações sem commit, um
único commit ou revisões base e head. **Verificação aprofundada** não está disponível para uma
verificação de alterações.

Você também pode pedir ao Codex que revise alterações sem commit em uma conversa:

```text
Use $codex-security:security-diff-scan to review my current uncommitted changes for security regressions.

Para um intervalo de commits ou de branches, especifique as duas revisões quando necessário:

```text
Use $codex-security:security-diff-scan to review the changes from origin/main to HEAD for security regressions. Focus on authentication, authorization, input handling, filesystem access, network requests, and secrets.

Você também pode indicar um pull request quando as revisões base e head estiverem disponíveis
no checkout local.

## Confirmar a alteração na configuração

1. Selecione **Alterações**.
2. Confirme o repositório em checkout, a branch atual e o commit mais recente.
3. Em **Alterações para revisão**, escolha:
   - `Uncommitted changes` para a árvore de trabalho atual.
   - O commit mais recente para uma revisão de um único commit.
   - As revisões base e head para um intervalo de branch ou pull request.
4. Confirme se o resumo descreve a alteração que você pretendia revisar.
5. Selecione **Iniciar verificação**.

O Codex não faz checkout de outra branch nem muda a árvore de trabalho selecionada. Se
uma revisão solicitada não estiver disponível localmente, faça o fetch antes da revisão ou
forneça revisões base e head disponíveis localmente.

## Tratar as descobertas

Depois de revisar os resultados, [corrija e verifique uma descoberta
aceita](/pt-BR/codex/security/plugin/fix-findings) ou [exporte e acompanhe as
descobertas](/pt-BR/codex/security/plugin/export-findings).

## Automatizar revisões no CI/CD

Se você tiver acesso à CLI independente em versão beta, consulte [Executar o Codex Security no
CI](/pt-BR/codex/security/cli/ci) para obter JSON estruturado, uma política de gravidade e o upload
de SARIF. Continue nesta seção para invocar a habilidade do plug-in instalado
por meio de `codex exec`.

Execute `$codex-security:security-diff-scan` no CI quando o runner puder invocar a
Codex CLI sem interação. Primeiro, instale a CLI sem expor a credencial da
verificação:

```bash
npm install --global @openai/codex

Instale o Plugin Codex Security na CLI:

```bash
codex plugin add codex-security@openai-curated

O comando de instalação usa o Marketplace público de plug-ins da Codex CLI. Consulte o
[registro de alterações do plug-in](/pt-BR/codex/security/plugin/changelog) antes de depender de uma
versão ou funcionalidade específica do plug-in no CI.

Em seguida, forneça uma chave de API da OpenAI armazenada no cofre de segredos do CI como
`CODEX_SECURITY_API_KEY`. Exponha a credencial somente para a verificação:

```bash
CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
  --sandbox workspace-write \
  "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

O Sandbox gravável permite que a verificação crie artefatos temporários. O prompt
ainda exige que o Codex mantenha inalterado o checkout do código-fonte.

A verificação grava a saída em
`$TMPDIR/codex-security-scans/<repository>/<scan-id>/`:

| Arquivo                 | Conteúdo                                                                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `report.md`          | Principal ponto de entrada legível para todo o diretório da verificação.                                                                                              |
| `findings/<slug>/`   | Relatórios detalhados de vulnerabilidades e arquivos complementares de prova de conceito, quando solicitados.                                                                     |
| `hardening/`         | Orientações para reforço estrutural e propostas complementares, quando solicitadas.                                                                                   |
| `findings.json`      | Descobertas com identificadores estáveis, gravidade, confiança, locais no código-fonte e remediação. Use-as para alimentar fluxos de trabalho internos de segurança aprovados ou ferramentas subsequentes. |
| `scan-manifest.json` | Recibo selado da verificação com o alvo revisado, as revisões e os hashes dos artefatos.                                                                             |
| `coverage.json`      | Superfícies revisadas, superfícies com revisão adiada, exclusões e completude da cobertura.                                                                                    |

O [esquema `findings.json`](https://github.com/openai/plugins/blob/main/plugins/codex-security/schemas/findings.schema.json)
define a estrutura completa. O esquema inclui estes campos:

| Campo                     | Tipo   | Descrição                                                            |
| ------------------------- | ------ | ---------------------------------------------------------------------- |
| `documentType`            | String | Identifica o documento como `codex-security.findings`.                  |
| `schemaVersion`           | String | Identifica a versão do esquema de descobertas.                                |
| `scanId`                  | String | Identifica a verificação que gerou as descobertas.                        |
| `findings`                | Array  | Contém zero ou mais objetos de descoberta.                                 |
| `findings[].findingId`    | String | Identificador estável da descoberta, derivado de sua impressão digital.        |
| `findings[].occurrenceId` | String | Identifica esta ocorrência da descoberta em uma verificação específica.          |
| `findings[].ruleId`       | String | Identifica a família da vulnerabilidade.                                   |
| `findings[].identity`     | Objeto | Contém a âncora semântica e o identificador opcional da instância irmã. |
| `findings[].fingerprints` | Objeto | Contém o algoritmo de impressão digital e a impressão digital principal.            |
| `findings[].title`        | String | Fornece o título curto da descoberta.                                      |
| `findings[].summary`      | String | Resume a vulnerabilidade e seu impacto.                           |
| `findings[].severity`     | Objeto | Contém o nível de severidade e detalhes opcionais de pontuação.              |
| `findings[].confidence`   | Objeto | Contém o nível de confiança e a justificativa.                           |
| `findings[].taxonomy`     | Objeto | Contém a categoria da vulnerabilidade e os identificadores CWE.               |
| `findings[].locations`    | Array  | Lista os arquivos afetados, os números de linha e as funções de cada localização.                |
| `findings[].remediation`  | String | Descreve a correção recomendada.                                         |
| `findings[].provenance`   | Objeto | Identifica a origem da descoberta.                                  |

Por exemplo, este comando imprime uma linha separada por tabulações para cada descoberta:

```bash
jq -r '
  .findings[] |
  [.findingId, .severity.level, .confidence.level, .locations[0].path, .locations[0].startLine, .title] |
  @tsv
' findings.json

Estes exemplos pressupõem um runner Linux confiável com Node.js e `npm`, Git, Python
3, `jq` e as ferramentas de linha de comando do provedor. O prefixo global de pacotes do `npm`
precisa ter permissão de gravação.

Escolha o exemplo correspondente ao seu provedor de CI:

Os resultados da verificação podem incluir detalhes confidenciais sobre vulnerabilidades. Mantenha os artefatos
em sigilo e só publique as descobertas depois de avaliar o público-alvo, o conteúdo e
as aprovações necessárias.

  <div slot="github">

```yaml
name: Codex Security review

on:
  pull_request:

jobs:
  security-review:
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Install Codex Security
        env:
          CODEX_HOME: ${{ runner.temp }}/codex-home
        run: |
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated

      - name: Review code changes
        env:
          CODEX_SECURITY_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_HOME: ${{ runner.temp }}/codex-home
          TMPDIR: ${{ runner.temp }}/codex-security
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_REVISION: ${{ github.event.pull_request.head.sha }}
        run: |
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_REVISION")"
          CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
            --sandbox workspace-write \
            "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: codex-security-review
          path: ${{ runner.temp }}/codex-security/codex-security-scans

  </div>

  <div slot="gitlab">

Crie uma variável de CI/CD mascarada chamada `CODEX_SECURITY_API_KEY` e revise em sigilo os
artefatos da verificação antes de compartilhar as descobertas.

```yaml
codex-security-review:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
  variables:
    GIT_DEPTH: "0"
  script:
    - |
      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
      CODEX_API_KEY="$codex_security_api_key" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
  after_script:
    - |
      unset CODEX_SECURITY_API_KEY
      scan_root="/tmp/codex-security-$CI_JOB_ID/codex-security-scans"
      if [ -d "$scan_root" ]; then
        tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
      fi
  artifacts:
    when: always
    paths:
      - codex-security-artifacts.tar.gz

  </div>

  <div slot="azure">

```yaml
trigger: none

pool:
  vmImage: ubuntu-latest

steps:
  - checkout: self
    fetchDepth: 0

  - bash: |
      set -euo pipefail

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
    displayName: Install Codex Security

  - bash: |
      set -euo pipefail

      CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
    displayName: Review code changes
    condition: and(succeeded(), ne(variables['System.PullRequest.IsFork'], 'True'))
    env:
      CODEX_SECURITY_API_KEY: $(CODEX_SECURITY_API_KEY)

  - publish: $(Agent.TempDirectory)/codex-security/codex-security-scans
    artifact: codex-security-review
    condition: always()

Para o Azure Repos, configure uma política de branch de **Validação de build** para que o
pipeline seja executado em pull requests.

  </div>

  <div slot="jenkins">

```groovy
pipeline {
  agent { label 'linux' }
  stages {
    stage('Codex Security review') {
      when {
        allOf {
          changeRequest()
          expression { !env.CHANGE_FORK?.trim() }
        }
      }
      steps {
        sh '''#!/usr/bin/env bash
          set -euo pipefail

          mkdir -p "$TMPDIR"
          git fetch --no-tags origin "$CHANGE_TARGET"
          target="$(git rev-parse FETCH_HEAD)"
          git fetch --no-tags origin "$CHANGE_BRANCH"
          git rev-parse FETCH_HEAD > "$TMPDIR/head"
          git merge-base "$target" "$(cat "$TMPDIR/head")" > "$TMPDIR/base"
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated
        '''
        withCredentials([string(credentialsId: 'codex-security-api-key', variable: 'CODEX_SECURITY_API_KEY')]) {
          sh '''#!/usr/bin/env bash
            set +x
            set -euo pipefail

            CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
              --sandbox workspace-write \
              "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
          '''
        }
      }
      post {
        always {
          sh '''#!/usr/bin/env bash
            set -euo pipefail
            scan_root="/tmp/codex-security-$BUILD_TAG/codex-security-scans"
            if [ -d "$scan_root" ]; then
              tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
            fi
          '''
          archiveArtifacts artifacts: 'codex-security-artifacts.tar.gz', allowEmptyArchive: true
        }
      }
    }
  }
}

  </div>

Os exemplos ignoram pull requests originados de forks. Execute jobs com credenciais somente a partir de uma
definição de pipeline protegida e apenas para colaboradores confiáveis que tenham acesso à credencial da
verificação. Arquive `codex-security-scans` para manter em um só lugar as descobertas estruturadas,
o manifesto, a cobertura e `report.md`, junto com quaisquer saídas solicitadas de
`findings/` ou `hardening/`. Comece com resultados informativos e analise
a cobertura e o tempo de execução antes de tornar o job uma verificação obrigatória.

Para saber mais sobre o gerenciamento de chaves de API e os controles do Sandbox, consulte [Modo
não interativo](/pt-BR/codex/non-interactive-mode). Se sua organização permitir o uso da [Codex
GitHub Action](/pt-BR/codex/github-action), ela poderá instalar a CLI em tempo de execução, mas
você ainda precisará instalar primeiro o plug-in e fazer a entrada `codex-home`
da ação apontar para o mesmo `CODEX_HOME`.

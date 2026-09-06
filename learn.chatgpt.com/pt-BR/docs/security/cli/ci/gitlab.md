<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/cli/ci/gitlab -->

Execute o Codex Security no GitLab CI/CD para fazer varreduras em alterações registradas em commits e branches
protegidas, publicar achados no GitLab Security e, opcionalmente, propor correções
verificadas em rascunhos de merge requests.

O fluxo de trabalho mantém as credenciais de varredura separadas do acesso de escrita ao repositório.
As alterações geradas sempre exigem revisão humana antes da mesclagem.

Comece apenas com relatórios de varredura. Habilite a remediação somente depois de verificar o
executor, os achados e os limites de acesso das credenciais do seu projeto.

## Antes de começar

Você precisa de:

- Um projeto do GitLab com um executor confiável que ofereça suporte ao espaço de nomes de
usuário do sandbox do Codex.
- A função de Mantenedor ou Proprietário no projeto do GitLab para poder configurar
[variáveis de CI/CD do projeto](https://docs.gitlab.com/ci/variables/) e recursos
  protegidos.
- Uma chave de API da OpenAI com acesso ao Codex Security. Organizações que usam chaves de API da plataforma
  podem [solicitar Trusted Access for
  Cyber](https://openai.com/form/enterprise-trusted-access-for-cyber/).
  Pessoas que usam a autenticação do ChatGPT podem usar o [fluxo pessoal do
  Trusted Access](https://chatgpt.com/cyber). Algumas contas ou repositórios exigem esse
  acesso para varreduras de todo o repositório.
- GitLab Ultimate 19.2 ou posterior para [ingestão de
  SARIF 2.1.0](https://docs.gitlab.com/user/application_security/detect/sarif/).
- O histórico completo do Git para que as tarefas de merge requests possam calcular a base de mesclagem.

A imagem do pipeline instala Node.js 26, Python 3, Git, `rg` e a
CLI do Codex Security na versão fixada. A remediação automatizada também exige um teste
de regressão existente e um executor capaz de executar comandos controlados pelo repositório
sem credenciais protegidas.

## Comece com um pipeline apenas de varredura

Crie uma variável de CI/CD do GitLab mascarada, oculta e protegida chamada
`CODEX_SECURITY_API_KEY`. Use uma chave de API da plataforma da OpenAI com acesso ao Codex Security
e defina seu escopo de ambiente como `codex-security/openai`. Consulte
[variáveis de CI/CD com escopo de ambiente](https://docs.gitlab.com/ci/environments/#limit-the-environment-scope-of-a-cicd-variable).

Primeiro, adicione este pipeline mínimo a um projeto de teste. Ele faz varreduras em alterações registradas em commits
nas merge requests protegidas que atendem aos critérios, publica SARIF a partir de uma tarefa de relatório
bem-sucedida e restaura o resultado da ferramenta de varredura em uma etapa de controle separada:

```yaml
stages:
  - security_scan
  - security_gate

.codex-security-merge-request:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID && $CI_MERGE_REQUEST_SOURCE_BRANCH_PROTECTED == "true" && $CI_MERGE_REQUEST_TARGET_BRANCH_PROTECTED == "true"'

codex-security:
  extends: .codex-security-merge-request
  stage: security_scan
  image: node:26-bookworm-slim
  environment:
    name: codex-security/openai
    action: access
  variables:
    GIT_DEPTH: "0"
  before_script:
    - npm install --prefix /tmp/codex-security-cli --ignore-scripts --no-audit --no-fund @openai/codex-security@0.1.20
  script:
    - |
      set -eu
      test -n "${CODEX_SECURITY_API_KEY:-}"

      CODEX_SECURITY_BIN="/tmp/codex-security-cli/node_modules/.bin/codex-security"
      RESULTS_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      ARTIFACT_DIR="codex-security-artifacts"
      BASE_REVISION="$(git merge-base \
        "$CI_MERGE_REQUEST_DIFF_BASE_SHA" "$CI_COMMIT_SHA")"
      install -d -m 700 "$RESULTS_DIR" "$ARTIFACT_DIR/results"

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY
      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          --diff "$BASE_REVISION" \
          --head "$CI_COMMIT_SHA" \
          --auth api-key \
          --output-dir "$RESULTS_DIR" \
          --json
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      case "$scan_exit" in
        0|1|2) ;;
        *) exit "$scan_exit" ;;
      esac

      "$CODEX_SECURITY_BIN" export "$RESULTS_DIR" \
        --export-format sarif \
        --source-root "$CI_PROJECT_DIR" \
        --output "$ARTIFACT_DIR/results.sarif"
      test -s "$ARTIFACT_DIR/results.sarif"
      cp -R "$RESULTS_DIR"/. "$ARTIFACT_DIR/results/"
      printf '%s\n' "$scan_exit" > "$ARTIFACT_DIR/scan-exit-code.txt"
      exit 0
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/results.sarif

codex-security-gate:
  extends: .codex-security-merge-request
  stage: security_gate
  image: alpine:3.20
  needs:
    - job: codex-security
      artifacts: true
  script:
    - exit "$(cat codex-security-artifacts/scan-exit-code.txt)"

  

Revise todas as alterações em `.gitlab-ci.yml` antes de executar uma tarefa com acesso a segredos.
O exemplo mínimo omite intencionalmente as varreduras completas e a remediação.

## Adote o pipeline de produção

1. [Baixe o pipeline completo do GitLab](/codex/security/cli/ci/gitlab.yml)
   e salve-o como `.gitlab-ci.yml` na raiz do repositório. Se o seu repositório
   já tiver um pipeline, incorpore as etapas, os modelos ocultos e as
   tarefas do exemplo ao arquivo existente.
2. Preserve as etapas existentes de compilação, teste e implantação. Se o projeto usar
`workflow: rules`, confirme que essa configuração permite os eventos de pipeline nos quais você quer executar
   varreduras.

O exemplo adiciona as etapas `security_scan`, `security_remediation`, `security_publish`
e `security_gate`. Para gerar apenas relatórios de varredura, basta configurar
`CODEX_SECURITY_API_KEY`.

Por padrão, a tarefa de varredura é executada apenas em merge requests entre branches
protegidas do mesmo projeto. Defina `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH=true` para executar varreduras
em pushes na branch padrão protegida e em pipelines manuais. Defina
`CODEX_SECURITY_SCHEDULED_DEEP_SCAN=true` e configure limites explícitos de tempo e custo
para habilitar varreduras aprofundadas agendadas na branch padrão protegida.

Um pipeline de merge request só pode acessar variáveis e executores protegidos quando:

- Você protege as branches de origem e de destino no mesmo projeto.
- O projeto [permite que pipelines de merge requests acessem variáveis e
  executores protegidos](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners).
- O usuário que inicia o pipeline pode fazer push ou mesclar alterações na branch de destino.

Pipelines de forks e merge requests não protegidas não recebem a credencial
de varredura. Revise todas as alterações em `.gitlab-ci.yml` antes de executar uma
tarefa com acesso a segredos. Mascarar e ocultar uma variável não torna seguro um código de CI
não confiável.

## Execute uma varredura e revise os achados

Crie uma merge request protegida que atenda aos critérios ou execute o pipeline na
branch padrão protegida. Comece com um diff pequeno antes de executar uma varredura paga
de todo o repositório.

Abra a tarefa `codex-security` e confirme que seus artefatos incluem:

- `scan-manifest.json`
- `findings.json`
- `coverage.json`
- `results.sarif`
- `scan-exit-code.txt`

Em seguida, abra a aba **Segurança** do pipeline, revise os avisos de ingestão e confirme
os identificadores dos achados, os níveis de gravidade e as localizações no código-fonte. As varreduras da branch padrão
também criam registros de vulnerabilidades do projeto. Os achados de merge requests aparecem
na aba Segurança do pipeline ou no widget de segurança da merge request, mas não criam
registros de vulnerabilidades para o projeto como um todo.

Restrinja o acesso aos artefatos, pois os resultados das varreduras podem conter trechos vulneráveis de
código-fonte, evidências e detalhes de remediação.

## Escolha um perfil de varredura

O pipeline seleciona um perfil com base no gatilho:

| Gatilho                                        | Alvo          | Modo       | Esforço  |
| ---------------------------------------------- | --------------- | ---------- | ------- |
| Merge request protegida no mesmo projeto           | Diff registrado em commit  | `standard` | `low`   |
| Push na branch padrão protegida ou execução manual, com habilitação explícita | Repositório inteiro | `standard` | `high`  |
| Agendamento na branch padrão protegida, com habilitação explícita    | Repositório inteiro | `deep`     | `xhigh` |

As varreduras de merge requests concentram o feedback na alteração registrada em commit.
As varreduras da branch padrão revisam o repositório integrado. As varreduras aprofundadas agendadas
oferecem uma cobertura periódica mais ampla. Uma varredura de diff concluída se aplica apenas àquela
alteração e não demonstra que todo o repositório está livre de problemas.

O fluxo de trabalho instala a CLI fora do repositório e a executa pelo caminho
absoluto. Sua verificação prévia em modo de simulação usa a chave de API com escopo restrito ao processo, mas não inicia uma
varredura paga nem verifica a autenticação da API, o acesso ao Codex Security, a cota ou a disponibilidade
do modelo.

O fluxo de trabalho grava o estado e os resultados da varredura fora da árvore de trabalho e restringe
`OPENAI_API_KEY` ao processo de varredura. A CLI recebe um ambiente reduzido e definido explicitamente,
em vez de herdar todas as variáveis do GitLab. Para varreduras de diff, o
fluxo de trabalho calcula a base de mesclagem e vincula a varredura às revisões inicial e
final já revisadas.

O exemplo fixa `@openai/codex-security` na versão `0.1.20`. Teste novamente a autenticação,
os artefatos, a ingestão de SARIF e o controle de política antes de alterar a versão fixada.

## Separe a geração de relatórios da aplicação da política

O GitLab ingere SARIF a partir de uma tarefa de relatório bem-sucedida. O pipeline publica o
relatório primeiro e restaura o status de saída da ferramenta de varredura em uma tarefa separada,
`codex-security-gate`.

A tarefa de relatório aceita achados com os códigos de saída `0` e `1`. Ela aceita o código de saída
`2` somente quando o manifesto da varredura comprova que ela foi concluída, a cobertura é
explicitamente `partial` e existe um relatório SARIF não vazio. Outras falhas de execução,
configuração ou exportação continuam bloqueando o pipeline.

A etapa de controle final preserva estes códigos de saída da ferramenta de varredura:

| Saída | Significado                                                                     |
| ---- | --------------------------------------------------------------------------- |
| `0`  | A análise foi concluída com cobertura completa e atendeu à política.            |
| `1`  | A análise foi concluída e encontrou um problema com gravidade igual ou superior ao limite configurado. |
| `2`  | A análise teve cobertura incompleta ou um erro de entrada ou de execução.              |

O exemplo permite temporariamente o código de saída `2` enquanto você calibra a cobertura parcial.
Remova essa permissão quando a cobertura incompleta precisar bloquear o pipeline.

A remediação e a publicação são executadas antes da etapa final de validação da política. Um achado elegível
pode gerar um rascunho verificado de solicitação de mesclagem mesmo que essa etapa
faça o pipeline falhar posteriormente.

## Ative a remediação verificada

A remediação automatizada é opcional e só é executada em pipelines da branch padrão
protegida. O processo de remediação do Codex e os comandos de verificação
controlados pelo repositório não recebem o token de acesso do projeto GitLab nem
as credenciais injetadas pelo executor.

O contrato de segurança tem três partes: comandos controlados pelo repositório nunca
recebem credenciais da OpenAI ou do GitLab; somente a tarefa de publicação recebe
acesso de escrita ao repositório; e toda alteração gerada permanece como rascunho até
que uma pessoa a revise e faça a mesclagem.

O fluxo de trabalho:

1. Exige cobertura completa da análise e um achado com gravidade
   `high` ou `critical`.
2. Confirma que o teste de regressão configurado falha antes da aplicação do patch.
3. Gera um patch focado e rejeita alterações em arquivos de CI, de credenciais, binários ou
outros arquivos protegidos.
4. Executa o teste de regressão sem credenciais da OpenAI, do GitLab, do registro, de implantação ou
de token de tarefa.
5. Usa `verify-fix` para retornar `fixed`, `still_vulnerable` ou `inconclusive`.
   A tarefa publica um patch somente quando `verify-fix` retorna `fixed` e o
   processo de verificação mantém o patch inalterado.

Defina estas variáveis protegidas para ativar a remediação:

- Defina `CODEX_SECURITY_ENABLE_REMEDIATION` como `true`.
- Defina `CODEX_SECURITY_VERIFICATION_COMMAND` com um teste de regressão existente que
  termine com o código de saída `1` antes da correção e `0` depois.
- Opcionalmente, defina `CODEX_SECURITY_SETUP_COMMAND` com um comando não interativo
  de configuração de dependências.

Escolha um teste de regressão que exercite a propriedade de segurança que deve ser preservada, não
uma implementação específica. Revise com o mesmo rigor as alterações geradas nos testes e
no código-fonte.

<details>
  <summary>Avançado: isolamento de comandos do repositório</summary>

Os comandos `validate`, `patch` e `verify-fix` recebem uma
`CODEX_API_KEY` com escopo restrito ao processo. Os comandos de configuração e teste controlados pelo repositório são executados como
outro usuário, sem privilégios, em uma cópia com permissão de escrita dos arquivos-fonte rastreados.
A cópia exclui intencionalmente os metadados do Git, o conteúdo dos submódulos e
os artefatos baixados. Comandos de configuração e teste que exigem `.git` ou
submódulos devem ser executados em uma tarefa separada, projetada para operar sem credenciais.

Somente as etapas do Codex sob controle do usuário root podem acessar a cópia de trabalho canônica ou o
diretório adjacente de variáveis do tipo arquivo do GitLab. O ambiente limpo da cópia contém apenas
`PATH`, `HOME`, `LANG`, `CI` e `CI_PROJECT_DIR`. Se um comando precisar de outro
valor não secreto, adicione-o à lista de permissões depois de revisar o comando. Se o
executor não puder alternar entre usuários, mova a verificação para uma tarefa separada,
sem credenciais, antes de ativar a remediação.

</details>

## Publique um rascunho de solicitação de mesclagem

Crie um [token de acesso de projeto
do GitLab](https://docs.gitlab.com/user/project/settings/project_access_tokens/#create-a-project-access-token)
com a função Desenvolvedor e os escopos `api` e `write_repository`. Armazene-o na variável
`GITLAB_REMEDIATION_TOKEN`, protegida, mascarada e oculta, com escopo restrito ao
ambiente `codex-security/publish`.

Defina `CODEX_SECURITY_CREATE_MR=true` para ativar a publicação. Defina também a variável não secreta
`CODEX_SECURITY_MR_TEST_COMMAND` com o teste de regressão de segurança específico do projeto
que toda branch de remediação gerada deve executar com sucesso. Mantenha essa variável
desprotegida para que a solicitação de mesclagem desprotegida gerada possa ler o comando.
O fluxo de publicação:

- Recebe o token de escrita no repositório, mas nenhuma credencial da OpenAI.
- Cria uma branch `codex-security/fix-<finding-hash>`.
- Abre um rascunho de solicitação de mesclagem e reutiliza um rascunho já aberto em vez de
criar uma duplicata.
- Executa o teste de regressão da branch de remediação desprotegida como um usuário sem privilégios,
em uma cópia que contém apenas arquivos rastreados, sem credenciais protegidas.
- Nunca faz a mesclagem da alteração gerada automaticamente.

Não use `CI_JOB_TOKEN` no lugar do token de acesso do projeto. Ele não permite executar
a operação necessária para criar a solicitação de mesclagem. Revise o patch proposto,
as evidências de verificação e o achado antes de fazer a mesclagem.

## Configure variáveis opcionais

Configure apenas as variáveis necessárias para os recursos que você ativar:

| Variável                                  | Quando é necessária                       | Valor padrão ou finalidade                                          |
| ----------------------------------------- | --------------------------------- | ----------------------------------------------------------- |
| `CODEX_SECURITY_API_KEY`                  | Todas as análises                        | Protegida, mascarada e oculta; restrinja o escopo a `codex-security/openai` |
| `CODEX_SECURITY_VERSION`                  | Atualização da CLI                       | Fixada em `0.1.20`; teste novamente antes de alterar                  |
| `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` | Análises completas da branch padrão         | Ativação explícita; desativado por padrão                             |
| `CODEX_SECURITY_SCHEDULED_DEEP_SCAN`      | Análises aprofundadas agendadas              | Ativação explícita; desativado por padrão                             |
| `CODEX_SECURITY_DEEP_MAX_TIME_HOURS`      | Análises aprofundadas agendadas              | Limite de tempo obrigatório, maior que `0` e menor que `8`     |
| `CODEX_SECURITY_DEEP_MAX_COST`            | Análises aprofundadas agendadas              | Limite obrigatório para o custo estimado em USD, maior que `0`      |
| `CODEX_SECURITY_ENABLE_REMEDIATION`       | Geração de patches                  | Ativação por variável protegida; desativado por padrão                            |
| `CODEX_SECURITY_VERIFICATION_COMMAND`     | Geração de patches                  | Teste de regressão protegido                                   |
| `CODEX_SECURITY_SETUP_COMMAND`            | Configuração opcional da remediação        | Instalação de dependências protegida                           |
| `CODEX_SECURITY_REMEDIATION_EFFORT`       | Ajuste opcional da remediação       | `high`                                                      |
| `CODEX_SECURITY_MAX_CHANGED_FILES`        | Limite opcional de tamanho do patch         | `8`; intervalo permitido de `1` a `20`                         |
| `CODEX_SECURITY_CREATE_MR`                | Criação de rascunho de solicitação de mesclagem      | Ativação por variável protegida; desativado por padrão                            |
| `GITLAB_REMEDIATION_TOKEN`                | Criação de rascunho de solicitação de mesclagem      | Token de projeto com a função Desenvolvedor e escopo restrito a `codex-security/publish`  |
| `CODEX_SECURITY_GITLAB_INTERNAL_URL`      | Publicação opcional em instância com hospedagem própria   | Origem do GitLab acessível pelo executor                     |
| `CODEX_SECURITY_MR_TEST_COMMAND`          | Publicação de solicitações de mesclagem em rascunho    | Teste de regressão obrigatório, não sigiloso e específico do projeto       |
| `CODEX_SECURITY_MR_SETUP_COMMAND`         | Configuração opcional da branch de correção | Configuração não sigilosa de dependências                                 |

O GitLab fornece as variáveis `CI_*`. O pipeline gerencia
`CODEX_SECURITY_BIN`, `CODEX_SECURITY_EFFORT`, `CODEX_SECURITY_MODE`,
`CODEX_SECURITY_STATE_DIR` e `CODEX_SECURITY_TARGET`; não as configure
como variáveis do projeto. Nas varreduras de diferenças, a CLI deriva a identidade canônica do alvo
das revisões normalizadas de base e de ponta.

## Ajuste a aplicação de políticas e o custo

Use varreduras focadas nas diferenças para dar retorno sobre solicitações de mesclagem, varreduras padrão do repositório
para a branch padrão e varreduras aprofundadas agendadas para uma cobertura mais ampla. Os dois
perfis de varredura do repositório completo ficam desativados por padrão. Uma varredura aprofundada agendada também exige
`CODEX_SECURITY_DEEP_MAX_TIME_HOURS` e `CODEX_SECURITY_DEEP_MAX_COST`; mantenha o
limite de tempo da CLI abaixo do tempo limite de oito horas da tarefa. Meça execuções representativas
antes de definir um orçamento. Trate `--max-cost` como um limite de custo estimado, não como
um teto rígido de cobrança.

Comece com varreduras que apenas geram relatórios. Adicione `--fail-on-severity` depois que sua equipe tiver
revisado achados representativos, cobertura, custo e tempo de execução. Consulte [Execute o Codex Security
em CI](/pt-BR/codex/security/cli/ci) para ver as políticas de gravidade e os detalhes dos
códigos de saída.

Quando uma tarefa falhar:

- A ausência de artefatos da varredura indica um problema de configuração ou no executor.
- Se houver artefatos com cobertura parcial, revise `coverage.json`.
- Se os achados não aparecerem no GitLab, verifique se a tarefa de relatório SARIF
foi concluída com sucesso e se o GitLab aceitou o relatório.
- Se a correção for ignorada, verifique a branch protegida, a cobertura
completa, a gravidade do achado, o comando de verificação e as variáveis de ativação.
- Em caso de erros de publicação, verifique a função, os escopos e a
restrição de ambiente do token do projeto.

Para informações sobre todos os comandos, opções e artefatos, consulte a [referência da
CLI do Codex Security](/pt-BR/codex/security/cli/reference).

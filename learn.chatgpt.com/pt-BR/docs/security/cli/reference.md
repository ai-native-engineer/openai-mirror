<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/cli/reference -->

Use esta referência para consultar os comandos `codex-security`, as flags,
os formatos de saída compatíveis e o comportamento de encerramento. Para realizar uma primeira varredura guiada, comece pelo
[início rápido da CLI](/pt-BR/codex/security/cli).

  O pacote `@openai/codex-security` é público. Para executar varreduras, é necessário ter acesso ao Codex
  Security. As varreduras usam suas permissões locais e não são interrompidas para solicitar
  aprovação. Antes de começar, consulte [Permissões para varreduras
  locais](#local-scan-permissions).

Execute a CLI com `npx @openai/codex-security`.

## Visão geral dos comandos

```text
usage: codex-security [--version] <command> [options]

A CLI oferece estes comandos:

| Comando                       | Finalidade                                               |
| ----------------------------- | ----------------------------------------------------- |
| `codex-security scan`         | Executar uma varredura do Codex Security.                            |
| `codex-security install-hook` | Instalar uma varredura de segurança pré-commit do Git.               |
| `codex-security bulk-scan`    | Descobrir repositórios e executar varreduras em massa que podem ser retomadas.   |
| `codex-security scans`        | Listar, inspecionar, comparar e recuperar logs de varredura salvos. |
| `codex-security findings`     | Revisar e atualizar achados de segurança salvos.            |
| `codex-security export`       | Exportar achados concluídos como CSV, JSON ou SARIF.     |
| `codex-security publish`      | Publicar no Linear os achados de varreduras concluídas.            |
| `codex-security validate`     | Verificar um ou mais possíveis achados de segurança.        |
| `codex-security patch`        | Aplicar patches a um ou mais problemas de segurança.                    |
| `codex-security login`        | Fazer login, armazenar credenciais ou verificar o status do login.  |
| `codex-security logout`       | Remover o login armazenado.                            |
| `codex-security info`         | Exibir metadados somente leitura do SDK e do plug-in incluído.       |

A CLI também oferece estes comandos de integração:

| Comando                      | Finalidade                               |
| ---------------------------- | ------------------------------------- |
| `codex-security completions` | Gerar scripts de preenchimento automático do shell.    |
| `codex-security mcp`         | Registrar a CLI como um servidor MCP.    |
| `codex-security skills`      | Sincronizar as habilidades do Codex Security com os agentes. |

Liste todos os comandos disponíveis:

```bash
npx @openai/codex-security --help

Adicione `--help` a um comando para inspecionar seus argumentos e opções:

```bash
npx @openai/codex-security scan --help

`codex-security --version` exibe a versão instalada e encerra a execução.
`codex-security info --json` informa as versões do SDK e do plug-in incluído.
Nenhum desses comandos requer Python.

### Descobrir comandos e conectar agentes

Exiba o manifesto de comandos em formato legível por agentes:

```bash
npx @openai/codex-security --llms

Inspecione o esquema dos argumentos da varredura em JSON:

```bash
npx @openai/codex-security scan --schema --format json

Gere o preenchimento automático do shell para Bash:

```bash
npx @openai/codex-security completions bash

Substitua `bash` por `zsh` ou `fish` para esses shells.

Os resultados da varredura aceitam `--format toon|json|yaml|jsonl` e `--full-output`. Essa
opção `--format`, no nível do framework, é diferente de `--export-format`, que seleciona
o formato de um artefato exportado de uma varredura concluída. A ajuda global dos comandos
também lista `md`, mas os resultados da varredura não aceitam saída em Markdown.

Registre a CLI como um servidor MCP:

```bash
npx @openai/codex-security mcp add

Sincronize as habilidades do Codex Security com seus agentes:

```bash
npx @openai/codex-security skills add

O MCP disponibiliza apenas o comando de metadados somente leitura `info`. Varreduras, exportações,
autenticação, validação e aplicação de patches continuam restritas à CLI.

## `codex-security scan`

Execute uma varredura em um repositório, em caminhos selecionados, em alterações registradas em commits ou na
árvore de trabalho.

```text
usage: codex-security scan [-h] [--auth {auto,chatgpt,api-key}]
                           [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                           [--path PATH | --diff BASE | --working-tree]
                           [--head HEAD] [--base BASE]
                           [--knowledge-base PATH] [--scan-prompt-file FILE]
                           [--post-scan-prompt-file FILE]
                           [--mode {standard,deep}] [--workers N]
                           [--subagents N] [--stop-after-no-new N]
                           [--max-discovery-runs N] [--max-time-hours HOURS]
                           [--model MODEL]
                           [--effort {minimal,low,medium,high,xhigh,max}]
                           [--output-dir DIR]
                           [--archive-existing]
                           [--plugin-path PATH] [--python PATH]
                           [--codex KEY=VALUE] [--fail-on-severity LEVEL]
                           [--patch] [--patch-severity {critical,high,medium,low}]
                           [--create-pr]
                           [--max-cost USD] [--dry-run] [--headless] [--verbose]
                           [--json] [--format {toon,json,yaml,jsonl}]
                           [--full-output] [repository]

Por padrão, `repository` é o diretório atual.

### Selecionar a autenticação da varredura

Use `--auth auto`, a opção padrão, para selecionar as credenciais automaticamente. Quando houver
um login no ChatGPT e também `OPENAI_API_KEY` ou `CODEX_API_KEY`,
as varreduras interativas com saída de texto perguntam qual credencial usar. Varreduras em CI, com saída JSON ou
JSONL, e outras varreduras sem um terminal interativo usam a
chave de API do ambiente. As execuções simuladas não solicitam nem carregam credenciais.

Para usar suas credenciais armazenadas, passe `--auth chatgpt`:

```bash
npx @openai/codex-security scan . --auth chatgpt

Para usar uma chave de API do ambiente, passe `--auth api-key`:

```bash
npx @openai/codex-security scan . --auth api-key

Para tornar as credenciais armazenadas o padrão automático, execute
`unset OPENAI_API_KEY CODEX_API_KEY`.

### Usar o OpenRouter ou o Fireworks

Selecione o OpenRouter com a respectiva chave de API e um modelo explícito:

```bash

npx @openai/codex-security scan . \
  --provider openrouter \
  --model anthropic/claude-sonnet-4.5

Selecione o Fireworks com a respectiva chave de API e um modelo explícito:

```bash

npx @openai/codex-security scan . \
  --provider fireworks \
  --model accounts/fireworks/models/qwen3-235b-a22b

Ambos os provedores também aceitam `bulk-scan`.

### Usar o Amazon Bedrock

Selecione o Amazon Bedrock com `--provider amazon-bedrock` e especifique explicitamente um
modelo do Bedrock com `--model`:

```bash
npx @openai/codex-security scan . \
  --provider amazon-bedrock \
  --model openai.gpt-5.6-sol

Defina `AWS_REGION` e autentique-se com `AWS_BEARER_TOKEN_BEDROCK`, chaves de acesso padrão da
AWS, um perfil da AWS, identidade da Web, credenciais de contêiner ou a
cadeia padrão de credenciais da AWS. As varreduras do Bedrock usam credenciais da AWS em vez de
`--auth`, de um login no ChatGPT ou de uma chave de API da OpenAI. Tanto `scan` quanto `bulk-scan`
aceitam `--provider`.

### Selecionar o alvo da varredura

Escolha um tipo de alvo para cada varredura.

| Argumento                 | Descrição                                                                     |
| ------------------------ | ------------------------------------------------------------------------------- |
| `--path PATH`            | Faça a varredura de um caminho relativo ao repositório. Repita a flag para adicionar mais caminhos.         |
| `--diff BASE`            | Faça a varredura das alterações registradas em commits de `BASE` até `--head`. Por padrão, a revisão de destino é `HEAD`.    |
| `--head HEAD`            | Defina a revisão de destino para `--diff`.                                             |
| `--working-tree`         | Faça a varredura das alterações preparadas e não preparadas em relação a `--base`. Por padrão, a revisão de base é `HEAD`. |
| `--base BASE`            | Defina a revisão de base para `--working-tree`.                                     |
| `--mode {standard,deep}` | Selecione o modo de varredura. O padrão é `standard`.                                |

`--path`, `--diff` e `--working-tree` são mutuamente exclusivos. `--head`
requer `--diff`, e `--base` requer `--working-tree`. O modo aprofundado é compatível com
alvos de repositório e de caminho.

As verificações de diferenças e da árvore de trabalho exigem que o argumento do repositório seja a raiz da
árvore de trabalho do Git. As referências selecionadas devem existir nesse checkout.

Verifique todo o repositório:

```bash
npx @openai/codex-security scan .

Verifique os caminhos selecionados:

```bash
npx @openai/codex-security scan . --path src --path tests

Verifique as alterações registradas em commits:

```bash
npx @openai/codex-security scan . --diff origin/main --head HEAD

Verifique as alterações preparadas e não preparadas:

```bash
npx @openai/codex-security scan . --working-tree --base HEAD

Faça uma revisão mais aprofundada do repositório:

```bash
npx @openai/codex-security scan . --mode deep

### Configurar verificações aprofundadas

Use estas opções com `--mode deep` para controlar a simultaneidade e o tempo de execução dos processos:

| Argumento                 | Descrição                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- |
| `--workers N`            | Limite de processos independentes de verificação padrão executados simultaneamente. O padrão é `4`.                |
| `--subagents N`          | Subagentes disponíveis para cada processo. O padrão é `3`.                                   |
| `--stop-after-no-new N`  | Interrompa depois que `N` verificações consecutivas concluídas pelos processos não encontrarem novos problemas. O padrão é `4`. |
| `--max-discovery-runs N` | Limite do número total de execuções independentes de verificações padrão. O padrão é `40`.                       |
| `--max-time-hours HOURS` | Limite de tempo de execução dos processos, em horas. O padrão é `96`; aceita valores fracionários.             |

`--subagents` aceita zero ou um número inteiro positivo. `--max-time-hours` aceita um
número positivo menor ou igual a `96`. As demais opções exigem um número inteiro
positivo. Essas opções não estão disponíveis em verificações padrão.

Por exemplo, use dois processos, permita até dez execuções e interrompa a execução dos processos
após 1,5 hora:

```bash
npx @openai/codex-security scan . \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

Quando o limite de tempo expira, a verificação interrompe os processos ainda em execução, preserva os resultados das
verificações concluídas e os consolida no relatório final. Se nenhum processo concluir a
revisão do código-fonte, a verificação registra cobertura parcial e retorna o código de saída `2`.

Defina valores padrão persistentes em `~/.codex/codex-security/config.toml` ou em
`$CODEX_HOME/codex-security/config.toml` quando definir `CODEX_HOME`:

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

As opções de linha de comando substituem esses valores padrão. `scan --workers` controla
os processos independentes de verificação padrão em uma única verificação aprofundada; `bulk-scan --workers`
controla as verificações simultâneas de repositórios. Defina `stop_after_consecutive_errors` somente
no arquivo TOML; o valor padrão é `3`.

### Adicionar contexto de segurança

Use `--knowledge-base PATH` para fornecer documentos de arquitetura, modelos de ameaças
ou políticas de segurança. Repita a opção para adicionar mais arquivos ou diretórios:

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Os documentos aceitos incluem arquivos `.md`, `.markdown`, `.txt`, `.pdf` e `.docx`.
A CLI pesquisa diretórios recursivamente, rejeita caminhos de entrada que sejam links simbólicos,
ignora entradas de diretório que sejam links simbólicos e mantém o conteúdo extraído dos documentos
fora dos resultados salvos da verificação.

### Adicionar instruções de verificação

Para adicionar instruções de verificação, forneça um arquivo de texto ou Markdown com
`--scan-prompt-file`. Use `--post-scan-prompt-file` para executar instruções complementares
na mesma sessão autenticada após verificações bem-sucedidas e
verificações com cobertura incompleta ou erros:

```bash
npx @openai/codex-security scan . \
  --scan-prompt-file security-focus.md \
  --post-scan-prompt-file follow-up.md

Por exemplo, use o prompt da verificação para se concentrar nos limites de autorização e solicite
que as instruções complementares gravem um novo `post-scan-summary.md` no diretório da verificação.
Se essas instruções falharem, a CLI exibe um aviso e preserva a verificação concluída.
As instruções complementares não são executadas após um cancelamento nem quando a verificação atinge seu
limite de custo.

### Definir opções de saída e política

Use estas opções para manter os artefatos, preservar resultados anteriores ou criar um
resultado legível por máquina.

| Argumento                   | Descrição                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `--output-dir DIR`         | Grave os artefatos da verificação em um diretório privado, fora da árvore de trabalho correspondente do Git. O padrão é o estado persistente do Codex Security. |
| `--archive-existing`       | Mova os resultados existentes para `DIR.previous-<timestamp>-<id>` e comece com um diretório de saída vazio. Requer `--output-dir`.  |
| `--fail-on-severity LEVEL` | Retorne o código de saída `1` quando uma verificação concluída relatar um achado de severidade igual ou superior a `critical`, `high`, `medium` ou `low`.                  |
| `--patch`                  | Corrija e verifique os achados selecionados após uma verificação completa.                                                                      |
| `--patch-severity LEVEL`   | Corrija achados com severidade igual ou superior a `critical`, `high`, `medium` ou `low`. O padrão é `low`.                                        |
| `--create-pr`              | Faça commit dos arquivos de correção verificados e abra um pull request no GitHub. Requer `--patch`.                                              |
| `--max-cost USD`           | Interrompa uma verificação quando o custo estimado do modelo ultrapassar o valor especificado em USD.                                                  |
| `--dry-run`                | Verifique o repositório, o alvo, a base de conhecimento, o diretório de saída e a configuração do Codex sem iniciar uma verificação.             |
| `--headless`               | Exiba o progresso em texto simples em vez do painel interativo da verificação.                                                          |
| `--verbose`                | Imprima em stderr diagnósticos sobre ciclo de vida, autenticação, progresso e custo com informações confidenciais ocultadas.                                          |
| `--json`                   | Imprima o manifesto, os achados, a cobertura, os caminhos e os metadados dos turnos como um único documento JSON.                                           |
| `--format FORMAT`          | Imprima o resultado completo da verificação como `toon`, `json`, `yaml` ou `jsonl`.                                                        |
| `--full-output`            | Imprima o resultado completo usando o formato padrão de saída estruturada.                                                        |

O limite de custo é uma estimativa, não um teto rígido de gastos. Solicitações já em
andamento podem ser concluídas um pouco acima do limite. Se uma verificação aprofundada atingir o limite
depois que o Codex Security consolidar os resultados dos processos concluídos, a CLI sela os
resultados disponíveis, marca a cobertura como `partial` e retorna o código de saída `2`.
Caso contrário, retorna `2` e mantém no disco qualquer saída parcial disponível.

Quando você omite `--output-dir`, os resultados ficam armazenados em
`$CODEX_HOME/state/plugins/codex-security/scans/<repository>`. O valor padrão de `CODEX_HOME`
é `~/.codex`. Defina `CODEX_SECURITY_STATE_DIR` para armazenar os resultados em
`$CODEX_SECURITY_STATE_DIR/scans/<repository>` em vez do local padrão. Esses diretórios podem
conter trechos de código-fonte e detalhes de vulnerabilidades; portanto, gerencie as permissões
e a retenção desses diretórios adequadamente.

O ambiente de análise mantém o histórico de verificações em
`$CODEX_HOME/state/plugins/codex-security/workbench.sqlite3`. Definir
`CODEX_SECURITY_STATE_DIR` também move o banco de dados do ambiente de análise.

O diretório de saída deve ficar fora do diretório verificado e de qualquer
árvore de trabalho do Git que o contenha. Uma verificação pode substituir um diretório de resultados existente com
`--archive-existing`.

Para preservar os resultados anteriores antes de reutilizar um diretório de saída:

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --archive-existing

Por padrão, as verificações apenas geram relatórios. Adicione `--fail-on-severity` para avaliar uma
política de severidade na CI:

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --json \
  --fail-on-severity high \
  > /path/outside/repository/codex-security.json

Uma execução simulada verifica as entradas locais, incluindo os documentos da base de conhecimento, sem
carregar credenciais, iniciar o Codex nem testar o interpretador Python
do plug-in:

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --dry-run

### Configurar o ambiente de execução

Use as opções do ambiente de execução quando precisar especificar um modelo, interpretador, plug-in ou
valor de configuração do Codex.

| Argumento                                                  | Descrição                                                                                              |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `--auth {auto,chatgpt,api-key}`                           | Selecione as credenciais da verificação. O padrão é `auto`.                                                      |
| `--provider {openai,openrouter,fireworks,amazon-bedrock}` | Selecione o provedor de inferência. O padrão é `openai`.                                                  |
| `--model MODEL`                                           | Selecione o modelo. O padrão é `gpt-5.6-sol`. É necessário especificar um modelo para OpenRouter, Fireworks e Amazon Bedrock.  |
| `--effort {minimal,low,medium,high,xhigh,max}`            | Selecione o esforço de raciocínio do modelo. O padrão é `xhigh`.                                             |
| `--plugin-path PATH`                                      | Use um diretório ou arquivo ZIP do Plugin Codex Security para substituir o plug-in incluído.                             |
| `--python PATH`                                           | Selecione o interpretador Python para o ambiente de execução do plug-in.                                                    |
| `--codex KEY=VALUE`                                       | Substitua um valor da configuração isolada do Codex. Os valores seguem a sintaxe TOML. Repita a opção para especificar mais valores. |

Para selecionar outro modelo e outro esforço de raciocínio sem escrever TOML:

```bash
npx @openai/codex-security scan . --model gpt-5.6-terra --effort high

Coloque entre aspas os valores de string passados por meio de `--codex` para que o analisador TOML receba uma
string:

```bash
npx @openai/codex-security scan . --codex 'model="gpt-5.6-terra"'

## `codex-security install-hook`

Instale no repositório atual uma verificação de segurança pre-commit do Git:

```bash
npx @openai/codex-security install-hook

A verificação analisa as alterações preparadas e não preparadas antes de cada commit e impede o commit em caso de
achados de alta gravidade ou erros de verificação. Ela respeita `core.hooksPath` e
não substitui um script de pré-commit existente. Defina outro limite de gravidade
quando necessário:

```bash
npx @openai/codex-security install-hook . --fail-on-severity medium

## `codex-security bulk-scan`

Descubra e verifique repositórios do GitHub ou execute uma verificação que pode ser retomada a partir de um
CSV de repositórios:

Para um guia completo sobre a descoberta de repositórios no GitHub, inventários em CSV, resultados de campanhas
e verificações em contêineres, consulte [Executar verificações de segurança
em lote](/pt-BR/codex/security/cli/bulk-scans).

```text
usage: codex-security bulk-scan [input] [--output-dir DIR]
                                [--workers N] [--mode {standard,deep}]
                                [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                                [--model MODEL]
                                [--effort {minimal,low,medium,high,xhigh,max}]
                                [--knowledge-base PATH]
                                [--scan-prompt-file FILE]
                                [--post-scan-prompt-file FILE]
                                [--max-attempts N] [--plugin-path PATH]
                                [--python PATH] [--codex KEY=VALUE]

Execute `npx @openai/codex-security bulk-scan` sem argumentos para selecionar
repositórios interativamente. Este fluxo requer login na GitHub CLI.

Para escolher um modelo e o esforço de raciocínio durante a descoberta interativa:

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

Para usar uma lista de repositórios já preparada, forneça um CSV e `--output-dir`:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

O CSV exige as colunas `id`, `repository` e `revision`. As revisões devem ser
hashes completos de commit. As colunas opcionais `scope`, `mode` e `prompt` configuram
repositórios individuais:

```csv
id,repository,revision,scope,mode,prompt
service,https://github.com/example/service.git,0123456789abcdef0123456789abcdef01234567,src,standard,Review authorization boundaries.

Use `--knowledge-base PATH` para compartilhar documentos de segurança entre todos os
repositórios. Use `--scan-prompt-file FILE` para adicionar instruções de verificação compartilhadas; a
coluna `prompt` do CSV adiciona instruções específicas de cada repositório após esse
prompt compartilhado. `--post-scan-prompt-file FILE` executa instruções de acompanhamento após cada
verificação, inclusive verificações com cobertura incompleta ou erros. Essas instruções não são executadas após
um cancelamento ou quando uma verificação atinge seu limite de custo.

`--workers` limita as verificações simultâneas de repositórios e tem `4` como valor padrão. `--mode`
tem `standard` como valor padrão, e `--max-attempts` tem `1` como valor padrão. Defina
`--max-attempts` para tentar novamente em caso de erros no repositório ou na verificação. Verificações concluídas com
cobertura incompleta não são repetidas. Seus resultados permanecem disponíveis, e o
comando retorna o código de saída `2`.

Execute o mesmo comando novamente para retomar a partir de um diretório de saída existente. A CLI
ignora verificações concluídas, inclusive aquelas com cobertura incompleta.

Para campanhas em contêineres, consulte [Executar verificações em lote no
Docker](/pt-BR/codex/security/cli/bulk-scans#run-bulk-scans-in-docker).

## `codex-security scans`

### Localizar verificações salvas

Liste as verificações salvas do diretório atual:

```bash
npx @openai/codex-security scans

Liste as verificações de outro repositório:

```bash
npx @openai/codex-security scans list /path/to/repository

Localize verificações armazenadas em um diretório de saída específico:

```bash
npx @openai/codex-security scans list --scan-root /path/outside/repository/results

### Inspecionar ou repetir uma verificação

Exiba os resultados e a configuração de uma verificação salva:

```bash
npx @openai/codex-security scans show SCAN_ID

Adicione `--show-linked-findings` para incluir links para achados de verificações anteriores.

Execute novamente a verificação no checkout atual usando sua configuração original:

```bash
npx @openai/codex-security scans rerun SCAN_ID

A nova execução exige a versão do plug-in registrada pela verificação original. Se a
versão instalada for diferente, o comando é interrompido em vez de ser executado com um
plug-in diferente.

### Inspecionar logs salvos de verificações

Leia todos os eventos de sessão salvos de uma verificação e de seus executores. Esses logs
não têm dados sensíveis ocultados e podem conter código-fonte ou credenciais; portanto, revise-os
antes de compartilhá-los:

```bash
npx @openai/codex-security scans logs SCAN_ID

Adicione `--json` para obter um resultado legível por máquina com todas as informações.

### Associar e comparar achados

Compare duas verificações para identificar achados novos, persistentes, reabertos, resolvidos e
desconhecidos:

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

A comparação associa automaticamente achados que têm a mesma causa raiz
e reutiliza associações salvas. Para salvar associações explicitamente, use `scans match`:

```bash
npx @openai/codex-security scans match PREVIOUS_SCAN_ID CURRENT_SCAN_ID

Um achado é classificado como desconhecido quando a verificação posterior tem cobertura incompleta ou não
abrange o local original do achado. Adicione `--force` ao comando `match` quando precisar
recalcular uma associação existente.

Para associar todas as verificações concluídas do repositório atual, incluindo as de
outros checkouts:

```bash
npx @openai/codex-security scans match --all

Os resultados das verificações podem variar mesmo quando você executa novamente a mesma configuração. A associação e
a comparação acompanham as mudanças; elas não tornam os resultados determinísticos nem comprovam que uma
vulnerabilidade deixou de existir. Use `validate` para verificar novamente um achado crítico para a segurança
no código atual.

## `codex-security findings`

Liste os achados em aberto nas verificações do repositório atual:

```bash
npx @openai/codex-security findings list

Forneça o caminho de um repositório para inspecionar outro checkout:

```bash
npx @openai/codex-security findings list /path/to/repository

Adicione `--json` para obter uma saída estruturada. A lista identifica os achados observados na
verificação mais recente e os achados anteriores que não foram confirmados nessa verificação.

Observe que os achados anteriores permanecem em aberto até serem resolvidos ou descartados (a ausência
na verificação mais recente não é considerada prova de que o problema foi corrigido).

Para registrar um achado revisado como falso positivo:

```text
usage: codex-security findings false-positive OCCURRENCE_ID
                       --reason REASON

Inspecione a verificação salva para identificar a ocorrência do achado:

```bash
npx @openai/codex-security scans show SCAN_ID

Registre uma explicação específica para o falso positivo:

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

O motivo não pode estar vazio. O Codex Security salva a decisão para o
repositório e a fornece como contexto para verificações futuras. Cada verificação reavalia de forma independente
o código-fonte atual, os controles e a alcançabilidade. Uma decisão anterior
não suprime uma regra, um caminho nem uma classe de vulnerabilidade.

## `codex-security export`

Exporte CSV, JSON ou SARIF de uma verificação concluída e selada. A exportação valida os
artefatos da verificação antes de gravar a saída e não altera o ambiente de execução do Codex nem as
credenciais.

```text
usage: codex-security export [--export-format {csv,json,sarif}]
                             [--output FILE|-] [--source-root PATH]
                             [--python PATH] scan_dir

`scan_dir` é o diretório da verificação concluída.

| Argumento                           | Descrição                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------- |
| `--export-format {csv,json,sarif}` | Selecione o formato de exportação. O padrão é `sarif`.                                           |
| `--output FILE\|-`                 | Grave o formato selecionado em um arquivo ou em stdout. Por padrão, ele é gravado em um arquivo no diretório atual. |
| `--source-root PATH`               | Adicione impressões digitais das linhas do código-fonte ao SARIF usando um checkout do repositório.                          |
| `--python PATH`                    | Selecione o interpretador Python para o exportador incluído.                                     |

`--source-root` funciona somente com `--export-format sarif`. O JSON preserva
o documento selado de achados. O CSV contém colunas portáteis de achados e
não inclui o estado de triagem da área de trabalho local.

Sem `--output`, a CLI grava o SARIF em `results.sarif`, o JSON em
`findings.json` e o CSV em `findings.csv` no diretório de trabalho atual.
As exportações podem conter trechos do código-fonte e detalhes de vulnerabilidades. Execute o comando
fora do repositório ou forneça `--output` com um caminho privado fora do
checkout verificado.

Grave o SARIF em um arquivo:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root /path/to/repository \
  --output /path/outside/repository/exports/results.sarif

Grave o SARIF em stdout:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root . \
  --output -

Exporte os achados como JSON:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format json \
  --output /path/outside/repository/exports/findings.json

Exporte os achados como CSV:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format csv \
  --output /path/outside/repository/exports/findings.csv

## `codex-security publish scan`

Publique todos os achados de uma verificação concluída no Linear:

```text
usage: codex-security publish scan [SCAN_DIR] --to linear
                                   [--linear-team TEAM_ID]
                                   [--project PROJECT_ID]
                                   [--linear-api-key KEY]
                                   [--linear-assignee EMAIL_OR_USER_ID]
                                   [--dry-run] [--json]

`SCAN_DIR` deve conter uma verificação concluída e selada. Omita-o em um terminal
interativo para selecionar uma verificação concluída no histórico local de verificações. Criar issues
também exige que a verificação e seus achados estejam no histórico local. Uma execução
simulada valida os artefatos selados sem essa verificação de persistência.

| Argumento                             | Descrição                                                                                                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--to linear`                        | Publique no Linear. Este argumento é obrigatório.                                                                                                                    |
| `--linear-team TEAM_ID`              | Selecione a equipe do Linear. Quando o argumento é omitido, usa `CODEX_SECURITY_LINEAR_TEAM`; uma das duas opções é obrigatória.                                                                 |
| `--project PROJECT_ID`               | Selecione um projeto do Linear. Quando o argumento é omitido, usa `CODEX_SECURITY_LINEAR_PROJECT`. Se nenhum dos dois estiver definido, as issues serão criadas diretamente na equipe.                          |
| `--linear-api-key KEY`               | Use uma chave de API pessoal do Linear para publicação direta. Quando o argumento é omitido, usa `CODEX_SECURITY_LINEAR_API_KEY`.                                                         |
| `--linear-assignee EMAIL_OR_USER_ID` | Atribua as issues criadas usando o endereço de e-mail ou o ID de usuário do Linear. Exige `--linear-api-key` ou `CODEX_SECURITY_LINEAR_API_KEY`. Se omitido, as issues permanecem sem responsável. |
| `--dry-run`                          | Prepare os payloads das issues sem iniciar o Codex, comunicar-se com o Linear, criar issues ou gravar o estado da publicação.                                                 |
| `--json`                             | Grave os resultados estruturados da publicação em stdout. O progresso permanece em stderr.                                                                                      |

  As descrições das issues do Linear e a saída da execução simulada podem incluir trechos de código-fonte
e detalhes de vulnerabilidades. Publique somente em uma equipe ou em um projeto autorizado do
Linear e trate a saída salva como informação confidencial.

Cada execução não simulada tenta criar uma nova issue para cada achado.
Publicar novamente a mesma verificação não associa, atualiza nem reutiliza issues existentes.
Se a publicação de alguns achados falhar, o comando preserva as issues criadas com sucesso e
retorna o código de saída `2`.
Com `--json`, revise os resultados `created` e `failed` antes de tentar novamente para
evitar duplicações.

Visualize os payloads das issues antes da publicação:

```bash
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --dry-run \
  --json

### Publicar com o aplicativo Linear conectado

Sem uma chave de API do Linear, o comando inicia o Codex usando sua configuração
existente e o aplicativo Linear conectado. Faça login e conecte o Linear à sua
conta do Codex antes da publicação:

```bash
npx @openai/codex-security login
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --project PROJECT_ID

### Publicar com uma chave de API do Linear

Ao informar `--linear-api-key` ou `CODEX_SECURITY_LINEAR_API_KEY`, a publicação ocorre
diretamente pela API do Linear e o Codex não é iniciado. A publicação direta
deixa as issues sem responsável, a menos que você selecione um responsável:

```bash

npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --linear-assignee teammate@example.com

Os valores da linha de comando substituem as variáveis de ambiente correspondentes. Para chaves
de API, prefira `CODEX_SECURITY_LINEAR_API_KEY` a `--linear-api-key`, pois
os argumentos da linha de comando podem aparecer no histórico do shell e nas listas de processos.

## `codex-security validate` e `codex-security patch`

Verifique se uma possível descoberta é válida:

```bash
npx @openai/codex-security validate findings.json \
  "Possible SQL injection in src/query.ts:42"

Gere uma correção com a habilidade de remediação incluída:

```bash
npx @openai/codex-security patch findings.json \
  "Missing authorization check in src/routes.ts:18"

Cada argumento posicional aceita texto literal ou o caminho de um arquivo. Essas entradas usam
o diretório atual. Use `validate` para verificar novamente uma descoberta após uma correção ou quando
uma varredura posterior deixar de informá-la. Comparar varreduras por si só não comprova que uma correção
funcionou.

Use `--effort` para selecionar o esforço de raciocínio de qualquer um dos comandos:

```bash
npx @openai/codex-security validate "Possible SQL injection" --effort high

### Corrigir descobertas após uma varredura

Use `scan --patch` para corrigir descobertas após uma varredura completa. É necessário usar
`@openai/codex-security` 0.1.15 ou posterior. O limite de gravidade padrão é
`low`. Este comando seleciona descobertas de gravidade alta e crítica:

```bash
npx @openai/codex-security scan . --patch --patch-severity high --json

As descobertas verificadas e já corrigidas não acionam `--fail-on-severity`.

### Corrigir descobertas salvas

Informe o ID de uma descoberta ou ocorrência para corrigir o repositório original ou selecione
descobertas de uma varredura salva:

```bash
npx @openai/codex-security patch OCCURRENCE_ID
npx @openai/codex-security patch --scan SCAN_ID --severity high --json
npx @openai/codex-security patch --scan latest --severity medium

`--scan latest` seleciona a última varredura concluída do repositório atual.
Os comandos para descobertas salvas aceitam `--json`; as entradas de texto literal e de arquivo, não.

Adicione `--create-pr` para fazer commit somente dos arquivos de correção verificados e abrir um pull request
com a CLI do GitHub:

```bash
npx @openai/codex-security patch --scan SCAN_ID --severity high --create-pr

Se o push ou o pull request falhar, execute o comando exibido `patch --resume-pr BRANCH`
no mesmo repositório para tentar novamente.

### Corrigir issues do Linear

Defina `CODEX_SECURITY_LINEAR_API_KEY` ou `LINEAR_API_KEY` para usar uma chave de API pessoal
ou `LINEAR_ACCESS_TOKEN` para usar um token OAuth. Prefira uma variável de ambiente a
`--linear-api-key KEY` para evitar que a chave apareça no histórico do shell.

Importe uma issue pelo ID ou pela URL. Repita `--linear-issue` para selecionar mais de uma
issue:

```bash
npx @openai/codex-security patch --linear-issue SEC-123 --linear-issue SEC-124

Use `--linear-project` para selecionar as issues abertas de um projeto. Adicione `--linear-filter`
para restringir a seleção:

```bash
npx @openai/codex-security patch --linear-project "Security backlog" \
  --linear-filter '{"labels":{"name":{"eq":"security"}}}'

A CLI exclui as issues concluídas e canceladas, a menos que o filtro defina `state`.
Ela não altera as issues do Linear.

## `codex-security login`, `logout` e `info`

Faça login de forma interativa:

```bash
npx @openai/codex-security login

Use a autenticação por dispositivo em uma máquina remota ou sem interface gráfica:

```bash
npx @openai/codex-security login --device-auth

Verifique o login atual:

```bash
npx @openai/codex-security login status

Remova o login armazenado:

```bash
npx @openai/codex-security logout

Armazene uma chave de API enviando-a por stdin:

```bash
printenv OPENAI_API_KEY | npx @openai/codex-security login --with-api-key

Armazene um token de acesso empresarial:

```bash
printenv CODEX_ACCESS_TOKEN | npx @openai/codex-security login --with-access-token

Inspecione os metadados somente leitura do SDK e do plug-in incluído:

```bash
npx @openai/codex-security info --json

Ao expor a CLI como um servidor MCP, `info` é o único comando disponível.
Varreduras, exportações, publicação, login, validação e aplicação de correções continuam disponíveis apenas na CLI.

## Ler a saída da varredura

Por padrão, as varreduras enviam o progresso, os resumos de conclusão e os erros para stderr
sem gravar o resultado completo da varredura em stdout. Use `--json`,
`--format` ou `--full-output` para enviar resultados estruturados da varredura para stdout.

Os terminais interativos exibem um painel em tempo real com a fase atual da varredura,
os arquivos revisados, a atividade, o uso de tokens e o custo estimado. Em CI e na saída
redirecionada, o progresso é exibido em texto simples. Adicione `--headless` para exibir o progresso
em texto simples em um terminal interativo:

```bash
npx @openai/codex-security scan . --headless

O painel também exibe detalhes da sessão em tempo real. Esses detalhes não têm informações sensíveis ocultadas e podem
conter código-fonte ou credenciais. Revise-os antes de compartilhá-los.

### Diagnósticos detalhados

Adicione `--verbose` para exibir em stderr diagnósticos de ciclo de vida, autenticação, progresso e custo
com informações sensíveis ocultadas:

```bash
npx @openai/codex-security scan . --verbose

Defina `CODEX_SECURITY_LOG_LEVEL=debug` para ativar os mesmos diagnósticos sem usar a
opção. `LOG_LEVEL=debug` também ativa os diagnósticos quando
`CODEX_SECURITY_LOG_LEVEL` não está definido.

### Resumo da conclusão

Uma varredura concluída registra em stderr o número de descobertas em aberto no repositório, a distribuição por gravidade,
a cobertura, o tempo decorrido, o caminho do relatório e o diretório de resultados. Também
inclui o uso de tokens e o custo estimado, quando disponíveis:

```text
  REPORT    /path/to/scan/report.md

  FINDINGS  4 (3 confirmed this scan; 1 previously found; 1 critical, 2 high, 1 informational)
  COVERAGE  complete
  ELAPSED   1s
  TOKENS    1,250 input, 200 cached, 30 output
  RESULTS   /path/to/scan

As descobertas informativas entram no total do resumo. As políticas de gravidade
avaliam apenas as descobertas `critical`, `high`, `medium` e `low` da varredura
atual, não as descobertas anteriores incluídas no total do repositório.

### Saída JSON

`scan --json` grava um documento JSON completo em stdout. Sua estrutura de nível superior
é:

```text
manifest
repositoryFindings
findings
coverage
scanDir
threadId
reportPath
artifactsDir
sarifPath
cost
turn
  id
  status
  durationMs
  finalResponse
  usage

Ao [aplicar correções](#patch-findings-after-a-scan), a saída JSON também inclui os resultados das correções
e qualquer pull request criado.

Informações de progresso, resumos de conclusão, avisos de arquivamento e erros continuam em stderr.
Uma varredura concluída ainda exibe o resultado JSON completo quando uma política de gravidade
retorna o código de saída `1` ou uma cobertura incompleta retorna o código de saída `2`.

  `codex-security scan --json` gera um documento JSON. `codex exec --json`
  gera um fluxo de eventos JSON Lines. Use o formato de saída correspondente ao
  comando executado.

## Artefatos da varredura

Uma varredura concluída mantém o relatório legível junto com os artefatos estruturados:

```text
<scan-directory>/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

Os arquivos estruturados têm funções diferentes:

| Arquivo                    | Conteúdo                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `scan-manifest.json`    | Identidade, status, alvo, escopo e produtor da varredura, além dos registros de artefatos selados.                                                    |
| `findings.json`         | Identificadores das descobertas, gravidade, confiança, taxonomia, locais, evidências, validação, fluxo de dados, alcançabilidade e remediação. |
| `coverage.json`         | Superfícies revisadas, exclusões, trabalho adiado, questões em aberto e completude da cobertura.                                        |
| `report.md`             | Relatório legível da varredura.                                                                                                           |
| `artifacts/`            | Artefatos auxiliares da varredura.                                                                                                      |
| `exports/results.sarif` | SARIF gerado durante a varredura, quando houver.                                                                                  |

A completude da cobertura tem três valores:

- `complete`: A varredura registra cobertura completa para o escopo selecionado.
- `partial`: A varredura registra trabalho adiado ou outros limites de cobertura.
- `unknown`: A varredura informa que a completude da cobertura é desconhecida.

Revise as superfícies cuja análise foi adiada, as exclusões explícitas e as questões em aberto antes de usar
a cobertura como evidência para uma decisão de segurança.

## Códigos de saída e sinais

A CLI usa estes códigos de saída:

| Saída  | Condição                                                                                                                                                                     |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`   | Uma verificação foi concluída com cobertura completa e atendeu à sua política de gravidade, uma verificação em lote ou publicação foi concluída sem falhas ou outro comando foi executado com sucesso.                  |
| `1`   | Uma verificação concluída informa um achado com gravidade igual ou superior à configurada.                                                                                                       |
| `2`   | A CLI encontrou um erro de entrada, execução ou exportação, uma verificação tem cobertura incompleta, uma verificação em lote inclui repositórios com erros ou a publicação de um ou mais achados falhou. |
| `130` | Ctrl-C interrompeu uma verificação ou publicação.                                                                                                                                     |
| `143` | SIGTERM encerrou uma verificação ou publicação.                                                                                                                                     |

Qualquer verificação com cobertura `partial` ou `unknown` retorna `2`, mesmo sem uma
política de gravidade. Quando você solicita uma saída estruturada, verificações concluídas e
publicações parciais ainda gravam os resultados disponíveis em stdout. A CLI
exibe o local de qualquer saída parcial após uma interrupção ou um erro de
execução.

## Permissões para verificações locais

As verificações da CLI e do SDK são executadas com suas permissões no sistema operacional local. Cada verificação
usa o perfil de sistema de arquivos `codex_security_scan` e define `approvalPolicy` como
`"never"`. O perfil permite ler o sistema de arquivos local e gravar nas
raízes do workspace e no diretório de estado selecionado para a verificação. As verificações não param para
solicitar aprovação interativa.

As configurações fornecidas por meio de `--codex` na CLI ou de `codexOverrides` no SDK, incluindo
`approval_policy`, `sandbox_mode` e permissões do sistema de arquivos, não podem substituir
nem restringir esses controles de verificação. As restrições de Host e de rede continuam em vigor.

Os processos de verificação e do workbench podem herdar seu ambiente, incluindo tokens de API
e credenciais de nuvem não relacionados. Verifique apenas repositórios nos quais você confia e que tem
permissão para avaliar e forneça somente as credenciais exigidas pela verificação.

## Autenticação e pré-requisitos

Defina `OPENAI_API_KEY` ou `CODEX_API_KEY`, faça login com
`npx @openai/codex-security login` ou use um login existente do Codex armazenado em
arquivo. Para OpenRouter ou Fireworks, configure a chave de API do provedor e selecione um
modelo. Para Amazon Bedrock, use uma chave de API do Bedrock ou a cadeia padrão de
credenciais da AWS.

Para selecionar credenciais, consulte [Selecionar a autenticação
da verificação](#select-scan-authentication).

Para CI, restrinja a chave de API à etapa de verificação e use um fluxo de trabalho confiável.

A CLI requer Node.js 22 (22.13.0 ou posterior), 24 ou 26. Verificações, verificações em lote,
exportações, histórico de verificações e achados salvos também exigem Python 3.10 ou posterior.
O Python 3.10 também requer `tomli`. Use `--python` com `scan`, `bulk-scan` ou
`export`, ou defina `PYTHON` para qualquer comando que dependa de Python.

Continue com o [início rápido da CLI](/pt-BR/codex/security/cli), o [guia de verificações
em lote](/pt-BR/codex/security/cli/bulk-scans), as [perguntas frequentes sobre a CLI](/pt-BR/codex/security/cli/faq), o [guia de
CI](/pt-BR/codex/security/cli/ci) ou o [guia do TypeScript SDK](/pt-BR/codex/security/sdk).

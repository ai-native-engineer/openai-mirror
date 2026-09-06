<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/cli -->

O Codex Security ajuda equipes de segurança e engenharia a encontrar, confirmar e corrigir
vulnerabilidades. Use sua interface de linha de comando (CLI) para realizar varreduras em
repositórios que você possui ou tem permissão para avaliar, analisar descobertas ao longo do tempo
e verificar alterações antes de serem integradas.

  O pacote `@openai/codex-security` é público. A execução de varreduras requer acesso ao Codex
  Security. Para fazer uma varredura interativa no Codex, comece pelo [início rápido do plug-in do Codex
  Security](/pt-BR/codex/security/plugin). Para repositórios conectados
  do GitHub, consulte a [configuração do Codex Security na nuvem](/pt-BR/codex/security/setup).

## Verifique os pré-requisitos

A CLI requer Node.js 22 (22.13.0 ou posterior), 24 ou 26. Varreduras, varreduras em massa,
exportações, histórico de varreduras e descobertas salvas também exigem Python 3.10 ou posterior.
Para mais detalhes, consulte [Autenticação e
pré-requisitos](/pt-BR/codex/security/cli/reference#authentication-and-prerequisites).

## Configure e verifique a CLI

Execute a CLI com `npx` e confira a versão:

```bash
npx @openai/codex-security --version

Para consultar a versão do pacote e a do plug-in incluído, execute:

```bash
npx @openai/codex-security info --json

Consulte as [versões da CLI e do SDK](https://github.com/openai/codex-security/releases)
para conferir as alterações no pacote.

Liste os comandos disponíveis:

```bash
npx @openai/codex-security --help

Consulte também a [referência da CLI](/pt-BR/codex/security/cli/reference).

## Fazer login

Para uso local, faça login com sua conta do ChatGPT:

```bash
npx @openai/codex-security login

Em uma máquina remota ou sem interface gráfica, use a autenticação por dispositivo:

```bash
npx @openai/codex-security login --device-auth

Para CI e outros fluxos de trabalho automatizados, defina uma chave de API da OpenAI:

```bash

Para credenciais da AWS, consulte a [configuração do
Amazon Bedrock](/pt-BR/codex/security/cli/reference#use-amazon-bedrock). Para [OpenRouter ou
Fireworks](/pt-BR/codex/security/cli/reference#use-openrouter-or-fireworks), defina a chave de API do
provedor e selecione um modelo com `--provider` e `--model`.

Para usar seu login do ChatGPT quando uma chave de API também estiver definida, selecione-o explicitamente:

```bash
npx @openai/codex-security scan . --auth chatgpt

Para exigir a chave de API do ambiente, selecione a autenticação por chave de API:

```bash
npx @openai/codex-security scan . --auth api-key

Dependendo da sua conta e do repositório, as varreduras de todo o repositório também podem
exigir [Trusted Access for Cyber](https://chatgpt.com/cyber).

## Prepare uma varredura

Escolha um repositório no qual você confie e que tenha permissão para avaliar. As varreduras usam suas permissões locais
do sistema operacional e não pausam para solicitar aprovação. Os processos de varredura
podem herdar seu ambiente, portanto remova credenciais não relacionadas antes
de começar. Consulte [Permissões de varredura
local](/pt-BR/codex/security/cli/reference#local-scan-permissions).

Escolha um diretório fora do repositório para armazenar os resultados da varredura:

```bash
REPOSITORY=/path/to/repository
SCAN_DIR=/path/outside/repository/codex-security-results

Se você omitir `--output-dir`, o Codex Security salvará os resultados no próprio diretório de estado
persistente. Os resultados podem incluir trechos de código-fonte e detalhes de vulnerabilidades;
portanto, escolha um local privado e uma política de retenção adequada.

Se o diretório de estado padrão não permitir gravação, selecione um diretório gravável
fora do repositório verificado:

```bash

Confira o repositório, o alvo e o diretório de saída antes de iniciar uma varredura:

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --dry-run

A simulação verifica as entradas locais, incluindo os caminhos informados em `--knowledge-base`,
sem iniciar o Codex, carregar credenciais nem testar o interpretador Python
do plug-in.

## Execute sua primeira varredura

Execute uma varredura padrão e mantenha os resultados no diretório selecionado:

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR"

Terminais interativos exibem um painel da varredura em tempo real. Adicione `--headless` para exibir
linhas de progresso em texto simples. Em CI e em terminais sem sessão interativa,
o progresso em texto simples é exibido automaticamente.

O painel também mostra detalhes da sessão em tempo real. Eles podem conter código-fonte
ou credenciais; portanto, revise-os antes de compartilhá-los.

Por padrão, a CLI grava o progresso da varredura e o resumo de conclusão em stderr.
Ela não imprime o resultado completo da varredura em stdout. Uma varredura concluída imprime um
resumo como este:

```text
  REPORT    /path/outside/repository/codex-security-results/report.md

  FINDINGS  2 (2 confirmed this scan; 0 previously found; 1 high, 1 medium)
  COVERAGE  complete
  ELAPSED   42s
  RESULTS   /path/outside/repository/codex-security-results

O uso de tokens e o custo estimado são exibidos quando disponíveis. Para imprimir o resultado
completo em JSON legível por máquina, solicite explicitamente a saída estruturada:

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --json

Por padrão, as varreduras apenas geram relatórios, portanto as descobertas continuam disponíveis para
revisão local. Quando estiver pronto para [executar varreduras em
CI](/pt-BR/codex/security/cli/ci), considere adicionar um limite de gravidade.

## Escolha um modelo e um nível de esforço de raciocínio

Por padrão, as varreduras usam `gpt-5.6-sol` com esforço de raciocínio `xhigh`. Selecione um
modelo e um nível de esforço diferentes quando a tarefa exigir:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --model gpt-5.6-terra \
  --effort high

Os níveis de esforço compatíveis são `minimal`, `low`, `medium`, `high`, `xhigh` e
`max`.

## Analise os resultados

Abra `report.md` para consultar o resultado em formato legível. O diretório da varredura também contém os
arquivos estruturados usados pela automação:

```text
codex-security-results/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

- `scan-manifest.json` registra o alvo, o escopo, o produtor e os artefatos
  selados.
- `findings.json` registra a gravidade, a confiança, as localizações, as evidências e a
  remediação de cada descoberta.
- `coverage.json` registra as superfícies analisadas, as exclusões, o trabalho adiado, as questões
  em aberto e a completude da cobertura.

A cobertura pode ser `complete`, `partial` ou `unknown`. Consulte todas as áreas adiadas ou questões
em aberto antes de considerar a varredura uma evidência de revisão.
A [referência da CLI](/pt-BR/codex/security/cli/reference#scan-artifacts) descreve
o contrato completo de artefatos e saídas.

## Analise e corrija as descobertas

Após uma varredura interativa completa com descobertas, a CLI oferece um navegador de
descobertas. Analise as evidências e escolha quais descobertas corrigir. Você pode encontrar
as tarefas salvas no aplicativo Codex para desktop.

Para corrigir descobertas de gravidade alta e crítica sem o navegador:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --patch --patch-severity high --json

Adicione `--create-pr` para fazer commit dos patches verificados e abrir uma pull request no GitHub.

Você também pode corrigir descobertas salvas ou importar issues do Linear. Consulte a
[referência de `validate` e `patch`](/pt-BR/codex/security/cli/reference#codex-security-validate-and-codex-security-patch).

## Escolha a próxima varredura

Use uma varredura por caminho quando um repositório contiver serviços ou pacotes separados:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --path services/billing \
  --path packages/auth

Analise as alterações incluídas em commits entre a revisão base e `HEAD`:

```bash
npx @openai/codex-security scan "$REPOSITORY" --diff origin/main --head HEAD

Analise as alterações preparadas e não preparadas em relação a `HEAD`:

```bash
npx @openai/codex-security scan "$REPOSITORY" --working-tree --base HEAD

As varreduras de diff e da árvore de trabalho exigem que o argumento do repositório seja a raiz da
árvore de trabalho do Git. Busque as revisões selecionadas antes de iniciar uma varredura de diff.

Use o modo aprofundado quando um repositório ou caminho precisar de uma análise mais abrangente:

```bash
npx @openai/codex-security scan "$REPOSITORY" --mode deep

Para controlar os workers, os subagentes e quando a varredura é interrompida:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

Essas opções exigem o modo aprofundado, que oferece suporte a repositórios e caminhos como alvos,
mas não a varreduras de diff ou da árvore de trabalho. Aqui, `--workers` controla workers
independentes de varredura padrão em uma única varredura; `bulk-scan --workers` controla varreduras
simultâneas de repositórios. `--max-time-hours` aceita um número positivo de até `96`,
inclusive horas fracionárias. Ao atingir o limite, a varredura interrompe os workers ainda em andamento,
preserva os resultados das varreduras concluídas e os consolida no relatório final.

## Adicione contexto de arquitetura e segurança

Forneça documentos de arquitetura, modelos de ameaças ou políticas de segurança como contexto da
varredura. Isso ajuda o Codex Security a avaliar as descobertas com base no funcionamento real
do seu sistema:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

## Adicione instruções personalizadas para a varredura

Adicione instruções que direcionem a varredura às suas prioridades de segurança. Use um
segundo arquivo para as instruções de acompanhamento:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --scan-prompt-file /path/to/scan.md \
  --post-scan-prompt-file /path/to/follow-up.md

O acompanhamento é executado na mesma sessão autenticada após varreduras bem-sucedidas
e varreduras com cobertura incompleta ou erros. Se o acompanhamento falhar, a CLI
emite um aviso e preserva a varredura concluída. Ele não é executado após um
cancelamento nem após uma varredura que atinja seu limite de custo. Ambas as opções também funcionam
com `bulk-scan`; uma coluna `prompt` no CSV adiciona instruções específicas para cada repositório.

## Defina um orçamento para a varredura

Use `--max-cost` para interromper uma varredura quando o custo estimado do modelo ultrapassar um limite
em USD:

```bash
npx @openai/codex-security scan "$REPOSITORY" --max-cost 5

Solicitações já em andamento podem ser concluídas com um custo ligeiramente acima do limite. Se uma varredura
aprofundada atingir o limite depois que o Codex Security consolidar os resultados dos workers
concluídos, a CLI salva o relatório concluído, marca sua cobertura como `partial`
e retorna o código de saída `2`. Se a varredura não puder gerar um relatório concluído,
qualquer saída parcial disponível permanece em disco.

## Verificar alterações antes de cada commit

Instale uma verificação de segurança de pre-commit do Git para o seu repositório:

```bash
npx @openai/codex-security install-hook

A verificação analisa as alterações preparadas e não preparadas antes de cada commit. Ela bloqueia
constatações de alta severidade e erros de verificação sem substituir um script
de pre-commit existente.

## Verificar repositórios em lote

Faça login no GitHub antes de descobrir repositórios:

```bash
gh auth login

Descubra e selecione repositórios da sua conta ou organização do GitHub:

```bash
npx @openai/codex-security bulk-scan

O fluxo interativo exclui repositórios arquivados e forks. Ele solicita que você
confirme os repositórios selecionados antes da verificação.

Para verificar uma lista de repositórios previamente preparada, forneça um CSV e um diretório de saída:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

Execute o mesmo comando novamente para retomar uma verificação em lote existente. O Codex Security
ignora os repositórios já concluídos. Adicione `--max-attempts 3` se quiser repetir a tentativa após
erros temporários no repositório ou na verificação.

Para saber mais sobre a descoberta de repositórios no GitHub, a preparação do CSV, os resultados de campanhas e a configuração do Docker, consulte
[Executar verificações de segurança em lote](/pt-BR/codex/security/cli/bulk-scans).

## Executar verificações em lote no Docker

Se o seu acesso incluir a imagem Docker do Codex Security, use a configuração
reforçada do Compose e o perfil de segurança fornecidos em um host Docker com Linux.
O host deve permitir a criação de namespaces de usuário sem privilégios. Forneça um CSV de repositórios,
mantenha os resultados e o estado de login em diretórios montados persistentes e
forneça credenciais por meio do seu ambiente ou de um gerenciador de segredos:

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

O contêiner executa verificações em lote sem prompts interativos. Use a CLI fora do
Docker quando quiser descobrir repositórios de forma interativa. Para repositórios
privados, forneça `GH_TOKEN` ou `GITHUB_TOKEN` por meio do seu ambiente ou de um
gerenciador de segredos. Os [requisitos de login](#sign-in), incluindo o acesso à conta e ao
repositório, também se aplicam às verificações executadas em contêineres.

## Revisitar uma verificação salva

Liste as verificações salvas do seu repositório:

```bash
npx @openai/codex-security scans list "$REPOSITORY"

Copie dos resultados o ID de uma verificação para inspecionar suas constatações e sua configuração:

```bash
npx @openai/codex-security scans show SCAN_ID

Para inspecionar os eventos salvos de uma verificação e de seus workers:

```bash
npx @openai/codex-security scans logs SCAN_ID

Os logs salvos não são editados para ocultar informações e podem conter código-fonte ou credenciais.
Revise-os antes de compartilhá-los.

Liste as constatações em aberto nas verificações do repositório:

```bash
npx @openai/codex-security findings list "$REPOSITORY"

Uma constatação anterior permanece em aberto quando a verificação mais recente não a confirma.

Para marcar uma constatação revisada como falso positivo, explique por que ela não
se aplica:

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The route already checks permissions"

As verificações posteriores consideram essa explicação, mas ainda assim reavaliam o código atual.

Execute a mesma verificação no checkout atual usando a configuração original:

```bash
npx @openai/codex-security scans rerun SCAN_ID

Compare duas verificações para encontrar constatações novas, persistentes, reabertas, resolvidas ou com status
desconhecido:

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

A comparação associa automaticamente as constatações com base na causa raiz e reutiliza as
correspondências salvas.

Para saber mais sobre o formato CSV para verificações em lote, os filtros do histórico de verificações e as opções de comando, consulte
a [referência da CLI](/pt-BR/codex/security/cli/reference).

Continue com o fluxo de trabalho adequado ao seu objetivo:

- [Executar verificações de segurança em lote](/pt-BR/codex/security/cli/bulk-scans) para descobrir repositórios do GitHub
  ou verificar um inventário CSV fixado.
- [Ler as perguntas frequentes da CLI](/pt-BR/codex/security/cli/faq) para obter respostas sobre o histórico de verificações,
  o feedback sobre falsos positivos, a cobertura e a verificação de correções.
- [Executar verificações em CI](/pt-BR/codex/security/cli/ci) para revisar pull requests, preservar
  os resultados e definir uma política de severidade.
- [Usar a referência da CLI](/pt-BR/codex/security/cli/reference) para consultar cada flag,
  formato de saída, artefato e código de saída.
- [Integrar o TypeScript SDK](/pt-BR/codex/security/sdk) para executar verificações a partir de um
  aplicativo ou de uma ferramenta de desenvolvimento.

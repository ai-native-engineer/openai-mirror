<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/cli/faq -->

Encontre respostas para perguntas comuns sobre a varredura de repositórios e o gerenciamento
de descobertas de segurança pelo terminal. Para instalar e executar a primeira varredura, comece
pelo [início rápido da CLI](/pt-BR/codex/security/cli).

## Varreduras de repositórios

### Quem pode usar a CLI

O pacote `@openai/codex-security` é público.

É necessário ter acesso ao Codex Security para executar varreduras. Para obter melhores resultados, use uma conta
verificada para o [Trusted Access for Cyber](https://chatgpt.com/cyber).

### Por que uma varredura usa uma chave de API após o login

Quando seu ambiente inclui `OPENAI_API_KEY` ou `CODEX_API_KEY`, as varreduras
sem terminal interativo e as varreduras em JSON e JSONL usam, por padrão, a chave
de API do ambiente, mesmo após um login bem-sucedido no ChatGPT ou com token de acesso.
As varreduras interativas com saída de texto solicitam que você escolha quando o login
no ChatGPT também está disponível. As simulações não exibem prompts nem carregam credenciais.

Para usar suas credenciais armazenadas em uma varredura, selecione-as explicitamente:

```bash
npx @openai/codex-security scan . --auth chatgpt

Para exigir uma chave de API de `OPENAI_API_KEY` ou `CODEX_API_KEY`:

```bash
npx @openai/codex-security scan . --auth api-key

Para usar automaticamente suas credenciais armazenadas como padrão, execute
`unset OPENAI_API_KEY CODEX_API_KEY`. Para conhecer todos os modos de autenticação compatíveis,
consulte a [referência da CLI](/pt-BR/codex/security/cli/reference#select-scan-authentication).

### Como funciona a varredura de repositórios em massa

Faça login com a CLI do GitHub:

```bash
gh auth login

Descubra e selecione repositórios de uma conta ou organização do GitHub:

```bash
npx @openai/codex-security bulk-scan

Para usar uma lista preparada, forneça um CSV de repositórios e um diretório de saída:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

Consulte [Executar varreduras de segurança em massa](/pt-BR/codex/security/cli/bulk-scans) para conhecer a descoberta de repositórios no GitHub,
o formato CSV, os resultados da campanha e as opções disponíveis.

### É possível retomar uma varredura em massa interrompida

Sim. Execute o mesmo comando de varredura em massa com o CSV e o diretório de saída originais.
O Codex Security ignora os repositórios que já tiveram a varredura concluída.

Adicione `--max-attempts 3` para tentar novamente em caso de erros temporários no repositório ou na varredura:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

Uma varredura concluída com cobertura `partial` ou `unknown` mantém os resultados e
faz a campanha encerrar com o código de saída `2`. Essa varredura não é repetida, mesmo com
`--max-attempts`.

### Como uma varredura pode usar a arquitetura e as políticas de segurança

Forneça documentos de arquitetura, modelos de ameaças ou políticas de segurança com
`--knowledge-base`:

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

O Codex Security usa esses documentos como contexto da varredura atual. Para saber quais
tipos de arquivo são compatíveis e como os diretórios são tratados, consulte [Adicionar contexto de
segurança](/pt-BR/codex/security/cli/reference#add-security-context).

## Descobertas e cobertura

### Onde as equipes podem encontrar resultados de varreduras anteriores

Liste as varreduras salvas do seu repositório:

```bash
npx @openai/codex-security scans list /path/to/repository

Use um ID de varredura dos resultados para inspecionar as descobertas dessa varredura:

```bash
npx @openai/codex-security scans show SCAN_ID

Cada varredura concluída mantém juntos o relatório, as descobertas, a cobertura e os artefatos
de apoio. Consulte [Artefatos da
varredura](/pt-BR/codex/security/cli/reference#scan-artifacts) para ver a estrutura completa.

Para inspecionar eventos salvos das varreduras e dos workers, execute `scans logs SCAN_ID`. Esses logs
não têm informações ocultadas e podem conter código-fonte ou credenciais.

### O que fazer se a CLI não conseguir salvar o histórico de varreduras

O Codex Security mantém o histórico de varreduras em um banco de dados de trabalho. Se o diretório
padrão de estado não permitir gravação, escolha um diretório privado fora do
repositório:

```bash

### Como as varreduras distinguem descobertas novas e conhecidas

Liste as descobertas em aberto de todas as varreduras de um repositório:

```bash
npx @openai/codex-security findings list /path/to/repository

A lista identifica as descobertas confirmadas na varredura mais recente e as descobertas anteriores em aberto
que a varredura não confirmou.

Compare as descobertas entre as duas varreduras:

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

A comparação associa automaticamente as descobertas pela causa raiz, reutiliza as correspondências
salvas e identifica descobertas novas, persistentes, reabertas, resolvidas e desconhecidas.
Uma descoberta só é considerada resolvida quando a varredura posterior cobre seu
alvo original e o caminho afetado sem lacunas de cobertura.

### Como funciona o feedback sobre falsos positivos

Inspecione a varredura salva para encontrar o ID da ocorrência:

```bash
npx @openai/codex-security scans show SCAN_ID

Registre por que essa descoberta não se aplica:

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

As futuras varreduras do mesmo repositório recebem essa explicação como contexto. Elas
continuam verificando de forma independente o código-fonte atual, os controles e a alcançabilidade. O
descarte não suprime uma regra, um caminho nem uma classe de vulnerabilidade.

Para ver detalhes do comando, consulte a [referência de
descobertas](/pt-BR/codex/security/cli/reference#codex-security-findings).

### Por que varreduras repetidas podem retornar descobertas diferentes

As varreduras assistidas por IA podem variar, mesmo com a mesma configuração de varredura. Comece
executando novamente sua varredura de referência:

```bash
npx @openai/codex-security scans rerun BASELINE_SCAN_ID

A nova execução preserva a configuração original da varredura e exige a mesma versão do
plug-in. Se o plug-in instalado tiver sido alterado, o comando é interrompido.

Compare a varredura de referência com a nova varredura:

```bash
npx @openai/codex-security scans compare BASELINE_SCAN_ID REPEAT_SCAN_ID

Forneça orientações compartilhadas de arquitetura e segurança quando a falta de contexto puder
contribuir para a variação. A correspondência pode identificar a mesma descoberta subjacente
em diferentes execuções, mas não torna as varreduras determinísticas. Verifique diretamente qualquer
descoberta importante que desaparecer.

### Como uma equipe pode confirmar que uma correção funcionou

Depois de aplicar uma correção, execute novamente a varredura original:

```bash
npx @openai/codex-security scans rerun BEFORE_SCAN_ID

Compare as descobertas originais com a nova varredura:

```bash
npx @openai/codex-security scans compare BEFORE_SCAN_ID AFTER_SCAN_ID

Confirme se a nova varredura cobre o alvo original e o caminho afetado sem
lacunas de cobertura. Em seguida, verifique diretamente a descoberta original no checkout
atual:

```bash
npx @openai/codex-security validate /path/to/original/findings.json \
  "Recheck the SQL injection in src/orders.ts:42 against the current code"

A ausência de uma descoberta ou apenas uma comparação de varreduras não comprova que uma correção funcionou.

### O que significa cobertura incompleta

A cobertura pode ser `complete`, `partial` ou `unknown`. Examine `coverage.json`
para identificar caminhos excluídos, superfícies cuja análise foi adiada e questões em aberto antes de considerar uma
varredura como evidência de revisão.

As varreduras com cobertura parcial ou desconhecida retornam o código de saída `2`, mesmo sem uma
política de gravidade. Elas ainda mantêm as descobertas e os dados de cobertura disponíveis. Uma varredura posterior
não pode confirmar que uma descoberta anterior deixou de existir quando não
cobre o caminho original dessa descoberta.

## Automação e custo

### Como funcionam os limites de tempo das varreduras aprofundadas

Defina um prazo de execução para os workers ao iniciar uma varredura aprofundada:

```bash
npx @openai/codex-security scan . --mode deep --max-time-hours 1.5

O prazo padrão é de `96` horas. Use qualquer valor positivo de até `96`, incluindo
frações. Ao atingir o prazo, o Codex Security interrompe os workers que não concluíram a execução, preserva
os resultados das varreduras padrão concluídas e os consolida no relatório final. Se
nenhum worker concluir a revisão do código-fonte, o relatório registra cobertura parcial e a
CLI retorna o código de saída `2`.

Para configurações persistentes ou campanhas em massa, defina `max_time_hours` em
`[deep_scan]` na [configuração da varredura
aprofundada](/pt-BR/codex/security/cli/reference#configure-deep-scans).

### Como funcionam os limites de custo das varreduras

Defina um limite de custo estimado em USD antes de iniciar a varredura:

```bash
npx @openai/codex-security scan . --max-cost 5

O limite é uma estimativa, não um teto rígido de gastos. As solicitações já em
andamento podem ser concluídas acima desse limite. Se uma varredura aprofundada atingir o limite
depois que o Codex Security consolidar os resultados dos workers que concluíram a execução, a CLI salvará o
relatório concluído com cobertura parcial e será encerrada com o código `2`. Caso contrário, preservará
qualquer saída parcial disponível.

### As varreduras podem verificar commits e pull requests

Instale uma verificação de segurança pré-commit para alterações preparadas e não preparadas:

```bash
npx @openai/codex-security install-hook

Para verificar pull requests, analise as alterações registradas em commits e defina um limite de
gravidade:

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --fail-on-severity high

Uma verificação completa retorna o código de saída `1` quando encontra uma issue de gravidade
igual ou superior à selecionada. Consulte [Executar verificações em CI](/pt-BR/codex/security/cli/ci) para conhecer o fluxo de trabalho
completo do GitHub Actions, o tratamento de artefatos e a exportação SARIF.

### Outro aplicativo pode executar verificações diretamente

Sim. Use o [TypeScript SDK](/pt-BR/codex/security/sdk) para iniciar verificações, selecionar
alvos, inspecionar achados e a cobertura, acompanhar o progresso e aplicar controles de custos
a partir de um aplicativo ou de uma ferramenta de desenvolvimento.

<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/cli/bulk-scans -->

Use `npx @openai/codex-security bulk-scan` para revisar repositórios em uma única
campanha. Descubra repositórios na sua conta pessoal do GitHub ou em uma
organização, ou forneça um CSV que fixe cada repositório em uma revisão exata
do Git.

  O pacote `@openai/codex-security` é público. A execução de varreduras exige
  acesso ao Codex Security. Siga o [início rápido da CLI](/pt-BR/codex/security/cli) para instalar
  a CLI e fazer login.

## Escolher a origem dos repositórios

| Origem           | Quando usar                                                                          |
| ---------------- | --------------------------------------------------------------------------------------- |
| Descoberta no GitHub | Escolha interativamente os repositórios na sua conta pessoal do GitHub ou em uma organização. |
| Inventário CSV    | Execute uma campanha automatizada e reproduzível em revisões exatas de repositórios.                |

Os dois fluxos de trabalho salvam o progresso, preservam os resultados de cada repositório e permitem
retomar uma campanha após uma interrupção.

## Descobrir repositórios do GitHub

Faça login com a GitHub CLI:

```bash
gh auth login

Inicie uma varredura em massa interativa:

```bash
npx @openai/codex-security bulk-scan

A CLI orienta você pelas seguintes etapas:

1. Escolha sua conta pessoal do GitHub ou uma organização.
2. Revise os repositórios ativos nos últimos 90 dias.
3. Pesquise na lista de repositórios e selecione quais serão verificados.
4. Escolha um diretório para os resultados da varredura.
5. Revise os repositórios selecionados e confirme a campanha.

A descoberta exclui repositórios arquivados e forks. A CLI registra o commit exato da
branch padrão de cada repositório selecionado em
`<output-directory>/repositories.csv`. Nenhuma varredura começa até que você confirme a
seleção.

Para usar o GitHub Enterprise Server, primeiro faça login no seu host do GitHub:

```bash
gh auth login --hostname github.example.com

Defina `GH_HOST` ao iniciar a descoberta de repositórios:

```bash
GH_HOST=github.example.com npx @openai/codex-security bulk-scan

A descoberta interativa exige um terminal. Para CI, contêineres ou uma lista preparada de
repositórios, use um inventário CSV.

## Criar um CSV de repositórios

Crie um CSV com uma linha para cada repositório e a respectiva revisão fixada:

```csv
id,repository,revision,scope,mode,prompt
payments,https://github.com/example/payments.git,0123456789abcdef0123456789abcdef01234567,services/api,standard,Review payment authorization and refunds.
identity,https://github.com/example/identity.git,fedcba9876543210fedcba9876543210fedcba98,,deep,Review session and identity boundaries.

O CSV aceita estas colunas:

| Coluna       | Obrigatório | Descrição                                                                                                |
| ------------ | -------- | ---------------------------------------------------------------------------------------------------------- |
| `id`         | Sim      | Identificador exclusivo do repositório. Use letras, números, pontos, hifens ou sublinhados.                      |
| `repository` | Sim      | URL HTTPS, URL SSH ou caminho de um repositório local. Os caminhos relativos são resolvidos a partir do diretório do CSV.               |
| `revision`   | Sim      | SHA completo do commit do Git, com 40 ou 64 caracteres. Não há suporte para nomes de branch, tags nem hashes abreviados de commit. |
| `scope`      | Não       | Um diretório a ser verificado, com caminho relativo ao repositório. Omita o valor para verificar o repositório inteiro.                       |
| `mode`       | Não       | `standard` ou `deep`. Omita o valor para usar o modo selecionado no comando.                                   |
| `prompt`     | Não       | Instruções de varredura específicas para este repositório.                                                             |

Para encontrar o SHA completo do commit de um repositório local, execute:

```bash
git -C /path/to/repository rev-parse HEAD

## Executar uma campanha a partir de um CSV

Informe o CSV e um diretório de saída privado localizado fora dos repositórios:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

`--workers` controla as varreduras simultâneas de repositórios e tem `4` como padrão. Essa opção
não define o número de workers independentes de varredura padrão em cada varredura aprofundada;
configure esses limites por meio de
[`[deep_scan]`](/pt-BR/codex/security/cli/reference#configure-deep-scans). Use `--mode
deep` para selecionar a varredura aprofundada para linhas sem um `mode` próprio. Cada linha do CSV
ainda pode definir seu próprio modo de varredura e escopo do repositório.

Defina `[deep_scan].max_time_hours` para limitar a execução dos workers em cada varredura aprofundada da
campanha. A flag `--max-time-hours` funciona com `scan`, não com `bulk-scan`.

A CLI faz o checkout de cada revisão fixada, verifica o destino selecionado, registra o
resultado e remove o checkout temporário do repositório. Um repositório só é considerado
concluído quando sua varredura tem cobertura completa e todos os artefatos de resultado
obrigatórios estão presentes.

## Compartilhar contexto e instruções de segurança

Adicione documentos de arquitetura, modelos de ameaças ou políticas de segurança a cada varredura
com `--knowledge-base`. Repita a flag para adicionar mais arquivos ou diretórios:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Para adicionar instruções de varredura compartilhadas ou executar uma etapa de acompanhamento após cada varredura,
forneça arquivos de prompt:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --scan-prompt-file scan-instructions.md \
  --post-scan-prompt-file follow-up.md

A CLI acrescenta o `prompt` do CSV de cada repositório depois das instruções de varredura
compartilhadas. As instruções de acompanhamento são executadas na mesma sessão autenticada
após varreduras bem-sucedidas ou com cobertura incompleta ou erros, mas não
após um cancelamento ou uma varredura que atinja seu limite de custo. Os caminhos dos arquivos de prompt
são resolvidos a partir do diretório atual.

## Escolher um modelo e o esforço de raciocínio

Por padrão, as varreduras em massa usam `gpt-5.6-sol` com esforço de raciocínio `xhigh`. Para
escolher outro modelo e outro nível de esforço para uma campanha CSV:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --model gpt-5.6-terra \
  --effort high

As mesmas opções funcionam durante a descoberta interativa de repositórios:

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

Os níveis de esforço aceitos são `minimal`, `low`, `medium`, `high` e `xhigh`.

Para usar o OpenRouter ou o Fireworks, defina `OPENROUTER_API_KEY` ou `FIREWORKS_API_KEY`,
respectivamente, e especifique `--provider` e `--model`. Para consultar credenciais e
exemplos, veja a [configuração do OpenRouter ou do
Fireworks](/pt-BR/codex/security/cli/reference#use-openrouter-or-fireworks) ou a [configuração do
Amazon Bedrock](/pt-BR/codex/security/cli/reference#use-amazon-bedrock).

## Revisar os resultados da campanha

O diretório de saída contém a campanha com revisões fixadas, um registro de resultados
que só aceita acréscimos e artefatos separados para cada repositório e tentativa:

```text
security-scans/
├── manifest.json
├── results.jsonl
├── checkouts/
└── artifacts/
    ├── payments/
    │   └── attempt-1/
    │       ├── scan-manifest.json
    │       ├── findings.json
    │       ├── coverage.json
    │       └── report.md
    └── identity/
        └── attempt-1/
            ├── scan-manifest.json
            ├── findings.json
            ├── coverage.json
            └── report.md

- `manifest.json` registra os repositórios, as revisões fixadas, os escopos, os modos de
  varredura e as instruções compartilhadas ou específicas de cada repositório na campanha.
- `results.jsonl` registra cada tentativa referente a um repositório, seu status, o diretório de
  artefatos e quaisquer detalhes disponíveis sobre custos ou erros.
- `report.md` fornece um relatório legível para uma tentativa em um repositório.
- `findings.json` e `coverage.json` registram os achados e o escopo
  revisado dessa tentativa.

Exporte uma verificação de repositório concluída quando precisar de um resultado portátil:

```bash
npx @openai/codex-security export \
  /path/outside/repositories/security-scans/artifacts/payments/attempt-1 \
  --export-format sarif \
  --output /path/outside/repositories/payments.sarif

Os resultados podem conter trechos do código-fonte e detalhes de vulnerabilidades. Mantenha o
diretório de saída privado, fora dos repositórios verificados e sujeito a uma
política de retenção adequada.

## Retomar uma campanha

Execute o comando original com o mesmo CSV e o mesmo diretório de saída:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

A CLI retoma as verificações inacabadas dos repositórios e ignora as concluídas. As verificações
com cobertura incompleta não são executadas novamente. Os resultados continuam disponíveis, e
o comando retorna o código `2`.

Não altere o inventário de repositórios nem as instruções de verificação e acompanhamento de
um diretório de saída existente. A CLI verifica o manifesto fixado e rejeita uma
campanha diferente. Use um novo diretório de saída ao alterar repositórios,
revisões, escopos, modos de verificação ou instruções compartilhadas ou específicas de cada repositório.

## Tentar novamente após erros em repositórios

Use `--max-attempts` para tentar novamente em um repositório após um erro temporário de checkout ou de
verificação:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

Por padrão, é feita uma tentativa por repositório. Cada tentativa recebe seu próprio
recibo e diretório de artefatos. São feitas novas tentativas em caso de erros de checkout, falhas de verificação
e ausência de artefatos obrigatórios. Verificações concluídas com cobertura incompleta
não são executadas novamente.

As verificações em lote usam os seguintes códigos de saída:

| Código de saída | Significado                                                                                                               |
| --------- | --------------------------------------------------------------------------------------------------------------------- |
| `0`       | O processamento de todos os repositórios foi concluído com sucesso.                                                                              |
| `2`       | O processamento de um repositório não pôde ser concluído, uma verificação apresentou cobertura incompleta ou o comando encontrou um erro de entrada ou de execução. |
| `130`     | Ctrl-C interrompeu a campanha.                                                                                      |
| `143`     | SIGTERM encerrou a campanha.                                                                                      |

## Executar verificações em lote no Docker

O [repositório do
Codex Security](https://github.com/openai/codex-security) inclui uma configuração reforçada
do Compose para campanhas automatizadas com CSV em um host Linux com Docker. O
host deve oferecer suporte à criação não privilegiada de namespaces de usuário.

Mantenha o CSV de repositórios, os resultados das verificações e o estado de autenticação montados em
diretórios persistentes. Forneça as credenciais da OpenAI por meio do ambiente ou de um gerenciador de
segredos. Para repositórios privados do GitHub, forneça `GH_TOKEN` ou `GITHUB_TOKEN`
da mesma forma.

Execute a imagem com o CSV e o diretório de saída montados:

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

Use o mesmo CSV e o mesmo diretório de saída montados para retomar a campanha. Para o
GitHub Enterprise Server, defina `CODEX_SECURITY_GIT_HOST` como seu host do GitHub.

Para ver todas as flags disponíveis, consulte a [referência do comando
bulk-scan](/pt-BR/codex/security/cli/reference#codex-security-bulk-scan). Para tirar dúvidas comuns
sobre a cobertura das verificações e os achados, consulte as [perguntas frequentes da
CLI](/pt-BR/codex/security/cli/faq).

<!-- source: https://learn.chatgpt.com/pt-BR/docs/agent-configuration/agents-md -->

O Codex lê os arquivos `AGENTS.md` antes de iniciar qualquer trabalho. Ao organizar em camadas as orientações globais e as substituições específicas do projeto, você pode iniciar cada tarefa com expectativas consistentes, não importa qual repositório abra.

## Como o Codex localiza as orientações

Quando é iniciado, o Codex cria uma cadeia de instruções (uma vez por execução; na TUI, isso geralmente significa uma vez por sessão iniciada). A localização segue esta ordem de precedência:

1. **Escopo global:** No diretório inicial do Codex (por padrão, `~/.codex`, a menos que você defina `CODEX_HOME`), o Codex lê `AGENTS.override.md`, se esse arquivo existir. Caso contrário, o Codex lê `AGENTS.md`. Nesse nível, o Codex usa apenas o primeiro arquivo que não esteja vazio.
2. **Escopo do projeto:** A partir da raiz do projeto (normalmente, a raiz do Git), o Codex percorre os diretórios até chegar ao diretório de trabalho atual. Se não encontrar a raiz do projeto, o Codex verificará apenas o diretório atual. Em cada diretório do caminho, ele procura primeiro `AGENTS.override.md`, depois `AGENTS.md` e, por fim, qualquer nome alternativo definido em `project_doc_fallback_filenames`. O Codex inclui no máximo um arquivo por diretório.
3. **Ordem de mesclagem:** O Codex concatena os arquivos desde a raiz, separando-os com linhas em branco. Os arquivos mais próximos do diretório atual têm precedência sobre as orientações anteriores porque aparecem mais adiante no prompt combinado.

O Codex ignora arquivos vazios e para de adicionar arquivos quando o tamanho combinado atinge o limite definido por `project_doc_max_bytes` (32 KiB por padrão). Para saber mais sobre essas opções, consulte [Localização das instruções do projeto](/pt-BR/codex/config-file/config-advanced#project-instructions-discovery). Se atingir o limite, aumente-o ou distribua as instruções entre diretórios aninhados.

## Criar orientações globais

Defina orientações padrão persistentes no diretório inicial do Codex para que todos os repositórios herdem suas convenções de trabalho.

1. Verifique se o diretório existe:

   ```bash
   mkdir -p ~/.codex

2. Crie o arquivo `~/.codex/AGENTS.md` com preferências reutilizáveis:

   ```md
   # ~/.codex/AGENTS.md

   ## Working agreements

   - Always run `npm test` after modifying JavaScript files.
   - Prefer `pnpm` when installing dependencies.
   - Ask for confirmation before adding new production dependencies.

3. Execute o Codex em qualquer diretório para confirmar que ele carrega o arquivo:

   ```bash
   codex --ask-for-approval never "Summarize the current instructions."

   Resultado esperado: o Codex cita os itens de `~/.codex/AGENTS.md` antes de propor qualquer trabalho.

Use `~/.codex/AGENTS.override.md` quando precisar de uma substituição global temporária sem excluir o arquivo base. Remova a substituição para restaurar as orientações compartilhadas.

## Organizar as instruções do projeto em camadas

Os arquivos no nível do repositório mantêm o Codex ciente das convenções do projeto, e seus padrões globais continuam sendo herdados.

1. Na raiz do repositório, adicione um arquivo `AGENTS.md` que abranja a configuração básica:

   ```md
   # AGENTS.md

   ## Repository expectations

   - Run `npm run lint` before opening a pull request.
   - Document public utilities in `docs/` when you change behavior.

2. Adicione substituições em diretórios aninhados quando equipes específicas precisarem de regras diferentes. Por exemplo, em `services/payments/`, crie `AGENTS.override.md`:

   ```md
   # services/payments/AGENTS.override.md

   ## Payments service rules

   - Use `make test-payments` instead of `npm test`.
   - Never rotate API keys without notifying the security channel.

3. Inicie o Codex no diretório de pagamentos:

   ```bash
   codex --cd services/payments --ask-for-approval never "List the instruction sources you loaded."

   Resultado esperado: o Codex informa primeiro o arquivo global, depois o `AGENTS.md` na raiz do repositório e, por último, o arquivo de substituição do diretório de pagamentos.

O Codex interrompe a busca ao chegar ao diretório atual. Portanto, coloque os arquivos de substituição o mais próximo possível do trabalho especializado.

Veja a seguir um exemplo de repositório depois de adicionar um arquivo global e uma substituição específica para pagamentos:

## Adicionar regras de revisão de código

Para a [revisão de código do Codex no GitHub](/pt-BR/codex/third-party/github#customize-what-codex-reviews),
adicione uma seção `## Code Review Rules` ao arquivo `AGENTS.md` mais próximo do código ao qual essas
regras se aplicam. Coloque na raiz as verificações válidas para todo o repositório e, para cada serviço, coloque
as verificações específicas em um arquivo aninhado.

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Mantenha as regras concisas, explique o comportamento que deve ser sinalizado e qualquer abordagem segura ou
exceção e deixe as verificações de formatação e lint para a CI. Consulte [Personalizar o que
o Codex revisa](/pt-BR/codex/third-party/github#customize-what-codex-reviews) para
ver orientações sobre a configuração e a redação de regras.

## Personalizar nomes de arquivo alternativos

Se o repositório já usa outro nome de arquivo (por exemplo, `TEAM_GUIDE.md`), adicione-o à lista de nomes alternativos para que o Codex o trate como um arquivo de instruções.

1. Edite a configuração do Codex:

   ```toml
   # ~/.codex/config.toml
   project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
   project_doc_max_bytes = 65536

2. Reinicie o Codex ou execute um novo comando para carregar a configuração atualizada.

Agora, o Codex verifica cada diretório nesta ordem: `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md`. Nomes de arquivo que não estão nessa lista são ignorados durante a localização de instruções. O limite maior em bytes permite combinar mais orientações antes que elas sejam truncadas.

Com a lista de nomes alternativos configurada, o Codex trata os arquivos alternativos como instruções:

Defina a variável de ambiente `CODEX_HOME` quando quiser usar outro perfil, como o de um usuário de automação específico do projeto:

```bash
CODEX_HOME=$(pwd)/.codex codex exec "List active instruction sources"

Resultado esperado: a saída lista os arquivos usando caminhos relativos ao diretório `.codex` personalizado.

## Verificar sua configuração

- Execute `codex --ask-for-approval never "Summarize the current instructions."` na raiz de um repositório. O Codex deve exibir as orientações dos arquivos globais e do projeto na ordem de precedência.
- Use `codex --cd subdir --ask-for-approval never "Show which instruction files are active."` para confirmar que as substituições aninhadas têm precedência sobre regras de escopo mais amplo.
- Para auditar quais arquivos de instruções o Codex carregou, habilite um log da TUI em texto simples com `codex -c log_dir=./.codex-log` e consulte `./.codex-log/codex-tui.log`, ou inspecione o arquivo `session-*.jsonl` mais recente se você habilitou o registro de sessões.
- Se as instruções parecerem desatualizadas, reinicie o Codex no diretório de destino. O Codex recria a cadeia de instruções em cada execução (e no início de cada sessão da TUI), portanto, não há cache que precise ser limpo manualmente.

## Resolver problemas na localização de instruções

- **Nada é carregado:** Verifique se você está no repositório pretendido e se `codex status` informa a raiz esperada do workspace. Certifique-se de que os arquivos de instruções tenham conteúdo; o Codex ignora arquivos vazios.
- **Orientações incorretas são exibidas:** Procure um `AGENTS.override.md` em um nível superior da árvore de diretórios ou dentro do diretório inicial do Codex. Renomeie ou remova o arquivo de substituição para voltar a usar o arquivo normal.
- **O Codex ignora nomes alternativos:** Confirme que você listou os nomes em `project_doc_fallback_filenames` sem erros de digitação e reinicie o Codex para que a configuração atualizada entre em vigor.
- **Instruções truncadas:** Aumente o valor de `project_doc_max_bytes` ou distribua arquivos grandes entre diretórios aninhados para manter intactas as orientações essenciais.
- **Confusão entre perfis:** Execute `echo $CODEX_HOME` antes de iniciar o Codex. Um valor diferente do padrão faz o Codex usar outro diretório inicial, não aquele que você editou.

## Próximas etapas

- Acesse o site oficial do [AGENTS.md](https://agents.md) para saber mais.
- Consulte [Criação de prompts no Codex](/pt-BR/codex/prompting) para conhecer padrões de conversa que funcionam bem com orientações persistentes.

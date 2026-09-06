<!-- source: https://learn.chatgpt.com/pt-BR/docs/custom-prompts -->

Os prompts personalizados foram descontinuados. Use [Habilidades](/pt-BR/codex/build-skills) para criar instruções
  reutilizáveis que o Codex pode invocar de forma explícita ou implícita.

Os prompts personalizados (descontinuados) permitem transformar arquivos Markdown em prompts reutilizáveis que você pode invocar como comandos de barra tanto na CLI do Codex quanto na extensão para IDE do Codex.

Os prompts personalizados precisam ser invocados explicitamente e ficam no diretório inicial local do Codex (por exemplo, `~/.codex`), por isso não são compartilhados pelo repositório. Se quiser compartilhar um prompt (ou que o Codex o invoque implicitamente), [use Habilidades](/pt-BR/codex/build-skills).

1. Crie o diretório de prompts:

   ```bash
   mkdir -p ~/.codex/prompts

2. Crie `~/.codex/prompts/draftpr.md` com instruções reutilizáveis:

   ```markdown
   ---
   description: Prep a branch, commit, and open a draft PR
   argument-hint: [FILES=<paths>] [PR_TITLE="<title>"]
   ---

   Create a branch named `dev/<feature_name>` for this work.
   If files are specified, stage them first: $FILES.
   Commit the staged changes with a clear message.
   Open a draft PR on the same branch. Use $PR_TITLE when supplied; otherwise write a concise summary yourself.

3. Reinicie o Codex para que ele carregue o novo prompt (reinicie sua sessão da CLI e, se estiver usando a extensão para IDE, recarregue-a).

Resultado esperado: quando você digita `/prompts:draftpr` no menu de comandos de barra, seu comando personalizado aparece com a descrição do bloco de metadados e uma indicação de que os arquivos e o título da PR são opcionais.

## Adicione metadados e argumentos

O Codex lê os metadados do prompt e resolve os placeholders na próxima inicialização da sessão.

- **Descrição:** É exibida abaixo do nome do comando na janela pop-up. Defina-a no bloco de metadados YAML como `description:`.
- **Dica de argumentos:** Documente os parâmetros esperados usando `argument-hint: KEY=<value>`.
- **Placeholders posicionais:** Os placeholders de `$1` a `$9` são substituídos pelos argumentos separados por espaços que você fornece após o comando. `$ARGUMENTS` inclui todos eles.
- **Placeholders nomeados:** Use nomes em letras maiúsculas, como `$FILE` ou `$TICKET_ID`, e forneça os valores como `KEY=value`. Coloque entre aspas os valores com espaços (por exemplo, `FOCUS="loading state"`).
- **Sinais de cifrão literais:** Escreva `$$` para inserir um único `$` no prompt expandido.

Depois de editar os arquivos de prompt, reinicie o Codex ou abra um novo chat para que as atualizações sejam carregadas. O Codex ignora arquivos que não sejam Markdown no diretório de prompts.

## Invoque e gerencie comandos personalizados

1. No Codex (na CLI ou na extensão para IDE), digite `/` para abrir o menu de comandos de barra.
2. Digite `prompts:` ou o nome do prompt, por exemplo, `/prompts:draftpr`.
3. Forneça os argumentos necessários:

   ```text
   /prompts:draftpr FILES="src/pages/index.astro src/lib/api.ts" PR_TITLE="Add hero animation"

4. Pressione Enter para enviar as instruções expandidas (omita qualquer argumento de que não precisar).

Resultado esperado: o Codex expande o conteúdo de `draftpr.md`, substitui os placeholders pelos argumentos fornecidos e envia o resultado como uma mensagem.

Gerencie os prompts editando ou excluindo arquivos em `~/.codex/prompts/`. O Codex verifica apenas os arquivos Markdown no nível superior dessa pasta; portanto, coloque cada prompt personalizado diretamente em `~/.codex/prompts/`, e não em subdiretórios.

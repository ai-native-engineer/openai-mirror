<!-- source: https://learn.chatgpt.com/pt-BR/docs/github-action -->

Use a GitHub Action do Codex (`openai/codex-action@v1`) para executar o Codex em jobs de CI/CD, aplicar patches ou publicar revisões a partir de um fluxo de trabalho do GitHub Actions.
A ação instala a CLI do Codex, inicia o proxy da Responses API quando você fornece uma chave de API e executa `codex exec` com as permissões especificadas.

Use a ação quando quiser:

- Automatizar o feedback do Codex em pull requests ou versões sem precisar gerenciar a CLI.
- Impedir que alterações avancem sem passar por verificações de qualidade realizadas pelo Codex como parte do seu pipeline de CI.
- Executar tarefas repetíveis do Codex (revisão de código, preparação de versões e migrações) a partir de um arquivo de fluxo de trabalho.

Para ver um exemplo de CI, consulte [Modo não interativo](/pt-BR/codex/non-interactive-mode) e explore o código-fonte no [repositório openai/codex-action](https://github.com/openai/codex-action).

## Pré-requisitos

- Armazene sua chave da OpenAI como um segredo do GitHub (por exemplo, `OPENAI_API_KEY`) e faça referência a esse segredo no fluxo de trabalho.
- Execute o job em um runner Linux ou macOS. No Windows, defina `safety-strategy: unsafe`.
- Faça checkout do código antes de invocar a ação, para que o Codex possa ler o conteúdo do repositório.
- Escolha quais prompts deseja executar. Você pode fornecer texto inline por meio de `prompt` ou indicar um arquivo versionado no repositório com `prompt-file`.

## Exemplo de fluxo de trabalho

O fluxo de trabalho de exemplo abaixo revisa novas pull requests, captura a resposta do Codex e a publica na PR.

```yaml
name: Codex pull request review
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  codex:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      final_message: ${{ steps.run_codex.outputs.final-message }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: refs/pull/${{ github.event.pull_request.number }}/merge
          fetch-depth: 0
          persist-credentials: false

      - name: Run Codex
        id: run_codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt-file: .github/codex/prompts/review.md
          output-file: codex-output.md

  post_feedback:
    runs-on: ubuntu-latest
    needs: codex
    if: needs.codex.outputs.final_message != ''
    permissions:
      issues: write
      pull-requests: write
    steps:
      - name: Post Codex feedback
        uses: actions/github-script@v7
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: process.env.CODEX_FINAL_MESSAGE,
            });
        env:
          CODEX_FINAL_MESSAGE: ${{ needs.codex.outputs.final_message }}

Substitua `.github/codex/prompts/review.md` pelo seu próprio arquivo de prompt ou use a entrada `prompt` para fornecer texto inline. O exemplo também grava a mensagem final do Codex em `codex-output.md` para inspeção posterior ou upload como artefato.

## Configurar `codex exec`

Ajuste a execução do Codex definindo as entradas da ação que correspondem às opções de `codex exec`:

- `prompt` ou `prompt-file` (escolha uma opção): instruções inline ou o caminho, no repositório, de um arquivo Markdown ou de texto com sua tarefa. Considere armazenar os prompts em `.github/codex/prompts/`.
- `codex-args`: flags adicionais da CLI. Forneça um array JSON (por exemplo, `["--ephemeral"]`) ou uma string de shell (`--profile ci`) para configurar sessões, perfis ou configurações do MCP.
- `model` e `effort`: escolha a configuração desejada para o agente do Codex; deixe os campos em branco para usar os valores padrão.
- `sandbox`: escolha o modo Sandbox (`workspace-write`, `read-only`, `danger-full-access`) compatível com as permissões necessárias para o Codex durante a execução.
- `output-file`: salve a mensagem final do Codex em disco para que etapas posteriores possam fazer upload dela ou compará-la.
- `codex-version`: fixe uma versão específica da CLI. Deixe em branco para usar a versão publicada mais recente.
- `codex-home`: indique um diretório inicial compartilhado do Codex se quiser reutilizar arquivos de configuração ou configurações de MCP entre as etapas.

## Gerenciar privilégios

O Codex tem acesso amplo nos runners hospedados no GitHub, a menos que esse acesso seja restringido. Use estas entradas para controlar o nível de exposição:

- `safety-strategy` (padrão: `drop-sudo`) remove o `sudo` antes de executar o Codex. Essa remoção não pode ser desfeita durante o job e protege os segredos na memória. No Windows, você deve definir `safety-strategy: unsafe`.
- `unprivileged-user` combina `safety-strategy: unprivileged-user` com `codex-user` para executar o Codex usando uma conta específica. Verifique se o usuário pode ler e gravar no checkout do repositório (consulte o [exemplo de `unprivileged-user`](https://github.com/openai/codex-action/blob/main/examples/unprivileged-user.yml) para ver como ajustar a propriedade).
- `read-only` impede que o Codex altere arquivos ou acesse a rede, mas ele ainda é executado com privilégios elevados. Não confie apenas em `read-only` para proteger segredos.
- `sandbox` limita o acesso ao sistema de arquivos e à rede dentro do próprio Codex. Escolha a opção mais restritiva que ainda permita concluir a tarefa.
- `allow-users` e `allow-bots` restringem quem pode acionar o fluxo de trabalho. Por padrão, apenas usuários com acesso de gravação podem executar a ação; liste explicitamente outras contas confiáveis ou deixe o campo em branco para manter o comportamento padrão.

## Capturar saídas

A ação disponibiliza a última mensagem do Codex por meio da saída `final-message`. Mapeie-a para uma saída do job (como mostrado acima) ou processe-a diretamente em etapas posteriores. Combine `output-file` com o recurso de upload de artefatos se preferir coletar a transcrição completa do runner. Quando precisar de dados estruturados, passe `--output-schema` por meio de `codex-args` para impor um formato JSON.

## Lista de verificação de segurança

- Limite quem pode iniciar o fluxo de trabalho. Prefira eventos confiáveis ou aprovações explícitas, em vez de permitir que qualquer pessoa execute o Codex no seu repositório.
- Filtre as entradas de prompt provenientes de pull requests, mensagens de commit ou corpos de issues para evitar injeção de prompt. Revise comentários HTML ou texto oculto antes de fornecê-los ao Codex.
- Proteja sua `OPENAI_API_KEY` mantendo `safety-strategy` definido como `drop-sudo` ou executando o Codex como um usuário sem privilégios. Nunca deixe a ação no modo `unsafe` em runners compartilhados por vários locatários.
- Execute o Codex como a última etapa de um job para que etapas posteriores não herdem alterações de estado inesperadas.
- Faça a rotação das chaves imediatamente se suspeitar que os logs do proxy ou a saída da ação tenham exposto material sigiloso.

## Solução de problemas

- **Você definiu prompt e prompt-file**: remova a entrada duplicada para fornecer exatamente uma fonte.
- **responses-api-proxy não gravou as informações do servidor**: confirme se a chave de API está presente e é válida; o proxy só é iniciado quando você fornece `openai-api-key`.
- **Era esperado que `sudo` fosse removido, mas `sudo` funcionou**: verifique se nenhuma etapa anterior restaurou `sudo` e se o sistema operacional do runner é Linux ou macOS. Execute novamente em um novo job.
- **Erros de permissão após `drop-sudo`**: conceda acesso de gravação antes da execução da ação (por exemplo, com `chmod -R g+rwX "$GITHUB_WORKSPACE"` ou usando o padrão unprivileged-user).
- **Acionamento não autorizado bloqueado**: ajuste as entradas `allow-users` ou `allow-bots` se precisar permitir contas de serviço além dos colaboradores com permissão de gravação autorizados por padrão.

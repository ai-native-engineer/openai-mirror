<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/plugin/fix-findings -->

Use o Codex Security para transformar uma constatação de segurança aceita em um patch pontual e
verificado. Você pode usar o ambiente de trabalho do Codex Security ou executar o fluxo de remediação
a partir de um prompt, da linha de comando ou do CI/CD. O Codex valida o problema
e, quando é seguro e prático testar, adiciona um teste de regressão específico que
falha antes da correção e passa depois dela. Ele também verifica se o comportamento legítimo
continua funcionando. Se um teste de regressão não for seguro ou for inviável, o Codex
registra a lacuna de comprovação e fornece o artefato de validação reproduzível mais robusto
como alternativa.

Comece com uma única constatação aceita e revise o patch proposto e as evidências de
verificação. Se o fluxo atender aos seus padrões, processe as demais constatações aceitas
uma de cada vez, em tarefas separadas do Codex ou em jobs de CI/CD. Manter cada tarefa
com o escopo delimitado facilita a revisão das alterações no código e das evidências.

## Corrigir uma constatação na interface

Abra uma constatação aceita em **Constatações** ou uma varredura concluída em **Varreduras**.
Revise as evidências e use **Patch** para gerar, revisar, aplicar e verificar
uma correção pontual.

1. Gerar um patch pontual

   Abra a constatação, selecione a aba **Patch** e escolha **Gerar patch**.
   Quando viável, o Codex valida ou reproduz o problema e cria um artefato de patch
   sem modificar o checkout selecionado.

2. Revisar o diff proposto

   Leia cada arquivo-fonte alterado, cada teste de regressão e cada artefato de validação. Rejeite
refatorações abrangentes, limpezas de código não relacionadas ou alterações que enfraqueçam outro controle de
segurança.

3. Aplicar o patch localmente

   Selecione **Aplicar patch** somente quando o diff estiver aceitável. O Codex aplica exatamente
   o patch gerado à árvore de trabalho e registra esse estado. Revise o diff da
   árvore de trabalho antes de continuar.

4. Verificar a correção

   Selecione **Verificar correção**. O Codex executa novamente o reprodutor original ou o teste de exploração mais
   robusto disponível. Se um teste de regressão for seguro e prático, o Codex
   verifica se ele falha antes da correção e passa depois dela. Se o teste não for
   seguro ou for inviável, o Codex registra a lacuna de comprovação e fornece, como alternativa, o
   artefato de validação reproduzível mais robusto. Ele também verifica
   o comportamento legítimo, as formas de contornar a correção em áreas próximas e os testes relevantes do repositório.

5. Encerrar a constatação de forma deliberada

   A verificação não encerra uma constatação automaticamente. Revise os comandos,
os resultados e a lacuna de comprovação restante; depois, encerre a constatação com um motivo
preciso ou mantenha-a aberta para continuar o trabalho.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Revise a correção de segurança gerada antes de aplicá-la ao seu checkout.
  </figcaption>
</figure>

## Corrigir uma constatação pela CLI

Use a CLI do Codex para corrigir uma constatação aceita proveniente de uma varredura, um ticket, um boletim,
uma divulgação, uma avaliação de segurança ou uma revisão interna.

Instale o Codex Security no `CODEX_HOME` usado pelo `codex exec` antes de
executar esses comandos. Um runner novo de CI não inclui plug-ins do Marketplace por
padrão.

```text
Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.

Inclua a origem e o destino conhecidos, a entrada controlada pelo invasor, o impacto, o invariante esperado,
o reprodutor, os arquivos afetados e o comando de validação. O Codex pode inspecionar o
repositório para identificar detalhes técnicos ausentes. Ele deve perguntar antes de presumir uma
política do produto ou o invariante de segurança pretendido.

Para uma execução automatizada, faça checkout do código, disponibilize o relatório da constatação
e instale o plug-in no `CODEX_HOME` do runner. Depois, habilite a permissão de gravação no workspace
e passe o prompt para `codex exec`:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

## Executar a varredura e corrigir constatações no CI/CD

Instale o Codex Security no `CODEX_HOME` do runner antes de invocar qualquer uma das duas
habilidades. Os comandos abaixo usam o plug-in instalado; eles não o instalam.

No CI/CD, separe a varredura das alterações da remediação e exija que a varredura
mantenha o checkout inalterado. Preserve o diretório da varredura concluída como artefato do job,
revise as constatações e inicie uma tarefa separada do Codex ou um job separado para cada
constatação aceita para remediação.

Por padrão, `codex exec` usa um Sandbox somente leitura. Execute tanto a varredura das alterações quanto a
remediação com `--sandbox workspace-write`. A varredura precisa dessa permissão
para salvar artefatos temporários, mas o prompt ainda deve exigir `Do not modify
the checkout`. A remediação precisa da mesma permissão para gravar o patch
pontual e as evidências de verificação. Consulte [Permissões e
segurança](/pt-BR/codex/non-interactive-mode#permissions-and-safety).

Para cada varredura e constatação aceita:

1. Determine as revisões base e head da alteração.
2. Execute `$codex-security:security-diff-scan` nesse diff sem modificar
   o checkout.
3. Preserve o diretório completo da varredura e selecione as constatações a corrigir.
4. Invoque `$codex-security:fix-finding` uma vez para cada constatação aceita, informando
   o ID da constatação e o diretório da varredura concluída.
5. Gere um patch pontual e adicione um teste de regressão que falhe antes da
correção e passe depois dela. Se esse teste não for seguro ou for inviável, registre a
lacuna de comprovação e use, como alternativa, o artefato de validação reproduzível mais robusto.
6. Verifique o problema original e o comportamento legítimo. Retorne separadamente cada patch, teste
ou artefato alternativo de validação, o comando de verificação e qualquer lacuna de
comprovação.

Primeiro, faça a varredura da alteração sem modificar o checkout:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:security-diff-scan to review changes from <base-revision> to <head-revision> for security regressions. Do not modify the checkout.'

Depois, corrija uma constatação aceita da varredura concluída:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <completed-scan-directory>. Validate the finding, generate one minimal patch, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

Repita o segundo comando em uma tarefa ou um job independente para cada constatação
aceita restante. Após a verificação, integre cada patch por meio do seu processo normal de
revisão de código e lançamento. Para repassar as constatações a outra equipe antes da
remediação, consulte [Exportar ou acompanhar
constatações](/pt-BR/codex/security/plugin/export-findings).

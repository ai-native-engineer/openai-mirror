<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/scan-code-changes-for-security -->

## Revise a alteração, não o repositório inteiro

Use uma análise de segurança do diff quando um pull request, commit, branch ou patch local
alterar um caminho de código sensível. O Plugin Codex Security usa o contexto do repositório
para entender a alteração e, em seguida, concentra a identificação dos achados e sua validação
no diff e no código diretamente relacionado.

Esse fluxo de trabalho complementa a revisão de código convencional. Use-o quando quiser evidências
sobre regressões de segurança, e não uma revisão geral de estilo ou de testes.

## Faça uma análise direcionada

1. Abra o repositório e faça checkout do conjunto exato de alterações gerenciado pelo Git que será revisado ou descreva-o.
2. Conclua as etapas do [Início rápido do Plugin Codex Security](/pt-BR/codex/security/plugin) e especifique no prompt inicial o pull request, commit, diff de branch ou patch da árvore de trabalho.
3. Indique as superfícies de alto risco na alteração, como autenticação, analisadores sintáticos, caminhos de arquivos, solicitações de rede ou tratamento de credenciais.
4. Execute o prompt sem solicitar uma correção, para que o primeiro resultado permaneça um artefato de revisão.
5. Verifique cada linha indicada como afetada, cada resultado da validação e cada lacuna de evidências informada antes de decidir se é preciso corrigir o problema.

## Dê seguimento a um achado

Um relatório útil diferencia um achado de segurança em um caminho alcançável e respaldado por evidências de uma
suspeita que ainda precisa de confirmação. Ele também pode incluir comentários inline no código
nas linhas afetadas. Para agir com base no resultado, abra uma nova tarefa com escopo delimitado
para corrigir o problema, usando o identificador do achado ou a seção relevante do relatório.
Consulte [Corrigir um backlog de vulnerabilidades](/pt-BR/codex/use-cases/remediate-vulnerability-backlog)
para conhecer o ciclo de correção e validação.

Para saber mais sobre seletores de alterações, escopo do diff e revisão dos resultados, consulte [Revisar alterações de código
quanto à segurança](/pt-BR/codex/security/plugin/code-changes).

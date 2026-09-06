<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/plugin/workbench -->

A área de trabalho do Codex Security reúne suas varreduras, seus achados e seus repositórios
no aplicativo Codex para desktop. O Codex analisa a varredura em uma tarefa comum, enquanto
a área de trabalho mantém a varredura e os resultados disponíveis para quando você voltar.

No aplicativo do ChatGPT para desktop, abra o menu suspenso do ChatGPT e selecione **Codex**.
Instale e ative o [Plugin Codex Security](/pt-BR/codex/security/plugin) e,
em seguida, selecione **Segurança** na barra lateral.

  Se **Segurança** não aparecer, confirme se **Codex** está selecionado e se o
  plug-in está instalado e ativado. Se necessário, atualize o aplicativo para desktop e o plug-in
  e verifique se o administrador do seu workspace permite o uso do plug-in.

## Iniciar uma varredura

Para obter a melhor qualidade de varredura, use <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
com o nível de esforço de raciocínio `xhigh`.

1. Abra **Varreduras** e selecione **+ Varredura**.
2. Selecione um repositório existente ou escolha outra pasta.
3. Escolha **Base de código** para fazer a varredura de um repositório ou **Alterações** para revisar uma
   alteração com controle de versão pelo Git.
4. Para uma varredura padrão da base de código, selecione todo o repositório ou uma pasta.
5. Para uma varredura aprofundada, primeiro selecione o repositório ou a pasta como base de código e depois
   ative **Varredura aprofundada**. As varreduras aprofundadas analisam toda a base de código selecionada.
6. Para uma varredura de alterações, selecione alterações sem commit, um commit ou um intervalo de
   revisões. A opção **Varredura aprofundada** não está disponível para varreduras de alterações.
7. Escolha um modelo e um nível de esforço de raciocínio. Abra **Contexto adicional** para descrever
   vetores de ataque relevantes, áreas de foco ou outro contexto de segurança.
8. Selecione **Iniciar varredura**.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Escolha um repositório e configure uma varredura na área de trabalho do Codex Security.
  </figcaption>
</figure>

Consulte [Executar uma verificação de segurança](/pt-BR/codex/security/plugin/scans), [Executar uma varredura de segurança
aprofundada](/pt-BR/codex/security/plugin/deep-scans) ou [Revisar alterações no código quanto à
segurança](/pt-BR/codex/security/plugin/code-changes) para ver detalhes de cada tipo de
varredura.

## Acompanhar o progresso da varredura

A página da varredura mostra a fase atual e o andamento informado pelo plug-in.
Em uma varredura padrão, as fases incluem modelagem de ameaças, descoberta, validação,
análise de impacto e de caminhos, geração de relatórios e finalização.

Selecione **Ver atividade** para abrir a tarefa do Codex que executa a varredura. Você pode
sair da área de trabalho e voltar para **Varreduras** sem perder uma varredura salva. Se quiser
interromper a execução, abra a varredura e selecione **Interromper varredura**.

Quando a varredura for concluída, abra os resultados para revisar o alvo, a revisão,
os achados, a cobertura e os artefatos de relatório disponíveis.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Revise os achados, a gravidade, a cobertura da varredura e os artefatos depois que uma varredura
for concluída.
  </figcaption>
</figure>

## Revisar achados de diferentes varreduras

Abra **Achados** para examinar os achados salvos em diferentes repositórios e varreduras.
Pesquise ou filtre a lista e selecione um achado para revisar o resumo, as
evidências do código-fonte, a validação e o impacto.

Use **Resumo** para ver os detalhes do achado e **Patch** quando quiser gerar,
revisar, aplicar ou verificar uma correção direcionada. Consulte [Corrigir e verificar achados de
segurança](/pt-BR/codex/security/plugin/fix-findings) para conhecer o fluxo de trabalho de remediação.

  A aba **Achados** mostra os achados das varreduras salvas do Codex Security. Tickets importados
  e outras issues de segurança existentes continuam fazendo parte de um processo separado, o
[fluxo de trabalho de triagem do backlog](/pt-BR/codex/security/plugin/triage-backlog).

## Inspecionar o histórico do repositório

Abra **Repositórios** para explorar os repositórios e as pastas disponíveis. Selecione um
repositório para examinar o histórico de varreduras, a última revisão analisada e os
achados em aberto. Nos detalhes do repositório, abra uma varredura anterior ou veja os achados
associados a esse repositório.

Se um repositório não tiver varreduras, inicie uma varredura nos detalhes do repositório ou selecione **+ Varredura**
na área de trabalho.

## Iniciar uma varredura a partir de uma conversa

Você também pode pedir ao Codex para executar o Plugin Codex Security instalado em uma
conversa comum. As varreduras que usam a área de trabalho compartilhada do plug-in aparecem em **Varreduras**,
para que você possa voltar a acompanhar o progresso e consultar os resultados na área de trabalho do Codex Security.

Para varreduras no terminal e automação, consulte o [Início rápido da CLI
do Codex Security](/pt-BR/codex/security/cli).

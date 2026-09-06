<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/plugin/export-findings -->

Use uma verificação concluída do Codex Security em um destes dois fluxos:

- **Exportar** cria um arquivo portátil JSON, CSV ou SARIF.
- **Acompanhar achados** prepara os achados selecionados
  como issues no Linear, GitHub ou Jira, ou como um único rascunho privado de aviso de segurança do GitHub. O Codex
  verifica se há duplicatas e aguarda sua aprovação antes de gravar.

Nenhum dos fluxos de trabalho altera o pacote lacrado da verificação.

  Os links de artefatos e os formatos de exportação disponíveis dependem da interface do Codex que você usa e
  da versão instalada do plug-in. Consulte o [registro de alterações
  do plug-in](/pt-BR/codex/security/plugin/changelog) antes de usar um formato
  em uma automação.

## Exportar um artefato portátil

No aplicativo para desktop, abra uma verificação concluída em **Segurança** \> **Verificações**. Use os
links de artefatos disponíveis para inspecionar `report.md`, `findings.json`,
`scan-manifest.json`, `coverage.json` ou um relatório SARIF, se estiver disponível.

Para criar outro formato compatível, peça ao Codex que exporte os achados da
verificação concluída sem modificar o pacote lacrado:

```text
Export the findings from [completed scan directory] as [JSON, CSV, or SARIF]. Do not modify the sealed scan bundle or upload its contents.

Escolha o formato adequado ao destino:

| Formato | Finalidade                                                        |
| ------ | ----------------------------------------------------------------- |
| JSON   | Preserve os achados estruturados e lacrados para uso em ferramentas e scripts.    |
| CSV    | Revise os achados e o estado atual da triagem local em uma planilha.  |
| SARIF  | Envie os achados a ferramentas compatíveis com o formato de intercâmbio SARIF. |

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Abra o artefato de cobertura, o de achados, o manifesto da verificação, o relatório Markdown ou o artefato
SARIF de uma verificação concluída.
  </figcaption>
</figure>

Selecione **Relatório Markdown** para abrir `report.md` no editor externo
configurado. O editor usado depende das configurações do sistema; o exemplo abaixo mostra o
conteúdo do relatório gerado.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Revise o escopo da verificação, o modelo de ameaças, os achados validados e os
links para relatórios detalhados no relatório Markdown gerado.
  </figcaption>
</figure>

Use o caminho retornado para o artefato. Se outra ferramenta precisar do contexto completo da
verificação, mantenha juntos os arquivos originais `scan-manifest.json`, `findings.json` e
`coverage.json`. A exportação não envia os achados a um serviço
de análise de código.

## Acompanhar achados selecionados

Execute `$codex-security:track-findings` com um achado validado ou com um
lote selecionado explicitamente com até 25 achados da mesma verificação lacrada. Cada
execução usa um único provedor e um único destino. Um rascunho privado de aviso de segurança do
GitHub aceita apenas um achado.

Para preparar uma issue no Linear, envie:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for the Linear team [team] and project [project, if
any]. Check for duplicates and show me the exact issue title, body, metadata,
and destination. Do not create or update anything until I approve that payload.

Para preparar uma issue no GitHub, envie:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for GitHub repository [owner/repository]. Check open
and closed issues for duplicates and show me the exact issue title, body,
metadata, repository visibility, and authenticated transport. Do not create or
update anything until I approve that payload.

Para preparar uma issue no Jira, envie:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for Jira project [project key] as [issue type].
Check for duplicates and show me the exact issue summary, description,
metadata, and destination. Do not create or update anything until I approve
that payload.

O acompanhamento no Jira requer o plug-in Atlassian Rovo no Codex. Reutilizar uma issue
requer acesso de leitura; criar ou atualizar uma issue requer acesso de leitura e gravação.

Para preparar um rascunho privado de aviso de segurança do GitHub, envie:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] as a private draft GitHub Security Advisory in
[owner/repository]. Verify the sealed source revision, repository, affected
paths, package metadata, and duplicate state. Show me the exact advisory
payload, authenticated GitHub CLI identity, and disclosure warnings. Do not
create anything until I approve that payload.

  Os rascunhos de avisos exigem um achado de uma verificação `git_revision` lacrada, o
  repositório de origem canônico, público e verificado e acesso de administrador. O
  fluxo não processa avisos em lote, nem os atualiza, publica ou fecha. Use um
  destino aprovado para issues privadas quando a origem não atender a esses requisitos.

## Revise a gravação proposta

1. Confirme se o ID e a impressão digital do achado vieram da verificação lacrada correta.
2. Confirme o provedor, a equipe exata do Linear, o repositório do GitHub, o projeto do Jira ou
o repositório do aviso de segurança, além da visibilidade efetiva do destino.
3. Revise o resultado da verificação de duplicatas: `create`, `reuse`, `update` ou `blocked`.
4. Leia na íntegra o título, o corpo, os locais no código-fonte e os metadados do provedor
propostos. Remova detalhes do exploit ou evidências internas que o destino
não deva expor.
5. Aprove somente esse payload exato. Qualquer alteração no destino, na visibilidade, no conjunto de achados
ou no corpo exige uma nova prévia.

Achados sensíveis devem ser enviados a um destino privado. Criar uma issue em um
repositório interno ou público do GitHub exige um aviso explícito sobre visibilidade
e a aprovação de todo o conteúdo. Considere que a descrição de um rascunho de aviso acabará
se tornando pública e remova credenciais, evidências privadas e detalhes desnecessários
do exploit antes da aprovação.

Revise e aprove as ações externas na conversa do Codex. A aprovação
não cria uma tela separada para a issue ou o aviso na área de trabalho de Segurança.

## Verifique o item acompanhado

Depois de aprovar a gravação proposta, o Codex verifica novamente a origem lacrada,
o destino, o acesso e o estado das duplicatas. Em um lote, ele processa os achados
um de cada vez e para no primeiro resultado incerto. A criação, a atualização ou a
reutilização só é concluída depois que o Codex relê a issue exata e verifica seus
identificadores de vinculação e seu conteúdo.

Guarde a URL canônica retornada da issue ou do aviso junto ao seu registro de triagem.
Prossiga com [Corrigir e verificar um achado](/pt-BR/codex/security/plugin/fix-findings)
quando o responsável aceitar o item para remediação.

<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/plugin/triage-backlog -->

Use `$codex-security:triage-finding` para revisar os achados de segurança existentes
com base no repositório atual. Este fluxo de trabalho realiza uma análise estática
somente leitura: o Codex trata cada achado como uma alegação não comprovada e examina as
evidências do repositório sem executar o código.

Execute este fluxo de trabalho em um projeto do Codex com escopo restrito ao repositório que você quer
avaliar. O Codex precisa conseguir ler o código-fonte do repositório. Os conectores do Jira e do Linear
podem fornecer dados dos achados, enquanto os achados do GitHub exigem acesso autenticado à
API REST do GitHub. Nenhuma dessas opções substitui o acesso ao código-fonte.

Nos bastidores, o Codex começa pelo código citado ou pelas informações de versão citadas. Ele
rastreia a origem supostamente controlada pelo invasor, os controles de segurança relevantes,
o sink perigoso e o caminho alcançável. Também verifica a superfície do produto e a fronteira de
confiança, procura evidências contraditórias e registra lacunas de comprovação. Em seguida, o Codex retorna
um veredito por achado e classifica os achados que exigem ação ou revisão
adicional.

Isso é diferente de `$codex-security:validation`, que pode compilar ou executar código,
criar um teste específico ou uma prova de conceito, ou usar uma interface real para
reproduzir ou refutar um achado. Use a triagem para classificar e ordenar um
backlog existente. Use a validação quando evidências obtidas em execução puderem esclarecer um achado
cuja avaliação permanece inconclusiva com as evidências estáticas.

  A triagem do backlog parte dos achados existentes. Para procurar novas
  vulnerabilidades no repositório, [execute uma verificação de segurança](/pt-BR/codex/security/plugin/scans). A triagem
  não modifica o repositório nem implementa correções.

## Escolha os achados para a triagem

Você pode fornecer um achado ou uma coleção de achados destas fontes:

| Fonte                   | O que fornecer                                                                                                                                                                                                                                                                                                                                                                                                                                        | Requisitos                                                                                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Achados colados ou locais | Resultados SARIF, um CVE ou GHSA, um aviso de segurança, um ticket de scanner, um relatório de bug bounty, um artefato de achado do Codex Security ou uma alegação de vulnerabilidade em linguagem simples.                                                                                                                                                                                                                                                                                          | Nenhum conector é necessário.                                                                                                                                                                           |
| Jira ou Linear           | URLs ou identificadores exatos de issues de segurança ou vulnerabilidade, uma consulta JQL do Jira ou uma equipe, um projeto ou um termo de pesquisa do Linear. Antes da triagem, o Codex recupera o conteúdo das issues selecionadas.                                                                                                                                                                                                                                                                            | [Jira via Atlassian Rovo](codex://plugins/plugin_connector_692de805e3ec8191834719067174a384) ou [Linear](codex://plugins/plugin_asdk_app_69a089a326dc8191b32a3f2553f5be2c) com acesso de leitura. |
| GitHub                   | Um repositório e uma fonte de achados: verificação de código, vulnerabilidades e malware do `Dependabot`, avisos de segurança e relatórios privados de vulnerabilidade ou todas as fontes. Se você não especificar um repositório, o Codex usará, quando disponível, o repositório do GitHub vinculado ao projeto atual do Codex. As issues do GitHub não estão incluídas nas fontes padrão do GitHub; forneça uma issue específica ou solicite explicitamente as issues do GitHub quando quiser fazer a triagem delas. | Acesso autenticado à API REST do GitHub, por exemplo, usando `gh auth token`, `GH_TOKEN` ou `GITHUB_TOKEN`, com permissão de leitura para o repositório e o tipo de achado selecionados.                                      |

O Codex mantém um resultado para cada achado fornecido, na ordem de entrada, para que cada
achado de origem continue rastreável. Ele não mescla nem descarta achados que parecem
ser duplicados.

## Execute uma triagem somente leitura

Para achados colados ou artefatos locais, envie um prompt como este:

```text
Use $codex-security:triage-finding to triage these existing security findings against this repository:

[Paste the findings or provide the artifact path.]

Para issues do Jira ou do Linear, identifique o conjunto de issues e mantenha o sistema de origem no modo
somente leitura:

```text
Use $codex-security:triage-finding to import and triage the security findings from [Jira or Linear issue URLs, identifiers, or query] against this repository.
Do not change the source issues.

Para achados do GitHub, informe o repositório e a fonte dos achados:

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from [owner/repository] against this repository.

Para usar o repositório do GitHub vinculado ao projeto atual do Codex, especifique
apenas a fonte dos achados:

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from GitHub against this repository. Use the GitHub repository attached to the current Codex project.

O fluxo de trabalho segue esta ordem:

1. Colete e organize os achados

   O Codex recupera todo o conteúdo solicitado de issues ou do GitHub, preserva os identificadores
e as referências da fonte e cria um item de triagem para cada entrada. Ele monta
a lista completa de itens antes de atribuir os vereditos.

2. Confirme o contexto do repositório

   O Codex identifica o repositório e a revisão atuais, quando disponíveis. Ele lê
`SECURITY.md`, quando presente, para que as versões com suporte, as entradas confiáveis, os
   limites do produto e as superfícies fora do escopo orientem a avaliação.

3. Inspecione as evidências estáticas

   Para cada achado, o Codex rastreia a origem supostamente controlada pelo invasor,
o controle de segurança relevante, o sink vulnerável, o caminho alcançável e a fronteira de
segurança contemplada. Ele registra as evidências que sustentam a alegação, as evidências contrárias a
ela e as lacunas de comprovação.

4. Atribua vereditos e posições no ranking

   O Codex atribui um veredito e um nível de confiança a cada achado. Ele classifica
os achados com veredito `confirmed` e `needs_review` por explorabilidade em filas separadas.

## Revise os resultados

| Veredito          | O que significa                                                                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `confirmed`      | As evidências do repositório mostram que o caminho vulnerável é alcançável sob as precondições declaradas e atravessa uma fronteira de segurança contemplada.                     |
| `not_actionable` | As evidências do repositório descartam a alegação, por exemplo, ao mostrar uma versão não afetada, um caminho inalcançável, uma proteção eficaz ou uma superfície que não faz parte do produto distribuído.                 |
| `needs_review`   | As evidências do repositório não bastam para uma decisão porque as informações necessárias estão ausentes, são ambíguas ou dependem da execução, do ambiente ou de políticas. |

  As posições no ranking de explorabilidade são números inteiros positivos a partir de `1`, atribuídos de forma independente
  em cada fila de veredito. Assim, as prioridades de correção ficam separadas do
  trabalho de revisão pendente. A posição `1` corresponde ao achado com veredito `confirmed` mais explorável
  ou ao achado com veredito `needs_review` de maior prioridade nesse conjunto de resultados. Essa posição
  não é uma pontuação de gravidade do scanner, e os achados com veredito `not_actionable` não recebem posição no ranking.

Para cada achado, revise:

- a justificativa do veredito e da posição no ranking
- as evidências que sustentam a alegação e as que a contradizem
- as perguntas em aberto e as lacunas de comprovação restantes
- o local e o componente afetados
- a superfície do produto e o nível de confiança da origem
- a próxima etapa recomendada
- o encaminhamento para [`$codex-security:fix-finding`](/pt-BR/codex/security/plugin/fix-findings),
  quando o achado tiver o veredito `confirmed`

A triagem é concluída quando cada achado fornecido tem um resultado, o Codex preserva
o respectivo identificador da fonte e toda incerteza fica explícita. Os registros do Jira e do Linear, além de outros
registros de backlog, permanecem inalterados, a menos que você peça ao Codex para atualizá-los depois de
revisar os resultados da triagem.

## Próximas etapas

- `confirmed`: Depois que uma pessoa aceitar o achado para correção, use
[`$codex-security:fix-finding`](/pt-BR/codex/security/plugin/fix-findings) para corrigi-lo e
  verificá-lo. A triagem prepara um encaminhamento pronto para ser usado em um prompt, mas não invoca a habilidade
  automaticamente.
- `needs_review`: Se a execução do código puder resolver a lacuna de comprovação, use
`$codex-security:validation` para realizar uma validação dinâmica de escopo delimitado. Passe para a validação, com base no resultado da triagem,
  a alegação do achado, os locais afetados, as precondições, as evidências estáticas e as
  lacunas de comprovação:

  ```text
  Use $codex-security:validation to dynamically validate finding [triage item ID or source ID] from the backlog triage result. Use the strongest realistic, bounded method, record exactly what was tested, and preserve any remaining proof gaps.

  Ao contrário da triagem, a validação pode compilar ou executar código, criar um teste específico ou
  uma prova de conceito, ou interagir com uma interface real. Revise os comandos propostos
  antes de aprová-los e mantenha em vigor as [políticas de aprovação e segurança
  do Codex](/pt-BR/codex/agent-approvals-security).

- `needs_review`: Se o achado depender da política do produto ou do contexto de
  implantação, responda às perguntas em aberto listadas antes de alterar o código.
- `not_actionable`: Mantenha as evidências junto ao registro da triagem. O Codex não
  fecha nem atualiza o ticket de origem automaticamente.
- Para procurar vulnerabilidades além das incluídas no backlog fornecido, [execute uma verificação
  de segurança](/pt-BR/codex/security/plugin/scans).

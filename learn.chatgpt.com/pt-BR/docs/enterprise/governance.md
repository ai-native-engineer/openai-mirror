<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/governance -->

A governança da atividade do Codex abrange análises interativas, geração programática
de relatórios, controles relacionados ao uso do ChatGPT e registros de auditoria. Escolha a
interface adequada à questão; os dados de análise e de conformidade têm
finalidades diferentes.

<a id="governance-and-observability"></a>
<a id="ways-to-track-codex-usage"></a>

| Se você precisa                                          | Comece por                                                                |
| ------------------------------------------------------- | ------------------------------------------------------------------------- |
| Entender a adoção em todo o ChatGPT                      | [Análises do workspace](/pt-BR/codex/enterprise/workspace-analytics)              |
| Analisar interativamente a adoção e a atividade do Codex        | [Análises do Codex](#analytics-dashboard)                                   |
| Carregar relatórios agregados do Codex em outro sistema     | [Analytics API](/pt-BR/codex/enterprise/analytics-api)                          |
| Exportar registros para auditoria ou investigação               | [API de Compliance](/pt-BR/codex/enterprise/compliance-api)                        |
| Analisar os controles de créditos do workspace do ChatGPT que dependem do plano | [Limites de uso e controles de gastos do ChatGPT](/pt-BR/codex/enterprise/usage-limits) |

## Acesse as interfaces de administração

- Acesse [Análises do workspace](https://chatgpt.com/admin/usage) para consultar relatórios interativos
  do workspace. O [guia de análises do workspace](https://help.openai.com/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu)
  descreve as funções e visualizações atuais.
- Acesse a [referência da Codex Analytics API](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)
  quando precisar gerar relatórios de forma programática e agendada.
- Acesse a [referência da Admin API](https://chatgpt.com/public/admin/api-reference)
  e o [guia da Plataforma de conformidade](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)
  para integrações de auditoria e investigação.

Por exemplo, use as análises do workspace para verificar rapidamente a adoção, a Analytics API
para carregar relatórios agregados do Codex em um sistema de inteligência de negócios
e a API de Compliance para enviar registros auditáveis a um SIEM ou a um fluxo de trabalho de
descoberta eletrônica.

## Painel de análises

<a id="dashboard-views"></a>
<a id="data-export"></a>

O ChatGPT oferece análises de todo o workspace para acompanhar de forma ampla a adoção e o engajamento.
As análises do Codex se concentram na atividade do Codex. Ambas são interfaces interativas de
relatórios, não logs brutos de auditoria.

Use [Análises do workspace](/pt-BR/codex/enterprise/workspace-analytics) para comparar as
duas experiências e encontrar as fontes atuais mantidas pelos responsáveis por cada uma. Você também pode
acessar [Análises do workspace](https://chatgpt.com/admin/usage) diretamente. Não
baseie um contrato estável de geração de relatórios nos rótulos do painel nem nos campos dos relatórios
baixados; eles podem mudar à medida que o produto evolui.

## Controles relacionados ao uso do ChatGPT

Os controles de uso do workspace do ChatGPT são separados das análises e não
configuram os direitos de acesso aos recursos. Dependendo do plano, atividades elegíveis do Codex
podem consumir créditos do workspace do ChatGPT e, quando os limites se esgotam, o acesso a
recursos elegíveis pode ser suspenso. Esses controles não definem um limite universal para o Codex nem regem
o faturamento da API da plataforma.

Consulte [Limites de uso e controles de gastos do ChatGPT](/pt-BR/codex/enterprise/usage-limits)
para conhecer o escopo estável desses controles e consultar as fontes atuais da Central de Ajuda.

## Analytics API

<a id="what-it-measures"></a>
<a id="endpoints"></a>
<a id="usage"></a>
<a id="code-review-activity"></a>
<a id="user-engagement-with-code-review"></a>
<a id="how-it-works"></a>
<a id="common-use-cases"></a>

Use a Analytics API para gerar relatórios agregados do Codex de forma programática. Ela é
indicada para armazéns de dados, sistemas de inteligência de negócios e relatórios
internos que não devem depender de um painel interativo.

A referência da API é a fonte oficial sobre requisitos de acesso, rotas, esquemas,
campos, períodos cobertos pelos relatórios e paginação. Consulte
[Analytics API](/pt-BR/codex/enterprise/analytics-api) para ver o escopo conceitual da integração
e o link para a referência canônica.

## API de Compliance

<a id="what-it-measures-1"></a>
<a id="what-you-can-export"></a>
<a id="activity-logs"></a>
<a id="metadata-for-audit-and-investigation"></a>
<a id="common-use-cases-1"></a>
<a id="what-it-does-not-provide"></a>

Use a API de Compliance em fluxos de trabalho de segurança, jurídicos e de governança que precisam de
registros auditáveis. Ela não é um painel de adoção nem de produtividade.

A referência da API é a fonte oficial sobre cobertura de eventos, esquemas, permissões,
filtros, retenção e comportamento das requisições. Consulte
[API de Compliance](/pt-BR/codex/enterprise/compliance-api) para ver o escopo conceitual
da integração e o link para a referência canônica.

<a id="recommended-pattern"></a>

Para definir a sequência de implementação e fazer verificações nessas interfaces, use o
[Guia de implementação para administradores](/pt-BR/codex/enterprise/admin-setup).

## Documentação relacionada

- [Guia de implementação para administradores](/pt-BR/codex/enterprise/admin-setup)
- [Análises do workspace](/pt-BR/codex/enterprise/workspace-analytics)
- [Analytics API](/pt-BR/codex/enterprise/analytics-api)
- [API de Compliance](/pt-BR/codex/enterprise/compliance-api)

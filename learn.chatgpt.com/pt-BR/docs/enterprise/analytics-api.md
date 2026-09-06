<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/analytics-api -->

A Codex Analytics API fornece métricas agregadas de uso e atividade do Codex para
um workspace do ChatGPT.

A [referência da Codex Analytics API](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)
é a fonte oficial sobre os requisitos de acesso atuais, as rotas, os esquemas de requisição e
resposta, as métricas, a semântica temporal e a paginação.

## Quando usar a Analytics API

A Analytics API é indicada quando você precisa:

- Automatizar a geração recorrente de relatórios do Codex.
- Combinar métricas agregadas do Codex com dados internos da organização.
- Criar uma camada controlada de geração de relatórios para públicos aprovados.
- Evitar acoplar uma integração a um painel interativo.

Não é uma interface para logs brutos de auditoria. Use a
[API de Compliance](/pt-BR/codex/enterprise/compliance-api) quando o fluxo de trabalho exigir
registros auditáveis de atividades.

## Confirme os limites administrativos

Os resultados da Analytics API têm como escopo um workspace do ChatGPT, mas as requisições
são autenticadas com uma chave de API de uma organização da Plataforma. A organização à qual a chave pertence deve
corresponder à organização associada ao workspace.

A referência da API é a fonte oficial das informações atualizadas sobre o provisionamento de chaves, os requisitos de escopo,
as rotas, os esquemas, os campos, a semântica temporal e o comportamento da paginação. Esta página
não reproduz esse contrato.

## Documentação relacionada

- [Análises do workspace](/pt-BR/codex/enterprise/workspace-analytics)
- [Guia de implementação para administradores](/pt-BR/codex/enterprise/admin-setup)
- [Governança](/pt-BR/codex/enterprise/governance)
- [API de Compliance](/pt-BR/codex/enterprise/compliance-api)

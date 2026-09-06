<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/workspace-analytics -->

Use as análises do workspace do ChatGPT para acompanhar a adoção geral no workspace. Use as análises
do Codex para gerar relatórios voltados ao Codex. Use a Analytics API para obter dados
agregados de forma programática e a API de Compliance para consultar registros auditáveis.

Essas opções de geração de relatórios não concedem acesso aos produtos nem definem políticas de execução. Consulte
[Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions)
para conhecer os limites de administração.

## Escolha uma opção de geração de relatórios

| Opção                     | Finalidade                                                    | Responsável pelo contrato                                                                                                         |
| --------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Análises do workspace do ChatGPT | Relatórios interativos sobre adoção e engajamento em todo o workspace | [Orientações da Central de Ajuda sobre análises do workspace](https://help.openai.com/en/articles/10875114)                               |
| Análises do Codex             | Relatórios interativos voltados à adoção e à atividade no Codex  | O [painel de análises do Codex](https://admin.openai.com/analytics/codex), disponível mediante autenticação                                |
| Analytics API               | Relatórios agregados do Codex gerados programaticamente                      | A [referência da Analytics API do Codex](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics) |
| API de Compliance              | Registros de auditoria, segurança, questões jurídicas e investigações             | A [referência da API de Administração](https://chatgpt.com/public/admin/api-reference)                                              |

## Consulte as análises do workspace do ChatGPT

As análises do workspace do ChatGPT oferecem uma visão interativa da adoção e
do engajamento nos recursos compatíveis do workspace. A disponibilidade, as funções, as seções
do painel, a atualidade dos dados, o comportamento relacionado à privacidade e os formatos de exportação podem mudar. Consulte
[Análises do workspace para ChatGPT Enterprise e Edu](https://help.openai.com/en/articles/10875114)
para verificar a cobertura e os procedimentos atuais.

Trate os relatórios baixados como dados organizacionais identificáveis.
Aplique a política da organização para acesso, armazenamento e retenção, em vez de
presumir que uma exportação tenha as mesmas características de privacidade que um painel
com dados agregados.

## Consulte as análises do Codex

O [painel de análises do Codex](https://admin.openai.com/analytics/codex), disponível mediante autenticação,
tem foco nos relatórios do Codex. Use-o para exploração interativa, não como um contrato estável
de esquema. As categorias, os campos, os filtros e os formatos de exportação do painel podem
mudar independentemente desta página.

Para gerar relatórios automatizados, use a [Analytics API](/pt-BR/codex/enterprise/analytics-api)
e siga a respectiva documentação de referência. Para obter registros auditáveis, use a
[API de Compliance](/pt-BR/codex/enterprise/compliance-api).

## Interprete os dados dos relatórios

Tenha em mente estes limites:

- As análises do workspace do ChatGPT e as análises do Codex abrangem escopos de produto
diferentes.
- As análises agregadas e os registros de auditoria atendem a finalidades diferentes e têm
contratos distintos.
- As análises descrevem a atividade; não concedem acesso nem alteram as
permissões de execução.
- [Os limites de uso e os controles de gastos do ChatGPT](/pt-BR/codex/enterprise/usage-limits) constituem
  um limite separado do workspace, que depende do plano.

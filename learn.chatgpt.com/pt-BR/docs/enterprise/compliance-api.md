<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/compliance-api -->

Use a API de Compliance em fluxos de trabalho de segurança, jurídicos, de governança e de investigação
que exijam registros auditáveis. Use análises, e não registros de conformidade,
para medir a adoção e as tendências.

A [referência da API de administração](https://chatgpt.com/public/admin/api-reference)
é a fonte oficial dos requisitos atuais de acesso, da cobertura de eventos, das rotas,
dos esquemas, dos filtros, da retenção e do comportamento das requisições.

Para ter uma visão geral dos recursos de conformidade disponíveis e dos padrões comuns de
integração, consulte o [guia da Plataforma de conformidade](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

## Quando usar a API de Compliance

A API de Compliance é indicada quando você precisa:

- Exportar os registros cobertos pela API para um sistema de auditoria ou investigação.
- Aplicar os processos de retenção e preservação legal da organização.
- Correlacionar a atividade do Codex com outros dados de segurança ou de identidade.
- Apoiar investigações aprovadas de segurança, jurídicas ou de governança.

Essa API não é um painel de produtividade. Não a use para inferir a qualidade do código nem
o desempenho individual. Use as [Análises do workspace](/pt-BR/codex/enterprise/workspace-analytics)
ou a [Analytics API](/pt-BR/codex/enterprise/analytics-api) para gerar relatórios de adoção.

## Primeiros passos

1. Abra a [referência da API de administração](https://chatgpt.com/public/admin/api-reference) e
   confirme se sua função de administrador tem acesso aos recursos de conformidade
   de que você precisa.
2. Use o fluxo de logs de conformidade, que só permite adicionar registros, para a coleta contínua. Consulte a
referência da API para conferir os recursos e padrões de recuperação
com suporte atualmente.
3. [Baixe os arquivos de log](#download-logs) e teste a ingestão, fora de produção, em um
   sistema de gerenciamento de informações e eventos de segurança (SIEM) ou em um data lake.
4. Agende a coleta contínua e aplique aos registros exportados os controles de acesso,
retenção e preservação legal da sua organização. Não presuma que a janela de retenção
da fonte substitua a política de retenção da sua organização.

Por exemplo, uma equipe de segurança pode transmitir eventos imutáveis de conformidade ao seu
SIEM para investigações ou encaminhar esses eventos a um fluxo de trabalho aprovado de descoberta
eletrônica. Consulte a referência da API para conferir as rotas e
os esquemas atuais, em vez de copiar deste guia um contrato de endpoint.

### Baixar logs

Baixe o [script Bash](/downloads/compliance-api/download_compliance_files.sh)
ou o [script PowerShell](/downloads/compliance-api/download_compliance_files.ps1).
Ambos listam e baixam todos os arquivos de log disponíveis após um carimbo de data/hora especificado, seguem
a paginação e gravam JSONL na saída padrão. Os erros são enviados à saída de erro padrão.

Defina `COMPLIANCE_API_KEY` com sua chave da API de Compliance para empresas. Substitua
`<workspace_or_org_id>` pelo ID do seu workspace do ChatGPT ou pelo ID da organização na
Plataforma de API, e `<after>` por um carimbo de data/hora ISO 8601 que inclua o fuso
horário. Este exemplo recupera arquivos `AUTH_LOG`, 100 por vez.

No macOS ou Linux, instale Bash, `curl` e `jq` e execute:

```bash
bash ./download_compliance_files.sh "<workspace_or_org_id>" AUTH_LOG 100 "<after>" > output.jsonl

O script para Windows é compatível com PowerShell 5.1 ou posterior. Revise o arquivo baixado.
Se o Windows o bloquear e a política de execução da sua organização permitir, execute
`Unblock-File -Path .\download_compliance_files.ps1`. Este exemplo usa
PowerShell 7 para salvar em UTF-8 sem uma marca de ordem de bytes:

```powershell
.\download_compliance_files.ps1 "<workspace_or_org_id>" AUTH_LOG 100 "<after>" |
  Set-Content -Encoding utf8NoBOM output.jsonl

## Confirme os limites administrativos

A cobertura de conformidade corresponde ao workspace do ChatGPT e aos produtos representados
na referência atual da API. Os dados das organizações da Plataforma de API estão sujeitos
aos controles próprios de dados e administração da API.

A referência da API define as rotas atuais, a cobertura de eventos, os esquemas,
os filtros, o comportamento de retenção, os requisitos de permissão e o funcionamento das requisições.
Esta página não reproduz esse contrato.

## Documentação relacionada

- [Análises do workspace](/pt-BR/codex/enterprise/workspace-analytics)
- [Guia de implementação para administradores](/pt-BR/codex/enterprise/admin-setup)
- [Governança](/pt-BR/codex/enterprise/governance)
- [Analytics API](/pt-BR/codex/enterprise/analytics-api)

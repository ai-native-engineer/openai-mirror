<!-- source: https://learn.chatgpt.com/pt-BR/docs/security -->

O Codex Security é um agente de segurança de aplicativos que ajuda equipes de segurança e
engenharia a encontrar, confirmar e corrigir vulnerabilidades. Use-o no
Codex, no seu terminal, por meio do TypeScript SDK ou com repositórios do GitHub
conectados.

Para uma primeira verificação local guiada, comece pelo [Início rápido do
Plugin Codex Security](/pt-BR/codex/security/plugin).

## Use o Codex Security no aplicativo para desktop

No aplicativo do ChatGPT para desktop, abra o menu suspenso do ChatGPT e selecione **Codex**.
Instale e ative o Plugin Codex Security para abrir **Segurança** na
barra lateral. A área de trabalho de Segurança reúne suas verificações, seus achados e seus repositórios em
um só lugar enquanto o Codex executa cada verificação em uma tarefa.

- Use **Verificações** para iniciar verificações, acompanhar o progresso e revisar os resultados salvos.
- Use **Achados** para inspecionar issues e evidências nas verificações concluídas.
- Use **Repositórios** para revisar o histórico do repositório e os achados em aberto.

Consulte [Usar a área de trabalho de Segurança](/pt-BR/codex/security/plugin/workbench) para conhecer o
fluxo de trabalho completo no aplicativo para desktop.

### Explore os casos de uso do plug-in

- [Executar uma verificação de segurança](/pt-BR/codex/security/plugin/scans) em um repositório ou em uma única pasta com escopo delimitado.
- [Executar uma verificação de segurança aprofundada](/pt-BR/codex/security/plugin/deep-scans) quando você precisar de uma revisão mais abrangente e puder esperar mais pela conclusão.
- [Revisar alterações no código](/pt-BR/codex/security/plugin/code-changes) antes de mesclar uma pull request ou uma branch.
- [Faça a triagem de um backlog](/pt-BR/codex/security/plugin/triage-backlog) quando você já tiver achados de segurança para revisar.
- [Corrigir e verificar achados](/pt-BR/codex/security/plugin/fix-findings) com patches de escopo delimitado para achados aprovados.
- [Exportar ou acompanhar achados](/pt-BR/codex/security/plugin/export-findings) como artefatos portáteis ou em destinos de acompanhamento que exigem aprovação.
- [Criar relatórios de vulnerabilidades](/pt-BR/codex/security/plugin/vulnerability-reports) com base nos achados, nas notas de divulgação, no código-fonte e nas PoCs fornecidos.
- [Propor reforço de segurança](/pt-BR/codex/security/plugin/security-hardening) com base nos resultados das verificações ou em outras evidências de segurança.
- [Ver as novidades](/pt-BR/codex/security/plugin/changelog) do Plugin Codex Security.

  A área de trabalho de Segurança do aplicativo para desktop e a Codex CLI usam o Plugin Codex Security.
  O Codex Security na nuvem verifica repositórios do GitHub conectados por meio do Codex Cloud.
  Para saber mais sobre o ambiente isolado, as aprovações, os controles de rede e as configurações administrativas do Codex, consulte
[Aprovações do agente e segurança](/pt-BR/codex/agent-approvals-security).

## CLI e SDK do Codex Security

A CLI e o TypeScript SDK estão disponíveis no pacote público
[`@openai/codex-security`](https://github.com/openai/codex-security).
Execute a CLI com `npx`:

```bash
npx @openai/codex-security --help

A execução de verificações requer acesso ao Codex Security. Para obter os melhores resultados, use uma conta
verificada para o [Trusted Access for Cyber](https://chatgpt.com/cyber).

Use o mesmo mecanismo de verificação do plug-in em diferentes repositórios e ao longo do tempo. A CLI
descobre repositórios do GitHub, retoma verificações em massa, acompanha achados entre
verificações e registra feedback sobre falsos positivos. Adicione sua arquitetura e suas políticas de segurança,
defina um limite estimado de custo ou execute verificações em CI e antes dos commits.
Use o TypeScript SDK para incorporar verificações, relatórios de progresso e controles de custo
a um aplicativo ou ferramenta de desenvolvimento.

- [Comece pelo Início rápido da CLI](/pt-BR/codex/security/cli) para configurar a CLI,
  realizar a verificação preliminar de um repositório e executar uma verificação local.
- [Executar verificações de segurança em massa](/pt-BR/codex/security/cli/bulk-scans) para descobrir repositórios do GitHub
  ou executar uma campanha que pode ser retomada com base em um inventário CSV.
- [Executar verificações em CI](/pt-BR/codex/security/cli/ci) para revisar alterações em pull requests,
  preservar artefatos, fazer upload de SARIF e definir uma política de severidade.
- [Leia as perguntas frequentes sobre a CLI](/pt-BR/codex/security/cli/faq) para encontrar respostas sobre o histórico de verificações,
  feedback sobre falsos positivos, cobertura e verificação das correções.
- [Use a referência da CLI](/pt-BR/codex/security/cli/reference) para verificar quais
  comandos, flags, formatos de saída, artefatos e códigos de saída são aceitos.
- [Integre o TypeScript SDK](/pt-BR/codex/security/sdk) para selecionar alvos,
  inspecionar resultados, acompanhar o progresso e cancelar verificações programaticamente.

## Codex Security na nuvem

No momento, o Codex Security na nuvem está em prévia de pesquisa. Ele verifica repositórios do
GitHub conectados em busca de prováveis issues de segurança.

Ele ajuda as equipes a:

1. **Encontrar vulnerabilidades prováveis** usando um modelo de ameaças específico do repositório e o contexto real do código.
2. **Reduzir o ruído** validando os achados antes de revisá-los.
3. **Encaminhar os achados para correção** com resultados priorizados, evidências e opções de patch sugeridas.

## Como funciona o Codex Security na nuvem

O Codex Security verifica os repositórios conectados commit a commit.
Ele cria o contexto da verificação com base no seu repositório, avalia vulnerabilidades prováveis nesse contexto e valida issues de alta relevância em um ambiente isolado antes de apresentá-las.

O fluxo de trabalho se concentra em:

- contexto específico do repositório, em vez de assinaturas genéricas
- evidências de validação que ajudam a reduzir falsos positivos
- correções sugeridas que você pode revisar no GitHub

## Acesso e pré-requisitos do Codex Security na nuvem

O Codex Security na nuvem funciona com repositórios do GitHub conectados por meio do
Codex Cloud. Se um repositório não estiver visível, confirme se ele está disponível no seu
workspace do Codex Cloud ou entre em contato com a equipe da OpenAI responsável pela sua conta.

## Documentação relacionada

- O [Início rápido do Plugin Codex Security](/pt-BR/codex/security/plugin) mostra como instalar o plug-in e executar uma primeira verificação local.
- A [Área de trabalho de Segurança](/pt-BR/codex/security/plugin/workbench) explica as verificações salvas, os achados, os repositórios e a atividade de verificação no aplicativo para desktop.
- O [Início rápido da CLI do Codex Security](/pt-BR/codex/security/cli) mostra como configurar a CLI, fazer a verificação preliminar e executar uma primeira verificação no terminal.
- A página [Executar verificações de segurança em massa](/pt-BR/codex/security/cli/bulk-scans) explica a descoberta de repositórios no GitHub, os inventários CSV, os resultados de campanhas e o comportamento de retomada.
- As [Perguntas frequentes sobre a CLI do Codex Security](/pt-BR/codex/security/cli/faq) respondem a dúvidas comuns sobre verificações, achados, cobertura e custos.
- O [TypeScript SDK do Codex Security](/pt-BR/codex/security/sdk) explica como executar verificações por meio de um aplicativo ou de uma ferramenta de desenvolvimento.
- A [Configuração do Codex Security na nuvem](/pt-BR/codex/security/setup) detalha a configuração, a execução de verificações e a revisão dos achados.
- A [Revisão de segurança](/pt-BR/codex/security/security-review) explica como realizar revisões de segurança aprofundadas em pull requests do GitHub.
- A página [Aprimorar o modelo de ameaças](/pt-BR/codex/security/threat-model) explica como ajustar o escopo, os pontos de entrada e as premissas de criticidade.
- As [Perguntas frequentes sobre o Codex Security na nuvem](/pt-BR/codex/security/faq) abordam dúvidas comuns sobre o produto na nuvem.

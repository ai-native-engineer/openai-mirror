<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/plugin -->

O Codex Security verifica seu código em busca de vulnerabilidades e valida achados
plausíveis. Para cada problema que pode ser relatado, fornece as evidências e as orientações de
correção necessárias para você revisar o resultado. Verifique somente código de sua propriedade ou que você tenha
permissão para avaliar.

Siga este guia de início rápido para instalar o plug-in e executar uma verificação padrão, somente leitura,
de um repositório local no Codex.

  Esta página aborda o Plugin Codex Security no aplicativo para desktop ou no Codex CLI. Para
  verificar um repositório conectado do GitHub no Codex Cloud, consulte a [configuração do Codex Security
  na nuvem](/pt-BR/codex/security/setup).

## Instalar o plug-in

1. Abra o [Codex no aplicativo do ChatGPT para desktop](/pt-BR/codex/app).
2. Abra **Plug-ins**, pesquise **Codex Security** ou use o botão abaixo:

   <div className="not-prose my-6">
     
       Instalar o Plugin Codex Security
     
   </div>

3. Confirme se o plug-in está ativado e abra **Segurança** na barra lateral.

1. No terminal, acesse o repositório que deseja avaliar e inicie o Codex:

   ```bash
   codex

2. Digite `/plugins`, pesquise **Codex Security** e selecione **Instalar
   plug-in**.
3. Digite `/new` para iniciar uma nova conversa para o repositório.

Para instalar o Codex Security em um repositório local, use o aplicativo do ChatGPT para desktop
ou o Codex CLI.

  Consulte o [registro de alterações do plug-in](/pt-BR/codex/security/plugin/changelog) antes de contar
  com um recurso ou iniciar uma verificação de longa duração. Se **Segurança** não aparecer
  na barra lateral do aplicativo para desktop, atualize o aplicativo e o plug-in e confirme se o plug-in
  está ativado.

## Executar sua primeira verificação

Para obter a melhor qualidade na verificação, use <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
com esforço de raciocínio `xhigh`.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Escolha um repositório e configure uma nova verificação de segurança antes de iniciá-la.
  </figcaption>
</figure>

1. Abrir a configuração da verificação

   Selecione **Segurança** na barra lateral, abra **Verificações** e selecione **+ Verificação**.

2. Escolher a base de código e a área da verificação

   Selecione um repositório existente ou use outra pasta. Escolha **Base de código**,
   deixe **Verificação aprofundada** desativada e selecione todo o repositório ou uma pasta.
   Confirme se a branch e a revisão correspondem ao código que você pretende verificar.

3. Adicionar contexto relevante

   Escolha o modelo e o esforço de raciocínio. Abra **Contexto adicional** somente quando
   precisar descrever um vetor de ataque específico, uma área sensível em termos de segurança
   ou um detalhe do repositório que deva orientar a revisão.

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       Ative o contexto adicional para descrever vetores de ataque, áreas de foco e
orientações de segurança relevantes.
     </figcaption>
   </figure>

4. Iniciar a verificação

   Selecione **Iniciar verificação** e acompanhe as etapas da verificação na área de trabalho de Segurança.
   Selecione **Ver atividade** para inspecionar a tarefa do Codex que executa a verificação.

5. Revisar o resultado

   Abra a verificação concluída para inspecionar os achados, a cobertura e os artefatos de relatório
   disponíveis. Use **Achados** para revisar problemas em diferentes verificações ou **Repositórios**
   para inspecionar o histórico de verificações de um repositório.

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       Revise os resultados, os achados e a cobertura da verificação na área de trabalho de Segurança.
     </figcaption>
   </figure>

1. Solicitar uma verificação padrão

   Envie este prompt na nova conversa:

   ```text
   Run a Codex Security scan on this repository.

2. Aguardar a conclusão da verificação

   O Codex executa a verificação no terminal sem abrir um workspace de configuração. Mantenha
a tarefa em execução até que o Codex informe que ela foi concluída. Se o Codex identificar
uma limitação de configuração, revise essa limitação e a alteração exata
proposta antes de aprovar uma atualização da configuração.

3. Revisar o resultado

   Revise o resumo no terminal e abra o arquivo `report.md` gerado para
   ver o resultado completo.

Execute este fluxo de trabalho local do plug-in no aplicativo do ChatGPT para desktop ou no Codex CLI.

## O que a verificação cria

As verificações concluídas permanecem disponíveis em **Verificações**. Revise os achados e a
cobertura na área de trabalho de Segurança ou inspecione os achados relacionados e o histórico do repositório
em **Achados** e **Repositórios**. A verificação também cria os arquivos
abaixo.

Cada verificação concluída apresenta um resumo no terminal e cria os arquivos
abaixo.

Execute este fluxo de trabalho local do plug-in no aplicativo do ChatGPT para desktop ou no Codex CLI.

- `report.md`, o principal arquivo legível para consultar os resultados da verificação.
- `findings/<slug>/`, quando houver relatórios detalhados de vulnerabilidades e arquivos complementares de
  prova de conceito.
- `hardening/`, quando houver orientações de reforço estrutural da segurança e propostas ou
  diagramas complementares.
- Dados estruturados da verificação em `scan-manifest.json`, `findings.json` e
`coverage.json` para automação e integrações. Você pode revisar os resultados da verificação
  sem abrir esses arquivos.

Mantenha o diretório completo da verificação intacto ao compartilhar ou arquivar os resultados, para que os
links em `report.md` continuem funcionando.

## Escolher seu próximo fluxo de trabalho

- [Usar a área de trabalho de Segurança](/pt-BR/codex/security/plugin/workbench) para gerenciar
  verificações salvas, achados, repositórios e atividades de verificação no aplicativo para desktop.
- [Executar uma verificação pela CLI](/pt-BR/codex/security/cli) se você tiver acesso beta e
  precisar de um fluxo de trabalho reproduzível no terminal com resultados estruturados.
- [Executar uma verificação padrão ou com escopo delimitado](/pt-BR/codex/security/plugin/scans) para revisar um
  repositório ou uma pasta com o fluxo de trabalho padrão.
- [Avaliar uma primeira verificação](/pt-BR/codex/security/plugin/scans#assess-a-first-scan)
  para comparar os resultados com problemas conhecidos e decidir quando fazer uma nova verificação.
- [Executar uma verificação aprofundada](/pt-BR/codex/security/plugin/deep-scans) para realizar uma verificação mais completa
  quando puder aguardar um tempo de execução maior.
- [Revisar alterações no código](/pt-BR/codex/security/plugin/code-changes) para avaliar um pull
  request, um commit, um intervalo de branches ou um patch da árvore de trabalho.
- [Faça a triagem de um backlog](/pt-BR/codex/security/plugin/triage-backlog) para revisar achados de
  segurança existentes.
- [Corrigir e verificar um achado](/pt-BR/codex/security/plugin/fix-findings) depois de
  aceitar um achado para correção.
- [Exportar ou acompanhar achados](/pt-BR/codex/security/plugin/export-findings) para criar
  JSON, CSV, SARIF, uma issue no Linear, no GitHub ou no Jira mediante aprovação, ou um
  rascunho privado de GitHub Security Advisory.
- [Criar relatórios de vulnerabilidades](/pt-BR/codex/security/plugin/vulnerability-reports)
  para transformar achados, notas de divulgação, código-fonte e PoCs fornecidos em
  relatórios completos e independentes.
- [Propor reforço de segurança](/pt-BR/codex/security/plugin/security-hardening) para
  considerar opções estruturais ou arquitetônicas com base nos resultados da verificação ou em outras
  evidências de segurança.

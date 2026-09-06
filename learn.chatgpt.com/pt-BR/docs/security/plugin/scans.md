<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/plugin/scans -->

Comece com uma verificação padrão do Codex Security para uma revisão inicial ou uma avaliação de rotina de um
repositório ou componente. Ela executa uma vez o fluxo de trabalho completo da verificação.

Para uma avaliação mais completa, revise os resultados e execute uma [verificação
aprofundada](/pt-BR/codex/security/plugin/deep-scans). As verificações aprofundadas demoram mais e fazem buscas
mais abrangentes.

## Escolher a área da verificação

No aplicativo para desktop, abra **Segurança**, selecione **Verificações** e depois **+ Verificação**.
Escolha um repositório existente ou outra pasta e selecione **Base de código**.

Verifique todo o repositório quando precisar de ampla cobertura e ele for uma
unidade adequada para revisão. Em um monorepo, escolha uma pasta quando um serviço,
pacote ou componente tiver um responsável bem definido e um limite de segurança claro.

Você também pode iniciar uma verificação em uma conversa do Codex:

```text
Use $codex-security:security-scan to scan this repository for security vulnerabilities.

Para concentrar essa conversa em uma pasta específica, identifique o componente:

```text
Use $codex-security:security-scan to scan this repository for security vulnerabilities, focusing on the services/billing component.

  Em um monorepo grande, comece por um limite relevante de produto ou serviço.

## Configurar a verificação

Para obter a melhor qualidade na verificação, use <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
com o nível de esforço de raciocínio `xhigh`.

1. Selecione **Base de código** e deixe **Verificação aprofundada** desativada.
2. Confirme o repositório selecionado, a branch atual e a revisão mais recente.
3. Defina **Área da verificação** como o repositório inteiro ou escolha uma pasta.
4. Escolha um modelo e um nível de esforço de raciocínio.
5. Abra **Contexto adicional** somente quando isso alterar a revisão. Um contexto útil
   identifica entradas controladas por invasores, limites de confiança, ações sensíveis ou uma
   área específica a ser priorizada.
6. Selecione **Iniciar verificação**.

Adicione `SECURITY.md` à raiz do repositório para registrar orientações de segurança persistentes.
Descreva o modelo de ameaças, os invariantes de segurança, os critérios para relatar achados,
as exclusões e o contexto de gravidade. Adicione arquivos `SECURITY.md` aninhados para fornecer
orientações específicas de cada diretório. Quando houver conflito entre políticas, prevalece o arquivo mais próximo do
código. O Codex Security trata esses arquivos como contexto de políticas,
não como instruções executáveis.

Use `AGENTS.md` para indicar os comandos de build e validação compatíveis, além de outras
instruções específicas do repositório.

## Aguardar a conclusão das fases

Uma verificação executa estas fases na seguinte ordem:

1. A **modelagem de ameaças** identifica ativos, pontos de entrada, limites de confiança e
   invariantes de segurança.
2. A **identificação de achados** analisa o código solicitado em busca de possíveis falhas nos
   controles e de caminhos da origem ao destino.
3. A **validação** testa ou verifica de outra forma cada possível achado e registra evidências
   ou lacunas de comprovação.
4. A **análise de impacto e caminhos** avalia os caminhos realistas de cada possível achado,
   seu impacto e sua gravidade.
5. A **geração de relatórios** registra os achados validados, a cobertura e os metadados da verificação.
   Relatórios detalhados de cada achado estão disponíveis quando solicitados.
6. O **fortalecimento estrutural**, quando solicitado, analisa o conjunto de achados e
   cria orientações de design.
7. A **finalização** valida o contrato estruturado da verificação e gera
`report.md`, incluindo links para relatórios detalhados ou orientações de fortalecimento.

A área de trabalho mostra a fase ativa da verificação e o progresso informado pelo plug-in.
Selecione **Ver atividade** para inspecionar a tarefa do Codex. Aguarde o resultado
completo, em vez de avaliar candidatos preliminares ou interromper a verificação porque uma fase demora
mais que outra.

## Revisar a verificação concluída

Revise o resultado nesta ordem:

1. Confirme o alvo, a revisão e a área da verificação.
2. Leia as superfícies revisadas e todas as áreas explicitamente adiadas ou indicadas para acompanhamento.
3. Para cada achado, inspecione o controle raiz ou o ponto de destino, a entrada controlada pelo invasor,
o método de validação, a incerteza restante, o alcance realista,
a justificativa da gravidade e a remediação proposta.
4. Descarte os achados cujas evidências não sustentam o caminho ou o impacto alegado.
5. Selecione um achado aceito antes de iniciar uma correção.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Revise a gravidade, o status da validação, a causa raiz e o caminho de
ataque do achado.
  </figcaption>
</figure>

## Avaliar a primeira verificação

Antes da verificação, escolha de dois a quatro critérios de avaliação, como descoberta
independente, qualidade das evidências, falsos positivos ou qualidade da remediação. Se você
fizer o teste com um achado conhecido, registre se informou esse achado ao Codex ou
se o omitiu da verificação.

Registre a revisão do repositório, a versão do plug-in, o modelo e o nível de esforço de raciocínio.
Use essa linha de base para comparar verificações posteriores após mudanças no código, nos controles de segurança ou
nas configurações da verificação.

## Escolher a cadência das verificações

Defina a cadência das verificações com base no risco do repositório e na capacidade da sua equipe
de tratar os achados. Faça verificações nestes momentos:

- **Linha de base:** Execute uma verificação padrão ao integrar um repositório, assumir
  a responsabilidade por um componente ou precisar de um ponto de partida para um novo modelo de ameaças.
- **Alterações no código:** [Revise as
  alterações no código](/pt-BR/codex/security/plugin/code-changes) quando um pull request ou um commit
  alterar código sensível à segurança ou uma integração externa.
- **Revisão periódica:** Defina um intervalo recorrente de revisão com base na exposição do sistema
  e na frequência das alterações no código. Ajuste esse intervalo à capacidade da sua equipe de
  tratar os achados.
- **Após uma correção:** [Corrija e verifique o
  achado](/pt-BR/codex/security/plugin/fix-findings). Confirme que a issue não
  se reproduz mais e mantenha a verificação original para comparação.

Esses gatilhos de verificação não criam um agendamento automatizado.

## Reabrir uma verificação anterior

Abra **Segurança** e selecione uma verificação salva em **Verificações** para revisar os
achados, a cobertura e os artefatos de relatório disponíveis. Para avaliar o código mais recente,
inicie outra verificação no mesmo repositório. A nova verificação não substitui a
anterior nem os respectivos artefatos.

## Usar os resultados

Use a área de trabalho de Segurança para revisar os achados, a cobertura e as áreas de acompanhamento
sem inspecionar o JSON bruto. Quando disponível, abra `report.md` como ponto de entrada
legível para o diretório completo da verificação. Mantenha o diretório inteiro junto ao
compartilhá-lo ou arquivá-lo: o relatório contém links para relatórios detalhados em `findings/`
e para orientações de fortalecimento estrutural em `hardening/` quando esses artefatos opcionais
estiverem disponíveis.

Nos bastidores do workspace, cada verificação mantém `scan-manifest.json`, `findings.json`,
e `coverage.json` para automação e integrações. Normalmente, você não precisa
abrir esses arquivos.

Para obter artefatos portáteis ou rastrear issues externamente, consulte [Exportar ou acompanhar
achados](/pt-BR/codex/security/plugin/export-findings).

## Próxima etapa

Depois de aceitar um achado, use [Corrigir e verificar um
achado](/pt-BR/codex/security/plugin/fix-findings) para gerar e revisar um único
patch de escopo delimitado. Não peça ao Codex que corrija todos os achados de uma verificação em um único chat.

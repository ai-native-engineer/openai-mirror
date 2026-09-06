<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/plugin/security-hardening -->

Use `$codex-security:propose-security-hardening` para transformar um conjunto de
evidências de segurança em opções de reforço estrutural ou arquitetônico. O
fluxo de trabalho pode analisar uma varredura concluída do Codex Security ou partir de
achados fornecidos, relatórios de divulgação de vulnerabilidades, análises de incidentes, documentos de avaliação e
código-fonte.

O resultado é um portfólio de design, não um patch, e não comprova a correção de uma
vulnerabilidade. O Codex só altera o repositório depois que você seleciona uma opção e
solicita explicitamente essa alteração.

## Preparar as evidências

Forneça ao fluxo de trabalho:

- Um diretório de varredura ou um conjunto explicitamente definido de achados e relatórios.
- A árvore de código-fonte de destino e, quando disponíveis, a revisão ou o snapshot relevante.
- PoCs, rastros, evidências de incidentes ou materiais de avaliação que respaldem os
achados.
- Restrições de desempenho, memória, compatibilidade, confiabilidade, operações,
prazo de entrega ou escopo da alteração.

O fluxo de trabalho usa as evidências para identificar violações recorrentes de invariantes, controles
dispersos, pontos críticos de acesso privilegiado, limites de isolamento frágeis e padrões recorrentes
de remediação. Ele também pode concluir que correções pontuais são mais
proporcionais do que uma mudança arquitetônica.

## Executar o fluxo de trabalho

Envie um prompt como este:

```text
Use $codex-security:propose-security-hardening to analyze [scan directory or finding paths] against [source tree and revision]. Develop evidence-backed structural hardening options with engineering tradeoffs, before-and-after diagrams, a migration plan, and an implementation handoff. Do not modify the repository.

## Revisar o portfólio

Um portfólio útil deve:

- Relacionar cada mudança proposta a achados concretos, ao código-fonte e às evidências do modelo de
ameaças.
- Descrever o design atual e os invariantes de segurança que o novo design deve
preservar.
- Comparar opções distintas quanto a risco residual, desempenho,
confiabilidade, operações, compatibilidade e custo de migração.
- Recomendar uma opção somente quando as evidências a sustentarem, explicitando as
premissas e questões em aberto.
- Incluir orientações sobre implantação, validação, reversão e implementação.
- Distinguir fatos observados, inferências e propriedades propostas para o design.

Revise as evidências e pondere as vantagens e desvantagens antes de escolher uma opção. Um diagrama de
arquitetura ou uma recomendação de design não substitui a validação dos achados
originais nem da correção implementada.

## Usar orientações de reforço de uma varredura

Você pode solicitar um portfólio de reforço para uma varredura padrão, aprofundada ou de alterações com
achados que podem ser relatados. O Codex grava o portfólio em `hardening/hardening.md`,
a análise estruturada em `hardening/hardening.json` e as propostas
ou os diagramas de apoio em `hardening/`. A varredura inclui um link para o portfólio em `report.md`.

Mantenha intacto o diretório completo da varredura para que esses links continuem funcionando. Para revisar
os relatórios individuais que embasam o portfólio, consulte [Escrever relatórios de
vulnerabilidades](/pt-BR/codex/security/plugin/vulnerability-reports).

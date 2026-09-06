<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/deep-security-scan -->

## Escolher uma análise aprofundada do repositório

Use uma varredura aprofundada quando precisar de uma análise mais abrangente de vulnerabilidades em
um repositório ou uma pasta especificada e puder reservar tempo para uma execução mais longa. O
Plugin Codex Security repete as passagens de descoberta antes de validar e priorizar os
achados; por isso, esse fluxo de trabalho consome mais tempo e recursos do que uma varredura comum.

Uma varredura aprofundada pode analisar um repositório inteiro ou um pacote ou
diretório indicado explicitamente. Para analisar um pull request, commit, diff de branch ou patch da árvore de trabalho,
use
[$codex-security:security-diff-scan](/pt-BR/codex/use-cases/scan-code-changes-for-security).

## Preparar uma varredura autorizada

1. Abra o repositório no Codex e conclua o [início rápido do Plugin Codex Security](/pt-BR/codex/security/plugin).
2. Confirme que você é proprietário do repositório ou tem autorização para avaliá-lo.
3. Inclua orientações sobre arquitetura, limites de confiança, invariantes de segurança, critérios de identificação de achados,
   exclusões e gravidade em `SECURITY.md`. Use arquivos `SECURITY.md`
   aninhados para definir políticas específicas de cada diretório.
4. Mantenha os comandos compatíveis de build, teste e validação, além de outras
   instruções do repositório, em `AGENTS.md`.
5. Execute o prompt inicial e deixe a varredura concluir as etapas de descoberta repetida,
validação, análise de caminhos de ataque e geração do relatório final.
6. Revise o workspace dos achados, o relatório e eventuais lacunas de comprovação. Solicite
relatórios detalhados de vulnerabilidades ou orientações para fortalecimento estrutural quando precisar.

## Revisar as evidências antes da correção

O resultado final deve indicar os locais afetados, explicar por que o comportamento é
alcançável, descrever a validação realizada pelo Codex, registrar eventuais lacunas de comprovação e apresentar uma
orientação de correção com escopo delimitado. Diferencie os achados sem evidências de validação
dos achados validados.

Inicie a correção apenas de um achado que você tenha selecionado e revisado. Use
[Corrigir um backlog de vulnerabilidades](/pt-BR/codex/use-cases/remediate-vulnerability-backlog)
para corrigir os achados um por vez com validação de regressão direcionada.

Para informações sobre configuração, verificações preliminares, alvos com escopo delimitado e expectativas quanto ao tempo de execução, consulte [Executar uma varredura aprofundada de
segurança](/pt-BR/codex/security/plugin/deep-scans).

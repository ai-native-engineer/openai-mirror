<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/threat-model -->

Saiba o que é um modelo de ameaças e como editá-lo melhora as sugestões do Codex Security.

## O que é um modelo de ameaças

Um modelo de ameaças é um breve resumo de segurança que descreve o funcionamento do seu repositório. No Codex Security, você o edita como `project overview`, e o sistema o usa como contexto para futuras varreduras, priorização e revisão.

O Codex Security cria o primeiro rascunho a partir do código. Se as descobertas parecerem fora do esperado, essa é a primeira coisa a editar.

Um modelo de ameaças útil destaca:

- pontos de entrada e dados de entrada não confiáveis
- limites de confiança e premissas de autenticação
- fluxos de dados confidenciais ou ações privilegiadas
- as áreas que sua equipe quer revisar primeiro

Por exemplo:

> API pública para alterações em contas. Aceita solicitações JSON e uploads de arquivos. Usa um serviço interno de autenticação para verificar identidades e grava alterações de cobrança por meio de um serviço interno. Concentre a revisão nas verificações de autenticação, na análise dos uploads e nos limites de confiança entre serviços.

Isso oferece ao Codex Security um ponto de partida melhor para futuras varreduras e para a priorização das descobertas.

## Como aprimorar e reavaliar o modelo de ameaças

Se quiser melhorar os resultados, edite primeiro o modelo de ameaças. Use-o quando não houver descobertas nas áreas que importam para você ou quando elas aparecerem em lugares inesperados. O modelo de ameaças altera o contexto das futuras varreduras.

  Alguns usuários copiam o modelo de ameaças atual para o Codex, usam um chat para aprimorá-lo
com base nas áreas que querem que sejam revisadas com mais atenção e depois colam a versão atualizada
de volta na interface da Web.

### Onde editar

Para revisar ou atualizar o modelo de ameaças, acesse [Varreduras do Codex Security](https://chatgpt.com/codex/security/scans), abra o repositório e clique em **Editar**.

## Documentação relacionada

- A página [Configuração do Codex Security na nuvem](/pt-BR/codex/security/setup) aborda a configuração do repositório e a revisão das descobertas.
- A página [Codex Security](/pt-BR/codex/security) apresenta uma visão geral do produto.
- A página [Perguntas frequentes sobre o Codex Security na nuvem](/pt-BR/codex/security/faq) aborda dúvidas comuns sobre a nuvem.

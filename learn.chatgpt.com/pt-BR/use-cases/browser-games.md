<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/browser-games -->

## Introdução

Criar um jogo é um dos exemplos mais claros de como o Codex ajuda em muito mais do que a geração de código. Um jogo de verdade geralmente exige um conceito documentado, uma camada de renderização, o desenvolvimento da estrutura do frontend, estado no backend, produção de recursos visuais e ajustes visuais constantes

Este caso de uso funciona melhor quando o Codex começa documentando exatamente o que o jogo deve fazer e depois faz iterações usando o Playwright interactive para testá-lo em um navegador em execução.

## Comece pelo plano do jogo

Antes de o Codex gerar qualquer estrutura inicial, peça que ele crie um arquivo `PLAN.md` que defina o jogo em termos concretos:

- o objetivo do jogador
- o loop principal
- as entradas e os controles
- os estados de vitória e derrota
- a progressão ou a dificuldade
- a direção visual
- as premissas sobre a stack e a hospedagem
- a ordem dos marcos

Esse plano é importante porque a instrução “criar um jogo” é vaga demais por si só. O Codex precisa saber como implementar cada parte do jogo e consultar com frequência os detalhes da implementação durante o desenvolvimento.

Você pode ativar o Modo planejamento com o comando de barra `/plan`.
Depois, salve a saída em um arquivo `PLAN.md`.

## Oriente o comportamento do Codex com AGENTS.md

Para garantir que o Codex siga o plano, verifique o próprio trabalho e use as ferramentas certas, crie um arquivo `AGENTS.md` como este:

```text
# Game name

Tech Stack:

- NextJS for frontend (hosted on Vercel)
- <insert technology> for rendering
- Fastify for backend, websockets (hosted on <hosting platform>)
- Postgres for database (hosted on <hosting platform>)
- Redis for caching and pub/sub (hosted on <hosting platform>)
- OpenAI for generative AI features

Tips:

- Use build and test commands to verify your work as soon as you complete a feature or task
- Use the PLAN.md file to guide your work when building new features
- Log your work under .logs (create new log files as you see fit) to record your thought process and decisions, and reference them when iterating on features
- Use playwright to test the visual output of your work, and iterate if it doesn't look right or fit the vibe
- Use imagegen to generate visual assets for your work, and every time you generate a collection of assets, save the prompts you used to be able to continue generating more of the same assets later (create files in .prompts)
- Use Context7 MCP to fetch <rendering framework> docs

Isso permite que o Codex trabalhe de forma independente por bastante tempo e use as habilidades relevantes conforme necessário.

## Aproveite as habilidades

Adicione as habilidades mencionadas no arquivo AGENTS.md:

- Imagegen, para que o Codex possa gerar recursos visuais para o jogo conforme necessário
- Playwright interactive, para que o Codex possa testar o jogo em um navegador em execução
- OpenAI docs, para que o Codex possa buscar a documentação mais recente da OpenAI API
- Opcionalmente, você pode adicionar o servidor MCP Context7 para buscar a documentação mais recente do framework de renderização

Para saber mais sobre como adicionar habilidades, consulte a [documentação de habilidades](/pt-BR/codex/build-skills).

  **Dica**: peça ao Codex para salvar os prompts de geração de imagens em um arquivo para que
  todos os recursos visuais sejam consistentes entre si. Dê orientações sobre o estilo dos recursos que você
  quer gerar e deixe o Codex elaborar prompts detalhados e reutilizáveis.

## Deixe o Codex trabalhar e iterar

O Codex vai gerar uma primeira versão do jogo com base no plano inicial.

Se houver muitos recursos visuais para gerar, essa primeira versão pode demorar um pouco para ficar pronta, às vezes várias horas. Como o Codex pode testar o próprio trabalho e experimentar o jogo em um navegador em execução, ele pode continuar trabalhando por bastante tempo sem precisar de nenhuma intervenção.

Quanto mais bem definido estiver o plano, melhor será o resultado final ao fim da primeira iteração.

Conforme você testa o jogo, faça as iterações necessárias, fornecendo capturas de tela e pedindo mudanças na jogabilidade ou atualizações nos recursos visuais, até ficar satisfeito com o resultado.

<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/idea-to-proof-of-concept -->

## Comece definindo uma direção visual

O GPT Image 2 é excelente para gerar mockups de UI de alta qualidade. Ao explorar novas ideias, você pode usar a geração de imagens para definir uma direção visual em vez de começar do zero.

Há duas maneiras de fazer isso:

- Refine a direção visual com a habilidade ImageGen e, quando estiver satisfeito com a UI proposta, peça ao Codex que crie um protótipo fiel a esse visual. Nesse caso, selecione o Codex, inicie uma nova conversa e anexe a imagem final que deseja implementar, em vez de continuar diretamente no chat do ChatGPT. O Codex funciona melhor quando pode usar como referência um anexo enviado pelo usuário.
- Use um plug-in e simplesmente descreva sua ideia: ele gerará a direção visual e cuidará das próximas etapas.

## Use um plug-in

Se você não precisar refinar a direção visual antes de iniciar a implementação, poderá usar um plug-in e descrever sua ideia.

Use o [plug-in Build Web Apps](https://github.com/openai/plugins/tree/main/plugins/build-web-apps)
para aplicativos web, dashboards, sites criativos e ferramentas que dependem muito do front-end. Seu
fluxo de trabalho orienta o Codex a primeiro gerar um design, reproduzi-lo em código e usar o
navegador para comparar o resultado com o conceito original.

Use o [plug-in Game Studio](https://github.com/openai/plugins/tree/main/plugins/game-studio)
quando a prova de conceito for um jogo para navegador. Essa abordagem deve definir os verbos
do jogador, o primeiro loop jogável, a engine, o fluxo de trabalho de assets, o HUD, os controles e o teste no
navegador antes de expandir o jogo.

## Fluxo de iteração

Uma boa prova de conceito se limita a um MVP que possa ser implementado rapidamente e validado com a equipe.
Se quiser garantir que o MVP funcione conforme o esperado, você pode usar o Playwright interactive para que o Codex verifique o próprio trabalho.

Quando a primeira versão estiver funcionando, você poderá aprimorá-la solicitando alterações com escopo delimitado no mesmo chat:

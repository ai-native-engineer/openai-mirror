<!-- source: https://learn.chatgpt.com/pt-BR/docs/image-inputs -->

Adicione imagens a um prompt quando a tarefa depender de contexto visual, como uma captura de tela de erro,
um design de interface, um diagrama de arquitetura ou um recurso existente. Explique
o que o ChatGPT deve analisar e qual resultado você deseja; não dependa apenas da imagem
para comunicar a tarefa.

Arraste uma imagem para o editor de prompts mantendo a tecla <kbd>Shift</kbd> pressionada para incluí-la
como contexto. Você também pode pedir ao ChatGPT que analise uma imagem em seu sistema ou usar
uma ferramenta de captura de tela para verificar o trabalho em outro aplicativo.

Anexe, cole ou arraste uma imagem para o editor do ChatGPT na Web. No prompt,
diga ao ChatGPT o que analisar e qual resultado você espera obter da imagem.

Cole uma imagem no editor interativo ou forneça um ou mais arquivos na
linha de comando:

```bash
codex -i screenshot.png "Explain this error and suggest the smallest fix"
codex --image before.png,after.png "Compare these states and list the regressions"

Para várias imagens, separe os caminhos com vírgulas ou repita `--image`. O Codex
aceita formatos de imagem comuns, incluindo PNG e JPEG.

Arraste uma imagem para o editor de prompts mantendo a tecla <kbd>Shift</kbd> pressionada, para que a
extensão aceite a imagem em vez de encaminhá-la ao editor.

## Escreva o prompt com base na imagem

Descreva o que a imagem mostra, indique a área relevante e especifique a saída
e as restrições. Se anexar mais de uma imagem, identifique cada uma e explique
como o ChatGPT deve compará-las.

Por exemplo:

```text
Compare this checkout screen with the design. Fix spacing and typography only;
do not change behavior. Verify the result with a new screenshot.

## Use o recurso de imagem adequado

Use uma entrada de imagem quando quiser que o ChatGPT analise uma referência visual. Use
[geração de imagens](/pt-BR/codex/image-generation) quando quiser que o ChatGPT
crie ou edite uma imagem.

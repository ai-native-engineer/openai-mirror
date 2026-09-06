<!-- source: https://learn.chatgpt.com/pt-BR/docs/image-generation -->

Peça ao ChatGPT para gerar ou editar imagens. Use a geração de imagens para recursos de UI,
banners, planos de fundo, ilustrações, folhas de sprites e espaços reservados que você queira
criar junto com o código ou em um Chat do ChatGPT.

Peça uma imagem no editor do aplicativo. Adicione uma imagem de referência quando quiser
que o ChatGPT transforme um recurso existente ou o use como orientação visual.

### Revise e edite as imagens geradas

Selecione uma imagem gerada para abrir o visualizador ampliado. Alterne entre a
**Visualização focada** para examinar uma imagem e a **Visualização em Canvas** para ver as imagens
geradas no mesmo Chat.

Na **Visualização em Canvas**, use **Comentar** para dar feedback preciso sobre uma ou mais
imagens. Selecione **Seleção múltipla** para escolher as imagens que deseja incluir e depois
envie seus comentários e outras instruções de edição no mesmo Chat.
Descreva o que deve mudar e o que deve permanecer igual.

Peça uma imagem em um Chat do ChatGPT na Web. Anexe uma imagem de referência ao
editor quando quiser que o ChatGPT a edite ou use como orientação visual.

Descreva a imagem em uma sessão interativa ou inclua `$imagegen` para invocar
explicitamente a habilidade de geração de imagens. Anexe uma imagem existente com `-i` ou
`--image` quando ela deva orientar o resultado.

Peça uma imagem no Chat da extensão. Arraste uma imagem de referência para
o editor com a tecla <kbd>Shift</kbd> pressionada quando quiser que o Codex edite ou use como base
um recurso existente.

## Gere ou edite uma imagem

Descreva a imagem em linguagem natural. Adicione uma imagem de referência quando quiser
que o ChatGPT transforme ou expanda um recurso existente.

Inclua `$imagegen` no prompt para invocar a habilidade de geração de imagens
de forma explícita.

A geração integrada de imagens usa `gpt-image-2` e é contabilizada nos seus limites gerais
de uso do Codex. Em média, as gerações de imagens consomem a cota incluída em um ritmo de 3 a 5 vezes maior
do que interações semelhantes sem geração de imagens, conforme a qualidade
e o tamanho da imagem. Para lotes maiores, defina `OPENAI_API_KEY` no seu ambiente e peça
ao ChatGPT para gerar imagens pela API; nesse caso, os preços da API serão aplicados.

A disponibilidade da geração de imagens e os limites de uso no ChatGPT na Web dependem do seu plano e das
configurações do workspace. Para gerar imagens de forma programática, use a [API de geração
de imagens](/api/docs/guides/image-generation).

## Crie prompts eficazes para imagens

Um bom prompt para imagens costuma ter apenas de uma a três frases claras. Descreva os
detalhes que determinam o sucesso do resultado:

- Explique a finalidade ou o público-alvo da imagem.
- Identifique o elemento principal e o que está acontecendo.
- Descreva o cenário, a composição e o estilo visual.
- Inclua enquadramento, dimensões, iluminação, cores ou materiais quando forem relevantes.
- Especifique as restrições, inclusive tudo o que a imagem não deve conter.

Use uma linguagem visual concreta em vez de avaliações genéricas. Por exemplo, descreva
de onde vem a luz em vez de pedir uma “iluminação bonita”. Repita qualquer
requisito que deva permanecer inalterado.

## Refine o resultado

Comece pela ideia central e depois faça revisões pequenas e direcionadas. Ajuste um
elemento por vez para preservar a composição e os outros detalhes importantes.
Você também pode selecionar uma área específica da imagem e descrever a alteração nessa
área.

Ao editar uma imagem existente, diga exatamente o que deve mudar e o que deve
permanecer igual.

Para revisões mais amplas, mantenha o feedback direto e prático: deixe a imagem
mais clara, reduza a saturação das cores, simplifique o plano de fundo ou mantenha a
composição enquanto altera o estilo.

## Use várias imagens de referência

Use um pequeno conjunto de imagens de referência quando uma imagem definir o conteúdo e
outra definir o estilo, o layout ou outra direção visual. Identifique cada
imagem pela ordem em que aparece e explique como elas se relacionam. Ao combinar elementos, use
termos espaciais como primeiro plano, plano de fundo, esquerda e direita.

## Adicione texto a uma imagem

Mantenha o texto na imagem curto e especifique-o com precisão. Coloque o texto exato entre
aspas, preserve o uso desejado de maiúsculas e minúsculas e descreva o estilo da
fonte, o tamanho, a cor e o posicionamento. Se o nome for incomum, soletre-o letra por letra
quando a precisão for importante. Informe se qualquer outro texto é permitido.

## Crie infográficos e layouts densos

A geração de imagens pode ajudar a criar rascunhos de materiais explicativos, pôsteres, diagramas com rótulos,
linhas do tempo e outros elementos visuais ricos em informações. Descreva a hierarquia das informações
e o layout, mantenha os rótulos concisos e peça que o texto seja renderizado com nitidez.
Quando houver muito texto ou a tipografia for crítica para a produção, revise cada palavra e finalize
o recurso em uma ferramenta de design, se necessário.

## Outras considerações

- **Tenha cuidado ao usar a imagem de alguém.** Ao retratar uma pessoa real, forneça uma
  foto de referência quando for apropriado e confirme que você tem permissão para usar
  a imagem dela.
- **Peça uma abordagem original.** Solicite um design genérico ou original
  em vez de imitar uma marca, um produto, um artista ou uma obra de arte em particular.
- **A atribuição de crédito é opcional.** Não é necessário dar crédito à OpenAI pelas imagens geradas,
  mas você pode explicar como um recurso foi criado quando esse contexto for útil.
- **Siga as políticas aplicáveis.** Use as imagens de acordo com as diretrizes da sua
  organização e com as [políticas de uso
  da OpenAI](https://openai.com/policies/usage-policies/).

## Documentação relacionada

- [Preços do Codex](/pt-BR/codex/pricing#image-generation-usage-limits)
- [Entradas de imagem](/pt-BR/codex/image-inputs)
- [Guia da API de geração de imagens](/api/docs/guides/image-generation)
- [Trabalhar com arquivos](/pt-BR/codex/artifacts-viewer)
- [Como criar imagens com o ChatGPT](https://openai.com/academy/image-generation/)

  
    <span slot="icon">
      
    </span>
    Explore mais prompts e resultados de geração de imagens.
  

- [Entradas de imagem](/pt-BR/codex/image-inputs)
- [Guia da API de geração de imagens](/api/docs/guides/image-generation)
- [Trabalhar com arquivos](/pt-BR/codex/artifacts-viewer)
- [Como criar imagens com o ChatGPT](https://openai.com/academy/image-generation/)

  
    <span slot="icon">
      
    </span>
    Explore mais prompts e resultados de geração de imagens.
  

- [Preços do Codex](/pt-BR/codex/pricing#image-generation-usage-limits)
- [Entradas de imagem](/pt-BR/codex/image-inputs)
- [Guia da API de geração de imagens](/api/docs/guides/image-generation)
- [Trabalhar com arquivos](/pt-BR/codex/artifacts-viewer)

  
    <span slot="icon">
      
    </span>
    Explore mais prompts e resultados de geração de imagens.

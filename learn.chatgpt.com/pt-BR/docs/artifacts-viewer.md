<!-- source: https://learn.chatgpt.com/pt-BR/docs/artifacts-viewer -->

Quando uma tarefa gerar um arquivo, forneça ao ChatGPT os dados de origem, o tipo de arquivo esperado,
a estrutura e os critérios de revisão relevantes para a tarefa. As ferramentas de pré-visualização e
revisão dependem da interface usada.

O aplicativo do ChatGPT para desktop exibe, ao lado do chat, pré-visualizações de documentos, apresentações,
planilhas e arquivos PDF gerados. Quando as pré-visualizações automáticas estão
ativadas, o aplicativo pode abrir um arquivo gerado após a conclusão da tarefa.

Quando as pré-visualizações HTML estiverem disponíveis, os arquivos `.html` e `.htm` gerados também podem
ser abertos como pré-visualizações interativas. Alterne entre a pré-visualização renderizada e a visualização
do código-fonte para inspecionar o resultado ou o HTML subjacente.

Use anotações para indicar uma parte específica de uma pré-visualização compatível e solicitar
uma revisão pontual.

No ChatGPT Work na Web, anexe arquivos de origem ou peça ao ChatGPT para criar um
documento, uma apresentação, uma planilha ou um PDF. Revise o arquivo gerado no
chat, baixe-o quando necessário e dê feedback específico para a próxima versão.

O Codex CLI pode criar e editar arquivos no diretório de trabalho, mas não
oferece pré-visualização gráfica dos arquivos nem uma interface de anotações. Peça ao Codex para informar cada
caminho de saída e as verificações que realizou.

A extensão para IDE pode criar e editar arquivos no workspace. Revise arquivos de texto e
de código no editor e abra documentos, apresentações, planilhas ou
arquivos PDF em um visualizador compatível.

  
    
  

## Criar arquivos para revisão

Para planilhas e apresentações, descreva as abas, as colunas, os gráficos,
as seções dos slides e as verificações esperadas. Peça ao ChatGPT para explicar onde salvou o
arquivo de saída e como verificou o resultado.

<a id="refine-files-with-annotations"></a>
<span id="follow-artifact-work"></span>
<a id="review-and-refine-files"></a>

## Refinar arquivos com anotações

As anotações permitem indicar uma parte específica de um arquivo e dizer ao ChatGPT
o que mudar. O mesmo fluxo de trabalho com anotações disponível para código, arquivos Markdown
e sites também funciona com documentos, planilhas e
apresentações.

Por exemplo, você pode:

- Selecione uma barra de navegação de um site e peça ao ChatGPT para alterar sua fonte.
- Destaque uma afirmação em uma tese de investimento e peça a fonte que a sustenta.
- Marque um gráfico em um slide e solicite um rótulo mais claro.

O ChatGPT usa a área selecionada como contexto para sua solicitação, permitindo que você refine
o arquivo sem começar do zero nem alterar as partes de que já gosta.
As anotações são especialmente úteis após o primeiro rascunho, quando o trabalho precisa de
revisão e novos ajustes.

## Revisar e refinar arquivos na Web

Abra ou baixe o arquivo gerado para revisá-lo no visualizador apropriado.
Ao solicitar uma revisão, indique a página, o slide, a aba, a tabela ou o trecho que
precisa de atenção e descreva o que deve permanecer inalterado. Peça ao ChatGPT para informar
o novo nome do arquivo e as verificações que realizou antes de você baixar a próxima
versão.

## Revisar e refinar arquivos

Use a barra lateral do chat enquanto uma tarefa estiver em execução. Ela pode exibir o plano do agente,
as fontes, os arquivos gerados e o resumo do chat para que você possa orientar o trabalho,
inspecionar os arquivos gerados e pedir outra rodada de ajustes.

Peça ao ChatGPT para explicar onde salvou cada arquivo e como verificou o
resultado. Use a pré-visualização para inspecionar o arquivo gerado e dê feedback específico sobre
os aspectos da estrutura, dos dados, do layout ou da validação que precisam de outra revisão.

## Documentação relacionada

- [Geração de imagens](/pt-BR/codex/image-generation)

<!-- source: https://learn.chatgpt.com/pt-BR/docs/extend/record-and-replay -->

O recurso Gravar e reproduzir está disponível no macOS. O Uso do computador também precisa estar disponível e ativado.

O recurso Gravar e reproduzir permite demonstrar um fluxo de trabalho no
Mac e transformá-lo em uma habilidade reutilizável. Use-o quando o fluxo for repetitivo,
depender das suas preferências ou for mais fácil de mostrar do que de descrever em um prompt.

Por exemplo, você pode gravar como registrar uma despesa, reservar uma vaga de estacionamento,
criar uma issue com a configuração correta, publicar um vídeo ou baixar um relatório
recorrente. O ChatGPT ou o Codex pode transformar esse padrão em uma habilidade que você pode usar
novamente com o Uso do computador, ações no navegador, plug-ins conectados ou uma combinação
desses recursos.

## Antes de começar

Escolha um fluxo de trabalho que você já saiba concluir. O recurso Gravar e reproduzir funciona
melhor quando as etapas são estáveis e os critérios de sucesso estão claros.

## Iniciar uma gravação

1. No aplicativo do ChatGPT para desktop, selecione ChatGPT e ative Work no seletor, ou selecione Codex. Depois, abra **Plug-ins**.
2. Abra o menu **+** .
3. Selecione **Gravar uma habilidade**.
4. Revise o prompt sugerido, adicione qualquer contexto útil e envie-o.
5. Quando o chat solicitar permissão para gravar suas ações, aprove a
solicitação assim que puder começar a demonstrar o fluxo de trabalho.
6. Execute o fluxo de trabalho no Mac.
7. Quando terminar, encerre a gravação pela barra de menus ou pela sobreposição, ou informe no
chat que terminou.

Durante a gravação, o ChatGPT ou o Codex observa as ações e o conteúdo das janelas
necessários para aprender o fluxo de trabalho. A gravação continua até você encerrá-la. Mantenha a
gravação focada na tarefa que você quer que a habilidade ensine.

Depois de encerrar a gravação, o ChatGPT ou o Codex analisa o fluxo de trabalho capturado e
cria o rascunho de uma habilidade. A habilidade explica quando usar o fluxo, quais dados de entrada são
necessários, quais etapas seguir e como verificar o resultado. Você também pode pedir
mais ajustes.

## Reproduzir o fluxo de trabalho

Inicie uma nova conversa no ChatGPT ou no Codex e peça que ele use a habilidade gerada. Informe
os valores que forem diferentes desta vez, como o arquivo a ser enviado, a
issue a ser criada ou o intervalo de datas do relatório.

O produto usa a habilidade como contexto reutilizável para a tarefa. Assim, ele pode
concluir o fluxo de trabalho com as ferramentas disponíveis no ambiente atual,
incluindo o Uso do computador, ações no navegador e plug-ins instalados.

## Dicas para gravações melhores

- Mantenha a demonstração breve e completa.
- Antes de começar a gravar, informe seu objetivo e quaisquer dados de entrada específicos que possam variar entre
os usos da habilidade.
- Use dados de entrada realistas, mas evite segredos e dados sensíveis.
- Depois da gravação, refine a habilidade para explicitar preferências implícitas importantes,
como convenções de nomenclatura, valores padrão de campos ou pontos de decisão.
- Encerre a gravação quando o fluxo de trabalho estiver concluído, em vez de continuar com
etapas de limpeza não relacionadas.

## Quando criar outro plug-in

Gravar e reproduzir é uma forma rápida de criar uma habilidade a partir de um fluxo de trabalho demonstrado.
Se quiser distribuir um pacote independente e estável para toda a equipe, agrupar
várias habilidades, incluir conectores, adicionar servidores MCP ou gerenciar
metadados de instalação, transforme esse fluxo de trabalho em um plug-in próprio. Consulte
[Criar plugins](https://developers.openai.com/plugins/build/plugins).

## Solução de problemas

### Não vejo o recurso Gravar e reproduzir

Se sua organização gerencia o Codex com `requirements.toml`, o requisito
`[features].computer_use` também controla o recurso Gravar e reproduzir. Definir
`computer_use = false` torna ambos os recursos indisponíveis.

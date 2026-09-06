<!-- source: https://learn.chatgpt.com/pt-BR/docs/skills-and-plugins -->

Habilidades e plug-ins ajudam o ChatGPT e o Codex a realizar tarefas recorrentes com as
instruções, os recursos e as ferramentas de que precisam. Com isso, você não precisa colar em cada chat o
mesmo prompt, modelo, conjunto de requisitos ou processo.

- Uma **habilidade** reúne instruções e recursos de apoio para uma
  tarefa ou um fluxo de trabalho específicos.
- Um **plug-in** é um pacote instalável que pode incluir habilidades, conectores ou
  ambos. Os conectores têm como base servidores do Model Context Protocol (MCP) e podem
  incluir, opcionalmente, uma interface personalizada do ChatGPT.

## Use habilidades em tarefas recorrentes

Uma habilidade é um fluxo de trabalho reutilizável que oferece ao ChatGPT ou ao Codex
orientações específicas para uma tarefa. Ela pode registrar como você já realiza atividades
recorrentes, para que qualquer um dos produtos siga o mesmo processo sempre que essa tarefa surgir.

Uma habilidade pode combinar:

- Um nome e uma descrição que ajudam o ChatGPT e o Codex a identificar quando a habilidade
se aplica.
- Instruções do fluxo de trabalho que definem o processo e o resultado esperado.
- Recursos de apoio, como modelos, exemplos, diretrizes de marca, esquemas
ou ferramentas conectadas.

As habilidades são mais úteis quando é preciso seguir sempre o mesmo processo para obter bons resultados. Por
exemplo, uma habilidade pode preparar um resumo diário, revisar a documentação, criar uma
apresentação, aplicar o padrão de redação de uma equipe ou coletar informações das
mesmas ferramentas conectadas toda semana.

Use habilidades para aumentar a consistência, integrar as práticas recomendadas da equipe ao
fluxo de trabalho e compartilhar um processo padronizado, em vez de depender de conhecimento
não documentado.

O ChatGPT e o Codex podem escolher uma habilidade quando sua solicitação corresponder à finalidade dela. Você
também pode selecionar uma explicitamente. O ChatGPT aceita menções com `@`, enquanto o Codex
aceita menções a habilidades com `$`.

## Criar habilidades

Você pode começar transformando uma tarefa que já repete em um guia prático e objetivo para
o ChatGPT e o Codex. Algumas boas opções para uma primeira habilidade são uma atualização semanal, um briefing de campanha,
o acompanhamento após uma reunião ou qualquer tarefa em que as etapas e o formato devam permanecer
consistentes.

Para criar uma habilidade útil:

1. **Escolha uma tarefa bem definida.** Anote o que costuma usar como ponto de partida, como
   arquivos, links ou notas, e como deve ser o resultado final.
2. **Descreva o fluxo de trabalho.** No ChatGPT, comece com `@skill-creator`; no Codex,
   use `$skill-creator`. Explique o objetivo, as etapas a seguir, o formato
   esperado e tudo o que a habilidade sempre deve incluir ou evitar. Adicione um modelo
   ou um bom exemplo, se tiver.
3. **Revise e teste o rascunho.** Confira as instruções, teste a habilidade com uma
   solicitação realista e faça ajustes se o resultado omitir alguma etapa ou se afastar
   do formato desejado.
4. **Instale e reutilize a habilidade.** Depois de habilitada, o ChatGPT ou o Codex pode usá-la
   em solicitações relevantes, ou você pode selecioná-la explicitamente. Você também pode
   compartilhá-la com colegas de equipe quando as configurações do workspace permitirem.

Para saber mais sobre como criar habilidades, consulte nosso guia específico abaixo.

  
    <span slot="icon">
      
    </span>
    Crie, teste e compartilhe habilidades reutilizáveis com o ChatGPT e o Codex.
  

## Use plug-ins para ferramentas e fluxos de trabalho compartilhados

Os plug-ins facilitam a instalação e o compartilhamento de funcionalidades reutilizáveis. Um plug-in pode
combinar habilidades com conectores de serviços como GitHub, Google Drive ou
Slack e incluir servidores MCP que oferecem ferramentas e contexto adicionais.

O ChatGPT e o Codex compartilham um único diretório universal de plug-ins. Explore-o quando quiser
adicionar um fluxo de trabalho existente em vez de criar um por conta própria. Depois de instalar
um plug-in, descreva a tarefa diretamente ou escolha explicitamente um plug-in ou uma habilidade incluída
usando a sintaxe de invocação da interface em uso.

[Saiba como instalar e usar plug-ins](/pt-BR/codex/plugins).

## Escolha entre uma habilidade e um plug-in

Use uma habilidade quando precisar de instruções reutilizáveis para uma tarefa específica. Use um
plug-in quando quiser um pacote instalável que combine instruções com
serviços conectados ou outras ferramentas.

Você também pode demonstrar um fluxo de trabalho com o recurso
[Gravar e reproduzir](/pt-BR/codex/extend/record-and-replay), que transforma a gravação em uma
habilidade reutilizável. Para empacotar e distribuir seu próprio pacote, consulte
[Criar plugins](https://developers.openai.com/plugins/build/plugins).

Se o seu plug-in precisar se conectar a um serviço ou disponibilizar ferramentas MCP, consulte
[Criar um servidor MCP](https://developers.openai.com/plugins/build/mcp-server). Quando seu plug-in estiver pronto para revisão pública,
consulte [Enviar plug-ins](https://developers.openai.com/plugins/deploy/submission).

Para ver mais exemplos de fluxos de trabalho reutilizáveis, consulte [Como usar habilidades na OpenAI
Academy](https://openai.com/academy/skills/).

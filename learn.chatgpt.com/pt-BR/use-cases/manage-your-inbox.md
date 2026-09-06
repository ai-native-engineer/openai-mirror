<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/manage-your-inbox -->

## Antes de começar

Você pode executar este fluxo no ChatGPT Work pelo navegador ou pelo aplicativo para desktop. Antes de começar:

- **Conecte seu email.** Instale o [plug-in do Gmail ou do Outlook Email](/pt-BR/docs/plugins). Você também pode conectar o Slack, o Google Drive e seu calendário para fornecer mais contexto ao ChatGPT ao criar rascunhos de resposta.
- **Escolha onde as verificações agendadas serão executadas.** Comece pelo navegador se quiser que as verificações continuem quando seu notebook estiver desligado. No desktop, mantenha o computador ligado e o aplicativo do ChatGPT para desktop em execução. Os chats por voz não oferecem suporte a [tarefas agendadas](/pt-BR/docs/automations), portanto, configure ou gerencie essas tarefas pelo chat.

## O que esperar

O ChatGPT analisa emails recentes, identifica mensagens que exigem atenção, propõe uma limpeza e prepara respostas sem enviá-las. Depois que você aprovar a limpeza, ele poderá aplicar essas alterações às mensagens antigas acumuladas. Veja como pode ser essa conversa:

<div data-use-case-export-only>

Analisei a caixa de entrada da sua conta profissional conectada, com foco em lançamentos de produtos, documentação e atividades de produção. Ela tem **116 mensagens, 96 não lidas**; a maioria das mensagens não lidas corresponde a atividades de projetos, atualizações do calendário, notificações de arquivos compartilhados e newsletters.

### O que exige atenção

- **Preparação para a gravação:** envie os tópicos solicitados para a demonstração, uma breve biografia e uma foto antes da sessão de amanhã.
- **Revisão da documentação:** resolva os pontos do feedback sobre a precisão das informações do produto antes de dar continuidade ao guia.
- **Falha na implantação da prévia:** investigue a falha no build antes de confiar nas alterações atuais.
- **Tarefa de benefícios:** conclua a alteração pendente nos benefícios.
- **Alerta de login:** confirme se o login recente foi feito por você e, caso contrário, siga as instruções do alerta.

### Limpeza

Eu aplicaria os marcadores `Project activity`, `Calendar` e `Docs` às notificações rotineiras de projetos, calendário e documentos e as arquivaria; os emails arquivados continuariam disponíveis para pesquisa. Solicitações diretas, revisões em andamento, builds com falha, alertas de segurança e qualquer item pendente continuariam visíveis. Vale a pena analisar newsletters e outras assinaturas recorrentes separadamente.

### Uma resposta à pessoa responsável pela gravação

A pessoa responsável pela gravação está aguardando os tópicos da demonstração, uma breve biografia e uma foto. Consultei as informações mais recentes sobre o agendamento e criei um rascunho de resposta no seu estilo:

> Vai ser ótimo. Pretendo mostrar os três fluxos de trabalho que discutimos e enviarei a biografia e a foto hoje. Vi o convite atualizado no calendário, então vou me organizar de acordo com o novo horário.

Daqui em diante, verificarei às **8h e às 16h nos dias úteis**. Destacarei emails novos ou alterados que exigirem sua atenção, consultarei fontes conectadas, como mensagens, documentos ou seu calendário, quando forem relevantes, e prepararei respostas no seu estilo. Você pode alterar minhas instruções a qualquer momento respondendo aqui.

### O que você gostaria que eu fizesse?

1. **Aplicar a limpeza?** Sim / não. As mensagens rotineiras receberão marcadores e serão arquivadas, não excluídas.
2. **Salvar a resposta como rascunho?** Sim / não.
3. **Manter a programação e as prioridades propostas?** Sim / não.

Responda com “1 sim, 2 sim, 3 não” e inclua qualquer alteração.

</div>

**Aviso:** O plug-in do Gmail pode mover emails para a Lixeira quando você pedir explicitamente. Primeiro, revise os grupos propostos e algumas mensagens de exemplo. Se tiver dúvidas sobre alguma mensagem, arquive-a em vez de excluí-la. As ações disponíveis podem variar de acordo com o plug-in de email e as configurações do workspace.

## Como funciona

Um fluxo de trabalho de email tem algumas partes:

- **Contexto conectado:** os plug-ins permitem que o ChatGPT leia seus emails e consulte outras ferramentas conectadas quando for necessário mais contexto para responder. O Slack pode ter a conversa ou a decisão mais recente, o Google Drive pode conter arquivos ou documentos relevantes do projeto e seu calendário pode esclarecer datas ou reuniões.
- **Prioridades:** você pode informar ao ChatGPT quais pessoas, solicitações, alertas e mensagens recorrentes devem ser priorizados ou ignorados. As verificações futuras podem seguir essas instruções.
- **Limites de aprovação:** o ChatGPT propõe uma limpeza e cria rascunhos de resposta, mas aguarda sua aprovação antes de agir.
- **Tarefas agendadas:** sem precisar esperar que você volte e peça novamente, o ChatGPT pode verificar se há novas mensagens na mesma tarefa de acordo com uma programação.

## Crie seu próprio fluxo de trabalho de email

Você pode ser mais específico quando já sabe o que quer. Um prompt de **email profissional**
pode destacar conversas ativas, solicitações, aprovações e o contexto
do projeto:

Já um prompt de **e-mail pessoal** pode dar mais destaque a pessoas conhecidas, contas,
encomendas, viagens, compromissos e alertas de conta:

Os dois exemplos seguem a mesma estrutura básica: o que verificar, o que é importante, o que fazer, quando fazer e o que exige aprovação.

## Vá além

Depois que o fluxo de trabalho básico estiver em execução, você poderá refiná-lo ou pedir ao ChatGPT que cuide de outras tarefas úteis de e-mail.

**Sempre consulte o contexto certo**

**Redija uma atualização recorrente**

**Acompanhe e-mails sem resposta**

**Altere o formato**

**Ensine o que é importante**

**Ajuste como as respostas são redigidas**

**Altere os horários das verificações**

Mantenha as ações de limpeza e resposta sujeitas à sua aprovação até confiar nas regras.

As ações do Gmail e do Outlook e as tarefas agendadas dependem do seu plano e das configurações do workspace.

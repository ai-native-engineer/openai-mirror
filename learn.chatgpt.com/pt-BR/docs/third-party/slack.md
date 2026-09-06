<!-- source: https://learn.chatgpt.com/pt-BR/docs/third-party/slack -->

Use o Codex no Slack para iniciar tarefas de programação em canais e threads. Mencione `@Codex` e inclua um prompt; o Codex cria um chat na nuvem e responde com os resultados.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>

<br />

## Configure o aplicativo do Slack

1. Configure os [chats do Codex na nuvem](/pt-BR/codex/cloud). Você precisa de um plano Plus, Pro, Business, Enterprise ou Edu (consulte os [preços do ChatGPT](https://chatgpt.com/pricing)), de uma conta do GitHub conectada e de pelo menos um [ambiente](/pt-BR/codex/environments/cloud-environment).
2. Acesse as [configurações do Codex](https://chatgpt.com/codex/settings/connectors) e instale o aplicativo do Slack no seu workspace. Dependendo das políticas do workspace do Slack, talvez um administrador precise aprovar a instalação.
3. Adicione `@Codex` a um canal. Se ele ainda não estiver no canal, o Slack solicitará que você o adicione ao mencioná-lo.

<a id="start-a-task"></a>

## Inicie um chat

1. Em um canal ou uma thread, mencione `@Codex` e inclua seu prompt. O Codex pode consultar mensagens anteriores da thread, então geralmente não é preciso repetir o contexto.
2. (Opcional) Especifique um ambiente ou repositório no prompt, por exemplo: `@Codex fix the above in openai/codex`.
3. Aguarde o Codex reagir (👀) e responder com um link para o chat. Quando terminar, o Codex publicará o resultado e, dependendo das suas configurações, uma resposta na thread.

### Como o Codex escolhe um ambiente e um repositório

- O Codex verifica os ambientes aos quais você tem acesso e seleciona aquele que mais se adequa à sua solicitação. Se a solicitação for ambígua, ele recorre ao ambiente usado mais recentemente.
- O chat é executado na branch padrão do primeiro repositório listado no mapa de repositórios desse ambiente. Atualize o mapa de repositórios no Codex se precisar usar outro repositório por padrão ou adicionar mais repositórios.
- Se nenhum ambiente ou repositório adequado estiver disponível, o Codex responderá no Slack com instruções para corrigir o problema antes de tentar novamente.

### Controles de dados para empresas

Por padrão, o Codex responde na thread. A resposta pode incluir informações do ambiente em que a tarefa foi executada.
Para evitar isso, um administrador de uma conta empresarial pode desmarcar **Permitir que o aplicativo Codex para Slack publique respostas quando a tarefa for concluída** nas [configurações do workspace do ChatGPT](https://chatgpt.com/admin/settings). Quando um administrador desativa as respostas, o Codex responde apenas com um link para o chat.

### Uso de dados, privacidade e segurança

Quando você menciona `@Codex`, o Codex recebe sua mensagem e o histórico da thread para entender sua solicitação e criar um chat.
O tratamento de dados segue a [Política de Privacidade](https://openai.com/privacy) e os [Termos de Uso](https://openai.com/terms/) da OpenAI, bem como outras [políticas](https://openai.com/policies) aplicáveis.
Para saber mais sobre segurança, consulte a [documentação de segurança](/pt-BR/codex/agent-approvals-security) do Codex.

O Codex usa modelos de linguagem de grande porte, que podem cometer erros. Sempre revise as respostas e os diffs.

### Dicas e solução de problemas

- **Conexões ausentes**: se o Codex não conseguir confirmar sua conexão com o Slack ou o GitHub, ele responderá com um link para restabelecer a conexão.
- **Escolha inesperada de ambiente**: responda na thread informando o ambiente desejado (por exemplo, `Please run this in openai/openai (applied)`) e mencione `@Codex` novamente.
- **Threads longas ou complexas**: resuma os detalhes principais na mensagem mais recente para que o Codex não deixe passar informações de contexto presentes em mensagens anteriores da thread.
- **Publicação no workspace**: alguns workspaces empresariais restringem a publicação de respostas finais. Nesses casos, abra o link do chat para ver o andamento e os resultados.
- **Mais ajuda**: consulte a [Central de Ajuda da OpenAI](https://help.openai.com/).

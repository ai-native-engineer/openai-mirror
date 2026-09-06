<!-- source: https://learn.chatgpt.com/pt-BR/docs/third-party/linear -->

Use o Codex no Linear para delegar trabalho a partir de issues. Atribua uma issue ao Codex ou mencione `@Codex` em um comentário, e o Codex criará um chat na nuvem e responderá informando o andamento e os resultados.

O Codex no Linear está disponível nos planos pagos (consulte [Preços](/pt-BR/codex/pricing)).

Se você estiver em um plano Empresas, peça ao administrador do workspace do ChatGPT para ativar os chats do Codex na nuvem nas [configurações do workspace](https://chatgpt.com/admin/settings) e habilitar o **Codex para Linear** nas [configurações do conector](https://chatgpt.com/admin/ca).

## Configurar a integração com o Linear

1. Configure os [chats do Codex na nuvem](/pt-BR/codex/cloud) conectando o GitHub ao [Codex](https://chatgpt.com/codex) e criando um [ambiente](/pt-BR/codex/environments/cloud-environment) para o repositório em que você quer que o Codex trabalhe.
2. Acesse as [configurações do Codex](https://chatgpt.com/codex/settings/connectors) e instale o **Codex para Linear** no seu workspace.
3. Vincule sua conta do Linear mencionando `@Codex` em uma thread de comentários de uma issue do Linear.

## Delegar trabalho ao Codex

Você pode delegar de duas maneiras:

### Atribuir uma issue ao Codex

Depois de instalar a integração, você pode atribuir issues ao Codex da mesma forma que as atribui aos colegas de equipe. O Codex começa a trabalhar e publica atualizações na issue.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

### Mencionar `@Codex` nos comentários

Você também pode mencionar `@Codex` em threads de comentários para delegar trabalho ou fazer perguntas. Depois que o Codex responder, continue a conversa na thread para prosseguir no mesmo chat.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

Depois que o Codex começa a trabalhar em uma issue, ele [escolhe um ambiente e um repositório](#how-codex-chooses-an-environment-and-repo) para trabalhar.
Para fixar um repositório específico, inclua-o no comentário, por exemplo: `@Codex fix this in openai/codex`.

Para acompanhar o andamento:

- Abra **Atividade** na issue para ver as atualizações de andamento.
- Abra o link do chat para acompanhar o andamento com mais detalhes.

Quando o Codex termina, ele publica um resumo e um link para o chat concluído para que você possa criar uma pull request.

### Como o Codex escolhe um ambiente e um repositório

- O Linear sugere um repositório com base no contexto da issue. O Codex seleciona o ambiente que melhor corresponde a essa sugestão. Se a solicitação for ambígua, ele recorre ao ambiente que você usou mais recentemente.
- O chat é executado na branch padrão do primeiro repositório listado no mapa de repositórios desse ambiente. Atualize o mapa de repositórios no Codex se precisar de outro repositório padrão ou de mais repositórios.
- Se não houver nenhum ambiente ou repositório adequado disponível, o Codex responderá no Linear com instruções para corrigir o problema antes de tentar novamente.

## Atribuir issues automaticamente ao Codex

Você pode atribuir issues automaticamente ao Codex usando regras de triagem:

1. No Linear, acesse **Configurações**.
2. Em **Suas equipes**, selecione sua equipe.
3. Nas configurações do fluxo de trabalho, abra **Triagem** e ative-a.
4. Em **Regras de triagem**, crie uma regra e selecione **Delegar** \> **Codex** (e quaisquer outras propriedades que você queira definir).

O Linear atribui automaticamente ao Codex as novas issues que entram na triagem.
Quando você usa regras de triagem, o Codex executa os chats com a conta de quem criou a issue.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

## Uso de dados, privacidade e segurança

Quando você menciona `@Codex` ou atribui uma issue ao Codex, ele recebe o conteúdo da sua issue para entender sua solicitação e criar um chat.
O tratamento dos dados segue a [Política de Privacidade](https://openai.com/privacy) e os [Termos de Uso](https://openai.com/terms/) da OpenAI, além de outras [políticas](https://openai.com/policies) aplicáveis.
Para saber mais sobre segurança, consulte a [documentação de segurança do Codex](/pt-BR/codex/agent-approvals-security).

O Codex usa modelos de linguagem de grande porte que podem cometer erros. Sempre revise as respostas e os diffs.

## Dicas e solução de problemas

- **Conexões ausentes**: se o Codex não conseguir confirmar sua conexão com o Linear, ele responderá na issue com um link para conectar sua conta.
- **Escolha inesperada de ambiente**: responda na thread informando o ambiente que você quer usar (por exemplo, `@Codex please run this in openai/codex`).
- **Parte errada do código**: adicione mais contexto à issue ou dê instruções explícitas no comentário em que mencionar `@Codex`.
- **Mais ajuda**: consulte a [Central de Ajuda da OpenAI](https://help.openai.com/).

<a id="connect-linear-for-local-tasks-mcp"></a>

## Conectar o Linear para trabalho local (MCP)

Se você usa o aplicativo do ChatGPT para desktop, o Codex CLI ou a extensão para IDE e quer acessar as issues do Linear localmente, configure o servidor Model Context Protocol (MCP) do Linear.

Para saber mais, [consulte a documentação do MCP do Linear](https://linear.app/integrations/codex-mcp).

As etapas de configuração do servidor MCP são as mesmas para a extensão para IDE e para a CLI, pois ambas compartilham a mesma configuração.

### Usar a CLI (recomendado)

Se você tiver a CLI instalada, execute:

```bash
codex mcp add linear --url https://mcp.linear.app/mcp

Esse comando solicita que você faça login na sua conta do Linear e a conecte ao Codex.

### Configurar manualmente

1. Abra `~/.codex/config.toml` no seu editor.
2. Adicione o seguinte:

```toml
[mcp_servers.linear]
url = "https://mcp.linear.app/mcp"

3. Execute `codex mcp login linear` para fazer login.

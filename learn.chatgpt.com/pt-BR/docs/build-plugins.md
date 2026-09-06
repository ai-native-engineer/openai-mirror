<!-- source: https://learn.chatgpt.com/pt-BR/docs/build-plugins -->

Para criar ou enviar um plug-in, consulte a documentação completa
[para criadores em developers.openai.com](/plugins).

<div className="not-prose my-6">
  
    Criar e enviar um plug-in
  
</div>

Esta página oferece uma breve introdução. Um plug-in é um pacote instalável
que pode incluir habilidades, um servidor MCP ou ambos. Um servidor MCP também pode retornar
uma interface opcional.

ChatGPT e Codex compartilham um único diretório universal de plug-ins. Publique um plug-in público
uma única vez para que a mesma listagem possa ser encontrada nas interfaces compatíveis dos dois
produtos. Durante o desenvolvimento, use um marketplace local para testar o pacote
antes de enviá-lo ao diretório universal.

Para distribuir plug-ins no workspace pelo GitHub, consulte
[Gerenciamento de plug-ins](/pt-BR/codex/enterprise/plugin-management).

Comece com uma habilidade enquanto ainda estiver aprimorando um único fluxo de trabalho pessoal.
Crie um plug-in quando quiser compartilhar esse fluxo de trabalho, agrupar habilidades relacionadas,
conectar-se a um serviço externo ou distribuir uma capacidade estável para uma equipe.

## Criar um plug-in com `@plugin-creator`

Para configurar mais rapidamente, use a habilidade integrada `@plugin-creator` no modo Work
do ChatGPT ou `$plugin-creator` no Codex.

  
    
  

Descreva o resultado esperado, as habilidades ou o servidor MCP a incluir e se deseja
uma listagem em um marketplace local para testes. Por exemplo:

```text
@plugin-creator Create a plugin named meeting-follow-up.
Include a skill that turns meeting notes into decisions, owners, and next steps.
Add it to a personal marketplace so I can test it locally.

A habilidade cria o manifesto obrigatório `.codex-plugin/plugin.json`, organiza
a pasta do plug-in e pode adicioná-lo a um marketplace local.

  
    
  

Quando terminar:

1. Revise `.codex-plugin/plugin.json`.
2. Verifique cada habilidade incluída em `skills/`.
3. Recarregue o ChatGPT ou o Codex e instale o plug-in usando a respectiva fonte do marketplace
local.
4. Teste o plug-in em uma nova conversa usando solicitações representativas.

Se o plug-in incluir um servidor MCP, primeiro crie e teste esse servidor. Depois,
forneça a `@plugin-creator` os detalhes da conexão registrada. Siga todo o
[fluxo de trabalho do servidor MCP](https://developers.openai.com/plugins/build/mcp-server)
para ferramentas, autenticação, implantação e testes.

## Criar manualmente um plug-in apenas com habilidades

Um plug-in mínimo contém um manifesto e pelo menos uma habilidade:

```text
meeting-follow-up/
├── .codex-plugin/
│   └── plugin.json
└── skills/
    └── meeting-follow-up/
        └── SKILL.md

Crie `.codex-plugin/plugin.json`:

```json
{
  "name": "meeting-follow-up",
  "version": "1.0.0",
  "description": "Turn meeting notes into decisions and next steps",
  "skills": "./skills/"
}

Depois, adicione `skills/meeting-follow-up/SKILL.md`:

```md
---
name: meeting-follow-up
description: Extract decisions, owners, and next steps from meeting notes.
---

Review the meeting notes. Return:

1. Decisions
2. Action items with owners
3. Open questions

Use um nome estável em kebab case para o plug-in. Descreva a habilidade com detalhes
suficientes para que o ChatGPT e o Codex reconheçam quando o fluxo de trabalho se aplica.

Use `@plugin-creator` para adicionar a pasta a um marketplace local. Em seguida, instale e
teste o plug-in antes de compartilhá-lo.

## Continuar com a documentação para criadores

Para consultar a documentação completa para criadores, acesse a
[documentação sobre Plug-ins](https://developers.openai.com/plugins/). Ela aborda:

- [Arquitetura de plug-ins](https://developers.openai.com/plugins/concepts/plugins)
- [Criar habilidades](https://developers.openai.com/plugins/build/skills)
- [Criar um servidor MCP](https://developers.openai.com/plugins/build/mcp-server)
- [Adicionar uma interface opcional](https://developers.openai.com/plugins/build/chatgpt-ui)
- [Empacotar um plug-in](https://developers.openai.com/plugins/build/plugins)
- [Testar um plug-in](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [Enviar e publicar](https://developers.openai.com/plugins/deploy/submission)

Para explorar, instalar, ativar ou remover plug-ins, consulte [Usar
plug-ins](/pt-BR/codex/plugins).

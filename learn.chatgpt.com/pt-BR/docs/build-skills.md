<!-- source: https://learn.chatgpt.com/pt-BR/docs/build-skills -->

Use habilidades de agentes para ampliar o ChatGPT e o Codex com capacidades específicas para cada tarefa. Uma
habilidade reúne instruções, recursos e scripts opcionais para que qualquer um dos produtos
possa seguir um fluxo de trabalho de forma confiável. As habilidades se baseiam no
[padrão aberto de habilidades de agentes](https://agentskills.io).

As habilidades são o formato de criação de fluxos de trabalho reutilizáveis. Os plug-ins distribuem
habilidades reutilizáveis e conectores pelo diretório universal de plug-ins compartilhado
pelo ChatGPT e pelo Codex. Os plug-ins funcionam no Chat e no Work do ChatGPT na Web,
no desktop e em dispositivos móveis, no Codex do aplicativo do ChatGPT para desktop e na Codex
CLI. Use habilidades para criar o fluxo de trabalho e depois empacote-o como um
[plug-in](https://developers.openai.com/plugins/build/plugins) quando quiser
que outras pessoas o instalem.

As habilidades independentes estão disponíveis no aplicativo do ChatGPT para desktop, na Codex CLI e na
extensão para IDE. As habilidades incluídas em plug-ins também estão disponíveis no Chat e no Work do
ChatGPT na Web, no desktop e em dispositivos móveis.

No aplicativo do ChatGPT para desktop, abra **Habilidades** na barra lateral para ver e explorar as habilidades
criadas nos seus projetos.

  
    
  

As habilidades usam **divulgação progressiva** para gerenciar o contexto com eficiência. O ChatGPT e o
Codex começam pelo nome e pela descrição de cada habilidade e depois carregam todas as instruções do arquivo
`SKILL.md` quando decidem usá-la.

No Codex, a lista inicial também inclui o caminho do arquivo de cada habilidade. Para não comprometer
o espaço disponível para o restante do prompt, essa lista usa no máximo 2% da janela de
contexto do modelo ou 8.000 caracteres quando a janela de contexto é desconhecida. Se muitas
habilidades estiverem instaladas, o Codex primeiro reduz suas descrições. Em conjuntos grandes de
habilidades, o Codex pode omitir algumas da lista inicial e exibir um aviso.

Esse limite se aplica apenas à lista inicial de habilidades. Quando o Codex seleciona uma habilidade, ele continua lendo todas as instruções do arquivo SKILL.md dessa habilidade.

Uma habilidade é um diretório com um arquivo `SKILL.md`, além de scripts e referências opcionais. O arquivo `SKILL.md` deve incluir `name` e `description`.

<a id="how-codex-uses-skills"></a>

## Como o ChatGPT e o Codex usam habilidades

O ChatGPT e o Codex podem ativar habilidades de duas formas:

1. **Invocação explícita:** inclua a habilidade diretamente no seu prompt. No
   ChatGPT, digite `@` para selecionar uma habilidade. Na Codex CLI ou na extensão para IDE, execute
`/skills` ou digite `$` para mencionar uma habilidade.
2. **Invocação implícita:** o ChatGPT ou o Codex pode escolher uma habilidade quando sua tarefa
   corresponder ao campo `description` da habilidade.

Como a correspondência implícita depende de `description`, escreva descrições concisas
com escopo e limites claros. Coloque o principal caso de uso e as palavras de acionamento no início
para que um host consiga identificar a habilidade mesmo quando as descrições forem encurtadas.

## Criar uma habilidade

Se você já conhece o fluxo de trabalho e é mais fácil mostrá-lo do que descrevê-lo, use
[Gravar e reproduzir](/pt-BR/codex/extend/record-and-replay). O gravador captura o
fluxo de trabalho, inspeciona as etapas e cria o rascunho de uma habilidade reutilizável a partir da
demonstração.

Se preferir descrever a habilidade, use o criador integrado. No ChatGPT
Work, invoque-o como `@skill-creator`. No Codex, invoque-o assim:

```text
$skill-creator

O criador pergunta o que a habilidade faz, quando deve ser acionada e se deve conter apenas instruções ou incluir scripts. Por padrão, ela contém apenas instruções.

Você também pode criar uma habilidade manualmente criando uma pasta com um arquivo `SKILL.md`:

```md
---
name: skill-name
description: Explain exactly when this skill should and should not trigger.
---

Skill instructions for ChatGPT or Codex to follow.

O Codex detecta automaticamente alterações nas habilidades. Se uma atualização não aparecer, reinicie o Codex.

<a id="where-to-save-skills"></a>

## De onde o Codex carrega habilidades locais

O Codex lê habilidades em locais do repositório, do usuário, do administrador e do sistema. Para repositórios, o Codex verifica `.agents/skills` em cada diretório, do diretório de trabalho atual até a raiz do repositório. Se duas habilidades tiverem o mesmo valor de `name`, o Codex não as mescla; ambas podem aparecer nos seletores de habilidades.

| Escopo da habilidade | Local                                                                                                  | Uso sugerido                                                                                                                                                                                        |
| :---------- | :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `REPO`      | `$CWD/.agents/skills` <br /> Diretório de trabalho atual: onde você inicia o Codex.                           | Se estiver em um repositório ou ambiente de código, as equipes podem versionar habilidades relevantes para uma pasta de trabalho. Por exemplo, habilidades relevantes apenas para um microsserviço ou módulo.                              |
| `REPO`      | `$CWD/../.agents/skills` <br /> Uma pasta acima do CWD quando você inicia o Codex dentro de um repositório Git.         | Se estiver em um repositório com pastas aninhadas, as organizações podem versionar habilidades relevantes para uma área compartilhada em uma pasta pai.                                                                       |
| `REPO`      | `$REPO_ROOT/.agents/skills` <br /> A pasta raiz de nível mais alto quando você inicia o Codex dentro de um repositório Git. | Se estiver em um repositório com pastas aninhadas, as organizações podem versionar habilidades relevantes para todos os usuários do repositório. Essas habilidades de raiz ficam disponíveis em qualquer subpasta do repositório. |
| `USER`      | `$HOME/.agents/skills` <br /> Qualquer habilidade adicionada à pasta pessoal do usuário.                         | Use para selecionar habilidades relevantes para um usuário e aplicáveis a qualquer repositório em que ele trabalhe.                                                                                                           |
| `ADMIN`     | `/etc/codex/skills` <br /> Qualquer habilidade adicionada à máquina ou ao contêiner em um local compartilhado do sistema. | Use para scripts de SDK, automação e para disponibilizar habilidades administrativas padrão a cada usuário da máquina.                                                                                     |
| `SYSTEM`    | Incluídas no Codex pela OpenAI.                                                                             | Habilidades úteis para um público amplo, como as habilidades skill-creator e plan. Disponíveis para todos ao iniciar o Codex.                                                                   |

O Codex oferece suporte a pastas de habilidades vinculadas por links simbólicos e segue o destino do link ao verificar esses locais.

Esses locais se destinam à criação e à descoberta locais. Quando quiser
distribuir habilidades reutilizáveis para além de um único repositório ou, se desejar, agrupá-las com
conectores, use [plug-ins](https://developers.openai.com/plugins/build/plugins).

## Distribuir habilidades com plug-ins

O uso direto de pastas de habilidades é ideal para criação local e fluxos de trabalho específicos de um repositório. Se
quiser distribuir uma habilidade reutilizável, agrupar duas ou mais habilidades ou
fornecer uma habilidade junto com um conector, empacote tudo como um
[plug-in](https://developers.openai.com/plugins/build/plugins).

Os plug-ins podem incluir uma ou mais habilidades. Opcionalmente, também podem reunir
conexões registradas com servidores MCP, configurações integradas de servidores MCP e
recursos de apresentação em um único pacote.

## Instalar habilidades selecionadas para uso local

Para adicionar habilidades selecionadas à sua configuração local do Codex, além das integradas, use `$skill-installer`. Por exemplo, para instalar a habilidade `$linear`:

```bash
$skill-installer linear

Você também pode pedir ao instalador que baixe habilidades de outros repositórios.
O Codex detecta automaticamente as habilidades recém-instaladas; se alguma não aparecer,
reinicie o Codex.

Use essa opção para configuração e experimentação locais. Para distribuir suas próprias
habilidades de forma reutilizável, prefira plug-ins.

## Ativar ou desativar habilidades locais do Codex

Use entradas `[[skills.config]]` em `~/.codex/config.toml` para desativar uma habilidade sem excluí-la:

```toml
[[skills.config]]
path = "/path/to/skill/SKILL.md"
enabled = false

Reinicie o Codex depois de alterar `~/.codex/config.toml`.

## Metadados opcionais

Adicione `agents/openai.yaml` para configurar os metadados da interface no [aplicativo do ChatGPT para desktop](/pt-BR/codex/app), definir a política de invocação e declarar dependências de ferramentas para tornar o uso da habilidade mais fluido.

```yaml
interface:
  display_name: "Optional user-facing name"
  short_description: "Optional user-facing description"
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
  brand_color: "#3B82F6"
  default_prompt: "Optional surrounding prompt to use the skill with"

policy:
  allow_implicit_invocation: false

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      description: "OpenAI Docs MCP server"
      transport: "streamable_http"
      url: "https://developers.openai.com/mcp"

`allow_implicit_invocation` (padrão: `true`): quando definido como `false`, o Codex não invoca a habilidade implicitamente com base no prompt do usuário; a invocação explícita com `$skill` continua funcionando.

## Práticas recomendadas

- Mantenha cada habilidade focada em uma única tarefa.
- Prefira instruções a scripts, a menos que precise de comportamento determinístico ou ferramentas externas.
- Escreva as etapas no imperativo, com entradas e saídas explícitas.
- Teste prompts com base na descrição da habilidade para confirmar que ela é acionada corretamente.

Para ver mais exemplos, consulte
[reparo da CI do GitHub](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci),
[PDF](https://github.com/openai/skills/tree/main/skills/.curated/pdf),
[Linear](https://github.com/openai/skills/tree/main/skills/.curated/linear),
[openai/skills](https://github.com/openai/skills) e a
[especificação de habilidades de agentes](https://agentskills.io/specification). Para
distribuir em formato instalável, prefira [plug-ins](https://developers.openai.com/plugins/build/plugins).

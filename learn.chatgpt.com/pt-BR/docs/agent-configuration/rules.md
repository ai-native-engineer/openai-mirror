<!-- source: https://learn.chatgpt.com/pt-BR/docs/agent-configuration/rules -->

Use regras para controlar quais comandos o Codex pode executar fora do Sandbox.

As regras ainda são experimentais e podem mudar.

## Criar um arquivo de regras

1. Crie um arquivo `.rules` dentro de uma pasta `rules/` ao lado de uma camada de configuração ativa (por exemplo, `~/.codex/rules/default.rules`).
2. Adicione uma regra. Este exemplo solicita aprovação antes de permitir que `gh pr view` seja executado fora do Sandbox.

   ```python
   # Prompt before running commands with the prefix `gh pr view` outside the sandbox.
   prefix_rule(
       # The prefix to match.
       pattern = ["gh", "pr", "view"],

       # The action to take when Codex requests to run a matching command.
       decision = "prompt",

       # Optional rationale for why this rule exists.
       justification = "Viewing PRs is allowed with approval",

       # `match` and `not_match` are optional "inline unit tests" where you can
       # provide examples of commands that should (or should not) match this rule.
       match = [
           "gh pr view 7888",
           "gh pr view --repo openai/codex",
           "gh pr view 7888 --json title,body,comments",
       ],
       not_match = [
           # Does not match because the `pattern` must be an exact prefix.
           "gh pr --repo openai/codex view 7888",
       ],
   )

3. Reinicie o Codex.

Na inicialização, o Codex verifica `rules/` em cada camada de configuração ativa, incluindo os locais da [Configuração da equipe](/pt-BR/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config) e a camada do usuário em `~/.codex/rules/`. As regras locais do projeto em `<repo>/.codex/rules/` só são carregadas quando a camada `.codex/` do projeto é considerada confiável.

Quando você adiciona um comando à lista de permissões na TUI, o Codex registra essa permissão na camada do usuário em `~/.codex/rules/default.rules`, para que execuções futuras possam dispensar a solicitação.

Quando as aprovações inteligentes estão ativadas (o padrão), o Codex pode sugerir uma
`prefix_rule` durante solicitações de elevação de permissões. Analise o prefixo sugerido
com atenção antes de aceitá-lo.

Os administradores também podem impor entradas restritivas de `prefix_rule` por meio de
[`requirements.toml`](/pt-BR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

## Entender os campos das regras

`prefix_rule()` aceita os seguintes campos:

- `pattern` **(obrigatório)**: uma lista não vazia que define o prefixo de comando que será usado na correspondência. Cada elemento pode ser:
  - Uma string literal (por exemplo, `"pr"`).
  - Uma união de literais (por exemplo, `["view", "list"]`) para corresponder a alternativas nessa posição da lista de argumentos.
- `decision` **(o padrão é `"allow"`)**: a ação a ser executada quando houver correspondência com a regra. Quando houver correspondência com mais de uma regra, o Codex aplica a decisão mais restritiva (`forbidden` \> `prompt` \> `allow`).
  - `allow`: executa o comando fora do Sandbox sem pedir aprovação.
  - `prompt`: pede aprovação antes de cada invocação correspondente.
  - `forbidden`: bloqueia a solicitação sem pedir aprovação.
- `justification` **(opcional)**: um motivo não vazio e compreensível para a regra. O Codex pode exibi-lo em solicitações de aprovação ou mensagens de rejeição. Ao usar `forbidden`, inclua uma alternativa recomendada na justificativa quando apropriado (por exemplo, `"Use \`rg\` em vez de \`grep\`."\`).
- `match` e `not_match` **(o padrão é `[]`)**: exemplos que o Codex valida ao carregar suas regras. Use-os para detectar erros antes que uma regra entre em vigor.

Quando avalia se deve executar um comando, o Codex compara a lista de argumentos do comando com `pattern`. Internamente, o Codex trata o comando como uma lista de argumentos (como a recebida por `execvp(3)`).

## Wrappers de shell e comandos compostos

Algumas ferramentas encapsulam vários comandos de shell em uma única invocação, por exemplo:

```text
["bash", "-lc", "git add . && rm -rf /"]

Como esse tipo de comando pode ocultar várias ações em uma única string, o Codex trata `bash -lc`, `bash -c` e seus equivalentes em `zsh` / `sh` de forma especial.

### Quando o Codex pode dividir o script com segurança

Se o script de shell for uma sequência linear de comandos formada somente por:

- palavras simples (sem expansão de variáveis e sem `VAR=...`, `$FOO`, `*` etc.)
- unidos por operadores seguros (`&&`, `||`, `;` ou `|`)

então o Codex analisa o script (usando tree-sitter) e o divide em comandos individuais antes de aplicar suas regras.

O script acima é tratado como dois comandos separados:

- `["git", "add", "."]`
- `["rm", "-rf", "/"]`

Em seguida, o Codex avalia cada comando de acordo com suas regras, e o resultado mais restritivo prevalece.

Mesmo que você permita `pattern=["git", "add"]`, o Codex não permitirá automaticamente a execução de `git add . && rm -rf /`, porque o trecho `rm -rf /` é avaliado separadamente e impede que toda a invocação seja permitida automaticamente.

Isso impede que comandos perigosos sejam ocultados entre comandos seguros.

### Quando o Codex não divide o script

Se o script usar recursos de shell mais avançados, como:

- redirecionamento (`>`, `>>`, `<`)
- substituições (`$(...)`, `...`)
- variáveis do ambiente (`FOO=bar`)
- padrões de caracteres curinga (`*`, `?`)
- fluxo de controle (`if`, `for`, `&&` com atribuições etc.)

então o Codex não tenta interpretar nem dividir o script.

Nesses casos, a invocação inteira é tratada como:

```text
["bash", "-lc", "<full script>"]

e suas regras são aplicadas a essa **única** invocação.

Com esse tratamento, cada comando é avaliado separadamente quando isso é seguro; quando não é, o comportamento é conservador.

## Testar um arquivo de regras

Use `codex execpolicy check` para testar como suas regras se aplicam a um comando:

```shell
codex execpolicy check --pretty \
  --rules ~/.codex/rules/default.rules \
  -- gh pr view 7888 --json title,body,comments

O comando gera um JSON que mostra a decisão mais restritiva e todas as regras correspondentes, incluindo os valores de `justification` dessas regras. Use a flag `--rules` mais de uma vez para combinar arquivos e adicione `--pretty` para formatar a saída.

## Entender a linguagem das regras

O formato de arquivo `.rules` usa `Starlark` (consulte a [especificação da linguagem](https://github.com/bazelbuild/starlark/blob/master/spec.md)). A sintaxe é semelhante à do Python, mas foi projetada para ser executada com segurança: o mecanismo de regras pode executá-la sem efeitos colaterais (por exemplo, sem alterar o sistema de arquivos).

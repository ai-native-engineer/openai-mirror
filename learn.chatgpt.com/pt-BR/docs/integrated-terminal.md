<!-- source: https://learn.chatgpt.com/pt-BR/docs/integrated-terminal -->

Cada chat no aplicativo do ChatGPT para desktop inclui um terminal com escopo restrito ao projeto atual ou
à árvore de trabalho. Abra-o pelo ícone do terminal no canto superior direito do aplicativo ou
pressione <kbd>Ctrl</kbd>+<kbd>\`</kbd>.

  
    
  

## Execute e valide seu projeto

Use o terminal para validar alterações, executar scripts e realizar operações do Git
sem alternar entre aplicativos. O ChatGPT pode ler a saída atual do terminal e, assim,
verificar um servidor de desenvolvimento em execução ou consultar uma compilação com falha enquanto trabalha
com você.

Alguns comandos comuns são:

- `git status`
- `git pull --rebase`
- `pnpm test` ou `npm test`
- `pnpm run lint` ou outra verificação específica do projeto

## Crie ações reutilizáveis

Se você executa um comando com frequência, defina uma ação no seu [ambiente local](/pt-BR/codex/environments/local-environment#actions).
As ações aparecem como atalhos no aplicativo do ChatGPT para desktop e são executadas no terminal
integrado.

<kbd>Cmd</kbd>+<kbd>K</kbd> abre a paleta de comandos do aplicativo; essa combinação não limpa o
terminal. Para limpar o terminal, pressione <kbd>Ctrl</kbd>+<kbd>L</kbd>.

<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/qa-your-app-with-computer-use -->

## Introdução

O Uso do computador é uma ótima opção para rodadas de QA, pois consegue visualizar a interface, percorrer fluxos clicando nos controles, preencher campos e registrar as falhas. Isso torna o recurso útil para detectar tanto bugs funcionais quanto problemas de UI em jornadas de usuário realistas.

O essencial é informar ao Codex qual ambiente testar, quais fluxos são mais importantes e que tipo de relatório você quer receber.

## Como usar

1. Instale o [plug-in Uso do computador](/pt-BR/codex/computer-use).
2. Diga ao Codex qual aplicativo, build ou ambiente ele deve testar.
3. Especifique os fluxos ou casos de uso prioritários para você.
4. Peça um relatório estruturado para facilitar a triagem ou o encaminhamento do resultado.

Você pode fazer uma solicitação mais abrangente:

- `@Computer Test my app. Find any major issues and give me a report.`

Ou pode ser mais específico:

- `@Computer Test my app in staging. Cover signup, invite a teammate, and upgrade billing. Log every bug with repro steps, expected result, actual result, and severity.`

Se você já mantém no repositório um arquivo com o plano de testes, anexe-o ao chat ou informe ao Codex onde encontrá-lo para que a rodada de QA siga seus fluxos existentes.

## Dicas práticas

### Detalhe a configuração

Se o estado da conta, os dados de teste, as flags de recurso ou a escolha do ambiente afetarem o fluxo, inclua essas informações logo no início. O Codex produzirá resultados muito melhores se souber se o teste ocorre em um ambiente local, de staging ou semelhante ao de produção.

### Indique os tipos de problema relevantes para você

Especifique se você quer que o Codex se concentre em funcionalidades com falhas, problemas de layout, textos confusos, regressões visuais ou em todos esses pontos.

### Decida se a execução deve parar ou continuar

Se um único problema bloqueador tiver que encerrar a execução, deixe isso claro. Caso contrário, instrua o Codex a percorrer o restante do fluxo e coletar todos os problemas não bloqueadores antes de resumir os resultados.

## Sugestões de acompanhamento

Após a rodada de QA, mantenha o mesmo chat aberto e peça ao Codex para corrigir um dos bugs encontrados, transformar os problemas identificados em rascunhos prontos para uso no Linear ou no GitHub ou concentrar a próxima rodada em um fluxo específico que esteja falhando.

## Prompt sugerido

**Execute uma rodada estruturada de QA**

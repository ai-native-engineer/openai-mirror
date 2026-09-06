<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/agent-friendly-clis -->

## Introdução

Quando o Codex usa repetidamente a mesma API, fonte de logs, caixa de entrada exportada, banco de dados local ou script da equipe, dê a esse trabalho uma interface combinável: um comando que ele possa executar de qualquer pasta e combinar com `git`, `gh`, `rg`, testes e scripts do repositório, e cujos resultados possa inspecionar e refinar.

Adicione uma habilidade complementar que registre quando o Codex deve usar a CLI, o que executar primeiro, como limitar a saída, onde os arquivos baixados são salvos e quais comandos de gravação exigem aprovação.

Nesse fluxo de trabalho, `$cli-creator` ajuda o Codex a criar o comando. `$skill-creator` ajuda o Codex a salvar uma habilidade reutilizável, como `$ci-logs`, que tarefas futuras poderão invocar pelo nome.

## Como usar

1. [Decida se a tarefa precisa de uma CLI](#choose-what-the-cli-should-do)
2. [Compartilhe a fonte que o Codex deve usar como referência](#share-the-docs-files-or-commands)
3. [Execute `$cli-creator`](#ask-codex-to-build-the-cli-and-skill)
4. [Teste o comando instalado](#verify-the-command-works-from-any-folder)
5. [Invoque a habilidade salva mais tarde](#use-the-skill-later)

## Escolha o que a CLI deve fazer

Comece pelo que você quer que o Codex faça, não pela tecnologia em que quer que ele implemente a solução. Uma boa CLI transforma ações recorrentes de leitura, pesquisa, download, exportação, criação de rascunhos, upload, consulta de status ou gravação segura em um comando que o Codex pode executar em qualquer repositório.

| Situação                                              | O que o Codex pode fazer com a CLI                                                                                              |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| **Os logs de CI ficam por trás de uma página de build.**                  | Aceitar uma URL de build, baixar os logs dos jobs que falharam em `./logs` e retornar os caminhos dos arquivos e pequenos trechos.                          |
| **Os tickets de suporte são recebidos em uma exportação semanal.**         | Indexar a exportação CSV ou JSON mais recente, pesquisar por cliente ou frase e ler um ticket pelo ID estável.                        |
| **Uma resposta de API é grande demais para o contexto.**          | Listar apenas os campos de que precisa, ler o objeto completo pelo ID e exportar a resposta inteira para um arquivo.                      |
| **Uma exportação do Slack tem threads longas.**                   | Pesquisar com `--limit`, ler uma thread e retornar o contexto ao redor em vez de todo o arquivo.                             |
| **Um script da equipe executa quatro etapas diferentes.**           | Separar a configuração, a descoberta, o download, a criação de rascunhos, o upload, a consulta de status e a gravação efetiva em comandos distintos.                               |
| **Um plug-in encontra o registro, mas o Codex precisa de um arquivo.** | Manter o plug-in no chat; usar uma CLI para baixar o anexo, o rastreamento, o relatório, o vídeo ou o pacote de logs e retornar o caminho. |

## Compartilhe a documentação, os arquivos ou os comandos

O Codex precisa de algo concreto para usar como referência: documentação ou uma especificação OpenAPI, um comando curl com dados sensíveis removidos, o caminho de uma exportação ou de um banco de dados, uma pasta de logs ou um script existente. Se quiser que a CLI siga um estilo conhecido, cole uma saída curta de `--help` do `gh`, do `kubectl` ou da própria ferramenta da sua equipe.

Se o comando exigir autenticação, informe ao Codex o nome da variável de ambiente, o caminho do arquivo de configuração ou o fluxo de login a que ele deve oferecer suporte. Defina você mesmo o segredo no shell ou no arquivo de configuração. Não cole segredos no chat. Peça ao Codex para fazer a verificação de configuração da CLI falhar de forma clara quando faltarem os dados de autenticação.

## Peça ao Codex para criar a CLI e a habilidade

Use o prompt inicial desta página. Preencha a fonte que o Codex deve usar como referência e a primeira tarefa que a CLI deve realizar.

Antes de o Codex escrever o código, ele deve mostrar a interface de comandos proposta e pedir apenas os detalhes que faltam e sem os quais não seria possível criar a CLI.

## Verifique se o comando funciona em qualquer pasta

O Codex não deve parar depois de executar `cargo run`, `python path/to/script.py` ou um comando de pacote sem instalá-lo. Peça que ele teste o comando instalado em outro repositório ou em uma pasta temporária, da mesma forma como ele será usado em uma tarefa futura.

**Teste a CLI como um agente a usaria no futuro**

Se o Codex retornar um blob JSON enorme, peça que limite a resposta padrão e adicione uma opção de exportação para arquivo dos payloads completos. Se ele esquecer o limite de aprovação, peça que atualize a habilidade complementar antes de usá-la em outra tarefa.

## Use a habilidade mais tarde

Quando precisar da CLI novamente, invoque a habilidade em vez de colar a documentação de novo:

Para trabalhos recorrentes, teste a habilidade uma vez em um chat e depois peça ao Codex para [agendar pelo chat uma tarefa para essa mesma invocação](/pt-BR/codex/automations#schedule-a-task-inside-a-chat).

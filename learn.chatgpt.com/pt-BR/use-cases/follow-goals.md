<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/follow-goals -->

## Introdução

Use `/goal` quando quiser que o Codex continue trabalhando em direção a um único objetivo persistente, em vez de parar após uma interação normal. Isso é útil para trabalhos com um objetivo claro, um ciclo de validação e margem suficiente para o Codex avançar sem que você precise orientar cada etapa. Quando você usa `/goal`, o Codex pode trabalhar de forma independente por várias horas sem precisar da sua intervenção.

Defina uma meta com `/goal <objective>`, consulte a meta atual com `/goal` e use `/goal pause`, `/goal resume` ou `/goal clear` quando precisar controlar a execução.

Se `/goal` não aparecer na lista de comandos de barra, ative `features.goals`
em `config.toml`:

```toml
[features]
goals = true

Você também pode executar `codex features enable goals` pela CLI ou pedir ao Codex para executar esse comando.

## Escolha o trabalho adequado

Uma boa meta é mais abrangente do que um único prompt, mas mais delimitada do que um backlog sem escopo definido. Ela deve especificar o que o Codex deve alcançar, o que não deve alterar, como deve validar o progresso e quando deve parar.

Isso funciona bem para:

- migração de código em que a stack de destino, as verificações de paridade e as restrições estejam claras
- grandes refatorações em que o Codex pode executar testes após cada ponto de controle
- experimentos, jogos ou protótipos em que o Codex pode continuar aprimorando um artefato funcional

Evite usar uma meta para uma lista vaga de tarefas sem relação entre si.

## Configure o ciclo

1. Defina um objetivo e uma condição de parada.
2. Indique ao Codex os arquivos, a documentação, a issue, os logs ou o plano que ele deve ler primeiro.
3. Defina os comandos ou artefatos que comprovam o progresso.
4. Oriente o Codex a trabalhar com pontos de controle e manter um registro breve do progresso.
5. Use `/goal` para verificar o status durante a execução.
6. Pause, retome ou limpe a meta quando a execução for concluída, estiver bloqueada ou mudar de direção.

O mais importante é o contrato. Antes de começar, o Codex deve saber o que caracteriza o trabalho como "concluído". Se a meta for uma migração, "concluído" pode significar que o novo caminho passe nos testes de contrato e que ainda haja uma opção de rollback para o caminho legado. Se a meta for um jogo ou protótipo, "concluído" pode significar que o aplicativo compila, inicia e corresponde à referência fornecida ou ao comportamento esperado.

  Peça ajuda ao Codex: primeiro, converse sobre o que você quer
criar; depois, peça que ele defina uma meta diretamente e comece a trabalhar.

## Deixe o Codex trabalhar de forma independente

Durante a execução de uma meta, peça relatórios concisos de progresso que aumentem a confiança na execução. Uma atualização de status útil informa o ponto de controle atual, o que foi verificado, o que falta e se o Codex está bloqueado.
Se o status ficar vago, torne a meta mais específica em vez de acrescentar mais instruções pontuais. Diga ao Codex exatamente qual é o próximo ponto de controle importante, qual comando o valida e o que deve levá-lo a pausar.

Ao seguir uma meta, o Codex pode trabalhar de forma independente por muitas horas sem que você precise pedir atualizações. Ele interromperá a execução quando estiver confiante de que atingiu a condição de parada. Portanto, considere `/goal` uma tarefa em segundo plano que você não precisa monitorar.

## Exemplos de metas

### Migrações

Seja para migrar jogos para uma nova stack, aplicativos móveis para uma nova plataforma ou uma base de código para um novo framework, você pode usar `/goal` para que o Codex execute a migração:

### Criação de protótipos

Seja para criar do zero um novo aplicativo, um novo jogo ou um novo recurso, você pode usar `/goal` para que o Codex produza uma primeira versão refinada. Você pode usar um arquivo PLAN.md para orientar a criação dessa primeira versão e descrever com precisão o que deseja criar.

### Otimização de prompts

Quando tiver uma suíte de avaliações, você poderá usar `/goal` para otimizar prompts com base nos resultados das avaliações. O Codex pode analisar as falhas, atualizar o prompt, executar novamente as avaliações e continuar iterando até que a pontuação melhore ou sua condição de parada seja atingida.

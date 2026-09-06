<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/macos-telemetry-logs -->

## Adicione um Logger quando a depuração ficar imprecisa

Este caso de uso se destina a fluxos de aplicativos para Mac em que "algo aconteceu" é uma descrição vaga demais para depurar apenas pela revisão de código. Peça ao Codex para adicionar alguns logs unificados de alto valor informativo em torno de um comportamento, executar o aplicativo, acionar esse comportamento e verificar pelo Console ou por `log stream` se os eventos esperados foram disparados.

Use o [plug-in Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) nesse ciclo. Sua habilidade de telemetria do macOS foi criada para ser leve: use o `Logger` da Apple, defina um par claro de subsistema/categoria, registre os limites das ações e as transições de estado, evite payloads sensíveis e verifique o evento depois de uma compilação/execução local, em vez de presumir que a instrumentação está configurada corretamente.

## Por que a telemetria é útil para a engenharia agêntica

Bons logs oferecem ao Codex um ciclo de feedback reproduzível após cada patch. Em vez de pedir que você inspecione manualmente cada janela, ação de menu ou transição de sincronização, o agente pode executar o aplicativo, percorrer o fluxo, inspecionar os logs filtrados e decidir a próxima alteração no código com base nas evidências.

Isso é especialmente útil em três ciclos agênticos:

- **Ciclo de depuração sem intervenção manual:** o Codex instrumenta um fluxo suspeito, inicia o aplicativo, clica na barra lateral ou aciona um comando, lê a sequência de logs gerada, aplica um patch ao fluxo de atualização do estado e executa novamente o mesmo fluxo até que os logs sejam coerentes com o comportamento da interface.
- **Ciclo de coleta da sessão do aplicativo:** o Codex adiciona um evento para cada um destes casos: inicialização do aplicativo, abertura de janela, seleção na barra lateral, início da importação, conclusão da importação e falha na importação. Depois, executa uma sessão local e resume a linha do tempo resultante, deixando evidentes as transições ausentes ou fora de ordem.
- **Ciclo de captura conduzido pelo usuário:** o Codex inicia o aplicativo com o registro de logs ativado, mantém ativo um fluxo de logs específico enquanto você percorre manualmente um fluxo complexo e depois inspeciona a sessão capturada para propor o próximo patch com base nesse rastreamento.

## Mantenha a instrumentação enxuta e fácil de filtrar

Peça ao Codex que use um logger por área de recurso, e não uma linha de log permanente para cada alteração de estado. Categorias de recursos como `Windowing`, `Commands`, `MenuBar`, `Sidebar`, `Sync` ou `Import` facilitam muito a filtragem dos logs na próxima rodada de depuração.

```swift

private let logger = Logger(
  subsystem: Bundle.main.bundleIdentifier ?? "SampleApp",
  category: "Sidebar"
)

@MainActor
func selectItem(_ item: SidebarItem) {
  logger.info("Selected sidebar item: \(item.id, privacy: .public)")
  selection = item.id
}

Use `info` para eventos concisos de ação e de ciclo de vida que continuem úteis ao longo do tempo, e `debug` para detalhes mais ruidosos do estado local que possam ser removidos ou rebaixados antes da conclusão da tarefa. Adicione marcadores apenas quando estiver medindo um intervalo de tempo, não por padrão.

## Peça ao Codex que comprove o evento pelos logs

O mais útil não é apenas adicionar chamadas a `Logger`. Peça ao Codex para executar o aplicativo, acionar o fluxo instrumentado e fornecer o filtro exato do Console ou o predicado de `log stream` usado, além de uma ou duas linhas de log representativas.

```bash
log stream --style compact --predicate 'subsystem == "com.example.app" && category == "Sidebar"'

Se um evento esperado não aparecer, peça ao Codex para reposicionar o log mais perto do fluxo de controle suspeito, executar novamente o mesmo fluxo e continuar iterando até que os logs expliquem o que aconteceu. Se a tarefa se transformar na análise de uma falha ou de um backtrace, passe para o fluxo de trabalho do plug-in para depuração por compilação/execução e mantenha a telemetria focada nos limites das ações.

## Salve um rastreamento da sessão para uma rodada posterior do Codex

Para bugs mais longos ou intermitentes, peça ao Codex para salvar um fluxo de logs específico em um pequeno arquivo local de rastreamento, resumir a linha do tempo e deixar esse artefato no workspace. Assim, uma execução posterior do Codex poderá inspecionar as mesmas evidências sem precisar reproduzir toda a sessão apenas com base na memória. Isso facilita a depuração em várias rodadas quando você quer usar uma execução do agente para coletar um rastreamento e outra para comparar o comportamento antes e depois de um patch.

Isso também funciona bem quando uma pessoa precisa conduzir parte da sessão. Peça ao Codex para iniciar o aplicativo em um ciclo de depuração adequado à coleta de logs, iniciar uma captura filtrada, aguardar enquanto você reproduz o problema manualmente e ler o arquivo de rastreamento salvo quando terminar.

## Dicas práticas

### Instrumente um recurso por vez

Comece com uma barra lateral, janela, comando ou fluxo de sincronização para que a sequência de logs continue fácil de inspecionar. Quando esse fluxo se tornar confiável, o Codex poderá aplicar o mesmo padrão aos fluxos relacionados.

### Inclua a privacidade no prompt

Peça ao Codex para explicar cada identificador incluído nos logs e evitar gravar segredos, dados pessoais ou conteúdo bruto nos logs unificados. Um vocabulário pequeno de eventos geralmente é suficiente para a depuração local.

### Mantenha um exemplo da saída no resumo final

Linhas de log representativas tornam a alteração muito mais confiável do que uma simples afirmação de que "a telemetria foi adicionada". Peça ao Codex para incluir o predicado do filtro e uma breve linha do tempo das ações, para que a próxima execução do agente possa reutilizar o mesmo ciclo de verificação.

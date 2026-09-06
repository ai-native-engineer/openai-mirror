<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/ios-simulator-bug-debugging -->

## Deixe o Codex conduzir todo o ciclo no simulador

Este caso de uso funciona melhor quando o Codex assume a responsabilidade por todo o ciclo: selecionar o target correto do aplicativo, iniciar o aplicativo no simulador, inspecionar a tela atual, executar as etapas de reprodução, coletar logs e capturas de tela, inspecionar um rastreamento de pilha se necessário, corrigir o código e repetir o mesmo fluxo para comprovar que o bug foi resolvido.

Use o [plug-in Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) quando quiser que esse ciclo continue agêntico. O fluxo de trabalho de depuração do iOS usa o XcodeBuildMCP como base, o que permite ao Codex interagir com um simulador já inicializado e coletar as mesmas evidências que uma pessoa normalmente coletaria de forma manual.

Quando o XcodeBuildMCP está configurado com fluxos de trabalho de automação do simulador, automação da interface, depuração e coleta de logs, o Codex pode assumir todo o ciclo de reprodução, depuração e verificação. Se o Codex ainda não tiver selecionado um projeto, um esquema e um simulador, peça que primeiro identifique esses itens e reutilize essa configuração pelo restante da sessão.

## Aproveite os recursos do XcodeBuildMCP

Estes são os grupos de recursos práticos que você deve pedir ao Codex para usar:

- Identificação do projeto e do simulador: verifique se o Codex já sabe qual target do aplicativo e qual simulador usar, localize o projeto ou workspace do Xcode, liste os esquemas, localize ou inicialize um simulador e mantenha essa configuração estável para as próximas etapas de compilação e execução.
- Controle da compilação e inicialização: compile o target ativo do aplicativo, instale e inicie a versão compilada para o simulador, reinicie-a com captura de logs quando necessário e determine o ID do bundle do aplicativo se o Codex precisar inspecionar logs de execução específicos do aplicativo.
- Inspeção e interação com a interface: leia a hierarquia de acessibilidade exibida na tela, faça capturas de tela, toque nos controles, digite nos campos, percorra listas e faça gestos de deslizar a partir das bordas ou outros gestos no simulador.
- Logs e estado do depurador: acompanhe os logs do simulador em tempo real, conecte o LLDB ao aplicativo em execução, defina pontos de interrupção, inspecione frames da pilha e variáveis locais e execute comandos do depurador quando uma falha ou um travamento exigir uma análise mais aprofundada.

O hábito mais importante é pedir ao Codex que inspecione a árvore de visualizações antes de realizar um toque. O XcodeBuildMCP disponibiliza a hierarquia de acessibilidade junto com as coordenadas, para que o Codex possa preferir rótulos estáveis ou IDs de elementos em vez de tentar adivinhar posições absolutas na tela.

## Transforme um bug vago em um script reproduzível

A habilidade de depuração do iOS é mais eficaz quando seu prompt descreve um bug específico e um resultado esperado e, então, deixa que o Codex controle o aplicativo e colete evidências de forma autônoma. Se forem necessários um login, um deep link ou uma fixture de teste, mencione isso uma única vez e peça ao Codex que pause somente se a falta desse item impedir o progresso.

## Dicas práticas

### Peça evidências, não apenas uma correção

Solicite o simulador e o esquema exatos, as capturas de tela, os trechos de logs e os detalhes da pilha que o Codex usou para explicar o bug. Isso torna o patch final muito mais fácil de revisar do que uma resposta como: "Acho que isso deve corrigir o problema."

### Prefira rótulos de acessibilidade a coordenadas

Se o Codex precisar tocar usando coordenadas porque um controle não tem um rótulo estável nem um identificador de acessibilidade, peça que ele deixe isso explícito. Em geral, esse é um sinal de que a correção do bug também deve incluir uma pequena melhoria na testabilidade da interface.

### Trate um bug por execução

Um ciclo de depuração baseado no simulador é poderoso, mas inspira mais confiança quando cada prompt se concentra em um único modo de falha. Peça ao Codex que conclua um ciclo de reprodução, correção e verificação antes de ampliar o escopo para issues relacionadas.

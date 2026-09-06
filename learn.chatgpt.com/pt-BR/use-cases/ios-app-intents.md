<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/ios-app-intents -->

## Torne as partes certas do seu aplicativo visíveis para o sistema

App Intents são uma das formas mais claras de tornar um aplicativo iOS mais útil fora da própria interface. Em vez de tratar seu aplicativo como um destino fechado que só funciona depois que alguém o abre e navega por suas telas, use o Codex para disponibilizar as ações e os objetos que devem estar acessíveis no app Atalhos, na Siri, no Spotlight, em widgets, controles e experiências mais recentes do sistema orientadas por assistentes.

Isso já é útil hoje para facilitar a descoberta e a automação e também é uma preparação importante para um futuro mais orientado por assistentes. Se seu aplicativo já sabe compor, abrir, filtrar, encaminhar ou resumir algo valioso, App Intents oferecem ao sistema uma forma estruturada de solicitar essa capacidade.

## Comece pelas ações e entidades, não por todas as telas

A melhor primeira implementação de App Intents normalmente não consiste em “espelhar o aplicativo inteiro”. Peça ao Codex para identificar:

- as poucas ações que um usuário gostaria de acionar sem percorrer toda a interface
- os objetos do aplicativo que o sistema precisa compreender para encaminhar essas ações corretamente
- os fluxos de trabalho que devem abrir o aplicativo em um estado específico e aqueles que devem ser concluídos diretamente em uma superfície do sistema

As diretrizes de App Intents da Apple oferecem uma boa estrutura para isso: defina a ação, defina a superfície de entidades de que o sistema precisa e, depois, torne essas ações fáceis de descobrir e reutilizar nas experiências do sistema. As referências mais úteis são [Como tornar ações e conteúdo fáceis de descobrir e amplamente disponíveis](https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-and-widely-available), [Como criar seu primeiro intent de aplicativo](https://developer.apple.com/documentation/appintents/creating-your-first-app-intent) e o exemplo de experiências do sistema [Adoção de App Intents para oferecer suporte a experiências do sistema](https://developer.apple.com/documentation/appintents/adopting-app-intents-to-support-system-experiences).

## Pense nas superfícies do sistema, não apenas nos atalhos

A oportunidade vai além de “adicionar um atalho”. Uma boa superfície de App Intents pode tornar seu aplicativo útil em vários lugares:

- Atalhos, onde os usuários podem executar ações diretamente ou combiná-las em automações maiores
- Siri, onde o aplicativo pode disponibilizar verbos significativos e deep links, em vez de apenas abrir de forma genérica
- Spotlight, onde entidades do aplicativo e App Shortcuts se tornam pontos de entrada do sistema fáceis de descobrir
- widgets, Atividades ao Vivo, controles e outras superfícies de interface orientadas por intents
- experiências mais recentes voltadas para assistentes, nas quais o sistema compreende ações e entidades estruturadas com muito mais facilidade do que fluxos de interface arbitrários

## Siga um padrão de aplicativo real

Isso geralmente funciona melhor quando o aplicativo adota uma estrutura como esta:

- um target dedicado a App Intents, em vez de espalhar tipos de intent por arquivos não relacionados do aplicativo
- entradas de `AppShortcutsProvider` para ações de alto valor para o usuário, como compor uma publicação ou abrir o aplicativo em uma aba específica
- tipos `AppEntity` pequenos para objetos que o sistema precisa interpretar, como contas, listas e filtros de linha do tempo
- tratamento de intents com encaminhamento claro de volta à cena principal do aplicativo, para que um intent invocado possa abrir o fluxo de composição correto ou mudar o aplicativo para a aba certa

Esse é o padrão que eu pediria ao Codex que seguisse na maioria dos aplicativos: começar com uma pequena camada de ações voltada para o sistema, manter a superfície de entidades restrita e implementar uma transferência previsível em tempo de execução de volta para o aplicativo quando o intent precisar da interface principal.

## Peça ao Codex para projetar a primeira superfície de intents

O prompt mais eficaz aqui informa ao Codex quais são os objetos centrais e as principais ações dos usuários no seu aplicativo e, em seguida, pede que ele escolha a menor superfície inicial útil de App Intents, em vez de disponibilizar tudo sem critério.

## Dicas práticas

### Exponha os verbos que os usuários realmente querem usar fora do aplicativo

Bons intents iniciais geralmente correspondem a ações como compor, abrir, encontrar, filtrar, iniciar, continuar ou inspecionar. Se uma ação só for útil depois de um longo fluxo de configuração dentro do aplicativo, talvez ela não deva fazer parte da primeira implementação de App Intents.

### Mantenha as entidades mais enxutas do que sua camada de modelos

Em geral, o sistema não precisa do seu modelo de persistência completo. Peça ao Codex para definir a menor superfície de entidades do aplicativo que ainda forneça à Siri, ao app Atalhos e ao Spotlight contexto suficiente para encaminhar e exibir a ação corretamente.

### Encare isso como infraestrutura para assistentes, não apenas como um recurso de atalhos

Mesmo que sua primeira versão só traga melhorias visíveis para o Shortcuts ou a Siri, o ganho mais importante é que seu aplicativo passa a expressar suas funcionalidades por meio de ações e entidades estruturadas. Isso facilita sua participação em futuros pontos de entrada do sistema e orientados por IA, em comparação com um aplicativo cujos recursos estão codificados apenas em toques e hierarquias de visualizações.

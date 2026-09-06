<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/react-native-expo-apps -->

## Comece com o Expo Go

O Expo é uma ótima opção padrão quando você quer que o Codex transforme a ideia de um aplicativo móvel em um
aplicativo React Native testado. O fluxo recomendado é usar `expo start` primeiro, depois o Expo Go
em um dispositivo e, por fim, um cliente de desenvolvimento ou build do EAS somente quando o aplicativo precisar de
código nativo personalizado, distribuição em lojas ou um recurso que o Expo Go não consegue executar.

Isso mantém o Codex focado no fluxo de trabalho do aplicativo, em vez de dedicar a primeira etapa
à configuração de uma IDE nativa e de um simulador, ao provisionamento ou à configuração de builds.

## Use o plug-in do Expo

A Expo publicou um [plug-in do Expo](https://docs.expo.dev/skills/) que fornece ao Codex orientações baseadas nas convenções do Expo para o Expo Router, interfaces com aparência nativa, formulários,
navegação, animações, obtenção de dados, configuração do NativeWind, módulos do Expo, clientes de
desenvolvimento, implantação, atualizações e integração da ação Codex Run.

Use-o quando o Codex estiver criando novas telas no Expo, adicionando pacotes, integrando chamadas
à API, preparando um cliente de desenvolvimento ou deixando um aplicativo pronto para TestFlight, App
Store, Play Store ou EAS Hosting.

Opcionalmente, adicione o [Servidor MCP do Expo](https://docs.expo.dev/eas/ai/mcp/) quando a tarefa exigir consulta à documentação atual
do Expo, instalação de pacotes compatíveis, operações do EAS relacionadas a builds e
fluxos de trabalho, capturas de tela, interação com o simulador, React Native DevTools,
ou dados do TestFlight.

## Processo de iteração

1. Peça ao Codex para inspecionar o repositório e confirmar se é um novo aplicativo Expo ou um
projeto Expo existente.
2. Comece pelo Expo Router e pelo Expo Go e use `npx expo install` ao adicionar
   pacotes do Expo.
3. Peça ao Codex para implementar um fluxo de trabalho completo com navegação que pareça nativa,
estados de carregamento, estados vazios e estados de erro.
4. Faça a verificação da forma mais rápida disponível, como usando o Expo Go em um dispositivo ou em um
simulador; depois, passe para um cliente de desenvolvimento ou para o EAS somente quando necessário.

## Prompt de acompanhamento sugerido

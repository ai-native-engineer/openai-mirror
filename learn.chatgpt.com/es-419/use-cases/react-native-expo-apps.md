<!-- source: https://learn.chatgpt.com/es-419/use-cases/react-native-expo-apps -->

## Comienza con Expo Go

Expo es una opción inicial sólida cuando quieres que Codex convierta una idea para una app móvil en una
app de React Native probada. El ciclo más práctico consiste en usar `expo start` primero, luego Expo Go
en un dispositivo y, por último, un cliente de desarrollo o una compilación de EAS, pero solo cuando la app necesite
código nativo personalizado, distribución en tiendas o una funcionalidad que no se pueda ejecutar en Expo Go.

Esto permite que Codex se concentre en el flujo de trabajo de la app en lugar de dedicar la primera iteración
a preparar el IDE nativo y el simulador, gestionar el aprovisionamiento o configurar la compilación.

## Usa el complemento de Expo

Expo publicó un [complemento de Expo](https://docs.expo.dev/skills/) que brinda a Codex orientación conforme a las convenciones de Expo sobre Expo Router, interfaces nativas, formularios,
navegación, animaciones, obtención de datos, configuración de NativeWind, módulos de Expo, clientes
de desarrollo, despliegue, actualizaciones e integración de la acción Codex Run.

Úsalo cuando Codex cree nuevas pantallas de Expo, agregue paquetes, integre llamadas a la API,
prepare un cliente de desarrollo o deje una app lista para TestFlight, App
Store, Play Store o EAS Hosting.

De forma opcional, agrega el [Servidor MCP de Expo](https://docs.expo.dev/eas/ai/mcp/) cuando la tarea requiera consultar la documentación actualizada
de Expo, instalar paquetes compatibles, realizar compilaciones de EAS y
operaciones de flujos de trabajo, tomar capturas de pantalla, interactuar con el simulador, usar React Native DevTools
o consultar datos de TestFlight.

## Proceso de iteración

1. Pídele a Codex que inspeccione el repositorio y confirme si se trata de una app nueva de Expo o de un
proyecto existente de Expo.
2. Comienza con Expo Router y Expo Go, y usa `npx expo install` cuando agregues
   paquetes de Expo.
3. Pídele a Codex que cree un flujo de trabajo completo con navegación de apariencia nativa,
estados de carga, estados vacíos y estados de error.
4. Realiza la verificación por la vía más rápida disponible, como Expo Go en un dispositivo o un
simulador, y pasa a un cliente de desarrollo o a EAS solo cuando sea necesario.

## Prompt de seguimiento sugerido

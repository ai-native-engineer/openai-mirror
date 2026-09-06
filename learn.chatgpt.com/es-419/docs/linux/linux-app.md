<!-- source: https://learn.chatgpt.com/es-419/docs/linux/linux-app -->

La aplicación de escritorio de ChatGPT para Linux está disponible en versión preliminar. Instala el paquete
correspondiente a tu distribución de Linux y a la arquitectura de tu procesador, y luego inicia sesión con tu
cuenta de ChatGPT para trabajar con proyectos, archivos locales y Codex.

## Distribuciones y arquitecturas compatibles

La versión preliminar es compatible con las versiones de escritorio de estas distribuciones de Linux:

- Ubuntu 24.04 LTS y 26.04 LTS
- Debian 13
- Fedora 43 y 44

Cada distribución compatible tiene paquetes para procesadores x64 y ARM64. Para comprobar
la arquitectura de tu procesador, ejecuta:

```bash
uname -m

El resultado `x86_64` identifica un procesador x64. El resultado `aarch64` o
`arm64` identifica un procesador ARM64.

## Descarga el paquete adecuado

Elige `.deb` para Ubuntu o Debian, y `.rpm` para Fedora:

| Distribución     | Arquitectura | Descarga                                                                                                          |
| ---------------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| Ubuntu o Debian | x64          | [Descarga `.deb` para x64](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_amd64.deb)     |
| Ubuntu o Debian | ARM64        | [Descarga `.deb` para ARM64](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_arm64.deb)   |
| Fedora           | x64          | [Descarga `.rpm` para x64](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.x86_64.rpm)    |
| Fedora           | ARM64        | [Descarga `.rpm` para ARM64](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.aarch64.rpm) |

## Instala en Ubuntu o Debian

Descarga el paquete `.deb` correspondiente a la arquitectura de tu procesador. Luego, abre una
terminal, cambia al directorio que contiene el paquete e instálalo con
`apt`:

```bash
cd ~/Downloads
sudo apt install ./chatgpt_amd64.deb

Para ARM64, reemplaza `chatgpt_amd64.deb` por `chatgpt_arm64.deb`.

Abre **ChatGPT** desde el menú de aplicaciones o ejecuta `chatgpt` en una terminal.
Inicia sesión con tu cuenta de ChatGPT y sigue el
[inicio rápido de la app de escritorio](/es-419/codex/quickstart?setup=app).

## Instala en Fedora

Descarga el paquete `.rpm` correspondiente a la arquitectura de tu procesador. Luego, abre una
terminal, cambia al directorio que contiene el paquete e instálalo con
`dnf`:

```bash
cd ~/Downloads
sudo dnf install ./chatgpt.x86_64.rpm

Para ARM64, reemplaza `chatgpt.x86_64.rpm` por `chatgpt.aarch64.rpm`.

Abre **ChatGPT** desde el menú de aplicaciones o ejecuta `chatgpt` en una terminal.
Inicia sesión con tu cuenta de ChatGPT y sigue el
[inicio rápido de la app de escritorio](/es-419/codex/quickstart?setup=app).

## Actualiza la app

Durante la instalación, el paquete configura el repositorio firmado de paquetes de OpenAI.
Usa el gestor de paquetes de tu distribución para instalar actualizaciones posteriores.

En Ubuntu o Debian, ejecuta:

```bash
sudo apt update
sudo apt install --only-upgrade chatgpt

En Fedora, ejecuta:

```bash
sudo dnf upgrade --refresh chatgpt

## Compatibilidad y limitaciones

La versión preliminar es compatible con las distribuciones de escritorio enumeradas en
[Distribuciones y arquitecturas compatibles](#supported-distributions-and-architectures).
Otras distribuciones de Linux pueden funcionar, pero no son oficialmente compatibles.

Algunas funciones tienen requisitos específicos de plataforma. Por ejemplo,
[Uso de la computadora](/es-419/codex/computer-use) está disponible en macOS y Windows, pero todavía no
en la versión preliminar para Linux. Una versión futura agregará compatibilidad con Linux.

## Compatibilidad con Wayland

La compatibilidad nativa con Wayland es experimental y seguirá mejorando. En una sesión de
Wayland, la app usa XWayland cuando está disponible. Para seleccionar explícitamente Wayland
nativo, cierra la app por completo y ábrela desde una terminal:

```bash
chatgpt --ozone-platform=wayland

Algunas funciones, como las ventanas flotantes, el posicionamiento de ventanas, el foco y los
atajos de teclado, podrían no funcionar por completo mientras se consolida la compatibilidad nativa con Wayland.

## Próximos pasos

- Sigue el [inicio rápido de la app de escritorio](/es-419/codex/quickstart?setup=app).
- Configura la [Extensión de Chrome](/es-419/codex/chrome-extension) para integrarla con el navegador.
- Revisa los [permisos](/es-419/codex/permissions) para los proyectos y comandos locales.

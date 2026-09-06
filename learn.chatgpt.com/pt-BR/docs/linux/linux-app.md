<!-- source: https://learn.chatgpt.com/pt-BR/docs/linux/linux-app -->

O aplicativo do ChatGPT para desktop no Linux está disponível em versão prévia. Instale o pacote
correspondente à sua distribuição Linux e à arquitetura do seu processador. Depois, faça login na sua
conta do ChatGPT para trabalhar com projetos, arquivos locais e o Codex.

## Distribuições e arquiteturas compatíveis

A versão prévia é compatível com as versões para desktop destas distribuições Linux:

- Ubuntu 24.04 LTS e 26.04 LTS
- Debian 13
- Fedora 43 e 44

Cada distribuição compatível oferece pacotes para processadores x64 e ARM64. Para verificar
a arquitetura do seu processador, execute:

```bash
uname -m

A saída `x86_64` identifica um processador x64. A saída `aarch64` ou
`arm64` identifica um processador ARM64.

## Baixe o pacote correto

Escolha `.deb` para Ubuntu ou Debian e `.rpm` para Fedora:

| Distribuição     | Arquitetura | Download                                                                                                          |
| ---------------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| Ubuntu ou Debian | x64          | [Baixar `.deb` para x64](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_amd64.deb)     |
| Ubuntu ou Debian | ARM64        | [Baixar `.deb` para ARM64](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_arm64.deb)   |
| Fedora           | x64          | [Baixar `.rpm` para x64](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.x86_64.rpm)    |
| Fedora           | ARM64        | [Baixar `.rpm` para ARM64](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.aarch64.rpm) |

## Instale no Ubuntu ou Debian

Baixe o pacote `.deb` correspondente à arquitetura do seu processador. Em seguida, abra um
terminal, acesse o diretório que contém o pacote e instale-o com
`apt`:

```bash
cd ~/Downloads
sudo apt install ./chatgpt_amd64.deb

Para ARM64, substitua `chatgpt_amd64.deb` por `chatgpt_arm64.deb`.

Abra o **ChatGPT** no menu de aplicativos ou execute `chatgpt` em um terminal.
Faça login com sua conta do ChatGPT e siga o
[guia de início rápido do aplicativo para desktop](/pt-BR/codex/quickstart?setup=app).

## Instale no Fedora

Baixe o pacote `.rpm` correspondente à arquitetura do seu processador. Em seguida, abra um
terminal, acesse o diretório que contém o pacote e instale-o com
`dnf`:

```bash
cd ~/Downloads
sudo dnf install ./chatgpt.x86_64.rpm

Para ARM64, substitua `chatgpt.x86_64.rpm` por `chatgpt.aarch64.rpm`.

Abra o **ChatGPT** no menu de aplicativos ou execute `chatgpt` em um terminal.
Faça login com sua conta do ChatGPT e siga o
[guia de início rápido do aplicativo para desktop](/pt-BR/codex/quickstart?setup=app).

## Atualize o aplicativo

O pacote configura o repositório de pacotes assinados da OpenAI durante a instalação.
Use o gerenciador de pacotes da sua distribuição para instalar atualizações posteriores.

No Ubuntu ou Debian, execute:

```bash
sudo apt update
sudo apt install --only-upgrade chatgpt

No Fedora, execute:

```bash
sudo dnf upgrade --refresh chatgpt

## Compatibilidade e limitações

A versão prévia é compatível com as distribuições para desktop listadas em
[Distribuições e arquiteturas compatíveis](#supported-distributions-and-architectures).
Outras distribuições Linux podem funcionar, mas não são oficialmente compatíveis.

Alguns recursos têm requisitos específicos de plataforma. Por exemplo,
o [Uso do computador](/pt-BR/codex/computer-use) está disponível no macOS e no Windows, mas ainda não
na versão prévia para Linux. Uma versão futura adicionará suporte ao Linux.

## Suporte ao Wayland

O suporte nativo ao Wayland é experimental e continuará sendo aprimorado. Em uma sessão do Wayland,
o aplicativo usa XWayland quando disponível. Para selecionar explicitamente o Wayland
nativo, feche completamente o aplicativo e inicie-o em um terminal:

```bash
chatgpt --ozone-platform=wayland

Alguns recursos, como janelas flutuantes, posicionamento de janelas, foco e atalhos
de teclado, podem não funcionar completamente enquanto o suporte nativo ao Wayland amadurece.

## Próximos passos

- Siga o [guia de início rápido do aplicativo para desktop](/pt-BR/codex/quickstart?setup=app).
- Configure a [Extensão do Chrome](/pt-BR/codex/chrome-extension) para integração com o navegador.
- Revise as [permissões](/pt-BR/codex/permissions) para projetos locais e comandos.

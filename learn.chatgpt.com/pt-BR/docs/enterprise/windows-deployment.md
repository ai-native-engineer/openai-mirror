<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/windows-deployment -->

Os usuários podem instalar o aplicativo para desktop do ChatGPT por conta própria, ou sua equipe de TI pode
implantá-lo com uma ferramenta de gerenciamento empresarial. O aplicativo é assinado pela Store, mas
os usuários não precisam abrir a Microsoft Store para instalá-lo ou atualizá-lo.

## Permitir que os usuários instalem e atualizem o aplicativo

Se os usuários puderem gerenciar os próprios aplicativos, encaminhe-os ao
[instalador Web](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi).
O instalador oferece a experiência padrão de instalação e atualização
automática. Componentes da Microsoft Store podem aparecer durante a instalação ou
as atualizações, mas os usuários não precisam acessar a Store por conta própria.

Também é possível instalar o aplicativo pela linha de comando:

```powershell
winget install --id 9PLM9XGG6VKS -s msstore

## Implantar o aplicativo com uma ferramenta de gerenciamento empresarial

Se sua organização gerencia software de forma centralizada, use o Microsoft Intune ou
outra plataforma compatível de gerenciamento de dispositivos móveis (MDM) ou de implantação
de software. Se sua plataforma oferecer suporte à implantação de aplicativos da Microsoft Store, procure
ChatGPT from OpenAI no fluxo de aplicativos da Store ou use este ID de produto da Store:

```text
9PLM9XGG6VKS

Para ver detalhes da configuração, consulte a seguinte documentação da Microsoft:

- [Guia de implantação para empresas](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDVdo5pE5P3QKg5r0eieSvfAeE7cW0yy58ncBFW7OYajwU?e=dGH94F)
- [Guia de implantação do Intune](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDh_5o31T6XT7bUn5RPldEJAZX58gEuRr8YnJD7d2IMpec?e=nByKw6)
- [Guia de implantação do MECM](https://1drv.ms/b/c/123ec1ed6c72a14a/IQB829f_TSbkR7-H9qA4Q9ntAa9D2He3qMjXksWi2ozdeg8?e=GTKgAl)
- [Adicionar aplicativos da Microsoft Store ao Microsoft Intune](https://learn.microsoft.com/en-us/intune/app-management/deployment/add-microsoft-store)

<a id="manage-in-app-updates"></a>

### Gerenciar atualizações do aplicativo

Para ver instruções de configuração e orientações de distribuição, consulte
[Gerenciar atualizações do aplicativo](/pt-BR/codex/enterprise/manage-app-updates).

## Instalar sem os serviços de distribuição da Microsoft

Se o seu ambiente não puder usar os serviços de distribuição de aplicativos da Microsoft para a
instalação inicial, baixe o pacote MSIX assinado pela Store correspondente a cada arquitetura de
dispositivo:

| Arquitetura do dispositivo | Pacote                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------- |
| x64                 | [ChatGPT-x64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-x64.msix)     |
| Arm64               | [ChatGPT-arm64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-arm64.msix) |

Estes links estáveis apontam para o pacote assinado pela Store publicado mais recentemente para cada
arquitetura. Em fluxos de trabalho de implantação offline que exigem um arquivo de licença,
baixe também a
[licença offline (`ChatGPT-License.xml`)](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-License.xml).
Importe o MSIX correspondente e, quando necessário, o arquivo de licença para seu MDM
ou sua plataforma de implantação de software.

Após a instalação inicial, os dispositivos que conseguem acessar
`persistent.oaistatic.com` podem instalar atualizações automaticamente, a menos que a configuração
gerenciada desative o mecanismo de atualização integrado do aplicativo. Se você desativar as atualizações
pelo próprio aplicativo, implante pacotes mais recentes por meio do seu MDM ou da sua ferramenta de implantação de software.

Este método de implantação:

- Permite a instalação inicial em ambientes restritos.
- É compatível com dispositivos x64 e Arm64.
- Não disponibiliza um MSI independente nem um EXE externo à Store.

## Recursos relacionados

- [Gerenciar atualizações do aplicativo](/pt-BR/codex/enterprise/manage-app-updates)
- [Aplicativo para desktop do ChatGPT no Windows](/pt-BR/codex/app/windows)

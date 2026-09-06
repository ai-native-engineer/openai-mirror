<!-- source: https://learn.chatgpt.com/pt-BR/docs/auth -->

## Autenticação da OpenAI

<a id="sign-in-with-chatgpt"></a>

O Codex oferece duas formas de login ao usar modelos da OpenAI:

- Entrar com o ChatGPT para ter acesso pela assinatura
- Entrar com uma chave de API para ter acesso com cobrança por uso

O aplicativo do ChatGPT para desktop, a Codex CLI e a extensão para IDE oferecem suporte aos dois métodos de login
para trabalho local. O Codex Cloud exige que você entre com o ChatGPT.

O método de login também determina quais controles administrativos e políticas de tratamento de dados se aplicam.

- Ao entrar com o ChatGPT, o uso do Codex segue as permissões do seu workspace
do ChatGPT, o controle de acesso baseado em funções (RBAC) e as configurações
de retenção e residência de dados do ChatGPT Enterprise.
- Já com uma chave de API, o uso segue as configurações de retenção e
de compartilhamento de dados da sua organização da API.

Em workspaces gerenciados, a autenticação é apenas uma camada de acesso. A associação ao workspace
e o provisionamento determinam quem pode entrar, enquanto as licenças e
as funções no workspace determinam quais interfaces e recursos do produto podem ser usados.
Para o trabalho local no aplicativo do ChatGPT para desktop, na Codex CLI ou na extensão para IDE,
os perfis de permissão limitam o que o agente pode fazer no dispositivo. Consulte
[Grupos e provisionamento](/pt-BR/codex/enterprise/groups-and-provisioning)
e [Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions)
para planejar esses controles.

### Entrar com o ChatGPT

Ao entrar com o ChatGPT pelo aplicativo do ChatGPT para desktop, pela Codex CLI ou pela extensão para IDE, o fluxo de login abre uma janela do navegador. Depois que você entra, o navegador repassa suas credenciais ao Codex.

### ChatGPT na Web

Abra o [ChatGPT](https://chatgpt.com), entre e escolha o workspace em que deseja
trabalhar. O ChatGPT na Web mantém a sessão autenticada no navegador.

#### Aplicativo do ChatGPT para desktop

Na tela de login, selecione **Continuar para entrar** e conclua o
fluxo no navegador.

#### Codex CLI

Execute `codex login` e conclua o fluxo no navegador. Esse é o método padrão de
autenticação quando não há uma sessão válida disponível.

#### Extensão para IDE

Na tela de login, selecione **Entrar com o ChatGPT** e conclua o
fluxo no navegador.

<a id="sign-in-with-an-api-key"></a>

### Entrar com uma chave de API

Você também pode entrar no aplicativo do ChatGPT para desktop, na Codex CLI ou na extensão para IDE com uma chave de API. Obtenha sua chave de API no [painel da OpenAI](https://platform.openai.com/api-keys).

#### Aplicativo do ChatGPT para desktop

Na tela de login, selecione **Entrar de outra forma**, informe sua chave e
selecione **Continuar**.

#### Codex CLI

Envie a chave para `codex login` via stdin:

```shell
printenv OPENAI_API_KEY | codex login --with-api-key

#### Extensão para IDE

Na tela de login, selecione **Usar chave de API**, informe sua chave e selecione
**OK**.

A OpenAI cobra o uso da chave de API pela sua conta da plataforma da OpenAI, de acordo com os preços padrão da API. Consulte a [página de preços da API](https://openai.com/api/pricing/).

A autenticação por chave de API oferece suporte a fluxos de trabalho locais do Codex, mas alguns recursos que
dependem do acesso ao workspace do ChatGPT ou de serviços de nuvem são limitados ou indisponíveis.
Compare a disponibilidade por plano em
[Disponibilidade de recursos](/pt-BR/codex/pricing#feature-availability).

Na Codex CLI e no Codex do aplicativo do ChatGPT para desktop, a autenticação por chave de API
inclui acesso aos plug-ins compatíveis selecionados pela OpenAI. Alguns plug-ins não estão
disponíveis porque seus fluxos de conexão exigem recursos OAuth sem
suporte. Consulte [Usar plug-ins](/pt-BR/codex/plugins#api-key-availability).

Ao entrar com uma chave de API, o Codex usa os preços padrão da API em vez dos
créditos incluídos no plano do ChatGPT.

Use a autenticação por chave de API em fluxos de trabalho programáticos da Codex CLI, como tarefas de CI/CD.
Não exponha a execução do Codex em ambientes não confiáveis ou públicos.

### Verificar a autenticação ou sair

Abra o menu do perfil para confirmar a conta e o workspace ativos. Para encerrar a
sessão do ChatGPT na Web nesse navegador, selecione **Sair**.

Abra o menu do perfil para ver a conta ativa ou o status da chave de API. Selecione
**Sair** para remover as credenciais atuais.

Execute `codex login status` para ver o método de autenticação ativo. Para autenticação
armazenada, execute `codex logout` para remover as credenciais atuais. Quando
o processo seleciona a identidade de carga de trabalho, o Codex rejeita `codex login` e
`codex logout`, pois o ambiente do processo controla a autenticação.

Abra o menu do perfil para ver a conta ativa ou o status da chave de API. Selecione
**Sair** para remover as credenciais atuais.

### Usar tokens de acesso do Codex para automação empresarial

Nos workspaces do ChatGPT Enterprise, os administradores podem conceder a permissão de token de acesso
para que membros autorizados criem tokens de acesso do Codex para fluxos de trabalho locais confiáveis
e não interativos do Codex. Use um token de acesso quando a automação
precisar de acesso ao workspace do ChatGPT, dos direitos de uso do Codex gerenciados pelo ChatGPT ou
dos controles do workspace empresarial sem login pelo navegador.

Os tokens de acesso se destinam a scripts confiáveis, agendadores e executores privados de CI.
Para chamadas gerais à API da OpenAI, continue usando chaves de API da plataforma.

Para ver as etapas de configuração e orientações sobre permissões, rotação e revogação, consulte
[Tokens de acesso](/pt-BR/codex/enterprise/access-tokens).

Se sua plataforma de nuvem, seu sistema de CI ou seu cluster já emite tokens de
carga de trabalho de curta duração, use a
[federação de identidade de carga de trabalho](/pt-BR/codex/enterprise/workload-identity)
em vez de armazenar uma credencial da OpenAI.

Se seu ambiente já fornece um token de acesso do Codex, redirecione-o para a CLI:

```shell
printenv CODEX_ACCESS_TOKEN | codex login --with-access-token

## Proteger sua conta do Codex Cloud

O Codex Cloud interage diretamente com sua base de código e, por isso, exige mais segurança do que muitos outros recursos do ChatGPT. Ative a autenticação multifator (MFA).

Se você usa um provedor de login social (Google, Microsoft ou Apple), não é obrigatório ativar a MFA na sua conta do ChatGPT, mas você pode configurá-la no seu provedor de login social.

Para ver as instruções de configuração, consulte:

- [Google](https://support.google.com/accounts/answer/185839)
- [Microsoft](https://support.microsoft.com/en-us/topic/what-is-multifactor-authentication-e5e39437-121c-be60-d123-eda06bddf661)
- [Apple](https://support.apple.com/en-us/102660)

Se você acessa o ChatGPT por login único (SSO), o administrador de SSO da sua organização deve exigir MFA para todos os usuários.

Se você entra usando e-mail e senha, precisa configurar a MFA na sua conta antes de acessar o Codex Cloud.

Se sua conta oferece mais de um método de login e um deles usa e-mail e senha, você precisa configurar a MFA antes de acessar o Codex, mesmo que entre de outra forma.

<a id="login-caching"></a>

## Cache de login

Quando você entra no aplicativo do ChatGPT para desktop, na Codex CLI ou na extensão para IDE usando o ChatGPT ou uma chave de API, seus dados de login são armazenados em cache e reutilizados. A CLI e a extensão compartilham os mesmos dados de login em cache. Se você sair de qualquer uma delas, precisará entrar novamente na próxima vez que iniciar a CLI ou a extensão.

O Codex armazena os dados de login localmente em um arquivo de texto simples no caminho `~/.codex/auth.json` ou no armazenamento de credenciais específico do sistema operacional.

Nas sessões iniciadas com o ChatGPT, o Codex renova os tokens automaticamente durante o uso, antes que expirem. Por isso, as sessões ativas normalmente continuam sem exigir outro login pelo navegador.

<a id="credential-storage"></a>
<a id="enforce-a-login-method-or-workspace"></a>

## Armazenamento de credenciais

Use `cli_auth_credentials_store` para controlar onde a Codex CLI armazena as credenciais em cache:

```toml
# file | keyring | auto
cli_auth_credentials_store = "keyring"

- `file` armazena as credenciais em `auth.json`, no diretório `CODEX_HOME` (o padrão é `~/.codex`).
- `keyring` armazena as credenciais no armazenamento de credenciais do sistema operacional.
- `auto` usa o armazenamento de credenciais do sistema operacional quando disponível; caso contrário, recorre a `auth.json`.

Consulte a [referência de configuração](/pt-BR/codex/config-file/config-reference) para obter o esquema completo de
`config.toml`.

  Se você usar o armazenamento baseado em arquivo, trate `~/.codex/auth.json` como uma senha: ele
  contém tokens de acesso. Não faça commit dele, não o cole em tickets nem o compartilhe no
  chat.

## Exigir um método de login ou um workspace

Em ambientes gerenciados, os administradores podem restringir como os usuários podem se autenticar:

```toml
# Only allow ChatGPT login or only allow API key login.
forced_login_method = "chatgpt" # or "api"

# When using ChatGPT login, restrict users to a specific workspace.
forced_chatgpt_workspace_id = "00000000-0000-0000-0000-000000000000"

Se as credenciais ativas não corresponderem às restrições configuradas, o Codex encerra a sessão do usuário e finaliza a execução.

Em geral, essas configurações são aplicadas por meio da configuração gerenciada, em vez de serem definidas individualmente para cada usuário. Consulte [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration).

## Diagnóstico de login

As execuções diretas de `codex login` gravam um arquivo dedicado, `codex-login.log`, no
diretório de logs configurado. Use-o para depurar falhas de login pelo navegador ou
por código do dispositivo, ou quando o suporte solicitar logs específicos de login.

## Pacotes de CA personalizados

Se sua rede usa um proxy TLS corporativo ou uma CA raiz privada, defina
`CODEX_CA_CERTIFICATE` como um pacote PEM antes de fazer login. Quando
a variável `CODEX_CA_CERTIFICATE` não está definida, o Codex usa `SSL_CERT_FILE` como alternativa. As mesmas
configurações personalizadas de CA se aplicam ao login, às solicitações HTTPS normais e às conexões WebSocket
seguras.

```shell

codex login

## Login em dispositivos sem interface gráfica

Se você estiver entrando no ChatGPT com a Codex CLI, a interface de login pelo navegador poderá não funcionar em algumas situações:

- Você está executando a CLI em um ambiente remoto ou sem interface gráfica.
- Sua configuração de rede local bloqueia o callback de localhost que o Codex usa para retornar o token OAuth à CLI após o login.

Nessas situações, prefira a autenticação por código do dispositivo (beta). Na interface interativa de login, escolha **Entrar com código do dispositivo** ou execute `codex login --device-auth` diretamente. Se a autenticação por código do dispositivo não funcionar no seu ambiente, use um dos métodos alternativos.

### Preferencial: autenticação por código do dispositivo (beta)

1. Ative o login por código do dispositivo nas configurações de segurança do ChatGPT (conta pessoal) ou nas permissões do workspace do ChatGPT (administrador do workspace).
2. No terminal em que você está executando o Codex, escolha uma destas opções:
   - Na interface interativa de login, selecione **Entrar com código do dispositivo**.
   - Execute `codex login --device-auth`.
3. Abra o link no navegador, entre e insira o código de uso único.

Se o login por código do dispositivo não estiver disponível no seu ambiente, use um dos
métodos alternativos abaixo.

### Alternativa: autenticar-se localmente e copiar o cache de autenticação

Se você conseguir concluir o fluxo de login em uma máquina com navegador, poderá copiar as credenciais em cache para a máquina sem interface gráfica.

1. Em uma máquina em que você possa usar o fluxo de login pelo navegador, execute `codex login`.
2. Confirme se o cache de login existe em `~/.codex/auth.json`.
3. Copie `~/.codex/auth.json` para `~/.codex/auth.json` na máquina sem interface gráfica.

Trate `~/.codex/auth.json` como uma senha: o arquivo contém tokens de acesso. Não faça commit dele, não o cole em tickets nem o compartilhe no chat.

Se o sistema operacional guardar as credenciais em um armazenamento de credenciais, em vez de `~/.codex/auth.json`, talvez este método não se aplique. Consulte
[Armazenamento de credenciais](/pt-BR/codex/auth#credential-storage) para saber como configurar o armazenamento baseado em arquivo.

Copie para uma máquina remota via SSH:

```shell
ssh user@remote 'mkdir -p ~/.codex'
scp ~/.codex/auth.json user@remote:~/.codex/auth.json

Ou use um comando de uma linha que dispensa `scp`:

```shell
ssh user@remote 'mkdir -p ~/.codex && cat > ~/.codex/auth.json' < ~/.codex/auth.json

Copie para um contêiner Docker:

```shell
# Replace MY_CONTAINER with the name or ID of your container.
CONTAINER_HOME=$(docker exec MY_CONTAINER printenv HOME)
docker exec MY_CONTAINER mkdir -p "$CONTAINER_HOME/.codex"
docker cp ~/.codex/auth.json MY_CONTAINER:"$CONTAINER_HOME/.codex/auth.json"

Para conhecer uma versão mais avançada desse mesmo padrão em executores confiáveis de CI/CD, consulte
[Manter a autenticação da conta do Codex em CI/CD (avançado)](/codex/auth/ci-cd-auth).
Esse guia explica como permitir que o Codex atualize `auth.json` durante execuções normais e
mantenha o arquivo atualizado para o próximo job. As chaves de API continuam sendo a opção padrão
recomendada para automação.

### Alternativa: encaminhar o callback de localhost por SSH

Se você puder encaminhar portas entre a máquina local e o host remoto, poderá usar o fluxo padrão pelo navegador criando um túnel para o servidor local de callback do Codex (por padrão, `localhost:1455`).

1. Na sua máquina local, inicie o encaminhamento de portas:

```shell
ssh -L 1455:localhost:1455 user@remote

2. Nessa sessão SSH, execute `codex login` e, na máquina local, acesse o endereço exibido.

## Provedores alternativos de modelos

Ao definir um [provedor de modelos personalizado](/pt-BR/codex/config-file/config-advanced#custom-model-providers) no arquivo de configuração, você pode escolher um destes métodos de autenticação:

- **Autenticação da OpenAI**: defina `requires_openai_auth = true` para usar a autenticação da OpenAI. Assim, você poderá entrar com o ChatGPT ou uma chave de API. Isso é útil ao acessar modelos da OpenAI por meio de um servidor proxy de LLM. Quando `requires_openai_auth = true`, o Codex ignora `env_key`.
- **Autenticação por variável de ambiente**: defina `env_key = "<ENV_VARIABLE_NAME>"` para usar uma chave de API específica do provedor obtida da variável de ambiente local chamada `<ENV_VARIABLE_NAME>`.
- **Sem autenticação**: se você não definir `requires_openai_auth` (ou definir seu valor como `false`) nem definir `env_key`, o Codex pressupõe que o provedor não exige autenticação. Isso é útil para modelos locais.

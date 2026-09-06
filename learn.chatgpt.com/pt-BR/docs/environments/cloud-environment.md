<!-- source: https://learn.chatgpt.com/pt-BR/docs/environments/cloud-environment -->

Use ambientes para controlar o que o Codex instala e executa durante os chats na nuvem. Por exemplo, você pode adicionar dependências, instalar ferramentas como linters e formatadores e definir variáveis do ambiente.

Configure os ambientes nas [configurações do Codex](https://chatgpt.com/codex/settings/environments).

<a id="how-codex-cloud-tasks-run"></a>

## Como funcionam os chats do Codex na nuvem

Ao enviar um prompt, acontece o seguinte:

1. O Codex cria um contêiner e faz checkout do seu repositório na branch selecionada ou no SHA do commit selecionado.
2. O Codex executa seu script de configuração e também um script de manutenção opcional quando um contêiner em cache é retomado.
3. O Codex aplica suas configurações de acesso à internet. Os scripts de configuração são executados com acesso à internet. O acesso do agente à internet fica desativado por padrão, mas você pode habilitar o acesso limitado ou irrestrito se necessário. Consulte [acesso do agente à internet](/pt-BR/codex/cloud/internet-access).
4. O agente executa comandos de terminal em loop. Ele edita o código, executa verificações e tenta validar o próprio trabalho. Se o repositório incluir `AGENTS.md`, o agente usa esse arquivo para encontrar comandos de lint e teste específicos do projeto.
5. Ao terminar, o agente mostra a resposta e um diff dos arquivos que alterou. Você pode abrir um PR ou fazer perguntas de acompanhamento.

## Imagem universal padrão

O agente do Codex é executado em uma imagem de contêiner padrão chamada `universal`, que vem com linguagens, pacotes e ferramentas comuns pré-instalados.

Nas configurações do ambiente, selecione **Definir versões de pacotes** para fixar as versões do Python, do Node.js e de outros ambientes de execução.

  Para ver detalhes do que está instalado, consulte
[openai/codex-universal](https://github.com/openai/codex-universal), que contém um
  Dockerfile de referência e uma imagem que pode ser baixada e testada localmente.

Embora `codex-universal` já venha com linguagens pré-instaladas para proporcionar mais velocidade e praticidade, você também pode instalar pacotes adicionais no contêiner usando [scripts de configuração](#manual-setup).

## Variáveis do ambiente e segredos

**Variáveis do ambiente** permanecem definidas durante todo o chat, incluindo os scripts de configuração e a fase do agente.

**Segredos** são semelhantes às variáveis do ambiente, mas há algumas diferenças:

- Eles são armazenados com uma camada adicional de criptografia e descriptografados somente para executar a tarefa.
- Eles ficam disponíveis somente para os scripts de configuração. Por motivos de segurança, os segredos são removidos antes do início da fase do agente.

## Configuração automática

Em projetos que usam gerenciadores de pacotes comuns (`npm`, `yarn`, `pnpm`, `pip`, `pipenv` e `poetry`), o Codex pode instalar dependências e ferramentas automaticamente.

## Configuração manual

Se sua configuração de desenvolvimento for mais complexa, você também pode fornecer um script de configuração personalizado. Por exemplo:

```bash
# Install type checker
pip install pyright

# Install dependencies
poetry install --with test
pnpm install

  Os scripts de configuração são executados em uma sessão Bash separada da sessão do agente, por isso comandos como
`export` não persistem na fase do agente. Para que as variáveis
  do ambiente persistam, adicione-as a `~/.bashrc` ou configure-as nas configurações do ambiente.

## Cache de contêineres

O Codex mantém o estado do contêiner em cache por até 12 horas para acelerar novos chats e interações subsequentes.

Quando um ambiente é armazenado em cache:

- O Codex clona o repositório e faz checkout da branch padrão.
- O Codex executa o script de configuração e armazena em cache o estado resultante do contêiner.

Quando um contêiner em cache é retomado:

- O Codex faz checkout da branch especificada para o chat.
- O Codex executa o script de manutenção (opcional). Isso é útil quando o script de configuração foi executado em um commit mais antigo e as dependências precisam ser atualizadas.

O Codex invalida o cache automaticamente se você alterar o script de configuração, o script de manutenção, as variáveis do ambiente ou os segredos. Se o repositório mudar de uma forma que torne incompatível o estado armazenado em cache, selecione **Redefinir cache** na página do ambiente.

  Para usuários do Business e de Empresas, os caches são compartilhados entre todos que têm
acesso ao ambiente. A invalidação do cache afetará todos os usuários do
ambiente no seu workspace.

## Acesso à internet e proxy de rede

O acesso à internet fica disponível durante a fase do script de configuração para instalar dependências. Durante a fase do agente, o acesso à internet fica desativado por padrão, mas você pode configurar o acesso limitado ou irrestrito. Consulte [acesso do agente à internet](/pt-BR/codex/cloud/internet-access).

Os ambientes são executados por trás de um proxy de rede HTTP/HTTPS para fins de segurança e prevenção de abusos. Todo o tráfego de saída para a internet passa por esse proxy.

<!-- source: https://learn.chatgpt.com/pt-BR/docs/amazon-bedrock -->

Configure as interfaces locais do ChatGPT Work e do Codex para usar modelos da OpenAI disponíveis
pelo Amazon Bedrock. Nessa configuração, o cliente local envia solicitações de modelo ao
Bedrock usando autenticação e controles de acesso gerenciados pela AWS.

## Como funciona

Quando você configura uma interface local do ChatGPT Work ou do Codex com o Amazon Bedrock como
provedor de modelos, a Responses API hospedada pela OpenAI não faz parte do caminho da solicitação.
O cliente local envia solicitações de modelo ao Amazon Bedrock, e o Bedrock fornece uma
implementação da Responses API compatível com a OpenAI para os modelos compatíveis da OpenAI.

  A autenticação é nativa da AWS. Os usuários se autenticam com uma chave de API do Bedrock ou credenciais do AWS
  IAM. Eles não usam o login do ChatGPT nem `OPENAI_API_KEY` para esse
  provedor.

## Antes de começar

Verifique se você tem:

- Acesso aos modelos compatíveis da OpenAI no Amazon Bedrock.
- Uma Região da AWS em que o modelo selecionado esteja disponível.
- Autenticação para o caminho Amazon Bedrock Mantle configurada na conta da
AWS.

## Configure o provedor

Adicione o provedor de modelos `amazon-bedrock` do caminho Amazon Bedrock Mantle em
`~/.codex/config.toml`. O aplicativo do ChatGPT para desktop, a Codex CLI, a extensão para IDE e o
SDK leem as mesmas camadas de configuração local. Especificar um modelo é opcional.
Selecione explicitamente um modelo compatível quando necessário.

```toml
model_provider = "amazon-bedrock"

  Este guia aborda o caminho Amazon Bedrock Mantle em Regiões comerciais da AWS
compatíveis. As interfaces locais do ChatGPT Work e do Codex não oferecem suporte a endpoints do Bedrock Mantle
nas Regiões do AWS GovCloud.

## Opções de autenticação

As interfaces locais do ChatGPT Work e do Codex oferecem suporte a dois métodos de autenticação do Bedrock.
Eles são verificados nesta ordem:

1. Chave de API do Bedrock.
2. Cadeia de credenciais do AWS SDK.

### Opção 1: chave de API do Bedrock

Defina a chave de API do Bedrock no ambiente lido pelo cliente local. É necessário
especificar uma Região ao usar a autenticação por chave de API.

```shell

### Opção 2: credenciais do AWS SDK

Use esse método quando sua organização gerencia o acesso ao Bedrock pela cadeia de
credenciais do AWS SDK. O cliente local pode usar estas fontes padrão de credenciais
do AWS SDK:

#### Arquivos de configuração compartilhados da AWS

Configure os arquivos compartilhados `config` e `credentials` da AWS:

```shell
aws configure

#### Variáveis do ambiente

Defina as variáveis padrão do ambiente para as credenciais do AWS SDK:

```shell

#### Credenciais do AWS Management Console

Faça login com as credenciais do AWS Management Console:

```shell
aws login

#### AWS SSO ou um perfil nomeado

Faça login com o AWS SSO e selecione o perfil nomeado:

```shell
aws sso login --profile codex-bedrock

#### Identidade federada

Para SSO corporativo ou federação OIDC, configure uma identidade federada com
`credential_process` fora do cliente local e deixe o AWS SDK resolver as
credenciais. Configure o login pelo navegador, a troca de tokens, o armazenamento em cache e a renovação no
auxiliar `credential_process` do seu perfil da AWS.

## Aplicativo para desktop e extensão para IDE

Aplicativos para desktop e extensões para IDE podem não herdar variáveis do ambiente do
shell. Coloque os valores necessários em `~/.codex/.env` e reinicie o aplicativo ou a
extensão.

```shell

## Verifique a configuração

- Na Codex CLI, abra `/status` e confirme se o Codex está usando o provedor de modelos
`amazon-bedrock`.
- No aplicativo do ChatGPT para desktop, selecione Work ou Codex e inicie uma nova tarefa depois de
reiniciar o aplicativo.
- Na extensão para IDE, inicie uma nova sessão depois de reiniciar a extensão.
- Confirme se o modelo selecionado está disponível na Região da AWS configurada e se
a identidade da AWS tem permissão para acessá-lo.

## Modelos compatíveis

Use os IDs exatos dos modelos:

```text
openai.gpt-5.6-sol
openai.gpt-5.6-terra
openai.gpt-5.6-luna
openai.gpt-5.5
openai.gpt-5.4

A disponibilidade dos modelos varia conforme a Região da AWS. Antes de selecionar um modelo, consulte [a compatibilidade dos modelos
por Região da
AWS](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html).

## Disponibilidade dos recursos

Esta configuração oferece suporte a fluxos de trabalho locais do ChatGPT Work e do Codex. O
ChatGPT Work hospedado na Web, o Codex Cloud e os recursos que dependem de serviços de nuvem hospedados
pela OpenAI, ferramentas hospedadas ou descoberta gerenciada na nuvem não estão disponíveis no
momento.

  O modo Fast não está disponível com o Amazon Bedrock. O modo Fast usa processamento
prioritário, e a oferta inicial do Amazon Bedrock oferece suporte apenas à inferência
sob demanda.

  

  <div
    id="codex-plan-region-limits"
    className="not-prose mt-3 text-sm text-secondary"
  >
    <sup>\*</sup> No momento, o recurso está limitado a regiões específicas. Consulte
    a documentação de cada recurso para saber mais sobre as restrições geográficas.
  </div>
  <div
    id="codex-plan-plugin-limits"
    className="not-prose mt-1 text-sm text-secondary"
  >
    <sup>†</sup> Estão disponíveis pacotes locais de plug-ins e plug-ins selecionados pela OpenAI que não
    exigem autenticação do ChatGPT, incluindo o Codex Security.
    Não estão disponíveis plug-ins que exigem autenticação do ChatGPT, conectores nem
    compartilhamento hospedado na nuvem.
  </div>

## Solução de problemas

Se a configuração falhar, verifique o seguinte:

- O ID do modelo corresponde exatamente ao de um modelo compatível.
- Você especificou uma Região da AWS em que o modelo está disponível.
- A chave de API do Bedrock ou as credenciais da AWS são válidas e não expiraram.
- A identidade da AWS tem permissão para acessar o modelo do Bedrock selecionado.
- `AWS_BEARER_TOKEN_BEDROCK` não está configurado com uma chave expirada ou diferente da pretendida.
- Para usar o aplicativo para desktop ou a extensão para IDE, as variáveis do ambiente necessárias estão
  presentes em `~/.codex/.env`.

## Limites do suporte

O Suporte da OpenAI pode ajudar com a preparação e a configuração dos clientes do ChatGPT Work e do Codex,
com o comportamento local da CLI, do aplicativo para desktop e da extensão para IDE
e com a experiência local com o produto.

Para credenciais da AWS, permissões do IAM, acesso a modelos do Bedrock, cotas, faturamento,
disponibilidade regional, falhas em solicitações ao Bedrock, logs de serviços da AWS ou comportamento do serviço do Bedrock,
entre em contato com o administrador da AWS do cliente ou com o Suporte da AWS.

<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/workload-identity -->

A federação de identidade de cargas de trabalho permite que automações confiáveis usem o Codex sem armazenar um token de acesso pessoal ou outra credencial de longa duração da OpenAI. Sua carga de trabalho apresenta um token de identidade de curta duração emitido por um provedor que você já opera. A OpenAI verifica esse token e retorna um token de acesso de curta duração para um usuário ou uma conta de serviço no seu workspace gerenciado do ChatGPT.

Use a identidade de cargas de trabalho para processos não supervisionados do Codex em plataformas de nuvem,
Kubernetes, sistemas de CI e outros ambientes capazes de emitir tokens OIDC ou
SPIFFE JWT-SVIDs. Para conhecer o modelo de confiança compartilhado e o fluxo separado da API da OpenAI,
consulte a [visão geral da identidade de cargas de trabalho](/api/docs/guides/workload-identity-federation).

  A federação de identidade de cargas de trabalho do Codex está em versão beta e precisa estar habilitada para o seu
  workspace. Para solicitar acesso, entre em contato com seu representante da OpenAI ou com o [Suporte da
  OpenAI](https://help.openai.com/en/articles/6614161-how-can-i-contact-support).

## Antes de começar

Você precisa de:

- Permissão para gerenciar identidades de cargas de trabalho no Portal de Administração da OpenAI.
- Um workspace gerenciado do ChatGPT.
- Um usuário do ChatGPT ou uma conta de serviço que seja membro ativo desse workspace, ou permissão para criar um deles durante a configuração.
- Um token OIDC ou SPIFFE JWT-SVID cujo emissor, público-alvo e declarações de identificação você conheça.
- Um ambiente de execução capaz de manter esse token atualizado em um arquivo protegido localizado em um caminho absoluto.
- Codex 0.148.0 ou posterior.
- Uma política de autenticação efetiva do Codex que permita a autenticação pelo ChatGPT
  e o workspace selecionado pela regra de federação. Consulte [Exigir um método de login
  ou workspace](/pt-BR/codex/auth#enforce-a-login-method-or-workspace).

A OpenAI não cria uma entidade principal nem uma associação ao workspace durante a troca de tokens. Um administrador seleciona ou cria a entidade principal antes que a carga de trabalho se conecte. A criação de um usuário humano consome uma vaga no workspace e segue as regras de associação desse workspace.

No Windows nativo, use o modo **elevado**
do [Sandbox do Windows](/pt-BR/codex/windows/windows-sandbox). Outros modos do Sandbox do Windows
não conseguem proteger o arquivo do token de identidade contra comandos controlados pelo modelo.

## Obtenha um token de identidade

O ambiente de execução da sua carga de trabalho obtém e renova o token de identidade de origem. O Codex não chama serviços de metadados da nuvem nem bibliotecas cliente de provedores de identidade em seu nome.

| Ambiente de execução                          | Origem recomendada do arquivo de token                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Kubernetes, AKS, EKS ou GKE     | Monte um token projetado de conta de serviço e configure o Codex para usar esse arquivo. A plataforma faz a rotação do token.                                  |
| Identidade gerenciada do Microsoft Entra | Execute um processo confiável no host ou um sidecar que solicite um token ao Azure IMDS e substitua o arquivo antes da expiração.                |
| Federação de identidade de saída da AWS | Execute um processo confiável no host que chame a operação `GetWebIdentityToken` do STS regional e substitua o arquivo antes da expiração.                   |
| Google Cloud                     | Execute um processo confiável no host que solicite um token de identidade ao servidor de metadados e substitua o arquivo antes da expiração.        |
| Oracle Cloud Infrastructure      | Execute um processo confiável no host que use uma entidade principal de instância para solicitar um token de acesso IDCS e substitua o arquivo antes da expiração. |
| GitHub Actions                   | Solicite o token OIDC do job, grave-o em um arquivo protegido e solicite um novo token antes de uma troca posterior.                    |
| SPIFFE                           | Use a SPIFFE Workload API ou um utilitário auxiliar aprovado para gravar um JWT-SVID atualizado no arquivo.                                      |
| Provedor OIDC personalizado             | Use o fluxo de cargas de trabalho do emissor para obter um JWT e atualize o arquivo protegido antes que o JWT expire.                            |

Siga o guia do seu provedor para configurar a emissão de tokens e inspecionar um token de exemplo:

- [Microsoft Azure](/api/docs/guides/workload-identity-federation/microsoft-azure)
- [AWS](/api/docs/guides/workload-identity-federation/aws)
- [Google Cloud](/api/docs/guides/workload-identity-federation/google-cloud)
- [Oracle Cloud Infrastructure](/api/docs/guides/workload-identity-federation/oracle-cloud)
- [GitHub Actions](/api/docs/guides/workload-identity-federation/github-actions)
- [Kubernetes](/api/docs/guides/workload-identity-federation/kubernetes)
- [SPIFFE](/api/docs/guides/workload-identity-federation/spiffe)

Decodifique localmente um token de exemplo e registre seus campos `iss`, `aud`, `sub` e quaisquer outras
declarações nas quais você pretende confiar. A decodificação não verifica a assinatura. Não cole um token
de produção em um site nem o grave em logs.

## Conecte a carga de trabalho

Um administrador cria o provedor e a regra de federação antes de iniciar o Codex.

1. Abra [Identidade de cargas de trabalho](https://admin.openai.com/workload-identity) no
   Portal de Administração da OpenAI e selecione **Conectar carga de trabalho**.
2. Reutilize um provedor configurado para o Codex ou crie um. As predefinições do provedor preenchem configurações comuns para GitHub Actions, Microsoft Entra ID, Google Cloud, AWS, Kubernetes, SPIFFE e provedores OIDC personalizados.
3. Selecione **Codex** e o workspace gerenciado que a carga de trabalho poderá usar.
4. Adicione as condições mais restritivas que identifiquem a carga de trabalho. Defina uma correspondência por assunto, declarações exatas, condição CEL ou uma combinação desses critérios. Adicione públicos-alvo aceitos para restringir quais tokens a regra aceita. Todos os critérios de correspondência configurados devem ser atendidos.
5. Associe a regra a um usuário existente do ChatGPT ou a uma conta de serviço existente, ou crie um deles durante a configuração.
6. Revise o provedor, as condições, o workspace, a entidade principal, os escopos e a validade
   do token de acesso. Selecione **Conectar carga de trabalho** e, em seguida, **Baixar configuração**.

O arquivo baixado contém um ID não confidencial da regra de federação e o caminho em que o Codex lerá o token de identidade. Ele não contém nenhuma credencial.

Para automatizar a configuração, use a [API de administração de identidade de cargas
de trabalho](/api/docs/guides/workload-identity-federation/admin-api). Para conhecer o comportamento dos critérios de correspondência
e consultar exemplos, veja a [referência das regras
de federação](/api/docs/guides/workload-identity-federation/federation-rules).

## Configure o processo do Codex

O processo que inicia o Codex exige estas duas variáveis de identidade de cargas de trabalho:

```bash

`OPENAI_FEDERATION_RULE_ID` não é um segredo. O arquivo do token, sim. Use um caminho absoluto
em um diretório dedicado, como `/var/run/secrets/openai.com`, pertencente à
conta da carga de trabalho e com o modo `0700`. Somente processos confiáveis no host devem gravar
nesse diretório. Mantenha-o fora de repositórios e de outros caminhos acessíveis às
ferramentas do Codex. Não inclua credenciais em logs, no histórico do shell ou em artefatos de build.

### Adicione atribuição de auditoria

Quando instâncias do ambiente de execução compartilham uma regra de federação, você pode identificar cada instância
nos eventos de auditoria de emissão de tokens. Defina a variável opcional
`OPENAI_WORKLOAD_IDENTITY_CONTEXT` como um objeto JSON codificado na forma de
string:

```bash

  "instance_id": "runner-42",
  "display_name": "payments-prod",
  "labels": {
    "environment": "production",
    "region": "us-west-2"
  }
}'

O objeto exige `instance_id`. Ele também pode conter `display_name` e até
oito rótulos. O objeto codificado pode ter até 1.024 bytes. `instance_id` e
`display_name` podem ter até 128 caracteres. As chaves dos rótulos podem ter até 64
caracteres, e os valores dos rótulos podem ter até 256 caracteres.

Os identificadores devem começar com uma letra ou um número ASCII. Em seguida, os valores podem conter
letras, números, `.`, `_`, `:`, `/`, `@` e `-`. As chaves dos rótulos aceitam letras,
números, `.`, `_` e `-`.

A OpenAI trata esse contexto como uma atribuição de auditoria informada pelo cliente, e não como uma identidade verificada da carga de trabalho. Ele não afeta a autenticação, a autorização, a correspondência de regras, os escopos, os limites de taxa, a revogação, as condições de habilitação de recursos nem as métricas. Não inclua credenciais, segredos, dados pessoais, prompts, saídas do modelo ou qualquer outro Conteúdo do Cliente.

Quando o contexto é válido, a OpenAI deriva um ID de atribuição estável restrito ao tenant,
ao provedor, à regra de federação e a `instance_id`. Para fins de atribuição, o token de acesso
contém o ID, mas não o contexto. O evento de auditoria de emissão bem-sucedida de token
contém o ID e o contexto normalizado. Um contexto que exceda um limite ou
viole esse esquema faz com que a troca falhe com `invalid_grant`.

O Codex lê o contexto quando o processo é iniciado e não repassa o contexto, o ID da regra nem o caminho do arquivo de token a shells, hooks ou servidores MCP controlados pelo modelo. Reinicie o Codex depois de alterar o contexto.

### Proteja o arquivo de token e faça sua rotação

Para implantações gerenciadas no Linux, no macOS e no WSL, adicione todo o diretório do token a
[`permissions.filesystem.deny_read`](/pt-BR/codex/enterprise/managed-configuration#enforce-deny-read-requirements)
nos requisitos gerenciados:

```toml
[permissions.filesystem]
deny_read = ["/var/run/secrets/openai.com"]

Isso impede que comandos controlados pelo modelo leiam o token ativo ou uma substituição temporária, enquanto o processo do host do Codex ainda pode usar o token para a troca. Para volumes de tokens projetados, bloqueie toda a montagem do token e quaisquer caminhos subjacentes ou caminhos de destino resolvidos fora dela. Os modos dos arquivos e a limpeza das variáveis de ambiente, por si só, não protegem as credenciais de outros processos executados pelo mesmo usuário. No Windows nativo, use o sandbox elevado descrito acima.

Para fontes de token que não projetam um arquivo, faça com que um processo confiável do host grave cada arquivo de substituição nesse diretório protegido e o renomeie para o local definitivo. Uma renomeação atômica impede que o Codex leia um token incompleto. Por exemplo, adapte este script de atualização controlado pelo host ao comando de token do seu provedor. Provisione o diretório antes de executar o script:

```bash
set -eu
TOKEN_DIR="/var/run/secrets/openai.com"
TOKEN_FILE="$TOKEN_DIR/identity-token"
umask 077
TOKEN_TEMP="$(mktemp "$TOKEN_DIR/.identity-token.XXXXXX")"
trap 'rm -f -- "$TOKEN_TEMP"' EXIT
trap 'exit 1' HUP INT TERM
your-identity-provider-command > "$TOKEN_TEMP"
test -s "$TOKEN_TEMP"
mv -f -- "$TOKEN_TEMP" "$TOKEN_FILE"

Execute o processo de atualização fora de qualquer shell ou ferramenta que o Codex possa controlar. Mantenha
o bloqueio de leitura durante a atualização e a limpeza. Mesmo que uma interrupção forçada
deixe um arquivo temporário, ele deverá permanecer no diretório com leitura
bloqueada. Não inclua configurações de identidade de carga de trabalho em `config.toml`.

## Verifique a conexão

Carregue o ambiente baixado e inspecione o método de autenticação selecionado:

```bash
. ./workload-identity-idpm_example.env
codex login status

No PowerShell:

```powershell
$env:OPENAI_FEDERATION_RULE_ID = "idpm_..."
$env:OPENAI_IDENTITY_TOKEN_FILE = "C:\run\openai\identity-token"
codex login status

Uma verificação bem-sucedida exibe `Logged in using workload identity`. Isso confirma
que o Codex trocou um token por meio da regra de federação configurada. O comando
não exibe o workspace, a entidade de segurança nem a regra resolvidos. Confirme esses valores
no Portal do Administrador antes de iniciar a carga de trabalho. Se o Codex informar outro
método de autenticação, as duas variáveis WIF obrigatórias não chegaram ao processo.

Se o provedor usar **Impedir a repetição de asserções** e a asserção tiver a declaração `jti`,
essa verificação consumirá esse `jti`. Grave uma asserção recém-emitida com um novo
`jti` antes de iniciar outro processo do Codex.

Execute uma pequena requisição no mesmo ambiente:

```bash
codex exec "Reply with only: workload identity is working"

O Codex troca o token de origem e mantém o token de acesso da OpenAI na memória.
Ele não grava nenhuma das credenciais em `auth.json`, no chaveiro do sistema nem em
`config.toml`.

## Mantenha o token atualizado

Atualize o arquivo do token de identidade antes que o token de origem expire. O Codex relê o arquivo quando precisa de outro token de acesso da OpenAI. O token da OpenAI expira no momento que ocorrer primeiro: o vencimento do token de origem ou o término do prazo definido pela regra de federação. Em nenhum caso ele dura mais de uma hora.

Quando um administrador ativa a proteção contra repetição, cada JWT de origem deve ter um
`jti` exclusivo. Grave uma asserção recém-emitida com um novo `jti` antes de cada
troca, inclusive nas renovações de um processo de longa duração. Asserções sem
`jti` não recebem proteção contra repetição.

O Codex compartilha uma única sessão de troca em memória dentro de cada processo do host. Requisições simultâneas nesse processo reutilizam um token de acesso válido da OpenAI e compartilham uma única renovação quando ele expira. Processos separados realizam trocas separadas e, portanto, precisam de asserções cujo uso seja permitido pelo provedor.

## Precedência das credenciais

As duas variáveis obrigatórias de identidade de carga de trabalho têm precedência sobre todas as outras fontes de credenciais:

1. Se `OPENAI_FEDERATION_RULE_ID` ou
`OPENAI_IDENTITY_TOKEN_FILE` estiver presente, o Codex selecionará a identidade de carga de trabalho.
2. Se apenas uma das variáveis obrigatórias estiver presente, o Codex retornará um erro. Ele não recorrerá a uma chave de API, a um token de acesso nem a um login armazenado.
3. `OPENAI_WORKLOAD_IDENTITY_CONTEXT`, isoladamente, não seleciona a identidade de carga de trabalho.
4. Quando nenhuma das variáveis WIF obrigatórias está presente, o Codex aplica as regras
   normais de credenciais dessa interface. Nas interfaces que permitem autenticação
   por chave de API, `CODEX_API_KEY` tem precedência em `codex exec`,
`codex review`, no TypeScript SDK e em `codex exec-server --remote`. Outras
   interfaces podem usar `CODEX_ACCESS_TOKEN` ou um login armazenado.

Uma opção `apiKey` do SDK se torna `CODEX_API_KEY`, mas WIF continua tendo precedência
quando qualquer uma das variáveis WIF obrigatórias está presente. Omita essa opção ao usar WIF para
que a carga de trabalho não mantenha uma credencial de longa duração sem uso.

Para migrar uma carga de trabalho existente sem interrupções, configure WIF enquanto sua credencial atual ainda estiver disponível. Inicie um novo processo com as duas variáveis WIF obrigatórias; WIF terá precedência mesmo que a credencial antiga ainda esteja presente. Depois que a carga de trabalho funcionar com WIF, remova a credencial antiga do ambiente de execução e do armazenamento de segredos e, em seguida, revogue-a. Antes da revogação, você pode reverter a alteração removendo as duas variáveis WIF obrigatórias e iniciando um novo processo.

## Interfaces compatíveis do Codex

Configure a identidade de carga de trabalho na máquina responsável pelo processo do Codex.

| Interface                                         | Compatibilidade e limites do host                                                                               |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Uso interativo de `codex`, `resume` e `fork`       | Compatível. Inicie a CLI no ambiente configurado.                                                 |
| `codex exec`, `exec resume` e `codex review` | Compatível. A presença de qualquer uma das variáveis WIF obrigatórias dá precedência à WIF.                                      |
| TypeScript SDK                                  | Compatível. O processo pai fornece as variáveis WIF obrigatórias e qualquer contexto opcional de atribuição. |
| `codex app-server`                              | Compatível. Configure WIF no host do app-server, não em um cliente remoto.                                |
| `codex exec-server --remote`                    | Compatível com a autenticação no registro de ambientes remotos. Configure WIF no host do exec-server. |
| Operações locais de processos do exec-server            | Não usam autenticação WIF. São executadas pelo protocolo local do exec-server.                         |
| `codex mcp-server`                              | Não compatível.                                                                                          |

Clientes remotos do app-server e do exec-server nunca enviam o token de identidade de origem por seus protocolos.

## Altere ou remova o acesso

Alterações nos assuntos, nos públicos-alvo, nas declarações, na condição CEL, nos escopos ou no prazo de validade do token de uma regra se aplicam a novas trocas. Um token emitido antes da alteração pode continuar válido até o fim de seu prazo de validade.

Desative um provedor ou uma regra para interromper o acesso imediatamente. A desativação bloqueia novas trocas e revoga os tokens de acesso da OpenAI já emitidos por meio desse recurso. O arquivamento tem o mesmo efeito sobre o acesso e não pode ser desfeito. A alteração da relação de confiança do provedor também revoga os tokens emitidos antes que a nova relação de confiança entre em vigor.

## Audite as alterações

A criação, a atualização e o arquivamento de provedores e regras de federação geram eventos
de auditoria. Use as [orientações sobre a API de Compliance e eventos
de auditoria](/pt-BR/codex/enterprise/compliance-api) para exportar os eventos compatíveis com seu
workspace. Correlacione-os com os logs de emissão do seu provedor de identidade e não
registre asserções de origem nem tokens de acesso da OpenAI em nenhum dos sistemas.

Quando o processo fornece `OPENAI_WORKLOAD_IDENTITY_CONTEXT`, os eventos
de auditoria de emissão bem-sucedida de tokens também contêm o ID de atribuição estável e o
contexto normalizado descritos acima.

## Solução de problemas

| Sintoma                                                               | Verificação                                                                                                              |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| O Codex informa que a configuração de identidade de carga de trabalho está incompleta              | Defina as duas variáveis obrigatórias no mesmo processo e use um caminho absoluto para o arquivo de token.                               |
| O Codex informa que sua política de login não permite a identidade de carga de trabalho | Permita a autenticação do ChatGPT na política efetiva e inclua o workspace da regra entre os workspaces permitidos. |
| O Codex informa outra credencial                                      | Carregue as duas variáveis WIF obrigatórias no processo do Codex, inicie um novo processo e execute `codex login status` novamente.  |
| A OpenAI rejeita o contexto da carga de trabalho                                       | Verifique a estrutura JSON, o tamanho, os caracteres permitidos e os limites dos campos. Remova conteúdo sensível ou Conteúdo do Cliente.            |
| A OpenAI rejeita o token                                              | Compare `iss`, `aud`, o vencimento, a chave de assinatura e o prazo de validade da asserção com a configuração do provedor.               |
| A regra não corresponde                                               | Confirme se o cliente usa o ID da regra pretendida e se todas as verificações de assunto, público-alvo, declaração exata e CEL são bem-sucedidas.  |
| A OpenAI rejeita a entidade de segurança                                          | Confirme que o usuário ou a conta de serviço tem status ativo e é membro ativo do workspace selecionado.                   |
| A OpenAI rejeita uma asserção repetida                                   | Obtenha um novo JWT com um novo `jti`; não tente usar novamente a mesma asserção protegida contra repetição.                                  |
| Um processo de longa duração para de atualizar                               | Confirme se o processo de atualização do host continua substituindo o arquivo de token antes do vencimento.                                  |

Para informações sobre verificação do provedor, limites e detalhes de CEL, consulte a [referência da regra
de federação](/api/docs/guides/workload-identity-federation/federation-rules).

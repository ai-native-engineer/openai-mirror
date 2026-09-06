<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/plugin-management -->

## Antes de começar

Os administradores do workspace podem importar um marketplace de plug-ins do GitHub e manter seus plug-ins atualizados a partir do repositório. Um marketplace é um catálogo JSON que lista os plug-ins a serem importados.

Use uma conta do GitHub com acesso de leitura ao repositório do marketplace e a todos os outros repositórios que ele referencia. Há suporte a repositórios públicos e privados do GitHub. Antes de importar, obtenha todas as aprovações da organização no GitHub exigidas para acessar o repositório.

Revise o conteúdo do repositório antes de importar. Novos plug-ins começam com a política de instalação **Disponível** e autenticação na instalação. Novos marketplaces têm a sincronização diária automática ativada. A importação processa todas as entradas válidas, e as próximas sincronizações adicionam automaticamente quaisquer novos plug-ins do repositório.

## Configure a sincronização de um marketplace

1. Abra **Administração** \> **Plug-ins** e selecione **Adicionar** \> **Importar marketplace**.
2. Em **Origem**, insira a URL do repositório, como `https://github.com/example/team-plugins`. Use apenas a URL do repositório, sem incluir uma URL de branch ou pasta.
3. Se o marketplace estiver em um subdiretório, insira esse diretório em **Caminho**. Por exemplo, use `team-tools` para `team-tools/.agents/plugins/marketplace.json`. Deixe **Caminho** em branco para usar a raiz do repositório. Não insira o nome do arquivo de manifesto.
4. Se quiser, preencha **Branch, tag ou commit**. Deixe esse campo em branco para usar a branch padrão do repositório. Use uma branch para receber commits futuros; um commit fixo permanece naquela revisão.
5. Selecione **Importar marketplace** e autorize o acesso ao GitHub quando solicitado. A importação inicial pode levar até uma hora para marketplaces muito grandes. As sincronizações diárias seguintes costumam levar alguns minutos.
6. Revise os **Resultados da importação** e abra cada plug-in importado para configurar sua política de instalação e os aplicativos necessários.

Para solicitar uma atualização sem esperar pela sincronização diária, abra o marketplace em **Administração** \> **Plug-ins** \> **Marketplaces** e selecione **Sincronizar agora**.

## Formatos compatíveis

O diretório selecionado deve conter um destes arquivos:

| Arquivo                               | Formato                                                               |
| ---------------------------------- | -------------------------------------------------------------------- |
| `.agents/plugins/marketplace.json` | Um marketplace do Codex com um vetor `plugins`.                          |
| `.claude-plugin/marketplace.json`  | Um marketplace compatível com o Claude com um vetor `plugins`.              |
| `.claude-plugin/plugin.json`       | Um plug-in independente do Claude, quando não há um manifesto de marketplace. |

Em um marketplace, as entradas podem referenciar plug-ins nativos com `.codex-plugin/plugin.json`, plug-ins compatíveis com o Claude, pacotes Agent Plugins 1.0 ou pacotes de habilidades compatíveis.

Para um marketplace do Codex, use caminhos locais para plug-ins no mesmo repositório:

```json
{
  "name": "team-plugins",
  "interface": {
    "displayName": "Team plugins"
  },
  "plugins": [
    {
      "name": "team-tools",
      "source": {
        "source": "local",
        "path": "./plugins/team-tools"
      }
    }
  ]
}

O caminho é relativo à raiz do marketplace selecionada, não a `.agents/plugins/`.

Um marketplace compatível com o Claude pode usar um caminho em texto para cada plug-in local:

```json
{
  "name": "team-plugins",
  "plugins": [
    {
      "name": "team-tools",
      "source": "./plugins/team-tools"
    }
  ]
}

As entradas de um marketplace do Codex também aceitam `source: "url"` para um plug-in na raiz de um repositório do GitHub e `source: "git-subdir"` para um plug-in em um subdiretório do GitHub. Por exemplo:

```json
{
  "name": "team-tools",
  "source": {
    "source": "git-subdir",
    "url": "https://github.com/example/team-tools.git",
    "path": "./plugins/team-tools",
    "ref": "main"
  }
}

As fontes Git permitem selecionar uma `ref` ou o `sha` completo de 40 caracteres de um commit. A conta do GitHub que autoriza o acesso deve ter acesso de leitura a todos os repositórios referenciados. Atualmente, a importação para o workspace aceita apenas repositórios do GitHub.

## Configure o acesso no workspace

A importação e a sincronização do GitHub não aplicam as políticas de instalação ou autenticação do repositório, incluindo `AVAILABLE`, `INSTALLED_BY_DEFAULT`, `NOT_AVAILABLE`, `ON_INSTALL` e `ON_USE`. Os administradores do workspace definem essas configurações para cada plug-in. Sincronizar uma atualização ou migrar um plug-in existente para o gerenciamento via GitHub preserva suas políticas do workspace.

Use **Política de instalação** para escolher **Disponível** ou **Instalado** para cada função elegível. Os aplicativos necessários também devem estar ativados, e os membros devem ter acesso ao serviço conectado. Importar um plug-in não concede acesso a aplicativos nem conecta as contas dos membros. Consulte [Controles de plug-ins](/pt-BR/codex/enterprise/apps-and-connectors) para saber mais sobre os controles de funções, aplicativos e ações.

## Migre um plug-in existente para o gerenciamento via GitHub

Adicione `pluginId` à entrada do plug-in existente no marketplace:

```json
{
  "name": "team-tools",
  "pluginId": "plugin_0123456789abcdef0123456789abcdef",
  "source": {
    "source": "local",
    "path": "./plugins/team-tools"
  }
}

Abra o plug-in em **Administração** \> **Plug-ins** e copie o ID que aparece após `/admin/plugins/` na URL. Coloque `pluginId` ao lado de `name` e `source` na entrada do marketplace. O plug-in existente deve estar no mesmo workspace.

Isso faz com que um plug-in do workspace enviado por upload ou não gerenciado passe a ser gerenciado via GitHub. O plug-in mantém seu ID, compartilhamento e políticas do workspace. As próximas atualizações vêm do GitHub; uploads de arquivos compactados não podem mais substituir o plug-in gerenciado. Um plug-in já gerenciado por outra fonte do GitHub não pode ter seu gerenciamento transferido dessa forma.

## Plug-ins exclusivos para desktop

Qualquer plug-in importado que declare servidores MCP em `mcp.json` ou `.mcp.json` recebe a indicação **Somente desktop** e funciona apenas no aplicativo do ChatGPT para desktop. Isso inclui servidores que usam uma URL HTTPS remota. A mesma restrição se aplica a outras formas de configuração de MCP compatíveis, como declarações de servidores em linha.

## Referencie um aplicativo existente com `.app.json`

Adicione `.app.json` à raiz do plug-in. O nome do arquivo começa com um ponto; `app.json`, sem o ponto, não é compatível.

```json
{
  "apps": {
    "team-tools": {
      "id": "asdk_app_example",
      "required": true
    }
  }
}

Substitua `asdk_app_example` pelo ID do aplicativo existente. Os IDs de aplicativos compatíveis começam com `asdk_app_`, `connector_` ou `templated_apps_`. Use o ID do aplicativo, não um ID `plugin_...`. Por exemplo, uma URL de plug-in que contém `plugin_asdk_app_example` representa o aplicativo `asdk_app_example`.

A chave `team-tools` dá nome à referência dentro deste arquivo. Defina `required` como `true` quando o plug-in depender do aplicativo. Você pode adicionar mais entradas para referenciar outros aplicativos existentes.

Para um plug-in nativo, defina `apps` como `./.app.json` em `.codex-plugin/plugin.json`. Veja o manifesto completo deste exemplo:

```json
{
  "name": "team-tools",
  "version": "1.0.0",
  "description": "Use the team's approved tools.",
  "author": {
    "name": "Example team"
  },
  "apps": "./.app.json",
  "interface": {
    "displayName": "Team tools",
    "shortDescription": "Use approved team tools",
    "longDescription": "Connect to the team's existing app.",
    "developerName": "Example team",
    "category": "Productivity",
    "capabilities": ["Read"]
  }
}

Mantenha os arquivos nesta estrutura:

```text
team-plugins/
├── .agents/plugins/marketplace.json
└── plugins/team-tools/
    ├── .codex-plugin/plugin.json
    └── .app.json

A referência não cria um aplicativo nem concede permissões. Os administradores devem disponibilizar o aplicativo para as funções pretendidas, e os membros devem concluir qualquer autenticação exigida. As permissões do aplicativo, os controles de ações e o acesso ao serviço existentes continuam valendo.

## Mantenha os plug-ins atualizados

Novos marketplaces verificam diariamente se há atualizações. Abra **Administração** \> **Plug-ins** \> **Marketplaces**, selecione o marketplace e escolha **Sincronizar agora** para solicitar uma atualização sem esperar pela sincronização automática.

A sincronização pode adicionar novas entradas ao marketplace e atualizar plug-ins existentes. Revise as alterações no repositório antes de mesclá-las, pois a sincronização automática importará quaisquer novos plug-ins.

Após uma sincronização, revise o status e o relatório salvo. **Concluído — N erros** significa que a execução terminou, mas alguns plug-ins não puderam ser processados. Se uma atualização de um plug-in existente for inválida, a última versão funcional será mantida. Corrija o problema relatado no GitHub e selecione **Sincronizar agora** para tentar novamente.

Remover uma entrada do repositório não exclui sua cópia importada no workspace. Ela recebe a indicação **Não está mais na origem**. Excluir o marketplace no ChatGPT exclui todos os plug-ins importados dele.

## Restabeleça ou altere o acesso ao GitHub

Para **restabelecer o acesso ao GitHub**, primeiro confirme que a conta do GitHub usada na importação ainda tem acesso ao repositório e a todos os repositórios referenciados. O administrador que importou o marketplace originalmente deve então abrir o plug-in do GitHub no ChatGPT e reconectar sua conta, pois a sincronização do marketplace usa a conexão desse administrador com o GitHub.

Para **transferir para um novo proprietário**, o novo administrador do workspace deve abrir **Administração** \> **Plug-ins** \> **Adicionar** \> **Importar marketplace** e importar o mesmo marketplace usando os mesmos valores de **Origem**, **Caminho** e **Branch, tag ou commit** . As próximas sincronizações usarão a conexão desse administrador com o GitHub.

Não exclua o marketplace apenas para reconectá-lo ou alterar sua propriedade: a exclusão também remove os plug-ins importados dele.

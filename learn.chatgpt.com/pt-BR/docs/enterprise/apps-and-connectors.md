<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/apps-and-connectors -->

Os plug-ins reúnem fluxos de trabalho reutilizáveis e podem incluir habilidades e aplicativos que se conectam
a outras ferramentas. O ChatGPT e o Codex usam o mesmo diretório público de plug-ins nas
interfaces compatíveis, enquanto os administradores definem quais plug-ins estão disponíveis no workspace.
Saiba mais sobre [plug-ins](/pt-BR/codex/plugins),
[habilidades](/pt-BR/codex/skills-and-plugins) e
[aplicativos e conectores](https://help.openai.com/en/articles/11487775).

Um membro só pode usar uma capacidade oferecida por um conector quando o plug-in e o aplicativo
estão disponíveis para sua função e ele tem acesso ao serviço conectado.

Os plug-ins funcionam no Chat e no Work do ChatGPT na Web, no desktop e em dispositivos móveis,
no Codex no aplicativo do ChatGPT para desktop e pelo navegador de plug-ins da Codex CLI.
Eles não estão disponíveis na extensão para IDE.

Para entender como esses controles se relacionam com as funções e permissões do workspace, consulte
[Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions).

## Entenda a cadeia de capacidades

Um plug-in pode abranger estas camadas de controle:

| Camada                   | O que determina                                                           | Onde gerenciar                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Disponibilidade            | Se o pacote do plug-in está disponível para o usuário                           | [Configurações do workspace](https://chatgpt.com/admin/settings) para as interfaces compatíveis na Web e no desktop; navegador de plug-ins da CLI para a CLI |
| Habilidades incluídas         | Quais instruções reutilizáveis o plug-in instalado fornece                 | O pacote do plug-in e os [Controles de habilidades](/pt-BR/codex/enterprise/skills)                                                               |
| Acesso a aplicativos              | Se os usuários podem usar uma capacidade oferecida por um conector                          | [Apps do workspace](https://chatgpt.com/admin/ca) e [Permissões e funções](https://chatgpt.com/admin/settings)                    |
| Ações e permissões | Quais ações os usuários podem executar e quando o ChatGPT solicita confirmação antes de usar o conector | O Controle de ações e as Permissões de App do conector em [Apps do workspace](https://chatgpt.com/admin/ca)                            |
| Autorização do serviço   | Quais dados e ações externos a identidade autenticada pode acessar        | O serviço conectado e seu provedor de identidade                                                                                 |
| Permissões em tempo de execução     | O que um agente pode fazer depois de receber dados ou uma ferramenta                        | Os controles do ambiente de execução, de sandbox e de aprovação da interface ativa                                                              |

Use essas camadas para uma implementação em duas etapas: primeiro, disponibilize os plug-ins adequados;
depois, configure as capacidades e permissões necessárias para cada fluxo de trabalho.

## Etapa 1: Disponibilize os plug-ins

Nas interfaces compatíveis na Web e no desktop, os controles de plug-ins do workspace determinam
quais funções podem usar ou instalar um plug-in. A Codex CLI usa seu próprio navegador de plug-ins
para a instalação. Consulte
[Criar plugins](https://developers.openai.com/plugins/build/plugins) para saber mais sobre
empacotamento e distribuição.

Para importar plug-ins do GitHub para o workspace e mantê-los atualizados, consulte
[Gerenciamento de plug-ins](/pt-BR/codex/enterprise/plugin-management).

### Exporte o catálogo público para revisão

Proprietários e administradores elegíveis de um workspace do ChatGPT Enterprise podem baixar um CSV com
os plug-ins públicos disponíveis nesse workspace. Use o arquivo exportado para revisar os metadados de
plug-ins, aplicativos e habilidades antes de alterar a disponibilidade dos plug-ins.

1. Abra [Administração \> Plug-ins](https://chatgpt.com/admin/plugins).
2. Selecione **Público**.
3. Selecione o ícone de download (**Exportar CSV**) no cabeçalho da página.

O arquivo baixado tem o nome `public-plugins-security-review.csv` e inclui:

- Metadados do plug-in: `Plugin Name`, `Plugin Description`, `Date Added (UTC)`,
`OpenAI Verified`, `Developer Name` e `Version`.
- Metadados do aplicativo: `App Name(s)` e `App Description(s)`.
- Metadados das habilidades do Chat: `Skill Name(s)` e `Skill Description(s)`.

Quando um plug-in inclui mais de um aplicativo ou habilidade, os valores correspondentes são separados
por ponto e vírgula. A exportação usa uma cópia do catálogo público que pode ter sido gerada até
48 horas antes,
inclui apenas plug-ins públicos visíveis no workspace atual e não inclui
plug-ins criados para esse workspace. Ela não está disponível em workspaces
FedRAMP.

## Etapa 2: Gerencie as capacidades

  Disponibilizar um aplicativo ou plug-in no ChatGPT não concede acesso a arquivos,
registros ou ações no serviço conectado. Antes de solucionar problemas ou
ampliar o acesso, verifique a função do membro no workspace e as configurações
aprovadas para as ações. Em seguida, confirme se a conta autenticada ou a conexão
compartilhada tem as permissões esperadas no serviço conectado.

Os plug-ins do ChatGPT e do Codex podem incluir conectores que pesquisam, recuperam ou sincronizam dados,
ou atuam em sistemas externos. A disponibilidade dos plug-ins e o acesso e as ações
concedidos a cada conector são controles independentes.

Gerencie as capacidades oferecidas por conectores em
[Apps do workspace](https://chatgpt.com/admin/ca) e em
[Permissões e funções](https://chatgpt.com/admin/settings). Os controles disponíveis
permitem aos administradores:

- Ativar aplicativos ou conectores e atribuir acesso conforme a função no workspace.
- Para conectores que oferecem suporte ao Controle de ações, permitir ações somente leitura ou um
conjunto personalizado aprovado, incluindo a definição de como o workspace lida com ações recém-adicionadas.
- Definir as Permissões de App que determinam quando o ChatGPT solicita confirmação antes de usar um aplicativo.
- Manter o acesso dentro dos escopos e das permissões concedidos por cada serviço
conectado e por cada usuário autenticado.

Para consultar a disponibilidade e os procedimentos atuais, veja
[Controles de administração, segurança e conformidade em aplicativos](https://help.openai.com/en/articles/11509118).

<a id="choose-a-starting-set-of-apps"></a>

## Escolha um conjunto inicial bem definido

Comece com plug-ins que atendam a uma necessidade clara de negócio. Decida se cada plug-in deve
ficar disponível para todos, ser restrito a uma função ou a um grupo piloto ou passar por
uma revisão adicional.

Para cada serviço conectado, registre o responsável na área de negócios, os dados permitidos, as ações de
leitura ou gravação aprovadas, o método de autenticação e um contato para suporte ou remoção.

Antes de ativar ações de gravação ou publicar uma nova capacidade conectada, verifique
o escopo de acesso por função e teste com uma conta que tenha apenas as permissões previstas
no serviço conectado.

Para uma implementação ampla, comece com categorias que as equipes usam no dia a dia, como e-mail,
calendário e sistemas de arquivos ou documentos. Use o
[Diretório de plug-ins](https://chatgpt.com/apps) para confirmar a disponibilidade atual
e as capacidades nas interfaces compatíveis do ChatGPT e do Codex.

Independentemente do conjunto inicial, comece com ações de leitura. Antes de ativar ações
de gravação, identifique o responsável pelo plug-in, revise os escopos do conector e as
permissões do serviço, confirme o acesso aos dados e documente os efeitos externos e um
procedimento de recuperação.

## Entenda o fluxo de dados e a segurança

Quando o ChatGPT usa um aplicativo ou conector incluído em um plug-in, envia uma solicitação
ao serviço conectado e retorna dados ou resultados de ações autorizados pelas
permissões do usuário autenticado nesse serviço.

O ChatGPT trata os dados de aplicativos conectados de duas formas:

- **Sem sincronização:** o ChatGPT processa temporariamente os dados do Chat e da pesquisa aprofundada
  e não os indexa.
- **Com sincronização:** o ChatGPT indexa antecipadamente o conteúdo selecionado dos serviços conectados. Você pode verificar
  na página do plug-in se um aplicativo oferece suporte à sincronização.

O modo altera a forma como o ChatGPT indexa o conteúdo dos serviços conectados; ele não substitui
os controles normais de retenção de conversas. As conversas do ChatGPT que usam aplicativos
continuam disponíveis pela API de Compliance.

As orientações da OpenAI sobre aplicativos documentam a criptografia em trânsito e em repouso, a autorização por usuário, os controles de funções e ações e o acesso restrito à rede para conversas que usam aplicativos. Também informam que, para clientes Business, Enterprise e Edu, as informações acessadas por aplicativos não são usadas para treinar modelos. Quando uma solicitação chega a um serviço conectado, os escopos, a retenção, a residência de dados e as demais políticas desse serviço também se aplicam.

Consulte [segurança e conformidade de aplicativos](https://help.openai.com/en/articles/11509118)
e [aplicativos com sincronização](https://help.openai.com/en/articles/10847137) para obter informações atualizadas sobre
o tratamento de dados. Para servidores MCP configurados localmente no aplicativo
do ChatGPT para desktop, na Codex CLI ou na extensão para IDE, consulte
[configuração do MCP no Codex](/pt-BR/codex/extend/mcp).

## Use procedimentos e referências atualizados

- [Controles administrativos, segurança e conformidade em aplicativos](https://help.openai.com/en/articles/11509118)
- [Apps no ChatGPT](https://help.openai.com/en/articles/11487775)
- [Apps com sincronização](https://help.openai.com/en/articles/10847137)
- [Gerenciar as configurações do workspace](https://help.openai.com/en/articles/8411955)
- [Plug-ins](/pt-BR/codex/plugins)
- [Habilidades e plug-ins](/pt-BR/codex/skills-and-plugins)
- [Criar plugins](https://developers.openai.com/plugins/build/plugins)
- [Guia de implementação para administradores](/pt-BR/codex/enterprise/admin-setup)

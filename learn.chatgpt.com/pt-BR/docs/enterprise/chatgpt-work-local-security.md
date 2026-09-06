<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/chatgpt-work-local-security -->

O ChatGPT Work pode usar arquivos, aplicativos e sessões de navegador aprovados no computador do usuário para concluir tarefas locais. O acesso depende das permissões do workspace, do acesso que o usuário já tem por meio de suas contas, das permissões do sistema operacional, das aprovações de aplicativos e das políticas de dispositivo compatíveis.

Os recursos locais dependem do aplicativo para desktop compatível, do sistema operacional, dos direitos de uso do workspace, das permissões por função, da política do dispositivo e da disponibilização do produto.

## Visão geral da segurança

- As tarefas locais são executadas pelo aplicativo do ChatGPT para desktop. Abrir uma tarefa hospedada na nuvem nesse mesmo aplicativo não a torna local.

- Os controles disponíveis para o Work local e hospedado dependem da configuração do workspace e da etapa de disponibilização.

- O acesso a arquivos, o Uso do computador, os navegadores e os aplicativos conectados usam permissões e aprovações diferentes.

- Um navegador ou aplicativo já conectado a um sistema da empresa pode disponibilizar as permissões dessa conta existente.

- As políticas compatíveis de dispositivos gerenciados podem restringir recursos locais sem substituir os controles de acesso do workspace.

- Os dados de workspaces Business, Enterprise e Edu processados pelos serviços da OpenAI abrangidos são criptografados em trânsito e em repouso e, por padrão, não são usados para treinar modelos da OpenAI.

- Arquivos locais, contexto de tarefas, dados do navegador, registros de sistemas conectados e eventos de auditoria podem seguir regras diferentes de armazenamento e retenção.

## Onde as tarefas locais são executadas

O Work Local acessa recursos aprovados pelo aplicativo para desktop no computador do usuário. O Work na Nuvem é executado em infraestrutura gerenciada pela OpenAI, mesmo quando aberto pelo mesmo aplicativo para desktop.

Os arquivos locais podem permanecer no dispositivo, mas trechos relevantes de arquivos, prompts, capturas de tela, conteúdo do navegador ou resultados de ferramentas podem ser enviados aos serviços da OpenAI para concluir uma tarefa. A execução local não significa que a inferência do modelo ocorra offline ou apenas no dispositivo.

## Arquivos e acesso ao dispositivo

Uma tarefa local pode trabalhar com informações que o usuário fornece ou disponibiliza, incluindo arquivos compatíveis, conteúdo de aplicativos, sessões de navegador e sistemas conectados autorizados. O acesso depende dos privilégios que o usuário já tem e dos controles que regem esse recurso específico.

Conceder acesso ao Work local não aprova automaticamente todos os aplicativos, não concede direitos de administrador nem contorna as permissões da conta usada para acessar outro sistema. Uma conexão compartilhada aprovada pode ter privilégios diferentes dos da conta pessoal do usuário.

## Uso do computador e aprovações de aplicativos

O [Uso do computador](/pt-BR/codex/computer-use) só pode interagir com aplicativos para desktop compatíveis quando o recurso estiver disponível, as permissões necessárias do sistema operacional tiverem sido concedidas e o usuário autorizar o aplicativo. Dependendo das opções disponíveis, a aprovação pode valer para a sessão atual ou para tarefas futuras.

No macOS, Gravação de Tela permite que o Uso do computador veja o conteúdo dos aplicativos, e Acessibilidade permite que ele clique, digite e navegue. As tarefas compatíveis no macOS podem ser executadas em segundo plano. No Windows, o Uso do computador opera na área de trabalho ativa e visível e não pode ser executado em segundo plano enquanto o usuário continua usando a mesma sessão.

Os usuários podem interromper uma tarefa a qualquer momento. O Uso do computador não pode aprovar solicitações de segurança do sistema operacional, autenticar-se como administrador nem automatizar aplicativos de terminal ou o próprio ChatGPT.

### Dispositivos bloqueados

As configurações compatíveis do macOS podem permitir, opcionalmente, que uma tarefa aprovada de Uso do computador continue enquanto o Mac estiver bloqueado. A disponibilidade depende da versão do aplicativo, da disponibilização do recurso, dos requisitos aplicáveis e da elegibilidade para controle remoto.

Os administradores podem desativar a operação com o dispositivo bloqueado por meio das opções compatíveis de configuração gerenciada. No Windows, o Uso do computador exige uma área de trabalho ativa e desbloqueada; o funcionamento com o macOS bloqueado não implica suporte equivalente no Windows.

## Sessões do navegador e contas já conectadas

O Work Local não obtém automaticamente acesso a todos os navegadores ou contas da empresa. O acesso depende do navegador usado, da conta conectada e das aprovações exigidas para essa modalidade de navegação.

| Forma de uso do navegador                                | Sessão e limite de segurança                                                                                                                                                                                                 |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Navegador integrado do aplicativo para desktop](/pt-BR/codex/browser)    | Usa um perfil de navegador separado daquele que o usuário utiliza normalmente. O usuário pode fazer login nesse perfil, e o acesso a sites compatíveis pode exigir aprovação. O navegador integrado não pode automatizar uploads de arquivos.              |
| [Extensão do Chrome](/pt-BR/codex/chrome-extension) | Pode interagir com abas e contas existentes do navegador quando a extensão e o acesso aos sites estiverem aprovados. Os usuários podem aprovar um acesso pontual a um site ou permitir acessos futuros; o acesso ao histórico de navegação e a arquivos locais exige uma revisão separada. |
| Uso do computador para operar um navegador            | Usa um navegador aprovado como aplicativo para desktop, incluindo as contas já conectadas nesse navegador. As permissões do sistema operacional, a aprovação do aplicativo e as permissões da conta existente continuam se aplicando.               |

As opções de aprovação de sites e as confirmações de ações sensíveis variam conforme a modalidade de navegação. Permitir todos os sites reduz as solicitações de aprovação futuras, por isso os usuários devem avaliar essa escolha antes de ativá-la.

Um navegador hospedado na nuvem é separado dos navegadores locais do usuário e não herda automaticamente as sessões já autenticadas nesses navegadores. Os fluxos de trabalho compatíveis na nuvem podem solicitar um login separado, autorizado pelo usuário.

## Apps, plug-ins e contas conectadas

Um aplicativo conectado pode fornecer acesso a informações ou ações em outro sistema. Um plug-in pode usar um aplicativo como ferramenta subjacente. Disponibilizar um plug-in não ativa automaticamente o aplicativo necessário, não autoriza uma conta nem permite todas as ações.

A disponibilidade de plug-ins e aplicativos depende do plano e da configuração do workspace. A [Visão geral do ChatGPT Work](/pt-BR/codex/enterprise/chatgpt-work-overview) informa que os plug-ins e os aplicativos que eles usam ficam desativados por padrão nos workspaces Enterprise e Edu e ativados por padrão nos workspaces Business. Verifique as configurações efetivas para o workspace e a experiência de uso do produto em questão.

Antes que uma tarefa use um sistema conectado, confirme que o workspace permite o aplicativo e todos os plug-ins necessários, que a conexão está autorizada e que a conta conectada pode acessar as informações ou executar a ação solicitada. As configurações de somente leitura, as ações permitidas e os requisitos de confirmação variam conforme a integração.

Plug-ins exclusivos para desktop, ferramentas locais e outros recursos disponibilizados localmente podem seguir processos de instalação ou aprovação diferentes. Não presuma que todas as ferramentas locais usam o mesmo processo de aprovação administrativa.

### Conexões pessoais e compartilhadas

Uma conexão pessoal usa as permissões do usuário conectado no sistema de origem. Uma conexão compartilhada ou pertencente a um agente usa as permissões da conta conectada, que podem permitir um acesso mais amplo do que o do próprio usuário.

Limite as contas compartilhadas aos dados e às ações necessários, restrinja quem pode usá-las e aplique os controles de ação ou confirmação compatíveis. Os registros no sistema conectado continuam sujeitos às permissões e às políticas de retenção desse sistema.

## Acesso de administradores e políticas de dispositivos gerenciados

Revise os controles do Work disponíveis em **Configurações do workspace** \> **Permissões e funções**. A configuração do workspace e a etapa de disponibilização determinam se o Work local e o hospedado aparecem como permissões distintas. Para mais orientações, consulte as [Perguntas frequentes para administradores do Work](/pt-BR/codex/enterprise/work-admin-faq).

Habilite apenas os ambientes de execução aprovados para cada usuário ou grupo e verifique o acesso efetivo após fazer alterações.

As permissões do workspace determinam quem pode usar o Work. Os administradores também podem restringir os recursos compatíveis para desktop por meio de requisitos obrigatórios definidos em `requirements.toml`. Dependendo da implantação, esses requisitos podem ser distribuídos por meio de uma configuração gerenciada pelo workspace, de um arquivo de configuração no nível do sistema ou de ferramentas compatíveis de gerenciamento de dispositivos móveis para macOS.

Os requisitos obrigatórios não podem ser substituídos por usuários individuais. Já os valores padrão gerenciados estabelecem configurações iniciais que os usuários podem ter permissão para alterar. Nenhum dos dois substitui as funções do workspace ou as permissões do sistema operacional.

| Configuração gerenciada                                       | Finalidade de segurança                                                             |
| ----------------------------------------------------- | ---------------------------------------------------------------------------- |
| `features.computer_use = false`                       | Desativar os recursos compatíveis do Uso do computador.                                 |
| `allow_appshots = false`                              | Impedir a captura de Appshot quando houver suporte.                                           |
| `features.in_app_browser = false`                     | Desativar o navegador integrado do aplicativo para desktop.                                  |
| `features.browser_use = false`                        | Desativar os recursos compatíveis de automação de navegador; revisar separadamente outras formas de uso do navegador. |
| `features.apps = false` ou `features.plugins = false` | Restringir aplicativos conectados ou plug-ins compatíveis.                        |
| `computer_use.allow_locked_computer_use = false`      | Impedir o Uso do computador enquanto um Mac estiver bloqueado, nos casos em que há suporte.                        |

As configurações e os métodos de distribuição disponíveis dependem do cliente, do sistema operacional, do workspace e da configuração de implantação. Valide as restrições em um dispositivo gerenciado representativo. Para ver as configurações de políticas compatíveis, exemplos de configuração e instruções para configurar o MDM, consulte [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration).

## Conectividade local e recursos privados

Uma tarefa pode acessar informações da empresa por meios como um navegador no dispositivo, um aplicativo para desktop aprovado ou um aplicativo conectado. Os controles existentes de dispositivo, proxy, VPN, sistema de origem e endpoint podem se aplicar de formas diferentes a cada um desses meios.

O acesso a uma VPN corporativa não autoriza automaticamente todas as ferramentas a usar todos os recursos internos. Da mesma forma, um navegador do Work na nuvem ou um controle de rede da nuvem não impõe uma restrição universal à conectividade de rede do dispositivo local. Avalie a conexão, a identidade, o destino e a ação efetivamente exigidos pelo fluxo de trabalho.

## Tratamento e retenção de dados

Aplique os controles de endpoint, acesso a arquivos, proxy e prevenção de perda de dados da sua organização ao dispositivo e ao fluxo de trabalho específicos. Confirme se esses controles podem impedir que informações sensíveis sejam incluídas na tarefa antes do processamento. Logs de auditoria e exportações de conformidade ajudam no monitoramento e na investigação, mas não bloqueiam o processamento por conta própria.

O armazenamento e a retenção dependem da categoria da informação e de onde ela é salva.

| Categoria da informação                            | O que revisar                                                                                                                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Registros de conversas locais                      | Como os registros locais são armazenados, excluídos, incluídos em backups ou compartilhados no aplicativo para desktop. Não presuma que as configurações de retenção de conversas hospedadas se apliquem a todos os artefatos locais. |
| Arquivos locais e resultados gerados               | Armazenamento do dispositivo, política de endpoint, uploads autorizados pelo usuário, compartilhamento externo e quaisquer cópias salvas separadamente.                                                       |
| Prompts, trechos de arquivos e contexto dos aplicativos | Conteúdo fornecido a um modelo ou serviço, termos aplicáveis ao workspace e como os dados de fato circulam no fluxo de trabalho.                                                           |
| Voz e Capturas do app                              | Áudio captado pelo microfone, capturas de tela da janela em primeiro plano, texto acessível dos aplicativos, armazenamento local de sessões e qualquer conteúdo enviado como contexto da tarefa.                          |
| Dados do navegador                                    | O perfil do navegador utilizado, as sessões já autenticadas, o histórico de navegação, os downloads, as aprovações de acesso a sites e qualquer conteúdo da tarefa armazenado separadamente.                           |
| Registros de sistemas conectados                        | Permissões e retenção no sistema de origem, identidade da conta conectada e quaisquer informações salvas separadamente na conversa ou em outro destino.              |
| Registros de conformidade e atividade                 | Quais eventos do Work Local estão disponíveis para o workspace, a integração com suporte e a política de retenção do sistema que recebe os dados.                                   |

Nos workspaces Business, Enterprise e Edu com suporte, os dados empresariais processados pelos serviços da OpenAI abrangidos são criptografados em trânsito e em repouso e, por padrão, não são usados para treinar ou aprimorar os modelos da OpenAI. Essas proteções não significam que a OpenAI controle todos os arquivos do dispositivo, aplicativos de terceiros, perfis de navegador ou registros dos sistemas de origem.

Não aplique aos registros locais um prazo de retenção de conversas hospedadas, uploads temporários ou logs de conformidade sem confirmar que ele se aplica à categoria específica de dados.

## Visibilidade para auditoria e conformidade

Os relatórios disponíveis dependem do plano do workspace, da experiência de uso do produto, do evento, do aplicativo conectado e da configuração implantada. Verifique a cobertura do Work Local antes de se basear em uma exportação do workspace para resposta a incidentes ou revisão regulatória.

Verifique se os sistemas relevantes registram a identidade da tarefa, os prompts e as respostas com suporte, as chamadas a aplicativos conectados, as aprovações relacionadas ao navegador, as ações em aplicativos, as atividades em arquivos locais ou os eventos de endpoint. Os registros do sistema de origem e do dispositivo podem oferecer uma visibilidade diferente da oferecida pelos registros do workspace do ChatGPT.

A OpenAI não armazena um registro separado e completo das ações realizadas no Chrome por meio da extensão. Não presuma que todas as operações em arquivos locais, capturas de tela, ações no navegador, aprovações ou atualizações externas apareçam na API de Compliance.

## Comece com uma tarefa aprovada

Comece com um pequeno grupo que use dispositivos gerenciados e escolha uma tarefa aprovada, como comparar pastas de trabalho financeiras selecionadas. Confirme o acesso de cada usuário ao Work e disponibilize apenas os arquivos, aplicativos, sessões de navegador ou contas conectadas de que a tarefa precisa.

Verifique se as ações aprovadas funcionam, se as ações restritas são bloqueadas e se os registros disponíveis atendem às suas necessidades de monitoramento. Peça a um usuário que revise os resultados e quaisquer alterações externas antes de ampliar o acesso.

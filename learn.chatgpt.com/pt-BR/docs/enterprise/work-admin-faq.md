<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/work-admin-faq -->

O ChatGPT Work leva a tecnologia por trás do Codex ao ChatGPT para tarefas mais longas,
com várias etapas. Ele pode reunir contexto de chats, arquivos, recursos do
workspace e sistemas conectados; usar ferramentas aprovadas; e criar resultados
prontos para revisão. O acesso, o contexto, as ações, o comportamento da rede e o uso de créditos variam conforme o
plano, as configurações do workspace, as permissões das fontes e a interface.

## Visão geral

O ChatGPT Work permite que os usuários deleguem ao ChatGPT tarefas mais longas e com várias etapas. Ele pode reunir
informações de fontes conectadas, raciocinar ao longo das etapas, criar documentos,
apresentações ou análises e devolver resultados para revisão.

O ChatGPT Work está disponível nas interfaces Web, móveis e de desktop compatíveis para
planos e workspaces elegíveis. Quando há suporte, os proprietários do workspace ou os administradores
autorizados podem gerenciar o Work na nuvem, o Work Local e o Codex Local por meio de permissões
distintas. Nos workspaces Enterprise e Edu elegíveis, a função padrão do workspace
inclui o Work, a menos que um administrador autorizado o desative. Os controles de navegador e
rede impõem outras restrições ao Work na nuvem, e a disponibilidade depende da função,
do plano, do workspace e da região. Consulte
[ChatGPT Work e Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

Estas perguntas frequentes explicam como os administradores gerenciam o ChatGPT Work: controles de acesso e dados,
conformidade e visibilidade, uso e gastos, resposta a incidentes e práticas de
implementação. Para entender o modelo de execução hospedada e os limites de segurança, consulte
[Visão geral do ChatGPT Work](/pt-BR/codex/enterprise/chatgpt-work-overview).

## Principais controles administrativos

Os administradores gerenciam o ChatGPT Work por meio destas camadas de controle:

- **Acesso ao workspace empresarial:** os controles de identidade e acesso gerenciam
  a autenticação e o acesso ao workspace. Dependendo do plano e da
  configuração, os recursos de identidade controlados pelos administradores podem incluir SSO,
  verificação de domínio, provisionamento SCIM, gerenciamento do ciclo de vida dos usuários e
  sincronização de grupos de identidade. O SCIM e os grupos de identidade sincronizados não estão
  incluídos no ChatGPT Business. Os usuários podem ativar a MFA da OpenAI no nível da conta.
  O ChatGPT não oferece um mecanismo para exigir MFA em todo o workspace; organizações que
  exigem essa proteção devem exigir SSO e MFA por meio do provedor de identidade. Gerencie o
  SSO e as configurações de identidade relacionadas no
[Console de administração global](https://help.openai.com/en/articles/12289294-admin-portal).
  Consulte [Autenticação multifator](https://help.openai.com/en/articles/7967234-enabling-or-disabling-multi-factor-authentication-mfa).
- **Acesso ao ChatGPT Work dentro do workspace:** quando disponível, o Work na nuvem
  controla o Work hospedado nas interfaces Web, móveis e de desktop compatíveis.
  O Work Local controla o Work local no desktop, enquanto o Codex Local controla o acesso local
  ao Codex em clientes compatíveis de desktop, CLI e IDE. As configurações de navegador e rede
  na nuvem restringem ainda mais o Work na nuvem. O controle de acesso baseado em funções (RBAC)
  personalizado e as permissões disponíveis dependem do plano e do workspace.
- **Associação a grupos:** nos planos que oferecem suporte ao SCIM, sincronize os grupos por meio de
  um provedor de identidade para que o acesso seja atualizado quando funcionários entram na organização,
  mudam de função ou saem dela. Consulte
[Grupos e provisionamento](/pt-BR/codex/enterprise/groups-and-provisioning).
- **Funções do workspace e dos membros:** as funções integradas do Enterprise incluem Proprietário,
  Administrador, Membro e Visualizador de análises. Nos planos compatíveis, funções personalizadas e o
  RBAC de membros controlam o acesso ao ChatGPT Work, a plug-ins e a outras capacidades.
  Quando há tipos de licença, os membros também precisam de uma licença que inclua o ChatGPT; uma
  licença exclusiva do Codex não concede acesso ao Work. Consulte
[Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions).
- **Plug-ins e aplicativos:** a política de plug-ins rege a disponibilidade e a
  instalação de plug-ins. O acesso a aplicativos, os controles de ações e o comportamento das aprovações são
  configurados separadamente. Os Agentes do workspace têm controles próprios quando
  disponíveis. Consulte [Controles de plug-ins](/pt-BR/codex/enterprise/apps-and-connectors),
[Plug-ins](/pt-BR/codex/plugins) e o
[documento técnico de segurança de aplicativos](https://cdn.openai.com/business-guides-and-resources/app-security-whitepaper.pdf).
- **Permissões dos sistemas de origem:** um usuário só pode acessar o conteúdo e as ações
  permitidos pela conta ou pela conexão compartilhada no aplicativo nativo. Consulte
[Controles administrativos, segurança e conformidade em aplicativos](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business).
- **Aprovação e restrições de ações:** para aplicativos que oferecem suporte ao Controle de ações,
  os administradores podem permitir todas as ações, ações somente leitura ou um conjunto personalizado e decidir
  como lidar com ações recém-adicionadas. As permissões dos aplicativos determinam separadamente
  quando o ChatGPT pede confirmação antes de usar um aplicativo.
- **Créditos:** o ChatGPT Work e o Codex compartilham preços, créditos e limites de uso.
  Administradores elegíveis dos planos Enterprise e Edu podem definir limites mensais por usuário por meio de um
  limite padrão do workspace, limites padrão de grupos e exceções individuais. Os usuários podem
  solicitar aumentos quando isso for permitido pelo workspace. O Business adota um modelo separado
  de créditos e controle de gastos. Consulte
[Limites de uso e controles de gastos do ChatGPT](/pt-BR/codex/enterprise/usage-limits).
- **Análises e relatórios:** o Console de administração global e as análises do workspace
  permitem analisar a adoção e o uso de créditos. Use a API de Compliance e as interfaces de
  relatórios do Codex de acordo com os escopos documentados de eventos e produtos; consulte os
  esquemas atuais antes de prometer cobertura para determinados prompts, arquivos,
  aprovações, ações, erros ou chamadas de ferramentas. Consulte
[Governança](/pt-BR/codex/enterprise/governance).

## Acesso, dados, sistemas e ações dos usuários

### Como são protegidos o acesso a dados e sistemas e as ações dos usuários?

O ChatGPT Work é regido pelos controles de identidade, acesso e permissões já
estabelecidos no seu workspace do ChatGPT. Os administradores usam o gerenciamento de identidade,
as funções do workspace e, nos planos elegíveis, o
[RBAC](https://help.openai.com/en/articles/11750701-rbac) para determinar quem pode
usar o ChatGPT Work.

Quando há suporte, o acesso pode ser sincronizado com seu provedor de identidade por meio do
[SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
e da sincronização de grupos. Isso permite gerenciar o acesso e as permissões de forma centralizada
quando funcionários entram na organização, mudam de função ou saem dela.

Os sistemas de origem aplicam as permissões da conta ou da conexão
compartilhada aprovada usada na operação. Uma conexão individual usa o acesso dessa
pessoa ao sistema de origem. Uma conexão pertencente a um agente ou compartilhada pode conceder
a usuários autorizados do agente acesso por meio da conta conectada, inclusive a dados ou
ações que a própria conta deles não poderia acessar. Restrinja os escopos da conexão,
as ações disponíveis e o público do agente ao necessário para a finalidade de negócio prevista. Consulte
[Conexões e permissões dos Agentes do workspace](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business).

<a id="how-does-work-access-data-and-context"></a>
<a id="how-does-work-mode-access-data-and-context"></a>

### Como o ChatGPT Work acessa dados e contexto?

O ChatGPT Work pode usar o chat atual, arquivos enviados, recursos do workspace e
sistemas conectados por meio de aplicativos aprovados e, quando aplicável, plug-ins.
Dependendo das capacidades e permissões ativadas, isso pode incluir documentos,
repositórios, tickets, canais, e-mails e calendários. Arquivos anteriores podem estar
disponíveis no chat atual, em projetos compatíveis, por meio do acesso autorizado à Biblioteca
ou de referências automáticas à Biblioteca, quando ativadas. As memórias salvas seguem seus
próprios controles do workspace e do usuário.

Cada fonte de contexto mantém seus próprios controles: os usuários fornecem o contexto do chat,
os administradores gerenciam os recursos do workspace, e os sistemas conectados aplicam os controles de autenticação
e permissões. O ChatGPT Work só pode acessar informações autorizadas para o usuário ou para uma
conexão compartilhada aprovada.

O ChatGPT Work herda as proteções aplicáveis do workspace do ChatGPT. A residência, a retenção,
o registro de logs e a disponibilidade de recursos variam conforme o plano, a região, a interface e o sistema
conectado; portanto, verifique a cobertura da sua configuração.

### Quais ações de alto impacto são restritas ou exigem revisão?

O risco depende da ação. Ler ou criar rascunhos geralmente tem menos impacto do que alterar
dados, compartilhar informações ou atuar em sistemas externos. Combine funções, permissões
e credenciais de escopo restrito e os mecanismos de aprovação disponíveis para limitar ações de maior
impacto a usos confiáveis e revisados.

Entre as categorias comuns de ações estão:

- **Leitura:** acessar, pesquisar ou resumir informações de fontes aprovadas
  sem alterar os dados subjacentes.
- **Rascunho:** preparar documentos, e-mails, relatórios, código ou outro conteúdo para uma
  pessoa revisar antes do uso.
- **Gravação:** criar, atualizar ou excluir registros em sistemas conectados, como
  documentos, tickets, repositórios ou ferramentas de gerenciamento de projetos.
- **Compartilhamento:** enviar, publicar ou disponibilizar informações de outra forma para mais
  pessoas, sistemas ou destinos externos.
- **Agendamento:** iniciar uma tarefa em um horário futuro ou de forma recorrente
  sem exigir que um usuário inicie cada execução.
- **Execução:** executar código, comandos do shell, automação do navegador ou outras
  tarefas realizadas por ferramentas que interagem diretamente com ambientes externos.

Para ações de maior impacto, use revisão humana, credenciais restritas, escopos
delimitados e os mecanismos de aprovação disponíveis. As ações de plug-ins continuam sujeitas às
permissões e aos controles de segurança de cada integração.

## Conformidade

<a id="how-does-work-support-enterprise-privacy-and-data-commitments"></a>
<a id="how-does-work-mode-support-enterprise-privacy-and-data-commitments"></a>

### Como o ChatGPT Work oferece suporte aos compromissos empresariais de privacidade e dados?

O ChatGPT Work adota os compromissos de privacidade, segurança e dados aplicáveis ao
workspace do ChatGPT do cliente, de acordo com o plano, a configuração, a interface, o recurso
e a região. Para o ChatGPT Enterprise, isso inclui
[não usar dados empresariais para treinamento por padrão](https://help.openai.com/en/articles/8983130-what-if-i-want-to-keep-my-history-on-but-disable-model-training),
criptografia em trânsito e em repouso, controles de acesso no nível do workspace e
os recursos disponíveis de registro de auditoria.

A cobertura de residência de dados, residência de inferência, HIPAA ou um Contrato de
Associado Comercial não é universal. Confirme as
[orientações atuais sobre residência de dados e inferência](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)
e o contrato do cliente para os recursos e as regiões em uso.

Os serviços conectados têm requisitos próprios de retenção, registro de logs, acesso, residência e
conformidade. Quando o ChatGPT Work usa plug-ins, repositórios ou sistemas de terceiros,
avalie tanto os controles do workspace do ChatGPT quanto os do sistema
conectado.

Para atividades do Codex, os controles empresariais podem abranger ambientes de desenvolvimento,
repositórios, ferramentas configuradas e atividades relacionadas. Consulte o
[Guia de implementação para administradores](/pt-BR/codex/enterprise/admin-setup) e a página de
[Governança](/pt-BR/codex/enterprise/governance) ao revisar os controles do workspace.

### Quais dados são armazenados, retidos ou excluídos?

A retenção e a exclusão de dados do ChatGPT Work são determinadas pelo plano do workspace do ChatGPT,
pelas configurações administrativas e pelas capacidades em uso. A retenção pode variar
conforme as informações acessadas pelo ChatGPT Work. As conversas e os arquivos elegíveis da Biblioteca
seguem as configurações aplicáveis do workspace. Arquivos de projetos, uploads
temporários, memórias salvas, eventos de conformidade, dados sincronizados de aplicativos e
registros de terceiros podem ter regras próprias de retenção e exclusão. Consulte
[Políticas de retenção de chats e arquivos](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt).

O ChatGPT Work pode criar conteúdo de chat, arquivos enviados ou gerados, artefatos
e metadados de execução. Os chats do Codex também podem criar metadados de repositório ou ambiente,
saídas de comandos, diffs e logs. Consulte a documentação atual do produto e da
[API de Compliance](/pt-BR/codex/enterprise/compliance-api) para conferir as classes exatas de dados,
os períodos de retenção e os procedimentos de exclusão.

Analise os requisitos de retenção tanto no workspace do ChatGPT quanto nos sistemas empresariais
conectados para que as políticas de governança de dados, conformidade e
retenção de registros da sua organização sejam aplicadas a cada sistema.

## Observabilidade

### Quais dados de uso estão disponíveis para administradores ou proprietários?

Administradores e proprietários podem usar análises de produtos e logs de conformidade para obter diferentes
tipos de visibilidade. O Console de administração global oferece visualizações de adoção e uso de créditos do ChatGPT e do
Codex, conforme o suporte disponível; os detalhamentos disponíveis por usuário, produto, agente e modelo
dependem da interface de análise e do workspace. Para workspaces
elegíveis, a API de Compliance fornece os registros de conversas do ChatGPT contemplados,
incluindo atividades do Work na nuvem para as quais há suporte. A cobertura depende do produto,
da interface, das permissões, do endpoint disponível e do esquema de eventos documentado. Consulte
[Análises do workspace](/pt-BR/codex/enterprise/workspace-analytics) e a
[API de Compliance](/pt-BR/codex/enterprise/compliance-api).

### Os prompts, resultados, arquivos, ações ou chamadas de ferramentas são registrados?

Para workspaces Enterprise e Edu elegíveis, a Plataforma de logs de conformidade
fornece os prompts dos usuários do Work e as respostas dos agentes.
[As chamadas a aplicativos conectados são registradas separadamente](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business),
e workspaces elegíveis podem acessar arquivos ativos da Biblioteca por meio dos
[endpoints disponíveis da API de Compliance específicos para a Biblioteca](https://help.openai.com/en/articles/20001052-library-for-chatgpt).
Esses registros não constituem uma trilha de auditoria completa para cada operação com arquivos no ambiente hospedado,
comando do shell, interação com o navegador, chamada de ferramenta ou aprovação.
Confirme a cobertura atual de eventos e produtos na documentação da API de Compliance
que exige autenticação.

A Plataforma de logs de conformidade retém os dados por 30 dias. Exporte os registros
continuamente para um sistema aprovado de descoberta eletrônica, prevenção contra perda de dados, SIEM
ou data lake quando sua organização exigir uma retenção mais longa. Consulte o
[guia da Plataforma de conformidade da OpenAI](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

### Comportamentos incomuns, falhas ou picos de uso podem ser detectados rapidamente?

As análises do workspace, os logs de conformidade e as ferramentas de monitoramento conectadas ajudam
os administradores a analisar o uso e investigar atividades do ChatGPT, do Work e do Codex
para as quais há suporte. Dependendo da interface de relatórios selecionada, os sinais podem incluir
usuários ativos, mensagens contempladas, atividades de aplicativos, uso de agentes, eventos de autenticação ou
administrativos e consumo de créditos. Os logs exportados podem dar suporte à
descoberta eletrônica, à prevenção contra perda de dados, a SIEM, à auditoria e a investigações.
A qualidade da detecção depende do plano, da cobertura de eventos, da atribuição, da atualidade dos dados e
das regras configuradas.

Entre os sinais que podem justificar uma revisão estão aumentos inesperados no uso ou no consumo de
créditos, atividades incomuns de usuários ou agentes, erros operacionais recorrentes e
eventos relevantes de autenticação ou administração. Verifique quais são exatamente esses sinais
nos esquemas aplicáveis de análise, conformidade e logs de auditoria.

Para atividades do Codex, as análises do Codex e a Analytics API fornecem métricas de adoção e atividade
para as quais há suporte. Organizações que usam clientes locais do Codex podem optar
por exportações via OpenTelemetry de eventos como solicitações de API, erros, metadados
de prompts, decisões de aprovação de ferramentas e resultados de ferramentas. O conteúdo dos prompts é
ocultado, a menos que `otel.log_user_prompt = true` seja ativado explicitamente
e de forma separada. Consulte
[Monitoramento e telemetria](/pt-BR/codex/agent-approvals-security#monitoring-and-telemetry).
Essa telemetria local do Codex não oferece exportação via OpenTelemetry para
o ChatGPT Work na Web.

## Governança

### Como os administradores podem controlar o acesso, as permissões e as políticas?

A governança abrange três camadas relacionadas, porém distintas:

- **Os controles de acesso do ChatGPT Work** determinam quem pode usar o ChatGPT Work em
  cada interface.
- **Os controles dos Agentes do workspace** determinam quem pode criar, publicar, compartilhar,
  agendar ou configurar agentes reutilizáveis e conexões compartilhadas, quando os
  Agentes do workspace estão disponíveis.
- **A configuração gerenciada do Codex** rege o comportamento do ambiente de execução local do Codex ao qual se aplica
  e não configura o ChatGPT Work hospedado.

A configuração gerenciada restringe o comportamento de execução para o qual há suporte. Ela não concede
acesso ao workspace, não substitui o RBAC nem revoga o acesso de um usuário ao workspace. Essas
camadas não formam uma única interface uniforme de políticas do ChatGPT Work. As análises e os logs de conformidade
oferecem visibilidade adicional dentro dos escopos documentados de produtos e
eventos.

Nos clientes locais compatíveis do Codex, os administradores empresariais podem aplicar
[configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration) e
[perfis de permissão](/pt-BR/codex/permissions). Esses controles dos clientes locais não
concedem acesso ao ChatGPT Work hospedado nem substituem as permissões do workspace para esse serviço.

### É possível definir o escopo de acesso por grupo, função, workspace ou capacidade?

Sim. Nos planos Enterprise e Edu elegíveis com suporte a RBAC personalizado para membros,
é possível definir o escopo das capacidades do ChatGPT Work com funções do workspace, grupos de identidade
e permissões definidas pelos administradores. O ChatGPT Business usa os controles aplicáveis
no nível do workspace, mas não inclui RBAC personalizado para membros nem sincronização
de grupos por SCIM. Atribua as capacidades compatíveis conforme as necessidades do negócio
e a política organizacional. Consulte o
[guia de RBAC](https://help.openai.com/en/articles/11750701-rbac) e este
[passo a passo de RBAC](https://vimeo.com/1207482321/d1286e4467?share=copy&fl=sv&fe=ci).

Quando o RBAC personalizado está disponível, as organizações podem usá-lo para determinar quais
usuários podem acessar o ChatGPT Work, gerenciar configurações do workspace, configurar
plug-ins aprovados ou usar recursos compatíveis dos Agentes do workspace. Nos workspaces Enterprise e
Edu elegíveis, os limites mensais de uso podem viabilizar uma implantação em fases por meio de um
limite padrão para o workspace, limites padrão por grupo e exceções por usuário.

O acesso aos sistemas conectados continua sendo controlado de forma independente. Restrinja o acesso a plug-ins,
credenciais compartilhadas, repositórios e ações com capacidade de gravação ao público estritamente
necessário, usando as permissões do workspace, as configurações dos plug-ins e os controles do
sistema de origem. Nos clientes locais compatíveis do Codex, a configuração gerenciada pode
restringir ainda mais as capacidades do ambiente de execução local. O Work hospedado segue seus próprios
controles de workspace e específicos do produto.

### Como são gerenciados os limites do ambiente de execução e da rede?

Os limites de segurança do ChatGPT Work dependem da tarefa. Uma conversa padrão no Chat, um
fluxo de trabalho conectado, uma tarefa agendada e um chat do Codex podem ser executados em
ambientes diferentes, com permissões, ferramentas e acesso à rede distintos.

Gerencie cada ambiente de execução com os controles aplicáveis. O Work na nuvem
controla o Work hospedado nas interfaces web, móveis e para desktop compatíveis. O Work
Local controla o Work local para desktop, e o Codex Local controla o acesso local
compatível ao Codex nos clientes para desktop, CLI e IDE. As permissões de rede do navegador e do shell
restringem ainda mais o Work na nuvem. Pesquisa, aplicativos, plug-ins, Agentes do workspace
disponíveis e permissões dos sistemas de origem continuam sendo controles separados.
A configuração gerenciada e as políticas de execução local aplicáveis controlam apenas
as experiências locais compatíveis. Esses controles não são intercambiáveis.

Nas atividades do Codex, as execuções locais no aplicativo do ChatGPT para desktop, na CLI e na IDE ocorrem
na máquina do usuário, em ambiente isolado pelo sistema operacional e com políticas de aprovação.
O Codex Cloud executa chats em ambientes isolados gerenciados pela OpenAI. Nos clientes
locais compatíveis, os administradores empresariais podem usar requisitos gerenciados para
restringir perfis de permissão, aprovações, acesso ao sistema de arquivos e à rede, servidores MCP,
hooks, regras de comandos e outros comportamentos compatíveis do ambiente de execução.

## Uso e custo

<a id="how-does-work-usage-translate-into-spend-over-time"></a>
<a id="how-does-work-mode-usage-translate-into-spend-over-time"></a>

### Como o uso do ChatGPT Work se reflete nos gastos ao longo do tempo?

[O ChatGPT Work e o Codex compartilham preços, créditos e limites de uso](/pt-BR/codex/pricing).
Nos contratos elegíveis baseados em créditos, compare o uso combinado de Chat e Work pelos funcionários
com a cota compartilhada de créditos do workspace. O consumo varia conforme
o modelo, as configurações de raciocínio ou velocidade aplicáveis, a entrada e a saída processadas
e as ferramentas ou os recursos elegíveis.

Usar os créditos contratados não aumenta automaticamente o valor da fatura. Os valores
cobrados dependem do saldo restante de créditos, das tarifas contratadas, da elegibilidade da conta
para uso excedente e do limite de excedente configurado para o workspace. Para exemplos
de planejamento, limites efetivos dos usuários, escopo dos relatórios e detalhes de cobrança,
consulte [ChatGPT Work: uso e custo](/pt-BR/codex/enterprise/chatgpt-work-usage-and-cost).

Os padrões com maior variação de custo costumam ser fluxos de trabalho executados com frequência,
que recuperam ou processam grandes volumes de informações, chamam várias ferramentas ou aplicativos,
repetem tentativas após falhas ou produzem artefatos grandes. Exemplos que exigem atenção aos custos
incluem tarefas agendadas ou recorrentes, arquivos grandes, buscas amplas
em fontes empresariais, chamadas repetidas a aplicativos e chats do Codex que
processam repositórios, executam comandos ou usam ambientes de nuvem. Os gatilhos da API de Agentes
do workspace também podem aumentar o uso quando disponíveis.

Use controles de gastos, análises de uso e relatórios para monitorar esses padrões
ao longo do tempo. Analise o uso pelas dimensões disponíveis na interface atual de análise
e ajuste os limites ou o escopo da implantação conforme o valor para o negócio. Não trate
análises agregadas como uma atribuição exata de custos por fluxo de trabalho.

As análises do workspace, os logs de conformidade e as ferramentas de monitoramento conectadas podem ajudar
os administradores a analisar o uso e investigar as atividades abrangidas. A capacidade de
detectar comportamentos arriscados ou incomuns depende do plano, da cobertura dos logs, da atribuição,
da atualidade dos dados e das regras configuradas nos sistemas de monitoramento.

### Quais limites de uso, alertas ou tetos estão disponíveis?

Os workspaces Enterprise e Edu elegíveis podem usar limites mensais por usuário e
controles de gastos para todo o workspace no uso baseado em créditos:

- **Monitore o consumo de créditos:** Analise os relatórios de uso de créditos disponíveis no
  Console de administração global e nas configurações do workspace.
- **Defina um limite mensal padrão:** Estabeleça um limite padrão de créditos por usuário
  para o workspace.
- **Aplique limites específicos por grupo:** Atribua aos grupos limites mensais padrão por usuário que
  reflitam seus fluxos de trabalho, responsabilidades ou estágio de implantação.
- **Crie exceções por usuário:** Atribua um limite diferente a um usuário específico sem
  alterar o padrão para todo o grupo.
- **Analise as solicitações de aumento:** Se as solicitações estiverem habilitadas, os usuários poderão solicitar um
  limite mensal maior. A aprovação cria uma exceção para o usuário.
- **Controle a exposição financeira total do workspace:** Configure separadamente os alertas de créditos do workspace e
  o limite de excedente no Console de administração global. Os alertas notificam os
  destinatários; o limite de excedente controla o uso elegível depois que o saldo de
  créditos contratados se esgota.
- **Exporte os dados de uso:** Os administradores Enterprise elegíveis podem acessar
  dados de uso de créditos pela Cost API unificada para gerar relatórios internos ou
  realizar monitoramento.

Os usuários podem consultar o próprio uso e, se essa opção estiver habilitada, solicitar mais créditos, mas
não podem alterar os limites atribuídos. Consulte
[Gerenciar limites de uso e excedentes](https://help.openai.com/en/articles/20001001-manage-usage-limits-and-overages-in-chatgpt-enterprise-and-edu)
e o
[passo a passo dos controles de gastos](https://vimeo.com/1207484127/0f2029dd01?share=copy&fl=sv&fe=ci).

## Controles de incidentes e revogação

### Como os administradores podem interromper o acesso ou a atividade?

Durante a remoção de um usuário ou a análise de um incidente, os administradores podem precisar interromper o acesso,
desativar aplicativos, revogar credenciais compartilhadas, pausar tarefas agendadas ou revogar credenciais
do Codex.

As formas de revogação incluem:

- Remova o acesso de um usuário ao workspace ou ao grupo. Para usuários gerenciados por SCIM, remova
o acesso no provedor de identidade; caso contrário, uma sincronização posterior poderá
provisionar o usuário novamente.
- Desative ou restrinja o plug-in ou aplicativo em questão.
- Revogue uma conexão compartilhada, um bot ou uma conta de serviço pela respectiva
interface de gerenciamento. Proprietários e administradores do workspace podem revogar separadamente os tokens de
acesso ao workspace do Codex.
- Cancele a publicação de um Agente do workspace ou exclua-o por meio do proprietário do agente
ou de um administrador do workspace.
- Desative a tarefa agendada correspondente ou, quando disponível, o gatilho da API de Agentes
do workspace.
- Para o acesso ao Codex, revogue separadamente o token de acesso correspondente, a conexão com o repositório
e o acesso ao ambiente de nuvem. A configuração gerenciada não é um
mecanismo de revogação de acesso.

## Recursos adicionais para suas equipes

| Tópico                    | Use este recurso para explicar                                                      | Página Aprender do ChatGPT                                               |
| ------------------------ | ----------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Visão geral do Work            | Como funcionam a execução na nuvem, o acesso ao navegador, a política de rede e os limites de dados | [Visão geral do ChatGPT Work](/pt-BR/codex/enterprise/chatgpt-work-overview) |
| Configuração do workspace e RBAC | Quem pode usar e administrar o Codex                                              | [Guia de implementação para administradores](/pt-BR/codex/enterprise/admin-setup)             |
| Autenticação           | Diferenças entre o login com o ChatGPT, o login com chave de API e a política do workspace             | [Autenticação](/pt-BR/codex/auth)                                    |
| Aprovações e ambiente isolado | Como o Codex controla ações relacionadas a arquivos, comandos e rede, além de ações de ferramentas com efeitos colaterais    | [Aprovações e segurança de agentes](/pt-BR/codex/agent-approvals-security)  |
| Política gerenciada           | Como os administradores impõem configurações do Codex que os usuários não podem substituir                        | [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration) |
| Ambientes de execução     | Como funcionam a configuração do Codex Cloud, os segredos, os caches e as fases das tarefas                  | [Ambientes de nuvem](/pt-BR/codex/environments/cloud-environment)      |
| Acesso à internet          | Como funcionam as listas de domínios permitidos e os métodos HTTP do Codex Cloud                       | [Acesso do agente à internet](/pt-BR/codex/cloud/internet-access)            |
| Permissões              | Como funcionam os controles de sistema de arquivos, de rede e de bloqueio de leitura                          | [Permissões](/pt-BR/codex/permissions)                                |
| Observabilidade            | Como funcionam as análises, os relatórios e as exportações de conformidade                         | [Governança](/pt-BR/codex/enterprise/governance)                       |
| Credenciais de automação   | Como os tokens de acesso são criados, limitados, revogados e auditados                  | [Tokens de acesso](/pt-BR/codex/enterprise/access-tokens)                 |

## Ações recomendadas para administradores

- **Confirme quem deve ter acesso primeiro.** Decida se deve restringir o acesso ao
  ChatGPT Work, realizar um projeto-piloto ou disponibilizá-lo amplamente. Muitas organizações começam
  com usuários avançados, multiplicadores ou equipes com casos de uso bem definidos.
- **Revise as funções e permissões.** Em **Permissões e funções**, confirme quais
  usuários ou grupos podem acessar o ChatGPT Work. Alinhe o acesso às necessidades da empresa, ao nível de preparo
  e às expectativas de governança.
- **Revise os plug-ins e as fontes de dados.** O ChatGPT Work é mais útil com contexto empresarial
  aprovado, como arquivos, e-mails, calendários, Slack ou CRM. Revise os
  plug-ins habilitados, quem pode usá-los e se as políticas de aplicativos continuam alinhadas à forma como os usuários
  devem delegar trabalho.
- **Defina expectativas sobre os casos de uso adequados.** Oriente o uso do ChatGPT Work para tarefas que envolvem várias etapas
  e geram mais valor, como pesquisa, síntese, análise, criação de arquivos,
  atualizações de fluxos de trabalho e resultados reutilizáveis. Use o Chat para perguntas rápidas,
  pequenas reformulações ou exploração de ideias.
- **Revise os controles de créditos e de uso.** Como o ChatGPT Work pode executar
  tarefas de maior duração, ele pode consumir mais créditos do que uma conversa padrão no Chat. Revise
  as configurações padrão gerais e por grupo, as exceções por usuário e as orientações internas sobre
  como adequar o esforço ao valor para a empresa.
- **Identifique seus primeiros fluxos de trabalho de alto valor.** Comece com resultados claros e que possam ser revisados,
  como informes sobre clientes, relatórios recorrentes, sínteses de pesquisas,
  atualizações em ferramentas de acompanhamento ou documentos e slides bem elaborados.
- **Prepare os multiplicadores e as equipes de suporte.** Forneça primeiro aos multiplicadores, aos responsáveis por treinamento
  e às equipes de suporte os recursos para a implantação, para que possam responder a perguntas,
  coletar feedback e mostrar como delegar tarefas de forma eficaz.
- **Comunique o que se espera quanto à revisão e à aprovação.** Lembre os usuários de que as pessoas
  continuam responsáveis por revisar os resultados, validar afirmações importantes e
  aprovar ações de impacto antes do compartilhamento ou uso dos resultados.
- **Monitore a adoção e faça ajustes.** Analise o uso, o feedback, o consumo de créditos
  e o trabalho delegado após a implantação. Use as conclusões para ajustar o acesso,
  as orientações, o treinamento e a expansão.

<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/admin-plugin -->

Use este guia para entender como o plug-in de administração ajuda nas tarefas administrativas comuns, preparar-se para uma tarefa e experimentar prompts para os principais casos de uso com as aprovações e o contexto adequados.

## 1. Entenda para que serve o plug-in de administração

O plug-in de administração foi desenvolvido para ajudar a gerenciar configurações, permissões e controles diretamente no ChatGPT Work. Você descreve o objetivo em linguagem cotidiana, e o plug-in reúne as informações necessárias, consulta o estado atual, explica o que encontrou e orienta você sobre como prosseguir dentro das ações que ele oferece.

### Problemas que o plug-in de administração busca resolver

- Transformar uma solicitação administrativa em um fluxo de trabalho claro, sem exigir que você escreva uma requisição de API.
- Revisar o estado atual do workspace antes de tomar uma decisão ou aprovar uma alteração.
- Mostrar quais fontes e campos autorizados fundamentam a resposta, além do que não foi possível verificar.
- Pausar para revisão antes de uma alteração que o plug-in possa executar e, depois, consultar o registro novamente para confirmar o resultado.

O plug-in usa internamente APIs de administração selecionadas e fontes de dados conectadas e aprovadas. Ele não reúne todos os sistemas administrativos, não amplia suas permissões nem disponibiliza todas as ações de API no ChatGPT. O sistema responsável pelos dados continua controlando o que o plug-in pode ler ou alterar.

### Problemas que as APIs de administração buscam resolver

Uma API de administração oferece ao software uma forma estruturada de solicitar dados ou uma ação que ela oferece. As organizações podem usar as APIs de administração para criar processos internos ou ferramentas externas. Exemplos comuns incluem relatórios agendados, tarefas repetidas em muitos registros e conexões com sistemas aprovados. Esses fluxos de trabalho geralmente exigem revisão de engenharia, segurança e governança.

Você não precisa criar um fluxo de trabalho com APIs para usar este guia. O restante do guia se concentra no plug-in de administração. A administração do workspace do ChatGPT e a administração da Plataforma de API da OpenAI também continuam separadas, cada uma com suas próprias permissões e exigências de autenticação.

### Mantenha as credenciais em sigilo

Use apenas conexões e sistemas de armazenamento de segredos aprovados pela sua organização. Nunca cole uma chave real de API de administração no ChatGPT, no Codex, em um documento ou em um arquivo de código-fonte.

## 2. Prepare-se para usar o plug-in de administração

Use o plug-in de administração quando quiser realizar, em linguagem cotidiana, uma tarefa pontual compatível com os recursos do plug-in. Descreva o objetivo e forneça os IDs estáveis ou o contexto aprovado para os relatórios. O plug-in mostra o que encontrou ou o que pretende alterar antes de você decidir se quer continuar.

O plug-in usa apenas as fontes, as credenciais e as ações autorizadas para aquela tarefa. Ele não reúne todos os sistemas administrativos nem amplia suas permissões. O sistema original continua sendo a fonte de verdade.

### Antes de começar

1. Localize a área de administração onde os registros estão.
2. Reúna as informações necessárias e obtenha a aprovação exigida.
3. Comece com uma solicitação somente leitura.
4. Pergunte ao plug-in quais fontes e campos ele usou e o que não conseguiu verificar.
5. Para uma alteração compatível com os recursos do plug-in, revise o plano antes de aprová-lo. Depois, peça ao plug-in que consulte o registro novamente e confirme o resultado.

Confirme que o plug-in está disponível no seu workspace e que você tem as permissões necessárias. Os casos de uso de funções e acesso abaixo refletem o escopo atual documentado do plug-in. O plug-in pode revisar funções, permissões de recursos e atribuições de funções a usuários ou grupos. Após sua confirmação, ele também pode atribuir uma função existente a um grupo existente.

O plug-in não pode criar funções, alterar as permissões de uma função nem confirmar o acesso a um conector específico.

Os casos de uso de análise de dados precisam de acesso a fontes de dados conectadas e aprovadas. A análise de ROI também precisa de resultados de negócios ou de engenharia aprovados; os registros de uso, por si só, não bastam.

## 3. Explore os principais casos de uso do plug-in de administração

Escolha um caso de uso, substitua cada marcador de posição por um valor da sua solicitação aprovada e siga as etapas na ordem. Comece com uma solicitação somente leitura, a menos que a tarefa seja uma alteração compatível com os recursos do plug-in e já aprovada.

### Liste as funções do workspace

**Prompt para experimentar**

```text
List the roles in workspace {workspace_id}. Separate built-in and custom roles. For each role, explain which features it can use and show the users or groups assigned to it. Don’t make changes.

**Etapas**

1. **Preparação:** Confirme o ID do workspace e que você tem permissão para visualizar essas informações.
2. **Execução:** Solicite a lista de funções em uma consulta somente leitura.
3. **Revisão:** Confira os tipos de função, o acesso aos recursos e as atribuições.
4. **Verificação:** Investigue qualquer informação inesperada sem fazer alterações.

### Revise uma função

**Prompt para experimentar**

```text
Review role {role_id}. Explain its permissions in plain language, show who has it, and flag anything that looks broader than expected. Don’t edit the role.

**Etapas**

1. **Preparação:** Confirme o ID da função e o workspace.
2. **Execução:** Solicite uma revisão somente leitura da função.
3. **Revisão:** Confira se as permissões e as atribuições correspondem à finalidade da função.
4. **Verificação:** Anote as dúvidas para o responsável pela função. Lembre-se: o plug-in não pode criar a função nem editar suas permissões.

### Entenda o acesso de um usuário ou grupo

**Prompt para experimentar**

```text
Help me understand the access for user {user_id} or group {group_id}. Show their assigned roles, explain what access those roles provide, and point out overlaps or gaps. Clearly say what you can’t verify.

**Etapas**

1. **Preparação:** Use o ID estável do usuário ou grupo.
2. **Execução:** Peça ao plug-in que explique o acesso.
3. **Revisão:** Confira quais funções estão atribuídas e que acesso elas concedem. Anote quaisquer sobreposições ou lacunas.
4. **Verificação:** Se o plug-in não conseguir visualizar alguma informação, marque-a como desconhecida em vez de fazer suposições.

### Atribua uma função existente a um grupo

**Prompt para experimentar**

```text
Before making a change, show the current roles for group {group_id} and explain what role {role_id} would add. Confirm the recorded approver and wait for my explicit approval. After the assignment, verify the group’s updated roles.

**Etapas**

1. **Preparação:** Confirme os IDs do grupo e da função. Confira a solicitação aprovada e o aprovador registrado.
2. **Execução:** Peça ao plug-in que mostre as funções atuais e o que mudaria.
3. **Revisão:** Aprove somente se o plano corresponder à solicitação aprovada.
4. **Verificação:** Após a atribuição, consulte o grupo novamente para confirmar que a função existente foi adicionada conforme aprovado.

### Verifique a permissão geral para conectores

**Prompt para experimentar**

```text
Check whether user {user_id} has general connector access through their assigned roles. Ask the plugin to show which permissions support its answer. If it can’t verify access to a specific connector, have it say so clearly.

**Etapas**

1. **Preparação:** Confirme o ID do usuário e sua permissão para revisar o acesso dele.
2. **Execução:** Solicite a verificação da permissão geral.
3. **Revisão:** Confira a função atribuída e a permissão usada para elaborar a resposta.
4. **Verificação:** Use isso apenas como uma verificação geral. Isso não comprova acesso a um conector específico ou a um item conectado.

### Solucione problemas em uma alteração aprovada

**Prompt para experimentar**

```text
Review approved change {change_record_id}. Compare the requested result with the current workspace. If it failed, check the workspace and role first. Then confirm who owns the record, explain the issue, and suggest the safest next step.

**Etapas**

1. **Preparação:** Confirme o registro da alteração aprovada e o resultado pretendido.
2. **Execução:** Peça ao plug-in que compare a solicitação com o estado atual do workspace.
3. **Revisão:** Confira o workspace e a função. Em seguida, verifique quem é o responsável pelo registro.
4. **Verificação:** Use o estado atual do workspace como fonte de verdade antes de escolher o próximo passo.

### Otimize os custos e a combinação de modelos

**Prompt para experimentar**

```text
For {date_range} in workspace {workspace_id}, group verified token use and cost by use case. Compare models and reasoning modes using the speed and quality information available. Flag costly workflows when the data shows little evidence of value. Recommend where spending could be reduced or redirected toward work with stronger productivity or cost results. Include any approved revenue or quality signals. Estimate possible savings, explain tradeoffs, and separate verified observations from assumptions or missing inputs. Keep this read-only.

**Etapas**

1. **Preparação:** Confirme o workspace, o intervalo de datas e se os dados de custos cobrem todo o período. Confira quais campos aprovados de desempenho ou resultados estão disponíveis.
2. **Execução:** Peça a comparação de custos e modelos.
3. **Revisão:** Separe o que os dados mostram das suposições, das informações ausentes e das vantagens e desvantagens envolvidas.
4. **Verificação:** Confira as possíveis economias com a equipe de Finance e os responsáveis pelos fluxos de trabalho antes de agir.

### Entenda o uso e a adoção

**Prompt para experimentar**

```text
Analyze workspace {workspace_id} during {date_range}. Show tasks and token use by team and business function. Group cost by use case. Summarize what teams use ChatGPT and Codex to accomplish. Include examples from Legal, Marketing, and Sales. Compare available use of skills and plugins. Only report tool calls, connected apps, and multi-tool workflows if those fields are available. Show where teams use more advanced workflows and where there may be room to expand. Rank the top {5_or_10} use cases and show whether a small group of highly active users accounts for most usage. Don’t guess about activity that is not in the data.

**Etapas**

1. **Preparação:** Confira o workspace, o intervalo de datas e os mapeamentos de equipes. Confirme que a geração de relatórios por usuário está aprovada.
2. **Execução:** Peça a análise de uso e adoção.
3. **Revisão:** Confira quais campos solicitados estão disponíveis. Deixe de fora as atividades sem dados disponíveis, em vez de fazer suposições.
4. **Verificação:** Um alto volume de uso não comprova uso avançado, valor para o negócio nem desempenho individual.

### Meça o valor para o negócio e o ROI

**Prompt para experimentar**

```text
For workspace {workspace_id} in {date_range}, combine verified usage and cost with approved outcomes. Estimate value by team and use case. Include approved Sales measures for productivity, revenue, and quality. Compare teams and models, as well as workflows and user segments. Rank returns against cost. Show the sources and formula. Clearly state assumptions, limits, and missing inputs. Don’t claim ChatGPT caused the outcomes. Keep this read-only.

**Etapas**

1. **Preparação:** Confira o workspace e o intervalo de datas e, em seguida, confirme os resultados aprovados. Revise a fórmula e as regras de privacidade.
2. **Execução:** Peça a análise de ROI.
3. **Revisão:** Confira cada fonte e suposição. Anote cada limitação ou informação ausente.
4. **Verificação:** O uso, por si só, não comprova ROI nem causalidade. Revise o resultado com a equipe de Finance e os responsáveis pelo negócio.

### Avalie o ROI do Codex

**Prompt para experimentar**

```text
For workspace {workspace_id}, combine verified Codex usage and cost from {date_range} with approved engineering outcomes. Estimate ROI by team, repository, and workflow. Compare productivity and delivery speed with code quality and engineering cost. Identify workflows that show high value or use many resources. Recommend changes to the model, reasoning mode, or workflow. Explain the tradeoffs and uncertainty. Present the findings as patterns in the available data, not proof that Codex caused the outcome. Return findings only; do not make changes.

**Etapas**

1. **Preparação:** Confirme o workspace e o período do relatório. Revise os mapeamentos de equipes e repositórios e os dados de referência aprovados.
2. **Execução:** Peça a análise de ROI do Codex.
3. **Revisão:** Distinga os padrões observados das suposições. Proteja os dados de usuários e repositórios.
4. **Verificação:** Revise as recomendações e os valores de referência dos resultados com a equipe de Engenharia.

## 4. Quando um fluxo de trabalho via API pode fazer sentido

Algumas organizações usam as APIs para criar seus próprios processos administrativos ou ferramentas externas. Essa abordagem pode viabilizar tarefas agendadas ou contínuas. Também pode ajudar quando um processo envolve muitos registros ou precisa se conectar a um sistema interno aprovado. Essa abordagem é distinta da experiência guiada do plug-in Admin.

Comece com uma tarefa administrativa definida: identifique as informações e permissões necessárias, os pontos de revisão, o resultado esperado e como ele será registrado. Se sua organização automatizar essa tarefa, envolva as equipes responsáveis de engenharia, segurança e governança; mantenha as credenciais em um sistema aprovado de armazenamento de segredos; e teste o fluxo de trabalho antes da implantação.

### Recursos relacionados

- [Referência da API de administração do workspace do ChatGPT](https://chatgpt.com/public/admin/api-reference)
- [Limites da administração](/pt-BR/codex/enterprise/roles-and-workspace-permissions#understand-the-control-boundaries)
- [Analytics API do workspace do ChatGPT](/pt-BR/codex/enterprise/analytics-api)
- [API de Compliance do workspace do ChatGPT](/pt-BR/codex/enterprise/compliance-api)

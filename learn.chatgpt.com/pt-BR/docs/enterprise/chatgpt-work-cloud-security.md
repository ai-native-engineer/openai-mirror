<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/chatgpt-work-cloud-security -->

O ChatGPT Work faz parte do workspace do ChatGPT que você já usa e segue suas
políticas aplicáveis de privacidade, segurança e tratamento de dados. Nos workspaces Business,
Enterprise e Edu, as proteções existentes incluem criptografia em trânsito
e em repouso, e a OpenAI não usa dados empresariais para treinar seus modelos por
padrão.

O Work na nuvem também oferece execução hospedada de tarefas e ferramentas opcionais que podem
acessar sistemas conectados ou realizar ações autorizadas. Analise as permissões,
as configurações de retenção e os registros de auditoria disponíveis para as capacidades que sua
organização ativa.

As capacidades e os controles dependem do plano do workspace, da disponibilização, da configuração
e da integração conectada. Para entender o modelo de execução de forma mais ampla, consulte a
[Visão geral do ChatGPT Work](/pt-BR/codex/enterprise/chatgpt-work-overview).

## Segurança em resumo

- As tarefas na nuvem são executadas na infraestrutura gerenciada pela OpenAI, não no dispositivo
do usuário.
- Uma tarefa na nuvem não herda arquivos locais, aplicativos para desktop, sessões
do navegador nem acesso à rede privada desse dispositivo.
- Os aplicativos conectados usam as permissões da conta autorizada, que pode ser
individual, compartilhada ou pertencente a um agente.
- Os controles do workspace e os controles específicos de cada recurso regulam o acesso ao Work, a
execução local, a navegação na nuvem, os aplicativos conectados e o acesso à rede por código ou shell.
- Os dados dos workspaces Business, Enterprise e Edu são criptografados em trânsito e em
repouso e, por padrão, não são usados para treinar modelos da OpenAI.
- A retenção e a visibilidade para auditoria dependem da categoria dos dados, do local de armazenamento,
do evento e da configuração aplicável do produto.

## Onde as tarefas na nuvem são executadas

As pessoas podem iniciar tarefas na nuvem pelas interfaces compatíveis do ChatGPT na Web, em dispositivos móveis
ou no desktop. O Work na Web e em dispositivos móveis é executado na nuvem. O aplicativo para desktop pode
executar tarefas na nuvem ou locais quando as permissões correspondentes estão disponíveis e
ativadas.

O dispositivo do usuário fica dentro do perímetro de confiança da própria organização, gerenciado pela TI,
fora dos sistemas operados pela OpenAI. Iniciar uma tarefa na nuvem pelo
aplicativo para desktop não dá à tarefa acesso direto ao computador do usuário.
A execução permanece no ambiente gerenciado pela OpenAI, independentemente da interface
usada para iniciá-la.

O Work na nuvem usa o harness de execução de tarefas do Codex. O Work e o Codex compartilham mecanismos
fundamentais de execução e isolamento, mas suas ferramentas, permissões e
controles administrativos disponíveis não são idênticos. O cliente controla o acesso ao workspace,
as conexões aprovadas e as informações fornecidas intencionalmente a uma tarefa;
a OpenAI gerencia o ambiente de execução hospedado.

O Work na nuvem é executado em infraestrutura compartilhada e gerenciada pela OpenAI. No fluxo de execução
atualmente compatível, as tarefas são executadas em sandboxes baseados em VMs, com o estado de execução
associado ao usuário autenticado da conta no workspace. O Work pode reutilizar
um ambiente entre tarefas ou substituí-lo preservando o estado elegível. Isso
não significa que cada tarefa receba um novo contêiner ou que cada cliente tenha um
host físico dedicado. Os clientes não fornecem, hospedam nem gerenciam contêineres
do Work na nuvem.

## O que uma tarefa na nuvem pode acessar

Uma tarefa na nuvem pode usar informações disponibilizadas por um meio autorizado:

- Informações que uma pessoa insere em uma conversa.
- Arquivos enviados intencionalmente, anexados a partir da Biblioteca ou disponibilizados
por meio de um projeto.
- Conteúdo recuperado por meio de um aplicativo ativado e de uma conexão autorizada
com uma conta.
- Conteúdo de sites acessado por um navegador na nuvem ativado ou por outro
recurso Web permitido, sujeito aos controles de acesso aplicáveis.

Uma tarefa na nuvem não herda diretamente acesso a arquivos locais, aplicativos
instalados ou à sessão do navegador do usuário. O acesso de um dispositivo a uma
VPN corporativa, a um site interno ou a uma rede privada não concede esse acesso
à tarefa na nuvem.

Uma conexão autorizada pode disponibilizar informações de um sistema interno
por sua própria via de acesso. Essa conexão não dá à tarefa na nuvem
acesso irrestrito ao dispositivo ou à rede do funcionário.

## Apps, plug-ins e contas conectadas

Um aplicativo pode dar ao Work acesso a informações ou ações em outro sistema. Um
plug-in pode ter um aplicativo entre as ferramentas que utiliza. Disponibilizar um plug-in
não ativa automaticamente o aplicativo usado por ele, não autoriza uma conta nem
aprova todas as ações que a integração pode executar.

Uma tarefa que usa um aplicativo conectado, diretamente ou por meio de um plug-in, só pode prosseguir
quando:

- O aplicativo e qualquer plug-in que dependa dele estão ativados no workspace.
- A pessoa tem o acesso necessário, concedido pelo workspace ou pela função.
- A conexão usa uma conta autorizada, seja individual, compartilhada ou pertencente
a um agente.
- A conta conectada, os escopos aprovados e as configurações disponíveis para as ações do aplicativo
permitem acessar as informações solicitadas ou realizar a operação solicitada.

Para aplicativos que oferecem suporte ao **Controle de ações**, os administradores podem permitir ações
somente leitura, todas as ações ou um conjunto personalizado. As **Permissões de aplicativos** controlam quando
o ChatGPT pede confirmação para trabalhar com um aplicativo. Dependendo do aplicativo e do
workspace, as opções podem incluir **Sempre perguntar**, **Qualquer alteração**, **Ações
importantes** e **Nunca perguntar**. Com **Qualquer alteração**, as operações de leitura compatíveis podem prosseguir
sem um prompt, enquanto as alterações exigem confirmação.

Uma operação de escrita autorizada pode ser executada sem um prompt quando a política configurada
permite. Isso não amplia as ações permitidas do aplicativo, o acesso ao workspace nem as
permissões da conta conectada. O ChatGPT ainda pode bloquear algumas ações de alto
risco.

Confirme se o plug-in e cada aplicativo que ele usa estão disponíveis no workspace.
Analise o acesso por função, a autorização da conta conectada e as permissões de ação como
decisões distintas. Consulte
[Controles de plug-ins](/pt-BR/codex/enterprise/apps-and-connectors).

### Conexões pessoais e compartilhadas

Uma conexão pessoal usa as permissões do funcionário cuja conta está conectada no sistema
de origem. Já uma conexão compartilhada ou pertencente a um agente usa as permissões da
conta conectada a ela. Essa conta pode acessar informações ou realizar
ações que a pessoa solicitante não conseguiria acessar ou realizar com uma conta pessoal.

Antes de ativar uma conexão compartilhada, limite as permissões e os
escopos da conta, escolha quem pode usá-la e analise as ações que ela pode realizar. Consulte
[Conexões e permissões de agentes do workspace](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business).

O conteúdo recuperado de um aplicativo conectado não é salvo automaticamente como arquivo
da Biblioteca. Se depois esse conteúdo for salvo em uma conversa, em um projeto, na Biblioteca ou em um
índice sincronizado, a cópia seguirá as regras do local onde foi salva.

## Navegador na nuvem e acesso à rede

O navegador na nuvem, a pesquisa na Web, os aplicativos conectados e o acesso à rede por código ou shell são
capacidades distintas. Restringir uma delas não desativa automaticamente as
outras.

### Navegador na nuvem

O navegador na nuvem é uma ferramenta hospedada que uma tarefa do Work pode usar para interagir com
sites. Abrir o ChatGPT em um navegador Web ou no aplicativo para desktop não ativa a navegação
na nuvem; uma tarefa na nuvem pode ser executada sem ela.

O navegador hospedado não herda o perfil do navegador local do usuário, as abas abertas,
as sessões já iniciadas, as senhas salvas, o gerenciador de senhas nem o histórico de navegação.
Quando há suporte, os usuários podem fazer login separadamente por meio de um fluxo seguro de login
no ambiente hospedado. Isso não concede acesso à sessão do navegador local do usuário.

As interações compatíveis com sites podem incluir formulários públicos e combinar
informações de um aplicativo autorizado com uma tarefa em um site. Quando disponíveis,
as permissões de sites incluem **Sempre perguntar**, **Aprovar automaticamente** e **Sempre
permitir**. A opção **Aprovar automaticamente** aplica verificações automatizadas de risco; **Sempre permitir**
remove a revisão interativa de acesso ao site. Nenhuma das duas opções concede novas permissões de
aplicativos ou aprova todas as ações em um site. Ações com consequências relevantes ainda podem
exigir confirmação separada.

Para que uma tarefa do Work use o navegador na nuvem em um workspace Enterprise,
os administradores precisam ativar tanto o acesso ao Work quanto o acesso ao navegador na nuvem. Consulte
[Como usar o navegador na nuvem no ChatGPT](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt).

### Acesso à rede por código e shell

O acesso à internet pública para a execução de código ou shell segue sua própria política
de rede. Quando o acesso à internet pública está desativado, os destinos de rede necessários para
o ChatGPT Work podem continuar acessíveis por meio de uma lista gerenciada de destinos permitidos.

A lista de destinos permitidos controla os destinos de rede, não os comandos de shell. Desativar
o acesso à internet pública para a execução de código ou shell não desativa, por si só,
o navegador na nuvem, a pesquisa na Web nem os aplicativos conectados. As alterações na configuração
de rede entram em vigor depois que a execução de código ou o comando de shell em andamento termina e o
ambiente de execução é atualizado.

Consulte [Ambiente isolado para código e shell](/pt-BR/codex/sandboxing?surface=web).

## Tratamento e retenção de dados

O Work na nuvem segue as proteções de privacidade e segurança aplicáveis ao workspace do ChatGPT
descritas acima. Consulte
[Privacidade para empresas](https://openai.com/enterprise-privacy/).

As informações associadas a uma tarefa na nuvem não seguem um único
prazo de retenção:

| Categoria de dados                        | Comportamento de retenção e exclusão                                                                                                                                                                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conversas do Work                   | Seguem as configurações de retenção de conversas do workspace. A exclusão permanente dos chats excluídos geralmente é programada para ocorrer em até 30 dias, respeitando as exceções publicadas relativas à segurança, à legislação e à desidentificação.                                                                                |
| Estado e instantâneos da execução hospedada | Seguem um ciclo de vida separado do das conversas e dos arquivos. O acesso ao estado de execução é restrito ao usuário da conta, e a configuração de retenção de conversas do workspace orienta a retenção dos instantâneos armazenados elegíveis. Encerrar uma tarefa ou excluir um chat não elimina imediatamente todos os artefatos relacionados. |
| Arquivos salvos na Biblioteca               | Os arquivos enviados ou gerados seguem as regras de retenção aplicáveis da Biblioteca e do workspace. Excluir uma conversa não exclui um arquivo salvo na Biblioteca.                                                                                                                                      |
| Arquivos de projeto                        | Permanecem associados ao projeto até serem removidos ou até o projeto ser excluído, sujeitos às regras de exclusão aplicáveis.                                                                                                                                                                       |
| Memórias salvas, quando ativadas         | Seguem controles de memória separados. Excluir uma conversa não exclui necessariamente uma memória já salva.                                                                                                                                                                             |
| Envios temporários                    | Arquivos temporários elegíveis enviados no Enterprise fora da Biblioteca podem expirar após 48 horas, a menos que outra configuração de retenção seja aplicável.                                                                                                                                                      |
| Conteúdo de aplicativos conectados                | Os registros do sistema de origem seguem as políticas desse sistema. As cópias salvas em uma conversa, projeto, Biblioteca ou índice sincronizado seguem as regras do local onde foram salvas.                                                                                                                         |
| Dados do navegador na nuvem                   | Os dados do navegador hospedado são separados dos dados do navegador local. Os usuários podem remover os cookies salvos no navegador na nuvem pelas configurações correspondentes.                                                                                                                                                    |
| Registros de conformidade                   | Os registros da Plataforma de logs de conformidade ficam disponíveis por 30 dias. As cópias exportadas seguem a política de retenção do sistema que as recebe.                                                                                                                                                               |

Excluir uma conversa, remover um arquivo da Biblioteca ou uma memória salva,
desconectar um aplicativo e limpar os dados do navegador hospedado são ações distintas.
Verifique o local de armazenamento correspondente em vez de presumir que uma única ação remove
todas as cópias. Consulte
[Políticas de retenção de chats e arquivos](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt).

Manter o contexto adequado da conversa e da execução pode ajudar o Work a retomar
tarefas interrompidas, consultar etapas anteriores e produzir resultados mais consistentes.
Períodos de retenção mais curtos ou a exclusão de dados podem reduzir essa continuidade. Por isso, escolha configurações
que equilibrem os requisitos de segurança com a utilidade do fluxo de trabalho.

Workspaces Enterprise e Edu elegíveis podem usar o Gerenciamento de chaves empresariais para
conteúdo armazenado compatível, incluindo instantâneos compatíveis de execução hospedada quando
for necessária criptografia gerenciada pelo cliente. A cobertura varia conforme a categoria dos dados e a
implantação. A rotação de uma chave não exclui dados existentes nem, por si só, impede
o acesso a conteúdo criptografado anteriormente. Revogar ou desativar o acesso à chave é uma
ação separada que pode interromper fluxos de trabalho compatíveis. Nenhuma dessas ações substitui uma
política de retenção ou exclusão.

A residência de dados e a residência de inferência se aplicam apenas a conteúdo elegível e
cargas de trabalho compatíveis, conforme o contrato, a região e a
configuração da organização. Aplicativos conectados, provedores externos e algumas operações de processamento ou
índices sincronizados podem seguir regras de localização distintas. Verifique se há suporte para o
produto, a integração e a região. Consulte
[Residência de dados e residência de inferência](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt).

O controle de [zero retenção de dados](/api/docs/guides/your-data#zero-data-retention) da API da OpenAI
é específico da API e não define a retenção do ChatGPT Work.

## Controles de acesso para administradores

Revise os controles que se aplicam a cada parte de uma tarefa na nuvem:

- **Work na nuvem e Work local:** Quando houver controles independentes disponíveis,
  gerencie o Work na nuvem e o Work local com controles distintos em **Configurações do workspace** \>
**Permissões e funções**. Em outros workspaces, o Work local pode compartilhar um controle
  com o Codex Local.
- **Apps e plug-ins:** Escolha quais integrações ficam disponíveis e quais
  pessoas ou funções podem usá-las.
- **Ações de contas conectadas:** Revise as permissões da conta, os escopos do aplicativo
  e os controles de ação ou confirmação disponíveis.
- **Navegador e acesso à rede:** Avalie separadamente o acesso ao navegador na nuvem e o acesso à rede pública
  para execução de código ou shell.

Ative **Work na nuvem** apenas para usuários ou grupos aprovados. Quando houver controles separados para
**Work na nuvem** e **Work local** , ative **Work na nuvem**
e desative **Work local** na função desejada para permitir o uso do Work na nuvem sem
execução local. Quando o Work local e o Codex compartilharem um controle, avalie o efeito
sobre ambos antes de desativar a execução local. Esses controles não impedem que uma
pessoa autorizada envie intencionalmente um arquivo para uma tarefa na nuvem.

Para as permissões de função compatíveis com os estados **Padrão**, **Ativado** e **Desativado** ,
**Padrão** herda a configuração do workspace, **Ativado** concede acesso e **Desativado**
remove o acesso concedido por essa função. Se um usuário tiver várias funções personalizadas, outra
função ainda poderá conceder acesso. Algumas configurações do Work e de plug-ins usam controles diferentes,
com dois estados. Verifique o acesso efetivo considerando todas as funções atribuídas. Consulte
[Controle de acesso baseado em funções](https://help.openai.com/en/articles/11750701-rbac).

Quando disponível, a permissão **Work na nuvem** se aplica às interfaces compatíveis na Web,
em dispositivos móveis e em computadores. Ela não determina de forma independente quais dessas
interfaces podem executar tarefas na nuvem. Considere o gerenciamento de dispositivos ou outros controles de acesso
se uma implantação precisar excluir uma interface específica.

## Visibilidade para auditoria e conformidade

Para workspaces Enterprise e Edu elegíveis, a Plataforma de logs de conformidade pode
incluir os prompts e as respostas do Work para os quais há suporte. As chamadas a aplicativos conectados têm logs separados,
e os registros de auditoria disponíveis no sistema de origem variam conforme a integração.
Endpoints de conformidade compatíveis podem dar acesso a arquivos elegíveis da Biblioteca.

A cobertura depende do evento e do sistema em que ele ocorre. Não presuma
que todo comando de shell, interação com o navegador, chamada a aplicativo, operação em arquivos ou
aprovação apareça em uma exportação de conformidade visível para o cliente.

O monitoramento de endpoints pode observar o cliente do ChatGPT ou o tráfego de rede em dispositivos
gerenciados, mas não pode inspecionar ações dentro do ambiente de execução hospedado. Para isso, use
os registros compatíveis do Work, de conformidade e dos sistemas conectados.

Analise a cobertura atual dos eventos de conformidade junto com os relatórios do workspace,
os logs de auditoria dos sistemas conectados e as políticas de retenção dos sistemas que recebem
registros exportados. Consulte a
[Plataforma de conformidade da OpenAI](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

## Comece com um pequeno projeto-piloto

Escolha uma tarefa prática para um grupo pequeno. Por exemplo, uma equipe de segurança poderia
comparar um boletim aprovado de um fornecedor com um inventário autorizado e revisar um
rascunho de avaliação de exposição antes de decidir o que fazer. Se a navegação na nuvem ou
os aplicativos conectados estiverem indisponíveis, forneça diretamente o boletim e um extrato aprovado
do inventário.

Habilite apenas o acesso necessário para a tarefa. Confirme as permissões das contas conectadas,
as configurações de retenção, os registros de auditoria disponíveis e em que ponto uma pessoa
deve revisar o resultado antes de ampliar o acesso. Para planejar a implementação, consulte o
[Guia de implementação para administradores](/pt-BR/codex/enterprise/admin-setup).

<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/chatgpt-work-overview -->

O ChatGPT Work e o Codex compartilham mecanismos fundamentais de execução,
isolamento e permissões e estão sujeitos aos mesmos limites de segurança previstos no seu
contrato do ChatGPT Business ou Enterprise. As capacidades e os controles
disponíveis em cada experiência dependem de a tarefa ser executada localmente ou
na nuvem, das ferramentas disponíveis e das políticas aplicáveis ao workspace.

O ChatGPT Work pode concluir tarefas com várias etapas usando informações, arquivos,
aplicativos e ferramentas disponíveis para um membro autorizado do workspace. Na web,
essas tarefas são executadas na nuvem, não no dispositivo do membro.

Esta visão geral explica o limite de execução, os controles de rede e de aplicativos,
o tratamento de dados e como as tarefas são executadas com segurança no ChatGPT Work
na web. A disponibilidade e os controles administrativos dependem do seu plano e da
configuração do workspace.

Para uma análise específica da execução hospedada, das permissões de contas conectadas,
das configurações de navegador e rede, da retenção e da visibilidade para auditoria, consulte
[Segurança na nuvem do ChatGPT Work](/pt-BR/codex/enterprise/chatgpt-work-cloud-security).

Para saber mais sobre acesso ao dispositivo, sessões do navegador local, políticas gerenciadas e tratamento
de dados locais, consulte
[Segurança local do ChatGPT Work](/pt-BR/codex/enterprise/chatgpt-work-local-security).

## Isolamento da execução, arquivos e acesso ao dispositivo

Os arquivos e as ferramentas disponíveis para o ChatGPT Work dependem de onde o Work está sendo executado,
das permissões do usuário e da configuração do administrador.

### Work local

O Work local executa tarefas pelo aplicativo do ChatGPT para desktop no dispositivo do usuário.
Ele pode acessar arquivos locais, aplicativos e outros recursos disponibilizados a ele,
de acordo com as permissões do usuário, os controles aplicáveis ao workspace e as políticas
de segurança do dispositivo. Ao contrário do Work na Web, o Work local pode usar recursos
que permanecem no computador sem exigir que você envie arquivos para uma conversa
na nuvem.

### Work na nuvem

O Work na nuvem está disponível nas interfaces compatíveis para web, dispositivos móveis e desktop. Ele executa
o harness do Codex em um ambiente isolado na infraestrutura gerenciada pela OpenAI.
As conversas na nuvem podem ser sincronizadas entre essas interfaces, e as tarefas compatíveis podem
continuar enquanto o usuário estiver ausente da conversa.

O Work na web não pode acessar diretamente arquivos, aplicativos ou abas abertas no navegador
do computador do usuário. O usuário pode disponibilizar arquivos enviando-os, adicionando-os
a um projeto compatível ou usando um aplicativo conectado autorizado. A experiência de desktop
controla o acesso a arquivos e aplicativos locais por meio de permissões
próprias.

Quando a
[Biblioteca](https://help.openai.com/en/articles/20001052-file-storage-and-library-in-chatgpt)
está disponível, os arquivos elegíveis enviados ou gerados podem ser salvos nela.
Os administradores podem controlar se o ChatGPT faz referência automática aos arquivos
salvos na Biblioteca. Desativar as referências automáticas não impede que os usuários
acessem ou anexem explicitamente arquivos que estão autorizados a usar.

Consulte [Ambiente isolado para código e shell](/pt-BR/codex/sandboxing?surface=web),
[Criação e edição de documentos, planilhas e apresentações](https://help.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work)
e
[Armazenamento de arquivos e Biblioteca no ChatGPT](https://help.openai.com/en/articles/20001052-library-for-chatgpt).

## Acesso à rede e destinos externos

O Work usa ferramentas como execução de código e shell e o navegador na nuvem para concluir
tarefas. Cada uma dessas ferramentas tem permissões configuráveis.

- **Comandos de código e shell**: o acesso à internet pública depende da política
  aplicável ao workspace e da configuração individual de rede do Work. Quando o acesso
  à internet pública não é permitido, os comandos ainda podem acessar destinos aprovados
  pela OpenAI que são necessários para o funcionamento do Work. Isso controla os destinos
  de rede, não quais comandos podem ser executados.
- **Pesquisa na Web**: a pesquisa tem controles separados da configuração de rede
  para código e shell do Work.

Quando disponível, a configuração individual de código e shell aparece em
**Configurações** \> **Controles de dados** \> **Acesso à rede do Work**. Ativar **Permitir acesso
à internet pública** não anula uma restrição
aplicável definida pelo administrador. Desativar essa opção limita os comandos de código e shell aos destinos
necessários incluídos na lista gerenciada de permissões; isso não desativa aplicativos conectados, a pesquisa
na Web nem o navegador na nuvem.

As alterações na configuração de rede para código e shell entram em vigor depois que a execução atual
termina e o Work atualiza seu ambiente de execução. Consulte
[Ambiente isolado para código e shell](/pt-BR/codex/sandboxing?surface=web) e
[Controles de acesso ao Work](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

Os controles de interações de saída são separados das
[restrições de acesso por IP ao workspace](https://help.openai.com/en/articles/12111596-ip-allowlisting-for-chatgpt),
que limitam o acesso de entrada ao workspace do ChatGPT ou à API de Compliance.

## Navegador na nuvem e acesso a sites

O
[Navegador na nuvem](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
é uma das ferramentas que o ChatGPT Work pode usar e é diferente do
[Navegador integrado](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app).
Ele funciona remotamente e usa uma sessão de navegador separada do navegador
local do usuário. Não pode acessar abas locais, extensões, histórico de navegação,
senhas salvas nem sessões locais autenticadas.

O navegador na nuvem pode navegar por sites públicos, inserir informações em formulários
públicos compatíveis e incorporar informações relevantes de um aplicativo aprovado a uma
tarefa em um site. O login em sites pelo navegador na nuvem não está disponível em
workspaces Enterprise ou Edu. A disponibilidade do navegador depende do seu plano,
da região, da disponibilização do recurso e das permissões do workspace.
Em workspaces Enterprise, um administrador precisa ativar o acesso ao navegador na nuvem,
além do acesso ao Work.

O acesso a sites e as ações realizadas neles têm controles separados:

- Por padrão, o ChatGPT pede aprovação antes de acessar um novo site. Quando essas opções estão disponíveis, os usuários
  podem selecionar **Sempre perguntar**, **Aprovar automaticamente** ou **Sempre permitir**, além de permitir ou
  bloquear sites específicos. **Aprovar automaticamente** aplica verificações automatizadas de risco.
**Sempre permitir** elimina a revisão interativa do acesso a sites. Os administradores
  também podem limitar as configurações de aprovação dos usuários (por exemplo,
  desativar **Sempre permitir** em todo o workspace).
- Permitir o acesso a um site não aprova todas as ações nesse site. O ChatGPT pode
solicitar uma confirmação separada antes de ações que possam gerar compromissos financeiros,
jurídicos, relacionados à conta ou outros compromissos com consequências relevantes.

Os usuários podem examinar as capturas de tela disponíveis das páginas e a reprodução da navegação em uma conversa
do Work. Esses registros visíveis aos usuários não significam que haja exportação pela API de Compliance
nem um histórico completo de execução visível aos administradores.

Consulte
[Como usar o navegador na nuvem no ChatGPT](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
e [Navegador](/pt-BR/codex/browser?surface=web).

## Aplicativos conectados, credenciais e permissões

Um aplicativo conectado ou plug-in permite que o Work acesse recursos somente por meio da integração
que o workspace permite e das permissões concedidas a essa conexão. Os administradores podem
controlar a disponibilidade de plug-ins e aplicativos, o acesso por função no workspace, a autorização
externa, as configurações de ações e as permissões dos sistemas de origem no painel
administrativo.

Nos workspaces Enterprise e Edu, os plug-ins e os aplicativos dos quais dependem vêm desativados
por padrão. Nos workspaces Business, plug-ins e aplicativos vêm ativados por padrão. Disponibilizar
um plug-in não ativa automaticamente o aplicativo necessário nem concede acesso a uma conta.
A conexão necessária deve ser autorizada para uma conta individual, compartilhada ou pertencente
a um agente antes que o ChatGPT Work possa acessar a conta. Uma conexão compartilhada ou
pertencente a um agente usa as permissões da conta conectada no sistema de origem,
que podem ser diferentes das permissões do usuário solicitante.

Quando houver suporte, os administradores podem restringir um aplicativo a ações de somente leitura ou a um
conjunto aprovado de ações. As configurações de permissão do aplicativo também podem determinar se
 o ChatGPT pede confirmação antes de usar um aplicativo, fazer alterações ou realizar ações
importantes. Nem todos os aplicativos oferecem os mesmos controles de ações, e nem toda ação
exige uma confirmação humana individual.

Em aplicativos sincronizados, alterações no conteúdo de origem ou nas permissões podem demorar
para aparecer. Desconectar um aplicativo não remove automaticamente as informações já salvas
em uma conversa, em um arquivo gerado ou em um registro com política de retenção
própria.

Consulte
[Controles administrativos, segurança e conformidade para plug-ins e aplicativos](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business),
[Controles de plug-ins](/pt-BR/codex/enterprise/apps-and-connectors),
[Configuração do Google Workspace gerenciada pelo administrador](https://help.openai.com/en/articles/10929079-google-workspace-admin-managed-setup)
e [Aplicativos do ChatGPT com sincronização](https://help.openai.com/en/articles/10847137-chatgpt-apps-with-sync).

## Privacidade e tratamento de dados

O ChatGPT Work segue as políticas de privacidade, segurança e tratamento de dados
aplicáveis ao seu workspace do ChatGPT. Conversas, arquivos enviados, arquivos gerados,
aplicativos conectados e dados do navegador podem estar sujeitos a regras diferentes de retenção e
exclusão.

Para mais detalhes, consulte [Privacidade para empresas](https://openai.com/enterprise-privacy/),
[Políticas de retenção de chats e arquivos](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt),
[Residência de dados e de inferência](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)
e as [Perguntas frequentes para administradores do ChatGPT Work](/pt-BR/codex/enterprise/work-admin-faq).

### A retenção depende do tipo de dados

- **Conversas do Work:** seguem as configurações aplicáveis de retenção e exclusão de conversas
  do workspace do ChatGPT.
- **Arquivos salvos na Biblioteca:** seguem as regras de retenção aplicáveis a arquivos e ao workspace.
  Excluir uma conversa não exclui arquivos armazenados
  na Biblioteca.
- **Arquivos do projeto:** permanecem no projeto até que ele seja excluído, sujeitos às
  regras e exceções de exclusão aplicáveis.
- **Arquivos temporários enviados fora da Biblioteca:** no Enterprise, esses arquivos podem
  expirar após 48 horas, a menos que se aplique outra configuração de retenção.
- **Memórias salvas, quando ativadas:** seguem controles de memória separados.
- **Cookies do navegador na nuvem:** permanecem separados dos dados do navegador local. Os usuários podem
  apagá-los nas configurações do navegador na nuvem.
- **Registros da Plataforma de logs de conformidade:** permanecem disponíveis na plataforma por 30
  dias. As cópias exportadas seguem a política de retenção do sistema que as recebe.
- **Dados de aplicativos conectados:** os registros de origem seguem as políticas do aplicativo
  conectado. As cópias salvas em um chat, arquivo ou índice sincronizado também
  seguem as regras aplicáveis de armazenamento e retenção da OpenAI.

Excluir uma conversa, encerrar uma tarefa do Work, apagar cookies do navegador e
reter registros de conformidade são operações diferentes. Excluir um chat faz com que ele deixe de ser exibido
e programa sua exclusão permanente em até 30 dias, sujeita às exceções publicadas
relacionadas à segurança, a questões legais e à desidentificação.

Consulte
[Políticas de retenção de chats e arquivos](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt),
[Memória no ChatGPT](https://help.openai.com/en/articles/8590148-memory-in-chatgpt-faq)
e a
[Plataforma de conformidade da OpenAI](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

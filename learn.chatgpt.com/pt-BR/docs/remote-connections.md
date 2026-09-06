<!-- source: https://learn.chatgpt.com/pt-BR/docs/remote-connections -->

Desktop,
  Storage,
  Terminal,
} from "@components/react/oai/platform/ui/Icon.react";

As conexões remotas permitem acessar o trabalho em execução em outro dispositivo ou computador.
No aplicativo móvel do ChatGPT, abra **Remoto** para trabalhar com chats do ChatGPT ou do Codex em
um dispositivo Mac ou Windows conectado. Você também pode continuar o trabalho em outro
dispositivo compatível que execute o aplicativo do ChatGPT para desktop ou conectar o aplicativo a projetos
em um host SSH.

O acesso remoto usa projetos, chats, arquivos, credenciais,
permissões, plug-ins, o Uso do computador, a configuração do navegador e ferramentas locais do host conectado.

## O que você pode fazer remotamente

- Iniciar novos chats em projetos no host ou continuar os existentes.
- Enviar instruções complementares, responder a perguntas e orientar o trabalho em andamento.
- Aprovar comandos e outras ações.
- Revisar saídas, diffs, resultados de testes, saídas do terminal e capturas de tela.
- Receber uma notificação quando o ChatGPT concluir uma tarefa ou precisar da sua atenção.
- Alternar entre hosts conectados e chats.

As próximas seções explicam como abrir **Remoto** no aplicativo móvel do ChatGPT para acessar um
host de desktop. Para conectar o Codex a um projeto em um host SSH, consulte
[conectar-se a um host SSH](#connect-to-an-ssh-host).

<div class="not-prose my-6 max-w-4xl rounded-xl bg-[url('/images/codex/codex-wallpaper-1.webp')] bg-cover bg-center p-4 md:p-8">
  
    
      
    
  
</div>

<a id="before-you-set-up-mobile-access"></a>

## Antes de configurar o Remoto

  O Remoto é compatível com hosts que executam o aplicativo do ChatGPT para desktop no macOS e no Windows.
  Você pode controlar um host pelo ChatGPT no iOS ou Android, ou por outro dispositivo Mac ou
  Windows quando a opção **Controlar outros dispositivos** estiver disponível. A disponibilidade pode
  variar conforme a liberação do recurso.

Confira se você tem:

- Acesso ao Codex na conta e no workspace do ChatGPT que você quer usar.
- A versão mais recente do aplicativo móvel do ChatGPT instalada em um dispositivo iOS ou Android. Se **Remoto**
  não aparecer no aplicativo, primeiro atualize o ChatGPT.
- A versão mais recente do aplicativo do ChatGPT para desktop no macOS ou Windows, em execução em um host que não esteja em repouso,
esteja online e conectado à mesma conta e ao mesmo workspace. A configuração pelo dispositivo móvel começa
no aplicativo; não é possível realizá-la pela Codex CLI nem pela extensão para IDE.
- Qualquer configuração necessária de autenticação multifator, SSO ou chave de acesso para
essa conta ou workspace.

Se você usa o Codex em um workspace do ChatGPT, talvez o administrador precise habilitar
o acesso ao Controle remoto antes que você possa se conectar pelo celular.

<a id="set-up-mobile-access"></a>

## Configurar o Remoto

Comece no aplicativo do ChatGPT para desktop no host ao qual você quer se conectar. O fluxo de configuração
habilita o acesso remoto para esse host e exibe um código QR que você pode escanear com o
celular.
O código QR emparelha esse celular com o host. Emparelhe cada celular ou dispositivo compatível
com o aplicativo para desktop com cada host que você quer que ele controle.

  As conexões existentes usadas desde 8 de junho de 2026 continuam emparelhadas. Se você não
usou uma conexão existente desde 8 de junho de 2026, atualize os dois aplicativos e emparelhe os
dispositivos novamente.

1. Inicie a configuração do Remoto.

   Abra o aplicativo do ChatGPT para desktop no host. Acesse **Configurações** \>
**Conexões** \> **Controlar este Mac ou PC** e selecione **Configurar** ou
**Adicionar**. Aprove o acesso remoto e conclua qualquer verificação solicitada.

2. Escaneie o código QR.

   Use o celular para escanear o código QR exibido pelo aplicativo. O código abre o ChatGPT
para que você conclua a conexão do aplicativo móvel ao host.

3. Conclua a configuração no ChatGPT.

   O ChatGPT abre o fluxo de configuração do Remoto. Confirme que está usando a mesma conta do ChatGPT
e o mesmo workspace e conclua as etapas necessárias de autenticação multifator, SSO
ou chave de acesso. Após a conclusão da configuração, o host aparecerá em Remoto no
celular.

4. Revise as configurações do host.

   No aplicativo do host, use **Configurações** \> **Conexões** para gerenciar os
   dispositivos conectados. Você também pode optar por manter o computador ativo, habilitar o
   Uso do computador ou instalar a Extensão do Chrome.

  

## Escolha o que conectar

Comece pelo notebook ou computador desktop em que você já usa o ChatGPT. Adicione um computador sempre ligado
ou um host SSH quando precisar de acesso contínuo ou de outro ambiente.

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>Seu notebook ou computador desktop</span></span>

Conecte o Mac ou PC com Windows em que o aplicativo para desktop já está instalado. Isso
oferece acesso remoto aos mesmos projetos, chats, credenciais, plug-ins e à configuração
local que você já usa.

Se esse computador entrar em repouso, perder o acesso à rede ou o aplicativo for fechado, o acesso remoto
será interrompido até que ele volte a ficar disponível. Se você usar esse computador como dispositivo host,
mantenha-o conectado à energia e use as configurações de conexão do host para mantê-lo ativo quando
essa opção estiver disponível.

Em um notebook Mac, o acesso remoto pode continuar disponível com a tampa aberta e o cabo de alimentação
conectado. Com a tampa fechada, conecte também um monitor externo. Selecionar
**Repouso** ainda interrompe o acesso remoto.

Em um host Windows, mantenha a sessão desbloqueada e disponível para tarefas que usam o
[Uso do computador](/pt-BR/codex/computer-use). No Windows, o Uso do computador é executado em
primeiro plano. Por isso, o controle remoto é mais indicado para iniciar ou verificar o trabalho enquanto você
dedica a área de trabalho do host à tarefa.

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>Um computador dedicado sempre ligado</span></span>

Use um Mac ou PC com Windows dedicado e sempre ligado quando quiser manter o ChatGPT
disponível para trabalhos mais longos.

Instale nessa máquina os projetos, as credenciais, os servidores MCP, as habilidades e as ferramentas que o ChatGPT ou
o Codex devem usar.

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>Um ambiente de desenvolvimento remoto</span></span>

Use um host SSH ou um ambiente de desenvolvimento remoto gerenciado quando o projeto
já estiver em um ambiente remoto. Primeiro, conecte o host do aplicativo para desktop a esse
ambiente; o celular continuará conectado ao mesmo host, e o ChatGPT trabalhará
no ambiente remoto com as respectivas dependências, políticas de segurança e recursos
de computação.

Para ver detalhes da configuração de SSH, consulte [conectar-se a um host SSH](#connect-to-an-ssh-host).

  Para tarefas no navegador ou na área de trabalho em um computador sempre ligado ou host remoto, habilite o
Uso do computador e instale a Extensão do Chrome nesse host.

## O que o host conectado fornece

Seu celular envia prompts, aprovações e mensagens de acompanhamento ao ChatGPT. O
host conectado fornece o ambiente usado pelo ChatGPT.

Isso significa que:

- Os arquivos do repositório e os documentos locais vêm do host conectado.
- Os comandos de shell são executados nesse host ou ambiente remoto.
- Os servidores MCP, as habilidades, o acesso ao navegador e o Uso do computador são fornecidos pela
configuração desse host.
- Sites com login ativo e aplicativos para desktop só ficam disponíveis quando o host consegue
acessá-los.
- As configurações do ambiente isolado, os controles de segurança e as aprovações de ações continuam se aplicando
à sessão conectada.

Uma camada segura de retransmissão mantém as máquinas confiáveis acessíveis pelos seus dispositivos
autorizados no ChatGPT, sem expô-las diretamente à internet pública.

## Retome o trabalho em outro dispositivo

Você pode continuar o trabalho em outro dispositivo com uma sessão iniciada, que execute o aplicativo do ChatGPT para desktop
e ofereça suporte ao controle remoto. Por exemplo, se o notebook não estiver disponível, você poderá
iniciar um chat pelo celular em um host sempre ligado e, mais tarde, abrir o aplicativo no
notebook e continuar o mesmo chat nele.

Em um dispositivo Mac ou Windows em que o recurso esteja disponível, use **Configurações \>
Conexões \> Controlar outros dispositivos** para adicionar o outro host. Um dispositivo pode permitir
o acesso remoto e controlar outro dispositivo ao mesmo tempo.

  

## Conectar-se a um host SSH

No aplicativo do ChatGPT para desktop, adicione projetos remotos de um host SSH e execute chats
no sistema de arquivos e no shell remotos. Os chats de projetos remotos executam comandos,
leem arquivos e gravam alterações no host remoto.

Mantenha o host remoto configurado segundo os mesmos critérios de segurança adotados no
acesso SSH normal: chaves confiáveis, contas com privilégios mínimos e nenhum
listener público sem autenticação.

1. Adicione o host à sua configuração SSH para que o Codex possa detectá-lo automaticamente.

   ```text
   Host devbox
     HostName devbox.example.com
     User you
     IdentityFile ~/.ssh/id_ed25519

   O Codex lê aliases de host explícitos em `~/.ssh/config`, resolve-os com
   o OpenSSH e ignora hosts definidos apenas por padrões.

2. Confirme que você consegue acessar o host por SSH a partir da máquina que executa o aplicativo.

   ```bash
   ssh devbox

3. Instale e autentique o Codex no host remoto.

   O aplicativo inicia o App Server remoto do Codex por SSH, usando o shell de login do
   usuário remoto. Verifique se o comando `codex` está disponível no
   `PATH` do host remoto nesse shell.

4. No aplicativo, abra **Configurações \> Conexões**, adicione ou ative o host SSH e
   selecione uma pasta de projeto remoto.

  

<a id="hand-off-a-thread-between-hosts"></a>
<a id="hand-off-a-chat-between-hosts"></a>
<a id="hand-off-a-task-between-hosts"></a>

## Transferir um chat entre hosts

A transferência move um chat existente e seu estado do Git entre o computador local
e um host remoto conectado. Use esse recurso para iniciar o trabalho localmente, continuar em uma
árvore de trabalho em um computador remoto e trazer o chat de volta mais tarde.

Antes de transferir um chat, conecte o host de destino e salve um projeto
para o mesmo repositório Git nesse host. Se o projeto for um subdiretório do
repositório, salve o mesmo subdiretório nos dois hosts. O Codex exibe apenas
destinos com um projeto salvo correspondente.

Para transferir um chat:

1. Abra o chat no aplicativo para desktop.
2. No rodapé do chat, selecione o local de execução atual e depois selecione o
   host de destino. Selecione **Este computador** para transferir um chat remoto de volta
   ao seu computador local.
3. Confira o destino e a branch e, em seguida, selecione **Transferir**.

O Codex cria ou reutiliza uma árvore de trabalho no host de destino, transfere o
chat e o estado do Git e muda o local de execução do chat para esse host. Se o chat estiver
em execução, a transferência interrompe a resposta atual antes de transferir o chat.

Você também pode pedir ao Codex, em outro chat, que transfira um chat identificado pelo nome para um
host conectado. O Codex não pode transferir o chat em que a solicitação foi feita, e não há suporte
para transferências para um ambiente do Codex Cloud.

## Autenticação e exposição à rede

As conexões remotas usam SSH para iniciar e gerenciar o App Server remoto do Codex.
Não exponha os mecanismos de transporte do App Server diretamente em uma rede compartilhada ou pública.

Se precisar acessar uma máquina remota fora da sua rede atual, use uma VPN
ou uma ferramenta de rede mesh em vez de expor o App Server diretamente à
internet.

## Solução de problemas

### O host não aparece no seu celular

Confirme que o aplicativo para desktop está em execução no host, que você ativou **Permitir
que outros dispositivos se conectem** e que ambos os dispositivos usam a mesma conta do ChatGPT e
o mesmo workspace. Se você não tiver usado a conexão desde 8 de junho de 2026, atualize os dois
aplicativos e emparelhe os dispositivos novamente.

### O Controle remoto fica desativado depois que você faz login novamente

Sair do ChatGPT desativa o **Controle remoto**, mas não remove os
emparelhamentos existentes dos seus dispositivos. Depois de fazer login novamente, ative o **Controle remoto** para
restaurar o estado anterior da conexão.

Se aparecer um erro depois que você ativar o **Controle remoto** e selecionar **Adicionar**,
reinicie o aplicativo do ChatGPT para desktop no host e tente novamente.

### A solicitação de aprovação não aparece

No aplicativo do ChatGPT para dispositivos móveis, abra **Remoto**. Confirme que o celular e o host usam
a mesma conta do ChatGPT e o mesmo workspace. Depois, escaneie o código QR novamente ou reinicie
a configuração a partir do host. Se você usa um workspace do ChatGPT, peça ao seu administrador para confirmar
se o acesso ao Controle remoto está ativado.

### A sessão remota se desconecta

Verifique se o host entrou em repouso ou perdeu o acesso à rede, ou se o aplicativo foi fechado.
Mantenha o host ativo e conectado enquanto o ChatGPT trabalha.

### A autenticação bloqueia a configuração

Conclua a solicitação de autenticação da conta ou do workspace exibida durante a configuração. Se
sua organização exigir SSO, autenticação multifator ou uma chave de acesso,
conclua esse fluxo antes de tentar novamente. Se a configuração ainda falhar, peça ao administrador do workspace
que confirme se o acesso ao Controle remoto está ativado.

## Veja também

- [Aplicativo do ChatGPT para desktop](/pt-BR/codex/app)
- [Recursos](/pt-BR/codex/features)
- [Configurações do aplicativo do ChatGPT para desktop](/codex/reference/settings)
- [Uso do computador](/pt-BR/codex/computer-use)
- [Extensão do Chrome](/pt-BR/codex/chrome-extension)
- [Opções de linha de comando](/codex/developer-commands?surface=cli)
- [Autenticação](/pt-BR/codex/auth)

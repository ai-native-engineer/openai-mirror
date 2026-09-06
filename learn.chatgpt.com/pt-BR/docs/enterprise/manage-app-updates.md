<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/manage-app-updates -->

O aplicativo do ChatGPT para desktop normalmente verifica e instala atualizações por conta própria. Se
sua organização precisar revisar novas versões antes que os usuários as recebam, você
poderá desativar o atualizador integrado do aplicativo e implantar versões aprovadas por meio
da sua plataforma de gerenciamento de dispositivos.

O atualizador do aplicativo permanece ativado por padrão. Desativá-lo não impede que
a Microsoft Store, o Microsoft Intune, o gerenciamento de dispositivos móveis (MDM), gerenciadores de
pacotes ou outras ferramentas externas de implantação instalem atualizações.

## Antes de começar

Confirme se você tem:

- Acesso de administrador do Codex à
[Configuração gerenciada](https://chatgpt.com/codex/settings/managed-configs)
  do seu workspace.
- Uma versão para macOS ou Windows do aplicativo do ChatGPT para desktop que ofereça suporte a
atualizações gerenciadas pela organização.
- Uma plataforma MDM ou de implantação de software que possa instalar pacotes aprovados do aplicativo
nos seus dispositivos gerenciados.
- Um processo para testar novas versões, implantar atualizações de segurança e acompanhar
as versões instaladas do aplicativo.

Se você ainda não implantou o aplicativo no Windows, comece por
[Implantar o aplicativo para Windows](/pt-BR/codex/enterprise/windows-deployment).

## Desativar as atualizações no aplicativo

  Ao desativar as atualizações no aplicativo, sua organização fica responsável por
implantar prontamente novas versões do aplicativo e correções de segurança. Adiar as atualizações pode
deixar o aplicativo e os componentes incluídos nele expostos a vulnerabilidades de segurança
conhecidas. Versões anteriores do aplicativo não recebem patches de segurança separados nem
suporte estendido.

Crie uma política gerenciada que desative o atualizador integrado do aplicativo para desktop:

1. Abra a
[Configuração gerenciada](https://chatgpt.com/codex/settings/managed-configs).
2. Selecione **Adicionar política** ou abra uma política existente para os usuários, grupos ou
   plataformas que você quer gerenciar.
3. Em **Destinos**, selecione **Adicionar destino** para atribuir a política a
**Grupos**, **Usuários** ou **Plataformas** específicos. Quando
   possível, comece com um pequeno grupo piloto.
4. Abra **TOML bruto** e localize o editor de **requirements.toml**.
5. Adicione a seguinte política:

   ```toml
   [features]
   in_app_updates = false

   Se sua política já tiver uma tabela `[features]`, adicione
`in_app_updates = false` a essa tabela. Não adicione uma segunda tabela `[features]`
   nem insira a configuração em **config.toml**.

6. Selecione **Salvar alterações**.
7. Peça aos usuários afetados que encerrem completamente e reabram o aplicativo do ChatGPT para desktop. Fechar
a janela do aplicativo nem sempre é suficiente para reiniciá-lo.

Alguns workspaces exibem um editor de lista de políticas em vez da aba **TOML bruto**. Nessa
interface, adicione o mesmo bloco TOML diretamente à política aplicável, use
**Grupos** para atribuí-la quando disponível e selecione **Salvar**.

Para saber mais sobre a distribuição e a precedência de políticas gerenciadas, consulte a
[Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration).

## Verificar a configuração gerenciada

Depois que o aplicativo reiniciar, verifique a política no dispositivo de um usuário afetado:

1. Entre no aplicativo do ChatGPT para desktop com uma conta abrangida pela política.
2. Abra **Configurações** \> **Geral**.
3. Localize **Atualizações no aplicativo** e confirme se o indicador **Gerenciado** e a mensagem
   “Sua organização desativou as atualizações no aplicativo.” são exibidos.
4. Confirme se sua plataforma de gerenciamento de dispositivos ainda consegue implantar uma
versão aprovada do aplicativo.

A opção de menu **Verificar atualizações** pode continuar visível mesmo quando a política
bloqueia as atualizações no aplicativo. Use o indicador **Gerenciado** para verificar a política
em vez de conferir se essa opção de menu é exibida.

Se o indicador não aparecer depois da primeira reinicialização, talvez o aplicativo ainda
esteja usando uma política em cache. Aguarde a atualização da política, encerre completamente e reabra o
aplicativo. Não conte com a restrição de atualizações até que **Gerenciado** apareça.

## Implantar versões aprovadas do aplicativo

Depois de desativar as atualizações no aplicativo, use o processo atual de gerenciamento de dispositivos
para distribuir novas versões:

1. Escolha uma versão do aplicativo que sua organização pretende implantar.
2. Obtenha o pacote de instalação compatível com cada sistema operacional e
arquitetura de dispositivo da sua frota.
3. Teste a versão com um pequeno grupo de usuários representativos.
4. Implante o pacote aprovado por meio do Microsoft Intune, da sua plataforma MDM ou de
outra ferramenta de implantação de software.
5. Verifique o inventário de dispositivos para confirmar se a plataforma instalou a versão
pretendida. Depois, amplie a implantação para outros grupos.

Sua plataforma de gerenciamento determina como você implanta versões em etapas, seleciona versões
e se recupera quando uma implantação não é concluída. Se a plataforma permitir
reversão, retornar a uma versão anterior não estende o suporte nem garante
compatibilidade com o serviço.

No macOS, baixe o
[instalador do aplicativo do ChatGPT para desktop](https://persistent.oaistatic.com/codex-app-prod/ChatGPT.dmg).
Para ver os métodos de instalação no Windows e os pacotes específicos para cada arquitetura, consulte
[Implantar o aplicativo para Windows](/pt-BR/codex/enterprise/windows-deployment).

## Reativar as atualizações no aplicativo

Para restaurar o comportamento normal de atualização do aplicativo:

1. Identifique as políticas gerenciadas, os arquivos `requirements.toml` do sistema e os perfis
   de MDM que desativam as atualizações para os usuários afetados.
2. Remova `in_app_updates = false` de cada tabela `[features]` aplicável.
3. Salve as alterações nas políticas e reimplante os requisitos gerenciados nos dispositivos que foram atualizados.
4. Peça aos usuários afetados que encerrem completamente e reabram o aplicativo do ChatGPT para desktop.
5. Em **Configurações** \> **Geral**, confirme se a linha gerenciada de **Atualizações no aplicativo**
   não é mais exibida.

Quando nenhuma política aplicável define `in_app_updates = false`, o atualizador
integrado do aplicativo segue o comportamento normal. Se o indicador **Gerenciado** ainda
aparecer, revise outras políticas do workspace, os perfis de MDM e os arquivos
`requirements.toml` do sistema. Consulte a seção
[Locais e precedência](/pt-BR/codex/enterprise/managed-configuration#locations-and-precedence)
para saber em que ordem as fontes gerenciadas são aplicadas.

## Entenda as responsabilidades de segurança e suporte

Depois de recebida e aplicada pelo aplicativo, a política de atualização gerenciada:

- Impede que o aplicativo para desktop verifique, baixe ou instale atualizações
por meio do próprio atualizador.
- Não oferece fixação de versão gerenciada pela OpenAI, um canal de lançamento separado
nem garantia de compatibilidade do serviço com versões anteriores.
- Aplica-se ao aplicativo do ChatGPT para desktop em compilações compatíveis do macOS e do Windows. Ela
não gerencia as atualizações dos aplicativos móveis, do Codex CLI nem da Extensão para IDE.

## Resolver problemas comuns

Se um problema de autenticação, de conexão ou um tempo limite impedir que o aplicativo
recupere ou aplique a política gerenciada, o atualizador integrado pode
continuar ativado. Não presuma que o aplicativo bloqueia atualizações a menos que **Gerenciado** apareça.

Se o indicador **Gerenciado** não aparecer, confirme se:

- O usuário afetado selecionou o workspace correto.
- A política abrange esse usuário, grupo ou plataforma.
- O dispositivo executa uma versão compatível do aplicativo.
- O aplicativo consegue se conectar ao serviço que distribui as políticas gerenciadas.
- A configuração está em **requirements.toml**, não em **config.toml**.
- O usuário encerrou completamente e reabriu o aplicativo depois que você salvou a política.

Se você não conseguir abrir a Configuração gerenciada ou salvar uma política, confirme se tem
acesso de administrador do Codex nesse workspace.

Se a versão do aplicativo mudar depois que você desativar as atualizações no aplicativo, verifique se
Microsoft Store, Intune, MDM, um gerenciador de pacotes ou outro sistema de implantação
instalou a atualização. A política controla apenas o atualizador integrado do aplicativo.

## Documentação relacionada

- [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration)
- [Implantar o aplicativo para Windows](/pt-BR/codex/enterprise/windows-deployment)
- [Referência de configuração do `requirements.toml`](/pt-BR/codex/config-file/config-reference#requirementstoml)
- [Guia de implantação para administradores](/pt-BR/codex/enterprise/admin-setup)

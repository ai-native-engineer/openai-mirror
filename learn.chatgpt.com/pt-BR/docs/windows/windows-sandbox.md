<!-- source: https://learn.chatgpt.com/pt-BR/docs/windows/windows-sandbox -->

Use o Codex no Windows com o [aplicativo do ChatGPT para desktop](/pt-BR/codex/windows/windows-app) nativo, a
[CLI](/pt-BR/codex/cli) ou a [extensão para IDE](/pt-BR/codex/ide).

O aplicativo do ChatGPT para desktop no Windows é compatível com fluxos de trabalho essenciais, como chats em paralelo,
árvores de trabalho, tarefas agendadas, funcionalidades do Git, o navegador integrado, pré-visualizações de arquivos,
plug-ins e habilidades.

O aplicativo pode ser executado nativamente no PowerShell com um sandbox do Windows, sem
exigir o WSL nem uma máquina virtual. Assim, o Codex permanece em fluxos de trabalho nativos do Windows,
com permissões delimitadas para o sistema de arquivos e a rede.

  
    
  

<div class="mb-8">
  
</div>

O sandbox nativo do Windows tem dois modos:

- nativamente no Windows com o sandbox `elevated`, que é mais robusto,
- nativamente no Windows com o sandbox alternativo `unelevated`.

<span id="windows-sandbox"></span>

## Configure o sandbox do Windows

Ao executar o Codex nativamente no Windows, o modo agente usa um sandbox do Windows para
bloquear gravações no sistema de arquivos fora da pasta de trabalho e impedir o acesso à rede
sem sua aprovação explícita.

O suporte ao sandbox nativo do Windows inclui dois modos que podem ser configurados em
`config.toml`:

```toml
[windows]
sandbox = "elevated" # or "unelevated"

`elevated` é o sandbox nativo preferencial do Windows. Ele usa usuários dedicados
do sandbox com privilégios reduzidos, limites de permissão do sistema de arquivos, regras de
firewall e alterações nas políticas locais necessárias aos comandos executados no sandbox.

`unelevated` é o sandbox nativo alternativo do Windows. Ele executa comandos com um
token restrito do Windows derivado do usuário atual, aplica limites do sistema de arquivos
baseados em ACL e usa controles offline no nível do ambiente em vez da
regra de firewall dedicada ao usuário offline. É menos robusto que `elevated`, mas
ainda é útil quando políticas locais ou corporativas bloqueiam a configuração aprovada
pelo administrador.

Se ambos os modos estiverem disponíveis, use `elevated`. Se o sandbox nativo padrão
não funcionar no seu ambiente, use `unelevated` como alternativa enquanto você
soluciona os problemas de configuração.

Os administradores corporativos podem restringir quais implementações do sandbox nativo
o Codex pode usar por meio de [`requirements.toml`](/pt-BR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml):

```toml
[windows]
allowed_sandbox_implementations = ["elevated"]

Este exemplo exige o sandbox `elevated` e impede que os usuários recorram
ao `unelevated`. Para permitir qualquer uma das implementações, inclua os dois valores;
o Codex prefere `elevated` quando nenhum modo é selecionado. Consulte a
[referência de `requirements.toml`](/pt-BR/codex/config-file/config-reference#requirementstoml) para ver
os valores aceitos.

Por padrão, os dois modos de sandbox também usam uma área de trabalho privada para reforçar o isolamento
da interface do usuário. Defina `windows.sandbox_private_desktop = false` somente se precisar do
comportamento anterior de `Winsta0\\Default` por motivos de compatibilidade.

### Permissões do sandbox

  Executar o Codex no modo Acesso completo significa que ele não fica limitado ao diretório do
  seu projeto e pode executar acidentalmente ações destrutivas que podem causar
  perda de dados. Para automatizar com mais segurança, mantenha os limites do sandbox e use
[regras](/pt-BR/codex/agent-configuration/rules) para exceções específicas ou defina a
[política de aprovação como
  nunca](/pt-BR/codex/agent-approvals-security#run-without-approval-prompts) para que
  o Codex tente resolver problemas sem solicitar permissões elevadas,
  com base na sua [configuração de aprovação e segurança](/pt-BR/codex/agent-approvals-security).

### Matriz de versões do Windows

| Versão do Windows                  | Nível de suporte   | Observações                                                                                                                                                                                 |
| -------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows 11                       | Recomendado     | Melhor base para usar o Codex no Windows. Use esta versão ao padronizar uma implantação corporativa.                                                                                       |
| Windows 10 recente e totalmente atualizado | Suporte dentro do possível     | Pode funcionar, mas é menos confiável que o Windows 11. No Windows 10, o Codex depende do suporte a consoles modernos, incluindo o ConPTY. Na prática, é necessário usar o Windows 10 versão 1809 ou posterior. |
| Builds mais antigas do Windows 10          | Não recomendado | Há maior probabilidade de não incluírem componentes de console obrigatórios, como o ConPTY, e de apresentarem falhas em configurações corporativas.                                                                          |

Outras premissas sobre o ambiente:

- `winget` deve estar disponível. Se não estiver, atualize o Windows ou instale
  o Gerenciador de Pacotes do Windows antes de configurar o Codex.
- O sandbox nativo recomendado depende de uma configuração aprovada pelo administrador.
- Alguns dispositivos gerenciados pela empresa bloqueiam as etapas de configuração necessárias mesmo quando a
própria versão do sistema operacional é aceitável.

### Conceder acesso de leitura ao sandbox

Quando um comando falhar porque o sandbox do Windows não consegue ler um diretório, use:

```text
/sandbox-add-read-dir C:\absolute\directory\path

O caminho deve ser absoluto e apontar para um diretório existente. Depois que o comando for concluído com êxito, os comandos subsequentes executados no sandbox poderão ler esse diretório durante a sessão atual.

<span id="windows-subsystem-for-linux"></span>

Use o sandbox nativo do Windows por padrão. Escolha o [WSL](/pt-BR/codex/windows/wsl)
quando precisar de ferramentas nativas do Linux, seu fluxo de trabalho já estiver no WSL2 ou
nenhum dos dois modos de sandbox nativo do Windows atender às suas necessidades.

## Solução de problemas e perguntas frequentes

Se estiver solucionando problemas em uma máquina Windows gerenciada, comece pelo modo do
sandbox nativo, pela versão do Windows e por qualquer erro de política exibido pelo Codex. A maioria dos problemas de suporte nativo no
Windows decorre da configuração do sandbox, dos direitos de logon ou das permissões do sistema de arquivos,
e não do próprio editor.

Se o Codex não conseguir concluir a configuração do sandbox `elevated`, as causas mais comuns
são:

- a solicitação do UAC do Windows ou a solicitação de administrador foi recusada,
- a máquina não permite criar usuários ou grupos locais,
- a máquina não permite alterar as regras de firewall,
- a máquina bloqueia os direitos de logon necessários aos usuários do sandbox,
- ou outra política corporativa bloqueia parte do fluxo de configuração.

O que tentar:

1. Tente configurar novamente o sandbox `elevated` e aprove a solicitação de administrador
   se o seu ambiente permitir.
2. Se o notebook da sua empresa bloquear isso, pergunte à equipe de TI se a máquina
permite uma configuração aprovada pelo administrador para criar usuários e grupos locais, configurar o firewall
e conceder os direitos de logon necessários aos usuários do sandbox.
3. Se a configuração padrão continuar falhando, use o sandbox `unelevated` para poder
   continuar trabalhando enquanto o problema é investigado.

Isso significa que o Codex não conseguiu concluir a configuração do sandbox `elevated`, que é mais robusto, na sua
máquina.

- O Codex ainda pode ser executado em um sandbox.
- Ele ainda aplica limites do sistema de arquivos baseados em ACL, mas não conta com o
  isolamento por usuários separados do sandbox `elevated` e oferece um isolamento de rede
  menos robusto.
- Essa é uma alternativa útil, mas não é a configuração corporativa preferencial
a longo prazo.

Se estiver usando um notebook corporativo gerenciado, a melhor solução a longo prazo geralmente é
fazer o sandbox `elevated` funcionar com a ajuda da sua equipe de TI.

Se comandos executados no sandbox falharem com o erro `1385`, o Windows está negando o tipo de logon
necessário para que o usuário do sandbox inicie o comando.

Na prática, isso geralmente significa que o Codex criou os usuários do sandbox com sucesso,
mas a política do Windows ainda impede que esses usuários iniciem
comandos no sandbox.

O que fazer:

1. Pergunte à sua equipe de TI se a política do dispositivo concede os direitos de logon necessários
aos usuários do sandbox criados pelo Codex.
2. Compare as diferenças de política de grupo ou de OU se o problema afetar apenas algumas
máquinas ou equipes.
3. Se precisar continuar trabalhando imediatamente, use o sandbox `unelevated` enquanto
   o problema de política é investigado.
4. Envie `CODEX_HOME/.sandbox/sandbox.log`, junto com sua versão do Windows e uma
   breve descrição da falha.

O Codex pode avisar que `Everyone` tem permissão de gravação em algumas pastas.

Se esse aviso aparecer, as permissões do Windows nessas pastas são amplas demais para
que o sandbox consiga protegê-las totalmente.

O que fazer:

1. Revise as pastas que o Codex lista no aviso.
2. Remova a permissão de gravação de `Everyone` nessas pastas, se isso for adequado ao
   seu ambiente.
3. Reinicie o Codex ou execute novamente a configuração do sandbox depois que essas permissões forem
corrigidas.

Se não souber como alterar essas permissões, peça ajuda à sua equipe de TI.

Alguns chats do Codex são executados intencionalmente sem acesso de saída à rede,
dependendo do modo de permissões em uso.

Se uma tarefa falhar porque não consegue acessar a rede:

1. Verifique se a tarefa deveria ser executada com a rede desativada.
2. Se você esperava ter acesso à rede, reinicie o Codex e tente novamente.
3. Se o problema persistir, colete o log do sandbox para que a equipe possa verificar
se o sandbox da máquina está em um estado parcial ou corrompido.

Isso pode acontecer depois de:

- mover um repositório ou workspace,
- alterar as permissões da máquina,
- alterar as políticas do Windows,
- ou fazer outras alterações na configuração do sistema.

O que tentar:

1. Reinicie o Codex.
2. Tente configurar novamente o sandbox `elevated`.
3. Se isso não resolver o problema, use temporariamente o sandbox `unelevated` como
   alternativa.
4. Colete o log do sandbox para revisão.

Se os problemas persistirem, envie:

- `CODEX_HOME/.sandbox/sandbox.log`

Também é útil incluir:

- uma breve descrição do que você estava tentando fazer,
- se o sandbox `elevated` falhou ou se o sandbox `unelevated` foi usado,
- qualquer mensagem de erro exibida no aplicativo,
- se apareceu o erro `1385` ou outro erro do Windows ou do PowerShell,
- e se você está usando o Windows 11 ou o Windows 10.

Não envie:

- o conteúdo de `CODEX_HOME/.sandbox-secrets/`

Talvez seu sistema não tenha as ferramentas de desenvolvimento C++ exigidas por algumas dependências nativas:

- Visual Studio Build Tools (carga de trabalho de C++)
- Microsoft Visual C++ Redistributable (x64)
- Com `winget`, execute `winget install --id Microsoft.VisualStudio.2022.BuildTools -e`

Depois da instalação, reinicie completamente o VS Code.

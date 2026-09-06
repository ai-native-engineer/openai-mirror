<!-- source: https://learn.chatgpt.com/pt-BR/docs/sandboxing -->

O Sandbox é o limite que permite ao agente agir de forma autônoma sem conceder a ele
acesso irrestrito à sua máquina. Quando um chat local executa comandos no
**aplicativo do ChatGPT para desktop**, na **Codex CLI** ou na **extensão para IDE**, esses comandos são executados em um
ambiente restrito, e não com acesso completo por padrão.

Esse ambiente define o que o agente pode fazer por conta própria, como quais arquivos ele
pode modificar e se os comandos podem acessar a rede. Quando uma tarefa permanece dentro
desses limites, o agente pode prosseguir sem parar para pedir confirmação. Quando
precisa ultrapassá-los, o fluxo de aprovação entra em ação.

  O ambiente isolado e as aprovações são controles diferentes que funcionam em conjunto. O
Sandbox define limites técnicos. A política de aprovação determina quando o
agente deve parar e solicitar aprovação antes de ultrapassá-los.

## O que o Sandbox faz

O Sandbox se aplica aos comandos iniciados pelo agente, não apenas às operações de arquivo
integradas. Se o agente executar ferramentas como `git`, gerenciadores de pacotes ou executores de testes,
esses comandos herdarão os mesmos limites do Sandbox.

Em cada sistema operacional, o Codex impõe os limites usando mecanismos nativos da plataforma. A implementação varia
entre macOS, Linux, WSL2 e Windows nativo, mas a ideia é a mesma em todas as
interfaces: oferecer ao agente um espaço delimitado para trabalhar, para que tarefas rotineiras sejam executadas
de forma autônoma dentro de limites claros.

## Por que isso é importante

O Sandbox reduz a fadiga causada pelas aprovações. Em vez de pedir que você confirme cada
comando de baixo risco, o agente pode ler arquivos, fazer alterações e executar comandos rotineiros do projeto
dentro dos limites que você já aprovou.

Ele também oferece um modelo de confiança mais claro para o trabalho agêntico. Você não está apenas
confiando nas intenções do agente; está confiando que ele opera
dentro de limites impostos. Assim, fica mais fácil deixar o agente trabalhar de forma independente
sem deixar de saber quando ele vai parar e pedir ajuda.

## Primeiros passos

O modo de permissões padrão ativa automaticamente o ambiente isolado.

### Pré-requisitos

No **macOS**, o ambiente isolado funciona sem configuração adicional usando o framework Seatbelt
integrado.

No **Windows**, o Codex usa o [Sandbox
do Windows](/pt-BR/codex/windows/windows-sandbox#windows-sandbox) nativo quando é executado no PowerShell e a
implementação do Sandbox no Linux quando é executado no WSL2.

No **Linux e no WSL2**, primeiro instale `bubblewrap` com seu gerenciador de pacotes:

  <div slot="ubuntu-debian">

```bash
sudo apt install bubblewrap

  </div>

  <div slot="fedora">

```bash
sudo dnf install bubblewrap

  </div>

O Codex usa o primeiro executável `bwrap` que encontra no `PATH`. Se não houver nenhum executável `bwrap`
disponível, o Codex recorre a um utilitário auxiliar incluído, mas esse utilitário
exige suporte à criação de namespaces de usuário sem privilégios. Instalar o
pacote da distribuição que fornece `bwrap` mantém essa configuração confiável.

O Codex exibe um aviso na inicialização quando `bwrap` não está disponível ou quando o utilitário auxiliar
não consegue criar o namespace de usuário necessário. Em distribuições que restringem essa
configuração do AppArmor, prefira carregar o perfil `bwrap` do AppArmor para que `bwrap` possa
continuar funcionando sem desativar a restrição globalmente.

  **Observação sobre o AppArmor no Ubuntu:** no Ubuntu 25.04, instalar `bubblewrap` pelo
  repositório de pacotes do Ubuntu deve funcionar sem configuração adicional do AppArmor. O perfil
`bwrap-userns-restrict` é fornecido no pacote `apparmor`, no caminho
`/etc/apparmor.d/bwrap-userns-restrict`.

No Ubuntu 24.04, o Codex ainda pode avisar que não consegue criar o namespace de usuário
necessário após a instalação de `bubblewrap`. Copie e carregue o perfil adicional:

```bash
sudo apt update
sudo apt install apparmor-profiles apparmor-utils
sudo install -m 0644 \
  /usr/share/apparmor/extra-profiles/bwrap-userns-restrict \
  /etc/apparmor.d/bwrap-userns-restrict
sudo apparmor_parser -r /etc/apparmor.d/bwrap-userns-restrict

`apparmor_parser -r` carrega o perfil no kernel sem exigir reinicialização. Você
também pode recarregar todos os perfis do AppArmor:

```bash
sudo systemctl reload apparmor.service

Se esse perfil não estiver disponível ou não resolver o problema, você poderá desativar
a restrição do AppArmor para namespaces de usuário sem privilégios com:

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0

## Como funcionam as permissões

Use o controle de permissões da sua interface para mudar como o Codex lida com ações
locais.

As aprovações determinam quando o Codex faz uma pausa antes de uma ação, enquanto o Sandbox
determina quais arquivos e recursos de rede os comandos podem acessar. Quando uma
aprovação oferece diferentes escopos, como aprovar uma única vez ou durante toda a sessão,
escolha o escopo mais restrito que permita continuar a tarefa. Mantenha o limite do projeto
como padrão; use projetos ou árvores de trabalho separados em vez de
ampliar o acesso a repositórios não relacionados.

O ChatGPT Work executa código e comandos de shell em um ambiente gerenciado e isolado.
A política do workspace e os controles específicos de cada ferramenta determinam quais recursos estão
disponíveis. Quando essa configuração estiver disponível, use **Configurações \> Controles de dados \> Acesso do Work
à rede** para gerenciar o acesso à rede para código e comandos de shell. Ative
**Permitir acesso à internet pública** para que esses comandos possam acessar a internet
pública. Quando essa opção está desativada, os comandos só podem acessar os nomes de host obrigatórios incluídos em uma
lista de permissões gerenciada.

A Pesquisa na Web, os Plug-ins e o navegador remoto têm controles separados.
As alterações entram em vigor depois que a execução atual de código ou shell termina e o Work
atualiza seu ambiente de execução. O ChatGPT na Web não disponibiliza o Sandbox local
do Codex nem o seletor de modo de aprovação.

No aplicativo do ChatGPT para desktop, use o controle de permissões abaixo do Editor.
Dependendo da sua configuração, o menu pode incluir **Pedir aprovação**,
**Aprovar por mim** para solicitações de aprovação elegíveis, **Acesso completo** e perfis de permissões
nomeados ou personalizados.

Na CLI, digite
[`/permissions`](/codex/developer-commands?surface=cli#cli-update-permissions-with-permissions)
para abrir o seletor de permissões e alterar o perfil de permissões ativo.

Na extensão para IDE, use o controle de permissões abaixo do Editor.
Dependendo da sua configuração, o menu pode incluir **Pedir aprovação**,
**Aprovar por mim** para solicitações de aprovação elegíveis, **Acesso completo** e perfis de permissões
nomeados ou personalizados.

<div class="not-prose my-8 max-w-[18rem] mr-auto">
  
    
      
    
  
</div>

<a id="configure-defaults"></a>

## Configurar valores padrão

Para começar sempre com o mesmo comportamento, defina os valores padrão em `config.toml`.
A [Configuração básica](/pt-BR/codex/config-file/config-basic) explica como isso funciona, e a
[Referência de configuração](/pt-BR/codex/config-file/config-reference) documenta as chaves exatas de
`sandbox_mode`, `approval_policy`, `approvals_reviewer` e
`sandbox_workspace_write.writable_roots`. Use essas configurações para definir o grau de
autonomia que o agente terá por padrão, em quais diretórios ele poderá gravar, quando deverá
pausar para solicitar aprovação e quem revisará as solicitações de aprovação elegíveis.

Em linhas gerais, os modos comuns do Sandbox são:

- `read-only`: o agente pode inspecionar arquivos, mas não pode editá-los nem executar
  comandos sem aprovação.
- `workspace-write`: o agente pode ler arquivos, fazer alterações no workspace e executar
  comandos locais rotineiros dentro desse limite. Esse é o modo padrão para trabalhar localmente
  com menos interrupções.
- `danger-full-access`: o agente opera sem as restrições do Sandbox. Isso remove
  os limites do sistema de arquivos e da rede e só deve ser usado quando você quiser
  que o agente atue com acesso completo.

As políticas de aprovação mais comuns são:

- `untrusted`: o agente pede aprovação antes de executar comandos que não estejam no seu conjunto
  de confiança.
- `on-request`: por padrão, o agente trabalha dentro do Sandbox e solicita aprovação quando
  precisa ultrapassar esse limite.
- `never`: o agente não interrompe a execução para solicitar aprovação.

Quando as aprovações são interativas, você também pode escolher quem as revisará por meio de
`approvals_reviewer`:

- `user`: as solicitações de aprovação são exibidas ao usuário. Esse é o padrão.
- `auto_review`: as solicitações de aprovação elegíveis são encaminhadas a um agente revisor (consulte a
[revisão automática](/pt-BR/codex/sandboxing/auto-review)).

Acesso completo significa usar `sandbox_mode = "danger-full-access"` junto com
`approval_policy = "never"`. Por outro lado, a predefinição de automação local de menor risco
usa `sandbox_mode = "workspace-write"` junto com
`approval_policy = "on-request"` ou as flags correspondentes da CLI
`--sandbox workspace-write --ask-for-approval on-request`. Depois, você pode manter
`approvals_reviewer = "user"` para aprovações manuais ou definir
`approvals_reviewer = "auto_review"` para a revisão automática de aprovações.

Se você precisar que o agente trabalhe em mais de um diretório, as raízes graváveis permitem
ampliar os locais que ele pode modificar sem remover totalmente o Sandbox. Se
você precisar de um limite de confiança mais amplo ou mais restrito, ajuste o modo padrão do Sandbox
e a política de aprovação em vez de depender de exceções pontuais.

Quando um fluxo de trabalho precisar de uma exceção específica, use [regras](/pt-BR/codex/agent-configuration/rules). As regras
permitem autorizar prefixos de comando fora do Sandbox, exigir aprovação para eles ou proibi-los, o que
costuma ser mais adequado do que ampliar o acesso de forma abrangente. Para saber como acessar as configurações
específicas da IDE, consulte as [configurações da extensão do Codex para IDE](/codex/developer-settings?surface=ide).

Quando disponível, a revisão automática não altera os limites do Sandbox. Ela é
uma opção de `approvals_reviewer` para solicitações de aprovação nesses limites, como
a elevação de permissões do Sandbox, o acesso bloqueado à rede ou chamadas de ferramentas com efeitos colaterais
que ainda exigem aprovação. As ações já permitidas dentro do Sandbox são executadas
sem revisão adicional. Para saber mais sobre o ciclo de vida do revisor, os tipos de acionamento, a semântica das
recusas e os detalhes de configuração, consulte a
[revisão automática](/pt-BR/codex/sandboxing/auto-review).

Os detalhes de cada plataforma estão na documentação correspondente. Para saber mais sobre configuração, comportamento
e solução de problemas no Windows nativo, consulte [Windows](/pt-BR/codex/windows/windows-sandbox). Para conhecer os requisitos administrativos
e as restrições no nível da organização relacionadas ao ambiente isolado e às aprovações, consulte
[Aprovações do agente e segurança](/pt-BR/codex/agent-approvals-security).

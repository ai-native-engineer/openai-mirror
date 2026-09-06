<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/use-your-computer-with-codex -->

## Introdução

Use o recurso [Uso do computador](/pt-BR/docs/computer-use) quando uma tarefa envolver aplicativos para desktop, janelas ou arquivos locais. O ChatGPT pode clicar, digitar e navegar nos aplicativos que você permitir e depois apresentar o resultado para revisão. Para acessar um site ou uma sessão autenticada no navegador, inicie uma tarefa separada no navegador com `@Chrome`.

**O Uso do computador requer o aplicativo do ChatGPT para desktop.** Nas regiões compatíveis, o Uso do computador está disponível no macOS e no Windows, no ChatGPT Work e no Codex. As tarefas do Work na nuvem, executadas na Web ou em dispositivos móveis, não podem acessar diretamente seus aplicativos e arquivos locais nem as sessões autenticadas do navegador para desktop. Ao conectar um host Mac ou Windows, você pode iniciar ou orientar uma tarefa no desktop pelo [Remoto em dispositivos móveis](/pt-BR/codex/remote-connections).

Bons exemplos são transferir anotações para um sistema de registro, consultar o contexto em alguns aplicativos antes de redigir uma resposta ou copiar detalhes aprovados entre ferramentas que não contam com um plug-in dedicado.

Veja como delegar com segurança uma tarefa no desktop quando seus planos para um fim de semana em uma cabana estão nos aplicativos Mensagens e Notas:

<div data-use-case-export-only>

**Tarefa no desktop:** Reúna ideias para um fim de semana em uma cabana com base nas conversas do aplicativo Mensagens e em uma lista de cabanas pré-selecionadas no aplicativo Notas, crie uma anotação local e redija uma resposta.

**Resultado:** Pine Lodge tem acesso sem degraus, fica a até duas horas de distância e custa $690 no total. Lake House pode ser uma opção, mas o tempo de viagem e a acessibilidade ainda precisam ser confirmados. Cedar Ridge foi descartada porque há escadas. O tamanho do grupo é desconhecido, então o preço por pessoa depende dessa informação.

A anotação local e o rascunho de resposta estão prontos para revisão. Nenhuma reserva foi feita e nada foi enviado.

</div>

## Como usar

1. Abra o aplicativo do ChatGPT para desktop e instale o [plug-in de Uso do computador](/pt-BR/docs/computer-use).
2. Comece sua solicitação com `@Computer` para usar aplicativos de desktop ou com `@Chrome` para tarefas no navegador.
3. Descreva a tarefa, os aplicativos ou arquivos envolvidos e o resultado desejado.
4. Revise as solicitações de acesso e faça uma pausa antes de ações que enviem, submetam ou alterem dados importantes.
5. No Windows, mantenha o aplicativo de destino visível enquanto o Uso do computador estiver em execução.

Se houver um plug-in para um aplicativo, o ChatGPT poderá usá-lo para realizar a ação estruturada. O Uso do computador é útil quando a tarefa depende da interface do aplicativo ou não há um plug-in disponível.

## O que experimentar

Comece com uma ferramenta: use `@Computer` para aplicativos de desktop e arquivos locais ou `@Chrome` para o navegador. O ChatGPT pode escolher outras ferramentas conforme necessário.

**Transforme mensagens em um plano**

**Encontre lugares para se hospedar**

**Atualize-se sobre um projeto**

**Atualize uma ferramenta de acompanhamento com base nas notas da reunião**

**Trabalhe no navegador em que você já fez login**

**Teste um site**

**Organize os arquivos locais**

**Mostre ao ChatGPT o que você está vendo**

No macOS, use uma [captura do app](/pt-BR/codex/appshots) para compartilhar a janela do aplicativo que está à sua frente. As capturas do app fornecem contexto visual; com isso, o Uso do computador pode abrir e inspecionar o aplicativo e interagir com ele, se você permitir.

## Dicas práticas

### Entenda como a tarefa é executada em cada computador

No macOS, o Uso do computador pode funcionar em segundo plano enquanto você usa outros aplicativos. Uma visualização em picture-in-picture mostra o aplicativo ativo; abra-a para acompanhar a tarefa ou mova-a para onde não atrapalhe. Se você usa um mascote, pode mover a visualização para ele.

No Windows, o Uso do computador é executado na área de trabalho ativa e assume o controle em primeiro plano. O ponteiro se moverá e o teclado será acionado durante a execução da tarefa. Mantenha o dispositivo desbloqueado e conectado ou execute o aplicativo para desktop em uma máquina virtual do Windows se precisar continuar usando sua área de trabalho principal.

### Escolha o navegador certo

As tarefas no navegador costumam fazer parte do Uso do computador. Escolha o navegador que tenha o contexto necessário:

- **[Extensão do Chrome](/pt-BR/codex/chrome-extension):** Use `@Chrome` para tarefas no navegador, incluindo pesquisas de anúncios, acesso a sites e uso do seu perfil do Chrome com sessão iniciada, de abas ou de extensões.
- **[Navegador integrado](/pt-BR/codex/browser?surface=app):** Use-o quando quiser uma sessão de navegador separada para localhost ou sites públicos. Ele mantém seu próprio estado de navegação e pode aguardar enquanto você faz login.
- **Navegador na nuvem do ChatGPT Work na Web ou em dispositivos móveis:** Use-o para acessar sites públicos compatíveis sem fazer login. Ele não pode acessar arquivos locais, abas abertas, extensões ou senhas salvas, fazer login em sites nem concluir pagamentos.

Quando necessário, informe o navegador no prompt e use a [personalização](/pt-BR/docs/customization/overview) para definir uma preferência recorrente para a área de trabalho.

### Evite execuções paralelas no mesmo aplicativo

Não execute duas tarefas de Uso do computador no mesmo aplicativo ao mesmo tempo. Ações simultâneas podem alterar a janela ou o estado atual e tornar o resultado pouco confiável.

### Prepare os aplicativos com sessão iniciada e o uso com tela bloqueada

Antes de iniciar uma tarefa na área de trabalho, faça login nos aplicativos e serviços necessários. No macOS, você pode ativar o [uso com tela bloqueada](/pt-BR/docs/computer-use#locked-use) se a tarefa precisar continuar após o bloqueio do Mac. O uso com tela bloqueada não está disponível para o Uso do computador no Windows.

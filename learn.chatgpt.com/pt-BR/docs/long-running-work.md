<!-- source: https://learn.chatgpt.com/pt-BR/docs/long-running-work -->

Para trabalhos que possam exigir muitas etapas, forneça ao ChatGPT um resultado claro, as restrições
e os critérios de conclusão. Mantenha os trabalhos relacionados no mesmo chat para que
o ChatGPT possa usar o mesmo contexto para escolher a próxima etapa e determinar quando o
trabalho foi concluído.

No aplicativo do ChatGPT para desktop, digite `/goal` para iniciar o modo Meta. A linha de progresso
permite pausar, retomar, editar ou remover a meta enquanto o ChatGPT trabalha.

Para trabalhos de longa duração hospedados no ChatGPT na Web, use o ChatGPT Work e inclua o
resultado, as restrições e os critérios de revisão diretamente no seu prompt.

Continue no mesmo chat na Web para adicionar contexto, alterar restrições ou
pedir uma atualização de status. Use chats separados quando tarefas independentes puderem ser executadas em
paralelo e evite conceder a duas tarefas acesso de gravação à mesma fonte conectada.
Para trabalhos relacionados, mantenha os chats e os arquivos-fonte juntos em um
[projeto](/pt-BR/codex/projects).

Em uma sessão interativa do Codex CLI, digite `/goal` para iniciar o modo Meta. Continue
na mesma sessão para orientar o trabalho ou pedir uma atualização de status.

No chat da extensão para IDE, digite `/goal` para iniciar o modo Meta no
workspace aberto. Continue no mesmo chat para orientar a tarefa durante a execução.

  
    
  

<a id="start-a-goal"></a>
<a id="define-what-done-means"></a>
<a id="steer-a-running-goal"></a>
<a id="run-goals-in-parallel"></a>
<a id="related-docs"></a>

## Inicie uma meta

Digite `/goal` no aplicativo do ChatGPT para desktop, no Codex CLI ou na extensão para IDE. O
texto da meta passa a ser tanto o primeiro prompt quanto os critérios de conclusão da
tarefa.

Se o resultado ainda não estiver claro, comece com `/plan`. Peça ao ChatGPT para entrevistar você,
identificar as restrições e transformar o resultado em uma meta com critérios de sucesso
mensuráveis. Depois, inicie a meta refinada com `/goal`.

## Defina os critérios de conclusão

Escreva uma meta que permita ao ChatGPT verificar o próprio progresso. Inclua estes três elementos quando
forem aplicáveis:

| Elemento da meta     | O que incluir                                                               |
| ---------------- | ----------------------------------------------------------------------------- |
| **Resultado**      | Descreva o resultado desejado, não apenas a atividade que o ChatGPT deve realizar.   |
| **Restrições**  | Liste as ferramentas necessárias, os limites, os requisitos de compatibilidade ou as abordagens a evitar. |
| **Verificação** | Adicione testes, medições ou critérios de revisão que comprovem a conclusão do trabalho.  |

Por exemplo:

```text
Migrate this codebase from JavaScript to TypeScript. Preserve existing behavior,
compile in strict mode without explicit `any` types, and make the full test suite pass.

## Oriente uma meta em execução

No aplicativo do ChatGPT para desktop, a linha de progresso da meta aparece acima do Editor. Use-a para
pausar ou retomar o trabalho, editar a meta ou removê-la. Você também pode enviar mensagens de acompanhamento
enquanto a meta estiver em execução para adicionar contexto ou ajustar as restrições.

Use um chat secundário quando quiser um resumo do status ou uma explicação sem
interromper o chat principal. Pause a meta se prever que vai perder a
conexão e retome-a quando estiver tudo pronto para o ChatGPT continuar.

<a id="steer-a-running-task"></a>

## Oriente o trabalho em execução

Continue no mesmo chat para adicionar contexto, ajustar as restrições ou pedir
um resumo do status. Inicie um chat separado quando outra tarefa puder ser executada
de forma independente.

## Oriente uma meta em execução

Envie uma mensagem de acompanhamento na mesma sessão interativa para adicionar contexto ou
ajustar as restrições. Peça um resumo do status quando quiser que o Codex resuma
o progresso antes de continuar.

## Oriente uma meta em execução

Continue no mesmo chat da IDE para adicionar contexto, ajustar as restrições ou pedir um
resumo do status. Mantenha o workspace disponível enquanto a meta estiver em execução.

Iniciar uma meta não concede ao ChatGPT acesso mais amplo. Ele mantém o mesmo
[Sandbox e a mesma política de aprovação](/pt-BR/codex/sandboxing) e pausa quando
precisa de uma decisão. Com [revisões automáticas de
aprovação](/pt-BR/codex/sandboxing/auto-review), um revisor independente pode
avaliar solicitações elegíveis sem ampliar esses limites.

## Execute metas em paralelo

Cada chat mantém seu próprio contexto, suas mensagens, seus resultados e sua meta. Execute chats
simultaneamente, mas evite que dois chats alterem os mesmos arquivos. Use
[árvores de trabalho](/pt-BR/codex/environments/git-worktrees) para disponibilizar checkouts separados aos chats de programação
em paralelo.

Para trabalhos locais, ative **Impedir repouso durante a execução** em Configurações para que seu Mac
permaneça ativo. Use [Mascotes](/pt-BR/codex/pets?surface=app) ou [notificações do
sistema](/pt-BR/codex/notifications?surface=app) para saber quando um chat precisa de uma ação sua
ou está pronto para revisão.

## Documentação relacionada

- [Projetos e chats](/pt-BR/codex/projects)
- [Modo Meta e criação de prompts](/pt-BR/codex/prompting#goal-mode)
- [Árvores de trabalho do Git](/pt-BR/codex/environments/git-worktrees)

## Documentação relacionada

- [Projetos e chats](/pt-BR/codex/projects)
- [Tarefas agendadas](/pt-BR/codex/automations)
- [Sandbox e permissões](/pt-BR/codex/sandboxing)

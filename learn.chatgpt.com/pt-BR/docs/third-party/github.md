<!-- source: https://learn.chatgpt.com/pt-BR/docs/third-party/github -->

Use a revisão de código do Codex para fazer mais uma rodada de revisão com achados relevantes em pull
requests do GitHub. O Codex analisa o diff da pull request, segue as orientações do seu repositório
e publica uma revisão de código padrão do GitHub voltada a problemas graves. A Revisão de
segurança, disponível em prévia de pesquisa, faz uma análise mais aprofundada de
possíveis problemas de segurança em uma pull request.

<br />

## Antes de começar

Verifique se você tem:

- O [Codex Cloud](/pt-BR/codex/cloud) configurado para o repositório que você quer revisar.
- Acesso às [configurações de revisão de código do Codex](https://chatgpt.com/codex/settings/code-review).
- Um arquivo `AGENTS.md`, caso queira que o Codex siga orientações de revisão específicas do repositório.

## Configurar a revisão de código do Codex

Para configurar revisões automáticas, você precisa de um repositório do GitHub conectado e
de permissão de push ou de administrador no GitHub para as configurações do repositório.

1. Configure o [Codex Cloud](/pt-BR/codex/cloud).
2. Acesse as [configurações do Codex](https://chatgpt.com/codex/settings/code-review).
3. Ative a **Revisão de código** no seu repositório.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## Solicitar uma revisão do Codex

1. Em um comentário da pull request, mencione `@codex review`.
2. Aguarde o Codex reagir (👀) e publicar uma revisão.

<div class="not-prose max-w-xl mr-auto">
  
    
      
    
  
</div>
<br />

O Codex publica uma revisão na pull request, como faria alguém da sua equipe. No
GitHub, o Codex sinaliza apenas problemas P0 e P1, para que os comentários da revisão se concentrem em
riscos de alta prioridade.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## Ativar revisões automáticas

Se quiser que o Codex revise automaticamente todas as pull requests, ative
**Revisões automáticas** nas [configurações do Codex](https://chatgpt.com/codex/settings/code-review).
O Codex publicará uma revisão sempre que alguém abrir uma nova PR para revisão, sem
precisar de um comentário com `@codex review`.

## Personalizar o que o Codex revisa

O Codex procura arquivos `AGENTS.md` no seu repositório e segue as regras aplicáveis de
revisão de código. Adicione uma seção `## Code Review Rules` ao arquivo mais próximo
do código ao qual as regras se aplicam. Quando for útil, use títulos `###` para agrupar verificações
relacionadas.

Por exemplo, um serviço de relatórios de experimentos pode impedir que o comportamento pós-exposição
altere uma coorte de comparação:

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Coloque as regras válidas para todo o repositório no arquivo `AGENTS.md` da raiz e as regras específicas do serviço
em um arquivo aninhado, como `services/experiment_reporting/AGENTS.md`. O Codex
aplica as orientações da raiz e as mais específicas que abrangem cada arquivo alterado. Assim,
alterações não relacionadas não precisam incluir contexto específico do serviço.

Comece com duas ou três regras concisas que formalizem verificações que os revisores explicam com frequência. Regras úteis:

- **Concentre-se em comportamentos relevantes e específicos do repositório.** Descreva a
  restrição de compatibilidade, o limite de dados ou o efeito colateral inseguro que deve ser sinalizado e
  por que isso é importante.
- **Informe o caminho seguro ou a exceção.** Dê ao Codex contexto suficiente para distinguir
  um problema real de um comportamento esperado.
- **Mantenha as regras com escopo delimitado e estáveis ao longo do tempo.** Dê preferência aos resultados, não a nomes de funções que
  podem mudar, e coloque as orientações perto do código ao qual se aplicam.
- **Deixe as verificações mecânicas na CI.** Não inclua nas regras de revisão formatação, lint ou outras
  verificações determinísticas.

Abra uma pull request representativa e solicite uma revisão com `@codex review`.
Aprimore as regras com base nos achados e no feedback que receber; reduza o escopo ou
remova orientações que gerem ruído.

As regras de revisão de código orientam o Codex; elas não substituem testes, proteções de branch nem
aprovações obrigatórias.

Para definir um foco pontual, inclua-o no comentário da pull request:

`@codex review for issues in the database migration`

## Revisão de segurança

A Revisão de segurança é uma revisão adicional para clientes que querem
dedicar atenção especial a problemas de segurança em pull requests. Ela analisa
os riscos específicos de segurança de forma mais aprofundada do que a Revisão de código, considerando o diff da pull request,
o contexto relevante do repositório e os modelos de ameaças ou as orientações de
segurança configurados.

A Revisão de código também pode identificar problemas de segurança como parte da revisão
geral. Por isso, pode haver sobreposição ocasional entre os achados da Revisão de código e da Revisão de
segurança.

### Configurar a Revisão de segurança

Para conhecer as instruções e opções de configuração em mais detalhes, consulte [Revisão de
segurança](/pt-BR/codex/security/security-review).

1. Configure o [Codex Cloud](/pt-BR/codex/cloud).
2. Acesse as [configurações do Codex](https://chatgpt.com/codex/settings/code-review).
3. Em **Preferências do repositório**, escolha quais pull requests receberão a Revisão de
   segurança e quando ela será executada. Selecione **Sempre que a revisão de código for executada** para executá-la
   junto com a Revisão de código.

### Solicitar uma Revisão de segurança

Para solicitar manualmente uma Revisão de segurança, adicione este comentário a uma pull request:

`@codex security review`

O Codex reage enquanto a revisão está em andamento e, em seguida, publica os achados de segurança diretamente
na pull request. Abra a tarefa correspondente do Codex e selecione a aba **Relatório de
segurança** para ver o relatório completo.

## Agir com base nos achados da revisão

Depois que o Codex publicar uma revisão, você poderá pedir a ele que corrija os problemas na mesma pull
request deixando outro comentário:

```md
@codex fix the P1 issue

O Codex inicia um chat na nuvem com a pull request como contexto e pode enviar uma correção
para a branch quando tiver permissão para isso.

## Atribuir outras tarefas ao Codex

Se você mencionar `@codex` em um comentário com algo diferente de `review`, o Codex iniciará um [chat na nuvem](/pt-BR/codex/cloud) usando a pull request como contexto.

```md
@codex fix the CI failures

## Solucionar problemas da revisão de código

Se o Codex não reagir ou não publicar uma revisão:

- Confirme se você ativou a **Revisão de código** para o repositório nas [configurações do Codex](https://chatgpt.com/codex/settings/code-review).
- Confirme se a pull request pertence a um repositório com o [Codex Cloud](/pt-BR/codex/cloud) configurado.
- Use exatamente o gatilho `@codex review` em um comentário da pull request.
- Para revisões automáticas, verifique se você ativou **Revisões automáticas** e se
  o evento da pull request corresponde às configurações do gatilho de revisão.

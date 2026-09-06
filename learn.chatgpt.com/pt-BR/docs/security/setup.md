<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/setup -->

Esta página orienta você desde o acesso inicial até a revisão das constatações e a criação de pull requests de correção
no Codex Security na nuvem.

  Primeiro, confirme se você já configurou o Codex Cloud. Caso contrário, consulte [Codex
  Cloud](/pt-BR/codex/cloud) para começar.

## 1. Acesso e ambiente

O Codex Security na nuvem verifica repositórios do GitHub conectados por meio do
[Codex Cloud](/pt-BR/codex/cloud).

- Confirme se seu workspace tem acesso ao Codex Security na nuvem.
- Confirme se o repositório que você quer verificar está disponível no Codex Cloud.

Acesse [Ambientes do Codex](https://chatgpt.com/codex/settings/environments) e verifique se o repositório já tem um ambiente. Caso contrário, crie um nessa página antes de continuar.

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

## 2. Nova verificação de segurança

Quando o ambiente estiver disponível, acesse [Criar uma verificação de segurança](https://chatgpt.com/codex/security/scans/new) e escolha o repositório que você acabou de conectar.

O Codex Security verifica os repositórios começando pelos commits mais recentes e retrocedendo para os anteriores. Assim, ele cria e atualiza o contexto da verificação à medida que novos commits chegam.

Para configurar um repositório:

1. Selecione a organização do GitHub.
2. Selecione o repositório.
3. Selecione a branch que você quer verificar.
4. Selecione o ambiente.
5. Escolha uma **janela de histórico**. Janelas mais longas oferecem mais contexto, mas a verificação retroativa leva mais tempo.
6. Clique em **Criar**.

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

## 3. As verificações iniciais podem levar algum tempo

Quando você cria a verificação, o Codex Security primeiro faz uma análise de segurança no nível dos commits em toda a janela de histórico selecionada.
A verificação retroativa inicial pode levar algumas horas, especialmente em repositórios maiores ou com janelas mais longas.
É normal que as constatações não apareçam imediatamente. Aguarde a conclusão da verificação inicial antes de abrir um chamado ou tentar solucionar o problema.

  A configuração da verificação inicial é automática e abrangente. Esse processo pode levar algumas horas. Não
se preocupe se o primeiro conjunto de constatações demorar a aparecer.

## 4. Revise as verificações e aprimore o modelo de ameaças

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

Quando a verificação inicial terminar, abra a verificação e revise o modelo de ameaças gerado.
Depois que as constatações iniciais aparecerem, atualize o modelo de ameaças para que corresponda à sua arquitetura, aos limites de confiança e ao contexto de negócios.
Isso ajuda o Codex Security a priorizar os issues para sua equipe.

  Se quiser alterar os resultados da verificação, você pode editar o modelo de ameaças com
informações atualizadas sobre escopo, prioridades e premissas.

Depois que as constatações iniciais aparecerem, revise o modelo para manter as orientações da verificação alinhadas às prioridades atuais.
Mantê-lo atualizado ajuda o Codex Security a produzir sugestões melhores.

Para uma explicação mais detalhada sobre modelos de ameaças e como eles afetam a criticidade e a triagem, consulte [Aprimorar o modelo de ameaças](/pt-BR/codex/security/threat-model).

## 5. Revise as constatações e aplique correções

Após a conclusão da verificação retroativa inicial, revise as constatações na visualização **Constatações** .

Você pode usar duas visualizações:

- **Constatações recomendadas**: uma lista dinâmica dos 10 issues mais críticos do repositório
- **Todas as constatações**: uma tabela de constatações de todo o repositório que pode ser ordenada e filtrada

  
    
  

Clique em uma constatação para abrir a página de detalhes correspondente, que inclui:

- uma descrição concisa do issue
- metadados importantes, como detalhes do commit e caminhos de arquivos
- raciocínio contextual sobre o impacto
- trechos de código relevantes
- contexto do caminho de chamadas ou do fluxo de dados, quando disponível
- etapas e saída da validação

Você pode revisar cada constatação e criar um PR diretamente na página de detalhes da constatação.

## Documentação relacionada

- [Codex Security](/pt-BR/codex/security) apresenta uma visão geral do produto.
- A página [Perguntas frequentes sobre o Codex Security na nuvem](/pt-BR/codex/security/faq) aborda dúvidas comuns sobre a nuvem.
- A página [Aprimorar o modelo de ameaças](/pt-BR/codex/security/threat-model) explica como aprimorar o contexto da verificação e a priorização das constatações.

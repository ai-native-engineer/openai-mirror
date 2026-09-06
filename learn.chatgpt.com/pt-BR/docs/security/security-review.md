<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/security-review -->

A Revisão do Codex Security está disponível em uma versão prévia para pesquisa.
Ela está disponível para clientes dos planos ChatGPT Enterprise, Business, Edu e Pro, mas
não está disponível no Plus. Durante o período inicial, a Revisão do Codex Security
não consome créditos do ChatGPT. Podem ser aplicados limites de uso.

A Revisão do Codex Security é uma revisão adicional para clientes que desejam
dar atenção especial a issues de segurança em pull requests.

A Revisão do Codex Security faz uma análise mais aprofundada dos riscos específicos de segurança do que a [Revisão de
código](/pt-BR/codex/third-party/github), analisando o
diff do pull request, o contexto relevante do repositório e os modelos de ameaças configurados
ou as orientações de segurança definidas. A Revisão de código também pode identificar issues relacionados à segurança como
parte da revisão geral, por isso pode haver alguma sobreposição entre os achados.

## Antes de começar

Para configurar a execução automática da Revisão do Codex Security, você precisa de:

- Acesso do seu workspace à versão prévia para pesquisa da Revisão do Codex Security
- O [Codex Cloud](/pt-BR/codex/cloud) configurado com um repositório do GitHub conectado
- Permissão de push ou de administrador no GitHub para acessar as configurações do repositório

Uma verificação existente do Codex Security é opcional.

<a id="configure-security-review"></a>

## Configurar a Revisão do Codex Security

1. Acesse as [configurações do Codex](https://chatgpt.com/codex/settings/code-review).
2. Em **Preferências do repositório**, escolha quais pull requests receberão a Revisão do Codex
   Security:
   - **Seguir preferências pessoais** permite que cada colaborador ative o recurso nas próprias configurações pessoais da
     Revisão do Codex Security.
   - **Revisar todos os PRs** se aplica a todos os pull requests do repositório.
   - **Revisar PRs da equipe**, quando disponível, se aplica aos pull requests abertos por
     membros do seu workspace do ChatGPT, não por membros de uma equipe do GitHub.
3. Escolha quando a Revisão do Codex Security será executada:
   - A opção **Ao abrir o PR** executa a revisão de forma independente quando um pull request é aberto.
   - A opção **A cada push** executa a revisão de forma independente após o push de novos commits.
   - A opção **Sempre que a revisão de código for executada** exige a Revisão de código e executa a Revisão do Codex
     Security junto com ela.

## Adicionar contexto do modelo de ameaças

Você pode configurar um modelo de ameaças para fornecer ao Codex contexto sobre seu aplicativo:
os ativos, os limites de confiança, as premissas de segurança e os riscos específicos do repositório.
Se o repositório tiver uma configuração já existente de verificação do Codex Security, você poderá usar
o modelo de ameaças dessa configuração. Caso contrário, informe o caminho de um arquivo de modelo de ameaças versionado
no repositório. Se você não especificar uma origem, o Codex gera novamente o
modelo de ameaças a cada revisão.

## Definir limites de severidade

Por padrão, nas revisões automáticas do Codex Security, achados de severidade **Alta** e **Crítica**
são relatados; nas revisões solicitadas manualmente, são relatados achados de severidade **Média**, **Alta** e
**Crítica**. Você pode alterar a severidade mínima de forma independente para
revisões automáticas e manuais e adicionar regras específicas por caminho.

Os achados publicados em um pull request herdam a visibilidade desse pull request no GitHub.
Qualquer pessoa que possa ver o pull request também pode ver esses achados,
inclusive em repositórios públicos ou em pull requests de colaboradores de fora
do seu workspace. Escolha com cuidado os limites de severidade em repositórios nos quais
os comentários em pull requests possam ter ampla visibilidade. O limite de severidade controla
o que o Codex publica no GitHub; o relatório completo da Revisão do Codex Security permanece no
Codex.

<a id="request-a-security-review"></a>

## Solicitar uma Revisão do Codex Security

Para solicitar manualmente uma Revisão do Codex Security, adicione este comentário a um pull request:

`@codex security review`

O Codex adiciona uma reação enquanto a revisão está em andamento e depois publica diretamente no pull request os achados que atendem ao seu
limite de severidade para revisões manuais. Abra a tarefa associada do
Codex e selecione a aba **Relatório de segurança** para ver o relatório completo,
incluindo a severidade, o caminho de ataque, as evidências de suporte, a validação e
as orientações de remediação. Se nenhum issue atender ao limite de severidade, o Codex não
publica achados no pull request.

## Documentação relacionada

- [Revisar pull requests do GitHub com o Codex](/pt-BR/codex/third-party/github) explica a Revisão de código e a integração com o GitHub.
- [Codex Security](/pt-BR/codex/security) apresenta uma visão geral do produto.
- [Configuração do Codex Security na nuvem](/pt-BR/codex/security/setup) explica as verificações de repositórios e a revisão de achados.
- [Aprimorar o modelo de ameaças](/pt-BR/codex/security/threat-model) explica como ajustar o contexto do repositório.

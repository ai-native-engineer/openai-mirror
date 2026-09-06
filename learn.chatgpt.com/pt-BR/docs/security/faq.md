<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/faq -->

Estas perguntas frequentes abordam o Codex Security na nuvem. Para varreduras locais e fluxos de trabalho executados em
uma tarefa do Codex, consulte o [início rápido do Plugin Codex Security](/pt-BR/codex/security/plugin).

{/* vale Microsoft.Auto = NO */}
{/* vale Vale.Spelling = NO */}

## Primeiros passos

### O que é o Codex Security?

A segurança de software continua sendo um dos problemas mais difíceis e importantes da engenharia. O Codex Security é um conjunto de ferramentas de análise de segurança baseado em LLM que inspeciona o código-fonte e retorna descobertas estruturadas de vulnerabilidades, classificadas por prioridade e acompanhadas de patches propostos. Ele ajuda desenvolvedores e equipes de segurança a identificar e corrigir problemas de segurança em escala.

### Por que isso é importante?

O software é fundamental para a indústria e a sociedade modernas, e as vulnerabilidades geram riscos sistêmicos. O Codex Security oferece suporte a um fluxo de trabalho que prioriza a defesa, identificando continuamente possíveis problemas, validando-os quando possível e propondo correções. Isso ajuda as equipes a reforçar a segurança sem desacelerar o desenvolvimento.

### Que problema de negócio o Codex Security resolve?

O Codex Security encurta o caminho entre a suspeita de um problema e uma descoberta confirmada e reproduzível, acompanhada de evidências e um patch proposto. Isso reduz a carga de triagem e os falsos positivos em relação ao uso isolado de scanners tradicionais.

### Como funciona o Codex Security?

O Codex Security executa a análise em um contêiner efêmero e isolado e clona temporariamente o repositório de destino. Ele realiza uma análise no nível do código e retorna descobertas estruturadas que incluem descrição, arquivo e localização, criticidade, causa raiz e uma correção sugerida.

No caso de descobertas que incluem etapas de verificação, o sistema executa os comandos ou testes propostos no mesmo Sandbox, registra êxito ou falha, códigos de saída, stdout, stderr, resultados dos testes e quaisquer diffs ou artefatos gerados, e anexa essa saída como evidência para revisão.

### Isso substitui o SAST?

Não. O Codex Security complementa o SAST. Ele acrescenta raciocínio semântico baseado em LLM e validação automática, enquanto as ferramentas SAST existentes continuam oferecendo ampla cobertura determinística.

## Recursos

### O que é o pipeline de análise?

O Codex Security segue um pipeline dividido em etapas:

1. A **análise** cria um modelo de ameaças para o repositório.
2. A **varredura de commits** analisa os commits mesclados e o histórico do repositório em busca de possíveis problemas.
3. A **validação** tenta reproduzir possíveis vulnerabilidades em um Sandbox para reduzir falsos positivos.
4. A **criação de patches** integra-se ao Codex para propor patches que os revisores podem inspecionar antes de abrir uma PR.

O Codex Security atua em conjunto com engenheiros no GitHub, no Codex e nos fluxos de trabalho padrão de revisão.

### Quais linguagens são compatíveis?

O Codex Security não depende de uma linguagem específica. Na prática, o desempenho depende da capacidade de raciocínio do modelo para a linguagem e o framework usados no repositório.

### O que recebo após a conclusão da varredura?

Você recebe descobertas classificadas por prioridade, com criticidade, status da validação e um patch proposto, quando disponível. As descobertas também podem incluir a saída da falha, evidências de reprodução, o contexto do caminho de chamadas e anotações relacionadas.

### Como o código do cliente é isolado?

Cada tarefa de análise e validação é executada em um contêiner efêmero do Codex com ferramentas restritas ao escopo da sessão. Os artefatos são extraídos para revisão, e o contêiner é removido após a conclusão da tarefa.

### O Codex Security aplica patches automaticamente?

Não. O patch proposto é uma correção recomendada. Os usuários podem revisá-lo e enviá-lo ao GitHub como uma PR pela interface de descobertas, mas o Codex Security não aplica automaticamente alterações ao repositório.

### É necessário fazer o build do projeto para realizar a varredura?

Não. O Codex Security pode gerar descobertas com base no contexto do repositório e dos commits, sem uma etapa de compilação. Durante a validação automática, ele pode tentar fazer o build do projeto dentro do contêiner se isso ajudar a reproduzir o problema. Para saber mais sobre a configuração do ambiente, consulte [Ambientes de nuvem do Codex](/pt-BR/codex/environments/cloud-environment).

### Como o Codex Security reduz falsos positivos e evita patches que não funcionam?

O Codex Security usa duas etapas. Primeiro, o modelo classifica os possíveis problemas por prioridade. Depois, a validação automática tenta reproduzir cada problema em um contêiner limpo. As descobertas reproduzidas com sucesso são marcadas como validadas, o que ajuda a reduzir falsos positivos antes da revisão humana.

### Quanto tempo levam as varreduras iniciais e o que acontece depois?

O tempo da varredura inicial depende do tamanho do repositório, do tempo de build e de quantas descobertas avançam para a validação. Em alguns repositórios, as varreduras podem levar várias horas. Em repositórios maiores, podem levar vários dias. As varreduras posteriores geralmente são mais rápidas porque se concentram em novos commits e alterações incrementais.

### O que é um modelo de ameaças?

Um modelo de ameaças é o contexto de segurança usado durante a varredura de um repositório. Ele combina uma visão geral concisa do projeto com detalhes sobre a superfície de ataque, como pontos de entrada, limites de confiança, premissas de autenticação e componentes que apresentam riscos. Para saber mais, consulte [Aprimorar o modelo de ameaças](/pt-BR/codex/security/threat-model).

### Como um modelo de ameaças é gerado?

O Codex Security solicita ao modelo que resuma a arquitetura do repositório e os pontos de entrada relacionados à segurança, classifique o tipo de repositório, execute extratores especializados e combine os resultados em uma visão geral do projeto ou em um artefato de modelo de ameaças usado durante toda a varredura.

### Isso substitui a revisão manual de segurança?

Não. O Codex Security acelera a revisão e ajuda a classificar as descobertas por prioridade, mas não substitui a validação no nível do código, as verificações de explorabilidade nem a avaliação humana das ameaças.

### Posso editar o modelo de ameaças?

Sim. O Codex Security cria o modelo de ameaças inicial, e você pode atualizá-lo à medida que a arquitetura, os riscos e o contexto de negócios mudam. Para conhecer o fluxo de trabalho de edição, consulte [Aprimorar o modelo de ameaças](/pt-BR/codex/security/threat-model).

### Preciso configurar uma varredura antes de usar a modelagem de ameaças?

Sim. As orientações para o modelo de ameaças dependem de como e do que você verifica, por isso é preciso configurar o repositório primeiro. Consulte [Configuração do Codex Security](/pt-BR/codex/security/setup).

### O que contém o patch proposto?

Quando é possível gerar uma correção para a descoberta, o patch proposto contém um diff mínimo que pode ser aplicado, com o nome do arquivo e as linhas de contexto.

### O patch modifica diretamente a branch da minha PR?

Não. O fluxo de trabalho gera um diff, um arquivo de patch ou uma alteração sugerida para inspeção pelos mantenedores e revisores antes que as alterações sejam aplicadas.

## Validação

### O que é a validação automática?

A validação automática é a etapa que tenta reproduzir um possível problema em um contêiner isolado. Ela registra o sucesso ou a falha da reprodução e captura logs, comandos e artefatos relacionados como evidência.

### O que acontece se a validação falhar?

A descoberta permanece sem validação. Os logs e relatórios ainda registram as tentativas feitas, para que os engenheiros possam tentar novamente, aprofundar a investigação ou ajustar as etapas de reprodução.

{/* vale Microsoft.Auto = YES */}
{/* vale Vale.Spelling = YES */}

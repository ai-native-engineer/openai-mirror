<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/chatgpt-apps -->

## O que você vai criar

Todo plug-in com suporte de MCP é composto por três partes:

- Um servidor MCP que define ferramentas, retorna dados, aplica as regras de autenticação e direciona o ChatGPT aos recursos de interface disponíveis.
- Um componente Web opcional renderizado em um iframe do ChatGPT. Você pode criá-lo com React ou apenas com HTML, CSS e JavaScript.
- Um modelo que decide quando chamar as ferramentas do plug-in com base nos metadados fornecidos.

O Codex é mais útil quando fica responsável pelo trabalho repetitivo de engenharia relacionado a essas partes:

- Planejar o escopo e os metadados das ferramentas.
- Criar a estrutura inicial do servidor e do widget.
- Configurar scripts para execução local.
- Adicionar autenticação e alterações de implantação em etapas bem delimitadas.
- Criar o ciclo de verificação que comprova que o plug-in funciona no ChatGPT.

## Por que o Codex é uma ótima opção

- Os plug-ins com suporte de MCP se dividem claramente em um servidor, uma interface opcional e
chamadas de ferramentas orientadas pelo modelo.
- A criação de prompts para o Codex funciona melhor quando a tarefa é explícita, tem escopo delimitado e
é simples de verificar, o que combina bem com o trabalho de criação de plug-ins.
- As Habilidades e `AGENTS.md` fornecem ao Codex as instruções reutilizáveis e as regras do projeto necessárias para trabalhar com base no contexto correto.

Para saber mais sobre como instalar e usar Habilidades, consulte nossa [documentação sobre Habilidades](/pt-BR/codex/build-skills).

## Como usar

## Pré-requisitos

- Comece com um único resultado principal para o usuário, em vez de tentar levar um produto inteiro para o chat.
- Escolha a stack logo no início: TypeScript ou Python para o servidor e React ou apenas HTML, CSS e JavaScript para o widget.
- Defina como disponibilizar o acesso por HTTPS durante o desenvolvimento, por exemplo, com `ngrok` ou Cloudflare Tunnel.
- Algumas configurações ainda usam termos antigos para uma conexão com um servidor MCP. Durante
os testes locais, considere que esses rótulos se referem ao servidor registrado.

1. Comece com um resultado específico para o plug-in e peça ao Codex que proponha de três a cinco ferramentas, definindo com clareza nomes, descrições, entradas e saídas.
2. Decida se a v1 pode trabalhar apenas com dados ou se precisa de um widget. Depois, crie a estrutura inicial do servidor MCP e do widget opcional seguindo os padrões existentes no repositório antes de adicionar dependências.
3. Execute o servidor MCP localmente e exponha-o por HTTPS, conecte-o ao ChatGPT no modo de desenvolvedor e teste-o com um pequeno conjunto de prompts diretos, indiretos e negativos.
4. Ajuste os metadados, o gerenciamento de estado, `structuredContent` e os payloads de `_meta` até que o fluxo principal de leitura funcione de maneira confiável no ChatGPT.
5. Adicione OAuth 2.1 somente quando dados específicos de cada usuário ou ações de gravação exigirem isso, sem complicar os fluxos anônimos ou somente leitura.
6. Prepare uma prévia hospedada com um endpoint `/mcp` estável, verifique o streaming e a hospedagem dos recursos da interface e revise a lista de verificação para o lançamento antes de compartilhar ou enviar o plug-in.

## Prompts sugeridos

Prompts eficazes para esse fluxo de trabalho têm os mesmos elementos:

- Um resultado claro: diga o que o plug-in deve ajudar o usuário a fazer no ChatGPT.
- Uma stack definida: diga se você quer TypeScript ou Python no servidor e se o widget deve usar React ou manter uma implementação leve.
- Limites explícitos para as ferramentas: peça ao Codex que proponha ou crie um pequeno conjunto de ferramentas, cada uma com uma única função.
- Expectativas de autenticação: informe se a primeira versão pode ser anônima ou se precisa de contas vinculadas e ações de gravação.
- Uma estratégia de desenvolvimento local: mencione o túnel ou a opção de hospedagem que você pretende usar nos testes HTTPS no ChatGPT.
- Etapas de verificação: diga ao Codex quais comandos executar, quais prompts testar e quais evidências apresentar.

Evite usar um único prompt enorme que peça planejamento, implementação, autenticação, implantação, envio e refinamento de uma só vez. Em vez disso, divida o trabalho em etapas menores.

**Planeje o plug-in antes de criar sua estrutura inicial**

**Crie a estrutura inicial da primeira versão funcional**

**Adicione autenticação somente depois que o fluxo principal funcionar**

**Prepare o plug-in para implantação e revisão**

## Preparação para o lançamento

- O plug-in oferece um único resultado bem delimitado que os usuários conseguem entender.
- O conjunto de ferramentas permanece pequeno, com metadados, entradas e saídas definidos explicitamente.
- O servidor MCP funciona de ponta a ponta e retorna um `structuredContent` conciso, reservando os dados exclusivos do widget para `_meta`.
- O widget, se necessário, é renderizado corretamente no ChatGPT.
- Um ciclo local de testes via HTTPS funciona no modo de desenvolvedor do ChatGPT.
- Um pequeno conjunto de prompts diretos, indiretos e negativos passa nos testes e produz o fluxo de conversa e os payloads das ferramentas esperados.
- A autenticação é adicionada somente quando necessária para dados específicos do usuário ou ações de gravação.
- Um plano de implantação e uma revisão da preparação para o lançamento abrangem metadados, indicações de uso das ferramentas, privacidade e prompts de teste antes que o plug-in seja compartilhado ou enviado.

## Armadilhas comuns

- Pedir ao Codex que adapte todo o produto ao ChatGPT. Melhor abordagem: peça que ele se concentre em um único resultado principal para o usuário, com três a cinco ferramentas e um único widget de escopo delimitado.
- Começar com um prompt gigantesco de implementação. Melhor abordagem: divida o trabalho em etapas de planejamento, criação da estrutura, autenticação, implantação e revisão.
- Criar a interface antes que o contrato das ferramentas esteja claro. Melhor abordagem: planeje primeiro o conjunto de ferramentas e o schema de resposta; depois, crie o widget.
- Deixar de usar a documentação oficial como fundamentação. Melhor abordagem: combine `$chatgpt-apps` com `$openai-docs` para que a estrutura gerada siga as orientações atuais para plug-ins.
- Deixar os metadados para depois. Melhor abordagem: escreva logo no início as descrições das ferramentas e a documentação dos parâmetros; depois, teste-as executando novamente um conjunto de prompts.
- Adicionar autenticação antes de validar o fluxo anônimo ou de somente leitura. Melhor abordagem: primeiro, faça o fluxo principal das ferramentas funcionar; depois, adicione OAuth às ferramentas que realmente precisam dele.
- Declarar que o plug-in está concluído antes de testá-lo no ChatGPT. Melhor abordagem: conecte
o servidor MCP no modo de desenvolvedor, inspecione os payloads das ferramentas e verifique o fluxo real
da conversa.

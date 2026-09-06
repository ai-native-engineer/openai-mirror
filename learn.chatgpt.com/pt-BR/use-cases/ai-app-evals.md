<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/ai-app-evals -->

## Introdução

Ao criar um aplicativo de IA ou modificar um existente, você precisa garantir que ele se comporte como esperado. As avaliações permitem testar sistematicamente um conjunto de cenários e detectar regressões antes que cheguem à produção.

Você pode usar o Promptfoo para executar avaliações no seu aplicativo de IA e o Codex para ajudar a criar e manter essas avaliações.

## Como usar

Use o Codex com a habilidade `$promptfoo-evals` do plug-in Promptfoo para transformar um comportamento do aplicativo de IA em uma suíte de avaliações reproduzível. Quando o aplicativo ainda não tiver um destino funcional do Promptfoo, `$promptfoo-provider-setup` ajudará a conectar a suíte ao caminho do aplicativo que você quer testar.

O Codex pode inspecionar o aplicativo, propor casos de alto valor informativo, adicionar a configuração do Promptfoo e os dados de teste, executar a suíte localmente e fornecer um comando para você continuar usando.

Este caso de uso funciona melhor quando o comportamento é concreto: qualidade das respostas de suporte, fundamentação em informações recuperadas, rótulos do classificador, chamadas de ferramentas, estrutura JSON, regras de negócio ou confiança na migração de prompts e modelos.

Uma primeira entrega sólida deve incluir código e dados de teste que possam ser revisados: um arquivo `promptfooconfig.yaml` ou uma configuração equivalente, um pequeno diretório `evals/`, casos de teste, qualquer adaptador de destino necessário para chamar o aplicativo e um comando local como `npm run evals`.

## Escolha o que avaliar

Comece com uma promessa perceptível para o usuário. Evite pedir ao Codex que avalie todo o sistema de IA de uma só vez. É mais fácil confiar em uma suíte menor, revisá-la e continuar executando-a.

Bons alvos iniciais incluem:

- **Correção:** classificação, extração, sumarização, roteamento ou transformação.
- **Fundamentação:** respostas que devem permanecer vinculadas aos documentos recuperados ou às fontes citadas.
- **Uso de ferramentas:** escolher a ferramenta certa, passar argumentos válidos e tratar erros das ferramentas.
- **Formato ou regras de negócio:** esquemas JSON, nomes de campos, limites definidos por regras de negócio ou contratos para textos exibidos na interface.
- **Migração de prompt ou de modelo:** garantir que um novo prompt, modelo, mensagem do sistema ou configuração de recuperação não faça casos importantes falharem.

Comece com requisitos de produto, relatórios de bugs, escalonamentos de suporte ou exemplos sanitizados que sua equipe se sinta à vontade para versionar no repositório.

## Peça um plano de avaliação

O Codex deve inspecionar antes de editar. Peça um plano que indique o caminho de destino, os fixtures, as asserções, o adaptador e os comandos. Assim, você terá a oportunidade de identificar um destino incorreto ou casos de teste fracos antes que os arquivos sejam adicionados.

Revise o plano antes da implementação. Ele deve indicar o caminho do aplicativo ou o endpoint que o Promptfoo chamará, os casos iniciais, as asserções, os arquivos que o Codex criará, o comando local e todos os segredos ou serviços necessários. Se o plano testar o modelo diretamente, em vez do caminho do aplicativo acessado pelos usuários, pergunte ao Codex se isso é intencional.

## Implemente, execute e itere

Quando o plano estiver correto, peça ao Codex para implementá-lo. A primeira implementação deve ser simples e previsível: configuração, casos, fixtures, um adaptador de destino se necessário, um comando e uma comprovação de que o comando foi executado.

Uma pequena suíte que testa o aplicativo pode ter esta aparência:

```text
evals/
  promptfooconfig.yaml
  tests/
    cases.yaml
  providers/
    provider.js  # only if the built-in provider cannot call the app directly

Execute a suíte antes de alterar o comportamento. A execução de referência indica se o aplicativo já falha nesses casos, se as asserções precisam de ajustes ou se o adaptador de destino está incorreto. Ajuste as asserções quando forem frágeis ou vagas demais, mas mantenha visíveis as falhas reais do produto.

Após a primeira execução, use a suíte para comparar as alterações no aplicativo antes que cheguem à produção. Adicione novos casos sempre que um bug, requisito de lançamento ou revisão de produto revelar um comportamento que você deseja manter estável. Quando o comando local estiver estável, peça ao Codex para adicioná-lo à CI ou à sua lista de verificação de lançamento.

<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/analyze-data-export -->

## Antes de começar

Anexe um arquivo CSV ou uma planilha, ou conecte o Google Drive e cole no chat a URL exata do Google Drive ou do Google Sheets. O Sites pode transformar essas fontes em um painel privado e interativo sem publicá-lo nem tornar seus dados públicos.

Você pode criar o painel no ChatGPT Work pelo navegador ou pelo aplicativo para desktop. Para que uma verificação agendada continue quando o notebook estiver desligado, inicie a tarefa no navegador. Uma tarefa executada no aplicativo para desktop exige que o computador esteja ligado e que o aplicativo esteja em execução.

## O que esperar

O ChatGPT verifica os dados de origem, cria um painel e mostra os números que embasam os gráficos. Este exemplo usa exportações trimestrais fictícias de vendas, um mapa de segmentos de clientes e uma prévia ilustrativa do painel. O exemplo diferencia a maior variação em dólares da maior variação percentual e sinaliza um pedido que não pode ser associado a um segmento de clientes.

<div data-use-case-export-only>

### Exemplo de painel

| Segmento de clientes | Receita do 1º trimestre | Receita do 2º trimestre |         Variação |
| ---------------- | ---------: | ---------: | -------------: |
| Empresas       |     $3,000 |     $2,450 | -$550 (-18.3%) |
| Médio porte       |     $1,000 |     $1,170 |   +$170 (+17%) |
| PMEs              |       $400 |       $520 |   +$120 (+30%) |

O segmento Empresas apresentou a maior variação em dólares, e o de PMEs apresentou a maior variação percentual. Um pedido do segundo trimestre no valor de $160 não correspondia ao mapa de segmentos de clientes e foi excluído dos totais por segmento. O painel privado inclui um gráfico de comparação, filtros por segmento e data, a data da última atualização da fonte e os cálculos em que os resultados se baseiam.

Quando você pede ao ChatGPT para verificar a fonte todas as manhãs de segunda a sexta-feira, ele atualiza o painel quando os dados da fonte aprovada mudam e sinaliza alterações relevantes ou registros ausentes. Ele não publica nem compartilha o painel sem aprovação.

</div>

## Como funciona

- **Conecte a fonte:** anexe uma exportação de vendas ou planilha, ou cole o link exato de uma Google Sheet aprovada ou de um arquivo aprovado do Google Drive. Antes de tirar conclusões, o ChatGPT verifica as colunas, as datas e os registros de clientes.
- **Crie o painel:** o Sites transforma os resultados em um painel privado e interativo com gráficos, filtros, a data da última atualização da fonte e os cálculos que fundamentam os resultados.
- **Mantenha-o atualizado:** uma tarefa agendada do ChatGPT Work verifica a fonte aprovada todos os dias úteis e atualiza o painel quando os dados mudam. O próprio site não executa o agendamento.
- **Destaque apenas o que importa:** peça ao ChatGPT para sinalizar alterações incomuns, registros ausentes ou decisões que precisam de revisão. Se nada importante mudar, ele não deve enviar notificações.
- **Revise antes de compartilhar:** analise primeiro o painel. Peça ao ChatGPT para compartilhá-lo com pessoas específicas somente depois que você aprovar a mudança no acesso.

## Compartilhe o painel

Depois de revisar o painel, peça ao ChatGPT para compartilhá-lo com pessoas específicas ou disponibilizá-lo no seu workspace. Você também pode gerenciar o acesso diretamente no [Sites](https://chatgpt.com/sites). Peça ao ChatGPT para mostrar as configurações atuais de compartilhamento e aguardar sua aprovação antes de convidar qualquer pessoa, publicar o painel ou alterar sua visibilidade.

Consulte a [documentação do Sites](/pt-BR/codex/sites) para ver as opções de compartilhamento e acesso ao workspace.

## Vá além

**Altere o que o painel acompanha**

**Configure um alerta mais útil**

**Prepare uma atualização semanal**

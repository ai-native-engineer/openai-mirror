<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/dependency-incident-audits -->

## Comece com um plano de auditoria seguro

Quando um incidente envolvendo uma dependência ou a cadeia de suprimentos evolui rapidamente, o primeiro resultado útil não é um patch feito às pressas. É um plano de auditoria claro: o que mudou, quais pacotes ou fluxos de trabalho podem ter sido afetados e quais evidências comprovariam que seu repositório está exposto.

Use o Codex para transformar o alerta em uma lista de verificação conservadora e somente leitura antes de instalar, fazer o build, testar ou executar qualquer coisa.

## Mantenha a primeira análise somente leitura

1. Forneça ao Codex o alerta público, o relatório do incidente ou a lista de pacotes afetados.
2. Peça a ele que diferencie as fontes oficiais dos comentários mais abrangentes.
3. Peça ao Codex que defina as evidências que comprovariam ou descartariam a exposição.
4. Deixe o Codex inspecionar manifestos, arquivos de lock, fluxos de trabalho de CI, scripts e arquivos relevantes do repositório.
5. Peça que os achados sejam agrupados por status das evidências, gravidade e próximo passo recomendado.

Em incidentes envolvendo pacotes, evite executar comandos de instalação, build, teste, importação ou ciclo de vida até saber o que o alerta afeta. O Codex pode pesquisar nos arquivos de lock e nos fluxos de trabalho sem executar código não confiável.

## Informe o status das evidências separadamente da gravidade

Um resultado de auditoria útil deve mostrar tanto a possível gravidade de um achado quanto a solidez das evidências:

  <p>
    <strong>Exposição confirmada:</strong> o arquivo de lock contém uma versão afetada
    do pacote em um caminho de dependência de produção.
  </p>
  <p>
    <strong>Verificação necessária:</strong> um job de CI tem permissões de publicação, mas
    o fluxo de trabalho não parece instalar diretamente o pacote afetado.
  </p>
  <p>
    <strong>Exposição descartada:</strong> o nome do pacote aparece apenas na documentação e não está
    presente nos manifestos nem nos arquivos de lock.
  </p>
  <p>
    <strong>Próximo passo:</strong> revise a atualização proposta da dependência e o plano de
    rotação de tokens antes de qualquer ação destrutiva.
  </p>

Após concluir a análise somente leitura, você pode pedir ao Codex que prepare um PR de correção, atualize as permissões de CI ou escreva uma nota de acompanhamento sobre o incidente. Mantenha essas ações separadas da auditoria inicial.

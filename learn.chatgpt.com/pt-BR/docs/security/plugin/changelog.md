<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/plugin/changelog -->

Consulte este registro de alterações para saber o que mudou no Plugin Codex Security.

**Versão mais recente do plug-in:** `0.1.20`.

Confira a versão do plug-in no seu ambiente atual do Codex antes de usar um recurso de uma versão mais recente.

As entradas do registro de alterações seguem a versão do plug-in, não a do pacote. Usuários da CLI e do
SDK podem executar `npx @openai/codex-security info --json` para conferir juntas as
versões do pacote e do plug-in incluído.

## 0.1.20 (17 de agosto de 2026)

### Execute verificações profundas como auditorias independentes completas

- Faça cada agente de execução das verificações profundas realizar a mesma auditoria de ponta a ponta usada nas verificações padrão, incluindo modelagem de ameaças, validação, análise de caminhos de ataque e geração de relatórios de cobertura.
- Combine os relatórios concluídos dos agentes de execução em uma única verificação, preservando os limites de tempo configurados, a cobertura parcial, a recuperação após reinicializações e o cancelamento.
- Use quatro agentes de execução simultâneos por padrão, interrompa após quatro verificações consecutivas concluídas
  sem novos achados e limite cada verificação profunda a 40 execuções desses agentes. As configurações
`workers = "auto"` existentes agora correspondem a quatro agentes de execução. Consulte
[Configure o ambiente de execução das verificações profundas](/pt-BR/codex/security/plugin/deep-scans#configure-deep-scan-runtime).
- Retome os agentes de execução que concluíram a revisão do código-fonte, mas perderam o rascunho final, em vez de repetir a auditoria completa.

### Verifique o Trusted Access for Cyber antes das verificações hospedadas

- Nos hosts do Codex que disponibilizam o aplicativo Codex Security Access, verifique o status do Trusted Access antes do início das verificações padrão, de alterações e profundas.
- Veja um aviso em destaque quando a saída protegida da verificação puder estar indisponível, com um link de inscrição quando o acesso não for concedido.
- Continue a verificação quando a checagem não conseguir confirmar o status do Trusted Access ou o acesso não for concedido; o aviso não determina se a verificação será executada.
- Os pacotes públicos da CLI e do SDK não exibem esse aviso na versão `0.1.20`.

### Execute verificações profundas em mais ambientes

- Inicie agentes de execução de verificações profundas a partir de instalações dos pacotes da CLI e do SDK, incluindo
  instalações no Windows sem um executável global `codex`.
- Mantenha as configurações de verificações profundas das instalações independentes da CLI e do SDK isoladas das demais verificações em execução.
- Mantenha as configurações de aprovação não interativa nos agentes de execução aninhados de verificações profundas.

### Preserve os resultados das verificações em mais casos de falha

- Preserve mais verificações salvas e resultados concluídos dos agentes de execução nos fluxos de recuperação por reinicialização, arquivamento e transferência de responsabilidade.
- Recupere achados válidos a partir de dados de verificação antigos ou incompletos.
- Conclua verificações quando relatórios de cobertura independentes se sobrepuserem.
- Informe corretamente a entrada em cache nos totais de uso de tokens nas respostas atuais e anteriores dos provedores.

## 0.1.19 (13 de agosto de 2026)

### Defina um limite de tempo para verificações profundas

- Defina `[deep_scan].max_time_hours` como uma duração positiva de até 96 horas.
  Você pode usar frações de hora.
- Preserve os resultados de descoberta já concluídos quando o prazo expirar e prossiga com a validação e a geração de relatórios.
- Marque o relatório como parcial se nenhuma revisão do código-fonte for concluída antes do prazo.

### Melhore a confiabilidade das verificações

- Preserve o trabalho de descoberta concluído quando um agente de execução parar ou um redutor fizer uma nova tentativa.
- Leia arquivos de código-fonte maiores e gere relatórios sem os antigos limites fixos de tamanho.
- Leia as alterações registradas em commits da revisão selecionada e preserve os caminhos relativos ao repositório no Windows.
- Repasse as credenciais do OpenRouter e do Fireworks aos agentes de execução de verificações profundas.

## 0.1.18 (7 de agosto de 2026)

### Use o Amazon Bedrock para verificações de segurança

- Execute verificações com tokens de portador do Amazon Bedrock e perfis da AWS, configurações regionais, identidade da Web ou credenciais de contêiner.
- Mantenha a autenticação da AWS disponível para os agentes de execução delegados para verificações profundas.

### Execute verificações padrão com menos coordenação

- Use um fluxo de trabalho mais simples para verificações padrão de repositórios e de caminhos com escopo delimitado.
- Preserve as orientações dos arquivos `SECURITY.md` em subdiretórios, o escopo exato da verificação, as atualizações de progresso
  e os relatórios finais da verificação.

### Inicie e conclua verificações com mais confiabilidade

- Dê às verificações iniciadas por prompt até cinco minutos para inicializar repositórios grandes, em vez de interrompê-las por tempo limite após 30 segundos.
- Conclua verificações padrão e profundas quando um host impuser limites ao comprimento dos nomes das ferramentas.

### Mantenha a remediação disponível após alterações no sistema de arquivos

- Remedie achados de verificações concluídas depois que uma remontagem do sistema de arquivos alterar seu identificador de dispositivo.
- Continue exigindo a cópia de trabalho e a revisão do Git originais antes de aplicar uma correção.

## 0.1.17 (5 de agosto de 2026)

### Acompanhe o progresso da verificação em tempo real

- Acompanhe a fase atual da verificação, o tempo decorrido, os agentes de execução ativos, os arquivos revisados e o uso de tokens em uma única visualização de progresso em tempo real.
- Veja o progresso da revisão do repositório ser atualizado à medida que a revisão de cada arquivo é concluída, em vez de esperar a verificação terminar.

### Retome verificações profundas interrompidas

- Continue uma verificação profunda em andamento depois que seu coordenador reiniciar, sem repetir revisões de arquivos já concluídas.
- Preserve os resultados de descoberta concluídos, a responsabilidade pela verificação e o trabalho pendente durante atualizações do aplicativo ou interrupções das sessões de verificação.

### Inicie e conclua verificações com menos sobrecarga

- Inicie verificações padrão, de alterações e profundas diretamente nos fluxos de trabalho nativos, sem abrir o componente incorporado de verificação que foi descontinuado.
- Reutilize resumos de verificações concluídas sem recarregar todos os achados, a menos que você solicite os resultados estruturados completos.

## 0.1.16 (4 de agosto de 2026)

### Acompanhe as medições de uso das verificações

- Analise o uso total de tokens e o uso de tokens de entrada, de entrada em cache e de saída na verificação principal e em seus agentes de execução delegados.
- Diferencie medições completas, parciais e indisponíveis, em vez de exibir dados de uso ausentes como zero.

### Execute verificações mais profundas com resultados consistentes

- Use as mesmas fases de modelagem de ameaças, descoberta, validação, análise de caminhos de ataque e geração de relatórios nas verificações padrão e aprofundadas.
- Configure os agentes das verificações aprofundadas, a delegação por agente, a saturação e os limites de descoberta pela CLI ou pelo SDK.
- Execute verificações aprofundadas com o ambiente de execução de agentes compatível com o modelo e recupere estados anteriores das verificações sem perder o histórico existente.
- Gere o relatório principal para verificações de alterações e verificações aprofundadas sem exigir relatórios separados de vulnerabilidades ou recomendações de reforço de segurança.

### Mantenha as orientações das verificações e os repositórios de destino corretos

- Atualize as orientações de segurança durante uma verificação ativa e repasse-as às fases posteriores e aos agentes com tarefas delegadas nas verificações aprofundadas.
- Preserve as URLs dos repositórios, as referências a pull requests e contextos de segurança mais extensos, sem permitir acesso à rede que você não solicitou.
- Encerre as verificações com falha quando o repositório ou o alvo da verificação mudar durante a execução, para que a automação não aceite achados desatualizados.
- Respeite as configurações de proxy corporativo e de certificados confiáveis em ambientes de rede gerenciados.

### Escreva relatórios de vulnerabilidades mais claros

- Produza relatórios de vulnerabilidades embasados no código-fonte que separem o comportamento observado das hipóteses não verificadas.
- Descreva de forma realista as limitações da prova de conceito e inclua as versões afetadas, os limites de segurança e orientações práticas de correção.

## 0.1.15 (30 de julho de 2026)

### Preserve os resultados das verificações quando o repositório mudar

- Mantenha os achados e relatórios concluídos vinculados à revisão original ou ao instantâneo original da árvore de trabalho, mesmo que os arquivos ou a revisão do repositório mudem durante a verificação.
- Mostre um aviso ao concluir a verificação quando o código selecionado mudar ou o alvo ficar indisponível, em vez de descartar os resultados.
- Arquive uma verificação existente antes de reutilizar seu diretório de saída em outra verificação.

### Aplique o feedback revisado sobre achados

- Registre um motivo ao encerrar um achado como falso positivo.
- Aplique as decisões revisadas sobre falsos positivos às verificações posteriores do mesmo alvo, sem estendê-las a outra cópia de trabalho ou a um alvo não relacionado.
- Suprima um achado recorrente somente quando o motivo anterior ainda se aplicar ao código e aos controles de segurança atuais.

### Recupere achados válidos sem superestimar a cobertura

- Mantenha os achados válidos quando outro achado, relatório ou artefato de reforço de segurança estiver malformado e mostre um aviso sobre os dados ignorados.
- Remova achados duplicados e mantenha o achado mais sólido com base na gravidade, na confiança e nas evidências que o sustentam.
- Marque a cobertura como parcial quando o Codex não puder verificar achados, comprovantes de revisão ou áreas que precisam de análise adicional.
- Inclua avisos de cobertura incompleta e de revisão adiada nas exportações SARIF.

### Mantenha as configurações e o progresso das verificações visíveis

- Salve o modelo e o esforço de raciocínio selecionados junto às verificações padrão e aprofundadas para que o histórico e o progresso permaneçam consistentes após recarregamentos.
- Mostre o número de revisões independentes ativas e concluídas nas verificações aprofundadas e indique quando a consolidação dos resultados começa.
- Adapte a descoberta das verificações padrão à capacidade disponível dos agentes, mantendo uma única lista de arquivos no escopo e uma única rodada de revisão de candidatos.

### Ofereça suporte a mais estruturas de repositórios e sistemas de arquivos

- Inclua repositórios Git aninhados ao capturar um instantâneo da árvore de trabalho.
- Preserve os caminhos literais dos arquivos no escopo e trate os caminhos do Windows que não diferenciam maiúsculas de minúsculas.
- Durante as checagens preliminares da verificação, expanda o valor configurado de `CODEX_HOME` se ele começar com `~`.

## 0.1.14 (28 de julho de 2026)

### Revise o histórico de verificações e os achados recorrentes

- Filtre repositórios, achados e o histórico de verificações com um número limitado de resultados por página e detalhes de status mais claros.
- Execute novamente uma verificação com as configurações salvas e compare verificações concluídas para distinguir achados novos, persistentes, resolvidos e não verificados novamente.
- Agrupe as árvores de trabalho do mesmo repositório e use identidades estáveis para repositórios e achados em todas as visualizações.

### Defina a política de segurança do repositório

- Use `$codex-security:define-security-policy` para revisar ou atualizar as orientações com escopo delimitado em
`SECURITY.md` sobre limites de confiança, invariantes de segurança, achados que devem ser
  relatados, gravidade, exclusões e risco aceito.
- Aplique o arquivo de política mais próximo, limitando seu tamanho e rejeitando links simbólicos que apontem para fora do repositório.

### Revise os achados antes de acompanhá-los

- Selecione até 25 achados de uma verificação concluída para acompanhamento no Linear ou em issues do GitHub.
- Envie os achados selecionados de volta ao Codex para revisão e aprovação, em vez de criar issues diretamente no workspace de achados.

### Execute verificações padrão com um fluxo de trabalho mais simples

- Use uma única lista determinística de arquivos no escopo e um registro compacto de candidatos para verificações padrão de repositórios e de caminhos com escopo delimitado.
- Preserve as saídas existentes de manifesto, achados, cobertura, relatório e SARIF, reduzindo as etapas repetidas da verificação.

## 0.1.13 (25 de julho de 2026)

### Revise achados em mais ambientes

- Mantenha os achados reais de segurança quando o código afetado for local, interno, usado para treinamento ou não estiver implantado em produção.
- Use o contexto de implantação e exposição para calibrar a gravidade e a confiança, em vez de suprimir o achado automaticamente.

## 0.1.12 (23 de julho de 2026)

### Execute verificações mais aprofundadas com informações de progresso mais claras

- Execute verificações aprofundadas que coordenam agentes em um repositório inteiro ou em um diretório selecionado.
- Aplique suas configurações de modelo e raciocínio às tarefas delegadas da verificação.
- Consulte os resultados das checagens preliminares, o progresso da verificação, a capacidade disponível dos agentes e o comportamento de contingência antes e durante uma verificação.

### Revise e execute novamente as verificações anteriores

- Abra as verificações atuais e anteriores na lista de verificações de segurança.
- Reabra uma verificação salva no workspace de achados ou execute-a novamente para atualizar os resultados.
- Veja estados de conclusão mais claros e maior consistência nos detalhes dos achados e no histórico de verificações.

### Configure as verificações com menos interrupções

- Inicie verificações pelo fluxo nativo de configuração sem sair da tarefa atual.
- Mantenha a configuração da verificação no painel lateral, mesmo quando o Codex estiver no modo de tela cheia.
- Feche a configuração quando não precisar dela e mantenha essa preferência para
varreduras futuras.

### Revise e remedie achados validados

- Mantenha os achados validados de baixa gravidade nos resultados finais.
- Revise detalhes mais consistentes dos achados nas varreduras, nos relatórios e nas exportações.
- Tente a remediação novamente e incorpore o contexto relevante da varredura às correções posteriores.

### Exporte resultados para os fluxos de trabalho de segurança existentes

- Exporte achados finalizados em JSON, CSV ou SARIF.
- Gere resultados SARIF localmente para integração com ferramentas de varredura de código
e de segurança.
- Mantenha os detalhes dos achados consistentes entre os formatos exportados.

## 0.1.11 (10 de julho de 2026)

### Produza relatórios detalhados de achados e de fortalecimento da segurança

- Gere um relatório de vulnerabilidade fundamentado no código-fonte para cada achado
reportável da varredura, acompanhado de arquivos de prova de conceito quando disponíveis.
- Revise um portfólio de fortalecimento estrutural da segurança que analisa o conjunto completo de achados,
as vantagens e desvantagens das decisões de engenharia, as opções de migração e os diagramas de apoio.
- Use `report.md` como ponto de entrada para esses resultados derivados em `findings/`
  e `hardening/`. Mantenha todo o conteúdo do diretório da varredura reunido ao compartilhar ou
  arquivar os resultados.

### Execute diretamente fluxos de trabalho de geração de relatórios

- Use `$codex-security:vulnerability-writeup` para transformar documentos de divulgação,
  achados preliminares, PoCs e código-fonte em relatórios bem elaborados sem precisar
  executar antes uma varredura do Codex Security.
- Use `$codex-security:propose-security-hardening` para desenvolver opções estruturais ou arquiteturais
  fundamentadas em evidências a partir de varreduras, achados, documentos de incidentes ou
  de avaliações e código-fonte.

### Aplique as orientações do repositório e a cobertura de forma consistente

- Defina o contexto do modelo de ameaças, os invariantes de segurança, os critérios para
  achados reportáveis, as exclusões e o contexto de gravidade em arquivos `SECURITY.md`
  na raiz ou em diretórios aninhados. O arquivo aplicável mais próximo tem precedência.
- Aprimore a cobertura da revisão do repositório antes da validação, preservando
as superfícies cuja análise foi explicitamente adiada e as lacunas de comprovação.
- Revise os arquivos-fonte excluídos nas varreduras de alterações e amplie a cobertura padrão
da revisão do repositório antes da validação.
- Verifique as habilidades das fases da varredura profunda, os executores delegados e a capacidade dos executores
antes de iniciar uma varredura profunda.

## 0.1.10 (23 de junho de 2026)

### Aprimore o recebimento de tickets do Jira e do Linear

- Solicite confirmação antes de importar sub-issues do Linear e preserve as relações
entre itens pai e filho nos resultados.
- Diferencie conexões ausentes, permissões insuficientes, tickets inacessíveis
e falhas temporárias do conector.
- Interrompa a execução em vez de emitir um veredito quando o conteúdo solicitado do ticket
não estiver disponível.
- Atribua posições únicas usando números inteiros positivos a partir de `1` em cada fila de itens confirmados
  ou que precisam de revisão.

### Revise alterações no código com mais confiabilidade

- Compare um commit inspecionado com seu commit pai real e preserve o alvo do diff
no workspace de achados.
- Informe que o estado do patch está indisponível em vez de revisar uma alteração diferente.
- Revise resultados de triagem e contextos de achados mais consistentes.

## 0.1.9 (18 de junho de 2026)

### Revise varreduras no workspace de achados

- Revise varreduras concluídas em um workspace dedicado que reúne achados,
cobertura, gravidade, confiança e artefatos da varredura.
- Filtre e ordene os achados, inclusive pelo maior grau de confiança,
preservando o estado do workspace durante as atualizações.
- Abra um achado para revisar as evidências do código-fonte, os detalhes de validação, a alcançabilidade,
o impacto e as orientações de remediação em um só lugar.

### Execute varreduras com menos configuração

- Execute varreduras padrão em repositórios Git, pastas individuais ou
bases de código sem histórico do Git. As varreduras profundas também podem ter como alvo uma pasta específica.
- Cancele explicitamente uma varredura ativa, retome uma varredura interrompida sem uma nova
solicitação de configuração e receba um aviso antes de iniciar varreduras profundas simultâneas.
- Acompanhe estados de configuração e progresso mais claros, com resumos de progresso
mais compactos e erros que permanecem visíveis até você resolvê-los.

### Exporte resultados portáteis e verificáveis

- Use um formato consistente para varreduras concluídas, com um manifesto, achados estruturados,
dados de cobertura e um relatório em Markdown derivado do mesmo resultado canônico.
- Exporte os achados em JSON, CSV ou SARIF para análise, arquivamento e integração
com outras ferramentas de segurança.
- Conclua as varreduras com mais confiabilidade, inclusive quando caminhos do Windows ou o mecanismo de bloqueio das varreduras
afetarem o acesso ao sistema de arquivos.

### Faça a triagem e acompanhe os achados existentes

- Faça a triagem dos achados existentes provenientes de ferramentas de varredura, avisos de segurança, relatórios de bug bounty,
do GitHub, do Jira, do Linear ou de resultados do Codex Security, em relação à base de código atual.
O fluxo de trabalho de triagem retorna um veredito fundamentado em evidências e uma fila de ações
ordenada por prioridade.
- Acompanhe os achados validados selecionados em issues do Linear, do Jira ou do GitHub, ou crie
um rascunho privado de GitHub Security Advisory quando o repositório atender aos
requisitos para esse tipo de aviso.
- Revise as verificações de duplicidade, o contexto de origem, a visibilidade no destino e o
conteúdo exato proposto antes de aprovar uma operação de gravação. O Codex relê o resultado
após a criação ou atualização para verificá-lo.

## 0.1.7 (4 de junho de 2026)

### Realize revisões de segurança fundamentadas em evidências

- Faça uma varredura em um repositório autorizado ou em uma pasta selecionada em busca de
vulnerabilidades de segurança.
- Execute várias rodadas de descoberta em todo o repositório quando precisar de uma
cobertura mais completa.
- Revise pull requests, commits, diferenças entre branches e patches locais para identificar
regressões de segurança.
- Passe cada candidato pelas etapas de modelagem de ameaças, descoberta de achados, validação
e análise de impacto antes de gerar os relatórios da varredura.
- Corrija um achado aceito com um patch direcionado, cobertura de testes de regressão e
verificação da issue original.

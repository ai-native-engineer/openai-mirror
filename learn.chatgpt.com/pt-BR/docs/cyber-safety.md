<!-- source: https://learn.chatgpt.com/pt-BR/docs/cyber-safety -->

O OpenAI Daybreak ajuda usuários aprovados a realizar atividades autorizadas de defesa em segurança cibernética. O Daybreak Blue oferece acesso a modelos principais com menos recusas em fluxos de trabalho defensivos autorizados. O Daybreak Red oferece, mediante aprovação separada, acesso a modelos especializados em segurança cibernética para pesquisas de segurança mais avançadas.

Combine seu modelo aprovado com um ambiente controlado, limites claros para os sistemas e as ações aprovados, permissões de privilégio mínimo e revisão automática antes que ações sensíveis sejam executadas. Use o modelo somente pela interface aprovada do produto e com a identidade aprovada, seja no workspace aprovado, seja na organização e no projeto aprovados da API.

## Escolha o modelo adequado

Para a maioria das atividades defensivas autorizadas, comece com **GPT-Daybreak-Blue** . Esse modelo oferece acesso a capacidades avançadas, com menos recusas em fluxos de trabalho de segurança defensiva, incluindo:

- Descoberta e triagem de vulnerabilidades.
- Revisão de segurança do código e modelagem de ameaças.
- Engenharia de detecção e resposta a incidentes.
- Análise de malware em um ambiente controlado.
- Remediação e validação de patches.

O **GPT-Daybreak-Red** é um modelo especializado em segurança cibernética para fluxos de trabalho explicitamente autorizados e aprovados separadamente, como reprodução controlada de vulnerabilidades, validação de provas de conceito ou exploits, testes de penetração, red teaming e análise de sistemas complexos. Ele não é a opção padrão para atividades rotineiras de segurança, e o acesso não fica disponível automaticamente nem em todas as interfaces.

Na ausência de uma autorização clara, esses fluxos de trabalho avançados podem parecer atividades maliciosas. Use o modelo e a interface aprovados somente em sistemas que pertençam a você ou para cuja avaliação você tenha autorização explícita, e mantenha a supervisão humana adequada.

Por exemplo:

- **GPT-Daybreak-Blue:** Analise o repositório aprovado do laboratório em busca de fragilidades na autenticação, classifique os achados de acordo com as evidências e o impacto e proponha patches sem acessar sistemas externos.
- **GPT-Daybreak-Red:** No laboratório aprovado e durante a janela de testes aprovada, reproduza a falha de autenticação documentada, valide uma prova de conceito mínima e interrompa a atividade antes de acessar credenciais, estabelecer persistência ou fazer alterações em produção.

## Trusted Access for Cyber

Solicite **acesso ao Daybreak** por meio do [Trusted Access for Cyber](https://help.openai.com/en/articles/20001258-trusted-access-for-cyber). O acesso depende de aprovação e provisionamento específicos para sua identidade ou seu serviço, seu workspace do ChatGPT ou sua organização e seu projeto da API, a oferta e o modelo autorizados e a interface permitida do produto.

- Pessoas físicas podem solicitar acesso pelo [formulário individual de inscrição no Trusted Access](https://chatgpt.com/cyber).
- As organizações podem enviar o [formulário de solicitação do Trusted Access para empresas](https://openai.com/form/enterprise-trusted-access-for-cyber/) e coordenar o processo com seu representante da OpenAI.

Enviar uma solicitação ou concluir a verificação de identidade não garante aprovação.

  Enviar uma solicitação, verificar sua identidade ou receber aprovação para o Daybreak Blue
não concede acesso ao Daybreak Red nem ao GPT-Daybreak-Red. A oferta especializada
exige aprovação e provisionamento separados.

No caso de acesso para empresas, use o workspace, a organização da API ou o projeto aprovados somente para o trabalho interno autorizado da sua organização. Não estenda esse acesso a usuários externos, clientes de terceiros, serviços oferecidos externamente, recursos de produtos derivados nem sistemas fora do escopo do trabalho aprovado. Se houver dúvida sobre a identidade, o workspace, a organização da API, o projeto, o modelo ou a interface aprovados, pare e confirme essas informações com seu representante da OpenAI.

O Trusted Access não concede automaticamente [zero retenção de dados](/api/docs/guides/your-data#data-retention-controls-for-abuse-monitoring). Antes de começar, confirme quais controles de retenção foram aprovados separadamente para a organização específica da API e o endpoint aplicável.

## Falsos positivos

Uma atividade legítima de segurança cibernética, ou mesmo uma atividade sem relação com ela, ainda pode acionar um mecanismo de proteção. Se um mecanismo de proteção bloquear, redirecionar ou limitar uma solicitação, examine o aviso disponível no cliente e os logs da solicitação. Consulte [Problemas comuns e solução de problemas](https://help.openai.com/en/articles/20001259) para saber quais detalhes coletar e conhecer as próximas etapas. Quando disponível, use `/feedback` para relatar possíveis falsos positivos do Codex. Em caso de restrições ao acesso à API ou de contestações, siga as [orientações sobre verificações de segurança cibernética da API](/api/docs/guides/safety-checks/cybersecurity#appeals).

Todos os usuários continuam sujeitos às [Políticas de Uso](https://openai.com/policies/usage-policies/) e aos [Termos de Uso](https://openai.com/policies/row-terms-of-use/).

## Configure seu fluxo de trabalho de segurança

O Trusted Access controla o acesso aprovado aos modelos, mas não configura seu ambiente, não aplica limites aos sistemas e às ações aprovados nem revisa as ações propostas.

- [Use a configuração recomendada](/pt-BR/codex/cyber-safety/recommended-configuration) para implementar isolamento, permissões de privilégio mínimo, limites claramente definidos e mecanismos de proteção para ações sensíveis.

<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/groups-and-provisioning -->

Os grupos organizam as pessoas em um workspace do ChatGPT e podem ter funções personalizadas. A associação a grupos não substitui a atribuição de licenças, não concede, por si só, permissões para recursos do workspace, não se sobrepõe à política do ambiente de execução local nem fornece acesso à API da plataforma ou a sistemas conectados.

Para conhecer o modelo completo de controle, consulte
[Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions).

## Compare as fontes de associação

Use grupos para pessoas com a mesma necessidade de acesso, como participantes de um piloto, operadores do workspace ou membros que precisem do mesmo recurso compatível.

### Crie um grupo para uma necessidade comum de acesso

Proprietários e administradores do workspace podem criar e gerenciar grupos. Crie um grupo gerenciado manualmente para um público pequeno ou temporário ou sincronize um grupo já existente no seu provedor de identidade quando a associação precisar seguir seu diretório.

Cada grupo tem uma única fonte oficial de associação:

| Tipo de grupo                | Fonte de associação                   | Quando se aplica                                                                  |
| ------------------------- | ----------------------------------- | -------------------------------------------------------------------------------- |
| Gerenciado manualmente          | Administração do workspace do ChatGPT    | O grupo é pequeno, temporário ou não é gerenciado por meio da sincronização de diretório             |
| Gerenciado pelo provedor de identidade | Seu provedor de identidade por meio do SCIM | A associação deve seguir o diretório da organização e o processo de remoção de membros |

Grupos gerenciados manualmente e grupos gerenciados pelo provedor de identidade podem coexistir. Nos grupos sincronizados, o provedor de identidade é a fonte de associação; atualizações posteriores de provisionamento podem sobrescrever alterações feitas no workspace. A Central de Ajuda é a fonte oficial de informações sobre o comportamento atual do SCIM, os atributos compatíveis e as etapas de configuração.

## Entenda os limites de acesso

A associação a um grupo, por si só, não concede permissão para usar um recurso do workspace.

### Vincule um grupo às permissões adequadas

Proprietários do workspace podem atribuir funções personalizadas a grupos ou, quando disponível, diretamente
aos membros. Verifique todas as funções aplicáveis: a opção **Desativado** definida explicitamente em qualquer função
nega essa permissão, mesmo quando outra função a concede. O tipo de licença do membro
e a elegibilidade para o produto continuam se aplicando.

O SCIM provisiona a associação ao workspace e as atribuições a grupos. Ele não concede permissões no GitHub, no Google Drive, no Slack nem em outro sistema conectado. Também não substitui os requisitos do ambiente de execução local nem o acesso à organização na API da plataforma.

O RBAC do workspace e os requisitos do ambiente de execução local são sistemas de controle separados. Um
grupo pode ser relevante para ambos, mas não deduza da ordem dos grupos do workspace nenhuma regra de correspondência
ou precedência para requisitos gerenciados. Consulte
[Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration) para conhecer as regras
documentadas de distribuição e precedência local.

## Use os procedimentos de configuração atuais

Os detalhes da administração do workspace podem mudar. Use estas fontes para consultar as etapas atuais na interface, a disponibilidade e os limites:

- [Gerenciar membros, tipos de licença, funções e acesso](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [Gerenciar grupos](https://help.openai.com/en/articles/9083985-group-permissions-in-gpts)
- [Perguntas frequentes sobre a integração com o SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
- [Gerenciar as configurações do workspace](https://help.openai.com/en/articles/8411955)

### Verifique entradas, movimentações e saídas de membros

- **Entradas:** Confirme que o membro aceita qualquer convite pendente para o workspace e
  recebe a licença, as associações a grupos, as permissões e os recursos compatíveis
  previstos.
- **Movimentações:** Atualize a fonte oficial de associação e verifique as
  permissões efetivas do membro em todas as funções aplicáveis.
- **Saídas:** Remova, por meio do provedor de identidade, o acesso do membro gerenciado pelo SCIM
  e confirme que ele não pode mais acessar o workspace. Se você remover o membro apenas
  do workspace, uma sincronização posterior poderá restabelecer
  o acesso.

## Documentação relacionada

- [Gerenciamento do ciclo de vida de usuários](/pt-BR/codex/enterprise/user-lifecycle)
- [Autenticação](/pt-BR/codex/auth)
- [Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions)
- [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration)
- [Guia de implementação para administradores](/pt-BR/codex/enterprise/admin-setup)

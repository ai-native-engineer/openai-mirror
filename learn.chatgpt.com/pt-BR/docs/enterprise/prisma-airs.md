<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/prisma-airs -->

Conecte o Prisma AIRS da Palo Alto Networks para aplicar suas políticas de segurança aos
prompts do Codex antes que cheguem ao modelo. Os administradores do workspace configuram a
integração uma única vez no workspace.

O Prisma AIRS pode aplicar as proteções configuradas no seu perfil de segurança, como
prevenção contra perda de dados, detecção de injeção de prompt e detecção de URLs
maliciosas.

## Antes de começar

Você precisa de:

- Um workspace do ChatGPT com acesso ao Prisma AIRS habilitado. Entre em contato com a equipe da OpenAI
responsável pela sua conta para solicitar acesso.
- Permissões de administrador do workspace.
- Uma chave de API do Prisma AIRS, um perfil de segurança configurado e o endpoint do serviço
para sua implantação.

## Conectar o Prisma AIRS

1. Abra [Controles de dados do Codex](https://chatgpt.com/codex/cloud/settings/data) como
   administrador do workspace.
2. Em **Proteções externas**, localize **Prisma AIRS**. Se esta seção não estiver
   disponível, peça à equipe da OpenAI responsável pela sua conta que habilite o acesso ao seu workspace.
3. Insira sua **Chave de API**, o nome ou ID do **Perfil de segurança** e a **URL do
   endpoint**.
4. Escolha as opções de **Modo de aplicação** e **Em caso de falha do AIRS**.
5. Selecione **Salvar conexão**. O Codex valida a conexão e criptografa sua
   chave de API.
6. Selecione **Testar conexão** para verificar a configuração salva.
7. Ative **Habilitar Prisma AIRS** para começar a verificar prompts em todo o
   workspace.

Salvar a conexão não ativa a verificação. Você também precisa ativar **Habilitar
Prisma AIRS**.

## Escolher um endpoint

Use o endpoint aprovado para sua implantação do Prisma AIRS:

| Região        | Endpoint                                                 |
| ------------- | -------------------------------------------------------- |
| Estados Unidos | `https://service.api.aisecurity.paloaltonetworks.com`    |
| Alemanha       | `https://service-de.api.aisecurity.paloaltonetworks.com` |
| Índia         | `https://service-in.api.aisecurity.paloaltonetworks.com` |
| Singapura     | `https://service-sg.api.aisecurity.paloaltonetworks.com` |

O Codex usa o endpoint dos Estados Unidos por padrão. Os requisitos de residência de dados
do workspace podem restringir qual endpoint você pode usar.

## Escolher como processar prompts

O **Modo de aplicação** determina o que acontece quando o Prisma AIRS sinaliza um prompt:

- **Bloquear**: Impede que o prompt chegue ao modelo. Essa é a opção padrão.
- **Somente alertar**: Registra a detecção e permite que o prompt continue.

**Em caso de falha do AIRS** determina o que acontece se o Prisma AIRS não estiver disponível ou
não responder:

- **Permitir prompts**: Permite que o prompt prossiga sem que a verificação seja concluída. Essa é a opção padrão.
- **Bloquear prompts**: Bloqueia o prompt até que o Prisma AIRS possa verificá-lo.

Escolha **Bloquear prompts** quando sua política de segurança exigir que cada prompt ao qual ela se aplica
receba uma decisão da verificação.

## Entender o que é verificado

O Codex envia o texto de cada prompt recém-enviado ao endpoint configurado do Prisma AIRS
para inspeção. Isso se aplica aos fluxos de trabalho do Codex abrangidos pela integração, incluindo o aplicativo, a CLI,
a extensão para IDE e a nuvem, quando os usuários se autenticam no workspace do ChatGPT
definido na configuração. A integração não abrange sessões autenticadas com uma chave de API da Plataforma. Consulte
[Exigir um método de login ou workspace](/pt-BR/codex/auth#enforce-a-login-method-or-workspace)
para exigir o uso do método de login e do workspace definidos.

O Prisma AIRS não verifica respostas do assistente, chamadas de ferramentas, resultados de ferramentas, arquivos
nem imagens por meio desta integração. O perfil de segurança configurado determina
quais ameaças e dados confidenciais o Prisma AIRS detecta.

O Codex criptografa sua chave de API e nunca a exibe depois que você a salva. Analise as políticas da Palo
Alto Networks sobre tratamento, retenção e residência de dados antes de habilitar a
inspeção de prompts. Essas políticas se aplicam aos prompts enviados ao Prisma AIRS.

## Gerenciar a conexão

Volte aos [Controles de dados do Codex](https://chatgpt.com/codex/cloud/settings/data)
para gerenciar a integração:

- Selecione **Testar conexão** para verificar a chave de API, o perfil de segurança
  e o endpoint salvos.
- Insira uma nova chave e selecione **Rotacionar chave de API** para substituir a chave salva
  sem alterar as demais configurações.
- Desative **Habilitar Prisma AIRS** para interromper a verificação e manter a configuração
  salva.
- Selecione **Desconectar** e depois confirme para interromper a verificação e excluir a conexão
  e a chave de API salvas.

Para configurar o workspace de forma mais abrangente e gerenciar políticas, consulte o
[Guia de implantação para administradores](/pt-BR/codex/enterprise/admin-setup) e a
[Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration).

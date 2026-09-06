<!-- source: https://learn.chatgpt.com/pt-BR/docs/permission-modes -->

{/* vale Microsoft.FirstPerson = NO */}

## Modos de permissão

As permissões controlam como o ChatGPT (no aplicativo para desktop) e o Codex (na CLI ou na IDE) lidam com ações locais, como editar arquivos, executar comandos e acessar a internet. O modo escolhido define o limite
entre o que o ChatGPT pode fazer por conta própria e o que precisa de revisão.

Para a maioria das tarefas, comece com **Pedir aprovação**. Com esse modo, o ChatGPT trabalha no
workspace atual e pausa antes de ultrapassar esse limite.

Selecione os diferentes modos abaixo para entender como cada um funciona.

## Ativar modos

Ao usar o aplicativo para desktop do ChatGPT pela primeira vez, você precisa ativar os modos nas configurações do aplicativo.

**Pedir aprovação** está sempre disponível. Para adicionar **Aprovar por mim** (chamado de
**Revisão automática** nas configurações) ou **Acesso completo** ao menu de permissões, abra
**Configurações \> Geral** no aplicativo para desktop do ChatGPT e ative o modo em
**Permissões**. Ativar um modo faz com que ele fique disponível no menu; isso não
seleciona o modo nem altera um chat existente.

  

  Os modos disponíveis podem depender da sua configuração local e dos requisitos da sua
organização. Um modo não permitido aparece desativado.

## Como funcionam as permissões

Dois controles funcionam em conjunto:

- O **Sandbox** define quais arquivos e recursos de rede o ChatGPT pode acessar.
- **As aprovações** determinam quando o ChatGPT pausa antes de executar uma ação ou envia a
  solicitação para revisão automática.

Alterar quem revisa uma solicitação não amplia o escopo do Sandbox. Por exemplo,
**Aprovar por mim** mantém o mesmo limite de workspace do modo **Pedir aprovação**;
esse modo encaminha para revisão automática as solicitações que ultrapassariam esse limite.

Use o controle de permissões abaixo do Editor no aplicativo para desktop do ChatGPT ou
na extensão para IDE.

Na CLI, digite `/permissions`. Para detalhes técnicos, consulte
[Sandbox](/pt-BR/codex/sandboxing), [revisão automática](/pt-BR/codex/sandboxing/auto-review) ou
[perfis de permissão](/pt-BR/codex/permissions).

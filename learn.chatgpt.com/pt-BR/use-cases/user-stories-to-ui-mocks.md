<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/user-stories-to-ui-mocks -->

## Introdução

As equipes de produto costumam coletar feedback de várias fontes, como conversas no Slack, issues no Linear, documentos ou planilhas do Google Drive e notas de chamadas com clientes. Em alguns casos, elas têm histórias de usuário claras que ilustram o problema que querem resolver; em outros, o contexto está nessas fontes.

O ChatGPT pode reunir esse contexto e transformá-lo em um mockup de UI para uma funcionalidade que resolva o problema. Depois de validar a proposta, o Codex poderá implementá-la no produto.

## Gere uma referência visual fiel

Se você já tiver uma história de usuário clara, pode começar por ela. Caso contrário, primeiro converse com o ChatGPT para reunir contexto de diferentes fontes e sintetizá-lo em uma história de usuário.

Em seguida, você pode pedir ao ChatGPT que use a geração de imagens para criar algumas propostas de mockup. Os mockups devem respeitar a arquitetura da informação do produto e as restrições do sistema de design.

Se for útil, você pode fornecer capturas de tela da UI atual ou um arquivo do Figma como referência.

Repita esse processo até ficar satisfeito com o mockup. Quanto mais delimitado for o escopo das alterações, maior será a probabilidade de o Codex gerar um mockup que possa ser implementado diretamente.

## Passe do mockup ao protótipo

Use a imagem do mockup final que você quer que o Codex implemente. Selecione o Codex, inicie uma nova conversa e anexe a imagem novamente, em vez de continuar diretamente na conversa do ChatGPT. Em seguida, peça ao Codex para implementar o mockup — com a opção de usar o [plug-in Build Web Apps](https://github.com/openai/plugins/tree/main/plugins/build-web-apps) caso esteja criando um aplicativo web — e transformá-lo em um protótipo funcional:

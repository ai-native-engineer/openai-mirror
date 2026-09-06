<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/deploy-app-or-website -->

## Comece pelo site e pelo destino da implantação

O Codex pode criar ou atualizar um site ou aplicativo, executar as verificações do projeto, implantá-lo com a Vercel e fornecer a URL.

O material fornecido deve ser concreto: um repositório, uma captura de tela, um mapa, um briefing de design, uma nota sobre o produto, a documentação de uma API ou uma fonte de dados. O Codex deve inspecionar o projeto antes de alterá-lo e, depois, usar o plug-in da Vercel para implantar uma prévia por padrão.

Use `@build-web-apps` quando o Codex precisar criar ou aprimorar o aplicativo. Use `@vercel` quando precisar implantar, inspecionar a implantação ou ler os logs de build da Vercel.

## Verifique o resultado antes de compartilhá-lo

O Codex deve informar o que alterou, qual comando usou para fazer o build do projeto e se a implantação da Vercel está pronta. Se a implantação exigir uma variável de ambiente, a escolha de uma equipe, uma configuração de domínio ou uma etapa de login, o Codex deve sinalizar isso em vez de tratar o site como concluído.

Deixe explícitas as alterações em produção. Uma implantação de prévia é o padrão; só peça uma implantação em produção quando essa for realmente a intenção.

## Faça iterações a partir da URL ativa

Assim que tiver a prévia, mantenha o mesmo chat aberto. Peça ao Codex para abrir a URL, corrigir problemas de layout, atualizar os textos, integrar os dados que faltam ou ler os logs da Vercel se a implantação falhar. O chat já tem o contexto do repositório, da implantação e do build.

Boas solicitações de acompanhamento são específicas:

- "O layout em dispositivos móveis está muito apertado. Corrija isso e reimplante a prévia."
- "Use o mesmo projeto e adicione os dados mais recentes de \[source\]."
- "Leia os logs do build que falhou e corrija a implantação."

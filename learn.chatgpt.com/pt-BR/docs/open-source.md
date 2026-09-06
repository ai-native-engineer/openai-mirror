<!-- source: https://learn.chatgpt.com/pt-BR/docs/open-source -->

A OpenAI desenvolve partes essenciais do Codex em código aberto. Esse trabalho está disponível no GitHub para que você possa acompanhar o progresso, relatar issues e contribuir com melhorias.

Se você mantém um projeto de código aberto amplamente utilizado ou quer indicar mantenedores responsáveis por projetos importantes, também pode [se candidatar ao programa Codex for OSS](/community/codex-for-oss) para receber créditos de API, ChatGPT Pro com Codex e acesso seletivo ao Codex Security.

## Componentes de código aberto

| Componente                     | Onde encontrar                                                                                             | Observações                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| CLI do Codex                     | [openai/codex](https://github.com/openai/codex)                                                           | Principal repositório para o desenvolvimento do Codex em código aberto      |
| SDK do Codex                     | [openai/codex/codex-sdk](https://github.com/openai/codex/tree/main/sdk)                                   | O código-fonte do SDK está no repositório do Codex                      |
| CLI do Codex Security            | [openai/codex-security](https://github.com/openai/codex-security)                                         | CLI para encontrar e validar vulnerabilidades de segurança |
| SDK do Codex Security para TypeScript | [openai/codex-security/sdk/typescript](https://github.com/openai/codex-security/tree/main/sdk/typescript) | SDK para TypeScript usado para executar verificações do Codex Security         |
| App Server do Codex              | [openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)         | O código-fonte do App Server está no repositório do Codex               |
| Habilidades                        | [openai/skills](https://github.com/openai/skills)                                                         | Habilidades reutilizáveis que ampliam as funcionalidades do ChatGPT e do Codex           |
| Plug-ins                       | [openai/plugins](https://github.com/openai/plugins)                                                       | Plug-ins reutilizáveis para o ChatGPT e o Codex                  |
| Extensão para IDE                 | -                                                                                                         | Não é de código aberto                                         |
| Codex Cloud                   | -                                                                                                         | Não é de código aberto                                         |
| Ambiente de nuvem universal   | [openai/codex-universal](https://github.com/openai/codex-universal)                                       | Ambiente base usado pelo Codex Cloud                    |

## Onde relatar issues e solicitar recursos

Use o repositório adequado no GitHub para relatar bugs e solicitar recursos:

- Relatos de bugs e solicitações de recursos do Codex: [openai/codex/issues](https://github.com/openai/codex/issues)
- Relatos de bugs e solicitações de recursos dos componentes CLI e SDK para TypeScript do Codex Security: [openai/codex-security/issues](https://github.com/openai/codex-security/issues)
- Fórum de discussão: [openai/codex/discussions](https://github.com/openai/codex/discussions)

Ao abrir uma issue, informe qual componente você está usando (CLI, SDK, extensão para IDE, Codex Cloud ou Codex Security) e, quando possível, a versão.

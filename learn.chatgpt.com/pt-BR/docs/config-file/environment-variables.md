<!-- source: https://learn.chatgpt.com/pt-BR/docs/config-file/environment-variables -->

O Codex usa `config.toml` para configurações persistentes. Use variáveis do ambiente para
substituições no escopo do shell, segredos de automação, comportamento do instalador ou diagnósticos.

Esta página lista as variáveis do ambiente públicas e estáveis que o Codex lê diretamente.
Ela não inclui variáveis internas de desenvolvimento, variáveis de teste nem
nomes de segredos específicos de provedores que você mesmo escolhe com
[`env_key`](/pt-BR/codex/config-file/config-advanced#custom-model-providers).

## Locais principais

| Variável            | Usada por                                    | Padrão      | Descrição                                                                                                                                                      |
| ------------------- | ------------------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_HOME`        | CLI, extensão para IDE, app-server e instaladores | `~/.codex`   | Define o diretório raiz do estado do Codex, incluindo configuração, autenticação, logs, sessões, habilidades e metadados do pacote autônomo. Se essa variável for definida, o diretório já deverá existir. |
| `CODEX_SQLITE_HOME` | Estado da CLI e do app-server                   | `CODEX_HOME` | Define onde os dados de estado armazenados em SQLite são mantidos. A opção de configuração `sqlite_home` tem precedência. Os caminhos relativos são resolvidos a partir do diretório de trabalho atual.           |

Para saber mais sobre os arquivos armazenados em `CODEX_HOME`, consulte
[Locais de configuração e estado](/pt-BR/codex/config-file/config-advanced#config-and-state-locations).

## Variáveis do instalador

Essas variáveis se aplicam aos scripts de instalação autônomos disponibilizados em
`https://chatgpt.com/codex/install.sh` e
`https://chatgpt.com/codex/install.ps1`.

| Variável                | Padrão                                                                              | Descrição                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_NON_INTERACTIVE` | `false`                                                                              | Defina como `1`, `true` ou `yes` para ignorar os prompts do instalador. Os prompts usam a resposta padrão; portanto, use essa opção em instalações e atualizações por script, não na configuração da primeira execução. |
| `CODEX_INSTALL_DIR`     | `~/.local/bin` no macOS/Linux; `%LOCALAPPDATA%\Programs\OpenAI\Codex\bin` no Windows | Altera o local de instalação do comando `codex` visível ao usuário. O cache do pacote autônomo permanece em `CODEX_HOME/packages/standalone`.                        |

Para instalações não assistidas, defina `CODEX_NON_INTERACTIVE=1` no shell que executa
o instalador baixado:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_NON_INTERACTIVE=1 sh

```powershell
$env:CODEX_NON_INTERACTIVE=1; irm https://chatgpt.com/codex/install.ps1 | iex

## Autenticação e rede

| Variável                           | Usada por                                          | Descrição                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_API_KEY`                    | Exec, revisão, TypeScript SDK e exec-server remoto | Fornece uma chave de API para um processo não interativo do Codex. Ao executar código controlado pelo repositório, defina-a inline, e não para o job inteiro.             |
| `CODEX_ACCESS_TOKEN`               | CLI, app-server e automação confiável              | Fornece um token de acesso do ChatGPT ou do Codex para automação confiável. Para persistir o login, envie-o por pipe para `codex login --with-access-token`.             |
| `OPENAI_FEDERATION_RULE_ID`        | Identidade de carga de trabalho                                | Seleciona a regra de federação configurada para a carga de trabalho.                                                                                        |
| `OPENAI_IDENTITY_TOKEN_FILE`       | Identidade de carga de trabalho                                | Aponta para o caminho absoluto do arquivo que contém o token OIDC atual ou o JWT-SVID do SPIFFE.                                                |
| `OPENAI_WORKLOAD_IDENTITY_CONTEXT` | Identidade de carga de trabalho                                | Opcionalmente, fornece identificadores JSON com limites definidos para a atribuição de auditoria informada pelo cliente. Não afeta a autenticação nem a autorização.         |
| `CODEX_CA_CERTIFICATE`             | Clientes HTTPS, de login e WebSocket              | Aponta para um pacote de certificados de CA em formato PEM para ambientes com interceptação corporativa de TLS ou certificados raiz privados. Tem precedência sobre `SSL_CERT_FILE`. |
| `SSL_CERT_FILE`                    | Clientes HTTPS, de login e WebSocket              | Caminho alternativo para o pacote de certificados de CA em formato PEM quando `CODEX_CA_CERTIFICATE` não estiver definida.                                                                               |

Para chaves de API de provedores, defina
[`env_key`](/pt-BR/codex/config-file/config-advanced#custom-model-providers) na configuração do provedor
de modelos. O Codex lê a variável indicada por essa configuração; portanto, o nome
da variável não corresponde a uma variável do ambiente fixa do Codex.

Para saber como gerenciar segredos de automação, consulte
[Usar autenticação por chave de API](/pt-BR/codex/non-interactive-mode#use-api-key-auth).
Para configurar tokens de acesso, consulte [Tokens de acesso](/pt-BR/codex/enterprise/access-tokens).
Para configurar a identidade de carga de trabalho, consulte
[Federação de identidade de carga de trabalho](/pt-BR/codex/enterprise/workload-identity).

## Diagnósticos

| Variável   | Usada por            | Descrição                                                                                                             |
| ---------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `RUST_LOG` | CLI e app-server | Controla a filtragem e a verbosidade dos logs do Rust. Por padrão, `codex exec` gera saída no nível `error`, a menos que você defina um valor mais detalhado. |

`RUST_LOG` aceita valores como `error`, `warn`, `info`, `debug` e
`trace`. Também aceita filtros de log do Rust mais específicos, como
`codex_core=debug,codex_tui=debug`.

Por padrão, a CLI interativa registra diagnósticos em armazenamentos locais com limites definidos, mas
o arquivo de texto simples `codex-tui.log` precisa ser habilitado explicitamente. Defina `log_dir` explicitamente quando
precisar de um log em texto simples para solucionar problemas:

```bash
RUST_LOG=debug codex -c log_dir=./.codex-log
tail -F ./.codex-log/codex-tui.log

No modo não interativo, `codex exec` exibe as mensagens diretamente em vez de gravá-las
em um arquivo de log separado da TUI.

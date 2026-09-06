<!-- source: https://learn.chatgpt.com/pt-BR/docs/security/plugin/deep-scans -->

Execute uma verificação aprofundada quando precisar de uma revisão mais completa e puder aceitar um tempo de
execução mais longo. As verificações aprofundadas examinam um repositório de forma mais abrangente e podem reduzir a
variabilidade entre as execuções.

Comece com uma [verificação padrão](/pt-BR/codex/security/plugin/scans) para conferir o escopo
e os resultados. Depois, use uma verificação aprofundada quando precisar de uma avaliação mais completa.

## Escolher entre verificações padrão e aprofundadas

|                         | Verificação padrão                                      | Verificação aprofundada                                             |
| ----------------------- | -------------------------------------------------- | ----------------------------------------------------- |
| Ideal para                | Primeiras execuções e revisões rotineiras de repositórios ou pastas | Revisões mais completas após uma verificação padrão           |
| Variabilidade             | Padrão                                           | Reduzida                                               |
| Escopo                   | Repositório ou pasta definida explicitamente                      | Repositório ou pasta definida explicitamente                         |
| Tempo de execução e recursos   | Menores                                              | Maiores                                                |
| Pull requests e diffs | Use o fluxo de trabalho de revisão de alterações                     | Não há suporte; em vez disso, use o fluxo de trabalho de revisão de alterações |

## Configurar o tempo de execução da verificação aprofundada

Para controlar a concorrência e a duração de uma verificação aprofundada, crie ou edite
`~/.codex/codex-security/config.toml`. Se você definir `CODEX_HOME`, use
`$CODEX_HOME/codex-security/config.toml` em vez disso.

Por exemplo, este perfil executa uma verificação mais curta com concorrência limitada:

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

| Configuração                         | Padrão | Descrição                                                                                                        |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------ |
| `workers`                       | `4`     | Número de workers independentes de verificação padrão que podem ser executados ao mesmo tempo. O valor legado `"auto"` também é interpretado como `4`. |
| `subagents`                     | `3`     | Número de subagentes que cada worker pode iniciar. Defina `0` para desativá-los.                                                |
| `stop_after_no_new`             | `4`     | Interrompa após o número especificado de verificações consecutivas concluídas por workers sem novos achados.                                   |
| `stop_after_consecutive_errors` | `3`     | Interrompa após o número especificado de erros consecutivos dos workers.                                                                    |
| `max_discovery_runs`            | `40`    | Limite o número de execuções independentes de verificações padrão antes da agregação.                                             |
| `max_time_hours`                | `96`    | Limite a execução dos workers a um número positivo de até `96` horas; use valores fracionários quando necessário.                          |

Valores menores podem reduzir o tempo de verificação e o uso de tokens, mas podem deixar de detectar achados.
As alterações na configuração se aplicam a novas verificações aprofundadas, não às que já estão em andamento.

Quando o limite de tempo expira, o Codex Security interrompe os workers ainda em execução, preserva
os resultados das verificações concluídas e os agrega no relatório final. Se nenhum worker
concluir a revisão do código-fonte antes do prazo, o relatório registra uma cobertura
parcial.

A configuração `max_time_hours` exige a versão `0.1.19` ou posterior do plug-in. Consulte o
[registro de alterações do plug-in](/pt-BR/codex/security/plugin/changelog) para obter detalhes sobre a versão.

## Iniciar a verificação aprofundada

No aplicativo para desktop, abra **Segurança**, selecione **Verificações** e depois **+ Verificação**.
Escolha um repositório ou outra pasta, selecione **Base de código** e ative
**Verificação aprofundada**. A verificação abrange todo o repositório ou toda a pasta selecionada.

Você também pode iniciar uma verificação aprofundada de todo o repositório em uma conversa do Codex:

```text
Use $codex-security:deep-security-scan to run a deep security scan of this repository.

Para um componente em um monorepo, especifique a pasta explicitamente:

```text
Use $codex-security:deep-security-scan to run a deep security scan of /absolute/path/to/repository/services/payments.

Para fazer uma verificação aprofundada com escopo delimitado no aplicativo para desktop, selecione a pasta como base de código.
A verificação abrange toda a pasta selecionada.

## Confirmar a configuração e a pré-verificação

Para obter a melhor qualidade de verificação, use <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
com o nível de esforço de raciocínio `xhigh`.

1. Selecione **Base de código** e ative **Verificação aprofundada**.
2. Confirme se o repositório ou a pasta selecionada corresponde ao código que você pretendia
verificar.
3. Escolha um modelo e um nível de esforço de raciocínio.
4. Abra **Contexto adicional** para informar vetores de ataque concretos, áreas sensíveis
   do aplicativo ou algum contexto do repositório que o código não consiga revelar.
5. Selecione **Iniciar verificação**.

Os workers da verificação aprofundada herdam as configurações selecionadas de modelo e raciocínio. Cada
worker executa uma verificação padrão completa, e o Codex Security agrega os
resultados das verificações concluídas. Acompanhe a verificação salva em **Verificações** ou selecione **Ver
atividade** para inspecionar a tarefa correspondente no Codex. Consulte o [registro de alterações
do plug-in](/pt-BR/codex/security/plugin/changelog) antes de atualizar o plug-in ou
iniciar uma verificação de longa duração.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Acompanhe a fase ativa da verificação aprofundada e inspecione a atividade correspondente no Codex antes de
revisar o resultado concluído.
  </figcaption>
</figure>

## Revisar o resultado

As verificações aprofundadas usam os mesmos detalhes salvos e o mesmo diretório completo das
verificações padrão. Abra a verificação concluída em **Verificações** ou revise seus achados em
**Achados**. O arquivo `report.md` gerado contém links para relatórios detalhados de vulnerabilidades
ou orientações de reforço estrutural quando você solicita esses resultados.
Mantenha os diretórios vinculados `findings/` e `hardening/` junto com o relatório ao
compartilhar ou arquivar o resultado.

Revise o resumo da cobertura antes dos achados. Até uma verificação aprofundada tem limitações,
portanto, verifique as superfícies cuja análise foi adiada e as lacunas de comprovação restantes antes de tirar uma
conclusão. Ao aceitar um achado, prossiga com [Corrigir e verificar um
achado](/pt-BR/codex/security/plugin/fix-findings).

Para revisar um pull request, commit, intervalo de branches ou patch local, use [Revisar alterações
no código](/pt-BR/codex/security/plugin/code-changes). Uma verificação aprofundada nunca substitui
o fluxo de trabalho voltado para diffs.

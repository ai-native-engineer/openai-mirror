<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/skills -->

As Habilidades são fluxos de trabalho reutilizáveis compostos por instruções e recursos de apoio.
As Habilidades do workspace do ChatGPT, as habilidades do sistema de arquivos usadas por recursos locais contemplados
no aplicativo ChatGPT para desktop, na Codex CLI ou na extensão para IDE, e os plug-ins que
empacotam habilidades têm controles separados de ciclo de vida e de acesso.

Para conhecer o modelo completo de administração, consulte
[Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions).

<a id="distinguish-the-distribution-models"></a>

## Distribuição e administração de habilidades

| Modelo de distribuição      | Use para                                                                                           | Escopo de administração                                                                       |
| ----------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Habilidade do workspace do ChatGPT | Compartilhar ou instalar um fluxo de trabalho aprovado por meio dos recursos compatíveis do workspace do ChatGPT              | Permissões e controles do ciclo de vida das habilidades do workspace do ChatGPT                                    |
| Habilidade do sistema de arquivos local  | Carregar um fluxo de trabalho instalado a partir de um local do repositório, do usuário, do administrador ou de um local de sistema fornecido no pacote     | Distribuição pelo sistema de arquivos, configuração do cliente local e permissões em tempo de execução                  |
| Plug-in                  | Empacotar uma ou mais habilidades com conectores opcionais, servidores MCP, hooks e metadados de apresentação | Disponibilidade e instalação do plug-in, além dos controles separados para cada recurso incluído no pacote |

A distribuição de habilidades no workspace do ChatGPT, a instalação de habilidades no sistema de arquivos local e
a instalação de plug-ins específica para cada interface seguem caminhos separados. Mover uma habilidade não
transfere a propriedade no workspace do ChatGPT, o compartilhamento, as atribuições de funções, o estado de instalação do plug-in
nem a autorização do conector.

Os Plug-ins funcionam no Chat e no Work nas versões Web, para desktop e para dispositivos móveis do ChatGPT,
no Codex do aplicativo ChatGPT para desktop e pelo navegador de plug-ins da Codex CLI.
Eles não estão disponíveis na extensão para IDE.
Nessas interfaces com suporte, os plug-ins públicos vêm de um único diretório universal
compartilhado pelo ChatGPT e pelo Codex.

## Controles responsáveis

Consulte [Criar habilidades](/pt-BR/codex/build-skills) para saber mais sobre os locais no sistema de arquivos e a criação de habilidades,
[Habilidades no ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
para conhecer os procedimentos atuais do workspace e [Criar plugins](https://developers.openai.com/plugins/build/plugins) para saber mais sobre
o empacotamento de plug-ins.

Os controles do workspace do ChatGPT não instalam habilidades do sistema de arquivos local nem plug-ins.
A distribuição pelo sistema de arquivos não atribui a propriedade nem funções no workspace do ChatGPT.
A instalação de um plug-in não concede acesso a um conector, servidor MCP ou
serviço conectado. Configure cada recurso na interface de controle
responsável por ele.

## Documentação relacionada

- [Habilidades e plug-ins](/pt-BR/codex/skills-and-plugins)
- [Plug-ins](/pt-BR/codex/plugins)
- [Criar habilidades](/pt-BR/codex/build-skills)
- [Criar plugins](https://developers.openai.com/plugins/build/plugins)
- [Guia de implantação para administradores](/pt-BR/codex/enterprise/admin-setup)
- [Controles de plug-ins](/pt-BR/codex/enterprise/apps-and-connectors)

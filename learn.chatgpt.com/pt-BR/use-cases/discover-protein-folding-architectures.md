<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/discover-protein-folding-architectures -->

## Explore uma hipótese de arquitetura para dobramento de proteínas

Use o modo Meta do Codex quando tiver uma hipótese sobre dobramento de proteínas que exija mais
de uma etapa de implementação. Dê ao Codex uma direção científica delimitada, uma
linha de base funcional e um benchmark com pontuação automática. O Codex pode implementar
o fork da arquitetura, acompanhar experimentos, diagnosticar falhas e continuar
iterando enquanto você analisa as evidências.

Este exemplo começou com uma pergunta específica: um modelo no estilo AlphaFold2
poderia aprender a geometria útil de proteínas com mais eficiência se seu tronco representasse não
apenas resíduos e pares de resíduos, mas também objetos topológicos explícitos de ordem
superior?

## Defina um experimento delimitado

O AlphaFold2 já usa um poderoso raciocínio com pares e triângulos dentro
do Evoformer. Suas operações triangulares aprimoram as representações de arestas, mas ainda
gravam o resultado em um tensor de pares. O cientista propôs testar se representações aprendidas e persistentes
para faces triangulares e células tetraédricas poderiam
fornecer um viés indutivo útil em um contexto com poucos dados.

O repositório público resultante, [SimplexFold](https://github.com/ChrisHayduk/SimplexFold),
adiciona estados esparsos de faces `F_ijk` e estados tetraédricos `U_ijkl`, além da
representação convencional de pares `Z_ij`.

```text
MSA representation M
        <-> pair / edge tensor Z_ij
        <-> sparse face tensor F_ijk
        <-> sparse tetra tensor U_ijkl
        -> structure module
        -> recycled geometry
        loops back into the next pass

Comece com o prompt inicial desta página, uma linha de base mínima no estilo AlphaFold2,
e o benchmark público NanoFold. O benchmark oferece uma base pequena e cuidadosamente selecionada,
com dados fixos e pontuação automática para a realização de experimentos de biologia estrutural.
Mantenha a primeira implementação pequena o suficiente para testá-la com
testes unitários direcionados e microbenchmarks antes de iniciar execuções de treinamento
dispendiosas.

## Execute a busca com o modo Meta

1. Forneça uma hipótese científica falsificável e de alto nível, em vez de pedir ao modelo que crie do zero toda uma agenda de pesquisa.
2. Use o GPT-5.5 Pro no ChatGPT para transformar essa direção em um plano de implementação com restrições e ablações explícitas.
3. Peça ao Codex para implementar a menor linha de base executável do [SimplexFold](https://github.com/ChrisHayduk/SimplexFold) e depois verificá-la com testes unitários direcionados e microbenchmarks.
4. Forneça o repositório resultante ao modo Meta do Codex e instrua-o a melhorar iterativamente o `lDDT-Cα` de validação no benchmark NanoFold, preservando registros de experimentos, planos e referências a artefatos.
5. Execute o modo Meta continuamente enquanto ele usa o feedback do benchmark para iterar sobre a arquitetura, a receita de treinamento e o harness experimental. Neste exemplo, o ciclo foi executado por mais de 150 horas.

Use `PLAN.md` para a estratégia atual e os próximos passos, `EXPERIMENTS.md` para um
registro estruturado dos resultados e `EXPERIMENT_NOTES.md` como rascunho contínuo.
Esses artefatos tornam uma busca de longa duração auditável e oferecem um local estável
para orientar a próxima iteração.

O modo Meta é útil aqui porque a busca exige ciclos repetidos de implementação,
testes, acompanhamento de experimentos, diagnóstico de falhas e iteração orientada pelo
benchmark. A pesquisa automatizada sem orientação muitas vezes se desviava para mudanças locais já conhecidas,
como funções de perda, otimizadores e hiperparâmetros. Uma hipótese de arquitetura concisa, fornecida pelo cientista,
deu ao Codex um espaço de busca mais relevante, sem deixar
de permitir testar, diagnosticar e refinar a implementação.

Este fluxo de trabalho também é útil para equipes que avaliam como a orientação com participação direta de um cientista
muda a qualidade da busca científica agêntica.

## Exemplo de resultado

O resultado deste fluxo de trabalho foi o [SimplexFold](https://github.com/ChrisHayduk/SimplexFold),
uma arquitetura experimental com estados explícitos de simplexos de ordem superior. Analise
a topologia junto aos registros do benchmark para confirmar que cada iteração ainda
testa a ideia científica original.

![Uma comparação da geometria de proteínas com simplexos de dimensões 1, 2 e 3.](/codex/use-cases/discover-protein-folding-architectures-simplex.webp)

A lição importante não é que o Codex resolveu de forma autônoma o dobramento de proteínas. O
fluxo de trabalho mostra como o modo Meta pode atuar como um ciclo persistente de engenharia científica:
um cientista contribui com a ideia conceitual, e o Codex encurta o ciclo de
implementação, experimentação, depuração e busca subsequente.

Considere diagnósticos promissores como evidência de que o caminho de implementação funciona,
não como prova de generalização. Analise periodicamente a trajetória do agente,
redirecione-o para questões de arquitetura com relevância científica caso ele
se limite ao ajuste local de hiperparâmetros e só faça afirmações após
comparações pareadas na validação pública e replicações adequadas.

## Recursos

- [Repositório do SimplexFold](https://github.com/ChrisHayduk/SimplexFold)
- [Plano de benchmark do SimplexFold](https://github.com/ChrisHayduk/SimplexFold/blob/main/BENCHMARK_PLAN.md)
- [Competição NanoFold](https://github.com/ChrisHayduk/nanoFold-Competition)
- [Regras da competição NanoFold](https://github.com/ChrisHayduk/nanoFold-Competition/blob/main/docs/COMPETITION.md)
- [Modo Meta em execução por mais de 150 horas](https://x.com/ChrisHayduk/status/2055757345506877759?s=20)
- [Artigo sobre o modo Meta](https://x.com/ChrisHayduk/status/2053807198870880743?s=20)

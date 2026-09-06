<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/bulk-rna-seq-fastq-qc -->

## Aproveite as Habilidades

O plug-in NGS Analysis inclui:

- `ngs-analysis-router`
- `ngs-bulk-rnaseq-counts-qc`
- `ngs-runtime-env`

Com o plug-in, o ChatGPT pode usar todas essas Habilidades incluídas no pacote.

## Guia passo a passo

1. Indique ao ChatGPT um diretório que contenha a planilha de amostras, os FASTQs, o FASTA do transcriptoma, o FASTA do genoma e o GTF, ou forneça referências exatas para esses arquivos.
2. Execute o prompt inicial para que, antes da execução, o ChatGPT valide a direcionalidade e a consistência das referências e confirme se as ferramentas estão prontas.
3. Abra no ChatGPT o relatório do MultiQC e os artefatos de matriz gerados para avaliar a taxa de mapeamento, a duplicação, a concordância do tipo de biblioteca e a prontidão dos recursos.
4. Continue no mesmo chat para resolver impedimentos, executar novamente com metadados atualizados ou usar as matrizes resultantes em nível de gene na análise posterior de expressão diferencial.

## Resultados

A execução retorna um pacote de contagens revisado quanto ao controle de qualidade, em vez de um resultado de quantificação
sem informações adicionais. Comece pelo relatório do MultiQC para identificar alertas que possam afetar
a interpretação posterior. Neste exemplo, o ChatGPT destaca os alertas do FastQC
sobre o conteúdo das sequências junto com o resumo da execução, para que a equipe possa decidir
se o padrão observado é esperado para o preparo da biblioteca.

![Revise os alertas do FastQC sobre o conteúdo das sequências junto com o resumo da execução de bulk RNA-seq.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-1.webp)

Em seguida, revise as estatísticas do Salmon no mesmo relatório. As taxas de mapeamento,
as atribuições de tipo de biblioteca e os sinais de duplicação permitem verificar rapidamente se os dados estão prontos
antes de prosseguir para a análise de expressão diferencial.

![Examine, no relatório gerado pelo MultiQC, as estatísticas de alinhamento e de tipo de biblioteca do Salmon.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-2.webp)

A matriz resultante de contagens em nível de gene é salva como um artefato reutilizável. Abra-a
no ChatGPT para confirmar a presença das amostras e dos genes esperados; depois, guarde-a
junto com a proveniência da execução para análises posteriores.

![Abra a matriz gerada de contagens em nível de gene para revisão posterior.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-3.webp)

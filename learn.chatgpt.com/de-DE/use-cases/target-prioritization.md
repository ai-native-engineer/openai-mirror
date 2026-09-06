<!-- source: https://learn.chatgpt.com/de-DE/use-cases/target-prioritization -->

## Skills nutzen

Das [Plug-in Life Science Research](https://github.com/openai/plugins/tree/main/plugins/life-science-research)
enthält Skills für jeden Evidenzstrang:

- Humangenetik und GWAS: `gwas-catalog-skill`, `opentargets-skill`, `gnomad-graphql-skill`
- Replikation in Kohorten und PheWAS: `finngen-phewas-skill`, `ukb-topmed-phewas-skill`, `biobankjapan-phewas-skill`, `tpmi-phewas-skill`
- Evidenz zum Zusammenhang zwischen Wirkstoffziel und Erkrankung sowie Krankheitskontext: `opentargets-skill`, `efo-ontology-skill`
- Klinische und regulatorische Präzedenzfälle: `clinicaltrials-skill`, `opentargets-skill`, `chembl-skill`, `pharmgkb-skill`
- Literatur und Kontext öffentlicher Datensätze: `ncbi-entrez-skill`, `ncbi-pmc-skill`, `biorxiv-skill`, `ncbi-datasets-skill`, `biostudies-arrayexpress-skill`
- Expression sowie Kontext zu Gewebe und Zelltyp: `human-protein-atlas-skill`, `gtex-eqtl-skill`, `cellxgene-skill`, `bgee-skill`

Nutze diese Skills, indem du sie ausdrücklich nennst, oder überlasse ChatGPT die Entscheidung, wann sie eingesetzt werden.

## Schritt-für-Schritt-Anleitung

1. Beginne mit einer konkreten Vergleichsfrage und nenne genau, welche Wirkstoffziele, welche Krankheit und welche Evidenzstränge ChatGPT untersuchen soll.
2. Rufe das Plug-in `Life Science Research` auf und weise ChatGPT an, die Evidenzstränge mithilfe von Subagenten parallel zu bearbeiten, damit die einzelnen Evidenzarten klar voneinander abgegrenzt bleiben.
3. Bitte ChatGPT, jeden Evidenzstrang anhand einer festen Skala von 1 bis 5 zu bewerten und direkte Evidenz für die Erkrankung von Evidenz zu verwandten Phänotypen getrennt zu halten.
4. Prüfe im selben Chat die gespeicherten Roh-Payloads, die Bewertungstabelle nach Evidenzstrang und Wirkstoffziel sowie die daraus abgeleitete Gesamtrangfolge.

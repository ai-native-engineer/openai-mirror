<!-- source: https://learn.chatgpt.com/ko-KR/use-cases/target-prioritization -->

## 스킬 활용하기

[Life Science Research 플러그인](https://github.com/openai/plugins/tree/main/plugins/life-science-research)에는
각 증거 영역에 필요한 스킬이 포함되어 있습니다:

- 인간 유전학 및 GWAS: `gwas-catalog-skill`, `opentargets-skill`, `gnomad-graphql-skill`
- 코호트 재현 검증 및 PheWAS: `finngen-phewas-skill`, `ukb-topmed-phewas-skill`, `biobankjapan-phewas-skill`, `tpmi-phewas-skill`
- 표적-질환 근거 및 질환 맥락: `opentargets-skill`, `efo-ontology-skill`
- 임상 및 규제 선례: `clinicaltrials-skill`, `opentargets-skill`, `chembl-skill`, `pharmgkb-skill`
- 문헌 및 공개 데이터 세트 맥락: `ncbi-entrez-skill`, `ncbi-pmc-skill`, `biorxiv-skill`, `ncbi-datasets-skill`, `biostudies-arrayexpress-skill`
- 발현 및 조직/세포 유형 맥락: `human-protein-atlas-skill`, `gtex-eqtl-skill`, `cellxgene-skill`, `bgee-skill`

이 스킬을 직접 지정해 사용하거나, 언제 사용할지는 ChatGPT가 결정하도록 할 수 있습니다.

## 단계별 가이드

1. 먼저 구체적인 비교 질문을 제시하고, ChatGPT가 다뤄야 할 표적과 질환, 증거 영역을 정확히 명시하세요.
2. `Life Science Research` 플러그인을 호출한 다음, 각 증거 유형의 조사 범위가 명확히 구분되도록 하위 에이전트를 사용해 증거 영역을 병렬로 조사하라고 ChatGPT에 지시하세요.
3. 각 증거 영역을 고정된 1~5점 척도로 채점하고, 질환에 대한 직접적인 근거와 인접 표현형에 대한 근거를 구분하도록 ChatGPT에 요청하세요.
4. 같은 채팅에서 저장된 원시 페이로드, 증거 영역별·표적별 점수표, 종합 순위를 검토하세요.

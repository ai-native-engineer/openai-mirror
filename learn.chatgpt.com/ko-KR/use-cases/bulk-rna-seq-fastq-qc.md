<!-- source: https://learn.chatgpt.com/ko-KR/use-cases/bulk-rna-seq-fastq-qc -->

## 스킬 활용

NGS Analysis 플러그인에는 다음 스킬이 포함되어 있습니다:

- `ngs-analysis-router`
- `ngs-bulk-rnaseq-counts-qc`
- `ngs-runtime-env`

플러그인을 사용하면 ChatGPT가 패키지에 포함된 이 모든 스킬을 활용할 수 있습니다.

## 단계별 가이드

1. 샘플 시트, FASTQ, 전사체 FASTA, 유전체 FASTA, GTF가 있는 디렉터리를 ChatGPT에 지정하거나 정확한 파일 참조를 제공하세요.
2. 분석을 시작하기 전에 ChatGPT가 가닥 특이성, 참조 데이터 일관성, 도구 준비 상태를 검증하도록 스타터 프롬프트를 실행하세요.
3. 생성된 MultiQC와 행렬 아티팩트를 ChatGPT에서 열어 매핑률, 중복도, 라이브러리 유형 일치 여부, 리소스 준비 상태를 검토하세요.
4. 같은 채팅에서 계속 작업하며 진행을 막는 문제를 해결하거나, 업데이트된 메타데이터로 다시 실행하거나, 생성된 유전자 수준 행렬을 후속 차등 발현 분석에 넘기세요.

## 결과

실행 결과로 단순한 정량화 출력이 아니라 QC 검토를 거친 카운트 번들이
반환됩니다. 먼저 MultiQC 보고서에서 후속 해석에 영향을 줄 수 있는 경고를
확인하세요. 이 예시에서는 ChatGPT가 실행 요약과 함께 FastQC의 서열 구성
경고를 보여 주므로, 팀은 관찰된 패턴이 라이브러리 제작 방식에서 예상되는
결과인지 판단할 수 있습니다.

![bulk RNA-seq 실행 요약과 함께 FastQC의 서열 구성 경고를 검토하세요.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-1.webp)

다음으로 같은 보고서에서 Salmon 통계를 검토하세요. 매핑률,
라이브러리 유형 할당, 중복 신호를 통해 차등 발현 분석 전 준비 상태를
간단히 확인할 수 있습니다.

![생성된 MultiQC 보고서에서 Salmon 정렬 및 라이브러리 유형 통계를 확인하세요.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-2.webp)

결과로 생성된 유전자 수준 카운트 행렬은 재사용 가능한 아티팩트로 저장됩니다. 이 행렬을
ChatGPT에서 열어 예상한 샘플과 피처가 포함되어 있는지 확인한 다음, 후속 분석을 위해
실행 이력과 함께 보관하세요.

![후속 검토를 위해 생성된 유전자 수준 카운트 행렬을 여세요.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-3.webp)

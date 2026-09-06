<!-- source: https://learn.chatgpt.com/ko-KR/use-cases/discover-protein-folding-architectures -->

## 단백질 접힘 아키텍처 가설 탐색

여러 차례의 구현 작업이 필요한 단백질 접힘 가설이 있다면 Codex Goal Mode를 사용하세요.
Codex에 범위가 한정된 과학적 방향, 작동하는 베이스라인, 자동 채점 가능한
벤치마크를 제공하세요. Codex는 아키텍처 포크를 구현하고 실험을 추적하며
실패를 진단하고, 사용자가 증거를 검토하는 동안에도 반복 작업을
계속할 수 있습니다.

이 사례는 다음과 같은 구체적인 질문에서 시작했습니다. AlphaFold2 스타일 모델의
트렁크가 잔기와 잔기 쌍뿐 아니라 명시적인 고차 위상 객체까지 표현한다면,
유용한 단백질 기하를 제한된 데이터로도 더 효율적으로 학습할 수
있을까요?

## 범위가 한정된 실험 정의

AlphaFold2는 이미 Evoformer 내부에서 강력한 쌍별 추론과 삼각형 기반 추론을
사용합니다. 삼각형 연산은 에지 표현을 개선하지만, 결과는 여전히 쌍 텐서에
다시 기록됩니다. 과학자는 삼각형 면과 사면체 셀의 학습된 표현을 지속적으로 유지하는 방식이
데이터가 제한된 환경에서 유용한 귀납적 편향을 제공할 수 있는지
검증하자고 제안했습니다.

그 결과 만들어진 공개 레포지토리 [SimplexFold](https://github.com/ChrisHayduk/SimplexFold)에는
희소 면 상태 `F_ijk`와 사면체 상태 `U_ijkl`가 기존의
쌍 표현 `Z_ij`와 함께 추가되었습니다.

```text
MSA representation M
        <-> pair / edge tensor Z_ij
        <-> sparse face tensor F_ijk
        <-> sparse tetra tensor U_ijkl
        -> structure module
        -> recycled geometry
        loops back into the next pass

이 페이지의 시작 프롬프트, 최소한의 AlphaFold2 스타일 베이스라인,
NanoFold 공개 벤치마크로 시작하세요. 이 벤치마크는 작고 엄선된 고정
데이터셋으로 구성되며 자동 채점이 가능한 구조생물학 실험 환경을 제공합니다.
비용이 많이 드는 학습을 실행하기 전에 선별된 단위 테스트와
마이크로벤치마크로 테스트할 수 있을 만큼 첫 구현의 범위를 작게
유지하세요.

## Goal Mode로 탐색 실행

1. 모델에게 연구 의제 전체를 처음부터 만들라고 요청하는 대신, 반증 가능한 상위 수준의 과학적 가설을 제공하세요.
2. ChatGPT에서 GPT-5.5 Pro를 사용해 그 방향을 명시적인 제약 조건과 어블레이션이 포함된 구현 계획으로 구체화하세요.
3. Codex에 실행 가능한 최소 규모의 [SimplexFold](https://github.com/ChrisHayduk/SimplexFold) 베이스라인을 구현하도록 요청한 다음, 선별된 단위 테스트와 마이크로벤치마크로 검증하세요.
4. 그 결과 만들어진 레포지토리를 Codex Goal Mode에 제공하고, 실험 로그, 계획, 아티팩트 참조를 보존하면서 NanoFold 벤치마크의 검증 `lDDT-Cα` 점수를 점진적으로 높이도록 지시하세요.
5. Goal Mode를 계속 실행하여 벤치마크 피드백을 바탕으로 아키텍처, 학습 레시피, 실험 하네스를 반복해서 개선하도록 하세요. 이 사례에서 루프는 150시간 넘게 실행되었습니다.

현재 전략과 다음 단계는 `PLAN.md`에, 구조화된 결과 로그는
`EXPERIMENTS.md`에, 진행 중인 스크래치패드는 `EXPERIMENT_NOTES.md`에 기록하세요.
이러한 아티팩트 덕분에 장기간의 탐색 과정을 추적하고 감사할 수 있으며, 다음 반복을
조정할 안정적인 공간도 확보할 수 있습니다.

이 탐색에는 구현, 테스트, 실험 추적, 실패 진단, 벤치마크 기반 반복이
계속 필요하므로 Goal Mode가 유용합니다. 방향을 제시하지 않은 자동 연구는
손실 함수, 옵티마이저, 하이퍼파라미터처럼 익숙하고 국소적인 변경으로
흐르는 경우가 많았습니다. 과학자가 제공한 간결한 아키텍처 가설 덕분에
Codex는 더 의미 있는 탐색 공간에 집중하면서도 구현을 테스트하고 진단해
개선할 여지를 유지할 수 있었습니다.

이 워크플로우는 과학자가 루프에 참여해 방향을 제시할 때 에이전트형
과학 탐색의 품질이 어떻게 달라지는지 평가하는 팀에도 유용합니다.

## 결과 예시

이 워크플로우의 결과물은 명시적인 고차 심플렉스 상태를 갖춘
실험적 아키텍처 [SimplexFold](https://github.com/ChrisHayduk/SimplexFold)였습니다. 각 반복이 여전히
원래의 과학적 아이디어를 검증하는지 확인하려면 벤치마크 로그와 함께
위상 구조를 검토하세요.

![1-, 2-, 3-심플렉스 단백질 기하 비교.](/codex/use-cases/discover-protein-folding-architectures-simplex.webp)

여기서 얻을 수 있는 교훈은 Codex가 단백질 접힘 문제를 자율적으로 해결했다는 것이
아닙니다. 이 워크플로우는 Goal Mode가 지속적으로 작동하는 과학 엔지니어링
루프가 될 수 있음을 보여 줍니다. 과학자가 개념적 전환을 제시하면 Codex가
구현, 실험, 디버깅, 후속 탐색으로 이어지는 주기를 단축합니다.

유망한 진단 결과는 구현 방식이 작동한다는 증거로만 보고, 일반화의 증명으로
간주하지 마세요. 에이전트의 진행 과정을 주기적으로 검토하고, 탐색이 국소적인
하이퍼파라미터 튜닝으로 축소되면 과학적으로 의미 있는 아키텍처 문제로
돌아가도록 방향을 조정하세요. 주장은 공개 검증에서 조건을 맞춘 비교와 적절한
반복 실험을 거친 후에만 제시하세요.

## 리소스

- [SimplexFold 레포지토리](https://github.com/ChrisHayduk/SimplexFold)
- [SimplexFold 벤치마크 계획](https://github.com/ChrisHayduk/SimplexFold/blob/main/BENCHMARK_PLAN.md)
- [NanoFold 대회](https://github.com/ChrisHayduk/nanoFold-Competition)
- [NanoFold 대회 규칙](https://github.com/ChrisHayduk/nanoFold-Competition/blob/main/docs/COMPETITION.md)
- [150시간 넘게 실행된 Goal Mode](https://x.com/ChrisHayduk/status/2055757345506877759?s=20)
- [Goal Mode 소개 글](https://x.com/ChrisHayduk/status/2053807198870880743?s=20)

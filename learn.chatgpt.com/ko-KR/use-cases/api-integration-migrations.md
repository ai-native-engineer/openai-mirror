<!-- source: https://learn.chatgpt.com/ko-KR/use-cases/api-integration-migrations -->

## 소개

새 모델과 API 기능이 출시되면 최신 개선 사항을 활용할 수 있도록 통합을 업그레이드하는 것이 좋습니다.
모델을 전환할 때는 모델 이름만 바꾸는 것으로 충분하지 않은 경우가 많습니다.

API에도 변경 사항이 있을 수 있습니다. 예를 들어 GPT-5.4 모델에서는 어시스턴트 메시지에 새로운 `phase` 매개변수를 추가했으며, 통합에 이 매개변수를 포함하는 것이 중요합니다. 무엇보다 모델의 동작이 달라져 기존 프롬프트를 수정해야 할 수도 있습니다.

새 모델로 마이그레이션할 때는 필요한 코드를 변경하는 데 그치지 말고 워크플로우에 미치는 영향도 평가해야 합니다.

## OpenAI 문서 스킬 활용하기

[모델 가이드](/api/docs/guides/latest-model) 페이지에서는 모델 세대별로 API 기능, 모델 동작, 마이그레이션, 프롬프팅 지침을 한데 모아 제공합니다.

OpenAI 문서 스킬에는 마이그레이션에 직접 참고할 수 있는 [구체적인 지침](https://github.com/openai/codex/blob/6323f0104d17d211029faab149231ba787f7da37/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-5p4.md)도 포함되어 있습니다. 현재 업그레이드 대상에 관한 내용은 [모델 가이드](/api/docs/guides/latest-model) 페이지를 참고하세요.

Codex에는 이제 OpenAI 문서 스킬이 기본으로 포함됩니다. OpenAI API로 개발할 때 최신 문서와 지침을 모두 활용할 수 있도록 프롬프트에 이 스킬을 명시하세요.

## 견고한 평가 파이프라인 구축하기

Codex는 최신 프롬프트 지침에 따라 프롬프트를 자동으로 업데이트할 수 있지만, 통합이 예상대로 작동하는지 자동으로 검증할 방법도 마련해야 합니다.

통합을 변경할 때마다 실행하여 기존 동작에 회귀 문제가 생기지 않았는지 확인할 수 있는 평가 파이프라인을 구축하세요.

이 [Cookbook 가이드](/cookbook/examples/evaluation/building_resilient_prompts_using_an_evaluation_flywheel)에서는 OpenAI의 [Evals API](/api/docs/guides/evals)로 이러한 검증을 수행하는 방법을 자세히 설명합니다.

<!-- source: https://learn.chatgpt.com/ko-KR/use-cases/github-code-reviews -->

## 사용 방법

먼저 GitHub 조직 또는 레포지토리에 Codex 코드 검토를 추가하세요.
자세한 내용은 [GitHub의 Codex 코드 검토](/ko-KR/codex/third-party/github)를 참고하세요.

Codex가 모든 Pull Request를 자동으로 검토하도록 설정할 수도 있고, Pull Request 댓글에 `@codex review`를 입력해 검토를 요청할 수도 있습니다.

Codex가 회귀나 잠재적 이슈를 지적하면 Pull Request에 `@codex fix it` 같은 후속 프롬프트를 댓글로 남겨 수정을 요청할 수 있습니다.

그러면 이슈를 수정하고 Pull Request를 업데이트하는 새 클라우드 채팅이 시작됩니다.

## 검토 지침 정의하기

Codex의 검토 대상을 맞춤 설정하려면 규칙이 적용되는 코드에 가장 가까운
`AGENTS.md`에 `## Code Review Rules` 섹션을 추가하세요. 예를 들면 다음과 같습니다:

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

레포지토리 전체에 적용되는 규칙은 루트 `AGENTS.md`에, 서비스별 규칙은
하위 경로의 파일에 작성하세요. 규칙은 간결하게 작성하고,
문제로 표시해야 할 동작과 안전한 처리 방법 또는 예외를 설명하세요. 포맷팅과 린트 검사는 CI에 맡기세요.
설정 및 규칙 작성 지침은 [Codex의 검토 대상 맞춤 설정](/ko-KR/codex/third-party/github#customize-what-codex-reviews)을
참고하세요.

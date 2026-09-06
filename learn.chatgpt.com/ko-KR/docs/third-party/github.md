<!-- source: https://learn.chatgpt.com/ko-KR/docs/third-party/github -->

GitHub Pull Request를 한 번 더 검토해 유의미한 피드백을 얻으려면 Codex 코드 검토를
사용하세요. Codex는 Pull Request diff를 검토하고 레포지토리 지침을 따르며,
심각한 이슈에 집중한 표준 GitHub 코드 검토를 게시합니다. 연구 프리뷰로
제공되는 보안 검토는 Pull Request의 잠재적인 보안 이슈를
더 심층적으로 검토합니다.

<br />

## 시작하기 전에

다음 사항을 준비하세요:

- 검토하려는 레포지토리에 [Codex 클라우드](/ko-KR/codex/cloud)가 설정되어 있어야 합니다.
- [Codex 코드 검토 설정](https://chatgpt.com/codex/settings/code-review)에 접근할 수 있어야 합니다.
- Codex가 레포지토리별 검토 지침을 따르도록 하려면 `AGENTS.md` 파일이 필요합니다.

## Codex 코드 검토 설정

자동 검토를 구성하려면 연결된 GitHub 레포지토리와 해당 설정에 대한
GitHub push 또는 admin 권한이 필요합니다.

1. [Codex 클라우드](/ko-KR/codex/cloud)를 설정하세요.
2. [Codex 설정](https://chatgpt.com/codex/settings/code-review)으로 이동하세요.
3. 레포지토리에서 **코드 검토를** 켜세요.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## Codex 검토 요청하기

1. Pull Request 댓글에서 `@codex review`를 멘션하세요.
2. Codex가 반응(👀)을 남기고 검토를 게시할 때까지 기다리세요.

<div class="not-prose max-w-xl mr-auto">
  
    
      
    
  
</div>
<br />

Codex는 팀원처럼 Pull Request에 검토를 게시합니다. GitHub에서는
검토 댓글이 우선순위가 높은 리스크에 집중되도록 Codex가 P0 및 P1 이슈만
표시합니다.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## 자동 검토 활성화

Codex가 모든 Pull Request를 자동으로 검토하도록 하려면 [Codex 설정](https://chatgpt.com/codex/settings/code-review)에서
**자동 검토를** 켜세요.
새 PR이 검토 대상으로 열릴 때마다 `@codex review` 댓글이
없어도 Codex가 검토를 게시합니다.

## Codex 검토 대상 맞춤 설정

Codex는 레포지토리에서 `AGENTS.md` 파일을 찾아 적용 가능한 코드 검토
규칙을 따릅니다. 규칙이 적용되는 코드와 가장 가까운 파일에 `## Code Review Rules` 섹션을
추가하세요. 필요하면 `###` 제목을 사용해 관련 검사를
그룹화하세요.

예를 들어 실험 보고 서비스에서는 노출 이후의 동작이 비교 코호트를
변경하지 않도록 할 수 있습니다:

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

레포지토리 전체 규칙은 루트 `AGENTS.md`에, 서비스별 규칙은
`services/experiment_reporting/AGENTS.md` 같은 중첩 파일에 작성하세요. Codex는
변경된 각 파일에 적용되는 루트 지침과 더 구체적인 지침을 함께 적용하므로,
관련 없는 변경 사항에 서비스별 컨텍스트를 포함할 필요가 없습니다.

검토자가 자주 설명하는 검사 기준을 담은 간결한 규칙 두세 개로 시작하세요. 유용한 규칙은 다음과 같습니다:

- **영향이 크고 레포지토리에 특화된 동작에 집중하세요.** 표시해야 할
  호환성 제약, 데이터 경계 또는 안전하지 않은 사이드 이펙트와 그것이
  중요한 이유를 설명하세요.
- **안전한 처리 방법이나 예외를 명시하세요.** Codex가 실제 이슈와
  예상되는 동작을 구별할 수 있도록 충분한 컨텍스트를 제공하세요.
- **규칙의 적용 범위를 명확히 하고 오래 유효하도록 작성하세요.** 바뀔 수 있는
  함수 이름보다는 결과를 중심으로 쓰고, 지침은 적용 대상 코드 가까이에 배치하세요.
- **기계적으로 수행할 수 있는 검사는 CI에 맡기세요.** 포매팅, 린트 등
  정해진 기준으로 판정할 수 있는 검사는 검토 규칙에 포함하지 마세요.

대표적인 Pull Request를 열고 `@codex review`로 검토를 요청하세요.
검토 결과와 피드백을 바탕으로 규칙을 다듬고, 노이즈를 유발하는 지침은
범위를 좁히거나 삭제하세요.

코드 검토 규칙은 Codex에 지침을 제공할 뿐, 테스트나 브랜치 보호 또는
필수 승인을 대체하지 않습니다.

이번 한 번만 특정 항목에 집중해서 검토하려면 Pull Request 댓글에 해당 내용을 추가하세요:

`@codex review for issues in the database migration`

## 보안 검토

보안 검토는 Pull Request의 보안 이슈를 특히 주의 깊게 살펴보려는
고객을 위한 추가 검토입니다. Pull Request diff, 관련 레포지토리 컨텍스트,
구성된 위협 모델 또는 보안 지침을 분석하여 코드 검토보다
보안 관련 리스크를 더 심층적으로
검토합니다.

코드 검토도 일반적인 검토 과정에서 보안 관련 이슈를 식별할 수 있으므로,
코드 검토와 보안 검토의 결과가
때때로 겹칠 수 있습니다.

### 보안 검토 설정

자세한 설정 안내와 구성 옵션은 [보안
검토](/ko-KR/codex/security/security-review)를 참조하세요.

1. [Codex 클라우드](/ko-KR/codex/cloud)를 설정하세요.
2. [Codex 설정](https://chatgpt.com/codex/settings/code-review)으로 이동하세요.
3. **레포지토리 환경 설정에서** 보안 검토 대상 Pull Request와
   실행 시점을 선택하세요. 코드 검토와 함께 실행하려면 **코드 검토가 실행될 때마다** 
   옵션을 선택하세요.

### 보안 검토 요청하기

보안 검토를 수동으로 요청하려면 Pull Request에 다음 댓글을 추가하세요:

`@codex security review`

검토가 진행되는 동안 Codex가 반응하고, 완료되면 보안 이슈를 Pull Request에 직접
게시합니다. 연결된 Codex 작업을 열고 **보안
보고서** 탭을 선택해 전체 보고서를 확인하세요.

## 검토 결과에 대응하기

Codex가 검토를 게시한 후 같은 Pull Request에 댓글을 하나 더 남겨 이슈를
수정해 달라고 요청할 수 있습니다:

```md
@codex fix the P1 issue

Codex는 Pull Request를 컨텍스트로 사용해 클라우드 채팅을 시작하며, 필요한 권한이
있으면 수정 사항을 해당 브랜치에 푸시할 수 있습니다.

## Codex에 다른 작업 맡기기

댓글에서 `review`가 아닌 다른 내용과 함께 `@codex`를 멘션하면, Codex가 Pull Request를 컨텍스트로 사용해 [클라우드 채팅](/ko-KR/codex/cloud)을 시작합니다.

```md
@codex fix the CI failures

## 코드 검토 문제 해결

Codex가 반응하지 않거나 검토를 게시하지 않는 경우:

- [Codex 설정](https://chatgpt.com/codex/settings/code-review)에서 해당 레포지토리의 **코드 검토가** 켜져 있는지 확인하세요.
- [Codex 클라우드](/ko-KR/codex/cloud)가 설정된 레포지토리의 Pull Request인지 확인하세요.
- Pull Request 댓글에 정확한 트리거인 `@codex review`를 사용하세요.
- 자동 검토의 경우 **자동 검토가** 켜져 있는지, Pull Request 이벤트가
  검토 트리거 설정과 일치하는지 확인하세요.

<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/security-review -->

Codex Security 검토는 연구 프리뷰로 제공됩니다.
ChatGPT Enterprise, Business, Edu, Pro 고객이 이용할 수 있으며
Plus에서는 이용할 수 없습니다. 도입 기간에는 Codex Security 검토에
ChatGPT 크레딧이 사용되지 않습니다. 사용량 제한이 적용될 수 있습니다.

Codex Security 검토는 Pull Request의 보안 이슈를
특히 중점적으로 살펴보려는 고객을 위한 추가 검토입니다.

Codex Security 검토는
Pull Request의 diff, 관련 레포지토리 컨텍스트, 구성된 위협 모델
또는 보안 지침을 분석하여 보안 관련 리스크를 [코드
검토](/ko-KR/codex/third-party/github)보다 심층적으로 다룹니다. 코드 검토도
일반 검토 과정에서 보안 관련 이슈를 식별할 수 있으므로 발견된 보안 이슈가 간혹 겹칠 수 있습니다.

## 시작하기 전에

Codex Security 검토가 자동으로 실행되도록 구성하려면 다음이 필요합니다:

- 워크스페이스의 Codex Security 검토 연구 프리뷰 이용 권한
- GitHub 레포지토리를 연결해 설정한 [Codex 클라우드](/ko-KR/codex/cloud)
- 레포지토리 설정에 필요한 GitHub 푸시 또는 관리자 권한

기존 Codex Security 스캔은 선택 사항입니다.

<a id="configure-security-review"></a>

## Codex Security 검토 구성

1. [Codex 설정](https://chatgpt.com/codex/settings/code-review)으로 이동하세요.
2. **레포지토리 환경설정에서** Codex
   Security 검토를 적용할 Pull Request를 선택하세요:
   - **개인 설정 따르기를** 선택하면 각 기여자가
     개인 Codex Security 검토 설정에서 직접 활성화할 수 있습니다.
   - **모든 PR 검토는** 레포지토리의 모든 Pull Request에 적용됩니다.
   - **팀 PR 검토는** 사용 가능한 경우 GitHub 팀 구성원이 아니라
     ChatGPT 워크스페이스 구성원이 연 Pull Request에 적용됩니다.
3. Codex Security 검토의 실행 시점을 선택하세요:
   - **PR을 열 때는** Pull Request가 열리면 독립적으로 실행됩니다.
   - **푸시할 때마다** 새 커밋이 푸시된 후 독립적으로 실행됩니다.
   - **코드 검토가 실행될 때마다** 옵션을 사용하려면 코드 검토가 필요하며, Codex Security
     검토도 함께 실행됩니다.

## 위협 모델 컨텍스트 추가

위협 모델을 구성하면 애플리케이션의 자산, 신뢰 경계, 보안 가정,
레포지토리별 리스크에 관한 컨텍스트를 Codex에 제공할 수 있습니다.
레포지토리에 기존 Codex Security 스캔 구성이 있다면 해당 구성의
위협 모델을 사용할 수 있습니다. 그렇지 않으면 레포지토리에 커밋된
위협 모델 파일의 경로를 입력하세요. 소스를 지정하지 않으면 Codex가
검토할 때마다 위협 모델을 다시 생성합니다.

## 보고 임계값 설정

기본적으로 자동 Codex Security 검토는 **높음** 및 **심각**
등급의 보안 이슈를 보고하고, 수동으로 요청한 검토는 **중간**, **높음**,
**심각** 등급의 보안 이슈를 보고합니다. 자동 검토와 수동 검토의 최소 심각도는
각각 변경할 수 있으며 경로 기반 재정의도 추가할 수 있습니다.

Pull Request에 게시된 보안 이슈에는 해당 Pull Request의 GitHub
공개 범위가 적용됩니다. Pull Request를 볼 수 있는 사람은 누구나 보안 이슈도 볼 수 있으며,
공개 레포지토리나 워크스페이스 외부 기여자가 연 Pull Request도
마찬가지입니다. Pull Request 댓글이 광범위하게 공개될 수 있는 레포지토리에서는
보고 임계값을 신중하게 선택하세요. 보고 임계값은 Codex가 GitHub에
게시하는 내용을 제어하며, 전체 Codex Security 검토 보고서는
Codex에 계속 유지됩니다.

<a id="request-a-security-review"></a>

## Codex Security 검토 요청

Codex Security 검토를 수동으로 요청하려면 Pull Request에 다음 댓글을 추가하세요:

`@codex security review`

검토가 실행되는 동안 Codex가 리액션을 표시한 후, 수동 보고 임계값을 충족하는
보안 이슈를 Pull Request에 직접 게시합니다. 관련
Codex 작업을 열고 **보안 보고서** 탭을 선택하면 심각도, 공격 경로, 근거 자료,
검증, 해결 지침을 포함한 전체 보고서를 볼 수 있습니다.
보고 임계값을 충족하는 보안 이슈가 없으면 Codex는
Pull Request에 보안 이슈를 게시하지 않습니다.

## 관련 문서

- [Codex로 GitHub Pull Request 검토하기](/ko-KR/codex/third-party/github)에서는 코드 검토와 GitHub 연동을 설명합니다.
- [Codex Security](/ko-KR/codex/security)에서는 제품 개요를 설명합니다.
- [Codex Security 클라우드 설정](/ko-KR/codex/security/setup)에서는 레포지토리 스캔과 보안 이슈 검토를 설명합니다.
- [위협 모델 개선](/ko-KR/codex/security/threat-model)에서는 레포지토리 컨텍스트를 조정하는 방법을 설명합니다.

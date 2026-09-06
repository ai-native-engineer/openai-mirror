<!-- source: https://learn.chatgpt.com/ko-KR/use-cases/native-ios-apps -->

## 앱과 빌드 루프 스캐폴딩

그린필드 작업은 일반 프롬프팅으로 시작하세요. Codex에 스타터 iOS SwiftUI 앱을 스캐폴딩하고 [로컬 환경](/ko-KR/codex/environments/local-environment)의 `Build` 작업에 연결할 수 있는 간단한 빌드 및 실행 스크립트를 작성하도록 요청하세요.

루프를 CLI 중심으로 유지하세요. Apple의 `xcodebuild`를 사용하면 터미널에서 스킴을 나열하고 빌드, 테스트, 아카이브, `build-for-testing`, `test-without-building` 작업을 처리할 수 있으므로 Codex가 Xcode GUI를 오가지 않고 에이전트 루프 안에서 계속 작업할 수 있습니다.

더 깔끔한 프로젝트 생성기를 원하고 서드 파티 도구를 사용해도 괜찮다면 다음 단계로 [Tuist](https://tuist.dev/)를 사용하는 것이 좋습니다. GUI 없이 Xcode 프로젝트를 생성하고 빌드할 수 있으며, Codex는 터미널에서 계속 앱을 빌드하고 실행할 수 있습니다.

완전한 Xcode 프로젝트에서 더 심층적인 자동화가 필요해지면 [XcodeBuildMCP](https://www.xcodebuildmcp.com/)를 사용하세요. 스킴, 타깃, 시뮬레이터 제어, 스크린샷, 로그 및 UI 상호작용이 중요해져 단순한 셸 명령만으로는 충분하지 않은 시점입니다.

## 스킬 활용하기

첫 단계에서는 스킬이나 MCP 서버가 필요하지 않은 경우가 많습니다. 작업이 전문화되거나 실행 과정에 더 탄탄한 SwiftUI 규칙을 반영하려는 경우 스킬을 추가하세요.

- [SwiftUI expert](https://github.com/AvdLee/SwiftUI-Agent-Skill)는 다양한 모범 사례가 이미 반영된 강력한 범용 SwiftUI 스킬입니다.
- [SwiftUI Pro](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/main/swiftui-pro/SKILL.md)는 최신 API, 유지보수성, 접근성 및 성능을 폭넓게 검토하는 SwiftUI 스킬입니다.

- [Liquid Glass expert](https://github.com/Dimillian/Skills/blob/main/swiftui-liquid-glass/SKILL.md)는 Codex가 새로운 iOS 26 Liquid Glass API를 도입하고 최신 시스템 디자인에 맞게 사용자 지정 컴포넌트를 조정하도록 돕습니다.
- [SwiftUI performance](https://github.com/Dimillian/Skills/blob/main/swiftui-performance-audit/SKILL.md)는 기능이 느리게 느껴지거나 SwiftUI 뷰 업데이트 경로가 의심스러울 때 유용합니다. 일반적인 SwiftUI 실수를 검사하고 수정할 항목과 성능 향상 폭이 가장 큰 지점을 우선순위별 보고서로 제공합니다.
- [Swift concurrency expert](https://github.com/Dimillian/Skills/blob/main/swift-concurrency-expert/SKILL.md)는 이해하기 어려운 오류와 컴파일러 경고가 원하는 변경을 가로막을 때 유용합니다. GPT-5.6 Terra에서는 필요성이 줄어들 수 있지만 Swift 동시성 진단 메시지가 복잡해질 때는 여전히 유용합니다.
- [SwiftUI view refactor](https://github.com/Dimillian/Skills/blob/main/swiftui-view-refactor/SKILL.md)는 파일 크기를 줄이고 레포지토리 전반에서 SwiftUI 코드의 일관성을 높이는 데 도움이 됩니다.
- [SwiftUI patterns](https://github.com/Dimillian/Skills/blob/main/swiftui-ui-patterns/SKILL.md) 스킬을 활용하면 앱이 커져도 예측 가능한 `@Observable` 및 `@Environment` 아키텍처 패턴을 적용할 수 있습니다.

스킬 설치 및 사용 방법에 대한 자세한 내용은 [스킬 문서](/ko-KR/codex/build-skills)를 참고하세요.

## 반복 개선하기

초기 구현이 작동하기 시작했거나 기존 프로젝트에서 시작한다면 UI 또는 동작을 반복해서 개선할 수 있습니다.

이 단계에서는 무엇을 어떻게 변경할지 구체적으로 설명하세요.

프롬프트에 이런 정보를 명시하세요. Codex가 그린필드 레포지토리와 기존 Xcode 프로젝트 중 어디에서 작업하는지, 계속 작동해야 할 iOS 기기 또는 배포 대상이 무엇인지, 어떤 검증 루프를 기대하는지 알려 주세요.

### 예시 프롬프트

예를 들어 기존 앱에 기능을 추가하려면 Codex에 다음과 같은 변경을 요청할 수 있습니다:

## 실용적인 팁

### 기본부터 시작하기

그린필드 작업은 일반 프롬프팅으로 시작하세요. Codex에 스타터 SwiftUI 앱을 스캐폴딩하고 [로컬 환경](/ko-KR/codex/environments/local-environment)의 `Build` 작업에 연결할 수 있는 간단한 빌드 및 실행 스크립트를 작성하도록 요청하세요. 이 첫 단계에서는 스킬이나 MCP 서버가 필요하지 않은 경우가 많습니다.

### 작고 신뢰할 수 있는 검증 루프 사용하기

각 변경 후에는 변경한 계약을 실제로 검증할 수 있는 가장 좁은 범위의 명령을 실행하도록 Codex에 지시하세요. 더 광범위한 빌드는 나중에 실행하세요. 이렇게 하면 모든 수정에 전체 앱 빌드가 필요한 것처럼 가정하지 않으면서도 Codex의 작업 속도를 유지할 수 있습니다.

### 루프를 CLI 중심으로 유지하기

루프는 CLI 중심으로 유지하세요. Apple의 `xcodebuild` 도구를 사용하면 스킴 목록을 확인하고 터미널에서 빌드, 테스트, 아카이브, `build-for-testing`, `test-without-building` 작업을 실행할 수 있습니다. 이를 통해 Codex는 Xcode GUI를 오가지 않고 에이전트 루프 안에서 계속 작업할 수 있습니다.

### XcodeBuildMCP 활용하기

전체 Xcode 프로젝트에서 작업하면서 더 심층적인 자동화가 필요해지면 바로 XcodeBuildMCP를 사용하세요. 스킴, 타깃, 시뮬레이터 제어, 스크린샷, 로그, UI 조작이 중요해져 단순한 셸 명령만으로는 충분하지 않게 되는 시점입니다.

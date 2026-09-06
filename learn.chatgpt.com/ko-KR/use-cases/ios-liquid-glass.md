<!-- source: https://learn.chatgpt.com/ko-KR/use-cases/ios-liquid-glass -->

## iOS 26 기준부터 시작하기

Liquid Glass를 먼저 iOS 26 및 Xcode 26 마이그레이션 프로젝트로 접근하세요. iOS 26 SDK로 앱을 다시 빌드하고 표준 SwiftUI 컨트롤에 기본으로 적용되는 결과를 확인한 다음, 여전히 지나치게 평면적이거나 무겁거나 시스템 UI와 동떨어져 보이는 커스텀 부분만 Codex에 재디자인하도록 요청하세요.

앱이 여전히 이전 iOS 버전을 지원한다면 이 제약 조건을 처음부터 명확히 하세요. [Build iOS Apps 플러그인](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps)에 포함된 SwiftUI Liquid Glass 스킬은 새로운 Liquid Glass 전용 API에 `#available(iOS 26, *)` 조건을 적용하고 이전 기기에서도 가독성을 유지하는 폴백 경로를 제공해야 합니다.

## iOS 플러그인 활용하기

Codex가 SwiftUI UI 변경과 시뮬레이터 기반 검증을 함께 수행하게 하려면 [Build iOS Apps 플러그인](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps)을 사용하세요. Liquid Glass 작업에서는 Codex에 플로우 하나를 점검하고 일부 표면을 마이그레이션하도록 요청한 다음, 범위를 확장하기 전에 iOS 26 시뮬레이터에서 결과를 실행하고 스크린샷을 캡처하는 것이 효과적입니다.

이 플러그인에는 프롬프트에 반영할 만한 간단한 기본 원칙을 담은 SwiftUI Liquid Glass 스킬이 포함되어 있습니다:

- 커스텀 블러 뷰 대신 네이티브 `glassEffect`, `GlassEffectContainer`, Liquid Glass 버튼 스타일, `glassEffectID` 전환을 우선 사용하세요.
- `.glassEffect(...)` 적용은 레이아웃 및 시각적 수정자 뒤에 배치하여 머티리얼이 실제로 원하는 최종 모양에 맞게 적용되도록 하세요.
- 여러 표면이 함께 나타날 때는 관련 Liquid Glass 요소를 `GlassEffectContainer`로 감싸세요.
- `.interactive()` 적용 대상은 실제로 터치에 반응하는 버튼, 칩, 컨트롤로 제한하세요.
- 제각각인 Liquid Glass 스타일을 섞지 말고 해당 기능 전체에서 모서리 모양, 틴트, 간격을 일관되게 유지하세요.
- iOS 26 미만 타깃을 위한 Liquid Glass 미적용 폴백을 유지하세요.

플러그인과 스킬 설치에 관한 자세한 내용은 [플러그인](/ko-KR/codex/plugins) 및 [스킬](/ko-KR/codex/build-skills) 문서를 참고하세요.

## WWDC 세션 시청하기

실제 프로덕션 플로우를 리팩터링하도록 Codex에 요청하기 전에 다음 WWDC25 세션을 참고하면 좋습니다:

- [Liquid Glass 만나보기](https://developer.apple.com/videos/play/wwdc2025/219/)
- [새로운 디자인 시스템 알아보기](https://developer.apple.com/videos/play/wwdc2025/356/)
- [새로운 디자인으로 SwiftUI 앱 빌드하기](https://developer.apple.com/videos/play/wwdc2025/323/)
- [새로운 디자인으로 UIKit 앱 빌드하기](https://developer.apple.com/videos/play/wwdc2025/284/)
- [SwiftUI의 새로운 기능](https://developer.apple.com/videos/play/wwdc2025/256/)

## 마이그레이션 계획을 요청한 다음 일부 구현하기

Liquid Glass 마이그레이션은 Codex가 "Liquid Glass를 어디에 적용해야 하는가?"와 "지금 모든 코드를 작성하라."를 분리해 처리할 때 더 원활합니다. 먼저 간단한 검토를 요청한 다음, 에이전트가 시뮬레이터 검증을 거쳐 독립적으로 완결된 범위 하나를 구현하도록 하세요.

## 실용적인 팁

### 모든 요소에 Liquid Glass를 적용하지 않기

Liquid Glass는 콘텐츠 위에 명확한 컨트롤 레이어를 형성해야 하며 모든 카드를 빛나는 패널로 바꿔서는 안 됩니다. Codex에 시스템 머티리얼과 충돌하는 장식용 배경을 제거하도록 요청하고, 가독성이 가장 중요한 곳은 장식 없는 콘텐츠로 유지하며, 틴트는 의미를 강조하거나 주요 동작을 나타낼 때만 사용하세요.

### 사용량이 많은 플로우 하나부터 시작하기

앱 전체를 한 번에 마이그레이션하기보다 탭 루트, 상세 화면, 시트, 검색 화면, 온보딩 플로우 중 하나를 첫 마이그레이션 대상으로 삼는 편이 좋습니다. 그러면 검토가 쉬워지고 어떤 Liquid Glass 관련 결정을 재사용 가능한 컴포넌트 패턴으로 만들어야 하는지 명확해집니다.

### 폴백 동작을 꼼꼼히 검토하기

배포 타깃이 iOS 26 미만이라면 Codex에 Liquid Glass 버전과 폴백 구현을 함께 보여 달라고 요청하세요. 이 검토 단계에서 의도치 않은 API 가용성 회귀를 발견할 수 있으며, 최신 시뮬레이터에서만 작동하는 마이그레이션 결과가 출시되는 것을 방지할 수 있습니다.

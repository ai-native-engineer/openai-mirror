<!-- source: https://learn.chatgpt.com/ko-KR/use-cases/react-native-expo-apps -->

## Expo Go로 시작하기

모바일 앱 아이디어를 테스트를 완료한 React Native 앱으로 구현하는 데 Codex를 활용하려면 Expo가
좋은 기본 선택입니다. 효율적인 개발 루프는 먼저 `expo start`를 실행하고, 그다음 기기에서 Expo Go로
테스트한 뒤, 앱에 커스텀 네이티브 코드, 스토어 배포 또는 Expo Go에서 실행할 수 없는 기능이
필요할 때만 개발 클라이언트나 EAS 빌드로 전환하는 것입니다.

이렇게 하면 첫 단계에서 네이티브 IDE 설정, 시뮬레이터 설정, 프로비저닝 또는 빌드 구성에
시간을 쓰지 않고 Codex가 앱 워크플로우에 집중할 수 있습니다.

## Expo 플러그인 사용하기

Expo는 Expo Router, 네이티브 UI, 폼, 내비게이션, 애니메이션, 데이터 가져오기, NativeWind 설정,
Expo 모듈, 개발 클라이언트, 배포, 업그레이드, Codex Run 액션 연결에 대해 Expo 방식에 맞는
지침을 Codex에 제공하는 [Expo 플러그인](https://docs.expo.dev/skills/)을 공개했습니다.

Codex가 새로운 Expo 화면을 빌드하거나 패키지를 추가하고 API
호출을 연결할 때, 개발 클라이언트를 준비하거나 TestFlight, App
Store, Play Store 또는 EAS Hosting에 앱을 배포할 준비를 할 때 사용하세요.

작업에 최신 Expo 문서 조회, 호환되는 패키지 설치, EAS 빌드 및 워크플로우 작업,
스크린샷, 시뮬레이터 상호작용, React Native DevTools 또는 TestFlight 데이터가
필요하다면 [Expo MCP 서버](https://docs.expo.dev/eas/ai/mcp/)를 선택적으로
추가하세요.

## 반복 개발 과정

1. Codex에 레포지토리를 검사해 새 Expo 앱인지 기존 Expo 프로젝트인지
확인하도록 요청하세요.
2. Expo Router와 Expo Go로 시작하세요. Expo 패키지를 추가할 때는 `npx expo install` 명령을
   사용하세요.
3. 네이티브 앱처럼 자연스러운 내비게이션과 로딩 상태, 빈 상태, 오류 상태를 모두 갖춘
완결된 워크플로우 하나를 빌드하도록 Codex에 요청하세요.
4. 기기의 Expo Go나 시뮬레이터처럼 가장 빠르게 사용할 수 있는 방법으로
검증한 다음, 필요한 경우에만 개발 클라이언트나 EAS로 전환하세요.

## 추천 후속 프롬프트

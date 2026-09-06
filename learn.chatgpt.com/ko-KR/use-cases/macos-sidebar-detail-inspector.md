<!-- source: https://learn.chatgpt.com/ko-KR/use-cases/macos-sidebar-detail-inspector -->

## Mac 씬 모델부터 시작하기

이 사용 사례에서는 터치 중심 스택을 데스크톱에 늘려 놓은 듯한 모습이 아니라, 데스크톱에 맞게 설계된 Mac 앱 셸로 앱 아이디어를 구현합니다. Codex에 먼저 씬 모델을 선택하도록 요청한 다음, 안정적으로 유지되는 사이드바 선택 상태, 세부 정보 영역, 보조 컨트롤이나 메타데이터를 위한 인스펙터를 중심으로 메인 창을 설계하게 하세요.

![사이드바에서 항목이 선택되고 세부 정보 패널에 콘텐츠가 표시된 Mac 네이티브 사이드바·세부 정보 앱 셸](/images/codex/use-cases/macos-sidebar-detail-inspector.png)

Codex가 이 데스크톱 구조를 적용하고 빌드/실행 루프를 셸 중심으로 유지하도록 하려면 [Build macOS Apps 플러그인](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps)을 사용하세요. 이 플러그인의 macOS SwiftUI 패턴 스킬은 씬 설계, 사이드바, 인스펙터, 명령, 설정뿐 아니라 SwiftUI만으로 특정 Mac 동작을 온전히 구현하기 어려울 때 필요한 소규모 AppKit 브리지에도 적합합니다.

## 사이드바, 세부 정보 패널, 인스펙터 만들기

탐색을 계속 표시하고 선택 항목을 안정적으로 유지해야 하는 기능이라면 `NavigationSplitView`를 우선 사용하세요. 사이드바 행은 네이티브하고 가볍게 유지하고, 사이드바에는 시스템 배경을 사용하며, 맞춤형 카드나 상세한 메타데이터는 세부 정보 패널이나 인스펙터에 배치하세요.

```swift
struct LibraryRootView: View {
  @SceneStorage("LibraryRootView.selection") private var selection: Item.ID?
  @SceneStorage("LibraryRootView.showInspector") private var showInspector = true

  var body: some View {
    NavigationSplitView {
      List(selection: $selection) {
        ForEach(items) { item in
          Label(item.title, systemImage: item.systemImage)
            .tag(item.id)
        }
      }
      .listStyle(.sidebar)
      .navigationTitle("Library")
    } detail: {
      ItemDetailView(selection: selection)
        .inspector(isPresented: $showInspector) {
          ItemInspectorView(selection: selection)
        }
    }
  }
}

앱에 특수한 분할 영역 크기 조절, 저수준 창 조정 또는 맞춤형 리스폰더 체인 동작이 필요하다면 Codex에 SwiftUI 셸을 그대로 유지하고 그 한 가지 공백을 메우는 데 필요한 최소한의 AppKit 브리지만 추가하도록 요청하세요.

## 데스크톱 계층에 명령, 툴바, 단축키 배치하기

Mac 사용자는 메뉴 막대, 툴바, 키보드 단축키에서 중요한 작업을 쉽게 찾을 수 있어야 합니다. 데스크톱 사용자가 제스처로만 사용할 수 있는 컨트롤을 찾아 헤매지 않도록 씬 수준의 `commands`, 상황별 메뉴 항목, 툴바 버튼을 동일한 앱 작업에 연결해 달라고 Codex에 요청하세요.

```swift
@main
struct LibraryApp: App {
  var body: some Scene {
    WindowGroup {
      LibraryRootView()
    }
    .commands {
      CommandMenu("Library") {
        Button("New Item") {
          // Create a new item.
        }
        .keyboardShortcut("n")

        Button("Toggle Inspector") {
          // Route this command to the focused window or selected item state.
        }
        .keyboardShortcut("i", modifiers: [.command, .option])
      }
    }

    Settings {
      LibrarySettingsView()
    }
  }
}

명령이 현재 세부 정보 항목에 적용되어야 한다면 `FocusedValue`, 씬 상태 또는 명시적 선택 상태를 사용하세요. 단축키가 여러 곳에 등록될 수 있다면 앱에 명확한 명령 경로가 하나만 남도록 소유권을 통합해 달라고 Codex에 요청하세요.

## `Settings`에서 환경설정 관리하기

앱 환경설정에는 전용 `Settings` 씬을 사용하고, `@AppStorage`로 지속적으로 유지해야 하는 사용자 선택 사항을 저장하세요. 이는 메인 콘텐츠 창 안에 설정 화면을 푸시하는 방식보다 일반적으로 Mac 앱에 더 적합합니다.

```swift
struct LibrarySettingsView: View {
  @AppStorage("showItemMetadata") private var showItemMetadata = true

  var body: some View {
    TabView {
      Form {
        Toggle("Show Item Metadata", isOn: $showItemMetadata)
      }
      .tabItem { Label("General", systemImage: "gearshape") }
    }
    .frame(width: 460, height: 260)
    .scenePadding()
  }
}

## 앱 개념을 프롬프트로 제시한 다음 셸 검증하기

이 페이지는 프롬프트에 앱 개념, 주요 콘텐츠 객체, 핵심 작업을 명시한 다음 Codex에 해당 워크플로우를 중심으로 데스크톱 셸부터 만들도록 요청할 때 가장 효과적입니다. 에이전트가 간단한 빌드/실행 검사를 수행하고 씬 구조, 명령 연결, 상태 소유권, AppKit 브리지가 필요했던 부분을 요약하게 하세요.

## 실용적인 팁

### 사이드바를 네이티브 형태로 유지하기

각 사이드바 행에는 아이콘 하나, 제목 한 줄, 짧은 보조 정보 최대 한 줄만 사용하세요. 사이드바 목록을 쉽게 훑어볼 수 있도록 더 풍부한 카드, 카운터, 메타데이터는 세부 정보 패널이나 인스펙터로 옮기세요.

### 메인 스택에 설정을 숨기지 않기

사용자 환경설정이 앱 전체에 영향을 준다면 또 다른 푸시형 설정 화면을 만들지 말고, Codex에 해당 컨트롤을 `@AppStorage`로 저장해 `Settings` 씬에 배치하고 앱 메뉴에서 진입점을 제공하도록 요청하세요.

### AppKit은 제한적인 데스크톱 기능 보완에만 사용하기

기능에서 열기/저장 패널, 퍼스트 리스폰더 제어 또는 맞춤형 `NSView` 사용이 필요하다면 전체 창을 AppKit으로 다시 작성하지 말고, SwiftUI가 소유하는 상태 모델 주변의 작은 보완 계층으로만 AppKit을 사용하세요.

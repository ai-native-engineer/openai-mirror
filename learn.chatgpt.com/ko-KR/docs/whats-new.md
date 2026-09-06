<!-- source: https://learn.chatgpt.com/ko-KR/docs/whats-new -->

이 주간 요약에서는 업무 방식을 바꿀 수 있는 ChatGPT와 Codex 기능을
예시 및 자세한 안내 링크와 함께 소개합니다. 버전별 업데이트와 버그 수정,
작은 개선 사항까지 모두 보려면 [Codex 변경 로그](/codex/changelog)를 확인하세요.

## 2026년 8월 31일~9월 4일

### GPT-6 Astra로 까다로운 작업 수행하기

[GPT-6 Astra](/ko-KR/codex/models#gpt-6-astra)는 고급 추론, 컴퓨터 사용,
향상된 판단력을 결합해 Codex와 ChatGPT Work에서 코드, 앱, 연구 전반의
복잡한 작업을 수행합니다. 워크플로우를 실행하고 결과를 확인한 뒤,
템플릿과 작업에 맞는 문서, 스프레드시트 또는
프레젠테이션을 만들어 보세요.

계정에서 Astra를 사용할 수 있게 되면 모델 선택기에서 선택하세요.
대규모 작업을 시작하기 전에 [사용량 및 요금](/ko-KR/codex/pricing)을 확인하세요.
Enterprise에서 이용하려면 출시 대상에 포함되어야 하며,
관리자가 기능을 활성화해야 합니다.

## 2026년 8월 24일~28일

### 더 다양한 웹사이트에서 작업하기

- **사용 중인 브라우저로 작업:** ChatGPT 데스크톱 앱에서 Chrome뿐 아니라 [Edge, Brave, Opera 또는 Vivaldi](/ko-KR/codex/chrome-extension)에서도
  작업할 수 있습니다. 열려 있는 탭을 ChatGPT Work 또는 Codex 채팅으로 가져와
  이미 로그인된 웹사이트에서 작업하세요.
  Opera는 브라우저 제어를 지원하지만 사이드 채팅은 제공하지 않습니다.

- **웹사이트 도구 사용:** [사이트 도구 (WebMCP)](/ko-KR/codex/webmcp)를 통해 ChatGPT Work와
  Codex가 데스크톱 앱의 내장 브라우저에서 웹사이트가 제공하는 동작을
  실행할 수 있습니다. 예를 들어 문서 편집기는 섹션을 찾거나
  댓글을 추가하는 도구를 제공할 수 있습니다. 데스크톱 앱을 업데이트하고
  GPT-5.6 Sol 또는 GPT-5.6 Terra를 사용하세요. 사이트 도구는 GPT-5.6 Luna나
  Enterprise 또는 Edu 워크스페이스에서는 사용할 수 없습니다.

- **클라우드 브라우저에서 로그인:** 지원되는 플랜에서는 웹, iOS 또는 Android의
  ChatGPT Work에서 웹사이트 계정이 필요한 작업을 계속할 수 있습니다.
  [로그인 요청](/ko-KR/codex/browser?surface=web#web-sign-in-to-a-website)에 따라
  채팅이 아닌 로그인 플로우에서 정보를 입력하세요. 이 과정에서
  로컬 브라우저 프로필이 연결되지는 않습니다. 웹사이트 로그인은
  Enterprise 또는 Edu 워크스페이스에서는 사용할 수 없습니다.

사용 가능 여부는 순차 출시 현황과 워크스페이스 설정에 따라 달라집니다.

[8월 25일 브라우저 릴리스
노트를 확인하세요](/codex/changelog#codex-2026-08-25-browser).

### 앱 이벤트로 예약 작업 실행하기

[예약 작업](/ko-KR/codex/automations?surface=web#web-trigger-tasks-from-app-events)은 이제 Gmail, Slack 또는 GitHub에서
지원되는 이벤트가 발생하면 시작할 수 있습니다. 이벤트 트리거를 사용하면
일정한 간격으로 폴링하지 않고도 새 이메일을 분류하거나 채널 활동을 요약하고
Pull Request 피드백에 대응할 수 있습니다.

지원되는 플랜에서는 웹과 모바일의 ChatGPT에서 이벤트로 실행되는 작업을 사용할 수 있습니다.
먼저 해당 앱을 연결하고 요청된 액세스 권한을 승인하세요.
관리형 워크스페이스에서는 관리자가 액세스를 제어할 수 있습니다.

<PromptComponent
  prompt={`<owner>/<repository>에서 내가 만든 Pull Request에 새 검토 피드백이 달리면, 피드백을 요약하고 수정 계획을 세워 줘.`}
/>

[8월 25일 릴리스
노트를 확인하세요](/codex/changelog#codex-2026-08-25-event-triggers).

## 2026년 8월 17일~21일

### 더 다양한 앱과 콘텐츠로 작업하기

- **Apple Messages:** [Mac의 Messages에서 대화를 찾고 메시지를 요약하며 답장을 작성해 전송하세요](/ko-KR/codex/plugins?surface=app#app-use-apple-messages-from-codex). 이 플러그인은 macOS용 ChatGPT 데스크톱 앱의 모든 플랜에서 사용할 수 있습니다. 일반 ChatGPT 채팅이 아닌 ChatGPT Work와 Codex에서 사용하세요. 기본적으로 ChatGPT는 사용자가 메시지와 수신자를 승인한 후에만 메시지를 전송합니다.

- **사이트 공동 편집:** 지원되는 환경에서는 [워크스페이스의 활성 멤버를 편집자로 초대하세요](/ko-KR/codex/sites#collaborate-on-a-site). 소유자가 사이트를 처음 게시한 후 편집자는 사이트를 개선하고 업데이트를 게시할 수 있습니다. 초대된 편집자는 사이트의 운영 중인 데이터베이스에 저장된 데이터를 읽을 수 있으며, 소유자는 공유와 설정을 계속 관리합니다.

- **사이트 URL 변경:** 지원되는 환경에서는 사이트를 다시 배포하지 않고 [기존 사이트의 ChatGPT 호스팅 주소를 새로 선택할 수 있습니다](/ko-KR/codex/sites#change-a-site-url). 이전 주소는 새 주소로 리디렉션됩니다.

- **유럽에서 컴퓨터 사용 기록 지원:** EEA, 스위스, 영국에서 [컴퓨터 사용 기록](/ko-KR/codex/customization/computer-history)을 사용할 수 있습니다. macOS의 ChatGPT Pro, Business, Enterprise 사용자에게는 여전히 기본적으로 꺼져 있습니다. Business 및 Enterprise 관리자가 먼저 액세스를 활성화해야 합니다.

- **스레드 스냅샷 공유:** macOS용 ChatGPT 데스크톱 앱에서 [로컬 Codex 스레드의 읽기 전용 스냅샷을 공유하세요](/ko-KR/codex/use-chatgpt#share-a-read-only-snapshot-of-a-codex-thread). 개인 계정의 링크는 링크가 있는 누구나 볼 수 있으며, 워크스페이스 계정의 링크는 해당 링크가 생성된 워크스페이스에서만 볼 수 있습니다. Codex는 알려진 비밀 정보 패턴에 해당하는 내용을 가리지만, 민감한 내용이 남아 있을 수 있으므로 공유하기 전에 스냅샷을 검토하세요.

- **고정 스레드 통합:** [고정한 채팅](/ko-KR/codex/projects?surface=app#app-organize-projects-and-chats)을 데스크톱과 iOS 간에 동기화하세요.

[8월 20일 릴리스 노트를 확인하세요](/codex/changelog#codex-2026-08-20-app).

### Codex 클라우드에서 GitLab 프로젝트로 작업하기

[GitLab 지원](/ko-KR/codex/third-party/gitlab)은 모든 ChatGPT 플랜에서
베타로 제공됩니다. 프로젝트를 연결하고 클라우드 환경을 만드세요. 이슈나 병합 요청에서
`@codex`로 작업을 시작하고, 병합 요청에 대한
일회성 검토 또는 자동 검토를 요청하세요.

이 연동 기능은 Codex 클라우드에서 실행되며, 관리형 워크스페이스 관리자가
비활성화할 수 있습니다. GitLab에서 시작되는 활동에는 해당 웹훅을 설정할 권한이 필요합니다.
GitLab Self-Managed 및 GitLab Dedicated에 연결하려면 워크스페이스 관리자가 설정해야 하며,
웹훅 활동에는 GitLab 19.0 이상이 필요합니다.

[8월 19일 GitLab 릴리스
노트를 확인하세요](/codex/changelog#codex-2026-08-19-gitlab).

### 공개 플러그인 메타데이터를 내보내 검토하기

지원 대상인 ChatGPT Enterprise 워크스페이스의 소유자와 관리자는
워크스페이스에 표시되는 공개 플러그인 목록을 CSV 파일로 다운로드할 수 있습니다.
[관리자 \> 플러그인](https://chatgpt.com/admin/plugins)에서 **공개** 항목을 선택한 다음,
다운로드 아이콘(**CSV 내보내기**)을 선택하세요.

내보낸 파일에는 플러그인, 앱, 채팅 스킬의 이름과 설명을 비롯해 개발자,
버전, UTC 기준 추가 날짜, OpenAI 검증 메타데이터가 포함됩니다.
최대 48시간 전의 공개 카탈로그 스냅샷을 사용하며, 해당 워크스페이스용으로
생성된 플러그인은 제외됩니다. FedRAMP 워크스페이스에서는
내보내기 기능을 사용할 수 없습니다.

[8월 17일 관리자 내보내기 기능 릴리스
노트를 확인하세요](/codex/changelog#codex-2026-08-17-admin-csv).

## 2026년 8월 10일~14일

### 컴퓨터 사용 기록으로 이전 작업 찾기

[컴퓨터 사용 기록](/ko-KR/codex/customization/computer-history)은 앱과 웹사이트에서의 활동을
검색 가능한 타임라인과 ChatGPT 및 Codex가 사용할 수 있는
메모리로 만듭니다. 이 컨텍스트를 공유하고 싶은 경우에만 기능을 켜세요.
수집 대상 앱과 웹사이트를 선택할 수 있으며, 언제든 수집을 일시 중지하거나
기록을 검토하고 삭제할 수 있습니다.

컴퓨터 사용 기록은 macOS용 ChatGPT 데스크톱 앱에서 ChatGPT Pro, Business,
Enterprise 고객에게 제공됩니다. Business 및 Enterprise 관리자가 먼저
액세스를 활성화해야 합니다. 초기 제공 지역에는
유럽연합, 스위스, 영국이 포함되지 않습니다.

### Linux에서 ChatGPT 데스크톱 앱 사용하기

[Linux용 ChatGPT 데스크톱 앱](/ko-KR/codex/linux/linux-app)이 이제 프리뷰로 제공됩니다.
지원되는 Ubuntu 또는 Debian 배포판에는 `.deb` 패키지를,
Fedora에는 `.rpm` 패키지를 설치하세요. 패키지는
x64와 ARM64 프로세서용으로 모두 제공됩니다.

ChatGPT 계정으로 로그인해 프로젝트, 로컬 파일, Codex를 사용하세요.
컴퓨터 사용을 포함한 일부 기능은 Linux 프리뷰에서
아직 사용할 수 없습니다.

### 기존 에이전트 설정과 작업 가져오기

ChatGPT 데스크톱 앱으로 [지침, 설정, 스킬, 플러그인, 프로젝트,
최근 작업을 가져오세요](/codex/import). **Claude Code**, <strong>Claude Cowork</strong> 또는
**Cursor에서** 가져올 수 있습니다. 가져온 작업을 계속 동기화하려면
**설정 \> 가져오기** 메뉴에서 자동 업데이트를 켜세요.

Codex CLI에서 `/import`를 사용하면 Claude Code 또는 Cursor의
지원되는 설정과 최근 채팅을 로컬 세션으로 가져올 수 있습니다.

[8월 11일 데스크톱 및 CLI 릴리스
노트를 확인하세요](/codex/changelog#codex-2026-08-11-app).

### 보안 방어 작업에 맞는 접근 권한 선택하기

Daybreak는 이제 승인된 보안 방어 담당자에게 두 가지 등급을 제공합니다. **Daybreak Blue는** 
보안 코드 검토, 사고 대응,
패치 검증 등 일반적인 방어 작업을 지원합니다. **Daybreak Red는** 별도의 승인이 필요하며,
허가된 보안 평가에 특화해 학습된 모델에 대한 접근 권한을 제공합니다.

이용하려면 [Trusted Access for
Cyber](/ko-KR/codex/cyber-safety#trusted-access-for-cyber)가 필요하며, 접근 권한은
승인된 신원, 워크스페이스 또는 조직, 모델, 제품 사용 환경에만 적용됩니다.

[8월 10일 Daybreak
발표를 확인하세요](/codex/changelog#codex-2026-08-10-daybreak).

## 2026년 8월 3~7일

### ChatGPT 음성 대화로 파일과 프로젝트에 관해 이야기하기

이제 [ChatGPT 음성 대화](/ko-KR/codex/features/voice)에서 업로드한 파일과
[ChatGPT 프로젝트](/ko-KR/codex/projects)를 지원합니다. 음성 대화 중 문서에 관해
질문하거나, 프로젝트의 최근 채팅, 자료,
지침을 활용해 프로젝트를 이어서 진행하세요.

### 교육 전용 플러그인으로 배우고 가르치기

세 가지 새로운 [플러그인](/ko-KR/codex/plugins)으로 ChatGPT Work와 Codex에서
교육 현장에 특화된 워크플로우를 사용할 수 있습니다. **College Student는** 학습 가이드, 연습 퀴즈,
플래시카드, 상호작용형 설명을 만듭니다. **College Educator는** 
강의 계획, 교재, 평가 자료 작성을 돕습니다. **K–12 Educator는** 
수업 계획 수립, 교실에서 사용할 자료 준비, 다양한 학습자에 맞춘
자료 작성을 지원합니다.

이 플러그인들은 ChatGPT Edu와 학군 단위로 도입한 ChatGPT for Teachers에서
사용할 수 있습니다. 사용 가능한 도구와 권한은 학교에서 관리합니다.
[교육용 플러그인
발표](https://openai.com/index/learn-teach-chatgpt-work-codex/)를 확인하세요.

### 저장된 파일 재사용 및 이전 작업 더 빠르게 찾기

웹에서는 라이브러리에 저장된 파일을 다시 업로드하지 않고도 대화에 추가하고,
라이브러리 안에서 검색하며, 제목, 링크, 목록을 유지한 채 서식 있는 텍스트를
붙여넣을 수 있습니다. 웹, iOS, Android에서는 폴더와 대화 제목도
검색할 수 있습니다.

이제 Enterprise와 Edu를 포함한 모든 ChatGPT 플랜에서
10,000자를 초과하는 텍스트를 붙여넣으면 첨부 파일로 변환됩니다. 내용을 메시지 안으로 다시 옮기려면
 **텍스트 필드에 표시를** 선택하세요.

[ChatGPT 릴리스
노트](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)를 확인하세요.

### 남은 ChatGPT Work 사용량 확인하기

개인 플랜 및 ChatGPT Business의 이용 자격을 갖춘 사용자는
웹 사이드바에서 남은 ChatGPT Work 사용량을 바로 확인할 수 있습니다. 이용 가능한 크레딧 옵션은
계정 및 워크스페이스 권한에 따라 다릅니다. ChatGPT Work와 Codex는 계속
동일한 [사용 한도와 크레딧](/ko-KR/codex/pricing)을 공유합니다.

### ChatGPT에서 GPT-5.6의 응답 방식 선택하기

ChatGPT Plus 및 Pro 사용자는 새 슬라이더로 GPT-5.6 Sol이 응답에 들이는
추론량을 조절할 수 있습니다. 업데이트된 모델은 더 신뢰할 수 있는 사실 정보와
핵심에 집중한 답변도 제공합니다. Free 및 Go 플랜에서는 GPT-5.6 Luna가
기본 ChatGPT 모델이 됩니다.

이 변경 사항은 ChatGPT 대화에 적용되며,
ChatGPT Work나 Codex에서의 모델 동작은 바뀌지 않습니다. [ChatGPT 릴리스
노트](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)를 확인하세요.

### Codex CLI 0.147.0에서 작업 정리 및 에이전트 전환하기

[Codex CLI 0.147.0](https://github.com/openai/codex/releases/tag/rust-v0.147.0)에는
순서를 직접 정할 수 있고 저장 상태가 유지되는 채팅 섹션과 이식 가능한 에이전트 플러그인이 추가되었습니다.
로컬, 개인, 워크스페이스, 원격 플러그인 카탈로그 전반을 검색하거나,
동기화된 대화를 중복 생성하지 않고
[Cursor와 Claude Code의 설정을 가져오세요](/ko-KR/codex/import).

`--approve-for-me` 옵션으로 요건을 충족하는 요청에 대한 [승인 요청 자동
검토](/ko-KR/codex/sandboxing/auto-review)를 활성화하세요. 이 기능은
파일 시스템이나 네트워크 권한을 확대하지 않습니다. Amazon Bedrock 세션에도 캐시된
웹 검색과 원격 대화 컨텍스트 압축 기능이 추가되었습니다.

### 심층 보안 스캔 추적 및 재개하기

호스팅형 Codex Security 플러그인의 `0.1.16`~`0.1.18` 버전에는 실시간 스캔
진행 상황, 측정된 토큰 사용량, 재개 가능한 심층 스캔, 설정 가능한
탐색 한도가 추가되었습니다. 최신 릴리스는 레포지토리 스캔과 해당 스캔에서 작업을 위임받은 워커에 대한
Amazon Bedrock 인증도 지원합니다.

[Codex Security 워크벤치](/ko-KR/codex/security/plugin/workbench)에서
스캔 진행 상황과 보안 이슈를 검토하세요. 더 철저한 평가가 필요하면 [심층 스캔을
설정하세요](/ko-KR/codex/security/plugin/deep-scans).
[플러그인 변경 로그](/ko-KR/codex/security/plugin/changelog)에서
설치된 버전이 지원하는 기능을 확인하세요.

### GitHub Pull Request의 보안 위험 검토하기

[Codex Security 검토](/ko-KR/codex/security/security-review)는 Pull Request의
변경 사항을 레포지토리 컨텍스트, 위협 모델, 보안 지침과 함께 분석합니다.
Pull Request가 생성되거나 새 커밋이 추가될 때 자동으로 검토하도록
설정하거나, `@codex security review`로 직접 검토를 요청하세요.

이 기능은 이용 자격을 갖춘 ChatGPT Enterprise,
Business, Edu 및 Pro 고객에게 연구 프리뷰로 제공됩니다. Plus에서는 사용할 수 없으며,
사용 한도가 적용될 수 있습니다.

## 2026년 7월 27~31일

### 더 낮은 요금으로 GPT-5.6 Terra와 Luna 사용하기

GPT-5.6 Terra의 요금이 20%, GPT-5.6 Luna의 요금이 80% 인하되었습니다. 입력,
캐시된 입력, 출력 요금이 각각 같은 비율로 인하되었습니다. 업데이트된
[사용 한도와 요금](/ko-KR/codex/pricing) 덕분에 Terra는 일상적인
작업에 더욱 적합해졌고, Luna는 범위가 명확한 코딩과 대량 작업에 특히 유용해졌습니다.

### 브라우저와 열려 있는 탭에서 유용한 컨텍스트 찾기

ChatGPT 데스크톱 앱의 [내장 브라우저](/ko-KR/codex/browser)에서는
방문 기록에서 페이지를 찾거나 주소창에서 바로
Google 검색을 할 수 있습니다. 작업에 이전 컨텍스트가 필요하면
ChatGPT도 방문 기록을 검색할 수 있습니다.

[Chrome 확장 프로그램](/ko-KR/codex/chrome-extension)을 사용하면 열린 탭을 언급하거나,
페이지에서 선택한 텍스트를 사이드 채팅으로 가져오거나, YouTube 동영상에 관해 질문하거나,
페이지의 컨텍스트 메뉴에서 **ChatGPT에 질문하기를** 선택할 수 있습니다.
ChatGPT가 방문 기록 정보를 작업에 포함하기 전에
방문 기록 사용 요청을 검토하고 승인하세요.

### 여러 레포지토리의 변경 사항 검토하기

[로컬 프로젝트에 폴더가
여러 개 있으면](/ko-KR/codex/projects#use-local-projects-for-folders-and-codebases) 데스크톱 앱에
모든 레포지토리와 각 레포지토리에서 변경된 줄이 표시됩니다.
**검토를** 선택하면 개별 검토 화면을 오갈 필요 없이
여러 레포지토리의 diff를 함께 확인할 수 있습니다.

### 대화에서 생성된 이미지 다듬기

생성된 이미지를 확대 뷰어에서 연 다음,
**집중 보기와** **캔버스 보기** 사이를 전환해 보세요. 채팅을 벗어나지 않고 여러 이미지에 댓글을 달고,
보관할 버전을 선택한 다음, 특정 부분의 수정을 요청하세요.
[이미지 생성](/ko-KR/codex/image-generation)에 대해 자세히 알아보세요.

### 확인이 필요한 채팅 찾기

데스크톱 앱의 새로운 **활동 보기에는** 최근에 참여한 채팅과
확인이 필요한 작업이 한곳에 모입니다. 사이드바의 종 아이콘을
선택해 열어 보세요.

[7월 30일 데스크톱 릴리스
노트를 확인하세요](/codex/changelog#codex-2026-07-30-app).

### ChatGPT로 로그인해 파트너 도구 연결하기

**ChatGPT로 로그인** 기능이 Airtable, GitLab, HubSpot, Notion, Supabase,
Vercel을 시작으로 지원되는 플러그인과 파트너 사이트에
베타로 순차 제공되고 있습니다. 더 간단한 절차로 파트너 계정을 만들거나 연결한 다음,
ChatGPT 또는 Codex에서 해당 서비스로 작업을 시작하세요.

파트너에게는 이름, 이메일 주소, 프로필 사진(있는 경우)만
전달됩니다. 각 플러그인이 요청하는 접근 권한은 별도로 검토하고
승인해야 합니다. [7월 29일 로그인 기능
발표](/codex/changelog#codex-2026-07-29)를 확인하세요.

### 학술 연구 전용 워크스페이스에서 협업하기

[ChatGPT for Academic Researchers](https://openai.com/index/chatgpt-for-academic-researchers/)는
자격 요건을 충족하는 교수진과 박사후연구원에게 전용 ChatGPT 워크스페이스를
12개월간 무료로 제공합니다. 승인된 팀은 같은 기관 소속으로 인증을 마친 연구자
최대 5명으로 구성할 수 있으며, 비즈니스 데이터 보호와 ChatGPT Pro 수준의
사용 한도가 적용됩니다. 참여자는 ChatGPT, ChatGPT Work, Codex에서 GPT-5.6을
연구 및 코딩 워크플로우에 사용할 수 있습니다.

이 프로그램은 ChatGPT 이용 권한을 제공하며, OpenAI API 크레딧은 포함하지 않습니다. 참여하려면
[소속 기관 인증과 요건을 충족하는 연구
논문](https://help.openai.com/en/articles/20001406)이 필요합니다.

### iOS에서 Codex 작업을 더 안정적으로 이어가기

iOS용 ChatGPT 1.2026.202에서는 앱으로 돌아오거나 Face ID로 기기 잠금을 해제할 때
작업에 더 안정적으로 다시 연결됩니다. 음성 대화에는 사용자가 선택한 ChatGPT 음성이 사용되며,
사용 한도 경고도 표시됩니다. 이제 Composer에서도 데스크톱 앱과 동일하게
설치된 플러그인과 해당 스킬을 제안합니다.

이번 릴리스에서는 목표 일시 중지 및 재개 기능, 인라인 표와
시각적 테마, 워크스페이스의 대규모 diff, 선택한 텍스트 참조, 모델
복원도 개선되었습니다. [7월 27일 iOS 릴리스
노트](/codex/changelog#codex-2026-07-27-mobile)를 확인하세요.

### 보안 스캔 비교 및 보안 이슈 관리하기

호스팅형 Codex Security 플러그인 릴리스 `0.1.14`와 `0.1.15`에는 스캔 비교,
오탐 피드백, 적용 범위가 지정된 `SECURITY.md` 정책이 추가되었으며,
레포지토리 및 보안 이슈 기록도 더 명확해졌습니다. Linear 또는 GitHub 이슈에서 추적할 보안 이슈를
선택할 수 있으며, 사용자가 승인하기 전에 Codex가 제안된 작업을 검토합니다.

데스크톱 앱의 기존 [Codex Security
워크벤치](/ko-KR/codex/security/plugin/workbench)에서 저장된 스캔, 보안 이슈,
레포지토리 기록 및 해결 조치를 검토하세요. 호스팅형 플러그인
카탈로그에서는 `0.1.15` 버전을, 공개 CLI 플러그인 마켓플레이스에서는
`0.1.11` 버전을 제공합니다. 새 기능을 활용하기 전에 [Codex Security 플러그인
변경 로그](/ko-KR/codex/security/plugin/changelog)를 확인하세요.

### 터미널, CI 또는 TypeScript에서 보안 스캔 실행하기

공개된 `@openai/codex-security` CLI와 TypeScript SDK가
버전 `0.1.5`로 업데이트되었으며, 릴리스 번호는 Codex Security 플러그인과 별도로 관리됩니다.
이 패키지로 [CLI에서 스캔을 실행](/ko-KR/codex/security/cli)하고, Pull Request의
변경 사항 검토와 SARIF 결과 업로드를 [CI](/ko-KR/codex/security/cli/ci)에서 수행할 수 있습니다. 또한
GitHub 레포지토리나 고정된 CSV 인벤토리를 대상으로 재개 가능한 [일괄 스캔](/ko-KR/codex/security/cli/bulk-scans)을
실행할 수 있습니다.

[Codex Security TypeScript SDK](/ko-KR/codex/security/sdk)를 사용하면 자체 도구에
스캔, 진행 상황 보고, 비용 제어, 취소 기능도
구현할 수 있습니다. 패키지는 공개되어 있지만, 스캔을 실행하려면 여전히 Codex Security
접근 권한이 필요합니다. 레포지토리 전체를 스캔하는 일부 작업에는 Trusted Access for Cyber도 필요합니다.

### Codex CLI 0.146.0에서 세션 정리 및 기능 확장하기

[Codex CLI 0.146.0](https://github.com/openai/codex/releases/tag/rust-v0.146.0)에서는
`/new release prep` 또는 `/clear bug bash`로 새 채팅의 이름을 지정하고, 중요한 스레드를
고정하며, 별도 대화를 닫지 않은 채 오갈 수 있습니다.
임시 대화 포크, 호환되는 사용자 지정 모델 제공자용 독립형 웹 검색,
실행기가 제공하는 스킬도 추가되었습니다. 또한 에이전트 플러그인 매니페스트,
워크스페이스 플러그인 게시, 다른 플러그인 마켓플레이스도 지원합니다.

사용자 지정 클라이언트에서는 [App Server](/ko-KR/codex/app-server)로 고정된 스레드를
필터링하고, 메모리 내 포크를 만들고, 설치된 커넥터의 상태를 확인하며,
커넥터 메타데이터를 읽을 수 있습니다. 실험적 WebSocket 지원을 통해 app-server를
원격 Code Mode 호스트에 연결할 수도 있습니다. 원격 연결을 노출하기 전에
[app-server 보안 요구 사항](/ko-KR/codex/app-server#connect-the-cli-terminal-ui)을
검토하세요. 이번 릴리스에서는 프록시 지원,
MCP 재연결, 터미널 응답성, Windows 샌드박스 안정성도 개선되었습니다.

### 호스팅형 Codex 작업에 GPT-5.6 Sol 사용하기

[GPT-5.6 Sol](/ko-KR/codex/models#recommended-models)이 이제 자격 요건을 충족하는 고객을 대상으로 Codex 클라우드의 코드
검토와 품질 보증에 사용됩니다. Sol은 복잡한 코딩, 연구, 컴퓨터 사용, 보안 작업을 위한
GPT-5.6 플래그십 모델입니다.
Codex 클라우드는 모델을 자동으로 선택하며, 지원되는 로컬 및 웹 환경에서는
Terra와 Luna를 계속 사용할 수 있습니다.

### GPT-5.4 모델 지원 종료에 대비하기

ChatGPT로 로그인해 Codex를 사용하는 경우, 8월 31일에 GPT-5.4와 GPT-5.4 mini 지원이
종료됩니다. 워크스페이스 기본값, 저장된 모델 설정, 관리형 구성,
사용자 지정 에이전트, 예약 작업에서 `gpt-5.4`를 `gpt-5.6-terra`로,
`gpt-5.4-mini`를 `gpt-5.6-luna`로 바꾸세요.

OpenAI API와 API 키로 인증된 Codex 세션은
영향을 받지 않습니다. 지원 종료 전에 [사용 중단 예정(deprecated)인 Codex 모델](/ko-KR/codex/models#deprecated-codex-models)과
[워크스페이스의 모델
사용 가능 여부](/ko-KR/codex/enterprise/workspace-model-availability)를
확인하세요.

## 2026년 7월 20–24일

### ChatGPT 음성 대화로 작업 논의하기

GPT-Live 기반의 [ChatGPT 음성 대화](/ko-KR/codex/features/voice)를 사용하면
ChatGPT 데스크톱 앱의 채팅, Work, Codex에서 작업을 말로 논의하고
조율할 수 있습니다. 음성 모드에서 새 채팅이나 작업을 시작한 다음, ChatGPT에 다른 스레드의 작업을
시작하거나 확인하거나 방향을 조정해 달라고 요청하세요.

macOS에서 **화면 컨텍스트** 기능이 켜져 있을 때 “이것 좀 봐 줘”라고 말하면
맨 앞에 있는 창의 [앱샷](/ko-KR/codex/appshots)을 공유할 수 있습니다.

음성 기능은 Plus, Pro, Business, Edu, Enterprise 플랜에서
데스크톱 앱과 [iOS의 원격 기능](/ko-KR/codex/remote-connections#set-up-mobile-access)으로 사용할 수 있습니다.

### 하나의 로컬 프로젝트에서 여러 폴더를 오가며 작업하기

이제 ChatGPT 데스크톱 앱의 로컬 프로젝트에 서로 관련된 폴더를
여러 개 포함할 수 있습니다. 새 채팅, Git 작업,
`AGENTS.md`·스킬·`config.toml` 자동 탐색에 사용할 기본 폴더를 선택하세요. 보조 폴더에서도
파일을 검색하고 읽고 편집할 수 있습니다.

**프로젝트 편집을** 열어 [폴더를 추가하고 기본
폴더를 선택하세요](/ko-KR/codex/projects#use-local-projects-for-folders-and-codebases).

[7월 23일 릴리스 노트를 확인하세요](/codex/changelog#codex-2026-07-23-app).

## 2026년 7월 13~17일

### 데스크톱에서 Work 대화와 프로젝트를 한곳에서 관리하기

이제 ChatGPT 데스크톱 앱의 ChatGPT 화면에서 채팅과 Work 대화를 함께 볼 수 있습니다.
클라우드 Work 대화는 웹, 모바일, 데스크톱 간에 동기화되고,
로컬 Work 대화는 사용자의 컴퓨터에 유지됩니다. ChatGPT 프로젝트도 데스크톱 앱에서
사용할 수 있습니다. Codex는 개발자 워크플로우를 위한 전용 화면과
별도의 기록을 유지합니다.

[데스크톱의 ChatGPT Work와 Codex를
비교](/ko-KR/codex/use-chatgpt#compare-chatgpt-work-and-codex-on-desktop)하고 작업에 맞는
화면을 선택하세요.

### Codex Micro로 병렬 Codex 작업 제어하기

7월 15일 OpenAI와 Work Louder는 한정 수량으로 제작한
[Codex Micro](/ko-KR/codex/features/codex-micro)를 출시했습니다. ChatGPT 데스크톱 앱에서 Codex를 제어하는
물리 컨트롤러로, 에이전트 키에 최대 6개 채팅의 상태가 표시되며 이 키로
채팅 간에 전환할 수 있습니다. 사용자 지정이 가능한 명령어 키와 아날로그 스틱,
다이얼로 키보드에서 손을 떼지 않고 자주 쓰는 동작이나 스킬을 실행하고,
눌러서 말하기를 시작하고 추론 수준을 조절할 수 있습니다.

### Amazon Bedrock에서 GPT-5.6 사용하기

Amazon Bedrock에서 GPT-5.6 Sol, Terra, Luna가 정식 출시되었습니다.
로컬 ChatGPT Work와 Codex에서는 Bedrock API 키나 AWS SDK 자격 증명 체인으로
내장 [`amazon-bedrock` 공급자](/ko-KR/codex/amazon-bedrock)를 사용할 수 있습니다.
지원 대상에는 ChatGPT 데스크톱 앱의 Work와 Codex,
Codex CLI, IDE 확장, Codex SDK가 포함됩니다.

### iOS에서 Codex 작업의 시각화 확인하기

iOS용 ChatGPT 1.2026.188에 Codex 작업의 인라인 시각화가 추가되고,
대화에서 작업을 생성하고 관리하는 기능이 개선되었습니다.
새로 생성한 작업으로 연결되는 링크도 더 안정적으로 작동합니다.
[7월 13일 iOS 릴리스 노트](/codex/changelog#codex-2026-07-13-mobile)를 확인하세요.

## 2026년 7월 6~10일

<a id="take-on-ambitious-work-with-chatgpt-work"></a>

### ChatGPT에서 더 큰 작업에 도전하기

ChatGPT의 [ChatGPT Work](/ko-KR/codex/get-started-with-work)는 파일과
[플러그인](/ko-KR/codex/plugins)에서 컨텍스트를 수집하고,
여러 워크플로우에서 작업을 수행하며, 검토 가능한 문서와 프레젠테이션,
스프레드시트, Sites 등 완성된 결과물을 만들 수 있습니다.
[GPT-5.6](/ko-KR/codex/models)을 기반으로 목표를 단계별로 나눠 몇 시간 동안 작업할 수 있습니다.
그동안 사용자는 진행 상황을 확인하고, 질문에 답하고, 방향을 바꾸고,
중요한 작업을 승인할 수 있습니다.

[예약 작업](/ko-KR/codex/automations)은 한 번만 실행하거나 정해진 일정에 따라 실행할 수 있으며,
이벤트가 발생할 때 또는 변경 사항을 모니터링하면서 실행할 수도 있습니다.
이를 통해 자리를 비운 동안에도 작업을 이어갈 수 있습니다.

### 적합한 GPT-5.6 모델 선택하기

[GPT-5.6 모델군](/ko-KR/codex/models#recommended-models)은 ChatGPT Work, ChatGPT 데스크톱 앱,
Codex CLI, Codex IDE 확장에서 사용할 권장 모델 3개를 제공합니다.
Sol은 복잡한 코딩, 컴퓨터 사용, 연구,
보안 작업을 위한 플래그십 모델입니다. Terra는 일상적인 작업에 적합하도록 성능과 비용의 균형을 맞추고,
Luna는 가장 빠르고 비용이 가장 낮은 모델입니다. 기본 **파워** 설정은
추론 수준을 중간으로 설정한 Sol을 사용합니다.

### ChatGPT 데스크톱 앱에서 Codex 사용하기

7월 9일 Codex 앱이 macOS 및 Windows용
[ChatGPT 데스크톱 앱](/ko-KR/codex/app)으로 통합되었습니다. Codex는 ChatGPT의 채팅 및 Work와 함께
전용 코딩 환경을 계속 제공합니다. Codex에서는
diff 내 인라인 편집, 사이드 패널의 Pull Request 검토,
GPT-5.6 기반의 더 빠른 [컴퓨터 사용](/ko-KR/codex/computer-use), 여러 레포지토리를 포함하는
프로젝트를 사용할 수 있습니다.

기존 Codex 앱 사용자는 평소처럼 업데이트할 수 있습니다. Codex를 기본 화면으로
설정하고, Codex 로고를 앱 아이콘으로 사용하고, ChatGPT 모바일 앱에서
데스크톱의 Codex 프로젝트에 접근할 수 있습니다. 업데이트된 데스크톱 앱은 Free를 포함한
모든 ChatGPT 플랜에서 전 세계적으로 사용할 수 있습니다.

## 2026년 6월 15~19일

### 시연한 워크플로우를 재사용 가능한 스킬로 만들기

[기록 및 재생](/ko-KR/codex/extend/record-and-replay)으로 macOS에서 ChatGPT나 Codex에
워크플로우를 시연하고, 그 과정을 재사용 가능한 스킬로 만들 수 있습니다.
설명보다 직접 보여 주기 쉬운 반복 작업에 사용해 보세요. 생성된 스킬을 다듬은 뒤
새 입력으로 다시 실행하세요. 초기 제공 대상에서
EEA, 영국, 스위스는 제외되며, 컴퓨터 사용 기능이 필요합니다.

<a id="continue-a-task-on-another-host"></a>

### 다른 호스트에서 채팅 이어가기

[채팅 이동](/ko-KR/codex/remote-connections#hand-off-a-chat-between-hosts) 기능은 로컬 컴퓨터와 연결된 원격 호스트 사이에서
채팅과 해당 Git 상태를 함께 옮깁니다.
Codex는 대상 호스트에 작업 트리를 만들거나 기존 작업 트리를 재사용하고,
채팅을 전송해 해당 프로젝트에서 작업을 이어갈 수 있습니다.

같은 데스크톱 릴리스에서는 예약 작업의 실행 기록에 일괄 처리 기능도 추가되었습니다.
모든 실행 기록을 읽음으로 표시하거나 보관 가능한 실행 기록을 한꺼번에 보관할 수 있습니다.

### iOS에서 워크스페이스 탐색 및 검토하기

iOS용 ChatGPT 모바일 앱의 **원격** 기능에 워크스페이스 파일 탐색기,
새 채팅용 디렉터리 선택기, diff를 펼치거나 접는 기능,
MCP 승인 범위를 개별 채팅이나 여러 채팅으로 선택하는 옵션이 추가되었습니다.

컴퓨터 사용, Chrome 확장 프로그램, 메모리, Chronicle도
EEA, 영국, 스위스에 순차적으로 제공되기 시작했습니다. 이 지역에서는 메모리가
기본적으로 꺼져 있으며, Chronicle은 macOS를 사용하는 ChatGPT Pro 구독자가 직접 활성화해 사용하는
연구 프리뷰입니다.

[6월 15일 iOS](/codex/changelog#codex-2026-06-15-mobile),
[6월 16일 제공 지역](/codex/changelog#codex-2026-06-16-app),
[6월 18일 앱](/codex/changelog#codex-2026-06-18-app) 릴리스 노트를 확인하세요.

## 2026년 6월 8~12일

### 브라우저 개발자 모드로 웹 앱 디버깅하기

[개발자 모드](/ko-KR/codex/browser?surface=app#app-developer-mode)를 사용하면 Codex가 Chrome과 내장 브라우저에서
Chrome DevTools Protocol 기능에 통제된 방식으로 접근할 수 있습니다.
Codex는 앱을 프로파일링하거나 디버깅하면서 네트워크 트래픽, 콘솔 출력, 런타임 오류,
페이지 상태를 확인할 수 있습니다. **설정** \> **브라우저의**
 **개발자 모드** 항목에서 **전체 CDP 접근 허용을** 켜세요. Codex는 이 접근 권한을 웹사이트에서 사용하기 전에
명시적인 승인을 요청합니다.

CDP와 DOM 스냅샷 최적화로 브라우저와의 통신 왕복 횟수가 줄어,
브라우저 사용 속도도 최대 두 배 빨라졌습니다.

  
    
  

### 기존 설정을 Codex로 가져오기

새 마이그레이션 플로우로 온보딩 중에 다른 코딩 에이전트의 설정 가운데
지원되는 항목을 가져올 수 있습니다. Codex 앱에는 프로젝트 지침을 만드는 `/init`도 추가되었으며,
플러그인 관리, 브라우저 진단,
완료된 채팅 요약도 개선되었습니다.

<a id="set-up-codex-tasks-from-ios"></a>

### iOS에서 Codex 채팅 설정하기

이제 iOS의 원격 기능으로 브랜치를 선택하고 작업 트리를 만들며, 환경 설정 스크립트를 실행할 수 있습니다.
목표를 관리하고 인라인 검토 댓글을 추가할 수도 있습니다.

[6월 9일 앱](/codex/changelog#codex-2026-06-09-app),
[6월 9일 iOS](/codex/changelog#codex-2026-06-09-mobile),
[6월 11일 앱](/codex/changelog#codex-2026-06-11-app) 릴리스 노트를 확인하세요.

## 2026년 6월 1~5일

### Sites로 웹사이트 만들고 배포하기

[Sites](/ko-KR/codex/sites)를 사용하면 ChatGPT가 OpenAI에서 호스팅하는 웹사이트,
대시보드, 내부 도구, 웹 앱, 게임을 만들고 저장하고 배포하고 살펴볼 수 있습니다.
웹과 데스크톱의 ChatGPT에는 Sites 전용 메뉴가 있어,
별도의 배포 스택을 구성하지 않고도 프로젝트로 돌아가
호스팅 환경의 값과 시크릿을 관리할 수 있습니다.

### Amazon Bedrock으로 Codex 사용하기

로컬 워크플로우에서 [Amazon Bedrock으로 Codex를 사용](/ko-KR/codex/amazon-bedrock)하면
AWS에서 관리하는 인증, 계정 제어, 청구 기능을 이용할 수 있습니다.
iOS의 원격 기능에는 선택적으로 사용할 수 있는 앱 내 잠금, 후속 동작 설정,
diff 줄 바꿈, Windows 컴퓨터로의 SSH 연결도 추가되었습니다.
데스크톱 앱에는 터미널 위치 조정 기능과
프로필 보기의 활동 인사이트가 추가되었습니다.

[2026년 6월의 모든 릴리스 노트를 확인하세요](/codex/changelog#month-2026-06).

## 2026년 5월 25~29일

### Windows 앱을 사용하고 Codex를 원격으로 제어하기

[컴퓨터 사용](/ko-KR/codex/computer-use#windows-foreground-use) 기능이 이제 Windows 데스크톱 앱에서
화면 확인, 클릭, 텍스트 입력을 지원합니다. 시작하기 전에
컴퓨터 사용 플러그인을 설치하세요. Windows에서 Codex는 활성 데스크톱을 사용하며,
작업이 실행되는 동안 포그라운드를 제어합니다. 원격 연결도
Windows를 지원합니다. ChatGPT 모바일 앱에서 **원격을** 열어
Windows 기기에서 작업을 시작하거나, ChatGPT 데스크톱 앱이 실행 중인 Mac을 사용하고
다른 곳에서 진행 상황을 확인하세요.

iOS의 원격 기능에는 Spotlight와 단축어를 통한 실행,
보관된 채팅 탐색, `/side`, 렌더링된 이미지를 저장하거나 복사하는 옵션도 추가되었습니다.
데스크톱 앱에는 로컬 프로젝트와 작업 트리의 채팅 조율 기능,
지난 채팅의 내용 및 브랜치 이름 검색 기능,
백그라운드 하위 에이전트를 구분하는 일관된 시각적 식별자가 추가되었습니다.

[5월 25일 iOS](/codex/changelog#codex-2026-05-25-mobile) 및
[5월 29일 앱](/codex/changelog#codex-2026-05-28-app) 릴리스 노트를 확인하세요.

## 2026년 5월 18~22일

### 앱샷으로 모든 Mac 앱의 컨텍스트를 Codex에 전달하기

양쪽 Command 키를 누르면 [앱샷](/ko-KR/codex/appshots)이 맨 앞에 있는 앱 창의
스크린샷과 가져올 수 있는 텍스트를 Codex로 보냅니다.
화면 내용을 복사해 붙여 넣거나 설명하지 않아도
Codex가 디자인 도구, 대시보드, 문서 등 다양한 앱에서 작업 컨텍스트를 얻을 수 있습니다.

### 장시간 진행되는 목표 추적하기

[목표 모드](/ko-KR/codex/prompting#goal-mode)가 실험 단계를 벗어나
Codex App, IDE 확장, CLI에서 몇 시간 또는
며칠이 걸리는 목표에 사용할 수 있게 되었습니다. [잠금 상태에서 사용](/ko-KR/codex/computer-use#locked-use) 기능을 사용하면
Mac이 잠긴 후에도 Codex가 승인된 컴퓨터 사용 작업을 계속할 수 있습니다.
ChatGPT 모바일 앱의 **원격** 기능에서도 가능합니다. ChatGPT Business 워크스페이스에서는
[재사용 가능한 플러그인 번들을 워크스페이스 멤버와 공유할 수도 있습니다](https://developers.openai.com/plugins/build/plugins#share-a-local-plugin-with-your-workspace).

[5월 21일 출시 안내를 확인하세요](/codex/changelog#codex-2026-05-21).

## 2026년 5월 11~15일

### 데스크톱 작업을 모바일에서 이어서 진행하기

ChatGPT 모바일 앱의 **원격은** ChatGPT 데스크톱 앱이 실행 중인
Mac에 연결됩니다. 작업은 연결된 호스트에서 실행되므로
휴대폰에서 작업을 이어갈 때도 프로젝트, 파일, 인증 정보,
플러그인, 스킬, 구성을 그대로 사용할 수 있습니다. [원격 연결](/ko-KR/codex/remote-connections)을 참고해
호스트를 설정하고 다른 기기에서 작업을 이어가세요.

### 신뢰할 수 있는 워크플로우 자동화하기

에이전트 수명 주기의 주요 시점에 사용자 지정 명령어를 실행하는 훅이
정식 출시되었습니다. ChatGPT Enterprise 관리자는
신뢰할 수 있는 스크립트, 스케줄러, 비공개 CI 러너에 [Codex 액세스 토큰](/ko-KR/codex/enterprise/access-tokens)을
사용할 수 있도록 설정할 수도 있습니다. 엔터프라이즈 가이드에는
Codex의 관리형 설정 및 제어 기능에 관한 내용이 추가되었습니다.

[5월 14일 출시 안내를 확인하세요](/codex/changelog#codex-2026-05-13-app).

## 2026년 5월 4~8일

### Chrome 확장 프로그램으로 여러 브라우저 탭에서 작업하기

[Chrome 확장 프로그램](/ko-KR/codex/chrome-extension)은 브라우저를 독점하지 않고
백그라운드에서 여러 탭의 작업을 병렬로 진행할 수 있습니다.
Codex가 사용할 수 있는 웹사이트를 직접 제어하면서, 여러 웹 앱에서 이루어지는 조사,
데이터 입력, 검증을 하나의 작업으로 묶어 처리할 수 있습니다.

Codex App에는 받아쓰기 텍스트 정리 기능과 이름,
파일 경로, 코드 심벌을 위한 사용자 지정 사전도 추가되었습니다. ChatGPT Enterprise 워크스페이스 소유자는
멤버가 [Codex 액세스 토큰](/ko-KR/codex/enterprise/access-tokens)을 만들어
신뢰할 수 있는 비대화형 로컬 워크플로우에서 사용하도록 허용할 수 있습니다.

[5월 5일 앱](/codex/changelog#codex-2026-05-05-app),
[5월 5일 액세스 토큰](/codex/changelog#codex-2026-05-05),
[Chrome용 Codex](/codex/changelog#codex-2026-05-07) 출시 안내를 확인하세요.

## 2026년 4월 20~24일

### 복잡한 작업에 GPT-5.5 사용하기

[GPT-5.5](/ko-KR/codex/models)가 대부분의 작업에 권장되는 모델로 Codex에 도입되었습니다.
구현, 디버깅, 테스트, 컴퓨터 사용,
연구, 지식 업무의 최종 결과물 완성에 강점을 보입니다.

### Codex에 브라우저 조작과 승인 요청 검토 맡기기

[내장 브라우저의 컴퓨터 사용](/ko-KR/codex/browser?surface=app#app-computer-use-in-the-browser) 기능으로
Codex가 로컬 개발 서버의 페이지와 파일 기반 페이지를 클릭해
문제를 재현하고 수정 결과를 검증할 수 있습니다. 조건에 맞는 승인 요청은
[승인 요청 자동 검토](/ko-KR/codex/sandboxing/auto-review)를 거칠 수도 있으며,
작업이 실행되기 전에 검토 상태와 위험이 표시됩니다.

[4월 23일 출시 안내를 확인하세요](/codex/changelog#codex-2026-04-23).

## 2026년 4월 13~17일

### 한곳에서 작업을 미리 보고 실행하기

[내장 브라우저](/ko-KR/codex/browser?surface=app)에 실시간 미리 보기와 페이지 댓글이 추가되었으며,
[컴퓨터 사용](/ko-KR/codex/computer-use)으로 Codex가 macOS 앱을 보고
조작할 수 있게 되었습니다. 두 기능 덕분에 화면 구현과 엔드 투 엔드 검증도
코드 변경과 함께 하나의 작업으로 수행할 수 있게 되었습니다.

  
    
  

<a id="start-with-a-task-and-keep-it-moving"></a>

### 채팅으로 시작해 작업 이어가기

[독립 채팅](/ko-KR/codex/projects#start-without-a-project)이 도입되어
프로젝트 폴더를 선택하지 않고도 시작할 수 있게 되었습니다. 같은 릴리스에는
[채팅 내 예약 작업](/ko-KR/codex/automations#schedule-a-task-inside-a-chat),
Pull Request 컨텍스트, 더 풍부해진 파일 미리 보기, 여러 채팅에 걸친 작업을 위한 [메모리](/ko-KR/codex/customization/memories)도
추가되었습니다.

[4월 16일 Codex App 릴리스 노트](/codex/changelog#codex-2026-04-16-app)를 읽어보세요.

## 2026년 4월 6~10일

### 앱에서 Pull Request 검토하고 반영하기

검토 기능에 접을 수 있는 인라인 댓글과 인라인 및 분리형 검토 모드가 추가되고,
Git과 소스 컨텍스트가 더 명확하게 표시되도록 개선되었습니다. 이어서 Pull Request 활동,
댓글, 푸시 옵션이 워크스페이스 파일 탭과 함께 앱에 통합되어,
다른 도구로 전환하지 않고도 변경 사항을 확인하고 대응할 수 있게 되었습니다.

[4월 9일](/codex/changelog#codex-2026-04-09-app)과
[4월 10일](/codex/changelog#codex-2026-04-10-app) Codex App 릴리스 노트를 읽거나,
[앱에서 변경 사항을 검토하는 방법](/ko-KR/codex/code-review?surface=app)을 알아보세요.

## 2026년 3월 23~27일

### 워크플로우를 플러그인으로 패키징하기

[플러그인](/ko-KR/codex/plugins)이 스킬, 커넥터, MCP 서버를 묶어
설치할 수 있는 형태로 출시되었습니다. 워크플로우 전체를 더 쉽게 찾아
설치하고 공유할 수 있게 되었으며, 새로 디자인된 플러그인 및 스킬 페이지에서는 구성 요소와
상태를 더 명확하게 확인할 수 있게 되었습니다. 같은 주에 지난 채팅 검색 기능도 추가되었습니다.

[작업 검색](/codex/changelog#codex-2026-03-24-app),
[플러그인 출시](/codex/changelog#codex-2026-03-25),
[Codex App](/codex/changelog#codex-2026-03-25-app) 릴리스 노트를 읽어보세요.

## 2026년 3월 16~20일

### 이전 메시지에서 채팅을 포크하고 Composer에서 도구 선택하기

이전 메시지에서 채팅을 포크할 수 있게 되어,
원래 흐름을 유지하면서 새로운 접근 방식을 더 쉽게 시도할 수 있게 되었습니다. 메시지를 작성하는 중에도 모델 및 추론 명령어를
사용할 수 있게 되었고, 활성화된 스킬이 `@` 메뉴에 표시되기 시작했습니다. GPT-5.4 mini는
가벼운 작업과 하위 에이전트를 위한 더 빠른 선택지로 추가되었습니다.

[GPT-5.4 mini](/codex/changelog#codex-2026-03-17),
[채팅 제어](/codex/changelog#codex-2026-03-18-app),
[스킬 메뉴](/codex/changelog#codex-2026-03-19-app) 릴리스 노트를 읽어보세요.

## 2026년 3월 9~13일

### 적절한 환경에서 작업 예약하기

[예약 작업](/ko-KR/codex/automations)에 모델과 추론 수준을 명시적으로 지정하고
로컬이나 작업 트리에서 실행할 수 있게 되었습니다. 재사용 가능한 템플릿으로 자주 하는
작업을 더 빠르게 설정하고, 사용자 지정 테마로 워크스페이스를 더 쉽게
취향에 맞게 꾸밀 수 있게 되었습니다.

  
    
  

### Codex에 터미널 출력 확인 맡기기

Codex가 현재 채팅의 [통합 터미널](/ko-KR/codex/integrated-terminal#run-and-validate-your-project)도
읽을 수 있게 되었습니다. 실행 중인 개발 서버나 빌드 출력을
붙여 넣어 달라고 요청하는 대신 직접 확인할 수 있게 되었습니다.

[3월 11일](/codex/changelog#codex-2026-03-11-app)과
[3월 12일](/codex/changelog#codex-2026-03-12-app) Codex App 릴리스 노트를 읽어보세요.

## 2026년 3월 2~6일

### Windows에서 Codex를 네이티브로 실행하기

Codex App이 네이티브 PowerShell 및 샌드박스 지원과 함께
작업 트리, 예약 작업, 스킬을 갖추고 [Windows](/ko-KR/codex/windows/windows-app)용으로 출시되었습니다. Linux 환경을 선호하는 개발자는
계속 WSL을 사용할 수 있었습니다.

  
    
  

<a id="move-tasks-between-local-and-worktree"></a>

### 로컬과 작업 트리 간에 채팅 이동하기

[로컬과 작업 트리 간 채팅 이동](/ko-KR/codex/environments/git-worktrees#working-between-local-and-worktree) 기능으로
컨텍스트를 유지하면서 진행 중인 채팅을 옮길 수 있게 되었습니다. 같은 주에 GPT-5.4도
Codex에 도입되어 코딩, 컴퓨터 사용, 더 긴 컨텍스트를 활용하는
워크플로우에 사용할 수 있게 되었습니다.

[Windows 출시](/codex/changelog#codex-2026-03-04-app),
[작업 트리 간 채팅 이동](/codex/changelog#codex-2026-03-03-app),
[GPT-5.4](/codex/changelog#codex-2026-03-05) 릴리스 노트를 읽어보세요.

## 2026년 2월 9~13일

### 실시간으로 개선하고 채팅을 포크해 다른 접근법 시도하기

실시간으로 코드를 개선할 수 있도록 거의 즉시 응답하는 모델 GPT-5.3-Codex-Spark가
연구 프리뷰로 공개되었습니다. 앱에는 채팅 포크 기능과
항상 맨 위에 표시되는 플로팅 채팅 창도 추가되어, 다른 접근법을 시도하거나
편집기 또는 브라우저 옆에 Codex를 띄워둘 수 있게 되었습니다.

[Spark](/codex/changelog#codex-2026-02-12)와
[Codex App](/codex/changelog#codex-2026-02-12-app) 릴리스 노트를 읽거나,
현재 [모델 가이드](/ko-KR/codex/models)를 참고하세요.

## 2026년 2월 2~6일

### macOS용 Codex App 출시

Codex App은 여러 프로젝트 채팅을 동시에 진행할 수 있고,
내장 Git 검토 기능, 작업 트리, 스킬, 예약 작업, 음성 받아쓰기를 지원하는 데스크톱 워크스페이스로 출시되었습니다.
현재 이러한 기능은 [ChatGPT 데스크톱 앱](/ko-KR/codex/app)의 Codex에서 제공됩니다.

  
    
  

### 진행 중인 작업 방향을 조정하고 파일 추가하기

응답 도중에 지시를 추가해 진행 중인 응답을 중단하지 않고도
Codex의 작업 방향을 바꿀 수 있게 되었으며, 이미지 외의 파일도 첨부할 수 있게 되었습니다. 이러한 방식은
Codex에 필요한 컨텍스트를 담은 후속 메시지로 [작업 방향을 조정하거나 후속 메시지를 대기열에 추가하는](/ko-KR/codex/prompting#steering-and-queuing)
기능의 기반이 되었습니다.

[Codex App 출시 노트](/codex/changelog#codex-2026-02-02)와
[2월 5일 앱 릴리스 노트](/codex/changelog#codex-2026-02-05-app)를 읽어보세요.

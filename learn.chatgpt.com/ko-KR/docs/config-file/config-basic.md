<!-- source: https://learn.chatgpt.com/ko-KR/docs/config-file/config-basic -->

Codex는 여러 위치에서 구성 정보를 읽습니다. 개인 기본값은 `~/.codex/config.toml`에 저장되며, `.codex/config.toml` 파일로 프로젝트별 설정을 재정의할 수 있습니다. 보안을 위해 Codex는 신뢰하는 프로젝트의 `.codex/` 계층만 로드합니다.

## Codex 구성 파일

Codex는 사용자 수준 구성을 `~/.codex/config.toml`에 저장합니다. 설정을 특정 프로젝트나 하위 폴더에만 적용하려면 레포지토리에 `.codex/config.toml` 파일을 추가하세요.

Codex IDE 확장에서 구성 파일을 열려면 오른쪽 상단의 톱니바퀴 아이콘을 선택한 다음 **Codex 설정 \> config.toml 열기를** 선택하세요.

CLI와 IDE 확장은 동일한 구성 계층을 공유합니다. 이 구성으로 다음을 설정할 수 있습니다:

- 기본 모델과 제공업체를 설정합니다.
- [승인 정책과 샌드박스 설정](/ko-KR/codex/agent-approvals-security#sandbox-and-approvals)을 구성합니다.
- [MCP 서버](/ko-KR/codex/extend/mcp)를 구성합니다.

## 구성 우선순위

Codex는 다음 순서로 값을 결정합니다(우선순위가 높은 항목부터):

1. CLI 플래그 및 `--config` 재정의
2. 프로젝트 구성 파일: `.codex/config.toml`. 프로젝트 루트부터 현재 작업 디렉터리까지 순서대로 적용합니다(현재 디렉터리에서 가장 가까운 파일이 우선하며, 신뢰하는 프로젝트에만 적용).
3. `--profile profile-name` 옵션으로 선택한 [프로필](/ko-KR/codex/config-file/config-advanced#profiles) 파일(`~/.codex/profile-name.config.toml`)
4. 사용자 설정: `~/.codex/config.toml`
5. 시스템 구성(있는 경우): Unix의 `/etc/codex/config.toml`
6. 기본 제공 값

이 우선순위를 활용해 공통 기본값은 `config.toml`에 설정하고, [프로필 파일](/ko-KR/codex/config-file/config-advanced#profiles)에는 달라지는 값만 지정하세요.

프로젝트를 신뢰하지 않는 것으로 표시하면 Codex는 프로젝트 로컬 구성, 훅, 규칙을 포함한 프로젝트 범위의 `.codex/` 계층을 건너뜁니다. 사용자/전역 훅과 규칙을 포함한 사용자 설정과 시스템 구성은 계속 로드됩니다.

`-c`/`--config`를 사용한 일회성 재정의(TOML 따옴표 사용 규칙 포함)는 [고급 구성](/ko-KR/codex/config-file/config-advanced#one-off-overrides-from-the-cli)을 참조하세요.

  조직에서 관리하는 기기에서는
`requirements.toml` 파일로 제약 조건을 적용할 수도 있습니다(예: `approval_policy = "never"` 또는
`sandbox_mode = "danger-full-access"` 설정 금지). [관리형
  설정](/ko-KR/codex/enterprise/managed-configuration)과 [관리자가 강제하는
  요구 사항](/ko-KR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)을 참조하세요.

## 주요 구성 옵션

가장 자주 변경하는 옵션 몇 가지를 소개합니다:

#### 기본 모델

CLI와 IDE에서 Codex가 기본적으로 사용할 모델을 선택하세요.

#### 승인 프롬프트

Codex가 생성한 명령어를 실행하기 전에 어떤 경우에 멈추고 승인을 요청할지 설정하세요.

```toml
approval_policy = "on-request"

`untrusted`, `on-request`, `never`의 동작 차이는 [승인 프롬프트 없이 실행](/ko-KR/codex/agent-approvals-security#run-without-approval-prompts)과 [일반적인 샌드박스 및 승인 조합](/ko-KR/codex/agent-approvals-security#common-sandbox-and-approval-combinations)을 참조하세요.

#### 샌드박스 수준

Codex가 명령어를 실행할 때 허용되는 파일 시스템 및 네트워크 접근 범위를 조정하세요.

```toml
sandbox_mode = "workspace-write"

보호되는 `.git`/`.codex` 경로와 네트워크 기본값을 비롯한 모드별 동작은 [샌드박스 및 승인](/ko-KR/codex/agent-approvals-security#sandbox-and-approvals), [쓰기 가능한 루트 내 보호 경로](/ko-KR/codex/agent-approvals-security#protected-paths-in-writable-roots), [네트워크 접근](/ko-KR/codex/agent-approvals-security#network-access)을 참조하세요.

#### 권한 프로필

Codex는 파일 시스템과
네트워크 정책을 재사용할 수 있도록 이름이 지정된 권한 프로필도 지원합니다. 기본 제공 프로필은 `:read-only`, `:workspace`,
`:danger-full-access`입니다. 사용자 지정 프로필은 `[permissions.<name>]` 테이블과
이에 대응하는 `default_permissions` 값을 사용합니다. [권한](/ko-KR/codex/permissions)을 참조하세요.

#### Windows 샌드박스 모드

Windows에서 Codex를 네이티브로 실행할 때는 `windows` 테이블에서 네이티브 샌드박스 모드를 `elevated`로 설정하세요. 관리자 권한이 없거나 권한 승격 모드 설정에 실패한 경우에만 `unelevated` 모드를 사용하세요.

```toml
[windows]
sandbox = "elevated"   # Recommended
# sandbox = "unelevated" # Fallback if admin permissions/setup are unavailable

#### 웹 검색 모드

Codex는 로컬 채팅에서 기본적으로 웹 검색을 활성화하고 웹 검색 캐시의 결과를 제공합니다. 이 캐시는 OpenAI가 관리하는 웹 검색 결과 인덱스이므로, 캐시 모드에서는 실시간 페이지를 가져오는 대신 미리 인덱싱된 결과를 반환합니다. 이 방식은 임의의 실시간 콘텐츠를 통한 프롬프트 인젝션 노출을 줄여 주지만, 웹 검색 결과는 여전히 신뢰할 수 없는 데이터로 취급해야 합니다. `--yolo` 또는 다른 [전체 권한 샌드박스 설정](/ko-KR/codex/agent-approvals-security#common-sandbox-and-approval-combinations)을 사용하면 웹 검색은 기본적으로 실시간 결과를 제공합니다. `web_search`로 모드를 선택하세요:

- `"cached"`(기본값)은 웹 검색 캐시의 결과를 제공합니다.
- `"indexed"` 모드는 검색 인덱스에서 요청을 허용한 경우에만 외부 웹 접근을 허용합니다.
- `"live"` 모드는 웹에서 최신 데이터를 가져옵니다(`--search`와 동일).
- `"disabled"` 모드는 웹 검색 도구를 끕니다.

```toml
web_search = "cached"  # default; serves results from the web search cache
# web_search = "indexed" # gate external web access through the search index
# web_search = "live"  # fetch the most recent data from the web (same as --search)
# web_search = "disabled"

#### 추론 강도

지원되는 경우 모델의 추론 강도를 조정하세요.

```toml
model_reasoning_effort = "high"

#### 커뮤니케이션 스타일

지원되는 모델의 기본 커뮤니케이션 스타일을 설정하세요.

```toml
personality = "friendly" # or "pragmatic" or "none"

나중에 활성 세션에서 `/personality` 명령어로 이 설정을 재정의할 수 있습니다. app-server API를 사용할 때는 스레드나 턴별로 재정의할 수도 있습니다.

#### TUI 키맵

`tui.keymap`에서 터미널 단축키를 사용자 지정하세요. 일부 Composer 동작은 별도 바인딩이 없으면 일치하는 `tui.keymap.global` 바인딩을 사용합니다. 컨텍스트별 바인딩이 지원되는 경우에는 해당 바인딩이 우선합니다. 빈 목록을 지정하면 해당 동작의 바인딩이 해제됩니다.

```toml
[tui.keymap.global]
open_transcript = "ctrl-t"

[tui.keymap.composer]
submit = ["enter", "ctrl-m"]

[tui.keymap.chat]
interrupt_turn = "f12"

#### 명령어 환경

Codex가 실행하는 명령어에 전달할 환경 변수를 설정하세요.
키 기반 필터로 필요한 변수만 유지하세요:

```toml
[shell_environment_policy]
ignore_default_excludes = false

[shell_environment_policy.filters]
"PATH" = "include"
"HOME" = "include"

`ignore_default_excludes`의 기본값은 `true`이며,
이름에 `KEY`, `SECRET` 또는 `TOKEN`이 포함된 변수를 자동으로 필터링하지 않습니다. 자동 필터링을 사용하려면
`false`로 설정하세요. 제외 규칙, 우선순위 및
레거시 구성은 [셸 환경
정책](/ko-KR/codex/config-file/config-advanced#shell-environment-policy)을 참조하세요.

#### 로그 디렉터리

Codex가 로컬 로그 파일을 기록하는 위치를 재정의하세요. `log_dir` 값을 명시적으로 설정하면
선택적으로 활성화할 수 있는 일반 텍스트 TUI 로그인 `codex-tui.log`도 해당 디렉터리에 기록됩니다.

```toml
log_dir = "/absolute/path/to/codex-logs"

일회성 실행에서는 CLI로도 설정할 수 있습니다:

```bash
codex -c log_dir=./.codex-log

## 기능 플래그

`config.toml`의 `[features]` 테이블로 선택적 기능과 실험적 기능을 켜거나 끄세요.

### 주요 기능 플래그

| 키                  |        기본값        | 성숙도     | 설명                                                                              |
| -------------------- | :-------------------: | ------------ | ---------------------------------------------------------------------------------------- |
| `apps`               |         true          | 안정       | 앱(커넥터) 통합 활성화                                                      |
| `goals`              |         true          | 안정적       | 목표 저장 및 자동 이어서 실행 활성화                                        |
| `hooks`              |         true          | 안정적       | `hooks.json` 또는 인라인 `[hooks]`에 정의된 라이프사이클 훅을 활성화합니다. [훅](/ko-KR/codex/hooks)을 참조하세요. |
| `fast_mode`          |         true          | 안정적       | 패스트 모드 선택 및 `service_tier = "fast"` 경로 활성화                          |
| `memories`           |         false         | 실험적 | [메모리](/ko-KR/codex/customization/memories) 활성화                                         |
| `multi_agent`        |         true          | 안정적       | 하위 에이전트 협업 도구 활성화                                                      |
| `personality`        |         true          | 안정적       | 성격 선택 컨트롤 활성화                                                    |
| `remote_plugin`      |         true          | 안정적       | 원격 플러그인 카탈로그 활성화                                                         |
| `shell_snapshot`     |         true          | 안정적       | 셸 환경의 스냅샷을 생성하여 반복 명령어 실행 속도 향상                            |
| `shell_tool`         |         true          | 안정적       | 기본 `shell` 도구 활성화                                                          |
| `unified_exec`       | `true`(Windows 제외) | 안정적       | 통합 PTY 기반 exec 도구 사용                                                     |
| `web_search`         |         true          | 사용 중단 예정(deprecated)   | 레거시 토글이며, 최상위 `web_search` 설정 사용을 권장합니다                                 |
| `web_search_cached`  |         false         | 사용 중단 예정(deprecated)   | 값이 설정되지 않은 경우 `web_search = "cached"`에 매핑되는 레거시 토글                            |
| `web_search_request` |         false         | 사용 중단 예정(deprecated)   | 값이 설정되지 않은 경우 `web_search = "live"`에 매핑되는 레거시 토글                              |

  이 표에는 일반적인 사용자 대상 플래그가 나열되어 있으며, 내부 기능이나
  개발 중인 기능이 모두 포함되지는 않습니다. 성숙도 열에는
  실험적, 베타, 안정적 등의 레이블이 사용됩니다. 각 레이블의 의미는 [기능
  성숙도](/ko-KR/codex/feature-maturity)를 참조하세요.

기본값을 유지하려면 기능 키를 생략하세요.

라이프사이클 훅 구성은 [훅](/ko-KR/codex/hooks)을 참조하세요.

### 기능 활성화

- `config.toml`에서 `[features]` 아래에 `feature_name = true`를 추가하세요.
- CLI에서 `codex --enable feature_name`을 실행하세요.
- 여러 기능을 활성화하려면 `codex --enable feature_a --enable feature_b` 명령어를 실행하세요.
- 기능을 비활성화하려면 `config.toml`에서 해당 키를 `false`로 설정하세요.

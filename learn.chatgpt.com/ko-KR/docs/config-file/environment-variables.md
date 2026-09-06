<!-- source: https://learn.chatgpt.com/ko-KR/docs/config-file/environment-variables -->

Codex는 지속적으로 유지할 설정을 `config.toml`에 저장합니다.
셸 범위의 설정 재정의, 자동화용 시크릿, 설치 프로그램 동작 또는 진단에는 환경 변수를 사용하세요.

이 페이지에는 Codex가 직접 읽는 안정적인 공개 환경 변수가 나와 있습니다.
내부 개발 변수, 테스트 변수 또는
[`env_key`](/ko-KR/codex/config-file/config-advanced#custom-model-providers)로 직접 지정하는 공급자별 시크릿 이름은
포함하지 않습니다.

## 주요 경로

| 변수            | 사용처                                    | 기본값      | 설명                                                                                                                                                      |
| ------------------- | ------------------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_HOME`        | CLI, IDE 확장, app-server, 설치 프로그램 | `~/.codex`   | 구성, 인증, 로그, 세션, 스킬, 독립 실행형 패키지 메타데이터를 포함한 Codex 상태 데이터의 루트 경로를 설정합니다. 이 변수를 설정할 경우 디렉터리가 이미 있어야 합니다. |
| `CODEX_SQLITE_HOME` | CLI 및 app-server 상태 데이터                   | `CODEX_HOME` | SQLite 기반 상태 데이터가 저장될 위치를 설정합니다. `sqlite_home` 구성 옵션이 우선합니다. 상대 경로는 현재 작업 디렉터리를 기준으로 해석됩니다.           |

`CODEX_HOME`에 저장되는 파일에 관한 자세한 내용은
[구성 및 상태 경로](/ko-KR/codex/config-file/config-advanced#config-and-state-locations)를 참조하세요.

## 설치 프로그램 변수

이 변수는
`https://chatgpt.com/codex/install.sh` 및
`https://chatgpt.com/codex/install.ps1`에서 제공되는 독립 실행형 설치 스크립트에 적용됩니다.

| 변수                | 기본값                                                                              | 설명                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_NON_INTERACTIVE` | `false`                                                                              | 설치 프로그램 프롬프트를 건너뛰려면 `1`, `true` 또는 `yes` 중 하나로 설정하세요. 각 프롬프트에는 기본 응답이 적용되므로 최초 실행 설정이 아닌 스크립트 기반 설치 및 업데이트에 사용하세요. |
| `CODEX_INSTALL_DIR`     | macOS/Linux에서는 `~/.local/bin`, Windows에서는 `%LOCALAPPDATA%\Programs\OpenAI\Codex\bin` | 사용자에게 노출되는 `codex` 명령어의 설치 위치를 변경합니다. 독립 실행형 패키지 캐시는 계속 `CODEX_HOME/packages/standalone`에 있습니다.                        |

무인 설치의 경우 다운로드한 설치 프로그램을 실행하는 셸에서
`CODEX_NON_INTERACTIVE=1` 설정을 적용하세요:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_NON_INTERACTIVE=1 sh

```powershell
$env:CODEX_NON_INTERACTIVE=1; irm https://chatgpt.com/codex/install.ps1 | iex

## 인증 및 네트워크

| 변수                           | 사용처                                          | 설명                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_API_KEY`                    | Exec, review, TypeScript SDK, 원격 exec-server | 비대화형 Codex 프로세스에 API 키를 제공합니다. 레포지토리에서 제어하는 코드를 실행할 때는 작업 전체에 적용하지 말고 인라인으로 설정하세요.             |
| `CODEX_ACCESS_TOKEN`               | CLI, app-server, 신뢰할 수 있는 자동화              | 신뢰할 수 있는 자동화에 사용할 ChatGPT 또는 Codex 액세스 토큰을 제공합니다. 로그인 정보를 저장하려면 이 토큰을 `codex login --with-access-token`에 파이프로 전달하세요.             |
| `OPENAI_FEDERATION_RULE_ID`        | 워크로드 ID                                | 워크로드에 구성된 페더레이션 규칙을 선택합니다.                                                                                        |
| `OPENAI_IDENTITY_TOKEN_FILE`       | 워크로드 ID                                | 현재 OIDC 토큰 또는 SPIFFE JWT-SVID가 포함된 파일의 절대 경로를 지정합니다.                                                |
| `OPENAI_WORKLOAD_IDENTITY_CONTEXT` | 워크로드 ID                                | 클라이언트가 보고하는 감사 주체를 식별하기 위해 크기가 제한된 JSON 식별자를 선택적으로 제공합니다. 인증이나 권한 부여에는 영향을 미치지 않습니다.         |
| `CODEX_CA_CERTIFICATE`             | HTTPS, 로그인 및 WebSocket 클라이언트              | 기업의 TLS 가로채기 또는 사설 루트 인증서를 사용하는 환경에 필요한 PEM CA 번들을 지정합니다. `SSL_CERT_FILE`보다 우선합니다. |
| `SSL_CERT_FILE`                    | HTTPS, 로그인 및 WebSocket 클라이언트              | `CODEX_CA_CERTIFICATE` 설정이 없을 때 사용하는 대체 PEM CA 번들 경로입니다.                                                                               |

공급자 API 키를 사용하려면 모델 공급자 구성에서
[`env_key`](/ko-KR/codex/config-file/config-advanced#custom-model-providers)를 설정하세요.
Codex는 해당 구성에 지정된 이름의 변수를 읽으므로
변수 이름 자체는 고정된 Codex 환경 변수가 아닙니다.

자동화용 시크릿 처리에 관한 내용은
[API 키 인증 사용](/ko-KR/codex/non-interactive-mode#use-api-key-auth)을 참조하세요.
액세스 토큰 설정은 [액세스 토큰](/ko-KR/codex/enterprise/access-tokens)을 참조하세요.
워크로드 ID 설정은
[워크로드 ID 페더레이션](/ko-KR/codex/enterprise/workload-identity)을 참조하세요.

## 진단

| 변수   | 사용처            | 설명                                                                                                             |
| ---------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `RUST_LOG` | CLI 및 app-server | Rust 로그 필터링과 출력 상세 수준을 제어합니다. 더 상세한 값을 설정하지 않으면 `codex exec`은 기본적으로 `error` 수준의 메시지만 출력합니다. |

`RUST_LOG`에는 `error`, `warn`, `info`, `debug`,
`trace` 등의 값을 지정할 수 있습니다. 또한
`codex_core=debug,codex_tui=debug`처럼 특정 대상을 지정하는 Rust 로깅 필터도 사용할 수 있습니다.

대화형 CLI는 기본적으로 저장량이 제한된 로컬 저장소에 진단 정보를 기록하지만,
일반 텍스트 `codex-tui.log` 파일 기록은 선택적으로 활성화해야 합니다. 문제 해결에
일반 텍스트 로그가 필요하면 `log_dir`를 명시적으로 설정하세요:

```bash
RUST_LOG=debug codex -c log_dir=./.codex-log
tail -F ./.codex-log/codex-tui.log

비대화형 모드에서 `codex exec` 명령어는 별도의 TUI 로그 파일에 기록하는 대신
메시지를 인라인으로 출력합니다.

<!-- source: https://learn.chatgpt.com/ko-KR/docs/amazon-bedrock -->

Amazon Bedrock을 통해 제공되는 OpenAI 모델을 사용하도록 로컬 ChatGPT Work 및 Codex
인터페이스를 구성하세요. 이 구성에서는 로컬 클라이언트가 AWS에서 관리하는 인증과 액세스 제어를
사용해 Bedrock에 모델 요청을 보냅니다.

## 작동 방식

로컬 ChatGPT Work 또는 Codex 인터페이스에서 Amazon Bedrock을 모델 제공자로 구성하면
OpenAI가 호스팅하는 Responses API는 요청 경로에 포함되지 않습니다.
로컬 클라이언트는 모델 요청을 Amazon Bedrock에 보내며, Bedrock은 지원되는
OpenAI 모델에 대해 OpenAI와 호환되는 Responses API 구현을 제공합니다.

  인증은 AWS 네이티브 방식입니다. 사용자는 Bedrock API 키 또는 AWS
  IAM 자격 증명으로 인증합니다. 이 제공자에서는 ChatGPT 로그인이나 `OPENAI_API_KEY`를
  사용하지 않습니다.

## 시작하기 전에

다음 항목이 준비되어 있는지 확인하세요:

- Amazon Bedrock에서 지원되는 OpenAI 모델에 대한 액세스 권한.
- 선택한 모델을 사용할 수 있는 AWS 리전.
- AWS 계정에 구성된 Amazon Bedrock Mantle 경로에 대한 인증.

## 모델 제공자 구성

Amazon Bedrock Mantle 경로용 `amazon-bedrock` 모델 제공자를
`~/.codex/config.toml`에 추가하세요. ChatGPT 데스크톱 앱, Codex CLI, IDE 확장, SDK는
동일한 로컬 구성 계층을 읽습니다. 모델 지정은 선택 사항입니다.
필요하면 지원되는 모델을 명시적으로 선택하세요.

```toml
model_provider = "amazon-bedrock"

  이 가이드에서는 지원되는 상용 AWS 리전의 Amazon Bedrock Mantle 경로를 다룹니다.
로컬 ChatGPT Work 및 Codex 인터페이스는 AWS GovCloud 리전의 Bedrock Mantle
엔드포인트를 지원하지 않습니다.

## 인증 옵션

로컬 ChatGPT Work 및 Codex 인터페이스는 두 가지 Bedrock 인증 방식을 지원하며,
다음 순서로 확인합니다:

1. Bedrock API 키.
2. AWS SDK 자격 증명 체인.

### 옵션 1: Bedrock API 키

로컬 클라이언트가 읽는 환경에 Bedrock API 키를 설정하세요. API 키 인증을
사용할 때는 리전을 지정해야 합니다.

```shell

### 옵션 2: AWS SDK 자격 증명

조직에서 AWS SDK 자격 증명 체인을 통해 Bedrock 액세스를 관리하는 경우 이 방식을
사용하세요. 로컬 클라이언트는 다음과 같은 표준 AWS SDK 자격 증명 소스를
사용할 수 있습니다:

#### 공유 AWS 구성 파일

공유 AWS `config` 및 `credentials` 파일을 구성하세요:

```shell
aws configure

#### 환경 변수

표준 AWS SDK 자격 증명 환경 변수를 설정하세요:

```shell

#### AWS Management Console 자격 증명

AWS Management Console 자격 증명으로 로그인하세요:

```shell
aws login

#### AWS SSO 또는 명명된 프로필

AWS SSO로 로그인하고 명명된 프로필을 선택하세요:

```shell
aws sso login --profile codex-bedrock

#### 페더레이션 ID

기업 SSO 또는 OIDC 페더레이션을 사용하는 경우 로컬 클라이언트 외부에서
`credential_process`로 페더레이션 ID를 구성하고 AWS SDK가 자격 증명을
가져오도록 하세요. 브라우저 로그인, 토큰 교환, 캐싱, 갱신은
AWS 프로필의 `credential_process` 헬퍼에서 처리하세요.

## 데스크톱 앱 및 IDE 확장

데스크톱 앱과 IDE 확장은 셸의 환경 변수를 상속하지 않을 수 있습니다.
필수 값을 `~/.codex/.env`에 추가한 다음 앱이나
IDE 확장을 다시 시작하세요.

```shell

## 설정 확인

- Codex CLI에서 `/status`를 열고 Codex가
`amazon-bedrock` 모델 제공자를 사용 중인지 확인하세요.
- ChatGPT 데스크톱 앱을 다시 시작한 다음 Work 또는 Codex를 선택하고
새 작업을 시작하세요.
- IDE 확장을 다시 시작한 다음 새 세션을 시작하세요.
- 선택한 모델을 구성된 AWS 리전에서 사용할 수 있고 AWS 자격 증명 주체에 해당 모델에
액세스할 권한이 있는지 확인하세요.

## 지원되는 모델

정확한 모델 ID를 사용하세요:

```text
openai.gpt-5.6-sol
openai.gpt-5.6-terra
openai.gpt-5.6-luna
openai.gpt-5.5
openai.gpt-5.4

사용할 수 있는 모델은 AWS 리전에 따라 다릅니다. 모델을 선택하기 전에 [AWS
리전별 모델
지원](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html)을 확인하세요.

## 기능 제공 여부

이 구성은 로컬 ChatGPT Work 및 Codex 워크플로우를 지원합니다. 웹에서 호스팅되는
ChatGPT Work, Codex 클라우드, OpenAI가 호스팅하는 클라우드 서비스, 호스팅 도구 또는
클라우드 관리형 탐색에 의존하는 기능은 현재 사용할 수 없습니다.

  Amazon Bedrock에서는 패스트 모드를 사용할 수 없습니다. 패스트 모드는 우선 처리 방식을
사용하지만, Amazon Bedrock의 초기 제공 범위에서는 온디맨드
추론만 지원합니다.

  

  <div
    id="codex-plan-region-limits"
    className="not-prose mt-3 text-sm text-secondary"
  >
    <sup>\*</sup> 이 기능은 현재 특정 지역에서만 사용할 수 있습니다. 지역 제한에 관한 자세한 내용은
    각 기능의 문서를 확인하세요.
  </div>
  <div
    id="codex-plan-plugin-limits"
    className="not-prose mt-1 text-sm text-secondary"
  >
    <sup>†</sup> Codex Security를 포함해 ChatGPT 인증이 필요하지 않은 로컬 플러그인 번들과
    OpenAI에서 선별한 플러그인을 사용할 수 있습니다.
    ChatGPT 인증, 커넥터 또는 클라우드 호스팅 공유 기능이 필요한
    플러그인은 사용할 수 없습니다.
  </div>

## 문제 해결

설정에 실패하면 다음을 확인하세요:

- 모델 ID가 지원되는 모델의 ID와 정확히 일치합니다.
- 모델을 사용할 수 있는 AWS 리전을 지정했습니다.
- Bedrock API 키 또는 AWS 자격 증명이 유효하고 만료되지 않았습니다.
- AWS 자격 증명 주체에 선택한 Bedrock 모델에 액세스할 권한이 있습니다.
- `AWS_BEARER_TOKEN_BEDROCK`에 만료되었거나 의도하지 않은 키가 설정되어 있지 않습니다.
- 데스크톱 앱 또는 IDE 확장을 사용하는 경우 필수 환경 변수가
  `~/.codex/.env`에 설정되어 있습니다.

## 지원 범위

OpenAI 지원팀은 ChatGPT Work 및 Codex 클라이언트 설정과 구성,
로컬 CLI, 데스크톱 앱, IDE 확장의 동작 및
로컬 제품 사용 환경에 관해 도움을 드릴 수 있습니다.

AWS 자격 증명, IAM 권한, Bedrock 모델 액세스, 할당량, 청구,
리전별 가용성, Bedrock 요청 실패, AWS 서비스 로그 또는 Bedrock
서비스 동작에 대해서는 고객의 AWS 관리자나 AWS Support에 문의하세요.

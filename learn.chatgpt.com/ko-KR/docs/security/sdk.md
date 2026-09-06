<!-- source: https://learn.chatgpt.com/ko-KR/docs/security/sdk -->

Codex Security TypeScript SDK를 사용하면 애플리케이션이나 개발자 도구에서 레포지토리와
코드 변경 사항에 대한 보안 스캔을 실행할 수 있습니다. SDK는 타입이 지정된 보안 이슈,
검토 범위 세부 정보와 스캔 아티팩트 경로를 반환합니다. 장시간 실행되는 스캔에는
사전 점검, 비용 한도, 진행 상황 콜백과 취소 기능을 지원합니다.

SDK는 ECMAScript 모듈(ESM)을 사용하며 Node.js 22
(22.13.0 이상), 24 또는 26을 사용하는 서버 측 환경에서 실행됩니다. 스캔에는 Python 3.10 이상도 필요합니다.
Python 3.10에서는 `tomli` 패키지도 필요합니다.

  Codex Security SDK는 [GitHub에
  공개되어 있습니다](https://github.com/openai/codex-security). 스캔을 실행하려면
  Codex Security 사용 권한이 필요합니다. 일반 코딩 에이전트에 대해서는 [Codex SDK
  가이드](/ko-KR/codex/codex-sdk)를 참조하세요. 터미널 및 CI 워크플로우에 대해서는 [Codex
  Security CLI 빠른 시작](/ko-KR/codex/security/cli)을 참조하세요.

## SDK 설정

SDK를 설치하세요:

```bash
npm install @openai/codex-security

스캔을 시작하기 전에 `OPENAI_API_KEY` 또는 `CODEX_API_KEY`를 설정하거나,
파일에 저장된 기존 Codex 로그인 정보를 사용하거나, [다른
제공업체를 구성하세요](#configure-the-runtime-and-credentials). Amazon Bedrock은 AWS
자격 증명을 사용하며, OpenRouter와 Fireworks는 제공업체별 API 키와
구성을 사용합니다.

최상의 결과를 얻으려면 [Trusted Access for
Cyber](https://chatgpt.com/cyber) 인증을 받은 계정을 사용하세요. 로그인하거나 API 키를 제공해도
Trusted Access 권한이 부여되지는 않습니다.

## 스캔 실행

신뢰할 수 있고 평가 권한이 있는 레포지토리만 스캔하세요. SDK는
사용자의 로컬 운영체제 권한으로 실행되며 승인을 요청하기 위해 실행을 멈추지 않습니다.
스캔 프로세스가 사용자 환경을 상속할 수 있으므로 시작하기 전에 관련 없는 자격 증명을
제거하세요. 자세한 내용은 [로컬 스캔
권한](/ko-KR/codex/security/cli/reference#local-scan-permissions)을 참조하세요.

`CodexSecurity` 클라이언트를 하나 생성해 표준 레포지토리 스캔을 실행하고,
작업이 완료되면 클라이언트를 닫으세요. `outputDir`를 전달해 해당 Git 작업 트리 외부의
비공개 결과 디렉터리를 지정하세요.

`outputDir` 설정을 생략하면 Codex Security는 자체 영구
상태 디렉터리에 결과를 저장합니다. 결과에는 소스 코드 발췌문과 취약점
세부 정보가 포함될 수 있으므로 적절한 권한과 보존 정책을 선택하세요.

```ts

const security = new CodexSecurity();

try {
  const result = await security.run("/path/to/repository", {
    outputDir: "/path/outside/repository/results",
  });

  console.log(result.reportPath);
  console.log(result.coverage.completeness);
  console.log(result.findings.findings.length);
} finally {
  await security.close();
}

`run`은 스캔을 시작하고 완료될 때까지 기다린 후 봉인된 아티팩트를 검증하여
`ScanResult`를 반환합니다. `close`는 격리된 런타임을 해제하며
여러 번 호출할 수 있습니다.

## 사전 점검으로 입력값 확인

스캔을 시작하기 전에 `preflight`로 레포지토리, 대상, 모드, 지식 베이스 문서,
출력 위치와 Codex 구성을 확인하세요:

```ts
const plan = await security.preflight("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
  knowledgeBasePaths: ["/path/to/architecture.md"],
  outputDir: "/path/outside/repository/results",
});

console.log(plan.repository);
console.log(plan.target.kind);
console.log(plan.mode);
console.log(plan.outputDir);

사전 점검은 Codex 런타임과 자격 증명을 변경하지 않습니다. 플러그인 및
Python 탐색도 실제 스캔 단계에서 수행됩니다. 따라서 장시간 실행되거나
자격 증명이 필요한 작업을 시작하기 전에 사용자 입력을 확인하는 데 유용합니다.

기존 결과 디렉터리의 아카이브 작업을 미리 확인하려면
`archiveExisting: true`로 설정하세요:

```ts
const plan = await security.preflight("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
});

console.log(plan.archiveDir);

반환된 `archiveDir`에서 아카이브 이름 지정 방식을 미리 확인할 수 있습니다.
`run`은 고유한 대상 경로를 별도로 생성하므로 최종 경로는 달라질 수 있습니다.
실제 아카이브 경로는 `onOutputArchived`로 확인하세요:

```ts
await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
  onOutputArchived(archiveDir) {
    console.log("Archived results:", archiveDir);
  },
});

스캔은 기존 결과를 아카이브한 다음 비어 있는 출력
디렉터리에서 시작합니다.

## 스캔 대상 선택

SDK는 레포지토리, 경로, 커밋된 변경 사항, 작업 트리를 스캔 대상으로 지원합니다.
기본 대상은 전체 레포지토리입니다.

### 선택한 경로 스캔

레포지토리 내부 경로를 배열로 전달하세요:

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
});

경로로 파일 또는 디렉터리를 지정할 수 있습니다. SDK는 각 경로를 레포지토리
내부 기준으로 해석하고 중복을 제거합니다.

### 커밋된 변경 사항 스캔

`DiffTarget.refs`로 로컬에서 사용할 수 있는 두 Git 리비전 사이의
커밋된 변경 사항을 스캔하세요:

```ts

const target = DiffTarget.refs({
  base: "origin/main",
  head: "HEAD",
});

const result = await security.run("/path/to/repository", { target });

헤드의 기본값은 `HEAD`입니다. diff 대상에서는 레포지토리 인수로
Git 작업 트리의 루트를 전달해야 합니다.

### 작업 트리 스캔

`DiffTarget.workingTree`로 기준 리비전과 비교해 스테이징된 변경 사항과
스테이징되지 않은 변경 사항을 스캔하세요:

```ts
const target = DiffTarget.workingTree({ base: "HEAD" });
const result = await security.run("/path/to/repository", { target });

기준 리비전의 기본값은 `HEAD`입니다. diff 또는 작업 트리 스캔을 시작하기 전에
선택한 리비전을 가져오세요.

### 딥 모드 선택

더 폭넓은 검토가 필요한 레포지토리 또는 경로 스캔에서는 `mode: "deep"`으로 설정하세요:

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing"],
  mode: "deep",
  workers: 2,
  subagents: 0,
  stopAfterNoNew: 3,
  maxDiscoveryRuns: 10,
  maxTimeHours: 1.5,
});

딥 모드는 레포지토리 및 경로 대상을 지원합니다. diff와
작업 트리 스캔에는 표준 모드를 사용하세요. 선택적 설정으로 동시에 독립적으로 실행되는
표준 스캔 워커 수, 워커당 하위 에이전트 수, 새 보안 이슈 없이 연속으로 완료된 워커 스캔 횟수,
워커의 총 실행 횟수 및 실행 시간을 제어할 수 있습니다. 이러한 설정을 사용하려면
`mode: "deep"` 설정이 필요합니다.

`maxTimeHours`의 기본값은 `96`이며, `96` 이하의 양수를 지정할 수 있습니다.
시간은 소수점 단위로도 지정할 수 있습니다. 제한 시간에 도달하면 Codex Security는 완료되지 않은
워커를 중지하고 완료된 스캔 결과를 유지한 뒤 최종
보고서로 집계합니다. 시간 제한이 적용된 스캔을 전체 범위를 검토했다는 근거로 삼기 전에 `result.coverage.completeness`를
검토하세요.

### 보안 지식 베이스 추가

아키텍처 문서, 위협 모델 또는 보안 정책을
`knowledgeBasePaths`로 전달하세요:

```ts
const result = await security.run("/path/to/repository", {
  knowledgeBasePaths: [
    "/path/to/architecture.md",
    "/path/to/security-policies",
  ],
});

SDK는 파일과 디렉터리를 입력으로 받으며 디렉터리를 재귀적으로 검색합니다.
지원되는 문서 형식은 `.md`, `.markdown`, `.txt`, `.pdf`, `.docx`입니다.
SDK는 링크된 입력 경로를 거부하고 링크된 디렉터리 항목을 건너뛰며,
추출한 문서 내용을 저장된 스캔 결과에 포함하지 않습니다.

### 스캔 및 후속 작업 지침 추가

`scanPrompt`로 스캔의 초점을 지정하고 `postScanPrompt`로 후속 작업을 요청하세요:

```ts
const result = await security.run("/path/to/repository", {
  scanPrompt: "Focus on tenant isolation and authorization checks.",
  postScanPrompt: "Write confirmed findings to post-scan-summary.md.",
});

후속 작업이 실패하면 SDK는 완료된 스캔을 유지하고
`onWarning`으로 오류를 보고합니다. 후속 작업으로 변경된 완료된 스캔 아티팩트도
모두 복원합니다.

### 스캔 예산 설정

예상 모델 비용이 한도를 초과하면 스캔이 중지되도록 `maxCostUsd` 값을 설정하세요.
스캔 중 비용을 추적하려면 `onCost`를 사용하세요:

```ts
const result = await security.run("/path/to/repository", {
  maxCostUsd: 5,
  onCost(cost) {
    console.log(cost.estimatedUsd);
  },
});

console.log(result.cost?.estimatedUsd);

이 한도는 예상 지출액을 나타낼 뿐 엄격한 상한은 아니므로 이미
진행 중인 요청이 완료되면 비용이 한도를 약간 초과할 수 있습니다. 딥 스캔에서
Codex Security가 완료된 워커의 결과를 집계한 후 한도에 도달하면 `run`은
`coverage.completeness`가 `"partial"`로 설정된 결과를 반환하고 예산 경고를
`onWarning`으로 보고합니다.

스캔이 완료된 부분 결과를 생성할 수 없으면 `run`은
`ScanCostLimitExceededError`를 발생시키고 사용 가능한 출력을 보존합니다.

## 스캔 결과 활용

`ScanResult`에서 구조화된 문서, 스캔 메타데이터 및 아티팩트
경로를 확인할 수 있습니다:

| 속성             | 내용                                                                           |
| -------------------- | ---------------------------------------------------------------------------------- |
| `manifest`           | 대상, 범위, 생성 주체 및 아티팩트 레코드를 포함하는 봉인된 스캔 매니페스트. |
| `findings`           | 현재 스캔에서 발견된 보안 이슈입니다. 보안 이슈 객체는 `findings.findings`에서 읽으세요.     |
| `repositoryFindings` | 스캔 기록이 있는 경우 레포지토리의 여러 스캔에서 아직 해결되지 않은 보안 이슈.             |
| `coverage`           | 검토한 영역, 제외 항목, 보류된 작업, 미해결 질문 및 완전성.    |
| `scanDir`            | 스캔 디렉터리.                                                                |
| `threadId`           | 해당 스캔의 Codex 스레드 식별자.                                          |
| `turnResult`         | 턴 상태, 응답 및 제공되는 사용량 메타데이터.                               |
| `cost`               | 모델 및 토큰의 예상 비용이며, 확인할 수 없으면 `null`입니다.                        |
| `reportPath`         | `report.md`의 경로.                                                           |
| `manifestPath`       | `scan-manifest.json`의 경로.                                                  |
| `findingsPath`       | `findings.json`의 경로.                                                       |
| `coveragePath`       | `coverage.json`의 경로.                                                       |
| `artifactsDir`       | supporting-artifacts 디렉터리.                                                |
| `sarifPath`          | 생성된 SARIF 경로이며, SARIF가 없으면 `null`입니다.                          |
| `pluginVersion`      | 스캔 생성 주체가 기록한 버전.                                         |

이후 스캔에서도 동일한 플러그인을 사용해야 한다면
`expectedPluginVersion: result.pluginVersion`을 전달하세요. 설치된 플러그인 버전이 다르면
SDK가 스캔을 거부합니다.

구조화된 보안 이슈와 검사 범위를 직접 사용하세요:

```ts
for (const finding of result.findings.findings) {
  const location = finding.locations[0];
  if (location === undefined) continue;

  console.log(
    finding.severity.level,
    `${location.path}:${location.startLine}`,
    finding.title
  );
}

for (const deferred of result.coverage.deferred) {
  console.log(deferred.id, deferred.reason);
}

보안 이슈에는 `codeEvidence`, `rootCause`, `validation`,
`attackPath`, `remediationTests`, `preventiveControls` 등의 선택적 필드가 포함될 수 있습니다.

레포지토리 전체의 보안 이슈를 확인할 때 `confirmedInLatestScan`은 최신 스캔에서 발견된 보안 이슈와
미해결 상태로 남아 있는 이전 보안 이슈를 구분합니다:

```ts
for (const finding of result.repositoryFindings ?? []) {
  console.log(finding.title, finding.confirmedInLatestScan);
}

검사 범위의 완전성은 `complete`, `partial`, `unknown` 중 하나입니다. 보안 관련 의사 결정의 근거로
스캔 결과를 사용하기 전에 검토가 보류된 영역, 제외 대상,
미해결 질문을 확인하세요.

`result.toJSON()`은 매니페스트, 레포지토리 및 현재 스캔의 보안 이슈,
검사 범위, 스캔 및 스레드 식별자, `reportPath`, `artifactsDir`,
`sarifPath`, 비용, 턴 메타데이터를 JSON으로 바로 변환할 수 있는 하나의 객체에 담아 반환합니다.

## 스캔 추적 또는 취소

`ScanOptions` 콜백을 전달해 스캔 시작, 워커 진행 상황 및
연결 재시도를 보고하세요:

```ts
const result = await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  onScanStarted() {
    console.log("Scan started");
  },
  onProgress(progress) {
    console.log(progress.phase, progress.filesCompleted, progress.filesTotal);
  },
  onWorkerStatus(status) {
    console.log(status.kind, status);
  },
  onSessionEvent(session) {
    console.log(session.threadId, session.worker, session.event["type"]);
  },
  onReconnect(attempt, maxAttempts) {
    console.log(`Reconnect attempt ${attempt} of ${maxAttempts}`);
  },
  onObserverError(observer, error) {
    console.error(`${observer} failed`, error);
  },
});

console.log(result.reportPath);

요청, 작업 컨트롤러 또는 타임아웃으로 취소되는 경우 `AbortSignal`을
전달하세요:

```ts

const controller = new AbortController();

try {
  const scan = security.run("/path/to/repository", {
    outputDir: "/path/outside/repository/results",
    signal: controller.signal,
  });

  controller.abort();
  await scan;
} catch (error) {
  if (error instanceof ScanInterruptedError) {
    console.error(error.scanDir);
  } else {
    throw error;
  }
}

스캔이 중단되면 `scanDir`에 부분 출력이 남을 수 있습니다. 결과를 조사해야 한다면
해당 디렉터리를 보존하세요.

스캔 설정 진행 상황을 표시하는 애플리케이션에서는 `ScanOptions`의
수명 주기 콜백도 사용할 수 있습니다:

| 콜백                            | 호출 시점                                          |
| ----------------------------------- | ---------------------------------------------------- |
| `onAuthentication(authentication)`  | 스캔이 인증 방식을 선택할 때.          |
| `onOutputArchived(archiveDir)`      | 기존 결과가 아카이브 디렉터리로 이동될 때.      |
| `onOutputDirReady(scanDir)`         | 비공개 스캔 디렉터리가 준비될 때.                 |
| `onScanStarted()`                   | 스캔 설정이 완료되고 실행이 시작될 때.           |
| `onTrustedAccessStatus(status)`     | Trusted Access 상태를 확인할 수 있게 될 때.             |
| `onReconnect(attempt, maxAttempts)` | SDK가 연결이 끊긴 스캔 스트림의 연결을 재시도할 때.          |
| `onActivity(activity)`              | 명령어, 도구, 추론 단계 또는 메시지가 업데이트될 때. |
| `onProgress(progress)`              | 스캔 단계 또는 검토한 파일 수가 변경될 때.       |
| `onWorkerStatus(status)`            | 워커의 사전 점검 또는 작업 배정 상태가 변경될 때.         |
| `onSessionEvent(session)`           | 스캔 또는 워커 세션에서 이벤트가 발생할 때.             |
| `onCost(cost)`                      | 업데이트된 예상 스캔 비용을 확인할 수 있게 될 때.         |
| `onWarning(warning)`                | 스캔에서 경고를 보고할 때.                          |
| `onObserverError(observer, error)`  | 다른 스캔 수명 주기 콜백에서 오류가 발생할 때.     |

Trusted Access 상태는 `granted`, `not_granted`, `unknown` 중 하나입니다. 액세스 권한이 없거나
상태를 알 수 없는 경우에도 `onWarning` 콜백이 호출됩니다.

`onSessionEvent` 콜백은 마스킹되지 않은 이벤트를 수신하며, 이러한 이벤트에는 소스
코드나 자격 증명이 포함될 수 있습니다. 공유 로그나 다른
서비스로 전송하기 전에 이벤트를 필터링하세요.

## 런타임 및 자격 증명 구성

특정 플러그인, 인터프리터 또는
Codex 설정이 필요한 경우 런타임 구성을 전달하세요:

```ts
const security = new CodexSecurity({
  pluginPath: "/path/to/codex-security-plugin",
  pythonPath: "/path/to/python",
  codexOverrides: {
    model: "gpt-5.6-terra",
    model_reasoning_effort: "high",
  },
});

`pluginPath`에는 플러그인 디렉터리나 ZIP을 지정할 수 있습니다. `pythonPath`는
플러그인 인터프리터를 선택합니다. `codexOverrides`는 지원되는 값을 격리된
Codex 구성에 병합합니다. 스캔에는 기본적으로 추론 수준을 매우 높게 설정한 `gpt-5.6-sol` 모델이
사용됩니다. 다른 모델이나 추론 수준을 사용하려면 `model`과 `model_reasoning_effort`를 `codexOverrides`에서
설정하세요. [Amazon
Bedrock](/ko-KR/codex/security/cli/reference#use-amazon-bedrock)을 사용하려면
`model_provider`와 `model`을 `codexOverrides`에서 설정하세요.

`codexOverrides`로는 스캔의 파일 시스템 접근을 제한하거나
승인 정책을 변경할 수 없습니다. [로컬 스캔
권한](/ko-KR/codex/security/cli/reference#local-scan-permissions)을 참조하세요.

OpenRouter 또는 Fireworks를 사용하는 경우 해당 API 키를 추가로 제공하고,
`codexOverrides`에 프로바이더 구성을 빠짐없이 지정하세요. 예를 들어
`OPENROUTER_API_KEY`를 설정하고 OpenRouter를 구성하세요:

```ts
const security = new CodexSecurity({
  codexOverrides: {
    model: "anthropic/claude-sonnet-4.5",
    model_provider: "openrouter",
    model_providers: {
      openrouter: {
        name: "OpenRouter",
        base_url: "https://openrouter.ai/api/v1",
        env_key: "OPENROUTER_API_KEY",
        wire_api: "responses",
      },
    },
  },
});

Fireworks를 사용하는 경우 두 `openrouter` 키를 모두 `fireworks`로 변경하고, `name`을
`Fireworks AI`로, `env_key`를 `FIREWORKS_API_KEY`로 설정하세요. 또한
`https://api.fireworks.ai/inference/v1`을 `base_url`로 사용하고 Fireworks
모델을 선택하세요.

클라이언트는 지원되는 인증 메서드도 제공합니다:

| 메서드                     | 용도                                                     |
| -------------------------- | ----------------------------------------------------------- |
| `loginApiKey(apiKey)`      | API 키로 격리된 런타임을 인증합니다.          |
| `loginChatGPT()`           | 브라우저 로그인 플로우를 시작하고 로그인 핸들을 반환합니다.     |
| `loginChatGPTDeviceCode()` | 기기 코드 로그인 플로우를 시작하고 로그인 핸들을 반환합니다. |
| `account()`                | 현재 인증 상태를 반환합니다.                    |
| `logout()`                 | 격리된 인증 정보를 삭제합니다.                              |

로그인 핸들은 `waitForInstructions`, `authUrl`, `verificationUrl`,
`userCode`, `wait`, `cancel`을 제공하므로 애플리케이션이 선택한 로그인
플로우를 표시하고 완료할 수 있습니다. SDK는 파일 기반 Codex 로그인을 재사용할 수 있습니다. API 키는
CI 및 서버 측 자동화에 적합합니다.

API 키와 저장된 로그인 정보가 모두 있으면 SDK는 기본적으로 API
키를 사용합니다. 대신 ChatGPT 로그인을 사용하려면 스캔에서 해당 로그인을 선택하세요:

```ts
const result = await security.run("/path/to/repository", {
  auth: "chatgpt",
});

환경 API 키를 필수로 사용하려면 `auth: "api-key"`로 설정하세요. `preflight`에서도
동일한 `auth` 옵션을 사용할 수 있습니다.

## 스캔 오류 처리

애플리케이션에서 취할 수 있는 조치에 해당하는 내보낸 오류 클래스를
포착하세요:

| 오류                            | 의미                                                            |
| -------------------------------- | ------------------------------------------------------------------ |
| `AuthenticationRequiredError`    | 스캔에 지원되는 자격 증명이 필요합니다.                               |
| `ConfigurationError`             | Codex 구성이나 오버라이드가 적합하지 않습니다.                  |
| `InvalidTargetError`             | 레포지토리, 경로, 모드 또는 Git 대상이 적합하지 않습니다.           |
| `OutputDirectoryError`           | 출력 위치 또는 해당 권한이 적합하지 않습니다.             |
| `OutputInsideProtectedRootError` | 출력 디렉터리가 스캔 대상 레포지토리나 작업 트리 안에 있습니다. |
| `PluginPythonUnavailableError`   | 사용 가능한 Python 인터프리터가 없습니다.                        |
| `PluginBootstrapError`           | 플러그인 런타임을 시작하지 못했습니다.                                |
| `ScanCostLimitExceededError`     | 스캔이 예상 비용 한도를 초과했습니다.                        |
| `IncompleteScanError`            | 필수 결과를 생성하기 전에 스캔이 종료되었습니다.               |
| `ContractValidationError`        | 완료된 스캔에서 구조화된 계약 오류가 반환되었습니다.             |
| `ScanInterruptedError`           | 스캔이 중단되었으며 부분 출력이 남았을 수 있습니다. |

이어서 [CLI 빠른 시작](/ko-KR/codex/security/cli), [CI
가이드](/ko-KR/codex/security/cli/ci) 또는 [CLI
참조 자료](/ko-KR/codex/security/cli/reference)를 확인하세요.

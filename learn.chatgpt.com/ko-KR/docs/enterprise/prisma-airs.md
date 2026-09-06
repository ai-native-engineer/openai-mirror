<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/prisma-airs -->

Palo Alto Networks Prisma AIRS를 연결해 Codex 프롬프트가 모델에 도달하기 전에
보안 정책을 적용하세요. 워크스페이스 관리자는 워크스페이스별로 이 통합을
한 번만 구성하면 됩니다.

Prisma AIRS는 보안 프로필에 구성된 보호 기능을 적용할 수 있습니다. 예를 들면
데이터 손실 방지, 프롬프트 인젝션 탐지, 악성 URL
탐지 등이 있습니다.

## 시작하기 전에

다음이 필요합니다:

- Prisma AIRS 액세스가 활성화된 ChatGPT 워크스페이스. 액세스를 요청하려면 OpenAI
계정 담당 팀에 문의하세요.
- 워크스페이스 관리자 권한.
- Prisma AIRS API 키, 구성된 보안 프로필, 배포 환경용
서비스 엔드포인트.

## Prisma AIRS 연결

1. 워크스페이스 관리자 권한으로 [Codex 데이터 제어를](https://chatgpt.com/codex/cloud/settings/data)
   여세요.
2. **외부 가드레일에서** **Prisma AIRS를** 찾으세요. 이 섹션을
   사용할 수 없다면 OpenAI 계정 담당 팀에 해당 워크스페이스의 액세스 활성화를 요청하세요.
3. **API 키**, **보안 프로필** 이름 또는 ID, **엔드포인트
   URL을** 입력하세요.
4. **적용 모드와** **AIRS 실패 시** 동작을 선택하세요.
5. **연결 저장을** 선택하세요. Codex가 연결을 검증하고
   API 키를 암호화합니다.
6. **연결 테스트를** 선택해 저장된 구성을 확인하세요.
7. **Prisma AIRS 활성화를** 켜면 워크스페이스 전체에서
   프롬프트 검사가 시작됩니다.

연결을 저장해도 검사가 활성화되지는 않습니다. **Prisma AIRS
활성화도** 켜야 합니다.

## 엔드포인트 선택

Prisma AIRS 배포에 승인된 엔드포인트를 사용하세요:

| 리전        | 엔드포인트                                                 |
| ------------- | -------------------------------------------------------- |
| 미국 | `https://service.api.aisecurity.paloaltonetworks.com`    |
| 독일       | `https://service-de.api.aisecurity.paloaltonetworks.com` |
| 인도         | `https://service-in.api.aisecurity.paloaltonetworks.com` |
| 싱가포르     | `https://service-sg.api.aisecurity.paloaltonetworks.com` |

Codex는 기본적으로 미국 엔드포인트를 사용합니다. 워크스페이스의 데이터 레지던시
요건에 따라 사용할 수 있는 엔드포인트가 제한될 수 있습니다.

## 프롬프트 처리 방식 선택

**적용 모드에 따라** Prisma AIRS가 프롬프트를 플래그했을 때의 처리 방식이 결정됩니다:

- **차단**: 프롬프트가 모델에 도달하기 전에 처리를 중지합니다. 기본값입니다.
- **알림만**: 탐지 결과를 기록하고 프롬프트가 계속 처리되도록 합니다.

**AIRS 실패 시** 설정은 Prisma AIRS를 사용할 수 없거나
응답하지 않을 때 수행할 작업을 결정합니다:

- **프롬프트 허용**: 검사가 완료되지 않아도 프롬프트 처리를 계속합니다. 기본값입니다.
- **프롬프트 차단**: Prisma AIRS가 검사할 수 있을 때까지 프롬프트 처리를 중지합니다.

보안 정책상 적용 대상인 모든 프롬프트가 검사 판정을 받아야 한다면
**프롬프트 차단을** 선택하세요.

## 검사 대상 알아보기

Codex는 새로 제출된 프롬프트 텍스트를 구성된 Prisma AIRS 엔드포인트로
보내 검사합니다. 사용자가 구성된 ChatGPT 워크스페이스에 로그인하면 App, CLI,
IDE 확장, 클라우드 등 적용 대상 Codex 워크플로우에 이 검사가 적용됩니다.
Platform API 키로 인증한 세션은 대상이 아닙니다. 지정된 로그인 방식과 워크스페이스를 사용하도록 요구하려면
[로그인 방식 또는 워크스페이스 강제 적용을](/ko-KR/codex/auth#enforce-a-login-method-or-workspace)
참조하세요.

Prisma AIRS는 이 통합을 통해 어시스턴트 응답, 도구 호출, 도구 결과, 파일,
이미지를 검사하지 않습니다. Prisma AIRS가 탐지할 위협과 민감한 데이터는 구성된 보안 프로필에
따라 결정됩니다.

Codex는 API 키를 암호화하며, 저장한 후에는 다시 표시하지 않습니다. 프롬프트
검사를 활성화하기 전에 Palo Alto Networks의 데이터 처리, 보존, 레지던시 정책을
검토하세요. 이 정책은 Prisma AIRS로 전송되는 프롬프트에 적용됩니다.

## 연결 관리

[Codex 데이터 제어로](https://chatgpt.com/codex/cloud/settings/data)
돌아가 통합을 관리하세요:

- 저장된 API 키, 보안 프로필, 엔드포인트를 확인하려면 **연결 테스트를**
  선택하세요.
- 다른 설정을 변경하지 않고 저장된 키를 교체하려면 새 API 키를 입력하고
  **API 키 교체를** 선택하세요.
- 저장된 구성을 유지하면서 검사를 중지하려면 **Prisma AIRS 활성화를**
  끄세요.
- 검사를 중지하고 저장된 연결과 API 키를 삭제하려면 **연결 해제를** 선택한 후
  확인하세요.

워크스페이스 전반의 설정과 정책 관리에 관한 자세한 내용은
[관리자 배포 가이드와](/ko-KR/codex/enterprise/admin-setup)
[관리형 구성을](/ko-KR/codex/enterprise/managed-configuration) 참조하세요.

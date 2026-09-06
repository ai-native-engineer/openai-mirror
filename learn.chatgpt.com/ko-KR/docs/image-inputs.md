<!-- source: https://learn.chatgpt.com/ko-KR/docs/image-inputs -->

오류 스크린샷, 인터페이스 디자인, 아키텍처 다이어그램 또는 기존 에셋처럼 작업에
시각적 컨텍스트가 필요한 경우 프롬프트에 이미지를 추가하세요. ChatGPT가 무엇을 살펴봐야 하는지와
어떤 결과를 원하는지 설명하고, 작업 내용을 전달할 때 이미지에만
의존하지 마세요.

이미지를 컨텍스트로 포함하려면 <kbd>Shift</kbd>를 누른 채 프롬프트 Composer에 끌어다 놓으세요.
또한 ChatGPT에 시스템에 있는 이미지를 살펴보도록 요청하거나, 스크린샷 도구를 사용해 다른 앱에서 한 작업을
확인할 수도 있습니다.

ChatGPT Web Composer에 이미지를 첨부하거나 붙여 넣거나 끌어다 놓으세요. 프롬프트에서
ChatGPT가 무엇을 살펴봐야 하는지, 이미지에서 어떤 결과를 원하는지 알려 주세요.

대화형 Composer에 이미지를 붙여 넣거나 명령줄에서 하나 이상의 파일을
전달하세요:

```bash
codex -i screenshot.png "Explain this error and suggest the smallest fix"
codex --image before.png,after.png "Compare these states and list the regressions"

이미지가 여러 개인 경우 경로를 쉼표로 구분하거나 `--image`를 반복해서 사용하세요. Codex는
PNG와 JPEG를 비롯한 일반적인 이미지 형식을 지원합니다.

드롭한 이미지가 에디터로 전달되지 않고 확장 프로그램에서 처리되도록 <kbd>Shift</kbd>를 누른 채
이미지를 프롬프트 Composer에 끌어다 놓으세요.

## 이미지에 맞춰 프롬프트 작성하기

이미지에 무엇이 표시되어 있는지 설명하고, 중요한 영역을 짚은 다음, 원하는 출력과
제약 조건을 명시하세요. 이미지를 두 개 이상 첨부하는 경우 각 이미지를 구분하고 ChatGPT가
어떤 방식으로 비교해야 하는지 설명하세요.

예:

```text
Compare this checkout screen with the design. Fix spacing and typography only;
do not change behavior. Verify the result with a new screenshot.

## 용도에 맞는 이미지 기능 사용하기

ChatGPT가 시각적 참고 자료를 살펴보게 하려면 이미지 입력을 사용하세요.
ChatGPT로 이미지를 만들거나 편집하려면 [이미지 생성](/ko-KR/codex/image-generation)을
사용하세요.

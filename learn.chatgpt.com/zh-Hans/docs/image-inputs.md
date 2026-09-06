<!-- source: https://learn.chatgpt.com/zh-Hans/docs/image-inputs -->

当任务依赖视觉上下文（例如错误信息的
屏幕截图、界面设计、架构图或现有素材）时，请在提示中添加图像。请说明
您希望 ChatGPT 检查哪些内容，以及希望得到什么结果；不要仅依靠图像
来传达任务。

按住 <kbd>Shift</kbd> 的同时，将图像拖入提示编辑器，即可将其作为
上下文加入。您还可以让 ChatGPT 检查您系统中的图像，或使用
屏幕截图工具验证在另一个应用中完成的工作。

在 ChatGPT 网页版编辑器中附加或粘贴图像，也可将图像拖入其中。在提示中，
告诉 ChatGPT 要检查哪些内容，以及您希望通过图像获得什么结果。

将图像粘贴到交互式编辑器中，或通过
命令行传入一个或多个文件：

```bash
codex -i screenshot.png "Explain this error and suggest the smallest fix"
codex --image before.png,after.png "Compare these states and list the regressions"

对于多张图像，请用逗号分隔各路径，或重复指定 `--image`。Codex
支持 PNG 和 JPEG 等常见图像格式。

按住 <kbd>Shift</kbd> 的同时，将图像拖入提示编辑器，这样
扩展程序会接收此次拖放操作，而不是将其传递给编辑器。

## 围绕图像编写提示

说明图像展示的内容，指出需要关注的区域，并明确所需的输出
和约束条件。如果您附加了多张图像，请分别标识每张图像，并说明
ChatGPT 应如何比较它们。

例如：

```text
Compare this checkout screen with the design. Fix spacing and typography only;
do not change behavior. Verify the result with a new screenshot.

## 选择合适的图像功能

当您希望 ChatGPT 检查视觉参考资料时，请使用图像输入。使用
[图像生成](/zh-Hans/codex/image-generation)，即可让 ChatGPT
创建或编辑图像。

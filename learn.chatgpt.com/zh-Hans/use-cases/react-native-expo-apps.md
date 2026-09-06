<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/react-native-expo-apps -->

## 从 Expo Go 开始

当您希望 Codex 将移动应用构想变为
经过测试的 React Native 应用时，Expo 是很合适的默认选择。高效的迭代流程是先运行 `expo start`，接着使用 Expo Go
在设备上运行应用；仅当应用需要以下任一项时，才使用开发客户端或 EAS 构建：
自定义原生代码、应用商店分发，或 Expo Go 无法运行的功能。

这样可让 Codex 专注于应用工作流，而不是在第一轮
就把时间花在原生 IDE 设置、模拟器设置、预配或构建配置上。

## 使用 Expo 插件

Expo 发布了一个 [Expo 插件](https://docs.expo.dev/skills/)，可为 Codex 提供符合 Expo 惯例的指导，涵盖 Expo Router、原生 UI、表单、
导航、动画、数据获取、NativeWind 设置、Expo 模块、开发
客户端、部署、升级以及 Codex Run 操作接入。

当 Codex 构建新的 Expo 界面、添加软件包、接入 API
调用、准备开发客户端，或准备将应用发布到 TestFlight、App
Store、Play Store 或 EAS Hosting 时，请使用该插件。

当任务需要查阅最新的
Expo 文档、安装兼容的软件包、执行 EAS 构建和
工作流操作、获取屏幕截图、与模拟器交互、使用 React Native DevTools，
或获取 TestFlight 数据时，可以选择添加 [Expo MCP 服务器](https://docs.expo.dev/eas/ai/mcp/)。

## 迭代流程

1. 请 Codex 检查代码仓库，并确认这是一个新的 Expo 应用，还是一个
现有的 Expo 项目。
2. 先使用 Expo Router 和 Expo Go，并使用 `npx expo install` 添加
   Expo 软件包。
3. 请 Codex 构建一个完整的工作流，其中包括符合原生体验的导航、
加载状态、空状态和错误状态。
4. 采用当前最快的可行方式进行验证，例如在设备或
模拟器上使用 Expo Go；仅在必要时才改用开发客户端或 EAS。

## 建议的后续提示

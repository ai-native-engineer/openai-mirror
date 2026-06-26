<!-- source: https://help.openai.com/en/articles/10119604-work-with-apps-on-macos -->

# Work with Apps on macOS

ChatGPT for macOS can now work with your apps, starting with coding tools like IDEs, terminals, and Notes.

Updated: 15 days ago

These features are available on version 1.2025.057 of ChatGPT for MacOS or later.

![ChatGPT on macOS reviewing and applying an edit to Xcode to add the missing planet Earth in Planet.swift](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-edcfb8b1bdccbadf7285f7ad/00f4992227b0e9216d0a01fcc24a5260/AD_4nXcywlfzLnt13EbZoG8AEsQLGnCSTznNmYTQhhzxc-kb7UYI_1JgWf4_kG-TY0fbUdi4HkpGb1KBHbJ29Lg9kTO-e7fYShPB_g1A3F8BkoAyY8vU6ydKq5v5__jg)

ChatGPT can now read and edit content in your coding apps, bringing you smarter answers tailored to your work, and helping you stay in flow.

## Getting Started

To get started, you'll need to install ChatGPT for MacOS by visiting <https://openai.com/chatgpt/desktop/> and following the download and setup instructions. During the initial setup, locate the app in Finder, launch it, and complete the login or signup process.   
  
Please ensure the ChatGPT app is actively running in order to access the features described below.

## Enterprise & Edu users

If the steps below are not appearing for you, please contact your enterprise admin. Enterprise admins can flip the "*Allow code edits on macOS*" toggle off in their [Admin Settings](https://chatgpt.com/admin/settings) to disable this functionality, which is why it would not be appearing for some users.

## How to work with plugins

To work with your active app, just open the ChatGPT Chat Bar by pressing **Option+Space** or by clicking the ChatGPT menubar icon. You can change this access shortcut in your MacOS app by navigating to *ChatGPT -> Settings -> Keyboard* Shortcut.  
  
You can also click the **Work with Apps** button in the ChatGPT window to manually connect with apps. Currently, ChatGPT supports only common coding and text editing applications, as listed below, with more app integrations coming soon. To set this up, you’ll need to add the desired app and grant the necessary permissions or install any required extensions.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-d996c7692f63b3cd55202f65/3573b040582e758e2cd1714f0bdd1d12/AD_4nXemkHKs6yaYqpjtp_3XRBqu8__DG8PlzlvTVDEDkB1acr_NUWbDDbJ8k2Ns7qrcBxM6dxX2hlznfP874N9j1oxMprwYZGHm2gDLaPOxKKvJcKKsAQzBg2iC7WL1)

You’ll see a banner over the Chat Bar indicating which apps ChatGPT is working with, and what content ChatGPT recognizes. When you send a message, ChatGPT will include that content with your message. If you don’t see this banner, ChatGPT is not working with any of your apps and will not include any additional content with your message.  
  
Once you hit send, ChatGPT will reply using any additional content and selection included from Work with Apps. You can see what ChatGPT looked at in your chat:

![ChatGPT on macOS using the Xcode app to inspect Planet.swift with focus on lines 25–33](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-7eef36dd04f0ae20b3a88b8e/736bab2a8a933279b559e3209ab5b5a2/AD_4nXfTZS1E-Jb_rkamWat0zUDOnIFAEfJAe8T4fgIWm4eG71oTZvRk4AdwX95au6pgbZBWwjZWZTpZgSXvyTt9cjXOmDtxVrZXc60bpRkenyqMjMtmwnzIZTIQmEaS)

This content becomes part of your chat history and is saved in your account until you delete it. Once you delete a chat or delete your account, chats are deleted from our systems within 30 days, unless they have previously been de-identified and disassociated from your account, or we have to keep them for security or legal reasons. To learn more about data controls, see the Data Controls FAQ.

## Code edits

When working with IDEs, you can ask ChatGPT to edit open files directly - no copy-pasting required. When you ask for an edit, ChatGPT will generate a diff that you can review and apply, and there’s also an option to automatically apply edits. Diffs are easy to revert in the ChatGPT UI, or by using CMD+Z in your editor.

![ChatGPT macOS companion window attached to Xcode while editing Planet.swift](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-a6bbb5c18cbef842d8518fc6/12b3cd70a777ac0e9b33d430093fb466/AD_4nXfwR5Mvs7WKTO9UwZh4WNs8xUzZLL9cef-8JK7xQnKdb1spLisEPqTE0gLLWyK_YRs6y4zN-rHu7Haqk_Xlo0FTfr1gloJvPZRoFDq6_qsMKbvJEQZSz2FrWCD5)

## Advanced voice

You can use Advanced Voice mode while working with apps. Just click the wave icon in the chat bar in the main window (please note, this will require access to the microphone). When you’re in an advanced voice session, the Work With Apps button gives you control of what apps you’re working with.  
  
Please note that you can’t launch advanced voice mode from the companion window yet and voice mode doesn’t yet support code edits.

![ChatGPT macOS voice session focused on Terminal with selected lines](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-73bed3a600d22471ccaf2227/c7008a372ced1f413c505d97dd4a8591/AD_4nXc_D-7sjqQOKnWNQbx2wRzJXrD5zzPQog4_UeO4YsFKWo0j4D7glaEePvc4oMtCxGEZ5E-Qz4Dt5gjAJBEd5iml5x-aTHpCxRZ8S8zTyrmm97VqzPXR1Dbfw6_3)

## What content is included along with messages?

* When working with text editors: Apple Notes, Notion, TextEdit, Quip

* When working with code editors: Xcode, VS Code (including Code, Code Insiders, VSCodium, Cursor, Windsurf), Jetbrains (including Android Studio, IntelliJ, PyCharm, WebStorm, PHPStorm, CLion, Rider, RubyMine, AppCode, GoLand, DataGrip), TextEdit

* When working with terminals: Terminal, iTerm, Warp, Prompt

* ChatGPT includes the last 200 lines of open panes.
* If you select text in a pane, ChatGPT focuses on the selection and includes neighboring text up to a truncation limit.

You can see which of your apps on your computer are compatible by going to ChatGPT > Settings > Work with Apps > Manage Apps.

## How does it work?

Enabling ChatGPT to work with most compatible apps requires the macOS Accessibility API to query content (System Settings - Accessibility). This also means you can disable the feature for those apps by disabling Accessibility permissions for ChatGPT in settings.  
  
Enabling ChatGPT to work with VS Code requires installing a VS Code extension to  
  
query content. You can install the extension in VSCode itself (extension name is *ChatGPT – Work with Code on macOS*).  
  
You can see which of your apps on your computer are compatible, and what is required to work with each, by going to Settings > Work with Apps > Manage Apps.

## Can I disable ChatGPT from working with apps?

Yes, just flip the “Enable Work with Apps” switch in ChatGPT settings on macOS. This will fully disable the functionality and remove the icon from the prompt window.

![ChatGPT macOS setting with Work with Apps enabled](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-244a985f4a10349d225b62ba/fddfcfa4c4d17b8f9fb853186b930292/Screenshot_2025-04-28_at_14_43_04.png)

Enterprise admins can flip the "Work with Apps" toggle off in their Admin Settings to disable this functionality for workspace members.

![Workspace setting for Work with Apps with the toggle turned off](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b45994d0d77d4557b79d66e0/1dcf8903af9774af7099943378b40397/AD_4nXecl4f818LHHLJbIKP938fa7tV_bC0wPBa4TwfrySWsHH0tYXCTuYT8hLDUtRDxu3xP8r3lh9aXiXn1JMkkYaZIcl17L1tlX4HoLPj_N2eXtS4mPWroYCd67uRb)

## Will OpenAI use content included from working with apps to train its models?

Content included from working with apps is part of your account’s chat history and works in the background to provide more helpful answers. We may use the content included to improve our model performance. You have control over how your data is stored and used:

* You can easily choose whether your conversations with ChatGPT can be used to improve and train our models by toggling the “Improve the model for everyone” setting.
* If you enable [Temporary Chat](/en/articles/8914046-temporary-chat-faq), your conversations with ChatGPT will not be saved in your ChatGPT account or used for improving OpenAI’s models.
* You can access other settings and [data controls](/en/articles/7730893-data-controls-faq), such as to export your chats from ChatGPT, or delete your ChatGPT account entirely.

Please note that we do not use content sent by customers to our business offerings such as our Team and Enterprise plans to improve model performance. Please see our Enterprise Privacy page for information on how we use business data.

## What is your full list of supported apps?

* Apple Notes
* Notion
* TextEdit
* Quip
* Xcode
* Script Editor
* VS Code (including Code, Code Insiders, VSCodium, Cursor, Windsurf)
* Jetbrains (including Android Studio, IntelliJ, PyCharm, WebStorm, PHPStorm, CLion, Rider, RubyMine, AppCode, GoLand, DataGrip)
* TextEdit
* Terminal
* iTerm
* Warp
* Prompt

Note that *editing* is only available with IDEs.

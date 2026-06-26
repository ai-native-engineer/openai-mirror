<!-- source: https://help.openai.com/en/articles/9982051-using-the-chatgpt-windows-app -->

# Using the ChatGPT Windows app

Updated: 14 days ago

System Requirements: Windows 10 (x64 and arm64) version 17763.0 or higher

We are excited to introduce an early version of the ChatGPT Windows app to ChatGPT users on paid plans (Plus, Team, Edu, and Enterprise). You can download the Windows app from the [Microsoft Store](https://www.microsoft.com/store/apps/9NT1R1C2HH7J). ChatGPT users that are familiar with our experience on the web can seamlessly integrate the Windows app into anything they’re doing on their computer.  
  
Please note that a subset of features available in the macOS and web version may not be available on this early version. We plan to make these features available in our full release.

## Use ChatGPT instantly with a companion window

You can use the Companion Window to instantly ask ChatGPT anything, upload files, generate a new image, or start a new conversation.  
  
To open the companion chat, press Alt + Space when you have the ChatGPT app open. The companion window remembers the last position it was in, and resets to the bottom center of your screen when your app resets.

![ChatGPT Windows app home screen with ChatGPT 4o selected and a new chat ready](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-f152bfc58b06cae6aec445aa/027e0e4e213f44c9d6e30ed5808d028f/AD_4nXeuwWjz2X7JWEgqRiwYShbtrPIwigouy6CCscC9DIgUPEAkFIoRWBbkvBRwQTX3zjGgnahn7LyKK_Ew7Sm4nEbP3okgKun42Zf310BLDgYebn3r8GdHpd-q4Jr7)

You can clear the content in the companion window by selecting New chat at the top of the window.

![ChatGPT Windows app new chat button highlighted with New chat tooltip](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-85636866e14a69c39793728b/3818f9ca41cc953da0deff4421b688eb/AD_4nXcRKeAfAK7Quvf3JK7K_yBOkHyi9YRl2WG4x0IbvDTaOeoypsSZBOY6YD7BtUltAY3m2EoWpCrFU8CC-PUURdW1NMxaNhfbx0aIs4v4ABGUNRqI7QeYRPpp4F_y)

If you accidentally close the companion window, you can reopen it with the keyboard shortcut or continue the conversation in the main ChatGPT window by opening it from chat history on the sidebar.

![ChatGPT Windows app with the model menu open and GPT-4o selected](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-fde92bf9870c28d3a849bbd2/a07f31ae3ad9c2f72e08e7cb3e508a06/AD_4nXfk6ie-_oN6wg9kPaUHPTvh6WzBdI-1zUP4hDObwDZn5TDvmokAaWhdxDJNAee5QZ65NNARHwsewS_8F2pBKtxzNcFIy_55jzwLkKjeLnjD4TPCLe527rST_O70)

Please note that the companion window shortcut will not work if it is already registered with another Windows application. If you need to update the companion window shortcut, it is located under Settings > App > Companion window hotkey.

## Distributing access to your organization (ChatGPT Enterprise & Edu)

Because ChatGPT is distributed on the Microsoft Store, access to the Windows app will follow the policies set by your IT admin for all apps in the Store. For instance, if employees can’t download apps directly from the Store, IT admins may choose to deploy the app to their devices using MDM/MAM tools like [Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune/apps/store-apps-microsoft).

## Our Enterprise and Edu Retention Policy

Please note that by default we do not use content submitted by customers to our business offerings such as our API and ChatGPT Enterprise to improve model performance. If you have explicitly opted in to share your data with us (for example, through [feedback](/en/articles/9883556-providing-feedback-in-the-api-playground)) to improve our services, then we may use the shared data to train our models.  
  
Check out our [Enterprise Privacy page](https://openai.com/enterprise-privacy) for information on how we use business data.

## Other installation methods

IT departments managing ChatGPT Enterprise workspaces may prefer to install ChatGPT Windows app using winget.

```
winget.exe install --id=9NT1R1C2HH7J --source=msstore --accept-package-agreements --accept-source-agreements –silent
```

## Reset the windows app

If you need to reset the Windows app, follow these steps:

* Open the **Settings** app
* Go to **Apps** > **Installed Apps**
* Locate **ChatGPT**
* Click the **three-dot menu** next to it
* Select **Advanced Options**
* Click **Reset**

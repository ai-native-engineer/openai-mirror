<!-- source: https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it -->

# What is the canvas feature in ChatGPT and how do I use it?

Common questions about using the canvas feature in ChatGPT

Updated: 3 days ago

Please note that canvas is available on Web, Windows, and MacOS. Coming soon to mobile platforms (iOS, Android, mobile web).

Canvas is a new interface for working with ChatGPT on writing and coding projects that require editing and revisions.  
  
With canvas, ChatGPT can better understand the context of what you’re trying to accomplish. You can highlight specific sections to indicate exactly what you want ChatGPT to focus on. It can also give in-line feedback and suggestions with the entire project in mind.  
  
You control the project in canvas. You can directly edit text or code. You can use the shortcuts to have ChatGPT to adjust writing length, debug your code, and quickly perform other useful actions. You can also restore previous versions of your work by using the back button in canvas.

Please note that Canvas is not available with pro-series models.

## How does React/HTML rendering work?

React/HTML code is rendered in a sandbox environment, allowing you to view the output of the code. Many npm packages and JavaScript libraries will work, but previews that need to load external packages or web resources may depend on your workspace’s canvas network access settings.

## Canvas code execution and network access toggles

Please note that code execution and React/HTML rendering can result in external network requests to be made. Enterprise workspace admins can control whether canvas code execution is available for users in the workspace along with the default network access behaviors. By default, **canvas code execution** is turned *on* while **Allow canvas code to access the network** is turned *off* for enterprise workspaces but these toggles are configurable in the [Admin settings](https://chatgpt.com/admin/settings) of your workspace.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-df8eb72a39631705af566884/b5da03ed91e563e08e57ee06edf87969/Screenshot_2025-02-06_at_12_57_57_E2_80_AFPM.png)

## Accessing canvas on ChatGPT

ChatGPT may open a canvas when it grasps what you’re trying to accomplish. For example, you can ask ChatGPT to generate a piece of writing (eg. "let’s write a long essay about why a strawberry is a pseudocarp") or draft code for you (eg. “write a web server in python”) and it will respond with a canvas. You can typically expect ChatGPT to open a canvas automatically when ChatGPT generates content greater than 10 lines or detects a scenario where it would be helpful to have an interface for writing or code. Additionally, you can include “use canvas…” in your prompt to ask ChatGPT to open canvas.  
  
Responses with canvas will automatically open a window on the right-hand side that contains your requested content.  
  
You can also get started with a blank canvas with ChatGPT on web by saying things like, “open a canvas”, or “open a coding canvas”. With a blank canvas, you can work on an existing project by pasting it into the blank canvas, or by just typing in the canvas.  
  
You can also paste content into ChatGPT and instantly open it in canvas via a shortcut in the upper right corner of the composer.

![ChatGPT composer with the Open in canvas button highlighted](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-9efbb0a0218943acceef6257/58bfe9d3fd024ce6af10cf1d6bb96dd8/AD_4nXemn7RQAg1fnKOZxz1451Ir2thgda3V2zgC-77oSuRJm53mEZCS8Xa_SUiZyAYCUL47tiNRZA8-NMOXt8UmLbXC-FxNNAOIiio4zYHVlwH2eMOOqJ-lcioO1Bv5)

Additionally, the toolbox in the prompt composer also enables you to ask ChatGPT to create a new canvas in your prompt. This can also be triggered by typing a backslash (“/”) and then using the “canvas” command.

![ChatGPT composer with the tools menu open, including the Canvas option](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e523c3240998ec093178ed59/af21b8147b4930d2a8255cb30a44664b/AD_4nXfW4Gq1OvhAw_8G8uaTLi9ccM525YlVEnabijkT9uANaizDb8-nMCgvmJFmEhZXEk2I1qbC7sV0JBcQjUz1y65Cy9rOZZ_sOAvLwn3sC6r9gzL3uSRQnY_x6iMH)

## Editing your project with canvas

You can make edits with canvas by simply asking for them in the chat. Additionally, you can select part of the content by highlighting the text or use the block comment icon to select an entire paragraph block. This will open an input where you can provide guidance on what to explain or edit in the selected section.

![Canvas text selected with a comment icon to add feedback](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-a9b5776cb487e06eaa0c75f3/262ce15cb25b554b61fdfa4a16db2c77/AD_4nXdvJhiI9YzBPzG_1cUeHhvC1c_SMwtrIT9qbWmv9NdEmBPRqp8qKT9FyyOatgEec6qoWGRfMjrosZGlbwM6VSOKjuyfc2uj8B43WI_ItL4p3H3aJC_l_n00NKlY)

You can also directly edit the canvas content by clicking into the canvas and typing. Please note that only basic markdown formatting options are supported, including bold, italic, headers, bullet points, and numbered lists. We don’t currently offer more advanced formatting options in canvas.  
  
You can get targeted comment suggestions from ChatGPT by simply selecting the **Suggest edits** or **Review code** shortcuts. By clicking on the comment bubble, you can see the specific suggestion provided by ChatGPT. You can either directly edit the flagged item and close the comment, or select Apply to have ChatGPT automatically generate content to address the comment.

![Canvas suggestion card in ChatGPT offering an edit and Apply button beside highlighted text](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-8b8fc27633f57914bf42a8cc/51ab16a479d0f67aa509d8708f76d3aa/AD_4nXcpJtODAwsLJq4FuSecPnXvu3XJ0pqGQCccLOaDhMStRO9uF-0cQ9ymDaAMe6EA12ftNOw_1Bk_cCyQfmEPJInYwmDr_9Ij2BAUfWup4uqlEHsgsQsKj-ghpMxb)

When working on a writing task, you also have the option to highlight specific portions of your text or code and ask ChatGPT to either request edits to that section or ask a question about it. Formatting options can also be accessed by highlighting a piece of text. Basic markdown formatting is supported, including bold, italic, headers, bullet points, and numbered lists. We don’t currently offer more advanced formatting options in canvas.

![ChatGPT canvas text selected with inline tools for Ask ChatGPT, bold, italic, and formatting](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-f81db57573c7bfb54ca8b9f7/d53227f1a0a32fe3ccec8fecb7f36211/AD_4nXcgHNSdYtAlSz5HdfeIoDz3-tJ6UxR4ifG5tK90MSygXyzmYZHME2NfsRb45O8yC8WxFL6tEveZ5_2eGfgdDbl-u6yyrNrPazSxRtzrWw8bh8pwCl-tRCHx0LPs)

## Shortcuts on canvas for writing and coding

Canvas with ChatGPT provides access to a bundle of writing shortcuts that enable you to ask for suggested edits, adjust the length of the output, update the intended reading level, and add emojis or a final polish to your piece. To find these shortcuts, hover over the shortcuts menu on the bottom-right of the page.

![ChatGPT canvas toolbar with Suggest edits selected](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-c45a9024b1044e9080fbe87d/d3e8be924934a6d02334350ea0d25dd6/AD_4nXdtmS3_0IqTZtnDqugg984LPyeKYS6x8-ETGQSOwyOpbJVw0QpAgdoVHdXxfqt2qugF5Q2xgqG6sO4s52hq5Wt5O0EWZSn71bS9AZ_3DKxaeFpEvfrmLGWsFAFg)

For writing documents, you can use the following shortcuts:

* **Suggest edits**: ChatGPT will add inline suggestions to improve your writing.
* **Adjust the length**: shortens or expands the length of your document.
* **Change reading level**: adjusts the reading level from Kindergarten to Graduate School.
* **Add final polish**: checks for grammar, clarity, and consistency.
* **Add emojis**: replaces words with emojis or adds them for extra emphasis and color.

For coding, you can use the following shortcuts:

* **Add logs**: inserts print statements to assist with debugging and tracking execution.
* **Add comments**: adds comments to explain the code and improve readability.
* **Fix bugs**: detects and rewrites problematic code to resolve errors.
* **Port to a language**: translates your code into languages like JavaScript, Python, Java, TypeScript, C++, or PHP.
* **Code review**: provides inline suggestions to optimize and improve your code.

Some shortcuts will immediately update the contents of your project, like **Add emojis**, **Add final polish**, **Fix bugs**, and **Port to a language**.

![ChatGPT canvas open to a draft titled Strawberry Pseudocarp with editing controls in the header](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-253d493849d4be717f6a57c1/4b8966a3e0c330bc2289f05a3fc2803a/AD_4nXd2t3LkMUKgIotwt0cl56JFExE7uXbJ3Dd7QiGtXBGekc7c2TfD2iv06501SsEByGFdvkhO5BgzeiMgoiZ-1XSRo6HkZdqt3qkorgD0IxycLo7GnQM6M5l1IhGs)

Other shortcuts can be tweaked with a slider. For instance, the **Adjust the length** shortcut gives you the flexibility to select options between Shortest to Longest length. The **Reading level** shortcut enables you to adjust the reading level from Kindergarten to Graduate School.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-0473b61251e45bc1fb05dd8d/c61c01555e61a95037192469a2363bf6/AD_4nXfaJMOASqOLwuCfTrbxRrI1Phf26pecP_CsP3mhVRtDJifkKsUsyjV939MmjdNDDPa0w2UZKaMb5ZJ1PRmJ6SQN1uoEZKWVnbd68gpCotIovBGE27n30-5GennM)

## Version history and show changes

You can navigate versions of your canvas document or code by using the version history via the arrows in the top toolbar. This allows you to see previous versions as well as restore these versions if you so choose. You can also copy the contents of your project by selecting the copy button.

![Canvas toolbar undo button tooltip labeled Previous version](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-378cdacbef37fa307ee72744/d2d1c5319f7e51a72cce061adff75bf9/AD_4nXdIV5lFHJczmpbzsHhLSZjze-uogM2uTLvih6LnXUMbAl2shQc_riIRQU2ZBRM2G0UD0NP3Y6Vx_gThP1MPtKXD3vGsg2FJ1nmW1JYrJT-ptTP1SMqHlZOA2CrE)

Additionally, you can see changes between canvas versions by using the **Show changes** button at the top toolbar. This will show additions and deletions for both documents and code.

![Canvas editing an email draft with suggested text replacing a selected paragraph](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-5eda42d13735407c007242cf/d3f8711fd6cc06477f96348e4eba1e80/AD_4nXfdtCtKwrGFlnJovtNiP1F3wzyEDiFrSUGQZaQGEg8roI1J9Y-KL16_9XNL6tXEB9R7X9MbwYeOtkRTcbZ9inftHV4c0ATEdAp4nMb3s8gEfojRfHLpvtn8jIgn)

## Executing Python code with canvas

You can execute code canvas files for Python directly on your browser when you are using canvas by selecting the Execute button in your canvas. When executing Python code, the output will appear in the console at the bottom of the screen. When there are errors that appear in the console, ChatGPT will provide a suggestion about the error – click the **Fix bug** button to have ChatGPT attempt to fix it for you!

![Canvas code editor with ChatGPT suggesting a fix for a Fibonacci function exception](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e1fa1144f8c266494c4fb7e8/8d634b2be7025e294f6baebbe22c2898/AD_4nXcOfCgnYQOYo7fwLaXkb-QHVAOd5pBPxyTb-BDpjFPV_gGH_2I30mR0XJmmp45bp4KsjJr4neHROOmKsmSTqJfhRr-P9nREp2vjNkEn4mc-nZbqlWOaAIzb-MQp)

This feature is currently only available for Python code but we plan to extend access to other programming languages in the future.

## Enabling canvas for your GPT

Canvas now works with GPTs. You can enable canvas access to GPTs by enabling the canvas capability in the GPT Builder. This enables your GPT end users to open a canvas while having a chat with your GPT.

*Model compatibility:* Canvas is not supported by GPT-5.5 or later models. When Canvas is enabled for a Custom GPT, choose a recommended model that supports Canvas. Models that do not support Canvas will be unavailable while the capability is enabled.

![Capabilities menu with Canvas selected](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b6e4ad920b1dd6a82df6dd4e/bd6c210b5d360b41e50414b8f2c05a48/AD_4nXerLuu6cTEo5hWTiEeosEoERh2XDtyiPgO6EXOG2t3npyqICrVC6_ra9S4fcnQXSsB_lKrxuxIrAU4NSFVnoF1xhv8xZamjWYxDulhzorg_14EGhIVGR0MWqS29)

Please note that this capability is off for all existing GPTs and on by default for any newly created GPTs. You can modify this at any time in the GPT Builder.  
  
  
[Learn more about the GPT Builder.](/en/articles/8770868-gpt-builder)

## Sharing a canvas with others

Sharing a canvas is available for all plans including Free, Plus, Pro, Team, Enterprise, and Edu.

Users can now share a canvas asset such as rendered React/HTML code, document, or code with another user, similar to how you share a conversation. You can do this from the canvas toolbar when canvas is open.

![ChatGPT canvas open with a coding project preview reading SHARING NOW AVAILABLE](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-9e4b4ca4147bd74e1110abe7/4852915f93c7c6b6563a8eda3a93881b/canvas-sharing-short.gif)

## Downloading your canvas file

You can now export your canvas documents in multiple formats depending on the type of content. Look for the **Download** button in the top-right corner of your canvas to try it out.  
  
For general documents (like essays or blog posts), canvas supports exporting to **PDF, Markdown (.md)** and **Word (.docx)** formats.

For code-based canvases, canvas intelligently detects the language and exports it in the appropriate file extension (e.g., `.py`, `.js`, `.sql`, etc.), preserving formatting and syntax.

This feature makes it easy to archive your work, share drafts, or continue editing in external tools.

## Canvas preview does not finish loading during “Installing Packages”?

Some JS/HTML Canvas previews need the user’s browser to load external packages or other web resources before they can render. If **Allow canvas code to access the network** is turned *off*, or if browser or organization network controls block a required external domain, the preview may not finish loading.  
  
Check the browser console for errors such as Failed to fetch, Refused to connect, or Content Security Policy errors. If canvas code network access is already enabled, check whether browser, proxy, firewall, or endpoint controls are blocking the required domain.

## Canvas and web safety

Canvas can preview websites and other web content. Web content is necessarily online and has the ability to communicate with third-parties that are not OpenAI.  
  
Communication that web preview makes can be as simple as using the internet to access an image — but it can also be as dangerous as sending information you have entered or shared with ChatGPT to a third-party.  
  
ChatGPT takes the information you provide as you talk and uses it to make informed responses. In some cases, like if you paste information from the internet, or when news or search results are retrieved, ChatGPT will use other information for its responses including in code generation with canvas.  
  
When you interact with canvas web preview, ChatGPT will ask you to confirm communications with third-parties OpenAI doesn’t know about. If you confirm this communication, we allow the preview to communicate with that third-party.

<!-- source: https://help.openai.com/en/articles/12574142-chatgpt-atlas-data-controls-and-privacy -->

# ChatGPT Atlas - Data Controls and Privacy

Updated: 3 days ago

ChatGPT Atlas helps you explore the web with ChatGPT. You control what it remembers about you, how your data is used, and the privacy settings that apply while you browse. This guide explains Browser memories, data controls, and key privacy options, with quick steps to review or change each setting.

# Data controls

The Data controls page is where you decide how Atlas handles your information.  
  
To open Data controls:

1. Click the blossom logo in the top right.
2. Select **Settings**.
3. Select **Data controls**.

## Include web browsing

This setting is available when “Improve the model for everyone” is enabled. It controls whether the content you browse in ChatGPT Atlas can be used to train our models. This toggle is **off by default**. Turning it on lets us use content you browse to make ChatGPT better for everyone. Even if you opt into training, webpages that opt out of GPTBot, will not be trained on.  
  
Note, this setting is separate from the main [ChatGPT training setting](/en/articles/5722486-how-your-data-is-used-to-improve-model-performance). If you’ve enabled training for chats in your ChatGPT account, training will also be enabled for chats in Atlas. This includes website contents you’ve attached when using the Ask ChatGPT sidebar, and Browser memories (if [enabled](#h_0521d59219)) that inform your chats. (Browser memories contain facts and insights from your browsing, but not full page content. [Learn more](#h_0521d59219).)  
  
Business and Enterprise content is not used for training.  
  
How to change it:

1. Go to **Data controls** → **Improve the model for everyone → Include web browsing**

1. Choose **On** or **Off**.

This setting is independent from **Help improve browsing & search** below.

## Shared links

Shared links are view‑only links you create from ChatGPT so others can see specific content. You can review and revoke these links in one place.  
  
To manage or revoke:

1. Open **Data controls** → **Shared links**.

1. Select a link to view details.

1. Choose **Revoke** to remove access. People with the link will no longer be able to open it.

## Archived chats

Archived chats are stored outside your main chat list so you can keep your workspace tidy while preserving information. You can restore archived chats at any time.

## Archive all chats

This setting moves all of your chats to Archive in one step. Use this when you want a clean chat list but do not want to lose your history.

## Delete all chats

Permanently deletes your chat history. This does not delete Browser memories, cookies, or other data specific to Atlas. Deletion cannot be undone. If you need a copy, export your data before deleting.

## Help improve browsing & search

Enabling this allows the browser to share diagnostic logs to improve how browsing and search work. Logs can include technical details and publicly known URLs, and are used to make the experience more reliable. This toggle is **on by default**.  
  
How to change it:

1. Go to **Data controls** → **Help improve browsing & search**.

1. Choose **On** or **Off**.

## Deleting Web Browsing History

You can delete your web browsing history by opening your Settings, going to Web Browsing, and clicking on **Delete** next to **Delete history**.  
  
You can select a Time range (Last 15 min, Last hour, Last 24 hours, Last 7 Days, Last 4 weeks, and All time) and choose to delete any of the following: your Chats, Web History, Cooking & other site data, and Cached images and file. When you delete Web History, any associated Browser memories will also be deleted. Please note that changes may take some time to refresh after deletion.  
  
Sites you delete will no longer be used to streamline your browsing experience, such as by autopopulating URLs.  
  
You can also open Advanced settings to delete your Download history, Passwords and other sign-in data, Autofill form data, and Site settings.

## Browsing with Incognito

You can open a new incognito window by pressing ⌘ + Shift + N or selecting Incognito window by clicking on your profile icon on the top-right of the browser window.  
  
  
**What does Incognito do?**

* What you do in Incognito isn’t linked to your ChatGPT account, and isn’t saved in your browser history.
* ChatGPT won’t save your Incognito browsing history, cookies, site data or information entered in forms after your Incognito session ends.

Incognito doesn’t make you invisible to ChatGPT or the rest of the internet.  
  
  
**How you're visible to ChatGPT:**

* Your chats: “You’re signed out of ChatGPT, so your chats won’t be saved to your account, create Memories or use any custom instructions unless you sign yourself back in. We retain signed-out chats separate from your account for 30 days to detect and prevent abuse.”
* Your account: “If you use sites that use OpenAI services, like APIs, we might receive data about your activity.

**How you're visible to third parties:**

* Other third parties: “Your activity might also be seen by your employer, school, or your internet service provider.”

# Browser Memories

Browser memories let ChatGPT remember useful details from your web browsing to provide better responses and suggestions, while maintaining privacy and user control. Users can opt-in during setup or in *Settings > Personalization > Reference browser memories*.  
  
As you browse in Atlas, web content is summarized on our servers. We apply safety and sensitive data filters that are designed to keep out personally identifiable information (like government IDs, SSNs, bank account numbers, online credentials, account recovery content, and addresses), and private data like medical records and financial information. We block summaries altogether on certain sensitive websites (like adult sites).  
  
We use these summaries to update the browser memories that users see and control. We delete web contents right after they are summarized, and delete the privacy-filtered summaries within 7 days.  
  
For more granular controls:

* **Turn it off:** You can enable or disable them in *Settings > Personalization > Reference browser memories.*
* **View your memories:** You can always view your browser memories in *Settings > Personalization > View browser memories*.
* **Delete your history**: Deleting your web browsing history will delete associated memories.
* **Archive browser memories**: You can archive memories you don’t want referenced from *Settings > Personalization > View browser memories*.
* **Personalize ChatGPT**: Browser memories take into account your custom instructions and saved memories.
* **Enable on-device summaries**: Users on macOS 26 have the option to have web content summarized on their device, so that web contents are not sent to our servers.

Illustrative examples of possible browser memories (individual users’ experiences may differ):

* The user is collecting ideas for vegetarian fall dinner recipes, reviewing a gallery of 25+ recipes and a butternut squash and black bean enchilada recipe
* The user is interested in and planning and researching Big Sur travel using the Big Sur Chamber of Commerce, Frogmom, Veggies abroad, [alltrails.com](http://alltrails.com/) and various resort websites
* The user uses EatingWell to find dinner recipes
* The user regularly browses Song Tea & ceramics and Steepster for specialty tea shopping

# Other controls

## Page visibility

If you want to make sure ChatGPT does not see the contents of specific web pages, you can change page visibility. Click the page settings button in the address bar and choose “ChatGPT page visibility.” Pages that aren’t visible to ChatGPT are excluded from Browser memories and won’t be used to generate chat responses in ChatGPT.

## Agent logged-in/out modes

See the [agent mode page](/en/articles/12628199-using-ask-chatgpt-sidebar-and-chatgpt-agent-on-atlas#h_231f55fcdd) for information on additional controls specific to using ChatGPT agent in Atlas.

## FAQ

#### What is the difference between Browser memories, ChatGPT memories, and cookies?

Browser memories and ChatGPT memories personalize your experience, but they are separate and controlled independently. Cookies and site data are stored by websites to keep you signed in, remember site settings, or track usage. You can delete cookies without deleting your memories, and you can archive browser memories without clearing cookies.

#### Does “Help improve browsing & search” train the model?

No. That toggle shares diagnostic logs (which may include publicly known URLs) to improve browsing and search quality. Model training is controlled by **Improve the model for everyone and Include web browsing**.

#### Does Atlas save everything I read on the web?

No. If you opt in to Browser memories, ChatGPT will remember facts and insights from your browsing, but will not store complete copies of the content. You can archive Browser memories you don’t want ChatGPT to use. You can also delete them by deleting the relevant browsing history.

#### Are Browser memories the same as ChatGPT memories?

No. They are separate and controlled independently. Turning Browser memory on or off does not change ChatGPT Memory, and changes to ChatGPT Memory do not change Browser memories.

#### Who can see my memories?

Your memories are tied to your account. Other members of your workspace cannot see your memories unless you share your account or device. Admins may control whether Browser memory is available.

#### Why am I missing some settings?

Some settings are only available on [chatgpt.com](http://chatgpt.com). In Business and Enterprise workspaces, your admin may control data and privacy settings.

<!-- source: https://help.openai.com/en/articles/12627856-publishers-and-developers-faq -->

# Publishers and Developers - FAQ

Updated: 14 days ago

# Publisher FAQs

### How can I get my website to appear in ChatGPT search results in the browser?

Any public website can appear in ChatGPT search. To help ensure your content can be discovered, surfaced, and clearly cited and linked, follow these guidelines:  
  
For your site content to be included in summaries and snippets in ChatGPT, make sure you aren't blocking OAI-SearchBot. If necessary, you may need to update your robots.txt file, to ensure OAI-SearchBot has access.  
  
Note, if we obtain the URL of a disallowed page from a third-party search provider or by crawling other pages and have signals the page is relevant to a user’s query, we may surface just the link and page title in ChatGPT Atlas.  
  
If you do not want this to happen, use the [noindex meta tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots?utm_source=chatgpt.com). Note, in order for our crawler to read a meta tag, it must be allowed to crawl the relevant page(s).  
  
Publishers who allow OAI-SearchBot to access their content can track referral traffic from ChatGPT using analytics platforms such as Google Analytics. ChatGPT automatically includes the UTM parameter utm\_source=chatgpt.com in referral URLs, enabling clear tracking and analysis of inbound traffic from ChatGPT search results.

### Does ChatGPT Atlas train on my web page content?

Publishers should disallow the [GPTBot user-agent](https://openai.com/bot/) from sites and pages they wish to exclude from potential training. We respect this signal for content acquired via users’ interactions in Atlas.  
  
Note: if **users** opt-in to training, webpages that opt out of GPTBot will not be trained on.

# Developer FAQs

### What can I do to improve my website performance with ChatGPT agent in Atlas?

Making your website more accessible helps ChatGPT Agent in Atlas understand it better.  
  
ChatGPT Atlas uses ARIA tags—the same labels and roles that support screen readers—to interpret page structure and interactive elements. To improve compatibility, follow [WAI-ARIA best practices](https://www.w3.org/WAI/ARIA/apg/) by adding descriptive roles, labels, and states to interactive elements like buttons, menus, and forms. This helps ChatGPT recognize what each element does and interact with your site more accurately.

### How do apps built with the Apps SDK work in Atlas?

Apps in ChatGPT work in Atlas in the same way they might work in ChatGPT on the web. When you start a message to ChatGPT with the name of an available app, like “Spotify, make a playlist for my party this Friday,” ChatGPT can automatically surface the app in your chat and use relevant context to help. The first time you use an app, ChatGPT will prompt you to connect so you know what data may be shared with the app. We recommend testing how your apps work within the Chat sidebar to ensure they work well at smaller widths.  
  
We are also working on ways to help users more easily access apps in ChatGPT while in Atlas. For developers that are interested in deeper integrations in Atlas, we hope to share more details soon.

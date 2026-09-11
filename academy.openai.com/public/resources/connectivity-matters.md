<!-- source: https://academy.openai.com/public/resources/connectivity-matters -->

# Connectivity Matters

![Connectivity Matters](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/ChatGPT-Academy-Cover-10--1fcd0ba4-8562-4ca2-995c-45eb0b729a11-1786029124682.jpeg?fit=scale-down&width=1200)

## What every government leader needs to know about using their data with AI

August 6, 2026

![David Sperry](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/headshot-1fbc689f-a7f5-4a7b-96f0-b216e1787803-1750880534951.jpeg?fit=scale-down&width=60)

David Sperry

![Connectivity Matters](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/ChatGPT-Academy-Cover-10--1fcd0ba4-8562-4ca2-995c-45eb0b729a11-1786029124682.jpeg?fit=scale-down&width=1200)

Most governments are now aware of the transformative power of artificial intelligence for their mission and are spreading out along a spectrum of adoption depth, and measurable impact. The single largest delineator between leaders and followers in government AI adoption is connectivity or lack thereof with their enterprise data.

Governments that take advantage of  [off-the-shelf enterprise connectors and apps](https://openai.com/index/introducing-company-knowledge/) for common productivity tools such as the Microsoft 365 and Google Workspace suites of products immediately place themselves in the leading half of their peers in terms of both adoption and impact.

The purpose of this article is to provide answers to the most common questions and concerns we hear from our government customers, and what actions have allowed other customers to move ahead with their first data connections, ***while upholding security and governance expectations***.

In this post, I’ll make the case for why these enterprise connections are critical to achieving meaningful and measurable outcomes from AI adoption, then show how governments can do it responsibly.

### The impact gap between government AI leaders and followers

The most common throughline I observe with government customers who choose not to connect enterprise systems such as Microsoft 365 or Google Workspace to ChatGPT is an assumption that connection is an “all or nothing” binary decision. As a result, when my team meets with customers, we spend time walking through the  [granular controls built into ChatGPT Enterprise](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business) to meet customer requirements.

For example, a government can choose to enable Microsoft Outlook Calendar but not Microsoft Outlook Email if that helps it meet a specific requirement. Further, within the chosen connections, customer administrators have fine-grained control over both who can use the connection (user group A, but not user group B) and how the connection operates, including whether an application is read-only or can take selected write actions.

To illustrate this, here is just a selection of the fine-grained controls we offer for the Microsoft Outlook Email connection ( [full list here](https://help.openai.com/en/articles/12512241)):

*- A user can be allowed to create an email draft, but not send it*

*- A user can be allowed to create an email draft, but not add attachments*

*- A user can be allowed to look up contacts, but not change contact records*

*- An administrator can limit which Microsoft account domains employees may connect*

*- An administrator can control whether shared-mailbox access and shared-mailbox actions are available*

Within Microsoft SharePoint, we provide the ability to  [select only specific sites and folders to sync](https://help.openai.com/en/articles/12143177-sharepoint-app-in-chatgpt) with ChatGPT, which addresses another core concern from many of our customers that they “*can’t connect SharePoint because they are not confident in the permissions for every file across all of their SharePoint*.”

This functionality allows administrators to scope the connection between ChatGPT and SharePoint to the sites and folders in which they are confident in the governance and permissions. Additionally, both our SharePoint and Microsoft Teams connections can use  [Microsoft Purview sensitivity-label filters](https://help.openai.com/en/articles/20001234-microsoft-teams-app-with-admin-managed-sync-in-chatgpt/) to narrow which content is synced.

We further address specific concerns around the use of data not authorized for use with ChatGPT through our  [Compliance Platform](https://help.openai.com/en/articles/9261474-openai-compliance-platform-for-enterprise-customers). The Compliance Platform integrates with many popular data loss prevention (DLP) and security information and event management (SIEM) solutions to give security teams a scalable, programmatic way to monitor activity, investigate, and remediate policy violations through targeted deletions.

Customers can combine these controls with the DLP solutions already deployed on user devices, such as the controls on most government computers that prevent someone from uploading a document containing sensitive information to an external recipient.

These controls matter because an agency can connect the systems its employees already use without making every source or every action available to every user. Administrators can choose the apps, users, sites and folders, actions, sensitivity rules and monitoring controls that fit the agency’s requirements.

### What this changes for employees and leaders

Here are three representative examples that we see from our customers who’ve successfully unlocked the value of combining their own data with ChatGPT.

**Program Management & Analysis:** A data call or request for information (RFI) can come from leadership, an oversight body, or another program office with little warning. That often means stopping the work already underway, emailing and calling colleagues, chasing information that is already sitting at rest in Outlook, Teams, SharePoint and other approved systems.

With those systems connected to ChatGPT, one analyst can query the relevant records, bring the facts together, cite each source and send the draft around with a simple, “Confirming this looks right before I reply.” If ten people each spend two hours responding to the request, that is 20 staff hours. One analyst producing the cited first pass in an hour, then routing it for short reviews, can turn the same request into a same-day response while the rest of the team stays focused on their work.

**Procurement:** A contracting officer preparing for a procurement meeting can compare the solicitation, current purchasing policy, approved clauses, vendor proposal, CPAR’s, stored in SharePoint or Google Drive and relevant Teams discussion. ChatGPT can identify gaps, cite each source and draft the questions that need to be resolved. The officer makes the procurement decision. The officer arrives with the relevant documents, the open questions and the source for each one without manually assembling a meeting packet from each system.

**Leadership:** An agency director can ask what changed across a program, which decisions remain open and where each fact came from. ChatGPT can search the permitted program documents, relevant Teams conversations, Outlook messages and meeting information, then produce a briefing with  [l](https://help.openai.com/en/articles/12628342-company-knowledge-in-chatgpt-business-enterprise-and-edu)inks back to the original sources. The director checks the evidence and sets priorities. Instead of asking staff to assemble a briefing from four separate systems, the leader receives one that shows what changed, which decisions remain open and where each fact came from.

### What this changes for employees and leaders

Governments that adopt powerful tools like ChatGPT, but hold back from connecting their critical daily productivity systems are leaving a significant portion of the value of AI on the table. The call to action here is not to set aside your security expectations and requirements, but to work with your OpenAI account team to find the path that will enable you to truly super power your agencies critical missions.

AI allows subject experts to build powerful custom knowledge universes around themselves, connectivity controls allow them to do it safely. Governance of AI is a living discipline that changes as capabilities and features change, but also as the methods of control, discretion and accountability advance.

In another post coming soon we’ll explore what’s beyond the use of “off the shelf” connectivity to productivity systems, and dive into how our most forward leaning and transformational government leaders are connecting their highest value custom business applications such as ERP systems, data warehouses, and their cloud or on premise infrastructure with ChatGPT. If you’d like an early preview, check out  [this knowledge article](https://developers.openai.com/api/docs/mcp).

By Amanda Bullock • Sep 10th, 2026 • Views 20

[Your next chapter starts here: 5 image prompts for workforce outreach](/public/clubs/government/blogs/your-next-chapter-starts-here-5-image-prompts-for-workforce-outreach)

By Laura Keenan • Sep 9th, 2026 • Views 12

[Expanding AI Access for Public Servants](/public/clubs/government/blogs/expanding-ai-access-for-public-servants)

By Alexis Bonnell • Sep 10th, 2026 • Views 40

[Before DC wakes up: A fictional tourism campaign case study](/public/clubs/government/blogs/before-dc-wakes-up-a-fictional-tourism-campaign-case-study)

By Laura Keenan • Sep 9th, 2026 • Views 19

By Amanda Bullock • Sep 10th, 2026 • Views 20

[Expanding AI Access for Public Servants](/public/clubs/government/blogs/expanding-ai-access-for-public-servants)

By Alexis Bonnell • Sep 10th, 2026 • Views 40

[Before DC wakes up: A fictional tourism campaign case study](/public/clubs/government/blogs/before-dc-wakes-up-a-fictional-tourism-campaign-case-study)

By Laura Keenan • Sep 9th, 2026 • Views 19

[Your next chapter starts here: 5 image prompts for workforce outreach](/public/clubs/government/blogs/your-next-chapter-starts-here-5-image-prompts-for-workforce-outreach)

By Laura Keenan • Sep 9th, 2026 • Views 12

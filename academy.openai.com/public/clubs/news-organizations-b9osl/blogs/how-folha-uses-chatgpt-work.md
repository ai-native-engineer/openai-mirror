<!-- source: https://academy.openai.com/public/clubs/news-organizations-b9osl/blogs/how-folha-uses-chatgpt-work -->

[Communities](/public/clubs)

[News Organizations](/public/clubs/news-organizations-b9osl/overview)

[Content](/public/clubs/news-organizations-b9osl/content)

Article

October 8, 2026

# How Folha built a better way to manage back-office workflows with ChatGPT Work

![How Folha built a better way to manage back-office workflows with ChatGPT Work](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Screenshot-2026-10-07-at-4-56-44-PM-082d8845-650d-4070-95c5-7a641733c8f7-1791406625001.jpeg?fit=scale-down&width=1200)

# ChatGPT for Work

# News

# News

# News Organizations

# Use Cases

# LATAM

## An IT manager with no professional software development experience used her knowledge of Folha’s business processes to build a corporate travel tool, now approved and in final testing.

![How Folha built a better way to manage back-office workflows with ChatGPT Work](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Screenshot-2026-10-07-at-4-56-44-PM-082d8845-650d-4070-95c5-7a641733c8f7-1791406625001.jpeg?fit=scale-down&width=1200)

Every month, Folha de S.Paulo’s expense administrator worked through a report of around 2,500 Uber rides, adding cost centers and divisions one record at a time. The next steps were just as manual: separate the records by department, email spreadsheets to managers for approval, and allocate the expenses for entry into the company’s business management system.

For **Layza G. S. Dionizio**, an Information Technology Manager at Folha, improving processes like this is part of the job. In 18 years at the organization, including 13 in leadership, her work has spanned budgets, contracts, processes, and performance indicators. She has an academic background in technology, but has never worked professionally in software development.

Having seen the processes she had already automated within Technology’s administrative function, Folha’s Controllership team approached her about mobility expenses. Along with reducing manual work, the team wanted to give managers and senior leaders a clearer view of how the company’s travel budget was being used.

Using ChatGPT Work through Folha’s Enterprise workspace, she built a working prototype in days. Her knowledge of the process guided the build, and she used everyday language to explain what the tool needed to do.

# Starting with a simple request

*“My contribution is understanding the business rules, knowing what the people using the solution need, and assessing whether the result fits the process,”* Layza says.

She began by asking ChatGPT to research Uber’s available reports using its official documentation. She also explored an API integration as a possible way to extract data in the future. To test the idea, she requested a sample file with generic data and gave ChatGPT a straightforward prompt:

*“Based on this CSV, I want to create an HTML dashboard showing the total number of rides per month and ride details, with filtering by cost center.”*

With a first version to work from, she used the structure of an actual Uber report as a reference and added requirements: managers should see only their own departments’ information and be able to approve rides individually or in bulk. Rides outside business days should be highlighted for review.

She asked for an implementation plan, refined the prototype step by step, and shared a reference dashboard to guide its layout and colors. The application grew to include summaries, approvals, imports, reports, administration, and scheduled approval requests.

# Replacing row-by-row work with an import and review

The tool changes how expense information is prepared. Relationships between employees, cost centers, and departments are registered in the platform. The administrator exports an Uber report and imports it, and the tool allocates expenses using those records.

That replaces the task of adding information to every ride with an import and review process. The administrator has a consolidated view, while managers can review their departments’ rides, identify potential discrepancies, and record approval decisions. An email scheduling module allows approval requests to be prepared in advance.

The result is fewer manual steps and a central place for information and approvals, making it easier to understand expenses by department and identify activity that needs closer review.

*“I encourage my team to use AI responsibly, with clear goals and a way to measure results. Without that, we risk building tools that no one uses,”* *s*ays João Ricardo Braz Cestari, Folha’s Director of Technology. *“**This project addresses a highly manual process involving several departments. What impressed me most was seeing someone on my administrative team, who works with budgets, use her knowledge of the business rules to build an automated tool that looks great and is easy to use.”*

# Working through the last steps

The next challenge was giving the administrator and managers access to the tool. Layza initially implemented Microsoft authentication, but publishing that version required help from infrastructure and development teams whose time was committed to other priorities.

She reworked authentication using ChatGPT’s Sites infrastructure so the administrator and managers could access the tool with their Enterprise accounts. She then published the prototype through Sites for review by senior leadership and the requesting department.

The tool has been approved and is in the final stages of refinement and functional testing with actual ride data from January through August. Testing with a director and the administrator responsible for the process will come before access expands to other managers.

The immediate benefit is clear: less manual work to separate data by department, send approval emails, and follow up on pending responses. The tool brings information and approvals into one place and allows approval requests to be scheduled. The exact time savings have not yet been measured.

The project offers a practical example for other news organizations: the knowledge needed to improve a process may already sit with the person managing it. In this case, experience with budgets, data, and business rules provided a clear way to direct ChatGPT Work and judge the results. A request from another department became an application that Folha can test, refine, and put into colleagues’ hands.

## Popular

[59:20](/public/videos/builder-bootcamp-rag-2026-09-14)

Video

[Builder Bootcamp: RAG](/public/videos/builder-bootcamp-rag-2026-09-14)

[49:00](/public/clubs/news-organizations-b9osl/videos/ai-essentials-for-journalists-2025-12-12)

Video

[AI Essentials for Journalists](/public/clubs/news-organizations-b9osl/videos/ai-essentials-for-journalists-2025-12-12)

[4:20](/public/clubs/news-organizations-b9osl/videos/skills-vs-agents-2026-07-13)

Video

[Skills vs. Agents](/public/clubs/news-organizations-b9osl/videos/skills-vs-agents-2026-07-13)

By Evan Hirsch

Dive in

## Related

Resource

[How News UK Broadcasting Uses ChatGPT Work as a Strategic Finance Partner](/public/clubs/news-organizations-b9osl/resources/how-news-uk-broadcasting-uses-chatgpt-work-as-a-strategic-finance-partner-2026-08-06)

Aug 6th, 2026 • Views 455

[53:30](/public/clubs/news-organizations-b9osl/videos/chatgpt-for-visual-storytelling-2026-09-24)

Video

[ChatGPT for Visual Storytelling](/public/clubs/news-organizations-b9osl/videos/chatgpt-for-visual-storytelling-2026-09-24)

By Tim Meko • Sep 24th, 2026 • Views 1.9K

[53:00](/public/clubs/news-organizations-b9osl/videos/building-and-scaling-ai-in-news-organizations-lessons-from-embedded-ai-fellows-2026-10-26)

Video

[Building and Scaling AI in News Organizations: Lessons from Embedded AI Fellows](/public/clubs/news-organizations-b9osl/videos/building-and-scaling-ai-in-news-organizations-lessons-from-embedded-ai-fellows-2026-10-26)

Oct 27th, 2026 • Views 86

[5:52](/public/clubs/news-organizations-b9osl/videos/chatgpt-sites-for-newsroom-scheduling-2026-10-26)

Video

[ChatGPT Sites For Newsroom Scheduling](/public/clubs/news-organizations-b9osl/videos/chatgpt-sites-for-newsroom-scheduling-2026-10-26)

By Evan Hirsch • Oct 26th, 2026 • Views 232

Resource

[How News UK Broadcasting Uses ChatGPT Work as a Strategic Finance Partner](/public/clubs/news-organizations-b9osl/resources/how-news-uk-broadcasting-uses-chatgpt-work-as-a-strategic-finance-partner-2026-08-06)

Aug 6th, 2026 • Views 455

[53:00](/public/clubs/news-organizations-b9osl/videos/building-and-scaling-ai-in-news-organizations-lessons-from-embedded-ai-fellows-2026-10-26)

Video

[Building and Scaling AI in News Organizations: Lessons from Embedded AI Fellows](/public/clubs/news-organizations-b9osl/videos/building-and-scaling-ai-in-news-organizations-lessons-from-embedded-ai-fellows-2026-10-26)

Oct 27th, 2026 • Views 86

[5:52](/public/clubs/news-organizations-b9osl/videos/chatgpt-sites-for-newsroom-scheduling-2026-10-26)

Video

[ChatGPT Sites For Newsroom Scheduling](/public/clubs/news-organizations-b9osl/videos/chatgpt-sites-for-newsroom-scheduling-2026-10-26)

By Evan Hirsch • Oct 26th, 2026 • Views 232

[53:30](/public/clubs/news-organizations-b9osl/videos/chatgpt-for-visual-storytelling-2026-09-24)

Video

[ChatGPT for Visual Storytelling](/public/clubs/news-organizations-b9osl/videos/chatgpt-for-visual-storytelling-2026-09-24)

By Tim Meko • Sep 24th, 2026 • Views 1.9K

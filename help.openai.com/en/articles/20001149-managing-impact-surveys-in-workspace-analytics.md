<!-- source: https://help.openai.com/en/articles/20001149-managing-impact-surveys-in-workspace-analytics -->

# Managing impact surveys in workspace analytics

Create, manage, and disable impact surveys in workspace analytics.

Updated: 15 days ago

# Overview

Impact surveys are in-product surveys that collect self-reported outcomes from workspace members. Responses are aggregated and displayed in the Impact section of workspace analytics to help admins understand adoption and organization-wide outcomes.  
  
For a full overview of workspace metrics and features, see: [Workspace analytics for ChatGPT Enterprise and Edu](https://help.openai.com/articles/10875114).

***Note:*** *OpenAI-created impact surveys will begin rolling out on or after* ***March 31, 2026****.* *To avoid receiving surveys, disable the* ***OpenAI-created impact surveys*** *setting before this date.*

# Survey types

## Admin-created surveys

Workspace owners can launch an admin-created survey at any time from **Workspace analytics > Impact**.  
  
Admin-created surveys:

* Allow you to choose the survey name and launch timing
* Use predefined question sets
* Do not support custom questions or answer choices

## OpenAI-created surveys

OpenAI-created surveys are automatically scheduled and appear during predefined survey windows. These surveys help measure adoption at key points in a workspace’s lifecycle.

![ChatGPT workspace impact survey banner with Take survey button above the message composer](https://images.ctfassets.net/j22is2dtoxu1/5YTYKTDV00XnsDKTpE2yD0/81caf9afee0ecc1a7c458b505b32f8f9/Screenshot_2026-03-20_at_12.38.04â__PM.png)

# Create an admin-created survey

To launch an admin-created survey:

1. Go to **Workspace analytics > Impact**.
2. Select **Push new survey**.
3. Enter a survey name.
4. Select **Create**.

Surveys are sent immediately after creation. Create the survey only when you are ready to launch it.

# Understand survey timing

OpenAI-created surveys are scheduled at specific milestones:

* **Day 120 after workspace creation** (30-day response window)
* **Day 240 after workspace creation** (30-day response window)

These timings are designed to capture impact after teams have established usage patterns, governance, and training.  
  
In some cases, a one-time catch-up survey may be issued if a workspace missed earlier survey windows.

# View survey reporting

Survey responses typically begin appearing in reporting within 1–2 days.

* Results are aggregated and shown in the **Impact** dashboard.
* Individual survey responses are not displayed.

## Export results

You can export impact survey data from workspace analytics for further analysis.  
  
For full export information, see the appendix in: [Workspace analytics in ChatGPT Enterprise and Edu](/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu#appendix-export-data-reference).

# Review survey question sets

Impact surveys use predefined question sets.

## Enterprise workspaces

Members are asked:

* "Which of the following best reflects how ChatGPT has impacted your productivity?”

* “On average, how many hours per week do you estimate ChatGPT helps you save on work-related tasks?”

Members also rate their agreement with the following statements:

* "ChatGPT has improved the quality of my work."
* "ChatGPT has increased my satisfaction at work."
* "ChatGPT has increased my ability to complete new tasks or activities."
* "ChatGPT has improved my ability to serve customers, partners, or stakeholders."

## Edu workspaces

Members are asked:

* "Which of the following best reflects how ChatGPT Edu has impacted your productivity in your work or studies?"

* "On average, how many hours per week do you estimate ChatGPT Edu helps you save on your work or studies?"

Members also rate their agreement with the following statements:

* "ChatGPT Edu improves the quality of my work or learning outputs."
* "Using ChatGPT Edu increases my satisfaction with my work or learning."
* "ChatGPT Edu helps me learn, understand, or apply new concepts."
* "ChatGPT Edu helps me think more creatively or explore new ideas."

# Disable impact surveys

## Disable an admin-created survey

1. Go to **Workspace analytics > Impact.**
2. Select the survey from the survey menu.
3. Select **Disable survey.**

## Disable OpenAI-created surveys

1. Go to **Workspace settings**.
2. Open the **General** tab.
3. Scroll to the **Workspace analytics** section.
4. Disable **Enable OpenAI-created impact surveys**.

# ChatGPT

Use a **Project**. That is the install for a personal account. Custom GPTs are still documented below for an account that can edit one.

Docs checked 16 November 2026: [Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt), [creating GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts), [GPT retirement](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq), [scheduled tasks](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt).

## Project (about five minutes)

1. In the sidebar, create a project. Name it Alfred.
2. Open the project menu (•••) → **Project settings**. Paste the whole of `chatgpt/instructions.md` into the instructions. It is under the 8,000-character cap so the same file fits a Custom GPT.
3. Upload knowledge:
   - **Free** (5 files): the five files in `knowledge-free-tier/` inside `dist/alfred-chatgpt-gpt.zip`.
   - **Plus or Go** (25), **Pro** (40), **Business, Enterprise or Edu** (40): upload every file in `knowledge/`. There are 12, which is also under the Custom GPT limit of 20.
4. Start a chat in the project. Say: **I'm doing the 7-day challenge.**

Project instructions replace your global custom instructions inside the project. Files you add are the day scripts, the skills, the templates and a fictional example. The example is not a real person.

The pictures from the course are in the zip under `images/`, for you. The day scripts already describe them in text, so they do not need to be knowledge files.

## Apps

If the account can add Google Drive, calendar, mail or Slack as a project source, connect the ones you actually use. Sign in yourself. Alfred will use a connector it can see, and ask you to paste when it cannot. It will not ask for a password.

## Scheduled briefings

You can ask ChatGPT to schedule a task, for example: **Weekdays at 07:50, run my morning briefing.**

A task created inside a Project cannot read files uploaded to that Project. Alfred is instructed to put the ritual's steps into the task itself, and to tell you that. The phrases "brief me", "heads-up" and "plan my week" work in the project chat either way.

## Custom GPT, if your account can still edit one

Personal ChatGPT accounts (Free, Go, Plus, Pro) cannot create a new GPT. An existing GPT can still be edited where the plan allows. Custom GPTs are scheduled to retire on **11 December 2026**. FedRAMP workspaces, and Enterprise workspaces with an approved deferral, are scheduled for **11 February 2027**. Follow the notice on the account. New work belongs in a Project.

If you are editing a GPT that already exists:

1. Name: **Alfred**. Description: a butler that runs the 7-day setup and then the briefing, the week and the ledgers.
2. Instructions: paste `chatgpt/instructions.md` (under 8,000 characters).
3. Knowledge: upload the 12 files in `knowledge/`. Leave the free-tier bundles out. They repeat the same text.
4. Turn on the apps the account already uses. Do not add an Action.
5. Conversation starters:
   - I'm doing the 7-day challenge.
   - Brief me.
   - Plan my week.
   - What did I promise today?

After 11 December 2026, move the same instructions and files into a Project. The pack does not depend on the GPT editor.

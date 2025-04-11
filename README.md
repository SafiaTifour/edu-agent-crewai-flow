# CrewAI Educator Flow

An intelligent agent pipeline that automates the process of researching and writing educational content using [CrewAI](https://github.com/joaomdmoura/crewai). This project orchestrates two independent but connected agent crews to first research a topic and then create polished educational content.

---

## 🧠 What It Does

This project creates a two-phase AI workflow:

1. **EduResearch Crew** – Handles research and planning.
2. **EduContentWriter Crew** – Writes, edits, and reviews educational material.

The full flow can be executed with a single command, and the final content is saved in Markdown format.

---

## 🔧 Tech Stack

- **CrewAI**: For agent and crew management
- **LLMs**: Powered by DeepSeek via OpenRouter
- **Pydantic**: For typed data handling between crews
- **crewAI-tools**: For web search with Serper.dev
- **Markdown**: Final output format

---


## 🔁 Pipeline Overview

You can visually explore the pipeline using the included [`crewai_flow.html`](./crewai_flow.html) file. It illustrates how the two crews work sequentially:

> **Generate Researched Content ➝ Generate Educational Content ➝ Save to Markdown**

Each crew contains specialized agents and tasks defined in YAML configs.

---

## 🧪 How It Works

### 1. **EduResearch Crew**
- **Researcher** agent uses Serper.dev to search the web.
- **Planner** agent organizes findings into structured educational sections.
- Outputs an `EducationalPlan` Pydantic model.

### 2. **EduContentWriter Crew**
- **Content Writer** agent drafts content per section.
- **Editor** improves clarity and flow.
- **Quality Reviewer** gives a final pass.

### 🔽 Output
The final result is saved in the `output/` directory as a Markdown file named after the topic and audience level.

---

## 🚀 Quickstart

```bash
# Clone repo and setup virtualenv
$ git clone https://github.com/SafiaTifour/edu-agent-crewai-flow.git
$ cd crewai-educator-flow

# Install dependencies
$ --requirements.txt will be added SOON!
# Create a .env file
OPENROUTER_API_KEY=your_openrouter_key
SERPER_API_KEY=your_serper_key

# Run the flow
$ crewai flow kickoff
```

---

## 🌍 Credits & Acknowledgements

- Powered by [CrewAI](https://github.com/joaomdmoura/crewai)
- LLMs via [OpenRouter](https://openrouter.ai)
- Web search via [Serper.dev](https://serper.dev)

---


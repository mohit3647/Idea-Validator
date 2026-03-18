# idea-validator-agent

An AI-powered tool that takes a raw product idea and returns a structured validation report — built for PMs who want to stress-test ideas before investing weeks of effort.

## The Problem

PMs waste weeks building products nobody wants because they skip structured validation. Most idea validation is ad-hoc: a few Slack messages, a gut feeling, maybe a Google search. There's no quick, repeatable way to get a first-pass reality check on whether an idea is worth pursuing.

## The Solution

Paste your product idea into the terminal. The agent analyzes it and returns a validation report covering: target audience, problem strength (scored 1-10), existing competitors, your unique angle, key risks, and 3 experiments you can run this week to test demand.

## Demo

```
$ python main.py

Idea Validator Agent
Paste your product idea below (then press Enter twice to submit):

An AI tool that reads customer support tickets and auto-generates a weekly product insight report for PMs

============================================================
IDEA VALIDATION REPORT
============================================================

Summary: AI-powered support ticket analyzer that generates weekly product insight reports.

Target Audience: Product managers at B2B SaaS companies (50-500 employees) who rely on support data for product decisions.

Problem Strength: 8 — PMs spend 3-5 hours/week manually reading tickets to find patterns. Most give up and miss critical signals.

Existing Solutions:
  - Productboard (manual tagging, expensive)
  - Dovetail (research-focused, not support-specific)
  - ChatGPT + copy-paste (no automation, no structure)

Unique Angle: Fully automated pipeline from ticket to insight — no tagging, no setup, just connect and read.

Key Risks:
  - Support data is messy and unstructured
  - Companies may not trust AI-generated insights for roadmap decisions
  - Integration with ticketing systems adds complexity

Validation Experiments:
  - Manually create 3 sample reports from real ticket data, share with 5 PMs, measure interest
  - Post the concept on LinkedIn and track DMs/comments
  - Build a waitlist landing page and run $50 of ads to test conversion

Verdict: Strong — Clear pain point with measurable time waste. Existing tools don't automate the full loop. Worth validating with 5 real PM conversations this week.
============================================================
```

## How to Use

### Prerequisites
- Python 3.9+
- An OpenAI API key

### Setup
```bash
git clone https://github.com/mohit3647/idea-validator-agent.git
cd idea-validator-agent
pip install -r requirements.txt
```

Create a `.env` file with your API key:
```
OPENAI_API_KEY=sk-your-key-here
```

### Run
```bash
python main.py
```

## How It Works

The agent sends your idea to GPT-4o-mini with a structured system prompt that forces a JSON response. The prompt acts as a seasoned PM advisor — it evaluates the idea across 8 dimensions (audience, problem strength, competitors, risks, etc.) and returns actionable next steps. The JSON output is parsed and pretty-printed as a readable terminal report.

## Tradeoffs and Decisions

- **Why GPT-4o-mini over GPT-4o:** For a first-pass validation, speed and cost matter more than maximum reasoning depth. GPT-4o-mini produces solid structured output at 1/10th the cost. If accuracy on competitor analysis becomes critical, upgrading is a one-line change.
- **Why terminal CLI over a web app:** The goal is to validate fast. A CLI removes all UI overhead and lets you go from idea to report in under 30 seconds. A web UI is a Week 2 improvement if there's demand.

## What I Learned

- Structured JSON output from LLMs is surprisingly reliable when you constrain the system prompt tightly — the key is specifying exact field names and types, not just describing what you want.
- The hardest part of validation isn't the analysis — it's forcing yourself to write the idea clearly enough for a machine to evaluate. The act of writing the input is itself a validation exercise.

## Next Steps

- [ ] Add support for batch validation (validate multiple ideas from a CSV)
- [ ] Export reports to Markdown or PDF
- [ ] Add a web UI with Streamlit
- [ ] Let users customize the evaluation criteria

## Built With

- Python
- OpenAI API (GPT-4o-mini)
- python-dotenv

---
Built by Mohit Pole | [LinkedIn](https://www.linkedin.com/in/mohitpole/)

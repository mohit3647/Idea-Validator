import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are an experienced product manager and startup advisor.
When given a product idea, produce a structured validation report in JSON format with these sections:

1. "summary": A one-line restatement of the idea.
2. "target_audience": Who this is for (be specific — job title, company size, context).
3. "problem_strength": Rate 1-10 how painful the problem is, with a one-line justification.
4. "existing_solutions": List 3-5 competing or alternative solutions that already exist.
5. "unique_angle": What makes this idea different from existing solutions.
6. "key_risks": List the top 3 risks that could kill this idea.
7. "validation_experiments": Suggest 3 quick experiments (under 1 week each) to test demand.
8. "verdict": One of "Strong", "Promising", or "Weak" with a 2-3 sentence explanation.

Return ONLY valid JSON. No markdown, no extra text."""


def validate_idea(idea: str) -> dict:
    """Send the idea to OpenAI and return a structured validation report."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": idea},
        ],
        temperature=0.7,
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


def print_report(report: dict):
    """Pretty-print the validation report to the terminal."""
    print("\n" + "=" * 60)
    print("IDEA VALIDATION REPORT")
    print("=" * 60)

    print(f"\nSummary: {report.get('summary', 'N/A')}")
    print(f"\nTarget Audience: {report.get('target_audience', 'N/A')}")

    strength = report.get("problem_strength", "N/A")
    print(f"\nProblem Strength: {strength}")

    print("\nExisting Solutions:")
    for solution in report.get("existing_solutions", []):
        print(f"  - {solution}")

    print(f"\nUnique Angle: {report.get('unique_angle', 'N/A')}")

    print("\nKey Risks:")
    for risk in report.get("key_risks", []):
        print(f"  - {risk}")

    print("\nValidation Experiments:")
    for exp in report.get("validation_experiments", []):
        print(f"  - {exp}")

    verdict = report.get("verdict", "N/A")
    print(f"\nVerdict: {verdict}")
    print("=" * 60 + "\n")


def main():
    import sys

    # Support both piped input and interactive mode
    if not sys.stdin.isatty():
        idea = sys.stdin.read().strip()
    else:
        print("Idea Validator Agent")
        print("Paste your product idea below (then press Enter twice to submit):\n")

        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)

        idea = "\n".join(lines)

    if not idea.strip():
        print("No idea provided. Exiting.")
        return

    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found. Create a .env file with your key.")
        print("Example: OPENAI_API_KEY=sk-...")
        return

    print("\nValidating your idea...")
    report = validate_idea(idea)
    print_report(report)


if __name__ == "__main__":
    main()

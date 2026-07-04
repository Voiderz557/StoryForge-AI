import json
import re

from src.utils.ollama import ask_ollama


def extract_json(text: str) -> dict:
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON object found")

    return json.loads(match.group(0))


def score_story(story: str) -> dict:
    prompt = f"""
You are a strict professional editor scoring a short-form story.

Return ONLY a JSON object.
No explanation.
No markdown.
No text before or after the JSON.

Use this exact format:

{{
  "hook": 1,
  "suspense": 1,
  "dialogue": 1,
  "believability": 1,
  "ending": 1,
  "retention": 1,
  "originality": 1,
  "overall": 1,
  "feedback": [
    "short improvement 1",
    "short improvement 2",
    "short improvement 3"
  ]
}}

Score each category from 1 to 10.

Story:
{story}
"""

    response = ask_ollama(prompt)

    try:
        return extract_json(response)
    except Exception:
        print("\nRAW CRITIC RESPONSE:\n")
        print(response)
        return {
            "overall": 0,
            "feedback": ["Could not parse AI response."]
        }
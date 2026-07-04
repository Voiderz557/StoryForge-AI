import json
import random
import re

from config import SAFE_CONTENT_RULES
from src.utils.ollama import ask_ollama


CATEGORIES = [
    "school mystery",
    "neighbor mystery",
    "family secret",
    "camping mystery",
    "strange phone call",
    "lost memory",
    "hotel mystery",
    "airport mystery",
    "childhood secret",
    "unexpected kindness with a twist",
]

FORBIDDEN_TWISTS = [
    "it was all a dream",
    "the narrator was dead",
    "it was me all along",
    "they were in a simulation",
    "evil twin",
    "abandoned mansion",
    "random time loop with no explanation",
]


def extract_json(text: str) -> dict:
    start = text.find("{")
    end = text.rfind("}")

    if start == -1:
        raise ValueError("No JSON object found in AI response")

    if end == -1:
        # Ollama sometimes forgets the final closing brace.
        text = text[start:].strip() + "\n}"
    else:
        text = text[start:end + 1]

    return json.loads(text)


def generate_story_plan() -> dict:
    category = random.choice(CATEGORIES)

    prompt = f"""
You are a viral short-form story producer.

Create ONE original story plan for a family-friendly YouTube Shorts story.

Category:
{category}

Safety rules:
{SAFE_CONTENT_RULES}

Avoid these overused twists:
{FORBIDDEN_TWISTS}

Return ONLY valid JSON.

Use this exact format:

{{
  "category": "...",
  "hook": "...",
  "main_character": "...",
  "setting": "...",
  "central_mystery": "...",
  "escalation_1": "...",
  "escalation_2": "...",
  "big_reveal": "...",
  "twist_ending": "...",
  "why_viewers_keep_watching": "..."
}}

Rules:
- The hook must be shocking in one sentence.
- The mystery must be understandable.
- The ending must answer the mystery.
- The twist must feel earned, not random.
- No graphic violence.
- No sexual content.
- No swearing.
- No abandoned mansions.
- No "it was me all along."
- No "it was only a dream."
"""

    response = ask_ollama(prompt, timeout=900)

    try:
        return extract_json(response)
    except Exception:
        print("\nRAW PLAN RESPONSE:\n")
        print(response)
        raise


def write_story_from_plan(plan: dict) -> str:
    prompt = f"""
You are an expert viral storyteller.

Write a complete original story based on this plan.

Story plan:
{json.dumps(plan, indent=2)}

Safety rules:
{SAFE_CONTENT_RULES}

Writing rules:
- 350 to 500 words.
- First-person narration.
- Start with the exact hook from the plan.
- Use short paragraphs.
- Add natural dialogue.
- Every paragraph must reveal something new.
- Build suspense quickly.
- The ending must clearly resolve the mystery.
- The twist must be satisfying and understandable.
- Make the story school-safe and family-friendly.
- Do not mention Reddit.
- Do not mention AI.
- Do not use headings.
- Do not explain the moral.
- Return ONLY the story.
"""

    return ask_ollama(prompt, timeout=900)


def generate_story() -> str:
    plan = generate_story_plan()
    return write_story_from_plan(plan)
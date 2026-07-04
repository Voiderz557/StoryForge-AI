from src.utils.ollama import ask_ollama


def improve_story(story: str, score: dict) -> str:
    feedback = score.get("feedback", [])

    prompt = f"""
You are a professional short-form story editor.

Rewrite the story below using the critic feedback.

Rules:
- Keep it completely SFW.
- Keep it family-friendly and school-safe.
- Keep first-person narration.
- Improve the hook.
- Increase suspense.
- Improve the ending.
- Add natural dialogue if useful.
- Do not make it longer than 500 words.
- Do not use headings.
- Do not mention AI.
- Do not explain what you changed.
- Return ONLY the rewritten story.

Critic feedback:
{feedback}

Original story:
{story}
"""

    return ask_ollama(prompt, timeout=900)
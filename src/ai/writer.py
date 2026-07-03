from config import SAFE_CONTENT_RULES
from src.utils.ollama import ask_ollama


def generate_story() -> str:
    prompt = f"""
You are an expert viral storyteller writing original short-form stories.

Write ONE completely original story.

Rules:
{SAFE_CONTENT_RULES}

Story requirements:
- 300 to 450 words.
- First-person narration.
- Starts with a shocking, emotional, or mysterious hook.
- Short paragraphs.
- Natural dialogue.
- Suspense increases every paragraph.
- Must feel believable.
- Must end with a satisfying twist.
- No headings.
- No bullet points.
- Do not mention Reddit.
- Do not mention AI.
- Do not say the story is fictional.
- Make it sound like a real person confessing something strange that happened.
- Keep the story fast-paced and do not overdescribe scenes.
"""

    return ask_ollama(prompt)
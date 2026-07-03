import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:8b"

VOICES = {
    "male_serious": "en-US-BrianNeural",
    "male_news": "en-US-ChristopherNeural",
    "male_dark": "en-US-SteffanNeural",
    "female_emotional": "en-US-AvaNeural",
    "female_story": "en-US-JennyNeural",
    "female_clear": "en-US-EmmaNeural",
    "british_male": "en-GB-RyanNeural",
    "british_female": "en-GB-SoniaNeural",
}

DEFAULT_VOICE_KEY = "male_serious"


def choose_voice_key(story: str) -> str:
    prompt = f"""
Choose the best narrator voice for this story.

Voice options:
- male_serious: serious dramatic male voice
- male_news: clear authoritative male voice
- male_dark: darker serious male voice for tense or scary stories
- female_emotional: emotional expressive female voice
- female_story: warm female storytelling voice
- female_clear: clear conversational female voice
- british_male: British male narrator voice
- british_female: British female narrator voice

Rules:
- Return only one voice key.
- Do not explain.
- Do not use punctuation.
- Choose based on the mood, narrator, and tone of the story.

Story:
{story}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=180,
    )

    response.raise_for_status()
    key = response.json()["response"].strip().lower()

    if key not in VOICES:
        return DEFAULT_VOICE_KEY

    return key


def choose_voice(story: str) -> str:
    key = choose_voice_key(story)
    return VOICES[key]
from src.utils.ollama import ask_ollama

VOICES = {
    "male_dark": "en-US-SteffanNeural",
    "male_story": "en-US-BrianNeural",
    "male_clear": "en-US-ChristopherNeural",
    "female_story": "en-US-JennyNeural",
    "female_emotional": "en-US-AvaNeural",
    "female_clear": "en-US-EmmaNeural",
    "british_male": "en-GB-RyanNeural",
    "british_female": "en-GB-SoniaNeural",
}

DEFAULT_VOICE = "en-US-BrianNeural"


def choose_voice(story: str) -> str:
    prompt = f"""
Choose the best narrator voice for this story.

Options:
male_dark
male_story
male_clear
female_story
female_emotional
female_clear
british_male
british_female

Return ONLY one option.

Story:
{story}
"""

    key = ask_ollama(prompt, timeout=300).strip().lower()
    return VOICES.get(key, DEFAULT_VOICE)
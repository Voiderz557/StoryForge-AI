import asyncio

from config import TEMP_DIR
from src.ai.producer import produce_best_story
from src.video.voice_selector import choose_voice
from src.video.voice import generate_voice


def main():
    result = produce_best_story(draft_count=3)

    story = result["final_story"]
    score = result["final_score"]

    print("\n===== FINAL STORY =====\n")
    print(story)

    print("\n===== FINAL SCORE =====\n")
    print(score)

    print("\nChoosing voice...")
    voice = choose_voice(story)
    print("Selected voice:", voice)

    print("\nGenerating voiceover...")
    audio_path = TEMP_DIR / "voice.mp3"
    asyncio.run(generate_voice(story, voice, audio_path))

    print("\nVoice saved to:")
    print(audio_path)


if __name__ == "__main__":
    main()
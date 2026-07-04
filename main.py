import asyncio

from config import TEMP_DIR
from src.ai.producer import produce_best_story
from src.video.voice_selector import choose_voice
from src.video.voice import generate_voice
from src.video.subtitles import generate_subtitles
from src.video.discussion_card import create_discussion_card
from src.video.renderer import render_video


def make_title(story: str) -> str:
    first_sentence = story.split(".")[0].strip()

    if len(first_sentence) > 75:
        return first_sentence[:72].rstrip() + "..."

    return first_sentence


def main():
    result = produce_best_story(draft_count=1)

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

    print("\nGenerating subtitles...")
    subtitles_path = TEMP_DIR / "captions.srt"
    generate_subtitles(audio_path, subtitles_path)

    print("\nGenerating discussion card...")
    card_path = TEMP_DIR / "card.png"
    title = make_title(story)
    create_discussion_card(title, card_path)

    print("\nRendering final video...")
    video_path = render_video(audio_path, subtitles_path, card_path)

    print("\nDONE.")
    print("Video saved to:", video_path)


if __name__ == "__main__":
    main()
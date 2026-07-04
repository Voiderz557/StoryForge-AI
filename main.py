from src.ai.writer import generate_story
from src.ai.critic import score_story
from src.ai.editor import improve_story


def main():
    print("Generating story...\n")
    story = generate_story()

    print("Scoring first draft...\n")
    first_score = score_story(story)

    print("FIRST SCORE:")
    print(first_score)

    if first_score.get("overall", 0) < 8:
        print("\nImproving story...\n")
        story = improve_story(story, first_score)

        print("Scoring improved draft...\n")
        final_score = score_story(story)
    else:
        final_score = first_score

    print("\n===== FINAL STORY =====\n")
    print(story)

    print("\n===== FINAL SCORE =====\n")
    print(final_score)


if __name__ == "__main__":
    main()
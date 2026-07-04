from src.ai.writer import generate_story
from src.ai.critic import score_story


def main():

    print("Generating story...\n")

    story = generate_story()

    print(story)

    print("\nScoring story...\n")

    score = score_story(story)

    print(score)


if __name__ == "__main__":
    main()
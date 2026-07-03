from src.ai.writer import generate_story


def main():
    print("Generating StoryForge story...")
    story = generate_story()

    print("\n===== STORY =====\n")
    print(story)
    print("\n===== END =====\n")


if __name__ == "__main__":
    main()
from src.ai.producer import produce_best_story


def print_section(title):
    print("\n" + "=" * 24)
    print(title)
    print("=" * 24 + "\n")


def main():
    result = produce_best_story(draft_count=3)

    print_section("DRAFT SCORES")
    for i, draft in enumerate(result["drafts"], start=1):
        print(f"Draft {i}: {draft['score'].get('overall', 0)}")
        print(draft["score"].get("feedback", []))
        print()

    print_section("FINAL SELECTED STORY")
    print(result["final_story"])

    print_section("FINAL SCORE")
    print(result["final_score"])


if __name__ == "__main__":
    main()
from src.ai.writer import generate_story
from src.ai.critic import score_story
from src.ai.editor import improve_story


def produce_best_story(draft_count: int = 3) -> dict:
    drafts = []

    for i in range(draft_count):
        print(f"\nGenerating draft {i + 1}/{draft_count}...")
        story = generate_story()

        print(f"Scoring draft {i + 1}...")
        score = score_story(story)

        drafts.append({
            "story": story,
            "score": score
        })

        print(f"Draft {i + 1} score:", score.get("overall", 0))

    best = max(drafts, key=lambda item: item["score"].get("overall", 0))

    print("\nBest first-draft score:", best["score"].get("overall", 0))

    final_story = best["story"]
    final_score = best["score"]

    if 7 <= final_score.get("overall", 0) < 8:
        print("\nImproving best story...")
        improved_story = improve_story(final_story, final_score)

        print("Scoring improved story...")
        improved_score = score_story(improved_story)

        if improved_score.get("overall", 0) > final_score.get("overall", 0):
            print("Improved version accepted.")
            final_story = improved_story
            final_score = improved_score
        else:
            print("Improved version rejected. Keeping original.")

    return {
        "drafts": drafts,
        "final_story": final_story,
        "final_score": final_score
    }
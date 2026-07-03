import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:8b"

prompt = """
You are an expert viral storyteller writing for YouTube Shorts.

Write ONE completely original fictional story.

Requirements:
- 550 to 700 words.
- Reading time around 3 to 4 minutes.
- First-person narration.
- The first sentence must immediately hook the viewer with something shocking, emotional, or impossible to ignore.
- Every paragraph must reveal new information or increase tension.
- Include realistic dialogue where it helps the story.
- Make the story feel believable, even if the situation becomes unusual.
- Build suspense continuously.
- End with a satisfying and unexpected twist.
- The ending should make viewers want to comment.
- Use short paragraphs.
- Use natural, emotional, conversational language.
- Make it sound like a real person confessing something that happened to them.

Forbidden:
- Do not use headings.
- Do not use bullet points.
- Do not summarize.
- Do not explain the moral.
- Do not mention Reddit.
- Do not mention AI.
- Do not say the story is fictional.
- Do not start with phrases like "I never thought" or "This happened last night."
"""

response = requests.post(
    OLLAMA_URL,
    json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    },
    timeout=300
)

response.raise_for_status()

story = response.json()["response"].strip()

print("\n===== GENERATED STORY =====\n")
print(story)
print("\n===== END =====\n")
import asyncio
import edge_tts

TEXT = """
My memories of that summer still feel like a bad dream.
But I know what really happened, and it's even worse than anything my imagination could conjure up.
"""

VOICE = "en-US-BrianNeural"
OUTPUT = "temp/test_voice.mp3"

async def main():
    communicate = edge_tts.Communicate(TEXT, VOICE, rate="+8%")
    await communicate.save(OUTPUT)
    print(f"Saved voice to {OUTPUT}")

asyncio.run(main())
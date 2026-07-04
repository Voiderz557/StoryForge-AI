import edge_tts
from pathlib import Path


async def generate_voice(text: str, voice: str, output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    communicate = edge_tts.Communicate(text, voice, rate="+8%")
    await communicate.save(str(output_path))
    return output_path
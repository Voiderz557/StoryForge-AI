from pathlib import Path

BASE_DIR = Path(__file__).parent

CLIPS_DIR = BASE_DIR / "clips"
OUTPUT_DIR = BASE_DIR / "output"
TEMP_DIR = BASE_DIR / "temp"
STORIES_DIR = BASE_DIR / "stories"
LOGS_DIR = BASE_DIR / "logs"

OLLAMA_MODEL = "llama3.2:3b"
OLLAMA_URL = "http://localhost:11434/api/generate"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920

DEFAULT_VOICE = "en-US-BrianNeural"

SAFE_CONTENT_RULES = """
The story must be completely SFW.
No sexual content.
No graphic violence.
No gore.
No slurs.
No drugs.
No self-harm.
No political extremism.
No excessive swearing.
Must be safe for schools, boarding schools, universities, and families.
"""
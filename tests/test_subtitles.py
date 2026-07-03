from faster_whisper import WhisperModel

AUDIO = "temp/test_voice.mp3"
OUTPUT = "temp/test_captions.srt"

def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

model = WhisperModel("base", device="cpu", compute_type="int8")
segments, info = model.transcribe(AUDIO)

with open(OUTPUT, "w", encoding="utf-8") as f:
    for i, segment in enumerate(segments, start=1):
        f.write(f"{i}\n")
        f.write(f"{format_time(segment.start)} --> {format_time(segment.end)}\n")
        f.write(f"{segment.text.strip()}\n\n")

print(f"Saved subtitles to {OUTPUT}")
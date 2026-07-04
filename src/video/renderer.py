import subprocess
from pathlib import Path
from config import CLIPS_DIR, OUTPUT_DIR


def get_duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return float(result.stdout.strip())


def render_video(audio_path: Path, subtitles_path: Path, card_path: Path) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    gameplay_path = CLIPS_DIR / "parkour.mp4"
    output_path = OUTPUT_DIR / "storyforge_output.mp4"

    duration = get_duration(audio_path)

    subtitles = str(subtitles_path).replace("\\", "/").replace(":", "\\:")
    card = str(card_path).replace("\\", "/").replace(":", "\\:")

    filter_complex = (
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,"
        "crop=1080:1920[bg];"
        "[2:v]scale=850:-1[card];"
        "[bg][card]overlay=(W-w)/2:180:enable='between(t,0,5)'[v1];"
        f"[v1]subtitles='{subtitles}':"
        "force_style='Fontname=Arial,Fontsize=18,"
        "PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
        "BorderStyle=1,Outline=2,Alignment=2,MarginV=110'[v]"
    )

    command = [
        "ffmpeg",
        "-y",
        "-stream_loop", "-1",
        "-i", str(gameplay_path),
        "-i", str(audio_path),
        "-i", str(card_path),
        "-t", str(duration),
        "-filter_complex", filter_complex,
        "-map", "[v]",
        "-map", "1:a:0",
        "-c:v", "libx264",
        "-preset", "fast",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        str(output_path),
    ]

    subprocess.run(command, check=True)
    return output_path
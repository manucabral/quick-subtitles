import subprocess
import re
import whisper
import argparse
from tqdm import tqdm


def get_video_info(file_path: str) -> str:
    command = ["ffmpeg", "-i", file_path]
    try:
        result = subprocess.run(
            command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True
        )
        return result.stderr
    except Exception as e:
        print(f"Error getting video info: {e}")
        return None


def transcribe_audio(audio_file: str, model: whisper.Whisper, language: str = None):
    result = model.transcribe(
        audio_file, verbose=True, best_of=5, fp16=False, language=language
    )
    return result["text"], result["segments"]


def save_to_srt(segments: list, srt_file: str) -> None:
    with open(srt_file, "w", encoding="utf-8") as f:
        for i, segment in enumerate(segments):
            start_time = segment["start"]
            end_time = segment["end"]
            text = segment["text"].strip()

            start_time_str = format_srt_time(start_time)
            end_time_str = format_srt_time(end_time)

            f.write(f"{i + 1}\n{start_time_str} --> {end_time_str}\n{text}\n\n")


def format_srt_time(seconds: float) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds_ms = seconds % 60
    seconds_int = int(seconds_ms)
    milliseconds = int((seconds_ms - seconds_int) * 1000)

    return f"{hours:02}:{minutes:02}:{seconds_int:02},{milliseconds:03}"


def parse_args():
    parser = argparse.ArgumentParser(description="Transcribe video files to SRT")
    parser.add_argument(
        "--model",
        default="tiny",
        help="Model to use for transcription (e.g., tiny, base, small, medium, large)",
    )
    parser.add_argument(
        "--src", required=True, help="Path to the video file to transcribe"
    )
    parser.add_argument(
        "--language",
        default=None,
        help="Language of the audio in the video (e.g., french, english, spanish...)",
    )

    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    video_file = args.src
    language = args.language
    srt_file = f"{video_file}.srt"
    model_name = args.model

    info = get_video_info(video_file)
    audio_format = re.search(r"Audio: (\w+)", info).group(1)
    print(f"Detected audio format: {audio_format}")

    output_audio_file = f"audio.{audio_format}"

    command = [
        "ffmpeg",
        "-i",
        video_file,
        "-vn",
        "-acodec",
        "copy",
        output_audio_file,
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Extrated audio: {output_audio_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error extracting audio: {e}")

    print(f"Loding model {model_name}...")
    model = whisper.load_model(model_name)
    print("Model loaded.")

    print("Transcribing audio...")
    transcript, segments = transcribe_audio(output_audio_file, model, language)

    print(f"Saving transcription to: {srt_file}")
    with tqdm(total=len(segments), desc="Saving SRT", unit="segment") as pbar:
        save_to_srt(segments, srt_file)
        pbar.update(len(segments))

    print(f"Transcription saved to: {srt_file}")
    print("Done.")

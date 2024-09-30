<h1 align="center">quick-subtitles</h1>
<p align="center">
An easy way to generate <b>SRT subtitles</b> from a <b>video</b> in Windows.
</p>


Powered by [Whisper](https://github.com/openai/whisper) and [ffmpeg](https://ffmpeg.org/)

## Usage
1. Download the [latest release](https://github.com/manucabral/quick-subtitles/releases) and extract it.
2. Place your video/episode/movie in the folder.
3. Open the terminal in the folder extracted.
4. Execute the following command:
```
quicksubtitles.exe --src video.mp4
```


### Models
To change the model, use:
```
quicksubtitles.exe --model large
```
> to see available models, [click here](https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages)

### Languages
To specify the source language, use:
```
quicksubtitles.exe --language french
```
> to see available languages, [click here](https://github.com/openai/whisper/blob/423492dda7806206abe56bdfe427c1096473a020/whisper/tokenizer.py#L10)

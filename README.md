<h1 align="center">quick-subtitles</h1>


<div align="center">
      <img src="https://img.shields.io/badge/python-3.12.7-blue" />
      <img src="https://img.shields.io/github/downloads/manucabral/quick-subtitles/total" />
      <img src="https://img.shields.io/github/license/manucabral/quick-subtitles" />
</div>

<p align="center">
An easy way to generate <b>SRT subtitles</b> from a <b>video</b> in Windows.
</p>

![Animation](https://github.com/user-attachments/assets/f19de1ee-11d9-4bbd-b0ca-54a083b66d60)

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

## Dev usage
> Note that this script was made for Python 3.12.6 version
1. Clone the repository.
```
git clone https://github.com/manucabral/quick-subtitles.git
cd quick-subtitles
```
2. Place your video, episode, or movie in the repository folder.
3. Install the requirements (I recommend using a virtual environment).
```
pip install -r requirements.txt
```
4. Download the [latest release of FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases/tag/latest) (shared version, eg: ffmpeg-master-latest-win64-lgpl-shared.zip)
5. Extract the FFmpeg zip file and copy the files from the **bin** folder into the repo folder.
7. Run main
```
main.py --src video.mp4
```

## More
- [fast-subtitles-translator](https://github.com/manucabral/fast-subtitles-translator)

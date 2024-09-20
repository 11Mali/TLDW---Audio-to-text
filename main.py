import os

from video_download import video_download
from audio_download import audio_download
from transcriber import transciber


def main():
    #Video Url
    video_url = input("Paste yt link:")

    video_file,video_title = video_download(video_url)

    audio_file = audio_download(video_file)

    transcript = transciber(audio_file)

    file_path = f"OUTPUT_PATH/{video_title}"

    with open(file_path, "w") as file:
        file.write(transcript)


    #clear tmp files
    def clean_up(files):
        for file in files:
            if os.path.exists(file):
                os.remove(file)

    clean_up([audio_file, video_file])
    return print( "output path : OUTPUT_PATH")

if __name__ == "__main__":
    main()
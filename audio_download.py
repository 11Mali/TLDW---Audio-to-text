import moviepy.editor as mp
from moviepy.editor import AudioFileClip
from pydub import AudioSegment

#process audio from video
def audio_download(video_file, output_audio="audio.wav"):
    #extract audio from video
    video_clip = AudioFileClip(video_file)
    video_clip.write_audiofile(output_audio)
    video_clip.close()
    
    #convert to mono for vosk
    audio = AudioSegment.from_file(output_audio)
    mono_audio = audio.set_channels(1)
    mono_audio.export(output_audio, format="wav")

    return output_audio
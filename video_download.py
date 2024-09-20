from pytube import YouTube
from pytube. innertube import _default_clients
#this is a fix for issues with downloading from youtube
_default_clients[ "ANDROID"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients[ "ANDROID_EMBED"][ "context"][ "client"]["clientVersion"] = "19.08.35"
_default_clients[ "IOS_EMBED"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_MUSIC"][ "context"]["client"]["clientVersion"] = "6.41"
_default_clients[ "ANDROID_MUSIC"] = _default_clients[ "ANDROID_CREATOR" ]

#download and process video
def video_download(url, output_path="videos"):
    yt = YouTube(url)
    
    #searching for the possible download
    audio_stream = yt.streams.filter(only_audio=True).first()
    
    if not audio_stream:
        raise Exception("No audio stream found for the provided video URL.")
    
    #download the video
    video_file = audio_stream.download(output_path)
    video_title = yt.streams[0].title
    return video_file, video_title

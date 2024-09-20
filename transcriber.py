#lib for transcribtion (audio-to-text)
import vosk
from vosk import Model, KaldiRecognizer
import wave
import json

#convert speech to text using Vosk
def transciber(audio_file):
    try:
        #load Vosk model from path
        model = Model("vosk-model-small-en-us-0.15") #FIXME

        #open audio file
        wf = wave.open(audio_file, "rb")
        if wf.getnchannels() != 1:
            print("Audio file must be mono channel (1 channel).")
            return ""
        
        #initialize the recognizer with the sample rate
        rec = KaldiRecognizer(model, wf.getframerate())

        #transcription result
        transcription = ""

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = rec.Result()
                transcription += json.loads(result)["text"] + " "

        #capture any remaining final transcription
        final_result = rec.FinalResult()
        transcription += json.loads(final_result)["text"]

        #return the transcription
        print("Transcription (Vosk): ", transcription[:200])  # Show first 200 
        return transcription
    except Exception as e:
        print(f"Error transcribing audio with Vosk: {e}")
        return ""



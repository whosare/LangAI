
from google.cloud import texttospeech 
import random


def main():
    quest=["¿Qué hiciste ayer?", "¿Qué es una meta que tiene?", "¿Qué harás mañana", "¿Qué comes para almuerzo?"] #list for random questions, will be upgraded later

    res=random.choice(quest) #random question is chosen
    #client
    client = texttospeech.TextToSpeechClient()
    
    #text to be said
    s_input=texttospeech.SynthesisInput(
        text=res
    )
    
    #voice
    voice = texttospeech.VoiceSelectionParams(
        language_code="es-us",
        name="es-US-Polyglot-1"
    )
    
    #audio config
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=0.75,
        pitch=0.0
    )
    
    #call API
    response = client.synthesize_speech(
        input=s_input,
        voice=voice,
        audio_config=audio_config
    )
    
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)

    print("audio content written to output.mp3")





    
    
if __name__=="__main__":
    main()


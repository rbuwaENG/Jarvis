#JARVIS
import os
import time
import pyaudio
import speech_recognition as spee
import playsound
from gtts import gTTS
import openai
import uuid

api_key = "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"
lang = 'en'

openai.api_key = api_key

guy = ""

#listen to audio
while True:
    def get_adio():
        r = spee.Recognizer()
        with spee.Microphone(device_index=1) as source:
            audio = r.listen(source)
            #STORE AUDIO IN SAID
            said = ""
            #CHECK KEY WORD IN AUDIO
            try:
                said = r.recognize_google(audio)
                print(said)
                global guy
                guy = said

                if "Jarvis" in said:
                    new_string = said.replace("Jarvis", "")
                    new_string = new_string.strip()
                    print(new_string)
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": new_string}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                    file_name = f"welcome_{str(uuid.uuid4())}.mp3"
                    speech.save(file_name)
                    playsound.playsound(file_name, block=False)

            except Exception as e:
                print(f"Exception: {str(e)}")

        return said

    if "stop" in guy:
        break

    get_adio()
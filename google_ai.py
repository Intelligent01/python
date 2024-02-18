import textwrap,colorama.ansi
import google.generativeai as genai
from playsound import playsound

import os
from gtts import gTTS

def to_markdown(text:str):
    text=text.replace('.',' *')
    return textwrap.indent(text,'> ',predicate=lambda _:True)


genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-pro')

while True:
    nput=input(f"{colorama.Fore.GREEN}ask your questions : {colorama.Fore.RESET}")
    if nput =='exit':
        break

    response=model.generate_content(nput,)
    print(response.text)
    audio=gTTS(response.text,slow=False)
    audio.save('audio.mp3')
    playsound('audio.mp3')
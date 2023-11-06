# WAP to greet a list of people using pyttsx3 [text to speech utility]

import pyttsx3

def Speek(command, speed=120, language="english"):
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)
    engine.setProperty('voice', language)
    engine.say( command )
    engine.runAndWait()

for name in ["Rahul", "Ajay", "Danish", "Harry", "Thomas", "Maria"]:
   Speek(f"Welcome {name}", 150, "czech")

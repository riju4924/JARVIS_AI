import os
from core.speaker import speak

def open_app(command):
    if "chrome" in command or "browser" in command:
        speak("Opening Google Chrome")
        os.system("start chrome")

    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "calculator" in command or "calc" in command:
        speak("Opening Calculator")
        os.system("calc")

    else:
        speak("I don't know which application to open yet.")

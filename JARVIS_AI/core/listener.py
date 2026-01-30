import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("🎧 Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"🗣 You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

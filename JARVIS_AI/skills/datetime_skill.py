import datetime
from core.speaker import speak

def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")

def tell_date():
    date = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today is {date}")

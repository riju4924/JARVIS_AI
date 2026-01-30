from ai.intent_classifier import get_intent
from skills.datetime_skill import tell_time, tell_date
from skills.system_control import open_app
from ai.llm_brain import ask_llm
from core.speaker import speak
from memory.memory_store import remember, recall

def route(command):
    command = command.lower()

    # 🧠 MEMORY: REMEMBER
    if command.startswith("remember"):
        # Example: remember my name is Riju
        try:
            parts = command.replace("remember", "").strip()
            key, value = parts.split(" is ")
            key = key.strip()
            value = value.strip()

            remember(key, value)
            speak(f"I will remember that {key} is {value}")
            return
        except:
            speak("Sorry, I could not remember that properly.")
            return

    # 🧠 MEMORY: RECALL
    if command.startswith("what is") or command.startswith("who is"):
        key = command.replace("what is", "").replace("who is", "").strip()
        value = recall(key)

        if value:
            speak(f"{key} is {value}")
            return

    # 🔁 NORMAL FLOW
    intent = get_intent(command)

    if intent == "GET_TIME":
        tell_time()

    elif intent == "GET_DATE":
        tell_date()

    elif intent == "OPEN_APP":
        open_app(command)

    elif intent == "EXIT":
        speak("Shutting down. Goodbye.")
        exit()

    else:
        answer = ask_llm(command)
        speak(answer)

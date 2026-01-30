from core.listener import listen
from core.speaker import speak
from core.command_router import route

WAKE_WORD = "jarvis"

def main():
    speak("Jarvis is now online and ready.")

    while True:
        command = listen()

        if command == "":
            continue

        if WAKE_WORD in command:
            speak("Yes?")
            command = listen()

            if command:
                route(command)

if __name__ == "__main__":
    main()

import os

from openai import OpenAI

try:
    from utils.config import OPENAI_API_KEY as CONFIG_API_KEY
except ModuleNotFoundError:
    CONFIG_API_KEY = ""

OPENAI_API_KEY = (os.getenv("OPENAI_API_KEY") or CONFIG_API_KEY).strip()

SYSTEM_PROMPT = """
You are Jarvis, a smart, calm, helpful AI assistant.
Be concise, friendly, and clear.
"""

def ask_llm(user_input: str) -> str:
    if not OPENAI_API_KEY:
        return "OpenAI API key is not configured. Set OPENAI_API_KEY before using LLM features."

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
            temperature=0.6,
        )
    except Exception as exc:
        print(f"⚠️ LLM error: {exc}")
        return "Sorry, I couldn't reach the AI service right now."

    return response.choices[0].message.content

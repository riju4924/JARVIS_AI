from openai import OpenAI
from utils.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are Jarvis, a smart, calm, helpful AI assistant.
Be concise, friendly, and clear.
"""

def ask_llm(user_input: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=0.6
    )
    return response.choices[0].message.content

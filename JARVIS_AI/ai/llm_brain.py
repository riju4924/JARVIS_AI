import logging
import os

from openai import OpenAI

try:
    from utils.config import OPENAI_API_KEY as CONFIG_API_KEY
except (ImportError, AttributeError):
    CONFIG_API_KEY = ""

def _resolve_api_key():
    env_key = os.getenv("OPENAI_API_KEY")
    if env_key and env_key.strip():
        return env_key.strip()
    if CONFIG_API_KEY and CONFIG_API_KEY.strip():
        return CONFIG_API_KEY.strip()
    return ""


OPENAI_API_KEY = _resolve_api_key()
LOGGER = logging.getLogger(__name__)
_CLIENT = None


def _get_client():
    global _CLIENT
    if _CLIENT is None:
        _CLIENT = OpenAI(api_key=OPENAI_API_KEY)
    return _CLIENT

SYSTEM_PROMPT = """
You are Jarvis, a smart, calm, helpful AI assistant.
Be concise, friendly, and clear.
"""

def ask_llm(user_input: str) -> str:
    if not OPENAI_API_KEY:
        return (
            "OpenAI API key is not configured. Set OPENAI_API_KEY in your environment "
            "or utils/config.py to use LLM features."
        )

    try:
        client = _get_client()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
            temperature=0.6,
        )
    except Exception as exc:
        LOGGER.exception("Failed to get LLM response")
        return (
            "Sorry, I couldn't get an AI response right now. "
            "Please check your API key, network connection, or logs for details."
        )

    return response.choices[0].message.content

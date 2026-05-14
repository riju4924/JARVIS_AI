import json
from pathlib import Path

MEMORY_FILE = Path(__file__).resolve().parent / "memory.json"

def load_memory():
    if not MEMORY_FILE.exists():
        return {}
    try:
        with MEMORY_FILE.open("r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_memory(memory):
    if not MEMORY_FILE.parent.exists():
        MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with MEMORY_FILE.open("w") as f:
        json.dump(memory, f, indent=4)

def remember(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)

def recall(key):
    memory = load_memory()
    return memory.get(key, None)

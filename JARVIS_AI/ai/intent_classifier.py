import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent / "intent_model.pkl"

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        "Intent model not found. Run train_intent_model.py in the ai directory to generate intent_model.pkl."
    )

model = joblib.load(MODEL_PATH)

def get_intent(command: str):
    prediction = model.predict([command])
    return prediction[0]

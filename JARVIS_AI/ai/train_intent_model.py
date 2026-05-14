from pathlib import Path

import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Training data
X = [
    "what is the time",
    "tell me the time",
    "current time please",
    "what is today's date",
    "tell me the date",
    "which day is today",
    "open chrome",
    "launch browser",
    "start notepad",
    "open calculator",
    "shutdown jarvis",
    "exit now",
    "stop jarvis"
]

y = [
    "GET_TIME",
    "GET_TIME",
    "GET_TIME",
    "GET_DATE",
    "GET_DATE",
    "GET_DATE",
    "OPEN_APP",
    "OPEN_APP",
    "OPEN_APP",
    "OPEN_APP",
    "EXIT",
    "EXIT",
    "EXIT"
]

# ML Pipeline
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

model.fit(X, y)

# Save model
MODEL_PATH = Path(__file__).resolve().parent / "intent_model.pkl"
joblib.dump(model, MODEL_PATH)

print("✅ Intent model trained and saved")

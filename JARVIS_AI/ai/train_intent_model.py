from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

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
joblib.dump(model, "ai/intent_model.pkl")

print("✅ Intent model trained and saved")

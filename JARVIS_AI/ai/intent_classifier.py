import joblib

model = joblib.load("ai/intent_model.pkl")

def get_intent(command: str):
    prediction = model.predict([command])
    return prediction[0]

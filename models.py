import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# storing model  path in a varriable
MODEL_PATH = "model/classifier.pkl"
VECTORIZER_PATH = "model/vectorizer.pkl"

# open the model
def save_model(vectorizer, model):
    os.makedirs("model", exist_ok=True)
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

# loading the model
def load_model():
    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return vectorizer, model

# predict with new data
def predict_category(email_text):
    vectorizer, model = load_model()
    X = vectorizer.transform([email_text])
    return model.predict(X)[0]

# train_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from models import save_model
from utils import mask_pii

# creating a function to train the model
def train():
    # read the csv file
    df = pd.read_csv("data/combined_emails_with_natural_pii.csv")  # columns: email_body, category
    # Go through each email row and mask any personal data and save in a new column
    df["masked_email"] = df["email"].apply(lambda x: mask_pii(x)[0])

    # creating TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # taking target and non-target column
    X = vectorizer.fit_transform(df["masked_email"])
    y = df["type"]

    # creating model as object
    model = MultinomialNB()
    # trainning the model
    model.fit(X, y)

    # saving model
    save_model(vectorizer, model)
    print("Model trained and saved successfully.")

if __name__ == "__main__":
    train()

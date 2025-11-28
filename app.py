import streamlit as st
import joblib
import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download(['stopwords','wordnet'])
stop = set(stopwords.words('english'))
lem = WordNetLemmatizer()
def clean_text(text):
    if not isinstance(text,str):
        return ""
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ',text)
    tokens = [t for t in text.split() if t not in stop and len(t) > 2]
    tokens = [lem.lemmatize(t) for t in tokens]
    return " ".join(tokens)
model = joblib.load("movie_genre_model.joblib")
st.title("🎬 Movie Genre Classifier")
st.write("Enter a movie plot and I’ll predict the genre for you!")
user_input = st.text_area("Movie Plot:")
if st.button("Predict Genre"):
    if user_input.strip() == "":
        st.warning("Please enter a movie plot.")
    else:
        cleaned = clean_text(user_input)
        prediction = model.predict([cleaned])[0]
        st.success(f"Predicted Genre: **{prediction}**")

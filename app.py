import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

import time

# Load dependencies
nltk.download('punkt')
nltk.download('stopwords')

# Initialize PorterStemmer
ps = PorterStemmer()

# Function to preprocess text
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():  # Remove special characters
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load the trained model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# 🎨 **Enhancing UI**
st.set_page_config(
    page_title="Spam Detector 🚀",
    page_icon="📩",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    h1 {
        color: #ff5733;
        text-align: center;
    }
    .stButton>button {
        background-color: #ff5733;
        color: white;
        font-size: 20px;
        border-radius: 10px;
        padding: 10px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 🌟 **Header Section**
st.markdown("<h1 style='text-align: center; color: #ff5733;'>📩 Email/SMS Spam Classifier 🚀</h1>", unsafe_allow_html=True)

# 📩 **Text Input**
input_sms = st.text_area("📨 Enter the message:", placeholder="Type or paste your email/SMS here...")

# 🔥 **Prediction Button**
if st.button("🚀 Predict Spam or Not"):
    with st.spinner("Analyzing message..."):
        time.sleep(1)

    # Step 1: Preprocess
    transformed_sms = transform_text(input_sms)
    
    # Step 2: Convert to feature vector
    vector_input = tfidf.transform([transformed_sms])
    
    # Step 3: Predict
    result = model.predict(vector_input)[0]

    # 🎯 **Display Result**
    if result == 1:
        st.markdown("<h2 style='color: red;'>⚠️ Spam Message!</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='color: green;'>✅ Not Spam</h2>", unsafe_allow_html=True)

# 📂 **Upload a file for bulk checking**
uploaded_file = st.file_uploader("📁 Upload a text file for bulk SMS/Email classification", type=["txt"])
if uploaded_file:
    file_content = uploaded_file.read().decode("utf-8")
    messages = file_content.split("\n")

    st.write("Processing messages...")
    results = []
    for msg in messages:
        if msg.strip():
            transformed_msg = transform_text(msg)
            vector_input = tfidf.transform([transformed_msg])
            result = model.predict(vector_input)[0]
            results.append((msg, "Spam" if result == 1 else "Not Spam"))

    st.write("### Results:")
    for msg, label in results:
        st.write(f"**{msg}** → `{label}`")

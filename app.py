import streamlit as st
import sklearn
import helper
import pickle
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

model = pickle.load(open("model/model.pkl", 'rb'))
vectorizer = pickle.load(open("model/Vectorizer.pkl", 'rb'))

# page configuration
st.set_page_config(page_title="Sentiment Analysis", page_icon="📝", layout="centered")

st.title("📊 Sentiment Analysis App")
st.subheader("Analyze the sentiment of your text: Positive or Negative.")

st.markdown("""
### Steps:
1. Enter your review or text in the input box below.
2. Click the **Predict** button.
3. The app will analyze the sentiment of your input and display the result.
""")

with st.sidebar:
    st.header("ℹ️ About")
    st.write("This app uses a machine learning model to predict sentiment (positive/negative) from text.")
    st.write("Built using **Streamlit**, **scikit-learn**, and **NLTK**.")

text = st.text_area("📝 Enter your review here:", placeholder="Type something...")

if st.button("🔍 Predict Sentiment"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        
        token = helper.preprocessing_step(text)
        vectorized_data = vectorizer.transform([token])
        prediction = model.predict(vectorized_data)
        
        
        if prediction[0] == 1:
            st.success("😊 Positive Sentiment")
        else:
            st.error("☹️ Negative Sentiment")

st.markdown("---")
st.markdown("Developed with ❤️ by [Abdelmseeh](https://www.linkedin.com/in/abdelmseeh-akram-347616262/)")

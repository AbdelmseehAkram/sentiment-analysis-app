# 📊 Sentiment Analysis Web App

A simple and interactive **Sentiment Analysis** web application built with **Streamlit**, **Scikit-learn**, and **NLTK**. The app predicts whether the sentiment of input text is **Positive 😊** or **Negative ☹️**.

---

## 🌟 Features

- 🔍 Predicts sentiment (positive/negative) from English text
- 🧹 Text preprocessing: tokenization, stopword removal, stemming
- 🧠 Trained with Decision Tree Classifier
- ⚡ Built using Streamlit for instant web deployment
- 📦 Uses NLTK and scikit-learn for NLP and ML

---

## 🖼️ App Interface

<p align="center">
  <img src="https://via.placeholder.com/700x400?text=App+Screenshot" alt="App Screenshot"/>
</p>

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [NLTK](https://www.nltk.org/)
- [Pandas](https://pandas.pydata.org/)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sentiment-analysis-app.git
cd sentiment-analysis-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> Or manually install:

```bash
pip install streamlit scikit-learn nltk pandas
```

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
📦 sentiment-analysis-app/
├── app.py            # Streamlit app code
├── helper.py         # Text preprocessing logic
├── model/
│   ├── model.pkl         # Trained ML model
│   └── Vectorizer.pkl    # Fitted CountVectorizer
└── README.md
```

---

## 🧠 How It Works

1. User enters a review or comment in a text box.
2. The input goes through a preprocessing function:
   - Lowercasing
   - Removing special characters
   - Tokenizing
   - Removing stopwords
   - Stemming
3. Preprocessed text is vectorized using a CountVectorizer.
4. The ML model predicts the sentiment (0 = Negative, 1 = Positive).
5. Result is shown with a message and emoji.

---

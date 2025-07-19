
This is a simple yet powerful Sentiment Analysis web application built using Streamlit, Scikit-learn, and NLTK. The app predicts whether a given piece of text (like a review or opinion) expresses positive or negative sentiment.

🌐 Live Demo
Coming soon... (You can deploy it on platforms like Streamlit Cloud or Render).

🧠 How It Works
The user enters any piece of English text.

The app preprocesses the text using NLP techniques (tokenization, stop word removal, stemming).

The preprocessed text is vectorized using a pre-trained CountVectorizer.

A trained machine learning model (Decision Tree) predicts the sentiment as Positive or Negative.

📂 Project Structure
bash
Copy
Edit
📁 sentiment-analysis-app/
│
├── app.py              # Streamlit frontend for the sentiment prediction
├── helper.py           # Preprocessing steps for text cleaning
├── model/
│   ├── model.pkl       # Trained ML model (Decision Tree Classifier)
│   └── Vectorizer.pkl  # Fitted CountVectorizer
└── README.md           # This file
🚀 Installation
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/sentiment-analysis-app.git
cd sentiment-analysis-app
2. Install dependencies
Make sure you have Python 3.7+ installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
If you don't have a requirements.txt, here are the basic libraries:

bash
Copy
Edit
pip install streamlit scikit-learn nltk pandas
3. Run the app
bash
Copy
Edit
streamlit run app.py
🛠️ Features
Clean and responsive web interface

Real-time sentiment prediction

Robust NLP preprocessing pipeline

Uses Decision Tree Classifier

Built with Streamlit for fast prototyping

📦 Preprocessing Logic
Implemented in helper.py:

Lowercasing

Removing special characters

Tokenization

Stop words removal

Stemming

🔐 Notes
Make sure the model.pkl and Vectorizer.pkl paths are valid. In production, use relative paths or cloud storage instead of absolute Windows paths like:

swift
Copy
Edit
C:/Users/dell/OneDrive/Desktop/New folder/model/model.pkl

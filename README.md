Quora Duplicate Question Pairs Detection using NLP and Feature Engineering
Objective

<img width="1873" height="814" alt="image" src="https://github.com/user-attachments/assets/3a737fe7-eb07-499c-9f20-05c762b0b4cf" />

# Quora Duplicate Question Pairs Detector

[Live Demo → Open the App](https://duplicatequestionpairs1.streamlit.app/)

The objective of this project is to build a machine learning model that can detect whether two given questions from Quora are duplicates or not. Duplicate questions are a major challenge for Quora, as multiple users often ask the same question in slightly different ways.

This project uses NLP techniques, feature engineering, and ML models to classify question pairs as Duplicate or Not Duplicate.

Description

Quora is a platform where millions of users ask and answer questions. However, many users ask the same question in different ways, which leads to:

Redundant content

Scattered answers

Poor user experience

For example:

"How can I learn machine learning?"

"What are the best ways to study machine learning?"

Both questions mean the same but are worded differently.

To solve this, we developed a model that analyzes pairs of questions and predicts whether they are duplicates.

The deployed Streamlit app allows users to enter two questions and instantly check if they are duplicates.


Dataset Information

We use the Quora Question Pairs Dataset, which contains over 400,000 question pairs.

Key Features in the Dataset:

qid1, qid2 → Question IDs

question1, question2 → The actual text of the questions

is_duplicate → Target variable (1 = Duplicate, 0 = Not Duplicate)

Additional engineered features:

Token similarity

Cosine similarity of TF-IDF vectors

Common word count

Fuzzy string matching scores

Strategic Planning

To address the problem, we followed a structured pipeline:

Import Libraries

pandas, numpy, scikit-learn, nltk, fuzzywuzzy, streamlit

Load Dataset

Import Quora dataset (CSV)

Data Preprocessing

Handle missing values

Text cleaning: lowercasing, stopword removal, punctuation removal

Tokenization & Lemmatization

Feature Engineering

Similarity-based features (cosine similarity, Jaccard similarity)

Length-based features (question length difference)

Fuzzy matching ratios

Model Training

Models tried: Logistic Regression, Random Forest, XGBoost

Evaluation using accuracy, precision, recall, F1-score

Deployment

Trained model saved as model.pkl

CountVectorizer saved as cv.pkl

Streamlit app built with input fields for two questions

Project Outcomes & Conclusion

✅ Built an ML pipeline that classifies Quora question pairs as duplicate or not.
✅ Improved feature engineering with similarity measures.
✅ Deployed a user-friendly Streamlit app for real-time predictions.
✅ Helps Quora reduce redundancy and improve user experience.

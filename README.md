Quora Duplicate Question Pairs Detection using NLP and Feature Engineering
Objective
<img width="1310" height="776" alt="image" src="https://github.com/user-attachments/assets/8efce7de-a9d5-4817-b3d1-0b7fb95e60ff" />

# Quora Duplicate Question Pairs Detector
[Live Demo → Open the App](https://duplicatequestionpairs1.streamlit.app/)

## 🎯 Objective
The objective of this project is to detect whether two given questions on **Quora** are semantically duplicate or not.  
This helps reduce redundant questions, improves search results, and enhances user experience

## 📖 Project Description  

Quora users often ask the same question in different ways:  

- *"How do I learn Python quickly?"*  
- *"What’s the fastest way to learn Python?"*  

Even though the wording differs, both mean the same.  

This project leverages **Natural Language Processing (NLP)**, **Feature Engineering**, and **Machine Learning** to identify such duplicate questions. A **Streamlit web app** makes it interactive and easy to use.  
## 📂 Dataset  

We used the **Quora Question Pairs Dataset**, which contains:  

- `qid1`, `qid2`: Question IDs  
- `question1`, `question2`: The text of the questions  
- `is_duplicate`: Target label (1 = Duplicate, 0 = Not Duplicate)  

---

## 🛠️ Workflow  

### 1️⃣ Data Preprocessing  
- Lowercasing & punctuation removal  
- Contraction expansion (`you're → you are`)  
- Stopword removal, tokenization  

### 2️⃣ Feature Engineering  
- **Token-based features**: word overlap, common word ratio  
- **Fuzzy matching features**: QRatio, PartialRatio, WRatio  
- **TF-IDF vectorization**: text embedding  

### 3️⃣ Modeling  
- Trained **LinearSVC** with tuned hyperparameters  
- Combined engineered features + TF-IDF vectors  
- Evaluated using **Accuracy, F1-score, and Confusion Matrix**  

### 4️⃣ Deployment  
- Saved trained model as `model.pkl` and vectorizer as `cv.pkl`  
- Developed **Streamlit Web App** with simple UI  
- Deployed live on Streamlit Cloud  




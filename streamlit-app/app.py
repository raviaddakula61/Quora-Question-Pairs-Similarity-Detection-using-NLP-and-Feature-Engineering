import os
import pickle
import streamlit as st
import helper

# Load model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Streamlit Page Config
st.set_page_config(
    page_title="Quora Question Pair Similarity",
    page_icon="❓",
    layout="centered"
)

# Header
st.title("🔍 Quora Question Pair Similarity Detector")
st.markdown(
    """
    This app helps you check whether two questions are **duplicate** or **not**  
    using **NLP + Machine Learning** 🚀
    """
)

# Input fields inside a nice box
st.markdown("### 📝 Enter Your Questions")
with st.container():
    q1 = st.text_input('✍️ Enter Question 1')
    q2 = st.text_input('✍️ Enter Question 2')

# Prediction button
if st.button('🔮 Find Similarity'):
    if q1.strip() == "" or q2.strip() == "":
        st.warning("⚠️ Please enter both questions before submitting.")
    else:
        query = helper.query_point_creator(q1, q2)
        result = model.predict(query)[0]

        if result:
            st.success("✅ These questions are **Duplicate**")
            st.balloons()  # 🎈 add fun animation
        else:
            st.error("❌ These questions are **Not Duplicate**")
            st.snow()  # ❄️ nice animation for contrast

# import streamlit as st
# import requests

# st.title("🚢 Titanic Chatbot")

# question = st.text_input("Ask me a question about the Titanic dataset!")

# if st.button("Ask"):
#     if question:
#         response = requests.get(f"http://127.0.0.1:8000/query/?question={question}")
#         answer = response.json().get("answer", "No answer found")
        
#         if "Generated histogram saved" in answer:
#             st.image("age_histogram.png")
#         else:
#             st.write(f"**Answer:** {answer}")


import matplotlib
matplotlib.use("Agg")  # ✅ Use a non-interactive backend

import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Streamlit Title
st.title("🚢 Titanic Chatbot")

# User Input
question = st.text_input("Ask me a question about the Titanic dataset!")

if st.button("Ask"):
    if question:
        response = requests.get(f"http://127.0.0.1:8000/query/?question={question}")
        answer = response.json().get("answer", "No answer found")
        
        # Check if user asked about a histogram
        if "histogram" in question.lower() and "age" in question.lower():
            # Load Titanic Dataset
            data_file = "Titanic-Dataset.csv"
            if os.path.exists(data_file):
                df = pd.read_csv(data_file)
                
                # Generate Histogram
                plt.figure(figsize=(8, 5))
                sns.histplot(df["Age"].dropna(), bins=20, kde=True, color="skyblue")
                plt.xlabel("Age")
                plt.ylabel("Count")
                plt.title("Distribution of Passenger Ages")
                
                # Save and Display Histogram
                hist_path = "age_histogram.png"
                plt.savefig(hist_path)
                st.image(hist_path)
            else:
                st.error("🚨 Titanic dataset not found! Please check the file path.")
        
        else:
            st.write(f"**Answer:** {answer}")

# Hide Streamlit branding
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

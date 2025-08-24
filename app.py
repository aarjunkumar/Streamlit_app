import google.generativeai as genai
import os 
import streamlit as st 
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("GOOGLe_API_KEY")
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-2.0-flash")

st.title("AI Search")
input_text=st.text_input("Search the topic you want")

if input_text:
  response=model.generate_content(input_text)
  st.write(response.text)

## http://192.168.29.104:8501

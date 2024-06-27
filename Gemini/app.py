from dotenv import load_dotenv
load_dotenv() #loading all env variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load Gemini pro model and get respones

model=genai.GenerativeModel("gemini-pro")
def get_gemini_responses(question):
    response=model.generate_content(question)
    return response.text

#intializing streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input=st.text_input(":Input: ",key="input" )
submit=st.button("Ask the question")

#when submitted 
if submit:
    response=get_gemini_responses(input)
    st.subheader("The Respons is")
    st.write(response)





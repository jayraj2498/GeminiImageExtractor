from dotenv import load_dotenv 
load_dotenv() 

import os 
import streamlit as st 
import google.generativeai as genai 


genai.configure(api_key=os.getenv('GOOGLE_API_KEY')) 

model = genai.GenerativeModel("gemini-pro") 

def get_gemini_respone(question): 
    response=model.generate_content(question)
    return response.text 



# by using stremlit app we host it on url 

st.set_page_config(page_title="Q&A Demo App") 

st.header("Gemini-pro-application")

input=st.text_input("Provide your Question : " ,key="input") 
submit=st.button("Enter") 

if submit:
    response=get_gemini_respone(input)
    st.subheader("Your Question response is : ") 
    st.write(response)
    
    
    
    

# --------------------------------------------------------------
# def get_gemini_respone(question): 
#     response=model.generate_content(question)
#     return response.text 

# Q= input("enter your Question :") 
# answer=get_gemini_respone(Q)

# print(answer)
# --------------------------------------------------------------
from dotenv import load_dotenv
import streamlit as st
import  google.generativeai as genai
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Gemini model and response

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title='Q&A chatbot')
st.header('Gemini LLM Application')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    
input=st.text_input("Input: ",key='input')
submit= st.button("Ask the question")

if submit and input:
    response=get_gemini_response(input)
    #user query, response and history
    st.session_state['chat_history'].append(('You',input))
    st.subheader('Response is')
    
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('Bot',chunk.text))
st.subheader("The chat history")
for role, text in st.session_state['chat_history']:
    st.write(f'{role}:{text}')

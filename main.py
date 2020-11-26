import streamlit as st
from transformers import pipeline

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

ner = pipeline("ner", grouped_entities=True)

st.title('Named Entity Recognition')
st.header('API by TN')

sentence = st.text_input('Input your sentence here:') 

if sentence:
    st.write((sentence))
import streamlit as st
from transformers import pipeline

ner = pipeline("ner", grouped_entities=True)

st.title('Named Entity Recognition')
st.header('API by TN')

sentence = st.text_input('Input your sentence here:') 

if sentence:
    st.write(output = ner(sequence))
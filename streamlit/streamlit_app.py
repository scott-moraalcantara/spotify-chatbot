import streamlit as st
import requests

st.title("Spotify Chatbot")

user_query = st.text_input("Ask me to play something!")

if st.button("Send"):
    response = requests.post("http://localhost:5000/chat", json={"query": user_query})
    st.write(response.json()["response"])
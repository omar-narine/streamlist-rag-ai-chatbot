import streamlit as st
import os, requests

# WEB PAGE CONFIGURATION
st.set_page_config(page_title="Codebase RAG Chatbot")

st.title("Codebase RAG Chatbot")

if 'repo_url' not in st.session_state:
    st.session_state.repo_url = "https://github.com/CoderAgent/SecureAgent"

if "messages" not in st.session_state:
    st.session_state.messages = []

## RESPONSE GENERATIONq
def get_response(query):
    data = {
        "query" : query,
        "repo_url" : st.session_state.repo_url
    }
    response = requests.get("http://localhost:5000/query", json=data)
    if response.status_code == 200:
       try:
           response_data = response.json()
           return response_data.get("response")
       except requests.exceptions.JSONDecodeError:
           print("Failed to decode JSON")
           return None
    else:
       print(f"Request failed with status code {response.status_code}")
       return None

## REPO UPDATING
def on_repo_url_change():
    repo_url = st.session_state.repo_url = st.session_state.repo_url
    
    if repo_url:
        url = f'http://127.0.0.1:5000/embed-repo'  # URL format

        data = {
            "repo_url": st.session_state.repo_url 
        }

        # Send a POST request with JSON data
        response = requests.post(url, json=data)

        print(response.text)
        print(str(response))
            
# WEB PAGE UI
st.markdown("### GitHub Repository")
    
st.text_input(
    label = "Enter a GitHub repository URL to chat with!",
    value=st.session_state.repo_url,
    disabled=False,
    key="repo_url",
    on_change=on_repo_url_change
)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
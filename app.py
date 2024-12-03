import streamlit as st
import os, requests

base_url = "http://localhost:5000"

# WEB PAGE CONFIGURATION
st.set_page_config(page_title="Codebase RAG Chatbot")

st.title("Codebase RAG Chatbot")

if 'repo_url' not in st.session_state:
    st.session_state.repo_url = "https://github.com/CoderAgent/SecureAgent"

if "messages" not in st.session_state:
    st.session_state.messages = []

## RESPONSE GENERATION
def get_response(query):
    data = {
        "query" : query,
        "repo_url" : st.session_state.repo_url
    }
    response = requests.get(f"{base_url}/query", json=data)
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
        data = {
            "repo_url": st.session_state.repo_url 
        }

        # Send a POST request with JSON data
        response = requests.post(f"{base_url}/embed-repo", json=data)
        
        st.session_state.messages = []
        
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

if prompt := st.chat_input("Can you explain the functionality of this codebase?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
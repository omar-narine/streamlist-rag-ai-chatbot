# Codebase RAG Chatbot

## Overview
This is a simple GitHub Repository Codebase RAG (Readability, Awesomeness, Generality) Chatbot built using Streamlit, a free and open-source Python library for building custom web applications. The chatbot aims to provide a friendly interface for users to ask questions and interact with a GitHub repository.

## Features

* Query Processing: The chatbot accepts user input queries and sends them to a backend API to generate responses.
* Repository Embedding: The chatbot can embed a GitHub repository directly into the application, enabling users to interact with the repository.
* Chat Interface: A user-friendly chat interface allows users to ask questions and receive responses.
* Repository URL Support: The chatbot supports different GitHub repository URLs.

## Requirements

* Python 3.8+
* Streamlit 1.5+
* Requests 2.25+

## Usage

1. Clone the repository: `git clone https://github.com/...`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the application: `streamlit run app.py`
4. Access the application at: `http://localhost:5000`

## Development
Developers can extend the chatbot's functionality by modifying the `app.py` file or creating additional backend APIs. The chatbot uses a modular design, making it easy to incorporate new features.

## API Documentation

### get_response(query, repo_url)
Args:
- `query`: The user input query.
- `repo_url`: The GitHub repository URL.
Returns:
- A JSON response containing the generated response or None on failure.

### on_repo_url_change(repo_url)
Args:
- `repo_url`: The updated GitHub repository URL.
Returns:
- Sends a POST request to the backend API to embed the repository.

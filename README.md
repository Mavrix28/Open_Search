# Open_Search


## 🔎 LangChain Chatbot with Search

This project is a conversational AI chatbot built using LangChain, Streamlit, and Groq AI. The chatbot leverages various tools like DuckDuckGo, Wikipedia, and Arxiv for retrieving information dynamically and intelligently responding to user queries.

## Features
	•	Multi-source search: Query information from DuckDuckGo, Wikipedia, and Arxiv.
	•	Conversational interface: Chatbot UI using Streamlit.
	•	Dynamic responses: Handles user inputs with an AI-powered language model (Groq’s Llama3).
	•	Session management: Maintains conversation history across interactions.
	•	Error handling: Graceful fallback for search errors and issues.

## Requirements
	•	Python 3.8 or above
	•	Python libraries:
	•	streamlit
	•	langchain
	•	langchain-community
	•	dotenv

 ## Usage
	1.	Open the app in your browser at the URL provided by Streamlit (usually http://localhost:8501).
	2.	Type your query in the chatbox. For example:
	•	“What is machine learning?”
	•	“Tell me about General Intelligence AI.”
	3.	The chatbot will fetch information and respond intelligently.

 ## Future Enhancements
	•	Add more tools (e.g., GPT-4, Bing Search, OpenAI API).
	•	Implement persistent session storage using databases or files.
	•	Enable customization of model parameters via the Streamlit sidebar.

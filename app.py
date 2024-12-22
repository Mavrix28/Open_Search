import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Ensure API Key is available
if not api_key:
    st.error("API key is missing. Please set your GROQ_API_KEY in the .env file.")
    st.stop()

# Initialize Arxiv and Wikipedia Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=500)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

search = DuckDuckGoSearchRun(name="Search", safe_search=True)

# Streamlit UI
st.title("🔎  - Open Your Thinking -")
st.sidebar.title("Settings")
st.sidebar.info("Using the GROQ API Key from environment variables.")

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

# Display Chat Messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User Input
if prompt := st.chat_input(placeholder="What is machine learning?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Initialize ChatGroq
    llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
    

    # Initialize Agent
    tools = [arxiv, wiki]  # DuckDuckGo removed temporarily

    search_agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True
     )

    # Generate Response
    with st.chat_message("assistant"):
        with st.spinner("Searching..."):
            try:
                st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=True)
                response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
            except Exception as e:
                response = f"Sorry, I encountered an error: {str(e)}"
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)
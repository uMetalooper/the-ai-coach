import streamlit as st
import requests
import json

# Configuration
BACKEND_URL = "http://localhost:8000/chat" # Default FastAPI port

st.title("AI Career Coach for Vietnamese Students in the UK")

# --- State Management ---
def initialize_state():
    if "industry" not in st.session_state:
        st.session_state.industry = None
    if "messages" not in st.session_state:
        st.session_state.messages = [] # Store chat history: {role: str, content: str}
    if "industry_selected" not in st.session_state:
        st.session_state.industry_selected = False

initialize_state()

# --- Industry Selection ---
if not st.session_state.industry_selected:
    st.header("Welcome!")
    industry_input = st.text_input("Which industry are you studying or interested in?")
    if st.button("Start Chatting"):
        if industry_input:
            st.session_state.industry = industry_input
            st.session_state.industry_selected = True
            st.rerun() # Rerun to switch to chat view
        else:
            st.warning("Please enter an industry.")
else:
    # --- Chat Interface ---
    st.header(f"AI Coach ({st.session_state.industry} Sector)")

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask your AI coach..."):
        # Add user message to chat history and display it
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Prepare request data for backend
        request_data = {
            "industry": st.session_state.industry,
            "messages": st.session_state.messages # Send the whole history
        }

        # Display assistant response while streaming
        with st.chat_message("assistant"):
            message_placeholder = st.empty() # Create a placeholder
            full_response = ""
            try:
                # Send request to backend and stream response
                with requests.post(BACKEND_URL, json=request_data, stream=True) as r:
                    r.raise_for_status() # Raise an exception for bad status codes
                    for chunk in r.iter_content(chunk_size=None): # None uses server's chunk size
                        if chunk: # filter out keep-alive new chunks
                            chunk_text = chunk.decode('utf-8')
                            full_response += chunk_text
                            message_placeholder.markdown(full_response + "▌") # Simulate typing
                message_placeholder.markdown(full_response) # Display final response
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to backend: {e}")
                # Remove the potentially incomplete assistant message placeholder
                st.session_state.messages.pop() # Remove the user message that failed
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
                # Remove the potentially incomplete assistant message placeholder
                st.session_state.messages.pop() # Remove the user message that failed 
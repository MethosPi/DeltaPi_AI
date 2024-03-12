import streamlit as st
import ollama

# Set app title
st.title("DeltaPi Chatbot")

# Create chat message
message = st.chat_message("assistant")
message.write("Hello I'm DeltaPi Chatbot, what can I do for you?")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Prompt:"):

# Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})    

   # Send user prompt to Ollama Phi
    response = ollama.chat(model='phi', messages=[
            {"role": "user", "content": f"{prompt}"}
        ])
    
    # Get assistant response
    assistant_response = response['message']['content']

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
    
        # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

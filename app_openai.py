import streamlit as st
from openai  import OpenAI

# Set up the OpenAI API client
client = OpenAI(api_key="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")

# Set app title 
st.title("DeltaPi Chatbot")

# Create chat message
message = st.chat_message("assistant")
message.write("Hello I'm DeltaPi Chatbot, what can I do for you?")

# Set instructions
instructions = st.sidebar.text_area("Instructions", value="")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# React to user input
if prompt := st.chat_input("Prompt:"):

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Send user prompt to OpenAI
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "user", "content": f"{prompt}"},
            {"role": "system", "content": f"Chat history: {st.session_state.messages}"},
            {"role": "system", "content": f"Instructions: {instructions}"}
        ]
    )

    # Get assistant response
    response = completion.choices[0].message.content

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
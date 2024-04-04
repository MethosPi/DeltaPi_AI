import streamlit as st
from groq import Groq


# Set app title 
st.title("DeltaPi Chatbot")

# Create chat message
message = st.chat_message("assistant")
message.write("Hello I'm DeltaPi Chatbot, what can I do for you?")

groq_api_key = st.secrets["my_api_key"]

model = st.sidebar.selectbox(
    'Select your LPU AI model (powered by Groq)', ("mixtral-8x7b-32768", "llama2-70b-4096", "gemma-7b-it") )

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


    # Set up the Groq API client
    client = Groq(api_key=groq_api_key)

    # Send user prompt to Groq
    completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": instructions},
        {"role": "system", "content": f"Chat history: {st.session_state.messages}"},
        {"role": "user", "content": prompt},
    ],
    model="mixtral-8x7b-32768",
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    stop=None,
    stream=False
    )

    # Get assistant response
    response = completion.choices[0].message.content

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
import gradio as gr
from groq import Groq

# Set up the Groq client
client = Groq(api_key="your-groq-api-key")

# Define the predict function
def predict(message, history):
    # Set up the chat history
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})
  
    # Send user prompt to Groq
    response = client.chat.completions.create(model='mixtral-8x7b-32768',
    messages= history_openai_format,
    temperature=1.0,
    stream=True)
    
    # Get assistant response
    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
              partial_message = partial_message + chunk.choices[0].delta.content
              yield partial_message

# Launch the app
gr.ChatInterface(predict).launch()

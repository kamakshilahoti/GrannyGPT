import streamlit as st
import gradio as gr
from openai import OpenAI
from huggingface_hub import hf_hub_download

# Initialize OpenAI and Hugging Face API
# (Ensure you've set up API keys for these)

def openai_chat(message):
    # Make a call to OpenAI API to generate response
    # Replace with your OpenAI model interaction code
    response = OpenAI.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()

def huggingface_chat(message):
    # Use Hugging Face models to respond (for example)
    # (Assuming Hugging Face API setup is already in place)
    model = hf_hub_download(repo_id="your-model-repo-id")
    response = model.generate(message)
    return response

# Define a basic function to handle chatbot
def chatbot(message):
    if st.button("Use OpenAI"):
        return openai_chat(message)
    else:
        return huggingface_chat(message)

# Streamlit UI for the chatbot
def main():
    st.title("Chatbot App")
    
    message = st.text_input("Ask me anything:")
    
    if message:
        response = chatbot(message)
        st.write("Response: ", response)

# Run the app
if __name__ == "__main__":
    main()

import streamlit as st
from huggingface_hub import hf_hub_download
from transformers import AutoModelForCausalLM, AutoTokenizer

# Function to interact with the Hugging Face model (Mistral, in this case)
def huggingface_chat(message):
    try:
        # Replace with your actual model's repo_id on Hugging Face
        model_repo = "mistral-7b"  # Example: replace with the correct model repo ID
        model_file = "pytorch_model.bin"  # This is typically the model's weights file

        # Download model from Hugging Face Hub
        model_path = hf_hub_download(repo_id=model_repo, filename=model_file)

        # Load the model and tokenizer from the downloaded path
        model = AutoModelForCausalLM.from_pretrained(model_path)
        tokenizer = AutoTokenizer.from_pretrained(model_path)

        # Tokenize the input message
        inputs = tokenizer(message, return_tensors="pt")

        # Generate a response
        outputs = model.generate(inputs["input_ids"], max_length=100)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return response
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI for the chatbot
def main():
    st.title("GrannyGPT Chatbot")
    
    message = st.text_input("Ask me anything:")

    if message:
        response = huggingface_chat(message)
        st.write("Response: ", response)

# Run the app
if __name__ == "__main__":
    main()

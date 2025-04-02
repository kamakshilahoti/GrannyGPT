import os
import requests
import streamlit as st

# Option 1: Load API key from environment variables (local development)
# Ensure to set the environment variable: export HF_API_KEY="your_private_api_key"
# Option 2: Alternatively, for Streamlit Cloud, use secrets (check Streamlit secrets management below)
# If running locally, make sure to create a `.env` file and use python-dotenv or set the environment variable directly.

# Load API key from Streamlit Secrets (use this for Streamlit Cloud)
HF_API_KEY = st.secrets.get("HF_API_KEY")

# Alternatively, you can load from environment variables (for local development).
if HF_API_KEY is None:
    HF_API_KEY = os.getenv("HF_API_KEY")
    
# If the key is not found, raise an error.
if HF_API_KEY is None:
    st.error("Hugging Face API Key is missing. Please set the HF_API_KEY environment variable or use Streamlit secrets.")
else:
    st.write("API Key loaded successfully.")

# Hugging Face API URL (you can replace this with the actual model URL you're using)
HF_API_URL = "https://api-inference.huggingface.co/models/mistral-7b"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def huggingface_chat(message):
    """Send the message to Hugging Face model and return the response."""
    payload = {"inputs": message}
    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()[0]["generated_text"]
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main function to run the Streamlit app."""
    st.title("GrannyGPT Chatbot")
    message = st.text_input("Ask me anything:")

    if message:
        response = huggingface_chat(message)
        st.write("Response:", response)

# Run the app
if __name__ == "__main__":
    main()

import streamlit as st
import requests

# Set your Mistral API endpoint and key
MISTRAL_API_KEY = ""  # Replace with your Mistral API key
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"  # Change if the endpoint is different

# Function to interact with Mistral API
def mistral_chat(message):
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    # Define the payload
    payload = {
        "messages": [{"role": "user", "content": message}],
        "model": "mistral-7b",  # Replace with your model if different
        "temperature": 0.7
    }

    # Send the request to Mistral API
    response = requests.post(MISTRAL_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "No response")
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit UI for the chatbot
def main():
    st.title("GrannyGPT Chatbot")
    st.write("Ask me anything:")

    # Get user input
    message = st.text_input("Enter your message:")
    
    if message:
        response = mistral_chat(message)
        st.write("Response: ", response)

# Run the app
if __name__ == "__main__":
    main()

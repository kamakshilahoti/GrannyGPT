async function sendMessage() {
  const userInput = document.getElementById('userInput').value;
  const mode = document.getElementById('mode').value; // Get the mode selected by the user
  const responseDiv = document.getElementById('response');

  const response = await fetch('https://api-inference.huggingface.co/models/kamakshiiiiii/granny-gpt', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer YOUR_HUGGING_FACE_API_KEY',
    },
    body: JSON.stringify({
      inputs: { topic: userInput, mode: mode },
    })
  });

  const data = await response.json();
  responseDiv.innerText = data[0]; // Assuming the result comes in as an array with one element
}

import requests

# Replace with your Hugging Face API key
API_KEY = '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'

# Select a model
MODEL = 'black-forest-labs/FLUX.1-dev'  # Change this to your chosen model

# Set up the endpoint
url = f'https://api-inference.huggingface.co/models/{MODEL}'

# Define your input data
input_data = {
    "inputs": "Once upon a time",
}

# Set up headers with the API key
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Make a POST request to the API
response = requests.post(url, headers=headers, json=input_data)

# Get the output
if response.status_code == 200:
    output = response.json()
    print("Output:", output)
else:
    print("Error:", response.status_code, response.text)

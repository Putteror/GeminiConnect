
import requests

# Replace with your actual Gemini API key
api_key = "AIzaSyAvZ8_lDANEV8rRwcib7i7SVLFUoOWm7h4"

# Text prompt for generation
prompt = "Write a poem about a cat."

# Base URL for the Gemini API
base_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

# Choose the appropriate model name (e.g., "text-davinci-003")
model_name = "text-embedding-004"

# Construct the full URL with API key and model name
url = base_url.format(api_key.split("-")[0], model_name)

# Prepare the request body
request_body = {"contents":[{"parts":[{"text":"how to rich in one day"}]}]}


# Set headers for authentication and content type
headers = {
    "Content-Type": "application/json",
}

# Send the POST request
response = requests.post(url, headers=headers, json=request_body)


# Check for successful response
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()

    # Access the generated text
    generated_text = response.json()
    print(generated_text)
else:

    print(f"Error: API request failed with status code {response.status_code}")


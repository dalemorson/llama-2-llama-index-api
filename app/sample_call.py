# Use POST as there is no limit to characters like GET

import requests
import json

url = "http://localhost:8000/ask"

payload = json.dumps({
  "question": "What is Llama 2?"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
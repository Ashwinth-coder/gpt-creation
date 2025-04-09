# chatbot.py
import requests
from config import MISTRAL_API_KEY

def chat_with_mistral(prompt):
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
    }
    data = {
        "model": "mistral-medium",  # or mistral-small / mistral-large
        "messages": [
            {"role": "system", "content": "You are AshGPT, a helpful and witty assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        return f"[Error] {e}"
    except KeyError:
        return "[Error] Unexpected response format"

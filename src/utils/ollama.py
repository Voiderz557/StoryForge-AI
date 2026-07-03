import requests
from config import OLLAMA_URL, OLLAMA_MODEL


def ask_ollama(prompt: str, timeout: int = 900) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=timeout,
    )

    response.raise_for_status()
    return response.json()["response"].strip()
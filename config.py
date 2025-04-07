# config.py

MODEL_CONFIG = {
    "provider": "ollama",  # openai, huggingface_api, huggingface_local, ollama
    "model_name": "llama2",  # e.g., gpt-3.5-turbo, mistralai/Mistral-7B-Instruct, llama2
    "temperature": 0.7,
    "max_tokens": 1000,
    "stream": False,

    # Optional API credentials
    "api_key": "",           # For OpenAI
    "hf_token": "",          # For Hugging Face API
    "local_model_path": ""   # For local Transformers, if needed
}

APP_SETTINGS = {
    "title": "Modular Chainlit Chatbot",
    "description": "Supports OpenAI, Hugging Face (API/local), and Ollama.",
    "debug": True
}

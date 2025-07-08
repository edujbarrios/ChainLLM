# config.py

MODEL_CONFIG = {
    "provider": "manifest",  # Only "manifest" is supported in this setup
    "manifest_client": "http",  # Use "http" for external server, or "local"
    "manifest_connection": "http://localhost:5000",  # Manifest server URL
    "manifest_cache": False  # Set to True if you want caching (SQLite, Redis, etc.)
}

APP_SETTINGS = {
    "title": "ChainLLM Chatbot",
    "description": "Test several LLMs at one site",
    "debug": True
}

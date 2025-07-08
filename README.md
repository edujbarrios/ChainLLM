# ChainLLM

By Eduardo J. Barrios [https://edujbarrios.com](https://edujbarrios.com)

---

A fully-configurable chatbot built with [Chainlit](https://www.chainlit.io/) that supports multiple model providers:

- OpenAI (`gpt-3.5-turbo`, etc.)
- Hugging Face Inference API
- Hugging Face Local (via Transformers)
- Ollama (local models like `llama2`, `mistral`, `gemma`, etc.)
---
All of them is now managed by Manifest (centralized backend and multi-provider orchestration)
---

## ⚙ Configuration [MIGRATED TO MANIFEST]

All settings are in `manifest.yml`:
```YML
client:
  # Choose the backend provider you want to route through Manifest.
  # Supported types include: openai, huggingface, cohere, local, http
  client_type: openai
  # Use an environment variable to store sensitive keys
  connection: ${OPENAI_API_KEY}  # Replace this for other clients:
  # connection: ${HF_API_KEY}    # if client_type is huggingface
  # connection: http://localhost:11434  # if using Ollama/local

# ---- MODEL SETTINGS ----
model:
  provider: openai  # Options: openai, huggingface, cohere, local, etc.
  model_name: gpt-3.5-turbo  # Change depending on provider

  # Optional tuning parameters:
  temperature: 0.7
  max_tokens: 1000
  stream: true
```
---

##  Using Manifest

1. Install the Manifest server:

```bash
pip install manifest-ml[server]
manifest server start
```

You can configure multiple LLM backends in `manifest.yml`.

---

## ▶ Run the Bot

```bash
chainlit run main.py
```

Then open your browser at `http://localhost:8000`.

---

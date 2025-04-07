# 🤖 Modular Chainlit Chatbot

A fully-configurable chatbot built with [Chainlit](https://www.chainlit.io/) that supports multiple model providers:

- ✅ OpenAI (`gpt-3.5-turbo`, etc.)
- ✅ Hugging Face Inference API
- ✅ Hugging Face Local (via Transformers)
- ✅ Ollama (local models like `llama2`, `mistral`, `gemma`, etc.)

---

## 📦 Setup

1. Clone and install dependencies:

```bash
git clone https://github.com/your-user/chainlit-chatbot.git
cd chainlit-chatbot
pip install -r requirements.txt
```

---

## ⚙️ Configuration

All settings are in `config.py`:

```python
MODEL_CONFIG = {
    "provider": "ollama",  # openai, huggingface_api, huggingface_local, ollama
    "model_name": "llama2",
    "temperature": 0.7,
    "max_tokens": 1000,
    "stream": False
}
```

---

## 🦙 Using Ollama

1. Install [Ollama](https://ollama.com/):

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

2. Download a model (e.g. `llama2`):

```bash
ollama run llama2
```

3. Set in `config.py`:

```python
"provider": "ollama",
"model_name": "llama2"
```

No API key is needed. Ollama runs locally via HTTP.

---

## 🚀 Run the Bot

```bash
chainlit run main.py
```

Then open your browser at `http://localhost:8000`.

---

## 🧠 Roadmap Ideas

- [ ] Add support for llama.cpp / GGUF
- [ ] Use `.env` or YAML for config
- [ ] Save chat history
- [ ] Custom UI

---

## 💬 Questions?

Feel free to reach out or contribute!

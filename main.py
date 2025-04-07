# main.py

import chainlit as cl
from config import MODEL_CONFIG, APP_SETTINGS

provider = MODEL_CONFIG["provider"]

# Provider-specific imports
if provider == "openai":
    import openai
    openai.api_key = MODEL_CONFIG["api_key"]

elif provider == "huggingface_api":
    import requests

elif provider == "huggingface_local":
    from transformers import pipeline
    pipe = pipeline("text-generation", model=MODEL_CONFIG["model_name"], device=0)

elif provider == "ollama":
    import httpx

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content=f"🤖 Welcome to: {APP_SETTINGS['title']}").send()

@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content

    if provider == "openai":
        response = openai.ChatCompletion.create(
            model=MODEL_CONFIG["model_name"],
            messages=[{"role": "user", "content": user_input}],
            temperature=MODEL_CONFIG["temperature"],
            max_tokens=MODEL_CONFIG["max_tokens"],
            stream=MODEL_CONFIG["stream"]
        )
        if MODEL_CONFIG["stream"]:
            async for chunk in response:
                delta = chunk.choices[0].delta.get("content", "")
                await cl.Message(content=delta).send()
        else:
            await cl.Message(content=response["choices"][0]["message"]["content"]).send()

    elif provider == "huggingface_api":
        headers = {
            "Authorization": f"Bearer {MODEL_CONFIG['hf_token']}" if MODEL_CONFIG['hf_token'] else None
        }
        data = {
            "inputs": user_input,
            "parameters": {
                "temperature": MODEL_CONFIG["temperature"],
                "max_new_tokens": MODEL_CONFIG["max_tokens"]
            }
        }
        url = f"https://api-inference.huggingface.co/models/{MODEL_CONFIG['model_name']}"
        res = requests.post(url, headers=headers, json=data)
        res_data = res.json()
        generated = res_data[0]["generated_text"] if isinstance(res_data, list) else str(res_data)
        await cl.Message(content=generated).send()

    elif provider == "huggingface_local":
        output = pipe(user_input, max_new_tokens=MODEL_CONFIG["max_tokens"], temperature=MODEL_CONFIG["temperature"])
        await cl.Message(content=output[0]["generated_text"]).send()

    elif provider == "ollama":
        async with httpx.AsyncClient() as client:
            payload = {
                "model": MODEL_CONFIG["model_name"],
                "prompt": user_input,
                "stream": MODEL_CONFIG["stream"]
            }

            if MODEL_CONFIG["stream"]:
                async with client.stream("POST", "http://localhost:11434/api/generate", json=payload) as response:
                    async for chunk in response.aiter_lines():
                        if chunk.strip():
                            try:
                                data = httpx.Response(200, content=chunk).json()
                                content = data.get("response", "")
                                if content:
                                    await cl.Message(content=content).send()
                            except Exception:
                                pass
            else:
                response = await client.post("http://localhost:11434/api/generate", json=payload)
                result = response.json()
                await cl.Message(content=result.get("response", "Error")).send()

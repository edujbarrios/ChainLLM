import os
import chainlit as cl
from config import MODEL_CONFIG, APP_SETTINGS

# Initialize Manifest client
from manifest import Manifest

manifest = Manifest(
    client_name=MODEL_CONFIG.get("manifest_client", "http"),
    client_connection=MODEL_CONFIG.get("manifest_connection", "http://localhost:5000"),
    cache_name="sqlite" if MODEL_CONFIG.get("manifest_cache") else "no_cache"
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content=f"🤖 Welcome to: {APP_SETTINGS['title']}").send()

@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content
    try:
        # Stream if supported
        if manifest.client.supports_streaming:
            full_response = ""
            async for chunk in manifest.astream([user_input]):
                full_response += chunk
                await cl.Message(content=chunk).send()
        else:
            output = manifest.run([user_input])
            await cl.Message(content=output[0]).send()
    except Exception as e:
        await cl.Message(content=f"❌ Manifest error: {e}").send()

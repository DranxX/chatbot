from google import genai
from google.genai import types
import json

def handler(request, response):
    data = request.json or {}
    prompt = data.get("prompt", "")

    client = genai.Client()

    chat = client.chats.create(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction="Kamu adalah pemandu di dunia Roblox … gaya tetua gunung"
        )
    )

    ans = chat.send_message(message=prompt)
    response.send(json.dumps({"reply": ans.text}))

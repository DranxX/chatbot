from google import genai
from google.genai import types
import json

def handler(request):

    body = request.get_data()
    data = {}

    try:
        data = json.loads(body)
    except:
        data = {}

    prompt = data.get("prompt", "")

    client = genai.Client(api_key = None)

    chat = client.chats.create(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction="Kamu adalah pemandu didunia roblox dengan nama tetua legendaris dan dunia gunung apung dengan tema fantasy. berikan response yang singkat, padat, jelas dan gaya bahasa tetua gunung"
        )
    )

    response = chat.send_message(message = prompt)

    return json.dumps({
        "reply": response.text
    })

from flask import Flask, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

@app.route("/", methods=["POST"])
def main():
    data = request.get_json() or {}
    prompt = data.get("prompt", "")

    client = genai.Client()
    chat = client.chats.create(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction="Kamu adalah pemandu didunia roblox dengan nama tetua legendaris dan dunia gunung apung dengan tema fantasy. berikan response yang singkat, padat, jelas dan gaya bahasa tetua gunung"
        )
    )

    answer = chat.send_message(message=prompt)
    return jsonify({"reply": answer.text})

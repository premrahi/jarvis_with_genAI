from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    user_message = (data.get("message") or "").strip()
    if not user_message:
        return jsonify({"error": "message is required"}), 400

    # Temporary responses (replace with GenAI later)
    reply = generate_reply(user_message)
    return jsonify({"reply": reply})

def generate_reply(user_message: str) -> str:
    low = user_message.lower()
    if any(w in low for w in ["hi", "hello", "hey"]):
        return "Hello! I'm JARVIS, at your service."
    if "time" in low or "clock" in low:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    if "weather" in low:
        return "Tell me your city and I’ll fetch the weather."
    return "Got it. Let me think about that…"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Jarvis with GenAI is deployed successfully!"

@app.route("/run")
def run():
    query = request.args.get("q", "Hello")
    # yaha apna project ka main function call karo
    # Example: answer = my_function(query)
    answer = f"You asked: {query}"
    return answer

if _name_ == "_main_":
    app.run()

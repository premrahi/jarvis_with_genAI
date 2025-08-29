from flask import Flask, request

from flask import Flask

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

if __name__ == "__main__":

    app.run()

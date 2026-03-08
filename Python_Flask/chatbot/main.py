from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

client = genai.Client(api_key='AIzaSyB__ga4HVGLkacSiP3To1kEaUr5d2j8LMc')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ChatBot", methods=['POST'])
def ChatBot():
    data = request.json
    user_message = data.get("message")

    try:
        response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents= user_message,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_level=types.ThinkingLevel.MEDIUM),
            system_instruction="you are Beta's AI assistant. Help users understand Beta's ML skills."
            )
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply":f"Erro: {str(e)}"}), 500
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

LOG_PATH = os.path.expanduser("~/MasterSystem/Security-Vault/memory_log.txt")

def get_vault_context():
    if os.path.exists(LOG_PATH):
        try:
            with open(LOG_PATH, "r") as f:
                return f.read()[-2000:]
        except:
            return "Error reading vault."
    return "No prior history found."

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/chat', methods=['POST'])
def chat():
    user_data = request.json
    user_input = user_data.get("message", "")
    vault_context = get_vault_context()
    
    full_prompt = f"SYSTEM: You are the Master System. Accessing Vault Context...\n{vault_context}\n\nUSER COMMAND: {user_input}"
    
    payload = {
        "model": "MasterSystem:latest",
        "prompt": full_prompt,
        "stream": False
    }
    
    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        answer = response.json().get("response", "No response from brain.")
        
        with open(LOG_PATH, "a") as f:
            f.write(f"\nSIR: {user_input}\nMASTER SYSTEM: {answer}\n")
            
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5000)

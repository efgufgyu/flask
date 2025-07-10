from flask import Flask, request

app = Flask(__name__)
connected_bots = []

@app.route('/')
def home():
    return 'Serveur C2 Flask en ligne'

@app.route('/connect', methods=['POST'])
def connect():
    ip = request.remote_addr
    if ip not in connected_bots:
        connected_bots.append(ip)
        print(f"[+] Nouveau bot connecté : {ip}")
    return 'OK'

@app.route('/bots', methods=['GET'])
def bots():
    return {'connected_bots': connected_bots}

if __name__ == '__main__':
    app.run()
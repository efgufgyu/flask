from flask import Flask, Response

app = Flask(__name__)

@app.route('/x9d3k7x2')  # <- nom de route discret
def redirect_bot():
    return Response("REDIRECT 37.66.40.122 9999", mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

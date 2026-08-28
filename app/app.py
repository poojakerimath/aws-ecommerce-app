from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Girija's Ecommerce App!to Big Sale 50% OFF</h1><p>Running on Docker + AWS</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
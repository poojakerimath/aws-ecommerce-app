from flask import Flask, render_template, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

REQUEST_COUNT = Counter('flask_requests_total', 'Total requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('flask_request_latency_seconds', 'Request latency', ['endpoint'])

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    REQUEST_COUNT.labels(request.method, request.path).inc()
    REQUEST_LATENCY.labels(request.path).observe(time.time() - request.start_time)
    return response

@app.route('/')
def home():
    return "<h1>Welcome to Girija's Ecommerce App! Big Sale 50% OFF</h1><p>Running on Docker + AWS</p>"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/health')
def health():
    return {"status": "healthy", "app": "ecommerce-app"}, 200

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
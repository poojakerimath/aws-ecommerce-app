from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')


@app.route('/products')
def products():
    return render_template('products.html')

# ONLY ONE - AT VERY BOTTOM
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# app2/app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def billing():
    return "Welcome to Billing!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

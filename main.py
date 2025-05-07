from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask on Railway!'

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

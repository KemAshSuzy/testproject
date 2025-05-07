from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, BAHO TAE ANG NAKA BASA ANEH!'

if __name__ == '__main__':
    # Get the port dynamically from the environment variable (Railway does this automatically)
    port = int(os.environ.get('PORT', 5000))
    # Ensure Flask listens on all network interfaces by using '0.0.0.0'
    app.run(debug=True, host='0.0.0.0', port=port)

from flask import Flask, jsonify

app = Flask(__name__)

# Sample route for testing
@app.route('/')
def hello():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
    
from flask import Flask, request, jsonify

model = None
app = Flask(__name__)

@app.route('/')
def home_endpoint():
    return 'Robots!'

if __name__ == '__main__':
    # app.run(host="0.0.0.0", debug=True)
    app.run(host='0.0.0.0', port=8000, debug=True)
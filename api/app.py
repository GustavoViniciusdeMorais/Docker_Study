from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_client = redis.Redis(host=redis_host, port=6379, db=0)

@app.route('/')
def hello():
    return jsonify(message="Hello, this API is connected to Redis!")

@app.route('/get/<key>')
def get_key(key):
    value = redis_client.get(key)
    if value:
        return jsonify({key: value.decode('utf-8')})
    return jsonify(error="Key not found"), 404

@app.route('/set/<key>/<value>')
def set_key(key, value):
    redis_client.set(key, value)
    return jsonify(message=f"Set {key} to {value}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

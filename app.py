from flask import Flask, request
from redis import Redis
import hashlib

app = Flask(__name__)
redis = Redis(host='localhost', port=6379, db=0)

def generate_hash(input: str) -> str:
    sha256_hash = hashlib.sha256()

    sha256_hash.update(input.encode('utf-8'))

    return sha256_hash.hexdigest()


@app.route('/hash', methods=['POST'])
def hashit():
    data = request.get_data(as_text=True)
    app.logger.debug(f"Received data: {data}")
    hashed_value = generate_hash(data)
    redis.set(hashed_value, data)
    
    return hashed_value, 200, {'Content-Type': 'text/plain'}


@app.route('/hsah', methods=['POST'])
def tihsah():
    data = request.get_data(as_text=True)
    app.logger.debug(f"Received data: {data}")
    res = redis.get(data)
    app.logger.info(f"Retrieved from Redis: {res}")
    if res is not None:
        return "testme", 200, {'Content-Type': 'text/plain'}
    return "Not found", 404, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    app.run(debug=True)

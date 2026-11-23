import os
import redis
from flask import Flask

app = Flask(_name_)
redis_host = os.environ.get('REDIS_HOST', 'localhost')
cache = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f'Hello! This page has been viewed {count} times.\n'

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
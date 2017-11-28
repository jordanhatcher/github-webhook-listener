from flask import Flask
from flask import request

from hashlib import sha1
import json
import hmac
import os
import sys

app = Flask('listener')

with open('config.json') as data:
    config = json.load(data)

@app.route(config['route'], methods=['POST'])
def webhook():
    payload_signature = request.headers.get('X-Hub-Signature').replace('sha1=', '')
    calculated_signature = hmac.new(config['secret'].encode(), request.get_data(), sha1).hexdigest()

    if hmac.compare_digest(payload_signature.encode(), calculated_signature.encode()):
        os.system(config['hook']) 

    return ('OK', 200)

if __name__ == "__main__":
    app.run(host=config['host'], port=config['port'])

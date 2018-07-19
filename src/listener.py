from flask import Flask
from flask import request

from hashlib import sha1
import json
import hmac
import os
import sys

app = Flask('listener')

try:
    with open('config.json') as data:
        config = json.load(data)
except:
    sys.exit('Unable to find config.json. Exiting.')

@app.route(config['route'], methods=['POST'])
def webhook():
    try:
        body = request.get_data()
        body_dict = json.loads(body.decode('utf-8'))
    except:
        return ('', 500)

    if body_dict['ref'] == 'refs/heads/master':
        payload_signature = request.headers.get('X-Hub-Signature').replace('sha1=', '')
        calculated_signature = hmac.new(config['secret'].encode(), body, sha1).hexdigest()

        if hmac.compare_digest(payload_signature.encode(), calculated_signature.encode()):
            os.system('\n'.join(config['hook']))
            return ('OK', 200)
        else:
            return ('Unauthorized', 401)
    return ('Unsupported branch', 200)


if __name__ == "__main__":
    app.run(host=config['host'], port=config['port'])

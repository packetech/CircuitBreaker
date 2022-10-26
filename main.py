# Let’s create some endpoints as a mock server

import random
import time

from flask import Flask
app = Flask(__name__)


@app.route('/success')
def success_endpoint():
    return {
        "msg": "Call to this endpoint was a smashing success."
    }, 200


@app.route('/failure')
def faulty_endpoint():
    r = random.randint(0, 1)
    if r == 0:
        time.sleep(2)

    return {
        "msg": "I will fail."
    }, 500

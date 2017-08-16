#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "webhookAction":
        return {}
    
    res = makeYqlQuery(req)
    return res


def makeYqlQuery(req):
    result = req.get("result")
    metadata = result.get("metadata")
    intent = metadata.get("intentName")
    if intent is None:
        return None
    
    if intent == "Everis Company Description":
        speech = "o intent é:" + intent + "resposta:" + ''' A everis é uma empresa multinacional de consultoria 
        que desenvolve soluções de negócio, tecnologia da informação e outsourcing para os setores de bancos, 
        seguros, telecomunicações, indústria e governo.'''
   
    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "weather-webhook"
    }





if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')

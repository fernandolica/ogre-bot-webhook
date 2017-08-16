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
    if req.get("result").get("action") != "planEverisPlus":
        return {}
   
    res = findIntent(req)
    return res


def findIntent(req):
    result = req.get("result")
    metadata = result.get("metadata")
    intent = metadata.get("intentName")
    if city is None:
        return None


    if intentName = "Plan Everis+ \\  Description"{
        speech = "o intent é :" + intent + "\n" + ''' resposta: 
        O plano everis+ é uma oferta inovadora, que surge no sentido de proporcionar um conjunto de
         benefícios que possibilitem, de forma mais eficiente, melhorar e ampliar as opções 
         disponíveis para os Colaboradores. O catalogo de benefícios encontram-se dividido em três categorias: 
         benefícios sociais, opções profissionais e créditos everis+. '''
    }

    if intentName = "Plan Everis+ \\  Objectives"{
        speech = "o intent é :" + intent + "\n" + ''' resposta: 
        O plano everis+ tem como objetivo proporcionar um conjunto de benefícios que possibilitem, 
        de forma mais eficiente, melhorar e ampliar as opções disponíveis para os Colaboradores.'''
    }

    if intentName = "Plan Everis+ \ Joining Conditions"{
        speech = "o intent é :" + intent + "\n" + ''' resposta: 
        Por favor, especifique qual o serviço do plano Everis+ ao qual quer aderir:
        - Passe Social
        - Internet e Data
        - Comunicação por Voz
        - Estacionamento
        - Formação Profissional
        - Dias Everis+
        - Equipamento Electrónico
        - Actividades Desportivas
        - Vouchers Cresce e Educação
        - Planos de Pensões '''
    }

    

    

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "weather-webhook"



if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')


#!/usr/bin/env python3
import http.client
import json

connection = http.client.HTTPConnection('localhost:3000')

headers = {'Content-type': 'application/json'}

produtos = [
["sobrecoxa", "Marca NAT é ruim","alimentacao"],
["calabresa", "Marca SADIA e SEARA são boas","alimentacao"],
["queijo-gorgonzola", "Marca Gran Mestri é boa","alimentacao"],
["queijo-mussarela", "Marca Casa do Pao de Queijo é boa","alimentacao"]
]

for p in produtos:
    connection.request('POST', '/produtos/' + p[0] + '/sumario', json.dumps({"sumario":p[1], "categoria":p[2]}), headers)
    response = connection.getresponse()
    response.read()
    endpoint = '/produtos/' + p[0]
    connection.request('GET', endpoint)
    response = connection.getresponse()
    print(endpoint + ": " + response.read().decode())

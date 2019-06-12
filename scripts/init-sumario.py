#!/usr/bin/env python3
import http.client
import json

connection = http.client.HTTPConnection('localhost:3000')

headers = {'Content-type': 'application/json'}

produtos = [
["banana", "Na feira R$ 2.79", "2.79", "feira"], 
["papel-toalha", "No bistek sempre R$3.49", "3.49", "bistek"],
]

for p in produtos:
    connection.request('POST', '/produtos/' + p[0] + '/sumario', json.dumps({"obs":p[1], "preco":p[2], "local":p[3]}), headers)
    response = connection.getresponse()
    response.read()
    endpoint = '/produtos/' + p[0]
    connection.request('GET', endpoint)
    response = connection.getresponse()
    print(endpoint + ": " + response.read().decode())

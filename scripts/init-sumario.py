#!/usr/bin/env python3
import http.client
import json

connection = http.client.HTTPConnection('localhost:3000')

headers = {'Content-type': 'application/json'}

produtos = [
["papel-toalha", "No bistek sempre R$3.49"],
]

for p in produtos:
    connection.request('POST', '/produtos/' + p[0] + '/sumario', json.dumps({"sumario":p[1]}), headers)
    response = connection.getresponse()
    response.read()
    endpoint = '/produtos/' + p[0]
    connection.request('GET', endpoint)
    response = connection.getresponse()
    print(endpoint + ": " + response.read().decode())

#!/usr/bin/env python3
import http.client
import json

connection = http.client.HTTPConnection('localhost:3000')

headers = {'Content-type': 'application/json'}

produtos = {
"banana": [
["2.79", "forte"],
],

"creme-leite": [
["2.79", "forte"]
],

"papel-toalha": [
["3.49", "bistek"]
]
}

for k, v in produtos.items():
    for d in v:
        connection.request('POST', '/produtos/' + k + '/historico', json.dumps({"preco":d[0], "local":d[1]}), headers)
        response = connection.getresponse()
        response.read()
    endpoint = '/produtos/' + k
    connection.request('GET', endpoint)
    response = connection.getresponse()
    print(endpoint + ": " + response.read().decode())

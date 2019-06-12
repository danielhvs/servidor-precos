#!/usr/bin/env python3
import http.client
import json

connection = http.client.HTTPConnection('localhost:3000')

headers = {'Content-type': 'application/json'}

produtos = {
"salgadinho-lays": [
["5.79", "forte"],
],
"acucar-refinado": [
["1.85", "forte"],
],
"papel-manteiga": [
["4.99", "forte"],
],
"passata": [
["5.49", "forte"],
],
"manteiga": [
["6.89", "forte"],
],
"queijo-mussarela": [
["22.90", "forte"],
],
"desodorante": [
["10.90", "forte"],
],
"sabonete-liquido": [
["5.49", "forte"],
],
"agua-coco": [
["6.89", "forte"],
],
"sache-johnny": [
["1.75", "forte"],
],
"detergente": [
["1.49", "forte"],
],
"detergente-maquina-louca": [
["15.90", "forte"],
],
"nutella": [
["14.50", "forte"],
],
"leite": [
["3.19", "forte"],
],
"cafe": [
["10.40", "forte"],
],
"arroz": [
["3.55", "forte"],
],
"sal": [
["2.55", "forte"],
],
"queijo-parmesao": [
["2.98", "forte"],
],
"banana": [
["2.79", "forte"],
],
"creme-leite": [
["1.55", "forte"]
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

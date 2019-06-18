#!/usr/bin/env python3
import http.client
import json

connection = http.client.HTTPConnection('localhost:3000')

headers = {'Content-type': 'application/json'}

produtos = {
"patinho": [
["23.59", "angeloni"],
],
"coxao mole": [
["21.39", "angeloni"],
],
"azeite": [
["15.34", "angeloni"],
],
"oleo": [
["5.99", "angeloni"],
],
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
["1.89", "angeloni"],
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
"suco-uva-1.5l": [
["8.94", "angeloni"]
],
"guardanapo": [
["3.59", "angeloni"]
],
"creme-leite": [
["1.55", "forte"]
],
"papel-toalha": [
["3.49", "bistek"],
["4.39", "angeloni"]
]
}

for k, v in produtos.items():
    for d in v:
        l = k.replace(" ", "%20")
        connection.request('POST', '/produtos/' + l + '/historico', json.dumps({"preco":d[0], "local":d[1], "obs":"obs"}), headers)
        response = connection.getresponse()
        response.read()
    endpoint = '/produtos/' + k
    connection.request('GET', endpoint)
    response = connection.getresponse()
    print(endpoint + ": " + response.read().decode())

comprasBistek = {
"sabonete liquido": [
["4.99"],
],
"sabonete Juju": [
["3.29"],
],
"glicerina": [
["6.45"],
],
"shampoo juju 400ml": [
["17.97"],
],
"kiboa": [
["3.79"],
],
"detergente": [
["1.85"],
],
"ajax pesado": [
["5.35"],
],
"limpa vidro": [
["9.97"],
],
"omo": [
["17.97"],
],
"batata palha": [
["2.99"],
],
"farelo de aveia 200g": [
["6.75"],
],
"leite": [
["2.97"],
],
"salgadinho": [
["6.25"],
["4.99"],
],
"biscoito de arroz": [
["5.79"],
],
"cafe 250g": [
["8.48"],
],
"maca verde": [
["7.99"],
],
"bifinho": [
["2.99"],
],
"espuma barbear": [
["20"],
],
"sobrecoxa": [
["7.97"],
],
"file de peito de frango": [
["9.97"],
],
"salame": [
["5.47"],
],
}


for k, v in comprasBistek.items():
    for d in v:
        l = k.replace(" ", "%20")
        connection.request('POST', '/produtos/' +  l + '/historico', json.dumps({"preco":d[0], "local":"bistek", "obs":""}), headers)
        response = connection.getresponse()
        response.read()
    endpoint = '/produtos/' + l
    connection.request('GET', endpoint)
    response = connection.getresponse()
    print(endpoint + ": " + response.read().decode())

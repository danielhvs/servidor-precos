#!/usr/bin/env python3
import http.client
import json

connection = http.client.HTTPConnection('localhost:3000')

headers = {'Content-type': 'application/json'}

produtos = [
{"nome": "cenoura", "local": "bistek", "preco": "2.98"},
{"nome": "banana", "local": "bistek", "preco": "3.98"},
{"nome": "tomate", "local": "bistek", "preco": "8.29"},
{"nome": "couve-flor", "local": "bistek", "preco": "4.49"},
{"nome": "sal", "local": "bistek", "preco": "3.69"},
{"nome": "molho yakissoba", "local": "bistek", "preco": "2.79"},
{"nome": "curcuma", "local": "bistek", "preco": "2.39"},
{"nome": "queijo ralado", "local": "bistek", "preco": "2.99"},
{"nome": "macarrao yakissoba", "local": "bistek", "preco": "4.89"},
{"nome": "biscoito de arroz", "local": "bistek", "preco": "3.98"},
{"nome": "torrada", "local": "bistek", "preco": "1.99"},
{"nome": "pao de castanha e nozes", "local": "bistek", "preco": "8.29"},
{"nome": "molho shoyo", "local": "bistek", "preco": "2.79"},
{"nome": "azeite", "local": "bistek", "preco": "19.87"},
{"nome": "mortadela", "local": "bistek", "preco": "5.93"},
{"nome": "alcatra", "local": "bistek", "preco": "25.98"},
{"nome": "iogurte grego", "local": "bistek", "preco": "1.89"},
{"nome": "queijo gorgonzola", "local": "bistek", "preco": "55.90"},
{"nome": "papel toalha", "local": "bistek", "preco": "3.49"},
{"nome": "pano umedecido", "local": "bistek", "preco": "8.22"},
{"nome": "fralda", "local": "bistek", "preco": "0.88"},
{"nome": "limao", "local": "big", "preco": "3.98"},
{"nome": "banana", "local": "big", "preco": "3.59"},
{"nome": "laranja", "local": "big", "preco": "3.86"},
{"nome": "oleo", "local": "big", "preco": "6.74"},
{"nome": "salame", "local": "big", "preco": "4.78"},
{"nome": "polvilho-doce", "local": "bistek", "preco": "3.99"},
{"nome": "polvilho-azedo", "local": "bistek", "preco": "7.99"},
{"nome": "leite-condensado-lata", "local": "bistek", "preco": "6.57"},
{"nome": "saco-lixo", "local": "bistek", "preco": "9.9"},
{"nome": "alcool-gel", "local": "bistek", "preco": "11.99"},
{"nome": "papel-toalha", "local": "bistek", "preco": "3.55"},
{"nome": "pasta-dente", "local": "bistek", "preco": "5.29"},
{"nome": "detergente", "local": "bistek", "preco": "1.85"},
{"nome": "agua-coco", "local": "bistek", "preco": "2.99"},
{"nome": "bicarbonato-sodio", "local": "bistek", "preco": "3.69"},
{"nome": "sabonete", "local": "bistek", "preco": "2.69"},
{"nome": "sabonete-johnson", "local": "bistek", "preco": "3.07"},
{"nome": "escova-dente", "local": "bistek", "preco": "7.41"},
{"nome": "faca", "local": "bistek", "preco": "4.79"},
{"nome": "colher-cozinha", "local": "bistek", "preco": "23.90"},
{"nome": "ajax", "local": "bistek", "preco": "2.97"},
{"nome": "macrovita-1l", "local": "bistek", "preco": "11.29"},
{"nome": "queijo-mussarela", "local": "bistek", "preco": "25.97"},
{"nome": "queijo-prato", "local": "bistek", "preco": "27.97"},
{"nome": "papel-higienico", "local": "bistek", "preco": "19.90"}
]

for v in produtos:
    l = v['nome'].replace(" ", "%20")
    connection.request('POST', '/produtos/' +  l + '/historico', json.dumps({"preco":v['preco'], "local":v['local'], "obs":""}), headers)
    response = connection.getresponse()
    response.read()
    endpoint = '/produtos/' + l
    connection.request('GET', endpoint)
    response = connection.getresponse()
    print(endpoint + ": " + response.read().decode())

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

comprasFort = {
"perfex": [
["4.99"],
],
"plastico grande com 100": [
["6.99"],
],
"plastico pequeno com 100": [
["4.99"],
],
"papel higienico": [
["1.07"],
],
"arroz": [
["3.85"],
],
"cafe aralto": [
["8.99"],
],
"cafe do ponto 500g": [
["10.40"],
],
"macarrao yakissoba": [
["4.19"],
],
"arroz multigraos 500g": [
["8.20"],
],
"arroz arboreo 1kg": [
["13.69"],
],
"macarrao penne 500g": [
["2.39"],
],
"salgadinho lays": [
["5.79"],
],
"nutella": [
["13.90"],
],
"leite condensado": [
["4.99"],
],
"feijao": [
["4.19"],
],
"pipoca 500g": [
["2.85"],
],
"creme de leite": [
["1.55"],
],
"salgadinho cheetos": [
["5.59"],
],
"passata": [
["5.99"],
],
"suco de uva 1.5L": [
["9.99"],
],
"quejo mussarela": [
["20.79"],
],
"sache-johnny": [
["1.75"],
],
"manteiga": [
["6.49"],
],
"salame": [
["5.89"],
],
"alcool": [
["4.99"],
],
"ajax pesado": [
["4.99"],
],
"saco de lixo 30L": [
["10.90"],
],
"pinho sol": [
["6.89"],
],
"lava louca": [
["15.90"],
],
"omo": [
["17.90"],
],
}

for k, v in comprasFort.items():
    for d in v:
        l = k.replace(" ", "%20")
        connection.request('POST', '/produtos/' +  l + '/historico', json.dumps({"preco":d[0], "local":"forte", "obs":""}), headers)
        response = connection.getresponse()
        response.read()
    endpoint = '/produtos/' + l
    connection.request('GET', endpoint)
    response = connection.getresponse()
    print(endpoint + ": " + response.read().decode())

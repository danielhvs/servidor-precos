#!/usr/bin/env python3
import http.client
import json

connection = http.client.HTTPConnection('localhost:3000')

headers = {'Content-type': 'application/json'}

higiene = [

{"nome": "desodorante", "local": "brasil", "preco":"10.69"},
{"nome": "desodorante", "local": "forte", "preco":"10.90"},
{"nome": "desodorante", "local": "forte", "preco": "9.90"},
{"nome": "escova-dente", "local": "bistek", "preco": "7.41"},
{"nome": "espuma barbear", "local": "bistek", "preco": "20"},
{"nome": "fralda", "local": "bistek", "preco": "0.88"},
{"nome": "gillete", "local": "forte", "preco":"4.83"},
{"nome": "lenco umedecido", "local": "bistek", "preco": "8.22"},
{"nome": "lenco umedecido", "local": "forte", "preco": "9.99"},
{"nome": "papel higienico", "local": "forte", "preco":"1.07"},
{"nome": "pasta-dente", "local": "bistek", "preco": "5.29"},
{"nome": "sabonete dove", "local": "forte", "preco": "2.29"},
{"nome": "sabonete-ju", "local": "bistek", "preco": "3.07"},
{"nome": "sabonete-ju", "local": "bistek", "preco": "3.29"},
{"nome": "sabonete liquido", "local": "bistek", "preco": "4.99"},
{"nome": "sabonete-liquido", "local": "forte", "preco":"5.49"},
{"nome": "sabonete", "local": "bistek", "preco": "2.69"},
{"nome": "shampoo juju 400ml", "local": "bistek", "preco": "17.97"},
{"nome": "shampoo juju 400ml", "local": "forte", "preco": "16.50"},
{"nome": "shampoo", "local": "forte", "preco":"6.99"},

]

limpeza = [

{"nome": "ajax", "local": "bistek", "preco": "2.97"},
{"nome": "ajax", "local": "forte", "preco": "3.75"},
{"nome": "ajax pesado", "local": "bistek", "preco": "5.35"},
{"nome": "ajax pesado", "local": "forte", "preco": "4.99"},
{"nome": "ajax pesado", "local": "forte", "preco":"4.99"},
{"nome": "ajax pesado", "local": "forte", "preco":"4.99"},
{"nome": "alcool-gel", "local": "bistek", "preco": "11.99"},
{"nome": "alcool", "local": "brasil", "preco":"5.49"},
{"nome": "alcool", "local": "forte", "preco":"4.99"},
{"nome": "detergente", "local": "bistek", "preco": "1.85"},
{"nome": "detergente", "local": "bistek", "preco": "1.85"},
{"nome": "detergente", "local": "forte", "preco":"1.49"},
{"nome": "detergente-maquina-louca", "local": "forte", "preco":"15.90"},
{"nome": "detergente-maquina-louca", "local": "forte", "preco":"15.90"},
{"nome": "detergente-maquina-louca", "local": "forte", "preco":"15.90"},
{"nome": "esponja", "local": "forte", "preco": "4.69"},
{"nome": "glicerina", "local": "bistek", "preco": "6.45"},
{"nome": "glicerina", "local": "brasil", "preco":"5.59"},
{"nome": "guardanapo", "local": "angeloni", "preco":"3.59"},
{"nome": "guardanapo", "local": "forte", "preco": "3.99"},
{"nome": "kiboa", "local": "bistek", "preco": "3.79"},
{"nome": "limpa vidros", "local": "bistek", "preco": "9.97"},
{"nome": "limpa vidros", "local": "forte", "preco": "7.59"},
{"nome": "omo", "local": "bistek", "preco": "17.97"},
{"nome": "omo", "local": "forte", "preco":"12.90"},
{"nome": "omo", "local": "forte", "preco": "17.50"},
{"nome": "omo", "local": "forte", "preco":"17.90"},
{"nome": "papel-higienico", "local": "bistek", "preco": "19.90"},
{"nome": "papel-manteiga", "local": "forte", "preco":"4.99"},
{"nome": "papel toalha", "local": "angeloni", "preco":"4.39"},
{"nome": "papel toalha", "local": "bistek", "preco": "3.49"},
{"nome": "papel toalha", "local": "bistek", "preco":"3.49"},
{"nome": "papel-toalha", "local": "bistek", "preco": "3.55"},
{"nome": "papel-toalha", "local": "forte", "preco": "4.29"},
{"nome": "perfex", "local": "forte", "preco":"4.99"},
{"nome": "perfex", "local": "forte", "preco": "6.39"},
{"nome": "pinho sol", "local": "forte", "preco":"6.89"},
{"nome": "plastico grande com 100", "local": "forte", "preco": "6.99"},
{"nome": "plastico grande com 100", "local": "forte", "preco":"6.99"},
{"nome": "plastico pequeno com 100", "local": "forte", "preco":"4.99"},
{"nome": "plastico pequeno com 100", "local": "forte", "preco": "5.59"},
{"nome": "sabonete-liquido", "local": "forte", "preco":"5.99"},
{"nome": "saco-lixo", "local": "forte", "preco":"10.90"},
{"nome": "saco-lixo", "local": "bistek", "preco": "9.9"},

]

alimentacao = [

{"nome": "acucar-refinado", "local": "forte", "preco":"1.85"},
{"nome": "acucar refinado", "local": "forte", "preco": "1.98"},
{"nome": "agua-coco", "local": "bistek", "preco": "2.99"},
{"nome": "agua-coco", "local": "forte", "preco":"6.89"},
{"nome": "alcatra", "local": "bistek", "preco": "25.98"},
{"nome": "alho", "local": "forte", "preco": "38.90"},
{"nome": "arroz arboreo 1kg", "local": "forte", "preco":"13.69"},
{"nome": "arroz", "local": "forte", "preco":"3.55"},
{"nome": "arroz", "local": "forte", "preco":"3.85"},
{"nome": "arroz", "local": "forte", "preco":"4.19"},
{"nome": "arroz multigraos 500g", "local": "forte", "preco":"8.20"},
{"nome": "arroz raris 500g", "local": "forte", "preco": "8.29"},
{"nome": "azeite", "local": "angeloni", "preco":"15.34"},
{"nome": "azeite", "local": "bistek", "preco": "19.87"},
{"nome": "azeite", "local": "forte", "preco":"16.90"},
{"nome": "azeite", "local": "forte", "preco": "17.50"},
{"nome": "banana", "local": "big", "preco": "3.59"},
{"nome": "banana", "local": "bistek", "preco": "3.98"},
{"nome": "banana", "local": "forte", "preco":"2.79"},
{"nome": "batata palha", "local": "bistek", "preco": "2.99"},
{"nome": "bicarbonato-sodio", "local": "bistek", "preco": "3.69"},
{"nome": "biscoito de arroz", "local": "bistek", "preco": "3.98"},
{"nome": "biscoito de arroz", "local": "bistek", "preco": "5.79"},
{"nome": "biscoito de arroz", "local": "forte", "preco": "4.28"},
{"nome": "biscoito zooreta", "local": "bistek", "preco": "1.79"},
{"nome": "cafe 500g", "local": "forte", "preco":"10.40"},
{"nome": "cafe 500g", "local": "forte", "preco":"10.40"},
{"nome": "cafe aralto", "local": "bistek", "preco": "8.48"},
{"nome": "cafe aralto", "local": "forte", "preco": "8.79"},
{"nome": "cafe aralto", "local": "forte", "preco":"8.99"},
{"nome": "cafe aralto", "local": "forte", "preco":"8.99"},
{"nome": "cenoura", "local": "bistek", "preco": "2.98"},
{"nome": "costela suina sem tempero", "local": "angeloni", "preco": "17.45"},
{"nome": "couve-flor", "local": "bistek", "preco": "4.49"},
{"nome": "coxao mole", "local": "angeloni", "preco":"21.39"},
{"nome": "coxao mole", "local": "angeloni", "preco": "24.59"},
{"nome": "cream-cheese", "local": "bistek", "preco":"3.93"},
{"nome": "creme de leite fresco", "local": "bistek", "preco": "15.97"},
{"nome": "creme de leite", "local": "forte", "preco":"1.55"},
{"nome": "creme-leite", "local": "angeloni", "preco":"1.55"},
{"nome": "curcuma", "local": "bistek", "preco": "2.39"},
{"nome": "detergente", "local": "forte", "preco": "1.45"},
{"nome": "essencia-baunilha", "local": "brasil", "preco":"6.99"},
{"nome": "farelo de aveia 200g", "local": "bistek", "preco": "6.75"},
{"nome": "feijao", "local": "brasil", "preco":"4.39"},
{"nome": "feijao", "local": "forte", "preco":"4.19"},
{"nome": "file de peito de frango", "local": "bistek", "preco": "9.97"},
{"nome": "file de peito de frango", "local": "forte", "preco": "12.97"},
{"nome": "gelatina", "local": "bistek", "preco": "4.89"},
{"nome": "iogurte grego", "local": "bistek", "preco": "1.89"},
{"nome": "iogurte", "local": "forte", "preco": "1.99"},
{"nome": "laranja", "local": "big", "preco": "3.86"},
{"nome": "leite-condensado-lata", "local": "bistek", "preco": "6.57"},
{"nome": "leite condensado", "local": "forte", "preco":"4.99"},
{"nome": "leite de coco", "local": "forte", "preco": "3.59"},
{"nome": "leite", "local": "bistek", "preco": "2.97"},
{"nome": "leite", "local": "brasil", "preco":"3.29"},
{"nome": "leite", "local": "forte", "preco": "3.19"},
{"nome": "leite", "local": "forte", "preco":"3.19"},
{"nome": "leite-ninho", "local": "brasil", "preco":"9.90"},
{"nome": "leite ninho", "local": "forte", "preco": "11.90"},
{"nome": "limao", "local": "big", "preco": "3.98"},
{"nome": "macarrao penne 500g", "local": "forte", "preco":"2.39"},
{"nome": "macarrao yakissoba", "local": "bistek", "preco": "4.89"},
{"nome": "macarrao yakissoba", "local": "forte", "preco":"4.19"},
{"nome": "maca verde", "local": "bistek", "preco": "7.99"},
{"nome": "macrovita-1l", "local": "bistek", "preco": "11.29"},
{"nome": "manteiga", "local": "forte", "preco":"5.99"},
{"nome": "manteiga", "local": "forte", "preco":"6.49"},
{"nome": "manteiga", "local": "forte", "preco": "6.89"},
{"nome": "manteiga", "local": "forte", "preco":"6.89"},
{"nome": "milho pipoca", "local": "forte", "preco": "2.85"},
{"nome": "milho-pipoca", "local": "forte", "preco":"2.85"},
{"nome": "milho pipoca", "local": "forte", "preco":"2.85"},
{"nome": "molho shoyo", "local": "bistek", "preco": "2.79"},
{"nome": "molho yakissoba", "local": "bistek", "preco": "2.79"},
{"nome": "mortadela", "local": "bistek", "preco": "5.93"},
{"nome": "nutella", "local": "forte", "preco":"13.90"},
{"nome": "nutella", "local": "forte", "preco":"14.50"},
{"nome": "oleo", "local": "angeloni", "preco":"5.99"},
{"nome": "oleo", "local": "big", "preco": "6.74"},
{"nome": "oleo", "local": "forte", "preco":"4.98"},
{"nome": "oleo", "local": "forte", "preco": "5.65"},
{"nome": "ovomaltine", "local": "forte", "preco": "13.90"},
{"nome": "pao de castanha e nozes", "local": "bistek", "preco": "8.29"},
{"nome": "passata", "local": "forte", "preco": "5.49"},
{"nome": "passata", "local": "forte", "preco":"5.49"},
{"nome": "passata", "local": "forte", "preco":"5.49"},
{"nome": "passata", "local": "forte", "preco":"5.99"},
{"nome": "patinho", "local": "angeloni", "preco":"23.59"},
{"nome": "polvilho-azedo", "local": "bistek", "preco": "7.99"},
{"nome": "polvilho-azedo", "local": "bistek", "preco": "8.59"},
{"nome": "polvilho-doce", "local": "bistek", "preco": "3.98"},
{"nome": "polvilho-doce", "local": "bistek", "preco": "3.99"},
{"nome": "queijo gorgonzola", "local": "bistek", "preco": "55.90"},
{"nome": "queijo gorgonzola", "local": "forte", "preco": "43.90"},
{"nome": "queijo-gorgonzola", "local": "forte", "preco":"44.99"},
{"nome": "queijo grana", "local": "forte", "preco": "79.99"},
{"nome": "queijo-mussarela", "local": "bistek", "preco": "25.97"},
{"nome": "queijo mussarela", "local": "forte", "preco": "19.99"},
{"nome": "queijo mussarela", "local": "forte", "preco":"20.79"},
{"nome": "queijo-mussarela", "local": "forte", "preco":"22.90"},
{"nome": "queijo-mussarela", "local": "forte", "preco":"23.90"},
{"nome": "queijo-parmesao", "local": "forte", "preco":"2.98"},
{"nome": "queijo-parmesao", "local": "forte", "preco":"2.98"},
{"nome": "queijo parmesao", "local": "forte", "preco": "2.99"},
{"nome": "queijo-prato", "local": "bistek", "preco": "27.97"},
{"nome": "queijo ralado", "local": "bistek", "preco": "2.99"},
{"nome": "sabonete liquido", "local": "forte", "preco": "5.99"},
{"nome": "salame", "local": "big", "preco": "4.78"},
{"nome": "salame", "local": "bistek", "preco": "5.47"},
{"nome": "salame", "local": "forte", "preco":"5.89"},
{"nome": "salame", "local": "forte", "preco":"5.89"},
{"nome": "salame", "local": "forte", "preco": "5.98"},
{"nome": "salgadinho", "local": "forte", "preco":"5.59"},
{"nome": "salgadinho", "local": "forte", "preco":"5.79"},
{"nome": "salgadinho", "local": "forte", "preco":"5.79"},
{"nome": "salgadinho", "local": "bistek", "preco": "4.99"},
{"nome": "salgadinho", "local": "bistek", "preco": "6.25"},
{"nome": "salgadinho", "local": "forte", "preco": "5.59"},
{"nome": "salgadinho", "local": "forte", "preco":"5.90"},
{"nome": "sal", "local": "bistek", "preco": "3.69"},
{"nome": "sal", "local": "forte", "preco":"2.55"},
{"nome": "sal", "local": "forte", "preco": "3.29"},
{"nome": "semolina", "local": "bistek", "preco": "4.48"},
{"nome": "sobrecoxa", "local": "bistek", "preco": "6.97"},
{"nome": "sobrecoxa", "local": "bistek", "preco": "7.97"},
{"nome": "suco de uva 1.5L", "local": "forte", "preco":"9.99"},
{"nome": "suco-uva-1.5l", "local": "angeloni", "preco":"8.94"},
{"nome": "suco uva 1.5L", "local": "forte", "preco": "9.90"},
{"nome": "tomate cereja", "local": "angeloni", "preco": "5.35"},
{"nome": "tomate", "local": "bistek", "preco": "8.29"},
{"nome": "torrada", "local": "bistek", "preco": "1.99"},
{"nome": "uva", "local": "bistek", "preco": "7.99"},

]

for v in limpeza:
    l = v['nome'].replace(" ", "%20")
    connection.request('POST', '/produtos/' +  l + '/historico', json.dumps({"preco":v['preco'], "local":v['local'], "obs":"", "categoria":"limpeza"}), headers)
    response = connection.getresponse()
    response.read()
    endpoint = '/produtos/' + l
    connection.request('GET', endpoint)
    response = connection.getresponse()
    print(endpoint + ": " + response.read().decode())

for v in alimentacao:
    l = v['nome'].replace(" ", "%20")
    connection.request('POST', '/produtos/' +  l + '/historico', json.dumps({"preco":v['preco'], "local":v['local'], "obs":"", "categoria":"alimentacao"}), headers)
    response = connection.getresponse()
    response.read()
    endpoint = '/produtos/' + l
    connection.request('GET', endpoint)
    response = connection.getresponse()
    print(endpoint + ": " + response.read().decode())

for v in higiene:
    l = v['nome'].replace(" ", "%20")
    connection.request('POST', '/produtos/' +  l + '/historico', json.dumps({"preco":v['preco'], "local":v['local'], "obs":"", "categoria":"higiene"}), headers)
    response = connection.getresponse()
    response.read()
    endpoint = '/produtos/' + l
    connection.request('GET', endpoint)
    response = connection.getresponse()
    print(endpoint + ": " + response.read().decode())


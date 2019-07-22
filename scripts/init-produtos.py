#!/usr/bin/env python3
import http.client
import json

connection = http.client.HTTPConnection('localhost:3000')

headers = {'Content-type': 'application/json'}

produtos = ["ajax", "alcool", "pinho-sol", "x14", "kiboa", "limpa-vidros", "anti-mofo-produto", "detergente", "papel-toalha", "guardanapo", "farelo-de-aveia", "salgadinho", "manteiga", "arroz", "feijao", "sal", "acucar-refinado", "acucar-mascavo", "acucar-demerara", "pipoca", "sobrecoxa", "sassami", "coxao-mole", "alcatra", "file-mignon", "maminha", "arroz-risoto", "biscoito-arroz", "biscoito-zooreta", "farinha-trigo", "cafe", "extrato-tomate", "leite-condensado", "passata", "creme-leite", "leite-coco", "extrato-baunilha", "fermento-biologico", "ovo", "sabonete", "sabonete-juju", "shampoo", "shampoo-juju", "lenco-umedecido", "papel-higienico", "gillete", "gillete-clarissa", "espuma-barbear", "escova-dentes", "escova-dentes-juju", "pasta-dentes", "pasta-dentes-juju", "condicionador", "condicionador-juju", "queijo-mussarela", "queijo-gorgonzola", "requeijao", "salame", "iogurte", "macarrao", "file-mignon-porco", "queijo-parmesao", "sal", "arroz", "canjica", "cafe", "leite", "nutella", "coco", "passata", "lava-louca", "desodorate", "agua-coco", "sabonete-liquido", "canela" 
]
for p in produtos:
    print('Nao inserimos mais produtos sem historico: ' + p)
    #connection.request('POST', '/produtos', json.dumps({"nome":p, "sumario": "", "melhor-preco": "9999999" "historico": []}), headers)
    #response = connection.getresponse()
    #response.read()

#connection.request('GET', '/produtos')
#response = connection.getresponse()
#print(response.read().decode())

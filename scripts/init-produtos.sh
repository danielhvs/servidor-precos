#!/bin/bash
prods=(
papel-toalha
papel-higienico
ajax
x14
alcool
pinho-sol
kiboa
)

for p in ${prods[@]}; do
curl -s -H "Content-Type: application/json"  --request POST -d "{\"$p\": {\"obs\":\"obs-$p\" \"historico\":[]}}" localhost:3000/produtos
done


curl localhost:3000/produtos

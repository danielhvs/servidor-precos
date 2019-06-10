#!/bin/bash
local="forte"

prods=(
(banana 123)
(risoto 456)
)

for p in ${prods[@]}; do
    curl -v -H "Content-Type: application/json"  --request POST -d "{\"preco\": $p[1] \"local\":\"$local\"}" localhost:3000/produtos/$p[0]/historico
done

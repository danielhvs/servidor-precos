#!/bin/bash

echo local:
read local

while true; do
    echo nome:
    read nome
    echo preco:
    read preco
    echo {\"nome\": \"$nome\", \"local\": \"$local\", \"preco\": \"$preco\"} >> ../resources/produtos-boot.json
done


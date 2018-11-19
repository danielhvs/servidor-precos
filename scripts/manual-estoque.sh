#!/bin/bash

while true; do
    echo nome:
    read nome
    echo estoque:
    read estoque
    echo {\"nome\": \"$nome\", \"estoque\": \"$estoque\"} >> ../resources/estoque-boot.json
done


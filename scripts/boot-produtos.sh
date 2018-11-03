#!/bin/bash
filename="$1"
echo $filename
echo Cadastrando $filename...
while read -r line
do
    json=$line
    curl  --header "Content-Type: application/json" --data "$json" --request POST http://localhost:3000/cadastra
    #curl  --header "Content-Type: application/json" --data "$json" --request POST https://infinite-crag-89428.herokuapp.com/cadastra
done < "$filename"

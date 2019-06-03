#!/bin/bash
filename="$1"
echo $filename
echo Cadastrando produtos $filename...
curl  --header "Content-Type: application/json" --data @$filename --request POST http://localhost:3000/boot-cadastra
#curl  --header "Content-Type: application/json" --data "$json" --request POST https://infinite-crag-89428.herokuapp.com/boot-cadastra

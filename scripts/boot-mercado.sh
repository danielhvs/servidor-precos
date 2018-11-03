#!/bin/bash
filename="$1"
echo $filename
echo Cadastrando mercado $filename...
curl  --header "Content-Type: application/json" --data @$filename --request POST http://localhost:3000/boot-mercado
#curl  --header "Content-Type: application/json" --data "$json" --request POST https://infinite-crag-89428.herokuapp.com/boot-mercado

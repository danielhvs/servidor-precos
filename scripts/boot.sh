#!/bin/bash
filename="$1"
echo $filename
echo "OK"?
read
while read -r line
do
    json=$line
    curl  --header "Content-Type: application/json" --data "$json" --request POST https://infinite-crag-89428.herokuapp.com/cadastra
done < "$filename"

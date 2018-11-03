#!/bin/bash
filename="../resources/mercado-boot.json"
filename2="../resources/produtos-boot.json"
echo boot-mercado: $filename
echo boot-produtos: $filename2
echo "OK"?
read

echo "Removendo tudo..."
echo
./remove.sh
echo
echo "Boot mercado..."
echo
./boot-mercado.sh $filename
echo
echo "Boot produtos..."
echo
./boot-produtos.sh $filename2

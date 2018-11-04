#!/bin/bash
filename="../resources/mercado-boot.json"
produtos=`ls ../resources/produtos-*.json`
echo boot-mercado: $filename
echo boot-produtos: $produtos
echo "OK"?
read

echo "Removendo tudo..."
echo
./remove.sh
echo
echo "Boot mercado..."
echo
./boot-mercado.sh $filename

for f in $produtos; do
	echo
	echo "Boot produtos $f ..."
	echo
	./boot-produtos.sh $f
done

#!/bin/bash
filename="../resources/estoque-boot.json"
produtos=`ls ../resources/produtos-*.json`
echo boot-estoque: $filename
echo boot-produtos: $produtos
echo "OK"?
read

echo "Removendo tudo..."
echo
./remove.sh
echo
echo "Boot estoque"
echo
./boot-estoque.sh $filename

for f in $produtos; do
	echo
	echo "Boot produtos $f ..."
	echo
	./boot-produtos.sh $f
done

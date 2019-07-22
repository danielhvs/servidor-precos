#!/bin/bash
echo " removendo..."
sh remove.sh &&
echo " inserindo sumarios"
./init-sumario.py 
echo " inserindo historicos..."
./init-historico.py 

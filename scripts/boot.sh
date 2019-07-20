#!/bin/bash
sh remove.sh &&
echo
echo " inserindo produtos..."
./init-produtos.py &&
echo
echo " inserindo historicos..."
./init-historico.py 

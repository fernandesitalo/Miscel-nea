#!/bin/bash
TEXTO="Primeiro script shell, fazendo testes!"
echo $TEXTO

COUNT=0
for i in `ls`
do 
echo "ACHEI ESSE AQUIVO AQUI $i"
COUNT=$((COUNT+1))
done
COUNT=$((COUNT-1))
if [ "$COUNT" -eq 0 ]; then
echo "Nenhum arquivo encontrado"
elif [ "$COUNT" -eq 1 ]; then
echo "Apenas 1 arquivo foi encontrado"
else 
echo "foram encontrados $COUNT arquivos"
fi
#!/bin/bash 

#variaveis
pasta_relatorios="/home/eduardo/ecommerce/vendas/backup"

arquivo_de_saida="relatorio_final.txt"


#loop usado para buscar todos arquivo com final .txt dentro do diretorio aonde está declarada a variavel  
for file in "$pasta_relatorios"/relatorio_*.txt; do
    if [ -f "$file" ]; then
        cat "$file" >> "$arquivo_de_saida"
        echo "Adicionado todos os relatorios ao relatorio final"
        echo -e "--------------------------------------------------------------" >> "$arquivo_de_saida"
    else
        echo "Arquivo não encontrado ou não é um arquivo regular"
    fi
done

    echo "Relatórios unidos em $arquivo_de_saida"

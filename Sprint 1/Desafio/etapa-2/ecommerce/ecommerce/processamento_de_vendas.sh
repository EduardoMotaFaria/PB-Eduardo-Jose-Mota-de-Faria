#!/bin/bash

#saida do codigo
cd /home/eduardo/ecommerce/ || exit 

#criação de pastas
if [ ! -d ~/ecommerce/vendas ]; then
     mkdir ~/ecommerce/vendas
     echo "diretorio vendas criado"
else
     echo "diretorio vendas ja existente"
fi

if [ !  -f ~/ecommerce/vendas/dados_de_vendas.csv ]; then
     cp dados_de_vendas.csv ~/ecommerce/vendas
     echo "arquivo dados_de_vendas.csv copiado para diretorio vendas"
 else
     echo "arquivo dados_de_vendas.csv ja existente no diretorio vendas "
fi

if [ ! -d ~/ecommerce/vendas/backup ]; then
     mkdir ~/ecommerce/vendas/backup
     echo "diretorio backup criado"
else
     echo "diretorio backup ja existente"
fi

if [ ! -f ~/ecommerce/vendas/backup/dados_de_vendas.csv ]; then
     cp dados_de_vendas.csv ~/ecommerce/vendas/backup
     echo "arquivo  dados_de_vendas.csv copiado para diretorio backup"
else
     echo "arquivo dados_de_vendas.csv  ja existente no diretorio backup"
fi
#renomeando o arquivo de dados_de_vendas.csv para dados-YYYYMMDD.csv
     mv ~/ecommerce/vendas/backup/dados_de_vendas.csv ~/ecommerce/vendas/backup/dados-$(date +%Y%m%d).csv
     echo "arquivo dados_de_vendas.csv renomeado para dados-YYYYMMDD.csv"

#renomeando  o arquivo de dados-YYYYMMDD.csv para backup-dados-YYYYMMDD
     mv ~/ecommerce/vendas/backup/dados-$(date +%Y%m%d).csv ~/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv
     echo "arquivo dados-YYYYMMDD.csv renomeado  para backup-dados-YYYYMMDD.csv"

#criação do relatorio 
data=$(date +%Y%m%d_%H%M%S)
base_nome_arquivo="relatorio_$data"

if [ ! -f ~/ecommerce/vendas/backup/"$base_nome_arquivo".txt ]; then
    touch ~/ecommerce/vendas/backup/"$base_nome_arquivo".txt
    echo "Novo relatorio "$base_nome_arquivo" criado"
fi



# informaçoes do relatorio
     echo "Data do Sistema" $(date +"%Y/%m/%d %H:%M") >> /home/eduardo/ecommerce/vendas/backup/"$base_nome_arquivo".txt
     echo "" >> /home/eduardo/ecommerce/vendas/backup/"$base_nome_arquivo".txt
     echo "data do primeiro registro de venda" >> /home/eduardo/ecommerce/vendas/backup/"$base_nome_arquivo".txt
     head -n 2 ~/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv | grep -oE '[0-9]{2}/[0-9]{2}/[0-9]{4}$' >> /home/eduardo/ecommerce/vendas/backup/"$base_nome_arquivo".txt
     echo "" >> /home/eduardo/ecommerce/vendas/backup/"$base_nome_arquivo".txt
     echo "data do ultimo registro de venda" >> /home/eduardo/ecommerce/vendas/backup/"$base_nome_arquivo".txt
     tail -n 1 ~/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv | grep -oE '[0-9]{2}/[0-9]{2}/[0-9]{4}$' >> /home/eduardo/ecommerce/vendas/backup/"$base_nome_arquivo".txt
     echo "" >> /home/eduardo/ecommerce/vendas/backup/"$base_nome_arquivo".txt

#variavel do local das quantidades de itens
arquivo="~/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv"

arquivo=$(echo "$arquivo" | sed "s|~|$HOME|")

total_de_itens_diferentes=$(tail -n +2 "$arquivo" |cut -d ',' -f 2 | sort | uniq | wc -l)

    echo "total de itens diferentes vendidos: $total_de_itens_diferentes" >> /home/eduardo/ecommerce/vendas/backup/"$base_nome_arquivo".txt
    echo "" >> /home/eduardo/ecommerce/vendas/backup/"$base_nome_arquivo".txt
    echo "as dez linhas do arquivo são:" >> /home/eduardo/ecommerce/vendas/backup/"$base_nome_arquivo".txt 
    head -n 11 ~/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv >> /home/eduardo/ecommerce/vendas/backup/"$base_nome_arquivo".txt

#zip arquivo
zip -r /home/eduardo/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d) /home/eduardo/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv
    echo "arquivo backup-dados-$(date +%Y%m%d) zipado"
#deletando os arquivos
    rm ~/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv
    rm ~/ecommerce/vendas/dados_de_vendas.csv
    echo "arquivo backup-dados-$(date +%Y%m%d).csv e arquivo dados_de_vendas.csv deletado"


SELECT 
    v.cdpro,
    v.nmcanalvendas,
    v.nmpro,
    SUM(v.qtd) AS quantidade_vendas
FROM 
    tbvendas v
WHERE 
    v.status = 'Concluído'
    AND (v.nmcanalvendas = 'Ecommerce' OR v.nmcanalvendas = 'Matriz')
GROUP BY 
    v.cdpro, v.nmcanalvendas, v.nmpro
ORDER BY 
    quantidade_vendas ASC
LIMIT 10;
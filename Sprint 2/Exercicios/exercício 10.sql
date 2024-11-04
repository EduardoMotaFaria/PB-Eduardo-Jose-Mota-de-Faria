SELECT 
    ven.nmvdd AS vendedor,
    SUM(v.qtd * v.vrunt) AS valor_total_vendas,
    ROUND(SUM(v.qtd * v.vrunt) * ven.perccomissao / 100, 2) AS comissao
FROM 
    tbvendas v
JOIN 
    tbvendedor ven ON v.cdvdd = ven.cdvdd
WHERE 
    v.status = 'Concluído'
GROUP BY 
    ven.cdvdd, ven.nmvdd
ORDER BY 
    comissao DESC;
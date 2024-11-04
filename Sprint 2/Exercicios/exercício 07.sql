SELECT 
    tbvendedor.cdvdd,
    tbvendedor.nmvdd
FROM 
    tbvendedor
JOIN 
    tbvendas ON tbvendedor.cdvdd = tbvendas.cdvdd
WHERE 
    tbvendas.status = 'concluída'
GROUP BY 
    tbvendedor.cdvdd, tbvendedor.nmvdd
ORDER BY 
    COUNT(tbvendas.cdevn) DESC
LIMIT 1;
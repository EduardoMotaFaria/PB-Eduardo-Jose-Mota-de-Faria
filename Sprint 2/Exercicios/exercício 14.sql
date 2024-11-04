SELECT 
    estado,
    ROUND(AVG(qtd * vrunt), 2) AS gastomedio
FROM 
    tbvendas
WHERE 
    status = 'Concluído'
GROUP BY 
    estado
ORDER BY 
    gastomedio DESC;
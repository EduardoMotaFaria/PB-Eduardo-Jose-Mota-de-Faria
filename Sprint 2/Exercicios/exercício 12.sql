WITH VendedorMenorVenda AS (
    SELECT 
        cdvdd,
        SUM(qtd * vrunt) AS valor_total_vendas
    FROM 
        tbvendas
    WHERE 
        status = 'Concluído'
    GROUP BY 
        cdvdd
    HAVING 
        valor_total_vendas > 0
    ORDER BY 
        valor_total_vendas ASC
    LIMIT 1
)
SELECT 
    d.cddep,
    d.nmdep,
    d.dtnasc,
    (SELECT SUM(qtd * vrunt) FROM tbvendas v WHERE v.cdvdd = vm.cdvdd AND v.status = 'Concluído') AS valor_total_vendas
FROM 
    tbdependente d
JOIN 
    VendedorMenorVenda vm ON d.cdvdd = vm.cdvdd;
SELECT ven.cdvdd, ven.nmvdd
FROM tbvendas t
JOIN tbvendedor ven ON t.cdvdd = ven.cdvdd
WHERE t.status = 'Concluído'
GROUP BY ven.cdvdd, ven.nmvdd
ORDER BY COUNT(*) DESC
LIMIT 1;
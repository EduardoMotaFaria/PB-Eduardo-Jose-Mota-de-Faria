SELECT 
    autor.codAutor,
    autor.nome,
    autor.nascimento,
    COUNT(livro.cod) AS quantidade
FROM 
    autor
LEFT JOIN 
    livro ON autor.codAutor = livro.autor
GROUP BY 
    autor.codAutor, autor.nome, autor.nascimento
ORDER BY 
    autor.nome ASC;
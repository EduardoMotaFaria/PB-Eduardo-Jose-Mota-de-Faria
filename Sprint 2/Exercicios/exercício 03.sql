SELECT 
    COUNT(livro.cod) AS quantidade,
    editora.nome,
    endereco.estado,
    endereco.cidade
FROM 
    livro
LEFT JOIN 
    editora ON livro.editora = editora.codEditora
LEFT JOIN 
    endereco ON editora.endereco = endereco.codEndereco
GROUP BY 
    editora.codEditora, editora.nome, endereco.estado, endereco.cidade
ORDER BY 
    quantidade DESC
LIMIT 5;
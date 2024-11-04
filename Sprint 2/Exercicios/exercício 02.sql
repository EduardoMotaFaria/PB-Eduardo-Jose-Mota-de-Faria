SELECT 
    COUNT(livros.cod) AS quantidade,
    editoras.nome,
    editoras.estado,
    editoras.cidade
FROM 
    livros
JOIN 
    editoras ON livros.cod = editoras.id
GROUP BY 
    editoras.codeditora, editoras.nome, editoras.estado, editoras.cidade
ORDER BY 
    quantidade DESC
LIMIT 5;
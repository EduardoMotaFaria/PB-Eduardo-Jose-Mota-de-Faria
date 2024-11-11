--Create View
CREATE VIEW	dim_Cliente AS
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
From Cliente c ;

CREATE VIEW dim_Vendedor AS
SELECT idVendedor,nomeVendedor,sexoVendedor,estadoVendedor
FROM Vendedor v ;

--Utilizei um JOIN para visualizar os dados dentro da tabela dim_Carro. 
--Pois não vejo necessidade de uma VIEW propia pra ele, visando que o modelo dimensional é focado em consulta
CREATE VIEW dim_Carro AS
SELECT 
    idCarro,classiCarro, kmCarro, marcaCarro, modeloCarro,anoCarro,co.idCombustivel,co.tipoCombustivel
FROM Carro c 
LEFT JOIN Combustivel co ON c.idCombustivel = co.idCombustivel;

CREATE VIEW fato_Locacao AS
SELECT idLocacao,dataLocacao,horaLocacao,qtdDiaria,vlrDiaria,dataEntrega,horaEntrega,dc.idCliente,dca.idCarro,dv.idVendedor
FROM Locacao l 
LEFT JOIN dim_Cliente dc ON l.idCliente = dc.idCliente
LEFT JOIN dim_Carro dca ON l.idCarro = dca.idCarro
LEFT JOIN dim_Vendedor dv ON l.idVendedor = dv.idVendedor

--Visualização das VIEWS 
SELECT *
FROM fato_Locacao;

SELECT * 
FROM dim_Cliente;

SELECT *
FROM dim_Vendedor;

SELECT *
FROM dim_Carro;

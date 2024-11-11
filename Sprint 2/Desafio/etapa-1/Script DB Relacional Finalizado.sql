--Creação das tabelas
CREATE TABLE Cliente(
idCliente INT PRIMARY KEY,
nomeCliente VARCHAR(100),
cidadeCliente VARCHAR(40),
estadoCliente VARCHAR(40),
paisCliente VARCHAR(40)
);

CREATE TABLE Carro(
idCarro INT PRIMARY KEY,
classiCarro VARCHAR(50),
kmCarro INT,
marcaCarro VARCHAR(80),
modeloCarro VARCHAR(80),
anoCarro INT,
idCombustivel INT,
FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
);
        
CREATE TABLE Vendedor( 
idVendedor INT PRIMARY KEY,
nomeVendedor VARCHAR(100),
sexoVendedor VARCHAR(2),
estadoVendedor VARCHAR(100)
);

CREATE TABLE Combustivel(
idCombustivel INT PRIMARY KEY,
tipoCombustivel VARCHAR(20)
);

CREATE TABLE Locacao(
idLocacao INT PRIMARY KEY,
dataLocacao DATE,
horaLocacao TIME,
qtdDiaria INT,
vlrDiaria DECIMAL(18,2),
dataEntrega DATE,
horaEntrega TIME,
idCliente INT,
idCarro INT,
idVendedor INT,
idCombustivel INT,

FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);

-- Inserção dos dados
INSERT INTO Cliente(idCliente,nomeCliente,cidadeCliente,estadoCliente,paisCliente)
SELECT DISTINCT idCliente,
                nomeCliente,
                cidadeCliente,
                estadoCliente,
                paisCliente
FROM tb_locacao

--Group BY Utilizado para agrupar todos os registro fora o MAX(kmCarro)
INSERT INTO Carro(idCarro,classiCarro,kmCarro,marcaCarro,modeloCarro,anoCarro)
SELECT DISTINCT idCarro,
                classiCarro,
                MAX(kmCarro),
                marcaCarro,
                modeloCarro,
                anoCarro
FROM tb_locacao
GROUP BY idCarro,classiCarro,marcaCarro,modeloCarro,anoCarro 

INSERT INTO Vendedor(idVendedor,nomeVendedor,sexoVendedor,estadoVendedor)
SELECT DISTINCT idVendedor,nomeVendedor,sexoVendedor,estadoVendedor
FROM tb_locacao

INSERT INTO Combustivel(idCombustivel,tipoCombustivel)
SELECT DISTINCT idCombustivel,tipoCombustivel
FROM tb_locacao

INSERT INTO Locacao (idLocacao,dataLocacao,horaLocacao,qtdDiaria,vlrDiaria,dataEntrega,horaEntrega,idCliente,idCarro,idVendedor,idCombustivel)
SELECT DISTINCT idLocacao,dataLocacao,horaLocacao,qtdDiaria,vlrDiaria,dataEntrega,horaEntrega,idCliente,idCarro ,idVendedor,idCombustivel
FROM tb_locacao

--Tratamento dos dados
UPDATE Vendedor 
SET sexoVendedor = 'M'
WHERE sexoVendedor = 0;

UPDATE Vendedor 
SET sexoVendedor = 'F'
WHERE sexoVendedor = 1;

UPDATE Locacao 
SET dataLocacao = SUBSTR(dataLocacao, 1, 4) || '-' || 
                  SUBSTR(dataLocacao, 5, 2) || '-' || 
                  SUBSTR(dataLocacao, 7, 2)
WHERE LENGTH(dataLocacao) = 8;

UPDATE Locacao
SET dataEntrega = SUBSTR(dataEntrega, 1, 4) || '-' || 
                  SUBSTR(dataEntrega, 5, 2) || '-' || 
                  SUBSTR(dataEntrega, 7, 2)
WHERE LENGTH (dataEntrega) = 8;

UPDATE Locacao 
SET horaLocacao = '0' || horaLocacao 
WHERE LENGTH(horaLocacao) = 4;

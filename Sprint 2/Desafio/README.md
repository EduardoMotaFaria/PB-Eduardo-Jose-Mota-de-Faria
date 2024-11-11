# Objetivo

O objetivo desta Sprint 2 foi realizar um desafio em SQL. Onde constituia em normalizar um Banco de Dados Relacional de uma concessionaria, aplicando as formas normais e depois converter esse modelo Relacional para um modelo Dimensional. Criação das estruturas e elaborar a modelagem de dados. 

# Etapas


1. Primeira etapa foi entender os atributos que contia na tabela `tb_Locacao`, e logo percebi que a formatação dos campos DATE estava errada, e utilizando o DBeaver foi fácil alterar a visualização, seguindo o caminho abaixo: 

* Botão direito do mouse na coluna que deseja alterar.
* Visualizar/Formatar, Fomato de exibição do valor, Nativo do banco de dados.

![Formatação das Datas](../Evidencias/Formatação%20das%20Datas.jpg)

2. Depois de entender os atributos, foi notado um nome comum entre eles, que são `Cliente`, `Vendedor` e `Carro`. Percebendo isso, foi criado tabelas para cada respectivo nome. Já Aplicando a `1FN` que exige que os dados estejam organizado de modo Atómico, para eliminar duplicidade. Feito isso a maioria dos atributos foram alocados as sua respectiva entidade, e ficou mais fácil a visualização dos outros atributos `Entrega`, `Locação`, `Diaria`. Foi criado uma tabela `Locacao`, com todos os outros atributos nela, já que ela seria a principal e comandaria outras tabelas.

* OBS: (Nesta etapa `idCombustivel` e `tipoCombustivel` estava na entidade `Carro`)

![Criação das tabelas](../Evidencias/Criação%20das%20tabelas%20Cliente,%20Vendedor%20e%20Carro.jpg)

3. Logo em seguida da criação das tabelas, o objetivo era enviar os dados da `tb_Locacao` para cada tabela. foi utilizado o comando `INSERT`, e depois de pesquisar e cogitar inserir os dados manualmente, conheci o comando `SELECT DISTINCT` que foi utilizado para remover as duplicidades que contia na tabela `tb_Locacao`, assim aplicando a `1FN`.

![Inserção dos Dados](../Evidencias/Inserção%20de%20Dados.jpg)

4. Feito isso, chegamos na `2FN` e `3FN`, que exige que os atributos não-chave devem depender exclusivamente da `PK`. Vemos que em `Carro` existe uma coluna `idCombustivel` que não é uma `PK`, mas ela determina outra coluna `tipoCombustivel`, que infringe a `3FN`.

Para resolver isso, foi criado uma tabela `Combustivel` que assim fazia referência a tabela `Carro`. 

![Criação da Tabela Combustivel](../Evidencias/Criação%20da%20Tabela%20%20Combustivel.jpg)

5. Nesta etapa foi referenciado todas as tabelas na tabela `Locacao`, utilizando a `FK`.

![Criação das FK](../Evidencias/Criação%20das%20FK.jpg)

6. Na última etapa foi notado que os dados `DATE` e `TIME`, não estava no formato padrão `ISO`, a data estava no formato YYYYMMDD, e o correto no padrão `ISO` seria YYYY-MM-DD. Nos dados `TIME` percebemos que a hora está no formato H:MM, enquanto que o formato correto seria HH:MM. Logo em seguida foi notado que o formato na coluna `sexoVendedor` estava no formato 0 e 1. O que fica muito confuso para entendimento. 

Para resolver esse problema utilizei o comando `UPDATE`. 

![Tratamento de Dados](../Evidencias/Tratamento%20de%20Dados.jpg)

Explicado o Desafio o diagrama final ficou do seguinte modo: 

![Modelagem Relacional](../Evidencias/Modelagem%20DB%20Relacional.jpg)




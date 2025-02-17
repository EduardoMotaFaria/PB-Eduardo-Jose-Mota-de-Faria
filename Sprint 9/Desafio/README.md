# Objetivo

O objetivo da `Sprint 09`, era a `Modelagem de dados`, baseando-se na modelagem `dimensional` com base na Análises que foi proposta nas Sprints anteriores. Objetivo era também particionar o `parquet` de acordo com a Modelagem de dados, Criar os `Crawlers` e gerar as Tabelas para leitura do `Athena`.

Além disso, ao longo da Sprint 09, tomei a liberdade de mudar a minha análise para melhorar o storytelling  com análises propostas, como:

* A Paramount produziu mais filmes de fantasia ou de ficção científica durante os anos de 2000 a 2022 ? 
* Qual filme com a temática ficção científica da Paramount mais obteve lucro entre os anos  de Pandemia (2019 a 2022)? 
* Qual foi o filme  com a temática ficção científica da Paramount que mais se destacou com avaliação do público entre os anos  de Pandemia (2019 a 2022)?
* Qual foi os 5 maiores diretores que produziram filme da companhia Paramount?

# Etapas Modelagem

1. O Modelo `Dimensional` ele é focado para relatórios e análises rápidas. Definido isso, e estudo na `Sprint 02`. Definimos que a tabela `fato` ela contém medidas numéricas e as chaves estrangeiras que relaciona com as tabelas `dimensão` que são as tabelas descritivas contém atributos relacionado aos fatos. Após isso o diagrama final do modelo `Dimensional` ficou do seguinte modo:

![Modelagem Dimensional](../Evidencias/Modelagem%20Dimensional.jpg)

# Etapas Script

1. Nesta primeira etapa o objetivo foi criar o script para fazer o tramento dos dados, e fazer o particionamento com base na Modelagem. Foi inciado utilizando as bibliotecas necessário.

![Bibliotecas do Job](../Evidencias/Utilizando%20as%20Bibliotecas.jpg)

2. Nesta segunda etapa o objetivo foi definindo os argumentos utilizado, sendo eles o inicio do job, os caminhos de inicio dos arquivos e os caminhos finais. Também foi feito o Inicio do `Spark` no `Glue`.

![Declaração de Argumentos e Inicializando o Spark](../Evidencias/Argumentos%20utilizados%20e%20inicio%20do%20Job.jpg)

3. Nesta Terceira etapa foi feito a declaração dos caminhos, aonde o arquivo `Parquet` seria armazenado, foi feito a declaração com base no `Job Parameters`.

![Criação dos caminhos](../Evidencias/Definindo%20os%20Caminhos.jpg)

![Criação dos Job Parameters](../Evidencias/Criação%20dos%20Job%20Parameters.jpg)

4. Nesta quarta etapa o objetivo foi fazer o processamento dos dados lendo o arquivo parquet como `DynamicFrame`, visto que é importante para leitura de um arquivo no `Glue`, e depois converter para DataFrame para fazer os `Tratamentos`.

![Leitura e Processamento de Dados](../Evidencias/Lendo%20o%20arquivo%20Parquet%20e%20convertendo%20para%20DataFrame.jpg)

5. Nesta etapa foi inicializado o `Tratamentos de dados`, foi "explodido" as colunas `production_companies`, `genres` e `revenue`, visto que elas se tratavam de um `Array`. Também foi convertido a coluna `release_date` para o formato `DateTime`, visto que ela estava sendo referenciada como do tipo `String`.

![Tratamento de dados nas Colunas Explodindo e Convertendo Colunas](../Evidencias/Tramento%20de%20dados%20Explodindo%20e%20Convertendo%20as%20Colunas.jpg)

6. Na sexta etapa foi continuado com o `Tratamento de dados`, visto que na coluna `director` não havia nenhum `id` para referenciar os diretores, foi preciso criar um `id` pra essa coluna. Foi criado um `DataFrame` para essa coluna, adicionado um `id` e depois juntado ao `DataFrame` original. Nesta etapa também foi Removido espaços extras e tratados valores nulos.

![Tratamento de dados na coluna Diretores e removendo valores nulos](../Evidencias/Tratamento%20de%20Dados%20na%20Coluna%20Diretores%20e%20removido%20Valores%20Nulos.jpg)

7. Finalizando o Script, o objetivo agora era fazer o particionamento com base na `Modelagem` acima, foi criado `DataFrames` para cada tabela correspondente na `Modelagem` e adicionado as colunas especificas a essa tabela, também foi adicionado o `dropDuplicates()` para remover linhas duplicadas dessas colunas. E depois foi salvar esses `DataFrames` no formato parquet em cada `repositório`, utilizando `coalesce(1)` para ele gerar apenas `1 Parquet`. E finalizado o `Job`

![Particionamento e salvando os Parquet](../Evidencias/Particionamento%20e%20salvando%20os%20Parquet.jpg)

8. Após tudo finalizado os `Parquet` ficou alocado no `Bucket` da seguinte forma:

![Camada Refined](../Evidencias/Mostrando%20a%20Camada%20Refined.jpg)

![Camada Contendo os Parquet](../Evidencias/Camada%20contendo%20os%20Parquet.jpg)

9. Finalizado os Script, o objetivo era criar o `Crawler`, para que ele pudesse gerar uma visão padronizado no `Data Catalog` e acessível pelo `AWS Athena`. 

* Criação dos Crawlers.
![Criação dos Crawler](../Evidencias/Criação%20dos%20Crawlers.jpg)

* Tabelas Geradas.
![Criação das Tabelas](../Evidencias/Criação%20das%20Tabelas.jpg)

* Acesso as tabela via `AWS Athena`.
![Acessivel no Athena](../Evidencias/Tabelas%20Acessivel%20no%20Athena.jpg)
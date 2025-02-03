# Objetivo

O objetivo da Sprint 8, era a manipulação de dados do `CSV` e dos `JSON` convertendo as para `Parquet` utilizando o `AWS Glue`, para otimizar consultas, desempenho de leitura e custos de armazenamento. Foi Criado 2 codígo um para `CSV` e um para os `JSON`. Foi feito também a criação do Crawler para registrar os dados no `Data Catalog`, e facilitar o uso do `Athena` para consultas futuras.

Além disso, ao longo da Sprint 08, tomei a liberdade de mudar a minha análise para melhorar o storytelling  com análises propostas, como:

* A Paramount produziu mais filmes de fantasia ou de ficção científica durante os anos de 2000 a 2022 ? 
* Qual filme com a temática ficção científica da Paramount mais obteve lucro entre os anos  de Pandemia (2019 a 2022)? 
* Qual foi o filme  com a temática ficção científica da Paramount que mais se destacou com avaliação do público entre os anos  de Pandemia (2019 a 2022)?
* Existe uma relação entre esses dois filmes, em relação a atores (protagonista) e diretores? (Comparação)

# Etapas

1. Nesta primeira etapa o objetivo foi criar o primeiro script para converter os dados do CSV para Parquet e foi inciado utilizando a bibliotecas necessário.

![Bibliotecas do CSV](../Evidencias/Bibliotecas%20utilizado%20no%20código%20do%20CSV.jpg)

2. Nesta segunda etapa o objetivo foi definindo os argumentos utilizado, sendo eles o inicio do job, os caminhos de inicio dos arquivos e os caminhos finais. Também foi feito o Inicio do `Spark` no `Glue`.

![Declaração de Argumentos e Inicializando o Spark](../Evidencias/Definindo%20os%20argumentos%20iniciais%20e%20Iniciando%20Spark%20no%20Glue.jpg)

3. Nesta Terceira etapa foi feito a declaração dos caminhos finais, aonde o arquivo `Parquet` seria armazenado, foi feito a declaração com base no `Job Parameters`.

![Criação dos caminhos finais](../Evidencias/Criando%20os%20caminhos%20finais%20do%20CSV.jpg)

![Criação dos Job Parameters](../Evidencias/Criação%20dos%20Job%20Parameters%20para%20os%20caminhos.jpg)

4. Nesta quarta etapa o objetivo foi fazer o processamento dos dados do `CSV Movies`, para converter para `Parquet`. Foi definido a conexão com `S3`, utilizado o argumento para saída final, definido também o separador `|` utilizado no `CSV`. Por fim a escrita do `Parquet`, foi utilizado o comando `coalesce()` para forçar a criação de um só `Parquet`.

![Processamento de Dados do CSV Movies](../Evidencias/Processamento%20do%20arquivo%20CSV%20de%20movies.jpg)

5. Nesta etapa o objetivo foi o mesmo da etapa de cima, porém os dados utilizado agora foi o `CSV Series`. Foi definido a conexão com `S3`, utilizado o argumento para saída final, definido também o separador `|` utilizado no `CSV`. Por fim a escrita do Parquet, foi utilizado o comando `coalesce()` para forçar a criação de um só `Parquet`. e logo depois Finalizado o Job.

![Processamento de Dados do CSV Series](../Evidencias/Processamento%20do%20arquivo%20CSV%20de%20Series.jpg)

6. Por fim Após tudo finalizado os `Parquet` ficou alocado no `Bucket` da seguinte forma: 

![Bucket Parquet Movies](../Evidencias/Bucket%20Parquet%20Movies.jpg)

![Bucket Parquet Series](../Evidencias/Bucket%20Parquet%20Series.jpg)

7. Finalizado o Script do `CSV`, o objetivo agora é a criação do Script para Processar os dados do `JSON`. Foi utilizado a mesma lógica das etapas acima. Foi iniciado o script com a declaração de todas as blibliotecas necessárias e declaração do argumentos, incluindo o início do `JOB` e os caminhos dos arquivos `JSON`.

![Bibliotecas do JSON e argumentos declarado](../Evidencias/Bibliotecas%20utilizado%20no%20codigo%20dos%20JSON%20e%20argumentos%20declarados.jpg)

8. Na etapa 8, foi iniciado o `Spark` no `Glue`, e declarado o caminho final aonde o arquivo `Parquet` será gerado como argumento. Foi feito a declaração com base no `Job Parameters`. Para o caminho final, foi considerado a data da ingestão dos dados do JSON, conforme recomendado na Sprint.

![Iniciando Spark e declarando caminho final](../Evidencias/Iniciando%20Spark%20no%20Glue%20e%20definindo%20o%20caminho%20final%20como%20argumento.jpg)

![Criação dos JOB Parameters para os JSON](../Evidencias/Criação%20dos%20Job%20Parameters%20para%20os%20JSON.jpg)

9. Finalizado a declaração dos argumentos, o objetivo Nesta Nona etapa é fazer a Leitura e processamento dos dados dos `JSON`, para converter para `Parquet`. Foi definido a conexão com `S3`, utilizado o argumento para saída final, definido também o formato do arquivo a ser precessado. E por fim a escrita do `Parquet`, foi utilizado o comando `coalesce()` para forçar a criação de um só `Parquet`. E Por fim finalizando o `JOB`

![Leitura e processamentos de dados dos JSON](../Evidencias/Leitura%20e%20processamento%20dos%20dados%20JSON.jpg)

10. Após tudo finalizado o `Parquet` ficou alocado no `Bucket` da seguinte forma:

![Bucket Parquet JSON](../Evidencias/Bucket%20Parquet%20JSON.jpg)

11. Finalizado os Script, o objetivo era criar o `Crawler`, para que ele pudesse gerar uma visão padronizado no `Data Catalog` e acessível pelo `AWS Athena`. 

* Criação dos Crawlers.
![Criação dos Crawler](../Evidencias/Criação%20dos%20Crawlers.jpg)

* Tabelas Geradas.
![Criação das Tabelas](../Evidencias/Criação%20das%20Tabelas.jpg)

* Acesso as tabela via `AWS Athena`.
![Acessivel no Athena](../Evidencias/Acesso%20as%20tabelas%20no%20AWS%20Athena.jpg)



# Objetivo

O objetivo da `Sprint 10` foi explorar e transformar dados em um `Dashboard` por meio do `AWS QuickSight`, uma ferramenta de `Business Intelligence` (BI) da `Amazon`. Durante essa etapa, conseguimos transformar grandes volumes de informações em gráficos intuitivos e indicadores de desempenho.

Além disso, ao longo do `Desafio Final`, as análises propostas foram:

* A Paramount produziu mais filmes de fantasia ou de ficção científica durante os anos de 2000 a 2022 ? 
* Qual filme com a temática ficção científica da Paramount mais obteve lucro entre os anos  de Pandemia (2019 a 2022)? 
* Qual foi o filme  com a temática ficção científica da Paramount que mais se destacou com avaliação do público entre os anos  de Pandemia (2019 a 2022)?
* Qual foi os 5 maiores diretores que produziram filme da companhia Paramount?

# Etapas Modelagem

1. Analisando a `Modelagem Dimensional` feito durante a `Sprint 09`, e visto que foi feito um `Feedback` sobre criar uma `Dim_Tempo`, já que estou trabalhando com datas para minha análise, foi feito as seguintes modificações:

- Criação da `Dimensão Tempo`.
- Particionamento das datas em `Year`, `Month`, `Day`.
- Criação de um `Id_tempo`.
- Relacionamento da `Dimensão Tempo` na tabela `Fato`.

Finalizado essas etapas a Modelagem Final ficou do seguinte modo:

![Modelagem Dimensional](../Evidencias/Modelagem%20Final.jpg)

# Etapas Dashboard

1. Nesta primeira etapa o objetivo foi responder a `Primeira pergunta` da análise, para mostrar quais Gêneros foram mais produzidos, visto que os Gêneros analisados foram `Ficção Cientifíca e Fantasia`. Foi selecionado o `Gráfico de Pizza`, sabendo que ele útil para pequenas comparações, foi agrupado pelo campo `name_genre`, para mostrar os nomes do Gêneros e o valor foi feito uma contagem nos `Id_genre`. Foi utilizado Filtro de Data, para filtrar apenas a data especifíca que a análise propõe, um filtro para selecionar apenas a Companhia `Paramount`, visto que a análise é feito sobre ela e um filtro de Gêneros, para comparar apenas os dois Gêneros.

![Gráfico de Pizza](../Evidencias/Gráfico%20de%20Pizza.jpg)

![Filtros Gráfico de Pizza](../Evidencias/Filtros%20Gráfico%20de%20Pizza.jpg)

2. Nesta segunda etapa o objetivo foi gerar um Gráfico para Mostrar qual desses Gêneros `(Ficção Cientifíca e Fantasia)` teve a maior `Receita` durante a `Pandemia`, para isso foi utilizado um `Gráfico de Linhas`, foi análisado pelo campo `Year`, então o eixo `X` do Gráfico mostra a métrica por ano, e o valor análisado foi usado o campo `total_revenue` para somar todas as `Receitas` por ano com base naquele Gênero, também foi utilzado o campo `name_genre` na cor das linhas, para diferenciar um Gênero do outro. E por fim, feito os filtros de `Data` para usar apenas a data da `Pandemia` e um filtro para comparar apenas os dois Gêneros.

![Gráfico de Linhas](../Evidencias/Gráfico%20de%20Linhas.jpg)

![Filtros Gráfico de Linhas](../Evidencias/Filtros%20Gráfico%20de%20Linhas.jpg)

3. Nesta Terceira etapa foi feito um Gráfico para responder a `Segunda pergunta`, para mostrar qual filme mais obteve `lucro` do Gênero `Ficção Cientifíca` durante a `Pandemia`. Foi utilizado um `KPI` que é um indicador de desempenho, nele foi adicinado um `Campo Calculado` que foi criado `Lucro`, foi feito com base no `total_revenue` menos o `Budget`. E foi agrupado pelo campo `original_title` para mostrar o nome do filme. Por fim foi utilizado Filtro de `Data`, para filtrar apenas a data da `Pandemia`, um filtro para selecionar apenas a Companhia `Paramount` e um filtro de `Gêneros`, para comparar entre apenas os dois Gêneros.

![Gráfico KPI](../Evidencias/Gráfico%20KPI.jpg)

![Filtros Gráfico KPI](../Evidencias/Filtros%20Gráfico%20KPI.jpg)

4. Nesta quarta etapa o objetivo foi criar um Gráfico para responder a `Terceira pergunta`, para mostral qual filme foi o maior avaliado pelo público durante a `Pandemia`. Para isso foi utilizado um `Gráfico de Barras Vertical`, foi agrupado no eixo `Y` pelo campo `original_title` para mostrar os filmes, e utilizado como valor para fazer a métrica o campo `vote_average` para agregar pelo máximo de votos. Por fim foi utilizado Filtro de `Data`, para filtrar apenas a data da `Pandemia`, um filtro para selecionar apenas a Companhia `Paramount` e um filtro de `Gêneros`, para comparar entre apenas os dois Gêneros.

![Gráfico de Barras](../Evidencias/Gráfico%20de%20Barras.jpg)

![Filtros Gráfico de Barras](../Evidencias/Filtros%20Gráfico%20de%20Barras.jpg)

5. Nesta etapa foi análisado que o Filme que mais obteve `Lucro` e o Filme mais bem `Avaliado` são diferentes, foi feito um `Gráfico de Tabelas` para comparar os dois entre `Diretores` e `Ano de Produção`, foi selecionado pelos campos `original_title` para mostrar os nomes dos filmes, `director` para mostrar qual diretor produziu os fimes, e `year` para mostrar o Ano de Produção. Por fim foi feito um filtro para selecionar apenas os `Dois` filmes.

![Gráfico de Tabelas](../Evidencias/Gráfico%20de%20Tabelas.jpg)

![Filtros Gráfico de Tabelas](../Evidencias/Filtros%20Gráfico%20de%20Tabelas.jpg)

6. Na sexta etapa o objetivo foi responder a `Quarta Pergunta`, para mostrar qual foi os Maiores `Diretor` que produziu filmes durante a `Pandemia`. Para isso foi criado um `Gráfico de Dispersão` foi agrupado no eixo `Y` pelo campo `vote_average` para pegar a média dos votos, e agrupado pelo eixo `X` pelo campo `original_title` para contar quantos filmes cada `Diretor` Produziu e agrupado por `Cor` o campo `director` para mostrar cada diretor no Gráfico. Por fim foi utilizado Filtro de `Data`, para filtrar apenas a data da `Pandemia`, um filtro para selecionar apenas a Companhia `Paramount` e um filtro para filtrar apenas os `5 Maiores Diretores`.

![Gráfico de Dispersão](../Evidencias/Filtros%20Gráfico%20de%20Dispersão.jpg)

![Filtros Gráfico de Dispersão](../Evidencias/Filtros%20Gráfico%20de%20Dispersão.jpg)


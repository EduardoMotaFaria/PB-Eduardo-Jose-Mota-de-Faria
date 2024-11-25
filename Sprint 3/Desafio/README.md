# Objetivo

O objetivo da Sprint 3 era processar um arquivo do Google Playstore, fazer análises e gerar gráficos no Jupyter Lab, utilizando a biblioteca Pandas e Matplotlib.  
 - Remover linhas duplicadas.
 - Desenvolver um gráfico Bars para mostrar os top 5 Apps por instalação e um gráfico Pie Chart para mostrar as categorias de Apps existente.
 - Fazer uma análise qual App mais caro existente.
 - Fazer uma análise de quais Apps são classificado "Mature +17".
 - Fazer uma análise para mostrar os top 10 Apps por número de reviews.
 - Fazer uma análise para  mostrar quantos aplicativos são Pagos e quantos são Free.
 - Fazer uma análise para mostrar quais os 5 maiores Gêneros que mais aparece no DataBase 
 - Desenvolver um gráfico Line Plot e um gráfico Scatter Plot das Análises acima.

# Etapas

1. Nesta primeira etapa foi preparado o ambiente importando as bibliotecas Pandas e Matplotlib, e utilizado o comando `read.csv` para ler o arquivo dentro da variável `dados_google`. Foi utilizado o comando `.shape` para verificar quantas Rows e columns existia dentro do arquivo.

    ![Importando as bibliotecas ](../Evidencias/Importando%20as%20biblioteca%20Pandas%20e%20Matplotlib.jpg)

2. Na segunda etapa o objetivo era remover as linhas duplicadas, por isso foi utilizado a função `duplicated().sum()` para somar todas as linhas duplicadas que contia dentro do arquivo. E em seguida a função `drop_duplicates()` para remover as rows duplicadas.
 - (OBS: são removidas as rows que contém todas as columns repetidas).

  ![Importando as bibliotecas ](../Evidencias/Removendo%20as%20linhas%20duplicadas.jpg)

3. Nesta etapa para criar um gráfico Bars baseado nas instalações, foi preciso fazer o tratamento de dados dessa column. Para isso foi utilizado a função `str.replace()` para remover caracteres como `+` e `,` e a função `str.strip()` que remove espaços vazios que podem ocasionar problemas futuros. Análisando column `Installs` foi notado que não era uma coluna do tipo `Int` e que poderia ocasionar problemas na hora de gerar o gráfico, para isso foi utilizado a função `str.isdigit()` que ignora qualquer valor que não seja númerico dentro da column, e a função `astype()` para converter esta coluna para `Int`. 

![Tratamento de dados da coluna Installs ](../Evidencias/Tratamento%20de%20dados%20da%20coluna%20Installs.jpg)

Feito isso foi utilizado o comando `nlargest()` dentro de uma variável `top_aplicativos` para retonar as 5 maiores linhas da coluna `Apps` e `Installs`. Assim mostrando os 5 maiores aplicativos que foram instalados. Para gerar o gráfico foi o utilizado comando `plt.bar()` como parámetro a variável `top_aplicativos` e qual column ele iria puxar.

![Gerando o gráfico final ](../Evidencias/Gerando%20o%20gráfico%20Bars.jpg)

  ### Comandos utilizado na visualização do gráfico
  - `plt.figure` utilizado para configurar o tamanho do gráfico.
  - `plt.title` utilizado para mostrar o título.
  - `plt.xlabel` configura o eixo X.
  - `plt.ylabel` configura o eixo Y.
  - `plt.xticks` configura os rótulos do eixo X.
  - `plt.show` utilizado para mostrar na tela o gráfico.

Finalizado tudo isso o gráfico foi gerado. 
- (OBS: Por causa dos 5 Apps passarem de 1 bilhão de instalações todas as barras do gráfico ficaram do mesmo tamanho).

![Gráfico Bars Pronto ](../Evidencias/Gráfico%20Bars%20final.jpg)

4. Nesta quarta etapa o objetivo era gerar um gráfico Pie Chart para mostrar todas as categorias de aplicativos existente e qual a frequência eles aparecem. Para isso foi utilizado a função `value_counts()` dentro da variável `quantidades_categorias` para fazer a contagem de cada valor que aparece na column `Category`.

![Gerando as categorias existente ](../Evidencias/Gerando%20as%20categorias%20existente.jpg)

Feito isso, para gerar o gráfico foi utilizado o comando `plt.pie` como parámetro a variável `quantidades_categorias`.

![Gerando o gráfico Pie Chart](../Evidencias/Gerando%20o%20gráfico%20Pie%20Chart.jpg)

   ### Comandos utilizado na visualização do gráfico
   - `labels` para definir os rótulos de cada fatia.
   - `autopct` utilizado para adicionar porcentagem para cada fatia.
   - `startangle` define o ângulo do gráfico.
   - `pctdistance` controla a distância da porcentagem no gráfico.
   - `labeldistance` controla a distância dos rótulo no gráfico.
   - `plt.show` utilizado para mostrar na tela o gráfico.
   
Finalizado tudo isso o gráfico foi gerado.
- (OBS: Por conta da quantidade de dados que contém na column `Category` a visualização dos dados não ficaram muito legíveis, uma boa prática seria usar outro tipo de gráfico).

![Gráfico Pie Chart pronto](../Evidencias/Gráfico%20Pie%20Chart.jpg)

5. Nesta etapa o objetivo era fazer uma análise e mostrar qual aplicativo mais caro existente no dataset. Para começar foi verificado os valores que foram inseridos na Column `Price` utilizando o comando `unique()` que mostra todos os valores inseridos.

![Verificação dos dados da coluna Price](../Evidencias/Verificação%20de%20dados%20da%20coluna%20Price.jpg)

Feito isso foi notado que foi inserido um valor não númerico sendo ele `Everyone` e por isso foi preciso fazer o tratamento de dados da column `Price`, para fazer o tratamento foi utilizado a função `str.replace()` para remover caracteres como `$` e `,`, tambem foi utilizado para remover o valor `Everyone` para `Nulo` com isso elimando valores não desejado dentro da column. Feito isso foi notado que a column `Price` não estava no tipo float e com isso o comando `astype()` foi utilizado para converter ela.

![Tratamento de dados da coluna Price](../Evidencias/Tratamento%20de%20dados%20da%20coluna%20Price.jpg)

Com o tratamento de dados pronto era necessário fazer a análise e para isso foi utilizado a função `idxmax()` dentro da variável `aplicativo_mais_caro` e com isso ganharia o maior valor.

![Aplicativo mais caro](../Evidencias/Gerando%20o%20aplicativo%20mais%20caro.jpg)

6. Nesta etapa foi utilizado a mesma lógica da etapa anterior usando o a função `unique()` dentro da column `Content Rating` para verificar como o valor `Mature +17` foi inserido.

![Verificação de dados da coluna Content Rating](../Evidencias/Verificação%20de%20dados%20da%20coluna%20Content%20Rating.jpg)

Visto que não existia nenhuma divergência, foi prosseguido para a análise e foi utilizado um operador de igualdade `==` para selecionar dentro da column `Content Rating` tudo que fosse igual ao valor `Mature +17`

![Gerando todos os aplicativos Mature +17](../Evidencias/Gerando%20todos%20os%20aplicativo%20Mature%20+17.jpg)

Feito isso foi obtido o seguinte resultado. 

![Resultado Mature +17](../Evidencias/Resultado%20Mature%20+17.jpg)

7. Na sétima etapa o objetivo era mostrar os top 10 aplicativos por números de reviews e ordenar eles de forma decrescente, análisando a column `Reviews`  foi natado que ela não era do tipo `Int` e para isso foi utilizado o comando `astype()`. Visto que foi tratado a column, foi utilizado também a função `dropna()` dentro da variável `coluna_review` para remover valores `Nulos` que poderiam conter na column `Reviews` e `Apps`, visto que é uma boa prática para amenizar futuros problemas. Com tudo isso finalizado era só gerar a análise, pórem na column `Apps` continha valores duplicados que não foram removidos pelo `drop_duplicates()` por conter valores diferentes em outras columns, como comentado na etapa acima. Para resolver este problema foi utilizado a função `groupby()` e `max()` para agrupar os valores repetidos e retonar o maior valor de cado grupo.

![Tratamento de dados da coluna Reviews](../Evidencias/Tratamento%20de%20dados%20da%20coluna%20Reviews.jpg)

Feito o tratamento de dados era necessário fazer a análise e foi utilizado a função `sort_values` dentro de uma nova variável `top_10_aplicativos_review` para ordenar todos os valores da column `Reviews`, também foi utilizado o comando `ascending = false`que indica que a ordenação será em ordem decrescente e que o comando `head()` seleciona as 10 primeiras linhas. Feito isso a análise foi gerada.

![Gerando a análise top 10 aplicativos](../Evidencias/Gerando%20a%20análise%20top%2010%20aplicativos.jpg)

8. Nessa etapa o objetivo é fazer uma análise que gere os aplicativos que são `Paid` e `Free` do DataBase. Foi utilizado a mesma lógica acima para verificar os tipos de dados que foram inseridos na column `Type` utilizando a função `unique()`

![Verificação de dados da tabela Type](../Evidencias/Verificação%20de%20dados%20da%20coluna%20Type.jpg)

Notado que os dados estavam inseridos certo e mesmo assim poderia existir valores `Nulos` foi utilizado a função `dropna()` para remover esses valores. Tramento feito agora é gerar a análise, e para isso foi utilizado a função `value_counts()` dentro da variável `contagem_tipo` para gerar a contagem de cada valor que aparece na column `Type`. Para mostrar no formato valor foi utilizado o atributo `values` para pegar os valores da variável `contagem_tipo` e jogar dentro da variável `Valores`.

![Gerando a análise dos Apps Pagos e Frre](../Evidencias/Gerando%20a%20análise%20dos%20Apps%20Pagos%20e%20Free.jpg)

9. Nesta etapa o objetivo é fazer uma análise que gere os 5 maiores gêneros existente no DataBase. Para isso foi utilizado a função `value_counts()` dentro da variável `top_5_generos` para gerar a contagem de cada valor que aparece na column `Genres`. Foi utilizado também a função `head()` que seleciona as 5 primeiras linhas. E para mostrar os valores no formato lista foi criado uma variável `top_5_generos_lista` que continha os valores da variável `top_5_generos` e utilizado a função `tolist()` para gerar no formato de lista.

![Gerando a análise dos 5 maiores Gêneros](../Evidencias/Gerando%20a%20análise%20do%20top%205%20gêneros%20existente.jpg)

10. Nesta ultima etapa era necessário fazer um gráfico Line Plot e Scatter Plot dos indicadores acima. Para gerar o gráfico da etapa `7` era necessário transformar as culunas `Apps` e `Reviews` em lista, e para isso foi utilizado o comando `tolist()` nas variáveis `Aplicativos` e `Reviews`. Feito isso, para gerar o gráfico foi utilizado o comando `plt.scatter` como parámetro das variáveis `Aplicativos` e `Reviews`.

![Gerando o gráfico Scatter](../Evidencias/Gerando%20o%20gráfico%20Scatter.jpg)

### Comandos utilizado na visualização do gráfico
- `plt.figure` utilizado para configurar o tamanho do gráfico.
- `plt.title` utilizado para mostrar o título.
- `plt.ylabel` configura o eixo Y.
- `plt.xlabel` configura o eixo X.
- `plt.xticks` configura os rótulos do eixo X.
- `plt.grid` para gerar as linhas de grade.

Finalizado tudo isso o gráfico foi gerado.

![Gráfico Scatter Final](../Evidencias/Gráfico%20Scatter%20final.jpg)


Feito o Scatter Plot, só restou o Line Plot, para gerar o gráfico foi utilizado o indicadores da etapa `9`. Como a análise ja estava feita, foi utilizado os `Values` e o `index` da variável `top_5_generos`. Para gerar o gráfico foi utilizado o comando `plt.plot`.

![Gerando o gráfico Line Plot](../Evidencias/Gerando%20o%20gráfico%20Line%20Plot.jpg)

### Comandos utilizado na visualização do gráfico
- `plt.figure` utilizado para configurar o tamanho do gráfico.
- `plt.title` utilizado para mostrar o título.
- `plt.ylabel` configura o eixo Y.
- `plt.xlabel` configura o eixo X.
- `plt.xticks` configura os rótulos do eixo X.
- `plt.grid` para gerar as linhas de grade.
- `plt.show` utilizado para mostrar na tela o gráfico.

Finalizado tudo isso o gráfico foi gerado.

![Gráfico Line Plot final](../Evidencias/Gráfico%20Line%20Plot%20final.jpg)






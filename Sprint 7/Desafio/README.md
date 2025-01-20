# Objetivo

O objetivo dessa Sprint é criar uma função na `AWS Lambda` para consumir dados de uma `API`, esses dados são armazenados em formato `JSON`, e enviado para um Bucket `S3` utilizando a biblioteca Boto3. A função é projetada para realizar a coleta de filmes e o upload para o `S3` automaticamente.

Além disso, foi realizado um estudo sobre o tema Sci-Fi/Fantasia, com algumas análises iniciais propostas, como:

* A Paramount produziu mais filmes de fantasia ou de ficção científica ?
* Qual filme com a temática ficção científica da Paramount mais obteve lucro? 
* Qual foi o filme  com a temática ficção científica da Paramount que mais se destacou com avaliação do público?
* Existe uma relação entre esses dois filmes, em relação a atores (protagonista) e diretores? (Comparação).

# Etapas

1. Nesta primeira etapa o objetivo foi configurar a API TMDB com a chave de acesso para realizar requisições. Foi utilizado a biblioteca `tmdbv3api` para fazer essa interação com a API. 

![Interação com API](../Evidencias/Interação%20com%20API.jpg)

2. Nesta segunda etapa o objetivo foi fazer a ligação da biblioteca `boto3` com o `bucket`. O objetivo também foi filtrar pelo `ID` dos `Gêneros` e pelo `ID` da `companhia`, visto que é necessário para realizar a análise, os `ID` foi extraido da documentação do `TMDB`.

![Interação com Bucket e Filtragem dos Gêneros](../Evidencias/Interação%20com%20Bucket%20e%20Filtro%20com%20ID%20dos%20Gêneros.jpg)

3. Nesta Terceira etapa foi feito uma função para converter os objetos da `API` para dicionários, para facilitar o armazenamento dos dados dentro do `JSON`.

![Função para tranforma os objetos em um dicionario](../Evidencias/Função%20para%20transformar%20os%20objetos%20em%20dicionario.jpg)

4. Nesta quarta etapa foi feito uma função para buscar os atributos `details` e `credits` dentro da API, também foi utilizado uma váriavel para limitar até 10 nomes de atores. Visto que ele retorna vários atores. Por fim ele retorna todos os dados de forma estruturada em formato dicionário. 

![Função buscando os Atributos credits e details](../Evidencias/Função%20para%20transformar%20os%20objetos%20em%20dicionario.jpg)

5. Nesta etapa foi feito uma função para buscar filmes populares filtrados pelo gêneros necessário e pela companhia, ele também limita o `JSON` a ter apenas `100` arquivos conforme recomendado. E por fim ele também limita as páginas a percorrer afim de evitar loop infinito.

![Parte 1 da função para buscar filmes populares pelo gêneros](../Evidencias/Parte%201%20da%20função%20para%20buscar%20filmes%20populares.jpg)

![Parte 2 da função para buscar filmes populares pelo gêneros](../Evidencias/Parte%202%20da%20função%20para%20buscar%20filmes%20populares.jpg)

6. Nesta etapa foi feita uma função para gravar os dados no `S3`, ele converte o arquivo para o formato `JSON` e os envia para o `bucket` especificado, organizando o arquivo de forma hierárquica por data. E por fim ele exibe uma mensagem confirmando o sucesso do envio.

![Função para gravar os dados no S3](../Evidencias/Função%20para%20gravar%20os%20dados%20no%20S3.jpg)

7. Nesta última etapa foi feita uma função para gerenciar se as funções de gravar os dados e enviar para o `S3`, ocorreram de forma correta. Ela verifica se o arquivo contem os filmes filtrados e verifica se foi enviado corretamente para o bucket. Feito tudo isso ele exibe um `statusCode`, com uma mensagem de sucesso. 

![Função para gerenciar outras funções](../Evidencias/Função%20para%20gerenciar%20se%20as%20funções%20de%20gravar%20os%20dados%20e%20enviar%20para%20o%20s3.jpg)



# Objetivo

O objetivo da Sprint 5, era a escolha de um `dataset` para responder uma análise que gerasse um `CSV`, seguindo algumas manipulações exigidas que são: 

 - Uma cláusula que filtra dados usando ao menos dois operadores lógicos.
 - Duas funções de Agregação.
 - Uma função de Condicional.
 - Uma função de Conversão.
 - Uma função de Data.
 - Uma função de String.

Feito isso, o objetivo era criar um script em python utilizando a biblioteca `Boto3` para que ele criasse um `Bucket` e fizesse `Upload` dos arquivos `CSV` utilizados e o `CSV` resultante.

Nesse desafio foi gerado a seguinte Análise : "Qual é o valor total e a média dos contratos no tipo 'Serviços', assinados entre 2020 e 2023, com a moeda 'BRL'? Adicionando uma coluna indicando o valor do contrato que excede 500.000 BRL e converter esses valores para ter o resultado com 2 casas depois da virgula."

# Etapas


1. Nesta primeira etapa foi a escolha de um `dataset` na base de dados do Governo Brasileiro, e foi escolhido um `dataset` sobre "Contratos realizados pela CAPES". Foi escolhido essa base de dados, por ela obter vários recursos como: Campos com datas, valores númericos, Campos com String, e os dados estar completos.
    
    ![Dataset Escolhido sem Tratamento de Dados](../Evidencias/Dataset%20Contratos%20Realizados%20pela%20CAPES%20Bruto.jpg)

2. Na segunda etapa, o objetivo foi análisar esse `dataset`, e logo foi percebido que ele precisava de um Tratamento de Dados. Com base em estudos anteriores foi utilizado a biblioteca `Pandas` e a biblioteca `Unidecode` para fazer esse tratamento. Utilizamos a biblioteca `Unidecode` para remover os acentos das palavras, visto que é uma boa prática para padronização dos dados e compatibilidade. Também foi utilizado uma função para remover espaços vazios no `dataset` evitando erros e melhorando a eficiência dos processos de análise. E por fim a conversão das colunas que continha `datas` para o tipo `DateTime`.

![Script Tratamento do Dataset](../Evidencias/Script%20Tratamento%20de%20Dados%20do%20Dataset.jpg)

Finalizando esse Script foi obtido o `dataset` tratado.

![Dataset Tratado](../Evidencias/Dataset%20Tratado%20os%20Dados.jpg)

3. Na terceira etapa, com o `dataset` tratado foi partir para análise desses dados. Com base na análise que está descrita no `Objetivo` acima, foi utilizado a biblioteca `Pandas`.

![Script de Análise dos Dados](../Evidencias/Script%20de%20Análise%20dos%20Dados.jpg)

Com esse Script foi utilizado:

 - Dois operadores : `&` e `==`
 - Duas funções de Agregações: `SOMA` e `MÉDIA`
 - Uma função condicional para criar uma nova coluna chamada `CONTRATO_ACIMA_500K`.
 - Uma função de conversão para alterar o tipo de dado da coluna `VL_CONTRATO`.
 - Uma função Data, foi utilizado `dt.year` para acessar só o ano da Coluna `AN_INICIO_VIGENCIA`.
 - Uma função String, foi utilizado `str.contains()` para filtrar a palavra `Servicos` da Coluna `TP_CONTRATO`.

Feito esse Script foi gerado o seguinte Dataframe.

![Dataframe resultante da Análise](../Evidencias/Dataframe%20resultante%20da%20Análise.jpg)

4. Nesta quarta etapa, o objetivo era implementar o primeiro script utilizando a biblioteca `Boto3`, ele irá criar o bucket e enviar os arquivos para o `S3` da `AWS`. De início foi usado as credenciais, visto que elas são essenciais para autenticar e autorizar o acesso aos serviços da `AWS`. Logo depois foi definido o nome do Bucket que iria ser criado, foi utilizado o nome `bucket-contratos-capes`. Também foi utilizado comando `try` para caso de algum erro ele acaba passando para a função `except` que exibe uma mensagem mostrando o erro. para criação do bucket foi utilizado o comando `create_bucket` em caso de sucesso ele imprime uma mensagem confirmando a criação do Bucket. Em caso de exceção e erro, o comando `except` exibe uma mensagem de erro. Por fim foi definido o caminho local do arquivo que será enviado, foi utilizado a mesma lógica da criação do bucket, porém substituíndo o comando para `upload_file`.

![Script para criar o bucket](../Evidencias/Script%20Criando%20o%20Bucket%20e%20enviando%20o%20dataset%20bruto.jpg)

Com esse script foi obtido o seguinte resultado.

![Bucket Criado e Arquivo enviado](../Evidencias/Resultado%20do%20Script%20de%20Criação%20do%20Bucket.jpg)

5. Na última etapa, visto que o bucket está criado, o `dataset` está tratado, e a análise já foi gerada. O objetivo agora era criar o script utilizando a biblioteca `Boto3`, para enviar o `dataset` tratado e o `resultado final` da análise. Foi utilizado a mesma Lógica da `Etapa 4`, foi definido também o caminho local do dois arquivos a serem enviados e logo depois utilizado o comando `upload_file` dentro do bloco de códigos `try`.

![Script Enviando os Arquivos finais para o Bucket](../Evidencias/Script%20para%20enviar%20o%20Dataset%20Tratado%20e%20o%20resultado%20final%20da%20análise.jpg)

Feito o último script foi obtido o seguinte resultado.

![Script Enviando os Arquivos finais para o Bucket](../Evidencias/Resultado%20do%20Script%20para%20enviar%20os%20ultimos%20arquivos.jpg)

Após todo Desafio feito o `Bucket` dentro do `S3` foi criado e contendo os objetos desejados.

![Bucket dentro da AWS](../Evidencias/Bucket%20dentro%20da%20AWS.jpg)

![Objetos dentro do Bucket](../Evidencias/Objetos%20dentro%20do%20Bucket.jpg)

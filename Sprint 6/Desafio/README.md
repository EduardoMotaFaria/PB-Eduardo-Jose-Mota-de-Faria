# Objetivo

O objetivo da Sprint 6, era criar um script em python utilizando a biblioteca `Boto3` para que ele criasse um `Bucket` e fizesse `Upload` do arquivo `CSV` que é um dataset. Feito isso o objetivo era rodar uma imagem no `Docker`, para carregar o arquivo `CSV` e executar o Script em python.

Visto que nesta sprint é a primeira etapa do `Desafio Final`, também foi gerado as seguintes análises sobre o tema `Sci-fi/Fantasia`:

* Quais filmes de fantasia tiveram as maiores bilheteiras?
* Qual é a duração média dos filmes de fantasia e como isso influencia as avaliações do público? 
* Quais diretores de filmes de sci-fi mais produzem filmes com alta bilheteria?
* Qual é a evolução dos lançamentos de filmes de sci-fi ao longo dos anos?

OBS: Visto que as análises será feita sobre filmes, foi feito somente o envio do dataset Filmes para o S3.


# Etapas

1. Nesta primeira etapa, o objetivo era implementar o Script utilizando a biblioteca `Boto3`, ele irá criar o bucket e enviar os arquivos para o `S3` da `AWS`. De início foi usado as credenciais, visto que elas são essenciais para autenticar e autorizar o acesso aos serviços da `AWS`. Para acesso das credenciais foi utilizado o comando `Input`, presando a segurança, visto que as credenciais não estarão exposta e só quem tem acesso a elas poderá fornecer. Logo depois foi definido o nome do Bucket que irá ser criado, foi utilizado o nome `bucket-desafio-final`. Neste script foi utilizado a biblioteca `datetime` para capturar a data atual quando o arquivo for enviado, ele extrai o ano, mês e dia, e formata o mês e dia para dois dígitos. Também foi destinado qual caminho o arquivo `CSV` ficará armazenado no `Bucket`, contendo a data do envio. Também foi utilizado comando `try` para caso de algum erro ele acaba passando para a função `except` que exibe uma mensagem mostrando o erro. para criação do bucket foi utilizado o comando `create_bucket` em caso de sucesso ele imprime uma mensagem confirmando a criação do Bucket. Em caso de exceção e erro, o comando `except` exibe uma mensagem de erro. Por fim foi definido o caminho local do arquivo que será enviado, foi utilizado a mesma lógica da criação do bucket, porém substituíndo o comando para `upload_file`.

![Script para envio do CSV](../Evidencias/Script%20para%20envio%20do%20CSV.jpg)

2. Na segunda etapa, visto que o Script está criado, o objetivo agora é criar uma imagem, para rodar um container que execute o script. Foi criado o `Dockerfile`, dentro do arquivo `Dockerfile`, foi utilizado comando `FROM` que define a imagem base e utilizado `Python 3` uma versão oficial disponível no `Docker Hub`. Foi utilizado o comando `RUN`, ele executa comandos durante o processo de construção da imagem, ele instala a biblioteca `Boto3`, isso garante que a biblioteca vai estar na imagem que o código vai rodar. Após esse processo foi utilizado o comando `WORKDIR`, ele define o diretório aonde todos os comandos do container serão executados, e `App` foi o diretório Absuluto usado. Proximo comando utilizado foi `COPY`, ele copia todos os arquivos e diretórios onde o `Docker` está sendo executado, para o sistema de arquivos do container onde será gerado a imagem. Por último o comando `CMD` foi utilizado, ele especifica o comando que será executado quando o container foi iniciado, dentro do `CMD` foi especificado o interpretador e o caminho aonde o Script estava localizado.

![Código Dockerfile](../Evidencias/Código%20Dockerfile.jpg)

3. Nesta terceira etapa, o objetivo foi buildar a imagem, baseado no arquivo `Dockerfile` que foi gerado na segunda etapa. Foi utilizado o comando `Docker build`, para criar a imagem. Foi utilizado também o comando `-t`, ele é usado para nomear a imagem, foi nomeado `implementacao-s3`. Por fim utilizado `.` que indica que o diretório atual será usado para construção da imagem.

![Buildando a imagem implementacao-s3](../Evidencias/Biuldando%20a%20imagem%20Implementacao-s3.jpg)

4. Na quarta etapa, a imagem já está criada, o objetivo agora era rodar esse ambiente. Para isso foi utilizado o comando `Docker run`, ele cria um container a partir da imagem e executa. Foi utilizado `-it`, para permitir acessar o container no modo interativo, e no final utilizado o nome da imagem que deveria rodar `implementacao-s3`.

![Bucket dentro da AWS](../Evidencias/Rodando%20o%20container%20que%20executa%20o%20código.jpg)

Feito as 4 etapas o `Bucket` dentro do `S3` foi criado e contendo os objetos desejados.

![Bucket Criado](../Evidencias/Bucket%20Criado.jpg)

![Objetos Inseridos no Bucket](../Evidencias/Objetos%20CSV%20inserido%20no%20Bucket.jpg)

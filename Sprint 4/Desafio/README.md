# Objetivo

O objetivo da Sprint 4, era a criação de 2 ambientes independentes utilizando `Docker`, que executasse um script `Carguru.py` e um Script de `Máscaramento`. Para o Script de `Máscaramento`, era importante enviar algumas palavras para o mascaramento, e o código foi Codado a partir das seguintes instruções abaixo.
 
 - Receber uma String via Input.
 - Gerar o Hash da String por meio do algoritmo SHA-1.
 - Imprimir o Hash em tela, utilizando o método Hexdigest.
 - Voltar a receber uma String.

Nesta Sprint uma parte do Objetivo era responder a seguinte pergunta: 
#### É possível reutilizar Containers ?

# Etapas

1. Nesta primeira etapa o processo foi construir um arquivo `Dockerfile`, para gerar a imagem que executasse o Script `Carguru.py`. Dentro do arquivo `Dockerfile`, foi utilizado comandos `FROM` que define a imagem base e utilizado `Python 3` uma versão oficial disponível no `Docker Hub`. Após esse processo foi utilizado o comando `WORKDIR`, ele define o diretório aonde todos os comandos do container serão executados, e `App` foi o diretório Absuluto usado. Proximo comando utilizado foi `COPY`, ele copia todos os arquivos e diretórios onde o `Docker` está sendo executado para o sistema de arquivos do container onde será gerado a imagem. Por último o comando `CMD` foi utilizado, ele especifica o comando que será executado quando o container foi iniciado, dentro do `CMD` foi especificado o interpretador e o caminho aonde o Script estava localizado.

![Dockerfile do Script Carguru](../Evidencias/Dockerfile%20Carguru.jpg)

2. Nesta segunda etapa, o objetivo foi buildar a imagem, baseado no arquivo `Dockerfile` que foi gerado na primeira etapa. Foi utilizado o comando `Docker build`, para criar a imagem. Foi utilizado também o comando `-t`, ele é usado para nomear a imagem, foi nomeado `Carguru_desafio`. Por fim utilizado `.` que indica que o diretório atual será usado para construção da imagem.

![Buildando a imagem Carguru_desafio](../Evidencias/Buildando%20Carguru_desafio.jpg)

3. Na terceira etapa, a imagem já está criada, o objetivo agora era rodar esse ambiente. Para isso foi utilizado o comando `Docker run`, ele cria um container a partir da imagem e executa. Foi utilizado `-it`, para permitir acessar o container no modo interativo, e no final utilizado o nome da imagem que deveria rodar `Carguru_desafio`.

![Rodando a imagem Carguru_desafio](../Evidencias/Rodando%20a%20imagem%20Carguru_desafio.jpg)
    
4. Finalizado essas três etapas, o objetivo nessa quarta etapa era responder a seguinte pergunta: 
### É possível reutilizar Containers ?

#### Sim, é possível.

Utilizamos o comando `Docker Restart` para inicializar um container parado. 

Na imagem abaixo, podemos perceber um container que contêm a imagem `carguru_desafio` foi finalizado a `22 minutos` atrás, e continha `9 Logs`.

![Logs Antes do comando Start](../Evidencias/Reutilizando%20container%20Docker%20PS%20e%20Logs.jpg)

Quando utilizamos o comando `Docker Restart` ele reinicia o container. Na imagem abaixo percebemos que ele reinicia o container utilizando o `CONTAINER ID`. E quando olhamos para o `STATUS`, nos mostra que o container foi finalizado a `21 segundos` atrás.

![Utilizando o Restart](../Evidencias/Utilizando%20Restart.jpg)

Agora quando utilizado o comando `Docker Logs` ele vai conter mais um log, mostrando assim que o container reinicializou e executou a imagem. 

![Confimação de Logs](../Evidencias/Utilizando%20Docker%20logs.jpg)

5. Respondido a pergunta, partimos para a imagem de mascarar dados que deveria ser criado. Foi utilizado a mesma lógica da imagem `Carguru_desafio`. Houve mudança no comando `WORKDIR`, esse comando define o diretório aonde todos os comandos do container será executados, e o nome do diretório foi nomeado como `Mascara`. Também houve mudança no comando `CMD`, ele utiliza o intepretador `Python`, porém agora ele busca o `script_mascara.py` para ser executado.

Comandos Utilizados nesta etapa: 

 - Criação do arquivo `Dockerfile`.
 - `FROM`
 - `WORKDIR`
 - `COPY`
 - `CMD`

![Criação do Dockerfile](../Evidencias/Dockerfile%20Mascarar-dados.jpg)

6. Para buildar a imagem `mascarar-dados`, e ela executar o script. Foi Necessário criar o Script, foi criado o `script_mascara.py` baseado nas seguintes instruções: 

  - Receber uma String via Input.
  - Gerar o Hash da String por meio do algoritmo SHA-1.
  - Imprimir o Hash em tela, utilizando o método Hexdigest.
  - Voltar a receber uma String.

  ![Criação do script_mascara.py](../Evidencias/Script%20Mascarar-dados.jpg)

7. Nesta etapa, o processo foi buildar a imagem, baseado no arquivo `Dockerfile`. Foi utilizado a mesma lógica da `Segunda etapa`, utilizamos o comando `Docker build` para criar a imagem, também foi utilizado o comando `-t` para nomear a imagem, foi nomeado `mascarar-dados`. Por fim utilizado `.` que indica que o diretório atual será usado para construção da imagem.

![Buildando a imagem Mascarar-dados](../Evidencias/Buildando%20Mascarar-dados.jpg)

8. Nesta útima etapa, o script já foi criado, a imagem já está criado. Objetivo agora é rodar esse ambiente, para isso foi utilizado a mesma lógica da `Terceira etapa`. Utilizamos o comando `Docker run`, ele cria um container a partir da imagem e executa. Foi utilizado `-it`, para permitir acessar o container no modo interativo, e no final utilizado o nome da imagem que deveria rodar `mascarar-dados`. O container vai executar a imagem e por estar no modo interativo, conseguimos interagir com o código, e conseguimos enviar qualquer mensagem para o código mascarar. Foi enviado a palavra `Eduardo` e `Faria` e depois `Sair`, para sair do Programa. Após sair do programa ele encerra o container.

![Rodando Mascarar-dados](../Evidencias/Rodando%20Mascarar-dados.jpg)
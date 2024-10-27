# Instruções

Objetivo dessa Sprint 1 foi Desafio usando terminal e comando Linux, onde tive que criar um arquivo executável que criasse um diretório e gerasse um relatorio.txt por dia, de segunda a quinta as 15:27. Dentro desse relatório, tinha que ter informações de vendas que me foi dado em um arquivo .csv, essas informações são:

* Data do sistema operacional.
* Data da primeira venda.
* Data da ultima venda.
* Quantidade de itens diferentes vendido.
* Mostrar as 10 primeiras linhas do arquivo que foi dado.

Para gerar esse relatório todos os dias e hora que foi pedido, agendei essa execução no `crontab`, comando que agenda execução de tarefas.
Depois de Criar esse relatório tive que criar outro arquivo executável para unir todos esses relatórios em um relatório final, e executar manualmente.

# Etapas


1. Nessa etapa tivemos a criações dos diretórios `ecommerce`, dentro deste diretório, criei o primeiro Script 1 `processamento_de_vendas.sh`.

![Descrição da Imagem](/Sprint%201/Evidencias/Diretório%20ecommerce.jpg)

Dentro desse Script utilizei os comandos abaixo para criar os diretórios 
 `Vendas`, `backup`. e copiei o arquivo `dados_de_vendas.csv`. Utilizei `if` para verficiar a existência dos diretórios.
#### Comandos Usado:

* `mkdir`: Cria diretórios.
* `cp`: Cópia Arquivos.
* `echo`: Exibe Mensagens.

![Descrição da Imagem](/Sprint%201/Evidencias/Criação%20de%20diretorios.jpg)

Com esse trecho de código obvtive a criação dos Diretórios `Vendas` e `backup`

![Descrição da Imagem](/Sprint%201/Evidencias/Diretório%20Vendas.jpg)

![Descrição da Imagem](/Sprint%201/Evidencias/Diretorio%20backup.jpg)



    
2. Nesta etapa renomei o arquivo  `dados_de_vendas.csv`.

#### Comandos Usado:

* `mv`: Renomeia arquivo.

![Descrição da Imagem](/Sprint%201/Evidencias/Renomeando%20Arquivos.jpg)

3. Na terceira etapa criei o Relatório, utilizei duas variáveis `data` e `base_nome_arquivo` para concatenar elas e criar Relatórios com nomes diferente. Utilizei um `if`, para fazer a verificação da existência desse relatório, caso não existe ele cria  um diretório novo.

#### Comandos Usado:

* `touch`: Cria um arquivo vazio.

![Descrição da Imagem](/Sprint%201/Evidencias/Criação%20dos%20Relatorios.jpg)

4. Nesta etapa são todas as informações que vai ser inserido nos Relatórios. Essas informações seria:

* Data do Sistema.
* Data do primeiro registro de venda.
* Data do último registro de venda.
* Total de itens diferente vendidos.
* 10 primeiras linhas do aquivo `dados_de_vendas.csv`.

Para gerar a `Data do Sistema`, utilizei o comando `date`.

Para gerar a `Data do primeiro registro de venda`, utilizei o comando `head` e `grep`.

Para gerar a `data do último registro de venda`, utilizei o comando `tail` e `grep`.

Para gerar o `total de intens diferentes vendidos`, utilizei uma variável `arquivo` com conteúdo que tem os dados a ser percorridos
e utilizei comandos como `cut`, `sort`, `uniq` e `wc`.

Para gerar as `10 primeiras linhas do arquivo`, utilizei o comando `head` com delimitador de linhas que eu precisava.

#### Comandos Usado:

* `head`: Utilizado para ver o topo do arquivo.
* `tail`: Utilizado para ver o fim do arquivo.
* `grep`: Filtrar uma parte do arquivo.
* `cut`: Ele delimita o arquivo, para buscar só o essencial.
* `sort`: Ele ordena o arquivo.
* `uniq`: Retira palavras repetida.
* `wc`: Percorre conta as Linha.

![Descrição da Imagem](/Sprint%201/Evidencias/Informações%20contida%20nos%20Relatórios.jpg)

5. Nesta etapa Zipei os arquivo que estavam em `.csv` para `.zip` com intuito de diminuir o espaço do armazenamento, e deletei arquivos que não ia ser utilizado.

#### Comandos Usado:

* `rm`: remove arquivo.
* `zip`

![Descrição da Imagem](/Sprint%201/Evidencias/Zip%20e%20Delete%20arquivos.jpg)




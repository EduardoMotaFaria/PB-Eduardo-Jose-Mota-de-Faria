# Instruções

Objetivo dessa Sprint 1 foi Desafio usando Shell Script e comando Linux, onde tive que criar um arquivo executável que criasse um diretório e gerasse um relatorio.txt por dia, de segunda a quinta as 15:27. Dentro desse relatório, tinha que ter informações de vendas que me foi dado em um arquivo .csv, essas informações são:

* Data do sistema operacional.
* Data da primeira venda.
* Data da ultima venda.
* Quantidade de itens diferentes vendido.
* Mostrar as 10 primeiras linhas do arquivo que foi dado.

Para gerar esse relatório todos os dias e hora que foi pedido, agendei essa execução no `crontab`, comando que agenda execução de tarefas.
Depois de Criar esse relatório tive que criar outro arquivo executável para unir todos esses relatórios em um relatório final, e executar manualmente.

# Etapas


1. Nessa etapa tivemos a criações dos diretórios `ecommerce`, dentro deste diretório, criei o primeiro Script 1 `processamento_de_vendas.sh` utilizando o editor `nano`.

![Diretório ecommerce](/Sprint%201/Evidencias/Diretório%20ecommerce.jpg)

Dentro desse Script utilizei os comandos abaixo para criar os diretórios 
 `Vendas`, `backup`. e copiei o arquivo `dados_de_vendas.csv`. Utilizei `if` para verficiar a existência dos diretórios.
#### Comandos Usado:

* `mkdir`: Cria diretórios.
* `cp`: Cópia Arquivos.
* `echo`: Exibe Mensagens.
* `nano`: Editor de texto.

![Criação de diretórios](/Sprint%201/Evidencias/Criação%20de%20diretorios.jpg)

Com esse trecho de código obvtive a criação dos Diretórios `Vendas` e `backup`

![Diretório vendas](/Sprint%201/Evidencias/Diretório%20Vendas.jpg)

![Diretório backup](/Sprint%201/Evidencias/Diretorio%20backup.jpg)



    
2. Nesta etapa renomei o arquivo  `dados_de_vendas.csv`.

#### Comandos Usado:

* `mv`: Renomeia arquivo.

![Renomeando Arquivos](/Sprint%201/Evidencias/Renomeando%20Arquivos.jpg)

3. Na terceira etapa criei o Relatório, utilizei duas variáveis `data` e `base_nome_arquivo` para concatenar elas e criar Relatórios com nomes diferente. Utilizei um `if`, para fazer a verificação da existência desse relatório, caso não existe ele cria  um diretório novo.

#### Comandos Usado:

* `touch`: Cria um arquivo vazio.

![Criação do Relatórios](/Sprint%201/Evidencias/Criação%20dos%20Relatorios.jpg)

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

![Informações Contida nos Relatórios](/Sprint%201/Evidencias/Informações%20contida%20nos%20Relatórios.jpg)

5. Nesta etapa Zipei os arquivo que estavam em `.csv` para `.zip` com intuito de diminuir o espaço do armazenamento, e deletei arquivos que não ia ser utilizado.

#### Comandos Usado:

* `rm`: remove arquivo.
* `zip`

![Zip e Delete dos Arquivos](/Sprint%201/Evidencias/Zip%20e%20Delete%20arquivos.jpg)

6. Agendar a execução desse Script para gerar um telatório por dia, de `Segunda` a `Quinta` as `15:27` Automatizado. (Obs: neste Script consegui realizar de `Quinta a Domingo`).
Utilizei o comando `Crontab`. 

#### Comandos Usado:

* `Crontab -e`: Cria um Crontab
* `Crontab -l`: Verifica o Agendamento

![Criação do Crontab](/Sprint%201/Evidencias/Criação%20do%20Crontab.jpg)

Com esta Linha de código obtive o agendamento.

![Crontab](/Sprint%201/Evidencias/Crontab.jpg)

Com este Script `processamento_de_vendas.sh` Obtive os 4 relatório gerados cada dia.

* Relatorio 1 
![Primeiro Relatório](/Sprint%201/Evidencias/Primeiro%20Relatório.jpg)

* Relatório 2
![Segundo Relatório](/Sprint%201/Evidencias/Segundo%20Relatório.jpg)

* Relatório 3
![Terceiro Relatório](/Sprint%201/Evidencias/Terceiro%20Relatório.jpg)

* Relatório 4 
![Quarto Relatório](/Sprint%201/Evidencias/Quarto%20Relatórios.jpg)

7. Nesta etapa criei o Segundo Script `consolidador_de_vendas.sh`. Utilizando o editor `nano`.

![Criação Segundo Script](/Sprint%201/Evidencias/Criação%20do%20Segundo%20Script.jpg)

8. Na etapa 8 criei a variável `pasta_relatorios`, onde o conteúdo dessa variável é o diretório `backup`, que estão localizados todos os relatórios.txt, também foi criado a variável `arquivo_de_saida`, o conteúdo dessa variável é o `relatório final`.

![Variáveis Segundo Script](/Sprint%201/Evidencias/Variáveis%20do%20segundo%20Executável.jpg)

9. Nesta última etapa utilzei um `for` para percorrer o diretório `backup` e buscar todos os arquivos que começa com nome `relatório` e termina com `.txt`, buscando esses arquivos ele concatena todos os relatórios criados no `relatório final`. caso ele não ache nenhum relatório, exibe uma mensagem de erro.

#### Comandos Usado:

* `cat`: Concatena Arquivo

![for Segundo Script](/Sprint%201/Evidencias/FOR%20para%20percorrer%20os%20Relatórios.jpg)

Com esses trecho de código obtive todos relátórios em um só.

![Relatório Final 1](/Sprint%201/Evidencias/Relatório%20final%201.jpg)

![Relatório Final 2](/Sprint%201/Evidencias/Relatório%20Final%202.jpg)

![Relatório Final 3](/Sprint%201/Evidencias/Relatório%20Final%203.jpg)

![Relatório Final 4](/Sprint%201/Evidencias/Relatório%20Final%204.jpg)


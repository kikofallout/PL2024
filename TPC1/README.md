# TPC1 : Processamento de informação de um ficheiro CSV

## Aluno

**Nome:** Francisco Lameirão

**Número:** a97504

## TPC

Neste TPC, pretende-se processar um ficheiro .csv sem utilizar o API de CSV do Python e posteriormente correr funções estatísticas nesses dados.

Para realizar este TPC, adicionei toda a informação em cada linha do .csv a um dicionário com o ID presente no .csv a servir como chave. Depois de dar parse ao ficheiro .csv, tenho várias funções para realizar a estatística pedida, que sâo:

**ordered_modalidadesAlphabetical():** Função que itera pelo dicionário todo, adicionando todas as modalidades a uma lista, que depois converte para um set (para remover duplicados) e dá sort antes de devolver

**percentage_valid:** Função que calcula o número de atletas que passaram e não ao exame médico, iterando por todo o dicionário, e devolve a percentagem de corretos

**athletes_by_age_group:** Função conta a quantidade de atletas com idade num intervalo de 5 anos (e.g. [1-4]). Para o fazer, é usado um dicionário com a idade do ínicio do intervalo a servir de chave e a quantidade como contéudo

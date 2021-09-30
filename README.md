#  Trabalho Teoria e Aplicacao de Grafos Trabalho 2 - UnB 1/2021

# Especificações :

Linguagem: Python3
S.O.:   Ubuntu 18.04


# Executar o código:
Para rodar o executavel rodar o comando:

` python main.py ` 


# Sobre o Algoritmo:

Funcionamento do algoritmo:

O código é programado em classes com a manipulação de dois objetos que servem como a base de dados(conjunto) entre alunos e projetos.

O algoritmo utilizado é semelhante ao da imagem: 
![Alt text](algorithm.jpeg?raw=true "Algoritmo")



Algoritmo:


    Para cada aluno do conjunto de alunos:
        Para cada projeto na lista de preferencia do aluno:

            Se a nota do aluno for abaixo do requisito da prova, pule para o proximo projeto;

            Else:
                Se o projeto ainda possuir vagas:
                    adicione o aluno ao projeto
                Se não tiver vagas:
                    Para cada aluno concorrente:
                        Se a nota do aluno > nota aluno oncorrente:
                            remova aluno concorrente do projeto
                            adicione aluno ao projeto

Remova projetos que possuem vagas restantes

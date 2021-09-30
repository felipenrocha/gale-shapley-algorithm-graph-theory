
from projetos import Projetos
from alunos import Alunos
from input import FileManagement
arquivo_string = 'entradaProj2TAG.txt'


def main():
    # objeto da classe FileManagement para manipulacao do arquivo de entrada
    file = FileManagement(arquivo=arquivo_string)

    # objeto da classe Alunos que armazena o conjunto de alunos
    alunos = Alunos(file.get_alunos())

    # objeto da classe Projetos que armazena o conjunto de projetos
    projetos = Projetos(file.get_projetos())

    # GaleAlgorithm
    gale(alunos, projetos)

    file.close_file()


def gale(alunos, projetos):
    """Gale-Shapley Algorithm """
    # conjunto de pares final
    s = []
    # loop para alunos do conjunto de alunos:
    for aluno_key in alunos.get_alunos():
        # dicionario do aluno do loop:
        aluno = alunos.get_aluno(aluno_key)
        # contador para loop pela lista de preferencia (comecando do primeiro)
        i = 0
        # Enquanto aluno tiver propostas de projetos (maximo 3)
        while(alunos.is_aluno_free(aluno_key) and i < 3):
            # id do projeto é o index do contador
            projeto = alunos.get_aluno_projetos(aluno_key)[i]
            # se a nota for maior ou igual ao requisito:
            if aluno['nota'] >= projetos.get_projeto_requisito(projeto):
                # if: se o projeto tiver vagas
                if (projetos.is_projeto_free(projeto)):
                    # casamento entre aluno e projeto
                    engage(projetos, alunos, aluno_key, projeto)
                    # adiciona a tupla ao conjunto final.
                    s.append((aluno_key, projeto))
                    # sai do loop (while) pois o aluno ja foi designado a um projeto
                    break
                # else: se o projeto nao tiver vagas
                elif projetos.is_project_full(projeto):
                    # para cada aluno concorrente que ja está no  projeto (casado)
                    for aluno_concorrente in projetos.get_projeto(projeto)['alunos']:
                        # se a nota do aluno atual for maior que a do aluno concorrente
                        if (aluno['nota'] > alunos.get_aluno_nota(aluno_concorrente)):
                            # divorcio entre aluno concorrente e projeto

                            desengage(projetos, alunos,
                                      aluno_concorrente, projeto)
                            # remove a tupla do conjunto final
                            s.remove((aluno_concorrente, projeto))
                            print('---- Desemparelhamento entre:   ' +
                                  aluno_concorrente + ' e ' + projeto + '----')

                            # casamento entre o aluno e o projeto
                            engage(projetos, alunos, aluno_key, projeto)
                            # adiciona a tupla ao conjunto final.
                            s.append((aluno_key, projeto))
                            print('---- Emparelhamento entre: ' +
                                  aluno_key + ' e ' + projeto + '----')
                            # sai do loop (while) pois o aluno ja foi designado a um projeto
                            break

            # se a nota nao for suficente pule para o proximo projeto:
            i = i + 1
    # depois do loop de alunos, é feito uma limpa nos projetos que nao possuem todas as vagas completadas
    projetos.remove_projects_not_full(s)

    # print do conjunto final:
    i = 0
    quantidade_projetos = projetos.get_quantidade_projetos()
    print(" ---------------- ")
    print('Quantidade de projetos designados:' + str(quantidade_projetos))


def engage(projetos, alunos, aluno_key, projeto_key):
    """Casamento entre aluno e projeto, nos objetos projetos e alunos"""
    projetos.add_aluno_to_projeto(aluno_key, projeto_key)
    alunos.set_aluno_to_project(aluno_key)


def desengage(projetos, alunos, aluno_key, projeto_key):
    """Divorcio entre aluno e projeto, nos objetos projetos e alunos"""
    projetos.remove_aluno_from_projeto(
        aluno_key, projeto_key)
    alunos.remove_aluno_from_projeto(aluno_key)


if __name__ == "__main__":
    main()

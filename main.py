
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
            # se a nota for suficiente de acordo com o requisito:
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
                else:
                    # para cada aluno concorrente que ja está no  projeto (casado)
                    for aluno_concorrente in projetos.get_projeto(projeto)['alunos']:
                        # se a nota do aluno atual for maior que a do aluno concorrente
                        if (aluno['nota'] > alunos.get_aluno_nota(aluno_concorrente)):
                            # divorcio entre aluno concorrente e projeto
                            desengage(projetos, alunos,
                                      aluno_concorrente, projeto)
                            # remove a tupla do conjunto final
                            s.remove((aluno_concorrente, projeto))
                            # casamento entre o aluno e o projeto
                            engage(projetos, alunos, aluno_key, projeto)
                            # adiciona a tupla ao conjunto final.
                            s.append((aluno_key, projeto))
                            # sai do loop (while) pois o aluno ja foi designado a um projeto
                            break
            # se a nota nao for suficente pule para o proximo projeto:
            i = i + 1
    # depois do loop de alunos, é feito uma limpa nos projetos que nao possuíram todas as vagas completadas
    final_set = projetos.remove_projects_not_full(s)
    print('Conjunto Final ((Aluno,Projeto),  ...) : ' + str(final_set))
    i = 0
    for key in projetos.get_projetos():
        if len(projetos.get_projeto(key)['alunos']) > 0:
            i = i + 1
            print('Projeto: ' + key + ' ' + 'Alunos: ' + str(projetos.get_projeto(key)['alunos']))
    print('Quantidade de projetos designados:' + str(i))


def engage(projetos, alunos, aluno_key, projeto_key):
    projetos.add_aluno_to_projeto(aluno_key, projeto_key)
    alunos.set_aluno_to_project(aluno_key)
    print('Aluno Adicionado a projeto: ' +
          aluno_key + ' e ' + projeto_key)


def desengage(projetos, alunos, aluno_key, projeto_key):
    projetos.remove_aluno_from_projeto(
        aluno_key, projeto_key)
    alunos.remove_aluno_from_projeto(aluno_key)
    print('Aluno removido de projeto: ' +
          aluno_key + ' e ' + projeto_key)


if __name__ == "__main__":
    main()

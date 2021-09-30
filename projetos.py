
class Projetos(object):

    """Módulo para obter os dados do Conjunto de Projetos"""

    def __init__(self, projetos):
        """Inicializa os projetos"""
        self.projetos = projetos

    def get_projetos(self):
        """Retorna lista dos nomes dos projetos"""
        return list(self.projetos.keys())

    def get_projeto(self, projeto):
        """Retorna informacoes do projeto"""
        return self.projetos[projeto]

    def get_projeto_vagas(self, projeto):
        """Retorna o numero de vagas do projeto"""
        return self.get_projeto(projeto)['vagas']

    def is_projeto_free(self, projeto):
        """Retorna se o projeto possui vagas (booleano)"""
        if int(self.get_projeto(projeto)['vagas']) > 0:
            return True
        return False

    def get_quantidade_projetos(self):
        """Retorna quantidade de projetos com vagas completas"""
        i = 0
        print('---------- GRAFO BIPARTIDO ----------------')
        for key in self.get_projetos():
            if len(self.get_projeto(key)['alunos']) > 0:
                i = i + 1
            print('Projeto: ' + key + ' ' + 'Alunos: ' +
                  str(self.get_projeto(key)['alunos']))

        return i

    def get_projeto_requisito(self, projeto):
        """Retorna o requisito do projeto"""
        return int(self.get_projeto(projeto)['requisito'])

    def is_project_full(self, projeto_key):
        """Retorna booleano se o projeto estiver cheio"""
        if len(self.get_projeto(projeto_key)['alunos']) >= self.get_projeto_vagas(projeto_key) - 1:
            return True
        return False

    def add_aluno_to_projeto(self, aluno, projeto):
        """Adiciona o aluno a lista de alunos do projeto"""
        self.get_projeto(projeto)['alunos'].append(aluno)
        self.get_projeto(projeto)['vagas'] = int(
            self.get_projeto(projeto)['vagas']) - 1

    def remove_aluno_from_projeto(self, aluno, projeto):
        """Remove o aluno da lista de alunos do projeto"""
        self.get_projeto(projeto)['alunos'].remove(aluno)
        self.get_projeto(projeto)['vagas'] = int(
            self.get_projeto(projeto)['vagas']) + 1

    def remove_projects_not_full(self, s):
        """Funçao para limpar todos projetos que ainda possuem vagas."""
        i = 0
        projeto_deletados = []
        for aluno, projeto in s:
            if self.get_projeto_vagas(projeto) > 0:
                i = i + 1
                s.remove((aluno, projeto))
                if projeto not in projeto_deletados:
                    projeto_deletados.append(projeto)
                self.remove_aluno_from_projeto(aluno, projeto)
        print('---------')
        print('Projetos removidos por falta de alunos: ' + str(projeto_deletados))
        return s

    def get_total_vagas_sobrando(self):
        """Funcao que retorna o total de vagas sobrando de todas os projetos"""
        # used for debugging
        vagas = 0
        for projeto_key in self.get_projetos():
            projeto = self.get_projeto(projeto_key)
            vagas = vagas + int(projeto['vagas'])
        return vagas


class Alunos(object):

    """Módulo para obter e manipular os dados do Conjunto de Alunos"""

    def __init__(self, alunos):
        self.alunos = alunos

    def get_alunos_names(self):
        return list(self.alunos.keys())

    def get_alunos(self):
        return self.alunos

    def has_projects_to_propose(self, aluno_key):
        if len(self.get_aluno_projetos(aluno_key)) > 0:
            return True
        return False

    def get_aluno(self, aluno):
        return self.alunos[aluno]

    def is_aluno_free(self, aluno):
        return self.get_aluno(aluno)['livre']

    def set_aluno_to_project(self, aluno):
        self.get_aluno(aluno)['livre'] = False

    def remove_aluno_from_projeto(self, aluno):
        self.get_aluno(aluno)['livre'] = True

    def get_aluno_projetos(self, aluno):
        return self.get_aluno(aluno)['projetos']

    def get_aluno_nota(self, aluno):
        return self.get_aluno(aluno)['nota']

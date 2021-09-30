
class Alunos(object):

    """Módulo para obter e manipular os dados do Conjunto de Alunos"""

    def __init__(self, alunos):
        """Inicializa alunos"""
        self.alunos = alunos

    def get_alunos_names(self):
        """Retorna lista do nome dos alunos"""
        return list(self.alunos.keys())

    def get_alunos(self):
        """Retorna o conjunto de alunos"""
        return self.alunos

    def get_aluno(self, aluno):
        """Retorna informações do aluno"""
        return self.alunos[aluno]

    def is_aluno_free(self, aluno):
        """Retorna se o aluno esta livre ou nao (booleano)"""
        return self.get_aluno(aluno)['livre']

    def set_aluno_to_project(self, aluno):
        """Define o aluno como "engaged"""
        self.get_aluno(aluno)['livre'] = False

    def remove_aluno_from_projeto(self, aluno):
        """remove aluno como engaged"""
        self.get_aluno(aluno)['livre'] = True

    def get_aluno_projetos(self, aluno):
        """Retorna lista de preferencia de projetos do aluno"""
        return self.get_aluno(aluno)['projetos']

    def get_aluno_nota(self, aluno):
        """Retorna nota do aluno"""
        return self.get_aluno(aluno)['nota']

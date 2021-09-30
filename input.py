"""Classe responsável para gerenciar a manipulação de dados dos arquivo de entrada txt"""
class FileManagement(object):
    def __init__(self, arquivo):
        """Inicializa a classe com o arquivo baseado no diretório"""
        self.file = open(arquivo, "r")
        # lista para armazenar tupla dos projetos conjunto V1
        self.projetos = self.add_projetos()
        self.alunos = self.add_alunos()  # lista para armazenar tupla dos alunos conjunto V2

    def read_file(self):
        """Leitura do arquivo em string"""
        return self.file.read()

    def get_projetos(self):
        return self.projetos

    def add_projetos(self):
        """Monta o dicionario para os projetos baseado no File"""
        projetos = dict()
        for line in self.file:
            if line.rstrip() == "ALUNOS":
                break
            line = self.split_line(line)
            projeto = line[0]
            vagas = line[1]
            requisito = line[2]
            projetos.update(
                {projeto: {'vagas': vagas, 'requisito': requisito, 'alunos': []}})
        return projetos

    def add_alunos(self):
        """Monta o dicionario de alunos"""
        alunos = dict()
        for position, line in enumerate(self.file):
            if position > 0 and position < 201:  # skip first line
                new_line = self.split_line(line)
                aluno = new_line[0]
                preferencia_projetos = [new_line[1], new_line[2], new_line[3]]
                nota = int(new_line[4])
                alunos.update(
                    {aluno: {"projetos": preferencia_projetos, "nota": nota, 'livre': True}})
        return alunos

    def get_alunos(self):
        return self.alunos

    def split_line(self, line):
        """Separa a linha do texto, remove caractéres desnecessários e retorna um array com as palavras"""
        disallowed_characters = "(),"
        for character in disallowed_characters:
            line = line.replace(character, "")
        line = line.replace(":", " ")
        return line.split()

    def close_file(self):
        self.file.close()


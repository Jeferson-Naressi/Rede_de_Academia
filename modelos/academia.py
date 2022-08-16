class ModelAcademi:
    def __init__(self, academia_id, nome, nota, valor, cidade):
        self.academia_id = academia_id
        self.nome = nome
        self.nota = nota
        self.valor = valor
        self.cidade = cidade

    def json(self):
        return {
            'academia_id': self.academia_id,
            'nome': self.nome,
            'nota': self.nota,
            'valor': self.valor,
            'cidade': self.cidade
        }
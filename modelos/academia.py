from sql_alchemy import banco

class ModelAcademia(banco.Model):
    __tablename__ = 'academias'

    academia_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    nota = banco.Column(banco.Float(precision=1))
    valor = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40))

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

    @classmethod
    def buscando(ModelAcademia, academia_id):
        academia = ModelAcademia.query.filter_by(academia_id=academia_id).first()
        if academia:
            return academia
        return None

    def save_academia(self):
        banco.session.add(self)
        banco.session.commit()
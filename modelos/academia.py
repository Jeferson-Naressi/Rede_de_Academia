from sql_alchemy import banco

class AcademiaModelo(banco.Model):
    __tablename__ = 'Academia'
    academia_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40))

    def __init__(self,academia_id, nome, estrelas, diaria, cidade):
        self.academia_id = academia_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'academia_id':self.academia_id,
            'nome':self.nome,
            'estrelas':self.estrelas,
            'diaria':self.diaria,
            'cidade':self.cidade
        }
    @classmethod
    def encontrarAcademia(cls, academia_id):
       academia = AcademiaModelo.query.filter_by(academia_id=academia_id).first() #Select * From academia WHERE academia_id
       if academia:
           return academia
       return None

    def save_academia(self):
        banco.session.add(self)
        banco.session.commit()

    def update_academia(self,nome,estrelas,diaria,cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def delete_hotel(self):
        banco.session.delete(self)
        banco.session.commit()
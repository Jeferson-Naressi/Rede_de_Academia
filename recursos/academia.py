from flask_restful import Resource, reqparse
from modelos.academia import AcademiaModelo

class Academias(Resource):
    def get(self):
        return {'academia': [academia.json() for academia in AcademiaModelo.query.all()]}

class Academia(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def get(self,academia_id):
        academias = AcademiaModelo.encontrarAcademia(academia_id)
        if academias:
            return academias.json()
        return {'message':'Academia not found.'}, 404
    def post(self,academia_id):
        if AcademiaModelo.encontrarAcademia(academia_id):
            return {'message':"Academia id '{}' already exists.".format(academia_id)}, 400
        dados = Academia.argumentos.parse_args()
        academia = AcademiaModelo(academia_id, **dados)
        academia.save_academia()
        return academia.json()

    def put(self,academia_id):
        dados = Academia.argumentos.parse_args()

        academia_encontrada = AcademiaModelo.encontrarAcademia(academia_id)
        if academia_encontrada:
            academia_encontrada.update_academia(**dados)
            academia_encontrada.save_academia()
            return academia_encontrada.json(),200
        academia = AcademiaModelo(academia_id, **dados)
        academia.save_academia()
        return academia.json(),201
    def delete(self,academia_id):
        academia = AcademiaModelo.encontrarAcademia(academia_id)
        if academia:
            academia.delete_hotel()
            return {'message':'Academia Deletada'}
        return {'message':'Academia Not found.'},404

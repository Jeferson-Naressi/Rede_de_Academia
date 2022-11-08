from flask_restful import Resource,reqparse
from modelos.academia import ModelAcademia

academias = [
        {
        'academia_id': 'smart',
        'nome': 'Smart Academia',
        'nota': 8.9,
        'valor': 119.99,
        'cidade':'São Paulo'},
        {
        'academia_id': 'nocaute',
        'nome': 'Nocaute Academia',
        'nota': 8.5,
        'valor': 99.99,
        'cidade':'Osasco'},
        {
        'academia_id': 'cross',
        'nome': 'Cross Life Academia',
        'notas': 9.0,
        'valor': 109.99,
        'cidade':'Campinas'},
    ]

class Academias(Resource):
    def get(self):
        return {'Academias': academias}

class Academia(Resource):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('nota')
        argumentos.add_argument('valor')
        argumentos.add_argument('cidade')

        def get(self,academia_id):
                academia = ModelAcademia.buscando(academia_id)
                if academia:
                        return academia
                return {'message': 'Hotel not found'}, 404
        def post(self,academia_id):
                if modelos.buscando(academia_id):
                        return {'Mensagem':'A Academia "{}" ja existe'.format(academia_id)}, 400 #Requisição errada
                dados = Academia.argumentos.parse_args()
                academia_objeto = ModelAcademia(academia_id,**dados)
                academia_objeto.save_academia()
                return academia_objeto.json()

        def put(self,academia_id):
                dados = Academia.argumentos.parse_args()
                academia_objeto = ModelAcademia(academia_id, **dados)
                nova_academia = academia_objeto.json()
                academia = Academia.buscando(academia_id)
                if academia:
                        academia.update(nova_academia)
                        return nova_academia,200
                academias.append(nova_academia)
                return nova_academia,201

        def delete(self,academia_id):
                global academias
                academias = [academia for academia in academias if academia['academia_id'] != academia_id]
                return {'message':'Academia deletada'}

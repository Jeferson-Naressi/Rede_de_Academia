from flask import Flask
from flask_restful import Api
from recursos.academia import Academias,Academia

app = Flask(__name__)
api = Api(app)

api.add_resource(Academias, '/academia')
api.add_resource(Academia,'/academia/<string:academia_id>')

if __name__ == '__main__':
    app.run(debug=True)

#Criar pasta com nome modelos e dentro um arquivo __init__.py deixar vazia e criar um arquivo academia.py



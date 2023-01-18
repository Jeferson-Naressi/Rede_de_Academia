from flask import Flask
from flask_restful import Api
from recursos.academia import Academias,Academia

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db' #C:\Users\Jefer\Desktop\Shopping
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def criar_banco():
    banco.create_all()

api.add_resource(Academias, '/academia')
api.add_resource(Academia, '/academia/<string:academia_id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
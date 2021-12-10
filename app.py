import json
from werkzeug.security import generate_password_hash
import jwt
from flask import Flask
from flask_restful import Resource, Api, request
from model import Usuarios


app = Flask(__name__)
api = Api(app)

class Usuario(Resource):
    def get(self, id):
        try:
            usuario = Usuarios.query.filter_by(id=id).first()
            response = {
                'id': usuario.id,
                'nome': usuario.nome,
                'email': usuario.email,
                'senha': usuario.senha
            }
            return response
        except:
            return {'ERROR': 'Usuario inexistente!'}

class Listar_usuarios(Resource):
   def get(self):
       usuario = Usuarios.query.all()
       return usuario

class Inserir_usuario(Resource):
   def post(self):
       usuario = Usuarios(nome='Carol', email='teste@gmail.com', senha=654321)
       usuario.save()

class Auth(Resource):
    def post(self):
        try:
            key = "senhaSuperSecretaESegura"
            user = json.loads(request.data)
            pass_hash = generate_password_hash(user["pass"])
            print(user)
            payload = {
                "user": "Caroline Barros",
                "login": "userLogin",
                "level": 5
            }
            encoded = jwt.encode(payload, key, algorithm="HS256")
            response = {
                "jwt-token": encoded
            }
            return response
        except:
            return {"error": "Bad request"}

    def get(self):
        try:
            token = request.headers.get('authorization')
            payload = jwt.decode(token, "senhaSuperSecretaESegura", algorithm=["HS256"])
            return {"status": "ok", "payload": payload}
        except:
            return {"error": "deu ruim"}

api.add_resource(Usuario, '/usuarios/<int:id>')
api.add_resource(Listar_usuarios, '/usuarios')
api.add_resource(Inserir_usuario, '/inserir')
api.add_resource(Auth, '/login')

if __name__ == '__main__':
    app.run(debug=True)

# desenvolvido por Caroline Barros, Miguel Morais e Pedro Lira - 3º período - ADS - Unit
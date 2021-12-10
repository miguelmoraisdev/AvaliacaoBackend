from model import Usuarios

def inserir_usuario():
    usuario = Usuarios(nome='Caroline', email='teste@teste.com', senha=12345)
    usuario.save()

def listar_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

def consulta_usuario():
    usuario = Usuarios.query.filter_by(nome='Caroline').first()
    print(usuario.id)

def atualiza_usuario():
    usuario = Usuarios.query.filter_by(id=5).first()
    usuario.nome = "Miguel"
    usuario.save()

def remover_usuario():
    usuario = Usuarios.query.filter_by(id=15).first()
    usuario.delete()

if __name__ == '__main__':
    # inserir_usuario()
    # remover_usuario()
    listar_usuarios()
    # atualiza_usuario()
    # consulta_usuario()

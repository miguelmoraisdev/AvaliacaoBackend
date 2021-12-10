from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#define a conexão com o banco
engine = create_engine('sqlite:///cadastro_usuarios.db', convert_unicode=True)

#inicia sessão com o DB
db_session = scoped_session(sessionmaker(bind=engine))

#padrão p instanciar a base e permitir as querys com o orm
Base = declarative_base()
Base.query = db_session.query_property()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), index=True)   #index em banco de dados são referências que permitem que você acesse o banco mais rápido.
    email = Column(String(50), index=True)
    senha = Column(Integer)

    def __repr__(self):
        return '<usuario = {}'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()

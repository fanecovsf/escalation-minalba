from db_config import db, BRANCH

from .unidade import Unidade

class Contato(db.Model):
    __tablename__ = 'tb_contatos'
    __bind_key__ = BRANCH
    __table_args__ = {
        'extend_existing': True
    } 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255))
    cargo = db.Column(db.String(255))
    nivel = db.Column(db.Integer)
    turno = db.Column(db.String(255))
    email = db.Column(db.String(255))
    telefone = db.Column(db.String(30))

    unidade_id = db.Column(db.Integer, db.ForeignKey('tb_unidades.id'), nullable=False)
    unidade = db.relationship('Unidade', backref=db.backref('contatos', lazy=True))

    def __init__(self, nome:str, cargo:str, nivel:int, turno:str, email:str, telefone:str, unidade:Unidade):
        self.nome = nome
        self.cargo = cargo
        self.nivel = nivel
        self.turno = turno
        self.email = email
        self.telefone = telefone
        self.unidade_id = unidade.id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

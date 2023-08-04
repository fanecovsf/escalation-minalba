from db_config import db, BRANCH

class Unidade(db.Model):
    __tablename__ = 'tb_unidades'
    __bind_key__ = BRANCH

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(500))

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

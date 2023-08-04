from db_config import db, BRANCH

class Unidade(db.Model):
    __tablename__ = 'tb_unidades'
    __bind_key__ = BRANCH
    __table_args__ = {
        'extend_existing': True
    } 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(500))

    def __init__(self, nome:str):
        self.nome = nome

    def get_id(self):
        unidade = db.session.get(Unidade, self.id)
        return unidade.id

    def insert(unidade):
        db.session.add(unidade)
        db.session.commit()

    def update(id, unidade):
        unidade_old = db.session.get(Unidade, id)
        unidade_old.nome = unidade.nome
        db.session.commit()


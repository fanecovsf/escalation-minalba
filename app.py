from flask import Flask, render_template

from routes.minalba import minalba_bp

from models.unidade import Unidade
from models.contato import Contato

from db_config import db, BRANCH

#Configurações
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['RESTFUL_JSON'] = {
    'ensure_ascii': False
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SQLALCHEMY_BINDS'] = {
    BRANCH: app.config['SQLALCHEMY_DATABASE_URI']
}

db.init_app(app=app)

#Landing page
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@app.route('/')
def landing():
    return render_template('landing.html')

#Blueprints
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
app.register_blueprint(minalba_bp)

#Execução
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    with app.app_context():
        if BRANCH == 'test':
            db.drop_all()
            db.create_all()

            unidade1 = Unidade('Barra Funda')
            unidade2 = Unidade('Campos do Jordão')

            unidade1.insert()
            unidade2.insert()


            contato1 = Contato('Gustavo', 'Analista', 2, 'ADM', 'gustavo@gmail.com', '993561207', unidade1.get_id())
            contato2 = Contato('Luciano', 'Supervisor', 4, 'A', 'luciano@gmail.com', '994561453', unidade2.get_id())

            contato1.insert()
            contato2.insert()


            db.session.commit()

    app.run(debug=True)

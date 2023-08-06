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
app.config['SQLALCHEMY_DATABASE_URI_PROD'] = 'postgresql://escalation_gn_user:PIyZ3GBLni8Y0teEebhr0Y1Opfqi7tA4@dpg-cj7h3r5jeehc73dnsms0-a.oregon-postgres.render.com/escalation_gn'

app.config['SQLALCHEMY_BINDS'] = {
    'test': app.config['SQLALCHEMY_DATABASE_URI'],
    'production': app.config['SQLALCHEMY_DATABASE_URI_PROD']
}

app.config['SQLALCHEMY_POOL_SIZE'] = 10
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 300
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 20
app.config['SQLALCHEMY_POOL_RECYCLE'] = 1800

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


            contato1 = Contato('Gustavo', 'Analista', 2, 'ADM', 'gustavo@gmail.com', '993561207', unidade1)
            contato2 = Contato('Luciano', 'Supervisor', 4, 'A', 'luciano@gmail.com', '994561453', unidade2)
            contato3 = Contato('Henrique', 'Assistente', 1, 'B', 'henrique@gmail.com', '998765732', unidade1)

            contato1.insert()
            contato2.insert()
            contato3.insert()
            

            db.session.commit()

    app.run(host='0.0.0.0')

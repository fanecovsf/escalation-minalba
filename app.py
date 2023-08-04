from flask import Flask

from db_config import db, BRANCH

#Configurações
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
app = Flask(__name__)

app.config['RESTFUL_JSON'] = {
    'ensure_ascii': False
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SQLALCHEMY_BINDS'] = {
    BRANCH: app.config['SQLALCHEMY_DATABASE_URI']
}

#Rotas
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@app.route('/')
def main():
    return 'Online'

#Execução
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)

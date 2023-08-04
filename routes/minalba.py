from flask import Response, Blueprint, jsonify, abort, request
import json

from models.unidade import Unidade
from models.contato import Contato

from db_config import db

#Configurações
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
minalba_bp = Blueprint('minalba', __name__)

#Error handling
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@minalba_bp.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404

@minalba_bp.errorhandler(500)
def internal_error(e):
    return jsonify(error=str(e)), 500

#Rotas
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@minalba_bp.route('/minalba/unidades')
def unidades():
    unidades = db.session.query(Unidade)

    data_list = []

    for unidade in unidades:
        data = {
            'id':unidade.id,
            'nome':unidade.nome
        }

        data_list.append(data)

    return Response(response=json.dumps(data_list, ensure_ascii=False), status=200, content_type="application/json")

@minalba_bp.route('/minalba/unidades/<int:id>')
def unidade(id):
    unidade = db.session.get(Unidade, id)

    if not unidade:
        abort(404, description='Ops! Parece que essa consulta está vazia.')

    else:
        data = [
            {
                'id':unidade.id,
                'nome':unidade.nome
            }
        ]

        return Response(response=json.dumps(data, ensure_ascii=False), status=200, content_type="application/json")
    
@minalba_bp.route('/minalba/unidades/add', methods=['PUT'])
def add_unidade():
    try:
        data = request.json
        nome = data.get('nome')

        unidade = Unidade(nome)
        unidade.insert()

        message_data = {
            'Sucesso':f'Unidade {nome} adicionada com sucesso!'
        }

        return Response(response=json.dumps(message_data, ensure_ascii=False), status=200, content_type="application/json")
        

    except Exception as e:
        error_data = {
            'error':str(e)
        }

        return Response(response=json.dumps(error_data, ensure_ascii=False), status=500, content_type="application/json")
    



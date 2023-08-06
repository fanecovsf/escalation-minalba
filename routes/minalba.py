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
        contatos = db.session.query(Contato).filter_by(unidade=unidade)

        contatos_list = []

        for contato in contatos:
            data = {
                'id':contato.id,
                'nome':contato.nome,
                'cargo':contato.cargo,
                'nivel':contato.nivel,
                'turno':contato.turno,
                'email':contato.email,
                'telefone':contato.telefone
            }

            contatos_list.append(data)

        data = {
            'id':unidade.id,
            'nome':unidade.nome,
            'contatos':contatos_list
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
            'sucess':f'Unidade {nome} adicionada com sucesso!'
        }

        return Response(response=json.dumps(message_data, ensure_ascii=False), status=200, content_type="application/json")
        

    except Exception as e:
        error_data = {
            'error':str(e)
        }

        return Response(response=json.dumps(error_data, ensure_ascii=False), status=500, content_type="application/json")
    
@minalba_bp.route('/minalba/unidades/delete', methods=['DELETE'])
def del_unidade():
    try:
        data = request.json
        id = data.get('id')

        unidade = db.session.get(Unidade, id)
        unidade.delete()

        message_data = {
            'sucess':f'Unidade {unidade.nome} deletada com sucesso!'
        }

        return Response(response=json.dumps(message_data, ensure_ascii=False), status=200, content_type="application/json")
        

    except Exception as e:
        error_data = {
            'error':str(e)
        }

        return Response(response=json.dumps(error_data, ensure_ascii=False), status=500, content_type="application/json")
    
@minalba_bp.route('/minalba/contatos')
def contatos():
    contatos = db.session.query(Contato)

    data_list = []

    for contato in contatos:
        data = {
            'id':contato.id,
            'nome':contato.nome,
            'cargo':contato.cargo,
            'nivel':contato.nivel,
            'turno':contato.turno,
            'email':contato.email,
            'telefone':contato.telefone,
            'unidade':{
                'id':contato.unidade.id,
                'nome':contato.unidade.nome
            }
        }

        data_list.append(data)

    return Response(response=json.dumps(data_list, ensure_ascii=False), status=200, content_type="application/json")

@minalba_bp.route('/minalba/contatos/<int:id>')
def contato(id):
    contato = db.session.get(Contato, id)

    data = {
        'id':contato.id,
        'nome':contato.nome,
        'cargo':contato.cargo,
        'nivel':contato.nivel,
        'turno':contato.turno,
        'email':contato.email,
        'telefone':contato.telefone,
        'unidade':{
            'id':contato.unidade.id,
            'nome':contato.unidade.nome
        }
    }

    return Response(response=json.dumps(data, ensure_ascii=False), status=200, content_type="application/json")

@minalba_bp.route('/minalba/contatos/add', methods=['PUT'])
def add_contato():
    try:
        data = request.json

        unidade = db.session.get(Unidade, data.get('unidade_id'))

        if not unidade:
            unidade_error = {
                'error':'Unidade inexistente'
            }

            return Response(response=json.dumps(unidade_error, ensure_ascii=False), status=404, content_type="application/json")

        else:
            contato = Contato(data.get('nome'), data.get('cargo'), data.get('nivel'), data.get('turno'), data.get('email'), data.get('telefone'), unidade)

            contato.insert()

            message_data = {
                'sucess':f'Contato {contato.nome} adicionado com sucesso!'
            }

            return Response(response=json.dumps(message_data, ensure_ascii=False), status=200, content_type="application/json")

    except Exception as e:
        error_data = {
            'error':str(e)
        }

        return Response(response=json.dumps(error_data, ensure_ascii=False), status=500, content_type="application/json")

@minalba_bp.route('/minalba/contatos/delete', methods=['DELETE'])
def del_contato():
    try:
        data = request.json

        id = data.get('id')

        contato = db.session.get(Contato, id)

        contato.delete()

        message_data = {
            'sucess':f'Contato {contato.nome} deletado com sucesso!'
        }

        return Response(response=json.dumps(message_data, ensure_ascii=False), status=200, content_type="application/json")

    except Exception as e:
        error_data = {
            'error':str(e)
        }

        return Response(response=json.dumps(error_data, ensure_ascii=False), status=500, content_type="application/json")


from flask import request, make_response, jsonify
from flask_restful import Resource

from api import api
from ..entidades import tarefas
from ..schemas import tarefa_schema
from ..services import tarefa_service


class TarefasList(Resource):

    # LISTAR TODAS TAREFAS
    def get(self):
        tarefas = tarefa_service.listar_tarefas()
        ts = tarefa_schema.TarefaSchema(many=True)
        return ts.jsonify(tarefas)

    # CADASTRAR TAREFA
    def post(self):
        ts = tarefa_schema.TarefaSchema()

        # Validando a informação
        validate = ts.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            data_expiracao = request.json["data_expiracao"]

            tarefa_nova = tarefas.Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao)

            result = tarefa_service.cadastrar_tarefa(tarefa_nova)

            return make_response(ts.jsonify(result), 201)


class TarefaDetail(Resource):
    def get(self, id):
        tarefa = tarefa_service.lista_tarefa_id(id)

        if tarefa is None:
            return make_response(jsonify("Tarefa não encontrada"), 404)
        else:
            ts = tarefa_schema.TarefaSchema()
            return make_response(ts.jsonify(tarefa), 200)

    def put(self, id):
        tarefa_bd = tarefa_service.lista_tarefa_id(id)

        if tarefa_bd is None:
            return make_response(jsonify("Tarefa não encontrada"), 404)

        ts = tarefa_schema.TarefaSchema()
        validate = ts.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            data_expiracao = request.json["data_expiracao"]

            # PASSA OS DADOS EDITADOS PELO USUÁRIO PARA A VARIÁVEL
            tarefa_editada = tarefas.Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao)

            # RECEBE DOIS PARAMETROS TAREFA CADASTRADA NO BANCO E OS DADOS EDITADOS PELO USUÁRIO
            tarefa_service.editar_tarefa(tarefa_bd, tarefa_editada)

            # FAZ UM GET NOS DADOS ATUALIZADOS E RETORNA PARA A VARIÁVEL TAREFA_ATUALIZADA.
            tarefa_atualizada = tarefa_service.lista_tarefa_id(id)

            # DISERIALIZA DE PYTHON PARA JSON PARA OBTER O RESULTADO E RETORNA O RESULTADO COM STATUS-CODE 200-OK
            return make_response(ts.jsonify(tarefa_atualizada), 200)

    def delete(self, Id):
        pass


api.add_resource(TarefasList, '/tarefas')
api.add_resource(TarefaDetail, '/tarefa/<int:id>')

from flask import request, make_response, jsonify
from flask_restful import Resource
from api import api

from ..schemas import funcionario_schema
from ..services import funcionario_service
from ..entidades import funcionario


class FuncionarioList(Resource):

    # GET
    def get(self):
        # Passa todos os projetos cadastrados no BD
        funcionarios = funcionario_service.listar_funcionarios()

        # Passa o schema do projeto para a variável PS. (many=True) Que que vai receber mais de um resultado
        fs = funcionario_schema.FuncionarioSchema(many=True)

        # Desserializando do Python para Objeto JSON com todos funcionarios cadastrados
        return make_response(fs.jsonify(funcionarios), 200)

    # POST
    def post(self):

        # Verificar se o funcionário existe
        pass

        # Instancia um Schema, responsável pela validação dos dados
        fs = funcionario_schema()

        # Passa o resultado da validação para o Validate
        validate = fs.validate(request.json)

        # Emite mensagem de erro, caso exista
        if validate is None:
            make_response(jsonify(validate), 400)
        else:

            # Atribui os valores do usuário as variáveis
            nome = request.json["nome"]
            idade = request.json["idade"]

            # Passa o resultado do input para a Entidade e atribui o resultado a variável
            funcionario_novo = funcionario.Funcionario(nome=nome, idade=idade)

            # Cria uma novo funcionario
            result = funcionario_service.cadastrar_funcionario(funcionario_novo)

            # Recebe o resultado com o objeto cadastrado
            return make_response(fs.jsonify(result), 201)


class FuncionarioDetail(Resource):

    # GET - POR ID
    def get(self, id):

        # Passa o ID do funcionário para a variável
        funcionario = funcionario_service.lista_funcionario_id(id)

        # Se projeto não existir
        if funcionario is None:
            return make_response(jsonify("Funcionário não encontrado"), 404)
        else:
            #  Armazena os dados do Schema na variável fs
            fs = funcionario_schema.FuncionarioSchema()

            # Retorna o resultado desserializado em JSON para o usuário
            return make_response(fs.jsonify(funcionario), 201)

    # PUT - Editar Funcionario
    def put(self, id):

        funcionario_bd = funcionario_service.lista_funcionario_id(id)

        if funcionario_bd is None:
            return make_response(jsonify("Funcionário não encontrado"), 404)
        else:
            fs = funcionario_schema.FuncionarioSchema()
            validate = fs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 404)
        else:

            # Atribui o input do usuário as variáveis para resem gravadas
            nome = request.json["nome"]
            idade = request.json["idade"]

            # Passa os dados da entidade para a variável projeto_editado
            funcionario_editado = funcionario.Funcionario(nome=nome, idade=idade)

            # Editando no banco
            funcionario_service.editar_funcionario(funcionario_bd, funcionario_editado)

            # Faz um GET dos dados atualizados e retorna para a variável
            funcionario_atualizado = funcionario_service.lista_funcionario_id(id)

            # Retorna para o usuário a tarefa editada
            return make_response(fs.jsonify(funcionario_atualizado), 200)

    # DELETE
    def delete(self, id):

        # Busca o funcionário pelo ID
        funcionario = funcionario_service.lista_funcionario_id(id)

        # Se o funcionário não existir
        if funcionario is None:
            make_response(jsonify("Funcionário não encontrado"), 404)
        else:

            # Passa o projeto para ser deletado no BD
            funcionario_service.deletar_funcionario(id)

            # Retorna apenas o Status Code
            return make_response('', 204)


api.add_resource(FuncionarioList, '/funcionarios')
api.add_resource(FuncionarioDetail, '/funcionario')

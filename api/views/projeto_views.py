from flask import request, make_response, jsonify
from flask_restful import Resource

from api import api
from ..entidades import projeto
from ..schemas import projeto_schema
from ..services import projeto_service


class ProjetoLIst(Resource):

    # GET - LISTAR TODOS OS PROJETOS
    def get(self):
        # Passa todos os projetos cadastrados no BD
        projetos = projeto_service.listar_projetos()

        # Passa o schema do projeto para a variável PS. (many=True) Que que vai receber mais de um resultado
        ps = projeto_schema.ProjetoSchema(many=True)

        # Desserializando do Python para Objeto JSON com todos projetos cadastrados
        return make_response(ps.jsonify(projetos), 200)

    # POST - CADASTRAR PROJETO
    def post(self):

        # Instancia o método com o Schema
        ps = projeto_schema.ProjetoSchema()

        # Atribui o resultado do erro de validação a variável VALIDATE
        validate = ps.validate(request.json)

        # Se a validação de erro for verdadeira, retorna um 404 para o usuário.
        if validate:
            return make_response(jsonify(validate), 400)
        else:

            # Atribui o input do usuário as variáveis para resem gravadas
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            funcionarios = request.json["funcionarios"]

            # Passa o resultado do input para a Entidade e atribui o resultado a variável
            projeto_novo = projeto.Projeto(nome=nome, descricao=descricao, funcionarios=funcionarios)

            # Cria uma nova tarefa
            result = projeto_service.cadastrar_projeto(projeto_novo)

            # Retorna um JSON com o objeto cadastrado
            return make_response(ps.jsonify(result), 201)


class ProjetoDetail(Resource):

    # GET - BUSCA POR ID
    def get(self, id):

        # Passa o projeto retornado do BD para a variável projeto
        projeto = projeto_service.lista_projeto_id(id)

        # Se projeto não existir
        if projeto is None:
            return make_response(jsonify("Projeto não encontrado"), 404)
        else:
            # Armazena os dados do Schema na variável PS
            ps = projeto_schema.ProjetoSchema()

            # Retorna o resultado desserializado em JSON para o usuário
            return make_response(ps.jsonify(projeto), 200)

    # PUT - EDITAR UM PROJETO
    def put(self, id):

        # Lista o projeto do BD requisitado pelo usuário
        projeto_bd = projeto_service.lista_projeto_id(id)

        # Verifica se o projeto existe, Se não existir
        if projeto_bd is None:
            return make_response(jsonify("Tarefa não encontrada"), 404)

        # Passa o Schema para a variável PS para retornar uma mensagem
        ps = projeto_schema.ProjetoSchema()
        validate = ps.validate(request.json)

        # Verifica se existe erro no validate
        if validate:
            return make_response(jsonify(validate), 400)
        else:

            # Atribui o input do usuário as variáveis para resem gravadas
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            funcionarios = request.json["funcionarios"]

            # Passa os dados da entidade para a variável projeto_editado
            projeto_editado = projeto.Projeto(nome=nome, descricao=descricao, funcionarios=funcionarios)

            # Editando no banco
            projeto_service.editar_tarefa(projeto_bd, projeto_editado)

            # Faz um GET dos dados atualizados e retorna para a variável
            projeto_atualizado = projeto_service.lista_projeto_id(id)

            # Retorna para o usuário a tarefa editada
            return make_response(ps.jsonify(projeto_atualizado), 200)

    # DELETE - DELETA UM PROJETO
    def delete(self, id):

        # Pesquisa o projeto pelo ID
        projeto = projeto_service.lista_projeto_id(id)

        # Se tiver erro, retorna mensagem
        if projeto is None:
            return make_response(jsonify("Projeto não encontrado"), 404)
        else:

            # Passa o projeto para ser deletado no BD
            projeto_service.deletar_projeto(projeto)

            # Retorna apenas o Status Code
            return make_response('', 204)


api.add_resource(ProjetoLIst, '/projetos')
api.add_resource(ProjetoDetail, '/projeto/<int:id>')

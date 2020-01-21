from flask import request, make_response, jsonify
from flask_restful import Resource

from api import api
from ..entidades import usuario
from ..schemas import usuario_schema
from ..services import usuario_service


class UsuarioList(Resource):

    # CADASTRAR TAREFA
    def post(self):
        us = usuario_schema.UsuarioSchema()

        # Validando a informação
        validate = us.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            email = request.json["email"]
            senha = request.json["senha"]

            usuario_novo = usuario.Usuario(nome=nome, email=email, senha=senha)

            result = usuario_service.cadastrar_usuario(usuario_novo)

            return make_response(us.jsonify(result), 201)


api.add_resource(UsuarioList, '/usuarios')

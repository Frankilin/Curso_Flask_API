from datetime import timedelta

from flask import request, make_response, jsonify
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from api import api
from ..schemas.login_schema import LoginSchema
from ..services import usuario_service


class LoginList(Resource):
    def post(self):
        ls = LoginSchema()
        validate = ls.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json["email"]
            senha = request.json["senha"]

            usuario_bd = usuario_service.listar_usuario(email)

            if usuario_bd and usuario_bd.compara_senha(senha):

                # Se usuario foi identificado, gera um token de acesso para o usuário
                access_token = create_access_token(
                    identity=usuario_bd.id,
                    expires_delta=timedelta(seconds=60)
                )

                return make_response(jsonify({
                    'access_token': access_token,
                    'message': 'login realizado com sucesso'
                }), 200)
            else:
                return make_response(jsonify({
                    'message': 'credencial inválida'
                }), 401)


api.add_resource(LoginList, '/login')

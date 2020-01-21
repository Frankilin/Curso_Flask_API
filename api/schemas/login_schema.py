from marshmallow import fields
from api import ma

from ..models import usuario_model


class LoginSchema(ma.ModelSchema):
    class Meta:
        model = usuario_model.Usuario
        fields = ("id", "nome", "email", "senha")

    nome = fields.String(required=False)
    email = fields.String(required=True)
    senha = fields.String(required=True)

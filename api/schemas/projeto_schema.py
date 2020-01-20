from marshmallow import fields

from api import ma
from ..models import projeto_model


class ProjetoSchema(ma.ModelSchema):
    class Meta:
        model = projeto_model.Projeto
        fields = ("id", "nome", "descricao", "tarefas", "funcionarios")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)


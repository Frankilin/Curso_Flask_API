from marshmallow import fields
from api import ma

from ..models import funcionario_model

class FuncionarioSchema(ma.ModelSchema):
    class Meta:
        model = funcionario_model.Funcionario
        fields = ("id", "nome", "idade")

    nome = fields.String(required=True)
    idade = fields.Int(required=True)

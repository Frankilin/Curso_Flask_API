from api import db

from ..models import funcionario_model


# POST - CADASTRO
def cadastrar_funcionario(funcionario):
    funcionario_db = funcionario_model.Funcionario(nome=funcionario.nome, idade=funcionario.idade)

    db.session.add(funcionario_db)
    db.session.commit()

    return funcionario_db


# GET - LISTA TODOS FUNCIONARIOS
def listar_funcionarios():
    funcionarios = funcionario_model.Funcionario.query.all()

    return funcionarios


# GET - LISTA FUNCIONARIO POR ID
def lista_funcionario_id(id):
    funcionario = funcionario_model.Funcionario.query.filter_by(id=id).first()

    return funcionario


# PUT - EDITAR FUNCIONARIO
def editar_funcionario(funcionario_bd, funcionario_novo):
    funcionario_bd.nome = funcionario_novo.nome
    funcionario_bd.idade = funcionario_novo.idade

    db.session.commit()


# DELETE - EXCLUI FUNCIONARIO
def deletar_funcionario(funcionario):
    db.session.delete(funcionario)
    db.session.commit()

from api import db

from ..models import projeto_model


# POST - CADASTRA UM PROJETO
def cadastrar_projeto(projeto):
    projeto_bd = projeto_model.Projeto(nome=projeto.nome, descricao=projeto.descricao)

    db.session.add(projeto_bd)
    db.session.commit()

    return projeto_bd


# GET - TODOS OS PROJETOS
def listar_projetos():
    projetos = projeto_model.Projeto.query.all()

    return projetos


# GET - PROJETO POR ID
def lista_projeto_id(id):
    projeto = projeto_model.Projeto.query.filter_by(id=id).first()

    return projeto


# PUT - EDITAR PROJETO
def editar_tarefa(projeto_bd, projeto_novo):
    projeto_bd.nome = projeto_novo.nome
    projeto_bd.descricao = projeto_novo.descricao

    db.session.commit()


# DELETE - EXCLUIR PROJETO
def deletar_projeto(projeto):
    db.session.delete(projeto)
    db.session.commit()

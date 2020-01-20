from api import db

from ..models import projeto_model
from ..services.funcionario_service import lista_funcionario_id


# POST - CADASTRA UM PROJETO
def cadastrar_projeto(projeto):
    projeto_bd = projeto_model.Projeto(nome=projeto.nome, descricao=projeto.descricao)

    # For com o Array de funcionarios
    for i in projeto.funcionarios:

        # Passa cada funcionario no FOR para a variável funcionário
        funcionario = lista_funcionario_id(i)

        # Grava no banco, na tabela secundaria
        projeto_bd.funcionarios.append(funcionario)

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

    # Limpa todos os usuários que vem do banco
    projeto_bd.funcionarios = []

    # For com o Array de funcionarios
    for i in projeto_novo.funcionarios:
        # Passa cada funcionario no FOR para a variável funcionário
        funcionario = lista_funcionario_id(i)

        # Grava no banco, na tabela secundaria
        projeto_bd.funcionarios.append(funcionario)

    db.session.commit()


# DELETE - EXCLUIR PROJETO
def deletar_projeto(projeto):
    db.session.delete(projeto)
    db.session.commit()

from api import db

from ..models import projeto_model


class Tarefa(db.Model):
    __tablename__ = "tarefa"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    data_expiracao = db.Column(db.Date, nullable=False)

    # Criando uma nova coluna na tabela TAREFA, inserindo o ID de um projeto
    projeto_id = db.Column(db.Integer, db.ForeignKey("projeto.id"))

    # Fazendo relacionamento (1 -> N) com a tabela projetos e sincronizando para
    # listar todas as tarefas que está vinculada a algum projeto
    projeto = db.relationship(projeto_model.Projeto, backref=db.backref("tarefas", lazy="dynamic"))

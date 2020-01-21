from api import db

from ..models import usuario_model


def cadastrar_usuario(usuario):
    usuario_bd = usuario_model.Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)

    # Chama o método para criar a senha criptografada
    usuario_bd.gen_senha()

    db.session.add(usuario_bd)
    db.session.commit()

    return usuario_bd


def listar_usuario(email):
    return usuario_model.Usuario.query.filter_by(email=email).first()

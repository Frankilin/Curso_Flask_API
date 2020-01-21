from passlib.hash import pbkdf2_sha256

from api import db


class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)

    def gen_senha(self):
        self.senha = pbkdf2_sha256.hash(self.senha)

    def compara_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)

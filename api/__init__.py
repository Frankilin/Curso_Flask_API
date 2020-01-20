from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

api = Api(app)

from .views import tarefas_views, projeto_views, funcionario_views
from .models import tarefa_model, projeto_model, funcionario_model

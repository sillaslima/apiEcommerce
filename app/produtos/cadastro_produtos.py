
from flask import Blueprint
from flask_restless import  APIManager
from app import db
from app import app

class Produto(db.Model):
    #fatores = ('A','B','C')
    #fatores_enum = Enum (*fatores, name='fator')
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(200))
    descricao = db.Column(db.String(400))
    imagem = db.Column(db.BLOB)
    valor = db.Column(db.Float(200))
    fator = db.Column(db.Enum('A','B','C', name='fator'))
db.drop_all()
db.create_all()

manager = APIManager(app,flask_sqlalchemy_db=db)

incluir_produto = manager.create_api_blueprint(Produto,methods=['GET','POST'],url_prefix='/v0',max_results_per_page=10,
                                               results_per_page=10)


from flask import Blueprint
from flask_restless import APIManager
from app import db


incluir_produto = Blueprint('inserir',__name__)
@incluir_produto.route('/produtos/inserir_produtos',methods=['GET','POST'])
def inserir_produtos():
    return 'inserir produtos'


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
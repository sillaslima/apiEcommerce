
from flask_restless import APIManager
from app import db
from app import app
from flask import Blueprint,json,request
import base64

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(200))
    descricao = db.Column(db.String(400))
    imagem = db.Column(db.BLOB)
    valor = db.Column(db.Float(200))
    fator = db.Column(db.Enum('A','B','C', name='fator'))


class Cliente(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(200))
    imagem=db.Column(db.LargeBinary(4000))

    def __init__ (self,id,nome,imagem):

        self.id=id
        self.nome=nome
        self.imagem=imagem


db.drop_all()
db.create_all()

manager = APIManager(app,flask_sqlalchemy_db=db)
incluir_produto = manager.create_api_blueprint(Produto,methods=['GET','POST'],url_prefix='/v0',max_results_per_page=10,
                                               results_per_page=10)

inc_produtos = Blueprint('produtos',__name__)
@inc_produtos.route('/produtos', methods=['POST'])
def incluir_produtos():
    if not request.json or not 'nome' in request.json:
        return 400
    print(request.json['id'])
    print(request.json['nome'])
    print(request.json['imagem'])
    imagem = request.json['imagem']
    img = base64.b64decode(imagem)

    print(img)
    cli = Cliente(id=request.json['id'],nome=request.json['nome'],imagem=img)
    db.session.add(cli)
    db.session.commit()
    #req=request.get_json(silent=True,force=True)

    #id_produto=req['id']
    #nome_produto=req['nome']
    #desc_produto=req['descricao']
    #imagem_produto=req['imagem']
    #imagem_produto.decode("utf-8")
    #valor_produto=req['valor']
    #fator_produto=req['fator']
    #print(id_produto,nome_produto,imagem_produto)
    #cli = Cliente(id='id_produto',nome="nome_produto",imagem="imagem_produto")


    #print(cli)


    #print(req['id'])
    #print(req['nome'])
    #print("Request:")
    #print(json.dumps(req,indent=4))
    return "testes"


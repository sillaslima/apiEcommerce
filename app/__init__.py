from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)



@app.route('/')
def index():
    return 'Raiz - api de produtos'

@app.errorhandler(404)
def not_found(error):
	return '404'

def registra_bluprint(app):
    from app.produtos.cadastro_produtos import incluir_produto
    app.register_blueprint(incluir_produto)
    from app.produtos.cadastro_produtos import inc_produtos
    app.register_blueprint(inc_produtos,url_prefix='/api')
registra_bluprint(app)



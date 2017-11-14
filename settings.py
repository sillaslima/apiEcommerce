import os
import pdb
#pdb.set_trace()
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media_files')
DEBUG = True
USE_RELOADER = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(PROJECT_ROOT,'produtos.db')
SQLALCHEMY_ECHO = True
PORT = 5555
HOST = "127.0.0.1"

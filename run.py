import sys
from app import app as application
print(application.config['HOST'])
print(application.config['PORT'])
print(application.config['DEBUG'])
print(application.config['SQLALCHEMY_DATABASE_URI'])

application.run(application.config['HOST'],
                application.config['PORT'],
                application.config['DEBUG'])

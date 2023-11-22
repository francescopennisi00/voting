import os


class BaseConfig:
    FLASK_APP = 'vote'
    FLASK_ENV = 'development'
    MYSQL_DATABASE_HOST = 'mysql'  # tanto per fare un esempio
    MYSQL_DATABASE_PORT = os.getenv('MYSQL_DATABASE_PORT', 3306) # tanto per fare un esempio

class ProdConfig(BaseConfig):
    pass

class DevConfig(BaseConfig):
    pass
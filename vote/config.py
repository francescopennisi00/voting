import os


class BaseConfig:
    FLASK_APP = 'vote'
    FLASK_ENV = 'development'
    MYSQL_DATABASE_HOST = 'mysql'
    MYSQL_DATABASE_PORT = os.getenv('MYSQL_DATABASE_PORT', 3306)

class ProdConfig(BaseConfig):
    pass

class DevConfig(BaseConfig):
    pass
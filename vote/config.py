import os


class BaseConfig:
    FLASK_APP = 'vote'
    FLASK_ENV = 'development'

    # tanto per fare un esempio (HP: la mia app verra' avviata in un Docker container collegato ad un
    # altro container di un server MySQL il cui nome sara' 'mysql')
    MYSQL_DATABASE_HOST = 'mysql'

    # tanto per fare un esempio: es. recupero la porta da una variabile di ambiente del mio Python virtual
    # enviroment (si può settare da CMD con set NOME_VARIABILE=VALUE, mentre in Linux si ha expose, non set)
    # in Windows Powershell per settare la env_variable del Python VirtualEnv si usa $env:NOME_VAR = "VALORE"
    # se non e' stata settata il valore dato alla variabile di configurazione e' 3306
    MYSQL_DATABASE_PORT = os.getenv("MYSQL_DATABASE_PORT", 3306)


class ProdConfig(BaseConfig):
    pass


class DevConfig(BaseConfig):
    pass

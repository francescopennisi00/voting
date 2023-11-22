from vote_app import create_app
from config import BaseConfig, ProdConfig
import os

env = os.environ.get("VOTE_ENV", 'dev')
#potremmo poi cambiare 'dev' in 'prod' nel caso in cui volessimo usare la configurazione di produzione
#da definire (insieme a quella di sviluppo) nel file config.py

config = BaseConfig

if env == 'prod':
    config = ProdConfig

app = create_app(config)

if __name__ == '__main__':
    foo = os.getenv('FOO','bar')
    print(foo)  #verra' stampato solo se faccio python app.py, non se faccio flask run
    app.run(host='0.0.0.0', debug=True,threaded=True)


#il comando activate può essere usato senza source (che non esiste su ambiente Windows)
#con il Activate su venv (cercare su stack overflow, activate flask without source)
#si trova su Scrpts (virtual env Python è diverso su Windows che su Linux)
#forse si attiva in automatico
#il feedback se e' attivo lo abbiamo da (venv) nella PowerShell